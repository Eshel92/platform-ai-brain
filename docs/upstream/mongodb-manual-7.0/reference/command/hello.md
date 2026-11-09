<!-- Converted from reference/command/hello.txt (reStructuredText). Includes are inlined. -->

# hello (database command)

## Definition

**`hello`**

**New in version:** 5.0

`hello` returns a document that describes the role of
the `mongod` instance. If the optional field
`saslSupportedMechs` is specified, the command also returns an
`array of SASL mechanisms` used
to create the specified user's credentials.

If the instance is a member of a
replica set, then `hello` returns a subset of the
replica set configuration and status including whether or not the
instance is the primary of the replica set.

When sent to a `mongod` instance that is not a member of a
replica set, `hello` returns a subset of this
information.

MongoDB drivers and clients use
`hello` to determine the state of the replica set
members and to discover additional members of a replica
set.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     hello: 1 
   } 
)
```

The `hello` command accepts optional fields
`saslSupportedMechs: <db.user>` to return an additional field
`hello.saslSupportedMechs` in its result and `comment <any>` to
add a log comment associated with the command.

```javascript
db.runCommand( 
   { 
     hello: 1, 
     saslSupportedMechs: "<db.username>", 
     comment: <any> 
   } 
)
```

The `db.hello()` method in `mongosh`
provides a wrapper around `hello`.

## Behavior

### Client Disconnection

If the client that issued `hello` disconnects before the operation 
completes, MongoDB marks `hello` for termination using 
`killOp`.

## Output

### All Instances

The following `hello` fields are common across all
roles:

**`hello.isWritablePrimary`**

A boolean value that reports when this node is writable. If
`true`, then this instance is a primary in a
replica set, or a `mongos` instance, or a standalone
`mongod`.

This field will be `false` if the instance is a
secondary member of a replica set or if the member is an
arbiter of a replica set.

**`hello.topologyVersion`**

*For internal use by MongoDB.*

**`hello.maxBsonObjectSize`**

The maximum permitted size of a BSON object in bytes for
this `mongod` process. If not provided, clients should
assume a max size of "`16 * 1024 * 1024`".

**`hello.maxMessageSizeBytes`**

The maximum permitted size of a BSON wire protocol message.
The default value is `48000000` bytes.

**`hello.maxWriteBatchSize`**

The maximum number of write operations permitted in a write batch.
If a batch exceeds this
`limit`, the client
driver divides the batch into smaller groups each with counts less
than or equal to the value of this field.

The value of this limit is `100,000` writes.

**`hello.localTime`**

Returns the local server time in UTC. This value is an
ISO date.

**`hello.logicalSessionTimeoutMinutes`**

The time in minutes that a session remains active
after its most recent use. Sessions that have not received a new
read/write operation from the client or been refreshed with
`refreshSessions` within this threshold are cleared from the
cache. State associated with an expired session may be cleaned up by the
server at any time.

Only available when `featureCompatibilityVersion` is `"3.6"` or greater.

**`hello.connectionId`**

An identifier for the `mongod` / `mongos`
instance's outgoing connection to the client.

**`hello.minWireVersion`**

The earliest version of the wire protocol that this
`mongod` or `mongos` instance is capable of using
to communicate with clients.

Clients may use `minWireVersion` to help negotiate
compatibility with MongoDB.

**`hello.maxWireVersion`**

The latest version of the wire protocol that this `mongod`
or `mongos` instance is capable of using to communicate
with clients.

Clients may use `maxWireVersion` to help negotiate
compatibility with MongoDB.

**`hello.readOnly`**

A boolean value that, when `true`, indicates that the
`mongod` or `mongos` is running in read-only mode.

**`hello.compression`**

An array listing the compression algorithms used or available for
use (i.e. common to both the client and the `mongod` or
`mongos` instance) to compress the communication
between the client and the `mongod` or
`mongos` instance.

The field is only available if compression is used. For example:

- If the `mongod` is enabled to use both the
  `snappy,zlib` compressors and a client has specified `zlib`,
  the `compression` field would contain:

  ```javascript
  "compression": [ "zlib" ]
  ```

- If the `mongod` is enabled to use both the
  `snappy,zlib` compressors and a client has specified `zlib,snappy`,
  the `compression` field would contain:

  ```javascript
  "compression": [ "zlib", "snappy" ]
  ```

- If the `mongod` is enabled to use  the
  `snappy` compressor and a client has specified `zlib,snappy`,
  the `compression` field would contain :

  ```javascript
  "compression": [ "snappy" ]
  ```

- If the `mongod` is enabled to use  the `snappy`
  compressor and a client has specified `zlib` or the client has
  specified no compressor, the field is omitted.

That is, if the client does not specify compression or if the client
specifies a compressor not enabled for the connected
`mongod` or `mongos` instance, the field
does not return.

**`hello.saslSupportedMechs`**

An array of SASL mechanisms used to create the user's credential or
credentials.  Supported SASL mechanisms are:

- `GSSAPI`
- `SCRAM-SHA-256`
- `SCRAM-SHA-1`

The field is returned only when the command is run with the
`saslSupportedMechs` field:

```javascript
db.runCommand( { hello: 1, saslSupportedMechs: "<db.username>" } )
```

### Sharded Instances

`mongos` instances add the following field to the
`hello` response document:

**`hello.msg`**

Contains the value `isdbgrid` when `hello`
returns from a `mongos` instance.

### Replica Sets

`hello` contains these fields when returned by a member
of a replica set:

**`hello.hosts`**

An array of strings in the format of `"[hostname]:[port]"` that
lists all members of the replica set that are neither
hidden, passive,
nor arbiters.

Drivers use this array and the `hello.passives` to determine
which members to read from.

**`hello.setName`**

The name of the current :replica set.

**`hello.setVersion`**

The current replica set config version.

**`hello.secondary`**

A boolean value that, when `true`, indicates if the
`mongod` is a secondary member of a replica
set.

**`hello.passives`**

An array of strings in the format of `"[hostname]:[port]"`
listing all members of the replica set which have a
`members[n].priority` of `0`.

This field only appears if there is at least one member with a
`members[n].priority` of `0`.

Drivers use this array and the `hello.hosts` to determine
which members to read from.

**`hello.arbiters`**

An array of strings  in the format of `"[hostname]:[port]"`
listing all members of the replica set that are
arbiters.

This field only appears if there is at least one arbiter in the
replica set.

**`hello.primary`**

A string in the format of `"[hostname]:[port]"` listing the
current primary member of the replica set.

**`hello.arbiterOnly`**

A boolean value that , when `true`, indicates that the current
instance is an arbiter.  The `arbiterOnly`
field is only present, if the instance is an arbiter.

**`hello.passive`**

A boolean value that, when `true`, indicates that the current
instance is passive.  The
`passive` field is only present for members with a
`members[n].priority` of `0`.

**`hello.hidden`**

A boolean value that, when `true`, indicates that the current
instance is hidden.  The
`hidden` field is only present for hidden members.

**`hello.tags`**

A `tags` document contains user-defined tag field and value pairs for
the replica set member.

```javascript
{ "<tag1>": "<string1>", "<tag2>": "<string2>",... }
```

- For read operations, you can specify a tag set in the read
  preference to direct the
  operations to replica set member(s) with the specified tag(s).

- For write operations, you can create a customize write concern using
  `settings.getLastErrorModes` and
  `settings.getLastErrorDefaults`.

For more information, see
replica-set-configuration-tag-sets.

**See also:**

`members[n].tags`

**`hello.me`**

The `[hostname]:[port]` of the member that returned
`hello`.

**`hello.electionId`**

A unique identifier for each election. Included only in the output
of `hello` for the primary. Used by clients
to determine when elections occur.

**`hello.lastWrite`**

A document containing optime and date information for the
database's most recent write operation.

**`hello.lastWrite.opTime`**

An object giving the optime of the last write operation.

**`hello.lastWrite.lastWriteDate`**

A date object containing the
time of the last write operation.

**`hello.lastWrite.majorityOpTime`**

An object giving the optime of the last write operation
readable by `majority` reads.

**`hello.lastWrite.majorityWriteDate`**

A date object containing the
time of the last write operation readable by
`majority` reads.

For details on the `ok` status field, the `operationTime` field,
and the `$clusterTime` field, see
Command Response.
