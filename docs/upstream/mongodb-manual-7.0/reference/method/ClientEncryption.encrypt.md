<!-- Converted from reference/method/ClientEncryption.encrypt.txt (reStructuredText). Includes are inlined. -->

# ClientEncryption.encrypt() (mongosh method)

**`ClientEncryption.encrypt(keyId, value, algorithm or encOptions)`**

`ClientEncryption.encrypt` encrypts the `value` using the
specified `keyId` and the algorithm specified by `algorithm` or 
`encOptions`. `encrypt` supports explicit 
(manual) encryption of field values.

:returns:

  A `binary data`  object with
  [subtype 6](https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/subtype6.rst).

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

```javascript
clientEncryption = db.getMongo().getClientEncryption()

clientEncryption.encrypt(
  keyId,
  value,
  algorithm or encOptions,
)
```

* - Parameter
  - Type
  - Description

* - `keyId`
  - `UUID`
  - The data encryption key to use for encrypting the `value`.

    The UUID (Universally unique identifier) is a BSON
    `binary data` object with subtype `4`
    that identifies a specific data encryption key. If the data
    encryption key does not exist in the key vault configured for
    the database connection, `encrypt()`
    returns an error. See field-level-encryption-keyvault
    for more information on key vaults and data encryption keys.

* - `value`
  - See encrypt-bson-types.
  - The value to encrypt.

* - `algorithm` or `encOptions`
  - string or document
  -
    - To explicitly encrypt fields with Client-Side Field Level
      Encryption:

      Specify the `algorithm` as a string or `encOptions` as a 
      document containing the field `algorithm`.

      The supported algorithms are:

      - `AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`
      - `AEAD_AES_256_CBC_HMAC_SHA_512-Random`

      For examples, see Set the Client-Side Field Level 
      Encryption Algorithm.

      For complete documentation on the supported encryption
      algorithms, see field-level-encryption-algorithms.

    - To explicitly encrypt fields with Queryable Encryption:

      Specify the `algorithm` as a string or `encOptions` as a 
      document containing the fields:

      - `algorithm`: The encryption algorithm to use for 
        encrypting the `value`. The supported algorithms are:

        - `Indexed`
        - `Unindexed`

      - `contentionFactor`: Required when `algorithm` is set
        to `Indexed`. Related to the frequency of the values for 
        this field.

      - `queryType`: The only query type currently supported is
        `"equality"`. `queryType` must be set when algorithm is 
        not `Indexed`.

      For examples, see Set the Queryable Encryption Algorithm.

      For details on the supported encryption algorithms, see
      qe-fundamentals-man-enc-algorithm-choice.

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

### Unsupported BSON Types

You cannot use `encrypt()` 
to encrypt values with the following BSON types:

- `minKey`
- `maxKey`
- `null`
- `undefined`

If encrypting a field using
`AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`,
`encrypt()` does *not* support the following
BSON types:

- `double`
- `decimal128`
- `bool`
- `object`
- `array`

## Examples

### Client-Side Field Level Encryption

The following example uses a locally managed KMS for the client-side
field level encryption configuration.

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

**Step 2: Encrypt Your Data**

Retrieve the `ClientEncryption` object
and use the `ClientEncryption.encrypt()` method to encrypt
a value using a specific data encryption key `UUID` and 
encryption algorithm:

```javascript
clientEncryption = encryptedClient.getClientEncryption();

clientEncryption.encrypt(
  UUID("64e2d87d-f168-493c-bbdf-a394535a2cb9"), 
  "123-45-6789", 
  "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
)
```

You can also specify the algorithm using a document with an
`algorithm` field:

```javascript
clientEncryption = encryptedClient.getClientEncryption();

clientEncryption.encrypt(
  UUID("64e2d87d-f168-493c-bbdf-a394535a2cb9"), 
  "123-45-6789", 
  { algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Random" }
)
```

#### Example Results

If successful, `encrypt` returns the encrypted 
value:

```javascript
BinData(6,"AmTi2H3xaEk8u9+jlFNaLLkC3Q/+kmwDbbWrq+h9nuv9W+u7A5a0UnpULBNZH+Q21fAztPpU09wpKPrju9dKfpN1Afpj1/ZhFcH6LYZOWSBBOAuUNjPLxMNSYOOuITuuYWo=")
```

For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see `Mongo()`.

### Queryable Encryption

The following example uses a locally managed KMS for the 
Queryable Encryption configuration.

**Step 1: Create Your Encrypted Connection**

a. Start mongosh

   Start the `mongosh` client.

   ```bash
   mongosh --nodb
   ```

#. Generate Your Key

   To configure Queryable Encryption for a locally managed key, 
   generate a base64-encoded 96-byte string with no line breaks.

   ```javascript
   const TEST_LOCAL_KEY = require("crypto").randomBytes(96).toString("base64")
   ```

#. Create the Queryable Encryption Options

   Create the Queryable Encryption options using the generated local key string:

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

#. Create Your Encrypted Client

   Use the `Mongo()` constructor with the queryable 
   encryption options configured to create a database connection. Replace 
   the `mongodb://myMongo.example.net` URI with the connection 
   string URI of the target cluster.

   ```javascript
   encryptedClient = Mongo( 
      "mongodb://myMongo.example.net:27017/?replSetName=myMongo", 
      autoEncryptionOpts
   )
   ```

**Step 2: Encrypt Your Data**

Retrieve the `ClientEncryption` object
and use the `ClientEncryption.encrypt()` method to encrypt
a value using a specific data encryption key `UUID` and 
encryption algorithm:

```javascript
const eDB = "encrypted"
const eKV = "__keyVault"

const clientEncryption = encryptedClient.getClientEncryption();
const keyVaultClient = Mongo().getDB(eDB).getCollection(eKV)

const dek = keyVaultClient.findOne({ keyAltNames: "dataKey1" })

clientEncryption.encrypt(
  dek._id,
  "123-45-6789", 
  "Unindexed"
)
```

You can also specify the algorithm using a document containing the
fields:

- `algorithm`
- `queryType`
- `contentionFactor`

```javascript
const eDB = "encrypted"
const eKV = "__keyVault"

const clientEncryption = encryptedClient.getClientEncryption();
const keyVaultClient = Mongo().getDB(eDB).getCollection(eKV)

const dek = keyVaultClient.findOne({ keyAltNames: "dataKey1" })

clientEncryption.encrypt(
  dek._id,
  "123-45-6789", 
  { 
    algorithm: "Indexed", 
    queryType: "equality", 
    contentionFactor: 4
  }
)
```

#### Example Results

If successful, `encrypt` returns the encrypted 
value:

```javascript
Binary(Buffer.from("05b100000005640020000000005ab3581a43e39a8e855b1ac87013e841735c09d19ae86535eea718dd56122ba50573002000000000703d2cba9832d90436c6c92eb232aa5b968cdcd7a3138570bc87ef0a9eb3a0e905630020000000009cb61df010b1bb54670a5ad979f25f4c48889059dfd8920782cf03dd27d1a50b05650020000000003f5acea703ea357d3eea4c6a5b19139a580089341424a247839fd4d5cf0d312a12636d00040000000000000000", "hex"), 6)
```

## Learn More

For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see `Mongo()`.
