<!-- Converted from reference/method/ObjectId.createFromBase64.txt (reStructuredText). Includes are inlined. -->

# ObjectId.createFromBase64() (mongosh method)

## Definition

Creates an ObjectId from a base64 value.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**`ObjectId.createFromBase64( <base64String> [ , <subType> ]  )`**

### Method Fields

The method accepts the following fields:

* - Field
  - Type
  - Description

* - `base64String`
  - String
  - Specifies a 16 character base64 value. For example,
    `"SGVsbG8gV29ybGQh"`.

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

The following examples show how to add an object identifier to a
document using `ObjectId.createFromBase64()` and how the object
identifier appears in the output when retrieved.

### Create Collection Containing Document with Base64 Number

The following example creates a collection named
`objectIdentifierValuesFromBase64`:

```javascript
db.objectIdentifierValuesFromBase64.insertOne( {
   _id: 0,
   objectIdentifierValue: ObjectId.createFromBase64( "SGVsbG8gV29ybGQh" )
} )
```

The `objectIdentifierValue` field contains the object identifier
created from the base64 string specified in
`ObjectId.createFromBase64()`.

### Retrieve Document from Collection with Object Identifier

The following example retrieves the document:

```javascript
db.objectIdentifierValuesFromBase64.findOne( { _id: 0 } )
```

Example output:

```javascript
{
   _id: 0,
   objectIdentifierValue: ObjectId("48656c6c6f20576f726c6421")
}
```
