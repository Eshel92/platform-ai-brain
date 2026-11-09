<!-- Converted from reference/method/KeyVault.rewrapManyDataKey.txt (reStructuredText). Includes are inlined. -->

# KeyVault.rewrapManyDataKey() (mongosh method)

**`KeyVault.rewrapManyDataKey(filter, options)`**

Decrypts multiple Data Encryption Keys (DEK) 
and re-encrypts them with a new Customer Master Key (CMK).
Use this method to rotate the CMK that encrypts your
DEKs. To learn more about CMKs
and DEKs, see csfle-key-architecture.

You specify a CMK through the `masterKey` parameter.
If you do not include a `masterKey` argument, the method decrypts
and encrypts each DEK with the CMK
referenced in that DEK's metadata. To learn more about
the metadata of DEKs, see
csfle-reference-decryption-metadata.

:returns:

  A BulkWriteResult object
  that reports how many data keys were affected.

**Warning:** Back-Up Your Key Vault collection

Before you rotate your Data Encryption Keys, ensure you create
a backup of your Key Vault collection. If you lose access to your
Data Encryption Keys, you will lose all your encrypted data.

To learn how to create a backup of a collection,
see manual-tutorial-backup-and-restore.

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

   
`KeyVault.rewrapManyDataKey` has the following syntax:

```javascript
let keyVault = db.getMongo().getKeyVault()

keyVault.rewrapManyDataKey(
  <filter>,
  <options>
)
```

* - Parameter

  - Type

  - Description

* - `filter`

  - query filter document 

  - The query filter for the keyvault collection

* - `options`

  - document

  - 
    This document has two fields:

    - `provider`: A KMS provider (AWS KMS, Azure Key Vault, 
      GCP KMS, the local provider, or KMIP)
    - `masterKey`: A KMS-specific key used to encrypt the new 
      data key

**Important:** Key Rotation Support

To view your driver's dependencies for the key rotation API, see
Compatibility.

## Behavior

This operation is not atomic and should not be run in parallel with 
other key management operations.

### Requires Configuring Client-Side Field Level Encryption on Database Connection

The `mongosh` client-side field level encryption methods
require a database connection with client-side field level encryption
enabled. If the current database connection was not initiated with
client-side field level encryption enabled, either:

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

## Example

These examples allow you to rapidly evaluate client-side field level 
encryption. For specific examples using each supported 
KMS (Key Management Service) provider, see
field-level-encryption-data-key-manage.

**Step 1: Start mongosh**

Start the `mongosh` client.

```bash
mongosh --nodb
```

**Step 2: Generate Your Key**

To configure client-side field level encryption for a locally 
managed key, generate a base64-encoded 96-byte string with no line 
breaks.

```javascript
const TEST_LOCAL_KEY = require("crypto").randomBytes(96).toString("base64")
```

**Step 3: Create the Client-Side Field Level Encryption Options**

Create the client-side field level encryption options using the
generated local key string:

```javascript
 let autoEncryptionOpts = {
   "keyVaultNamespace" : "encryption.__dataKeys",
   "kmsProviders" : {
     "local" : {
       "key" : BinData(0, TEST_LOCAL_KEY)
     }
   }
 }
```

**Step 4: Create Your Encrypted Client**

Use the `Mongo()` constructor with the client-side field level 
encryption options configured to create a database connection. Replace 
the `mongodb://myMongo.example.net` URI with the connection 
string URI of the target cluster.

```javascript
encryptedClient = Mongo( 
  "mongodb://myMongo.example.net:27017/?replSetName=myMongo", 
   autoEncryptionOpts
)
```

Retrieve the `KeyVault` object and use the
`KeyVault.rewrapManyDataKey` method to rewrap the existing
keys in a new `masterKey`. If no new `masterKey` is given, each
data key retains its respective current `masterKey`. 

### Rewrap Data Keys with the Current masterKey

The following example shows how you can rewrap each data key with its 
respective current `masterKey`:

```javascript
let keyVault = mongo.getKeyVault()

keyVault.rewrapManyDataKey()
```

### Rewrap Data Keys with a New masterKey

The following example shows how you can rewrap each data key with a new `masterKey`:

```javascript
let keyVault = mongo.getKeyVault()

keyVault.rewrapManyDataKey({}, {
  provider: 'aws',
  masterKey: {
    region: 'us-east-2',
    key: 'arn:aws:kms:us-east-2:...'
  }
})
```

### Rewrap Data Keys That Have Not Been Rewrapped Recently

The following example shows how to rewrap data keys that have not
been rewrapped in the previous thirty days.

```javascript
let keyVault = mongo.getKeyVault()

const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

keyVault.rewrapManyDataKey({ updateDate: { $lt: thirtyDaysAgo } });
```

### Output

`KeyVault.rewrapManyDataKey()` returns a `BulkWriteResult`
object detailing how many data keys were affected:

```json
{
  bulkWriteResult: BulkWriteResult {
    result: {
      ok: 1,
      writeErrors: [],
      writeConcernErrors: [],
      insertedIds: [],
      nInserted: 0,
      nUpserted: 0,
      nMatched: 3,
      nModified: 3,
      nRemoved: 0,
      upserted: [],
      opTime: { ts: Timestamp({ t: 1655840760, i: 3 }), t: 23 }
    }
  }
}
```
