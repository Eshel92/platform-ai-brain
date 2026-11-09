<!-- Converted from reference/method/Binary.createFromBase64.txt (reStructuredText). Includes are inlined. -->

# Binary.createFromBase64() (mongosh method)

## Definition

Creates a binary object from a base64 value.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**`Binary.createFromBase64( <base64String> [ , <subType> ] )`**

### Method Fields

The method accepts the following fields:

* - Field
  - Type
  - Description

* - `base64String`
  - String
  - Specifies a string that contains a base64 value. For example,
    `"SGVsbG8gV29ybGQhCg=="`.

* - `subType`
  - Integer
  - Optional. Specifies a binary subtype.

    - `0`: Generic binary subtype

    - `1`: Function

    - `2`: Byte array (deprecated)

    - `3`: Old UUID (deprecated)

    - `4`: UUID

    - `5`: MD5

    - `128` through `255`: User defined

## Examples

The following examples show how to add a binary object to a document
using `Binary.createFromBase64()` and how the binary object appears in
the output when retrieved.

### Create Collection Containing Document with Binary Object

The following example creates a collection named
`binaryObjectsFromBase64`:

```javascript
db.binaryObjectsFromBase64.insertOne( {
   _id: 0,
   binaryObject: Binary.createFromBase64( "SGVsbG8gV29ybGQhCg==" )
} )
```

The `binaryObject` field contains the binary object created from the
string specified in `Binary.createFromBase64()`.

### Retrieve Document from Collection with Binary Object

The following example retrieves the document:

```javascript
db.binaryObjectsFromBase64.findOne( { _id: 0 } )
```

**Note:**

Starting in `mongosh` 2.0.0, binary objects are shown
as `Binary.createFromBase64( <base64String> )` values instead of
`Binary( Buffer.from( <base64String> ) )` values. This only changes
the display of binary values.

Example output, starting in `mongosh` 2.0.0:

```javascript
{
   _id: 0,
   binaryObject: Binary.createFromBase64("SGVsbG8gV29ybGQhCg==")
}
```
