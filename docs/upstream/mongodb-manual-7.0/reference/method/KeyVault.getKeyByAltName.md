<!-- Converted from reference/method/KeyVault.getKeyByAltName.txt (reStructuredText). Includes are inlined. -->

# KeyVault.getKeyByAltName() (mongosh method)

**`KeyVault.getKeyByAltName(keyAltName)`**

Gets all data encryption keys with the specified `keyAltName`. 

:returns:

  Document representing a matching data encryption key.

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

`getKeyByAltName()` has the following syntax:

```none
keyVault = db.getMongo().getKeyVault()

keyVault.getKeyByAltName("keyAltName")
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

The following example uses a locally managed KMS for the client-side
field level encryption configuration. 

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
`KeyVault.getKeyByAltName()` method to retrieve the data
encryption key whose `keyAltNames` array includes the specified key
alternate name:

```javascript
keyVault.getKeyByAltName("data-encryption-key")
```

`getKeyByAltName()` returns the following data
encryption key:

```json
{
    "_id" : UUID("b4b41b33-5c97-412e-a02b-743498346079"),
    "keyMaterial" : BinData(0,"PXRsLOAYxhzTS/mFQAI8486da7BwZgqA91UI7NKz/T/AjB0uJZxTvhvmQQsKbCJYsWVS/cp5Rqy/FUX2zZwxJOJmI3rosPhzV0OI5y1cuXhAlLWlj03CnTcOSRzE/YIrsCjMB0/NyiZ7MRWUYzLAEQnE30d947XCiiHIb8a0kt2SD0so8vZvSuP2n0Vtz4NYqnzF0CkhZSWFa2e2yA=="),
    "creationDate" : ISODate("2019-08-12T21:21:30.569Z"),
    "updateDate" : ISODate("2019-08-12T21:21:30.569Z"),
    "status" : 0,
    "version" : Long(0),
    "masterKey" : {
        "provider" : "local"
    },
    "keyAltNames" : [
        "data-encryption-key"
    ]
}
```
