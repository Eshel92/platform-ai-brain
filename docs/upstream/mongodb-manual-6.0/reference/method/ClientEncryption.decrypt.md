<!-- Converted from reference/method/ClientEncryption.decrypt.txt (reStructuredText). Includes are inlined. -->

# ClientEncryption.decrypt()

**`ClientEncryption.decrypt(encryptedValue)`**

`ClientEncryption.decrypt` decrypts the `encryptionValue` *if*
the current database connection was configured with access to the Key
Management Service (KMS) and key vault used to encrypt `encryptionValue`.

:returns: The decrypted value.

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

`decrypt` has the following syntax:

```bash
clientEncryption = db.getMongo().getClientEncryption()

clientEncryption.decrypt(encryptedValue)
```

The `encryptedValue` *must* be a `binary data` object 
with [subtype 6](https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/subtype6.rst)
created using client-side field level encryption.

## Behavior

Read operations issued from a database connection `configured`
with access to the correct Key Management Service (KMS) and Key Vault can
automatically decrypt field values encrypted using
`ClientEncryption.encrypt()`. Clients only need to use
`decrypt()` to decrypt `Binary` subtype 6 
values not stored within a document field.

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

Retrieve the `ClientEncryption` object
and use the `ClientEncryption.decrypt()` method to decrypt
a value encrypted by `ClientEncryption.encrypt()`.

```javascript
clientEncryption = encryptedClient.getClientEncryption();

clientEncryption.decrypt(BinData(6,"AmTi2H3xaEk8u9+jlFNaLLkC3Q/+kmwDbbWrq+h9nuv9W+u7A5a0UnpULBNZH+Q21fAztPpU09wpKPrju9dKfpN1Afpj1/ZhFcH6LYZOWSBBOAuUNjPLxMNSYOOuITuuYWo="))
```

If successful, `decrypt()` returns the
decrypted value:

```javascript
"123-45-6789" 
```

For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see `Mongo()`.
