<!-- Converted from reference/method/KeyVault.deleteKey.txt (reStructuredText). Includes are inlined. -->

# KeyVault.deleteKey() (mongosh method)

**`KeyVault.deleteKey(UUID)`**

Deletes a data encryption key with the specified UUID from the key
vault associated to the database connection.

:returns: A document indicating the number of deleted keys.

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

`deleteKey()` has the following syntax:

```none
keyVault = db.getMongo().getKeyVault()

keyVault.deleteKey(UUID("<UUID String>"))
```

The UUID (Universally unique identifier) is a BSON 
`binary data` object with subtype `4`.

## Behavior

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

The following example is intended for rapid evaluation of
client-side field level encryption. For specific examples of using
`KeyVault.deleteKey()` with each supported
KMS (Key Management Service) provider, see
field-level-encryption-data-key-delete.

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

Retrieve the `KeyVault` object and
use the `KeyVault.deleteKey()` method to 
delete the data encryption key with matching `UUID`:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.deleteKey(UUID("b4b41b33-5c97-412e-a02b-743498346079"))
```

If successful, `deleteKey()` returns output similar to
the following:

```json
{ "acknowledged" : true, "deletedCount" : 1 }
```

**See also:**

field-level-encryption-data-key-delete
