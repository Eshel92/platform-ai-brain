<!-- Converted from core/queryable-encryption/fundamentals/encrypt-and-query.txt (reStructuredText). Includes are inlined. -->

# Field Encryption and Queryability

## Overview

Learn about the following Queryable Encryption topics:

- Considerations when enabling queries on an encrypted field.
- How to specify fields for encryption.
- How to configure an encrypted field so that it is queryable.
- Query types and which ones you can use on encrypted fields.
- How to optimize query performance on encrypted fields.

## Considerations when Enabling Querying

When you use Queryable Encryption, you can choose whether to make an encrypted field queryable.
If you don't need to perform CRUD operations that require you
to query an encrypted field, you may not need to enable querying on that field.
You can still retrieve the entire document by querying other fields that are queryable or not encrypted.

When you make encrypted fields queryable, Queryable Encryption creates an index for each encrypted field, which
can make write operations on that field take longer. When a write operation updates
an indexed field, MongoDB also updates the related index.

When you create an encrypted collection, MongoDB creates 
two metadata collections, increasing 
the storage space requirements.

## Specify Fields for Encryption

With Queryable Encryption, you specify which fields you want to automatically
encrypt in your MongoDB document using a JSON encryption schema. The
encryption schema defines which fields are encrypted and which queries
are available for those fields.

**Important:**

You can specify any field for encryption except the
`_id` field.

To specify fields for encryption and querying, create an encryption schema that includes the following properties:

* - Key Name
  - Type
  - Required

* - `path`
  - String
  - Required

* - `bsonType`
  - String
  - Required

* - `keyId`
  - Binary
  - Required. Specify a key value for each field. 

    **Note:**

    If you call `createEncryptedCollection()` 
    and set `keyId: null`, the MongoDB driver automatically creates a 
    data key. `createEncryptedCollection` then returns a new 
    encryption schemaa with the new `keyId` values.

* - `queries`
  - Object
  - Optional. Include to make the field queryable.

### Example

This example shows how to create the encryption schema.

Consider the following document that contains personally identifiable 
information (PII), credit card information, and sensitive medical information:

```json
{
   "firstName": "Jon",
   "lastName": "Snow",
   "patientId": 12345187,
   "address": "123 Cherry Ave",
   "medications": [
      "Adderall",
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

To ensure the PII and sensitive medical information stays secure, create
the encryption schema and configure those fields for automatic 
encryption. You must generate a unique key for each encrypted field in advance. 
For example:

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
      }
   ]
}
```

Configure `AutoEncryptionSettings` on the client, then use the 
`createEncryptedCollection()` helper method to create 
your collections.

## Configure Fields for Querying

Include the `queries` property on fields to make them queryable. This
enables an authorized client to issue read and write queries against
those fields. Omitting the `queries` property prevents clients from querying a 
field.

### Example

Add the `queries` property to the previous example schema to make the
`patientId` and `patientInfo.ssn` fields queryable.

```javascript
const encryptedFieldsObject = {
   fields: [
      {
         path: "patientId",
         bsonType: "int",
         queries: { queryType: "equality" }
      },
      {
         path: "patientInfo.ssn",
         bsonType: "string",
         queries: { queryType: "equality" }
      },
      {
         path: "medications",
         bsonType: "array"
      },
      {
         path: "patientInfo.billing",
         bsonType: "object"
      },
   ]
}
```

## Contention

Concurrent write operations, such as inserting the same field/value pair into
multiple documents in close succession, can cause contention: conflicts that
delay operations.

With Queryable Encryption, MongoDB tracks the occurrences of each field/value pair in an
encrypted collection using an internal counter. The contention factor
partitions this counter, similar to an array. This minimizes issues with
incrementing the counter when using `insert`, `update`, or `findAndModify` to add or modify an encrypted field
with the same field/value pair in close succession. `contention = 0`
creates an array with one element at index 0. `contention = 4` creates an
array with 5 elements at indexes 0-4. MongoDB increments a random array element
during insert.

When unset, `contention` defaults to `8`, which provides high performance
for most workloads. Higher contention improves the performance of insert and
update operations on low cardinality fields, but decreases find performance.

### Adjusting the Contention Factor

You can optionally include the `contention` property on queryable fields to
change the contention factor from its default value of `8`. Before you modify 
the contention factor, consider the following points:

Consider increasing `contention` above the default value of `8` only if the
field has frequent concurrent write operations. Since high contention values
sacrifice find performance in favor of insert and update operations, the
benefit of a high contention factor for a rarely updated field is unlikely to
outweigh the drawback.

Consider decreasing `contention` if a field is often queried, but
rarely written. In this case, find performance is preferable to write and 
update performance.

You can calculate contention factor for a field by using a formula where:

- `ω` is the number of concurrent write operations on the field in a short
  time, such as 30ms. If unknown, you can use the server's number of virtual 
  cores.
- `valinserts` is the number of unique field/value pairs inserted since last
  performing metadata compaction.
- `ω``∗` is `ω/valinserts` rounded up to the nearest integer. For a
  workload of 100 operations with 1000 recent values, `100/1000 = 0.1`,
  which rounds up to `1`.

A reasonable contention factor, `cf`, is the result of the following 
formula, rounded up to the nearest positive integer:

`(ω``∗` `· (ω``∗` `− 1)) / 0.2`

For example, if there are 100 concurrent write operations on a field in 30ms,
then `ω = 100`. If there are 50 recent unique values for that field, then
`ω``∗` `= 100/50 = 2`. This results in `cf = (2·1)/0.2 = 10`.

**Warning:**

Don't set the contention factor on properties of the data itself, such as
the frequency of field/value pairs (cardinality). Only set the contention factor based on your workload.

Consider a case
where `ω = 100` and `valinserts = 1000`, resulting in `ω``∗` ``=
100/1000 = 0.1 ≈ 1` and `cf = (1·0)/0.2 = 0 ≈ 1``. 20 of
the values appear very frequently, so you set `contention = 3` instead. An
attacker with access to multiple database snapshots can infer that the high
setting indicates frequent field/value pairs. In this case, leaving
`contention` unset so that it defaults to `8` would prevent the attacker
from having that information.

For thorough information on contention and its cryptographic implications, see
"Section 9: Guidelines" in MongoDB's [Queryable Encryption Technical Paper](https://www.mongodb.com/collateral/queryable-encryption-technical-paper)

### Query Types

Passing a query type to the `queries` option in your encrypted fields
object sets the allowed query types for the field. Querying non-encrypted fields or encrypted fields with a supported query
type returns encrypted data that is then decrypted at
the client.

Queryable Encryption currently supports `none` and `equality` query types. If the
query type is unspecified, it defaults to `none`. If the query type is
`none`, the field is  encrypted, but clients can't query it.

The `equality` query type supports the following expressions:

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

Queries that compare an encrypted field to `null` or to a regular expression result in an error, even with supported query operators.

Queryable Encryption `equality` queries don't support read or write operations
on a field when the operation compares the encrypted field to any of the
following BSON types:

- `double`
- `decimal128`
- `object`
- `array`

## Client and Server Schemas

MongoDB supports using
schema validation
to enforce encryption of specific fields
in a collection. Clients using automatic Queryable Encryption have
specific behavior depending on the database connection
configuration:

- If the connection 
  `encryptedFieldsMap` object contains a key for the specified collection, the 
  client uses that object to perform automatic Queryable Encryption, 
  rather than using the remote schema. At a minimum, the local rules **must** 
  encrypt those fields that the remote schema marks as requiring 
  encryption.

- If the connection
  `encryptedFieldsMap` object does *not* contain a key for the specified 
  collection, the client downloads the server-side remote schema for 
  the collection and uses it to perform automatic Queryable Encryption.

  **Important:** Behavior Considerations

  When a client does not have an encryption schema for the
  specified collection, the following occurs:

  - The client trusts that the server has a valid schema with respect
    to automatic Queryable Encryption.

  - The client uses the remote schema to perform automatic
    Queryable Encryption only. The client does not enforce any other
    validation rules specified in the schema.

To learn more about automatic Queryable Encryption, see the following resources:

- Queryable Encryption Introduction
- qe-quick-start

## Enable Queryable Encryption

Enable Queryable Encryption before creating a collection. Enabling Queryable Encryption after
creating a collection does not encrypt fields on documents already in
that collection. You can enable Queryable Encryption on fields in one of two ways:

- Pass the encryption schema, represented by the
  `encryptedFieldsObject` 
  constant, to the client that the application uses to create the collection:

```javascript
const client = new MongoClient(uri, {
   autoEncryption: {
      keyVaultNameSpace: "<your keyvault namespace>",
      kmsProviders: "<your kms provider>",
      extraOptions: {
         cryptSharedLibPath: "<path to Automatic Encryption Shared Library>"
      },
      encryptedFieldsMap: {
         "<databaseName.collectionName>": { encryptedFieldsObject }
      }
   }

   ...

   await client.db("<database name>").createCollection("<collection name>");
}
```

For more information on `autoEncryption` configuration options, see the
section on qe-reference-mongo-client.

- Pass the encrypted fields object to `createCollection()` to create a new collection:

```javascript
await encryptedDB.createCollection("<collection name>", {
   encryptedFields: encryptedFieldsObject
});
```

**Tip:**

Specify the encrypted fields when you create the collection, and also
when you create a client to access the collection. This ensures that
if the server's security is compromised, the information is still 
encrypted through the client.

**Important:**

Explicitly create your collection, rather than creating it implicitly
with an insert operation. When you create a collection using
`createCollection()`, MongoDB creates an index on the encrypted
fields. Without this index, queries on encrypted fields may run slowly.
