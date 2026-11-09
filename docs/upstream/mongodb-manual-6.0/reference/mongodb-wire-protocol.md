<!-- Converted from reference/mongodb-wire-protocol.txt (reStructuredText). Includes are inlined. -->

# MongoDB Wire Protocol

**Note:**

This MongoDB Wire Protocol Specification is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). You may
not use or adapt this material for any commercial purpose, such as
to create a commercial database or database-as-a-service offering.

## Introduction

The MongoDB Wire Protocol is a simple socket-based, request-response
style protocol. Clients communicate with the database server through a
regular TCP/IP socket.

## TCP/IP Socket

Clients should connect to the database with a regular TCP/IP socket.

### Port

The default port number for `mongod` and `mongos`
instances is 27017. The port number for `mongod` and
`mongos` is configurable and may vary.

### Byte Ordering

All integers in the MongoDB wire protocol use little-endian byte order:
that is, least-significant byte first.

## Messages Types and Formats

MongoDB uses the OP_MSG opcode for both client
requests and database replies. There are several message formats used in
older versions of MongoDB which have been deprecated in favor of
`OP_MSG`.

**Note:**

This page uses a C-like `struct` to describe the message
structure.

The types used in this document, such as `int32` and `cstring`,
are the same as those defined in the [BSON specification](http://bsonspec.org/#/specification).

## Standard Message Header

In general, each message consists of a standard message header followed
by request-specific data. The standard message header is structured as
follows:

```c
struct MsgHeader {
    int32   messageLength; // total message size, including this
    int32   requestID;     // identifier for this message
    int32   responseTo;    // requestID from the original request
                           //   (used in responses from the database)
    int32   opCode;        // message type
}
```

| Field | Description |
|---|---|
| `messageLength` | The total size of the message in bytes. This total includes the 4 bytes that holds the message length. |
| `requestID` | A client or database-generated identifier that uniquely identifies the message. |
| `responseTo` | The `requestID` taken from the messages from the client. |
| `opCode` | Type of message. See wp-request-opcodes for details. |

## Opcodes

MongoDB uses these `opCode` values:

| Opcode Name | Value | Comment |
|---|---|---|
| `OP_COMPRESSED` | 2012 | Wraps other opcodes using compression |
| `OP_MSG` | 2013 | Send a message using the standard format. Used for both client requests and database replies. |
| \| `OP_REPLY` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 1 | Reply to a client request. `responseTo` is set. |
| \| `OP_UPDATE` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 2001 | Update document. |
| \| `OP_INSERT` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 2002 | Insert new document. |
| `RESERVED` | 2003 | Formerly used for OP_GET_BY_OID. |
| \| `OP_QUERY` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 2004 | Query a collection. |
| \| `OP_GET_MORE` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 2005 | Get more data from a query. See Cursors. |
| \| `OP_DELETE` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 2006 | Delete documents. |
| \| `OP_KILL_CURSORS` \| *Deprecated in MongoDB 5.0. Removed in MongoDB 5.1.* | 2007 | Notify database that the client has finished with the cursor. |

### `OP_COMPRESSED`

Any opcode can be compressed and wrapped in an `OP_COMPRESSED` header.
The `OP_COMPRESSED` message contains the original compressed opcode
message alongside the metadata necessary to process and decompress it.

The format of the `OP_COMPRESSED` message is:

```bash
struct {
    MsgHeader header;            // standard message header
    int32  originalOpcode;       // value of wrapped opcode
    int32  uncompressedSize;     // size of deflated compressedMessage, excluding MsgHeader
    uint8  compressorId;         // ID of compressor that compressed message
    char    *compressedMessage;  // opcode itself, excluding MsgHeader
}
```

| Field | Description |
|---|---|
| `MsgHeader` | Message header, as described in wp-message-header. |
| `originalOpcode` | Contains the value of the wrapped opcode. |
| `uncompressedSize` | The size of the deflated `compressedMessage`, which excludes the `MsgHeader`. |
| `compressorId` | The ID of the compressor that compressed the message. A list of `compressorId` values is provided below. |
| `compressedMessage` | The opcode itself, excluding the `MsgHeader`. |

Each compressor is assigned a predefined compressor ID as follows:

| compressorId | Handshake Value | Description |
|---|---|---|
| `0` | noop | The content of the message is uncompressed. This is used for testing. |
| `1` | snappy | The content of the message is compressed using snappy. |
| `2` | zlib | The content of the message is compressed using zlib. |
| `3` | zstd | The content of the message is compressed using zstd. |
| `4-255` | reserved | Reserved for future use. |

### `OP_MSG`

`OP_MSG` is an extensible message format used to encode both client
requests and server replies on the wire.

`OP_MSG` has the following format:

```none
OP_MSG {
    MsgHeader header;           // standard message header
    uint32 flagBits;            // message flags
    Sections[] sections;        // data sections
    optional<uint32> checksum;  // optional CRC-32C checksum
}
```

| Field | Description |
|---|---|
| `header` | Standard message header, as described in wp-message-header. |
| `flagBits` | An integer bitmask containing message flags, as described in wire-msg-flags. |
| `sections` | Message body sections, as described in wire-msg-sections. |
| `checksum` | An optional CRC-32C checksum, as described in wire-msg-checksum. |

#### Flag Bits

The `flagBits` integer is a bitmask encoding flags that modify the
format and behavior of `OP_MSG`.

The first 16 bits (0-15) are *required* and parsers **MUST**
error if an unknown bit is set.

The last 16 bits (16-31) are *optional*, and parsers **MUST**
ignore any unknown set bits. Proxies and other message forwarders
**MUST** clear any unknown optional bits before forwarding messages.

| Bit | Name | Request | Response | Description |
|---|---|---|---|---|
| 0 | `checksumPresent` | ✓ | ✓ | The message ends with 4 bytes containing a CRC-32C [#f1]_ checksum. See wire-msg-checksum for details. |
| 1 | `moreToCome` | ✓ | ✓ | Another message will follow this one without further action from the receiver. The receiver **MUST NOT** send another message until receiving one with `moreToCome` set to 0 as sends may block, causing deadlock. Requests with the `moreToCome` bit set will not receive a reply. Replies will only have this set in response to requests with the `exhaustAllowed` bit set. |
| 16 | `exhaustAllowed` | ✓ |  | The client is prepared for multiple replies to this request using the `moreToCome` bit. The server will never produce replies with the `moreToCome` bit set unless the request has this bit set. This ensures that multiple replies are only sent when the network layer of the requester is prepared for them. |

#### Sections

An `OP_MSG` message contains one or more sections. Each section starts
with a `kind` byte indicating its type. Everything after the `kind`
byte constitutes the section's payload.

The available kinds of sections follow.

#### Kind 0: Body

A body section is encoded as a **single** BSON object.
The size in the BSON object also serves as the size of the section. This
section kind is the standard command request and reply body.

All top-level fields **MUST** have a unique name.

#### Kind 1: Document Sequence

* - Type
  - Description

* - int32
  - Size of the section in bytes.

* - C String
  - Document sequence identifier. In all current commands this field
    is the (possibly nested) field that it is replacing from the body
    section.

    This field **MUST NOT** also exist in the body section.

* - Zero or more BSON objects
  - - Objects are sequenced back to back with no separators.

    - Each object is limited to the `maxBSONObjectSize` of the
      server. The combination of all objects is not limited to
      `maxBSONObjSize`.

    - The document sequence ends once `size` bytes have been consumed.

    - Parsers **MAY** choose to merge these objects into the body as
      an array at the path specified by the sequence identifier when
      converting to language-level objects.

#### Kind 2

This section is used for internal purposes.

#### Checksum

Each message **MAY** end with a CRC-32C [#f1]_ checksum that covers all
bytes in the message except for the checksum itself.

If you do not use TLS/SSL connections, `mongod` instances and 
`mongos` instances exchange messages with checksums.

If you use TLS/SSL connections, `mongod` instances and 
`mongos` instances skip the checksum.
   
Drivers and older binaries will ignore the checksum if presented with
messages with checksum.

The presence of a checksum is indicated by the `checksumPresent` flag
bit.

### Legacy Opcodes

Starting in MongoDB 5.1, these opcodes are removed in favor of
OP_MSG:

- `OP_DELETE`
- `OP_GET_MORE`
- `OP_INSERT`
- `OP_KILL_CURSORS`
- `OP_QUERY` [#op-query-footnote]_
- `OP_REPLY`
- `OP_UPDATE`

If you are running an older version of MongoDB and need detailed
information on the previous opcodes, see wire-legacy-opcodes.

**Footnotes**
