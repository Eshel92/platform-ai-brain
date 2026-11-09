<!-- Converted from core/queryable-encryption/fundamentals/encrypt-and-query.txt (reStructuredText). Includes are inlined. -->

# Field Encryption and Queryability

## Overview

In this guide, you can learn about the following Queryable Encryption topics:

- How to specify fields for encryption.
- How to specify whether an encrypted field is queryable when you create a collection.
- Query types and which ones you can use on encrypted fields.
- What to consider when deciding whether to enable queries on an encrypted field.

## Specify Fields for Encryption

Queryable Encryption allows you to specify which fields you want to automatically
encrypt in your MongoDB document.

**Important:**

You can specify any field in your document for encryption except the
`_id` field.

To specify fields for encryption and querying, define a JSON
schema that includes the following properties:

| Key Name | Type | Required? |
|---|---|---|
| `path` | String | Required |
| `bsonType` | String | Required |
| `keyId` | Binary | Required |
| `queries` | Object | Optional, omit unless you want to be able to query the field. |

### Example

This example shows how to create a JSON schema that specifies which fields that
the Queryable Encryption feature should automatically encrypt.

Consider the following document that contains personally identifiable information
(PII), credit card information, and sensitive medical information:

```json
{
   "firstName": "Jon",
   "lastName": "Snow",
   "patientId": 12345187,
   "address": "123 Cherry Ave",
   "medications": [
      "Adderal",
      "Lipitor"
   ],
   "patientInfo": {
      "ssn": "921-12-1234",
      "billing": {
            "type": "visa",
            "number": "1234-1234-1234-1234"
      }
   }
}
```

To ensure the PII and sensitive medical information stays secure, create a JSON
schema that configures Queryable Encryption to automatically encrypt those fields.
The following sample JSON schema shows how you can specify which fields to encrypt:

```javascript
const encryptedFieldsObject = {
   fields: [
      {
         path: "patientId",
         keyId: "<unique data encryption key>",
         bsonType: "int"
      },
      {
         path: "patientInfo.ssn",
         keyId: "<unique data encryption key>",
         bsonType: "string"
      },
      {
         path: "medications",
         keyId: "<unique data encryption key>",
         bsonType: "array"
      },
      {
         path: "patientInfo.billing",
         keyId: "<unique data encryption key>",
         bsonType: "object"
      },
   ]
}
```

Note that the `keyId` field requires a unique Data Encryption Key (DEK) which Queryable Encryption
uses to encrypt the fields. For more information on DEKs, see
qe-fundamentals-manage-keys.

## Specify Queryable Encrypted Fields

Include the `queries` property on fields you want to make queryable in your JSON
schema. This enables an authorized client to issue read and write queries using
encrypted fields. You can omit the `queries` property unless you want to be able
to query the field.

### Example

The following code snippet shows how to add the `queries` property to the
JSON schema to make the `patientId` and `patientInfo.ssn`
fields queryable..

```javascript
const encryptedFieldsObject = {
   fields: [
      {
         path: "patientId",
         keyId: "<unique data encryption key>",
         bsonType: "int",
         queries: { queryType: "equality" }
      },
      {
         path: "patientInfo.ssn",
         keyId: "<unique data encryption key>",
         bsonType: "string",
         queries: { queryType: "equality" }
      },
      {
         path: "medications",
         keyId: "<unique data encryption key>",
         bsonType: "array"
      },
      {
         path: "patientInfo.billing",
         keyId: "<unique data encryption key>",
         bsonType: "object"
      },
   ]
}
```

For more information on query types, see qe-query-types.

## Enable Queryable Encryption

You can enable Queryable Encryption on fields you specify in a JSON schema in the following ways:

- Pass the JSON schema, represented by the `encryptedFieldsObject` constant,
  to the client that the application uses to create the collection as shown in the
  following code snippet:

```javascript
const client = new MongoClient(uri, {
   autoEncryption: {
      keyVaultNameSpace: "<your keyvault namespace>",
      kmsProviders: "<your kms provider>",
      extraOptions: {
         cryptSharedLibPath: "<path to FLE Shared Library>"
      },
      encryptedFieldsMap: {
         "<databaseName.collectionName>": { encryptedFieldsObject }
      }
   }

   ...

   await client.db("<database name>").createCollection("<collection name>");
}
```

**Note:**

It's important to enable Queryable Encryption before creating the collection. Enabling
Queryable Encryption after creating the collection does not encrypt fields on documents
already in that collection.

For more information on `autoEncryption` configuration options, see the
section on qe-reference-mongo-client.

- Pass the encrypted fields object to your call to create a new collection as
  shown in the following code snippet:

```javascript
await encryptedDB.createCollection("<collection name>", {
   encryptedFields: encryptedFieldsObject
});
```

**Tip:**

For the highest level of security, specify the encrypted fields both when
creating the collection, and when creating a client to access the collection.
This ensures that if the server's security is compromised, the information
is still encrypted through the client.

**Important:**

MongoDB recommends explicitly creating your collection when using Queryable Encryption, rather
than implicitly creating the collection through an insert operation. When you
create a collection using `createCollection()`, the operation creates an index
on the encrypted fields. Without an index, querying on encrypted fields could
run slowly.

## Query Types

Queryable Encryption allows you to specify on which fields you want to enable querying by passing
a query type to the `queries` option in your encrypted fields object.

Queryable Encryption currently supports `none` or `equality` query types.
The new cryptography framework introduced as part of Queryable Encryption 
in MongoDB 6.0 is designed to accommodate additional 
expressive encrypted searches, such as range and string operators. 

A query type of `none` indicates that the data will be encrypted but 
is not intended to be queryable. Queries cannot be run on encrypted 
data with a query type of `none`. Encrypted data will be returned 
if queries are run on:

- non-encrypted fields 
- fields with a query type of `equality` in the same collection 
  and decrypted at the client.

**Important:** None Specified Query Types

If query type is not explicitly specified, the query type will
default to `none` and the data will not be queryable.

The `equality` query type allows you to query encrypted fields 
using the following expressions:

- $eq
- $ne
- $in
- $nin
- $and
- $or
- $not
- $nor
- $expr

**Note:**

Queries that compare an encrypted field to `null` or to a regular expression will
result in an error, even when using a supported query operator.

Queryable Encryption using the `equality` query type doesn't support read or write operations
on a field when the operation compares the encrypted field to any of the following
BSON types:

- `double`
- `decimal128`
- `object`
- `array`
- `javascriptWithScope` (Deprecated)

## Considerations when Enabling Querying

When you use Queryable Encryption, you can choose whether to make an encrypted field queryable.
If you don't need to perform read operations, or write operations that require you
to read an encrypted field, you may decide not to enable querying on that field.
You can still retrieve the entire document by querying other fields that are queryable or not encrypted.

When you make encrypted fields queryable, Queryable Encryption creates an index for each encrypted field, which
can make write operations on that field take longer. When a write operation updates
an indexed field, MongoDB also updates the related index.

When you enable querying on an encrypted field, your collection requires more storage space.
These collection names, which begin with `enxcol_.`, contain important encryption metadata.

**Warning:**

Do not modify collections beginning with `enxcol_.`.
