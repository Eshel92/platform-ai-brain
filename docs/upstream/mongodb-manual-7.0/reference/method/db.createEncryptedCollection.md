<!-- Converted from reference/method/db.createEncryptedCollection.txt (reStructuredText). Includes are inlined. -->

# db.createEncryptedCollection() (mongosh method)

**New in version:** 7.0

**`db.createEncryptedCollection(collName, options)`**

`db.createEncryptedCollection()` creates an encrypted collection
specified by `collName` on the current database.

This method is a wrapper around
`ClientEncryption.createEncryptedCollection()` that
automatically creates data keys if `encryptedFields.fields[*].keyId`
is `null` or omitted in the
`options.createCollectionOptions.encryptedFields` definition.

## Compatibility

This command is available in deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`db.createEncryptedCollection()` has the following syntax:

```javascript
db.createEncryptedCollection(
   collName,
   {
      provider: kmsProviderName,
      createCollectionOptions: encryptedFieldsMap,
      masterKey: customerMasterKeyCredentials
   }
)
```

## Command Fields

`db.createEncryptedCollection()` takes these fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `collName` | string | Required | Name of the collection to encrypt on the current database. |
| `options` | document | Required | Options to configure the encrypted collection. |
| `options.provider` | string | Required | KMS you are using to store your Customer Master Key. |
| `options.createCollectionOptions` | document | Required | Fields to encrypt. Must contain an `encryptedFields` document. See qe-specify-fields-for-encryption for details on how to configure the `encryptedFields` document. |
| `options.masterKey` | document | Optional | Specifies the credentials and key identification fields needed to access the master key when the KMS Provider is AWS, GCP, or Azure. Optional when the KMS Provider is `local`. |

## Behavior

The `mongosh` client-side field level and queryable 
encryption methods require a database connection configured for 
client-side encryption. If the current database connection was not 
initiated with client-side field level encryption enabled, either:

- Use the `Mongo()` constructor from the `mongosh`
  to establish a connection with the required client-side field
  level encryption options. The `Mongo()` method supports the
  following Key Management Service (KMS) providers for Customer
  Master Key (CMK) management:

  - Amazon Web Services KMS
  - Azure Key Vault
  - Google Cloud Platform KMS
  - Locally Managed Key

*or*

- Use the `mongosh` command line options to establish a
  connection with the required options. The command line options only
  support the Amazon Web Services KMS provider for CMK management. 

### Wrapper Behavior

The `db.createEncryptedCollection()` method runs in the context
of the current `db` and uses the same Queryable Encryption-enabled
connection as the current `mongosh` session. Internally, it calls
`ClientEncryption.createEncryptedCollection()` with the current
database name, the specified collection name, and the provided options
document.

When `options.createCollectionOptions.encryptedFields.fields[*].keyId`
is `null` or omitted, the method automatically creates the required
data keys in the key vault and populates the corresponding `keyId`
values in the created collection's `encryptedFields` definition.

## Example

The following example uses a locally managed KMS for the
Queryable Encryption configuration.

**Step 1: Create Your Encrypted Connection**

a. Start mongosh

   Run:

   ```bash
   mongosh --nodb
   ```

   `--nodb` means don't connect to a database.

#. Generate a Key String

   Generate a base 64 96-byte string:

   ```javascript
   const TEST_LOCAL_KEY = require("crypto").randomBytes(96).toString("base64")
   ```

#. Create an Encryption Options Object

   To create a client-side field level encryption options object, use
   the `TEST_LOCAL_KEY` string from the previous step:

   ```javascript
      var autoEncryptionOpts = {
         "keyVaultNamespace" : "encryption.__dataKeys",
         "kmsProviders" : {
            "local" : {
               "key" : BinData(0, TEST_LOCAL_KEY)
            }
         }
      }
   ```

#. Create an Encrypted Client Object

   To create an encrypted client object, use the `Mongo()`
   constructor. Replace the `mongodb://myMongo.example.net` URI with
   the connection string URI for the target
   cluster. For example:

   ```javascript
   encryptedClient = Mongo( 
      "mongodb://myMongo.example.net:27017/?replSetName=myMongo", 
      autoEncryptionOpts
   )
   ```

**Step 2: Specify which Fields to Encrypt**

Create an `encryptedFieldsMap` to specify which fields to encrypt:

```javascript
const encryptedFieldsMap = {
  encryptedFields: {
    fields: [
      {
        path: "secretField",
        bsonType: "string",
        queries: { queryType: "equality" },
        // keyId omitted; db.createEncryptedCollection() generates it
      },
    ],
  },
};
```

**Step 3: Create Your Encrypted Collection**

Create an encrypted `enc.users` collection using the helper on
the current database:

```javascript
const encDb = encryptedClient.getDB("enc");

let result = encDb.createEncryptedCollection(
  "users",
  {
    provider: "local",
    createCollectionOptions: encryptedFieldsMap,
    masterKey: {} // masterKey is optional when provider is local
  }
);
```

**Step 4: Check Your Result Object**

`db.createEncryptedCollection()` returns a result object that
includes the created collection name and the collection's
`encryptedFields` definition.

Check the value of `result.collection` to confirm the collection
was created in the desired location, and optionally inspect the
populated `encryptedFields`:

```javascript
enc> result.collection
enc.users

enc> result.encryptedFields
{
  fields: [
    {
      path: "secretField",
      bsonType: "string",
      queries: { queryType: "equality", /* ... */ },
      keyId: UUID("...")
    }
  ]
}
```

## Learn More

- For complete documentation on initiating MongoDB connections with
  client-side field level encryption enabled, see `Mongo()`.

- For a complete example of how to create and query an encrypted
  collection, see qe-quick-start.
