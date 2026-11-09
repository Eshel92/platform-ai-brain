<!-- Converted from reference/method/getClientEncryption.txt (reStructuredText). Includes are inlined. -->

# getClientEncryption()

**`getClientEncryption()`**

Returns the `ClientEncryption` object for the current database
collection. The `ClientEncryption` object supports explicit
(manual) encryption and decryption of field values for
Client-Side field level encryption.

:returns:

  The `ClientEncryption` object for current database connection.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`getClientEncryption()` has the following syntax:

```javascript
db.getMongo().getClientEncryption();
```

Use the `ClientEncryption` object to access the following 
explicit encryption methods:

- `encrypt()` 
- `decrypt()`

## Behavior

### Enable Client-Side Field Level Encryption on Database Connection

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

The `getKeyVault()` method automatically creates a
unique index  on the `keyAltNames` field
with a partial index filter for only
documents where `keyAltNames` exists. `getKeyVault()`
creates this index in the key vault collection. This prevents any two
data encryption keys in the same key vault from having the same key
alternative name and therefore avoids ambiguity around which data
encryption key is appropriate for encryption/decryption.

**Warning:**

Do not drop the unique index created by `getKeyVault()`.
Client-Side Field Level Encryption operations depend on
server-enforced uniqueness of `keyAltNames`. Removing the index
may lead to unexpected or unpredictable behavior.

The following example uses a locally managed KMS for the client-side
field level encryption configuration.

To configure client-side field level encryption for a locally managed
key:

- generate a base64-encoded 96-byte string with no line breaks
- use `mongosh` to load the key

```bash
export TEST_LOCAL_KEY=$(echo "$(head -c 96 /dev/urandom | base64 | tr -d '\n')")

mongosh --nodb
```

Create the client-side field level encryption object using the
generated local key string:

```javascript
 var autoEncryptionOpts = {
   "keyVaultNamespace" : "encryption.__dataKeys",
   "kmsProviders" : {
     "local" : {
       "key" : BinData(0, process.env["TEST_LOCAL_KEY"])
     }
   }
 }
```

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

Use the `getClientEncryption()` method to
retrieve the client encryption object:

```javascript
clientEncryption = encryptedClient.getClientEncryption()
```

For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see `Mongo()`.
