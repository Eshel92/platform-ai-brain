<!-- Converted from reference/method/KeyVault.addKeyAlternateName.txt (reStructuredText). Includes are inlined. -->

# KeyVault.addKeyAlternateName()

**`KeyVault.addKeyAlternateName(UUID, keyAltName)`**

Adds the `keyAltName` to the `keyAltNames` array of the data
encryption key with `UUID`.

`keyAltName` *must* be unique among all keys in the key vault. The
`getKeyVault()` method automatically creates a 
unique index  on the `keyAltNames` field 
with a partial index filter for only 
documents where `keyAltNames` exists.

:returns:

  Returns the previous version of the data encryption key document.

  Returns `null` if no data encryption key has the specified
  `UUID()`.

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

`addKeyAlternateName()` has the following syntax:

```none
keyVault = db.getMongo().getKeyVault()

keyVault.addKeyAlternateName(
   UUID("<UUID string>"),
   "keyAlternateName"
)
```

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
`KeyVault.addKeyAlternateName()` with each supported
KMS (Key Management Service) provider, see
field-level-encryption-data-key-manage.

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

Retrieve the `KeyVault` object and use the
`KeyVault.addKeyAlternateName()` method to add a new key
alternate name to the data encryption key with matching `UUID`. The
specified key alternate name *must* be unique:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.addKeyAlternateName(UUID("b4b41b33-5c97-412e-a02b-743498346079"),"Other-Data-Encryption-Key")
```

If successful, `addKeyAlternateName()` returns the
previous version of data encryption key document:

```json
{
    "_id" : UUID("b4b41b33-5c97-412e-a02b-743498346079"),
    "keyMaterial" : BinData(0,"PXRsLOAYxhzTS/mFQAI8486da7BwZgqA91UI7NKz/T/AjB0uJZxTvhvmQQsKbCJYsWVS/cp5Rqy/FUX2zZwxJOJmI3rosPhzV0OI5y1cuXhAlLWlj03CnTcOSRzE/YIrsCjMB0/NyiZ7MRWUYzLAEQnE30d947XCiiHIb8a0kt2SD0so8vZvSuP2n0Vtz4NYqnzF0CkhZSWFa2e2yA=="),
    "creationDate" : ISODate("2019-08-12T21:21:30.569Z"),
    "updateDate" : ISODate("2019-08-12T21:21:30.569Z"),
    "status" : 0,
    "version" : NumberLong(0),
    "masterKey" : {
        "provider" : "local"
    },
    "keyAltNames" : [
    ]
}
```

To view the current version of the data encryption key document, use
`KeyVault.getKey()` specifying the `_id` of the returned
document *or* `KeyVault.getKeyByAltName()` specifying one of the
`keyAltNames`.

**See also:**

field-level-encryption-data-key-manage
