<!-- Converted from reference/method/ObjectId.createFromHexString.txt (reStructuredText). Includes are inlined. -->

# ObjectId.createFromHexString() (mongosh method)

## Definition

Creates an ObjectId from a hexadecimal value.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**`ObjectId.createFromHexString( <hexadecimalString> )`**

The `hexadecimalString` field specifies a string that contains a 24
character hexadecimal value. For example,
`"64c13ab08edf48a008793cac"`.

## Examples

The following examples show how to add an object identifier to a
document using `ObjectId.createFromHexString()` and how the object
identifier appears in the output when retrieved.

### Create Collection Containing Document with Object Identifier

The following example creates a collection named
`objectIdentifierValuesFromHex`:

```javascript
db.objectIdentifierValuesFromHex.insertOne( {
   _id: 0,
   objectIdentifierValue: ObjectId.createFromHexString( "64c13ab08edf48a008793cac" )
} )
```

The `objectIdentifierValue` field contains the object identifier
created from the hexadecimal string specified in
`ObjectId.createFromHexString()`.

### Retrieve Document from Collection with Object Identifier

The following example retrieves the document:

```javascript
db.objectIdentifierValuesFromHex.findOne( { _id: 0 } )
```

Example output:

```javascript
{
   _id: 0,
   objectIdentifierValue: ObjectId("64c13ab08edf48a008793cac")
}
```
