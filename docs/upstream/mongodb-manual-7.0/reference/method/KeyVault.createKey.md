<!-- Converted from reference/method/KeyVault.createKey.txt (reStructuredText). Includes are inlined. -->

# KeyVault.createKey() (mongosh method)

**`KeyVault.createKey(keyManagementService, customerMasterKey, ["keyAltName"])`**

Adds a data encryption key to the key vault associated to the
database connection. Client-Side Field Level Encryption uses data encryption keys for supporting
encryption and decryption of field values.

:returns:

  The `UUID` unique identifier of the created data encryption
  key.

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

`createKey()` has the following syntax:

```javascript
keyVault = db.getMongo().getKeyVault()

keyVault.createKey(
  keyManagementService,
  customerMasterKey,
  [ "keyAltName" ]
)
```

* - Parameter

  - Type

  - Description

* - `keyManagementService`

  - string

  - *Required* 

    The Key Management Service (KMS) to use for retrieving the
    Customer Master Key (CMK). Accepts the following parameters:

    - `aws` for Amazon Web Services KMS. Requires specifying a
      Customer Master Key (CMK) string for `customerMasterKey`.

    - `azure` for Azure Key Vault. Requires
      specifying a Customer Master Key (CMK) document for
      `customerMasterKey`.

      **New in version:** 5.0

    - `gcp` for Google Cloud Platform KMS. Requires specifying a
      Customer Master Key (CMK) document for
      `customerMasterKey`.

      **New in version:** 5.0

    - `local` for a locally managed key.

    If the `database connection` was not 
    configured with the specified KMS, data encryption key
    creation fails.

* - `customerMasterKey`

  - string or document

  - The Customer Master Key (CMK) to use for encrypting the data
    encryption key. Required if `keyManagementService` is
    `aws`, `azure`, or `gcp`.

    Provide the CMK as follows depending on your KMS provider:

    - For the Amazon Web Services KMS, specify the full
      [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
      of the master key as a single string.

    - For the Azure Key Vault KMS, specify a
      document containing the following key value pairs:

      - `keyName` - The [Azure Key Vault Name](https://docs.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates#vault-name-and-object-name)
      - `keyVaultEndpoint` - The DNS name of the Azure Key Vault
        to use
      - `keyVersion` - Optional. The version of the key
        specified in `keyName`, if applicable

      **New in version:** 5.0

    - For the Google Cloud Platform KMS, specify a
      document containing the following key value pairs:

      - `projectId` - The GCP project name
      - `location` - The location of the KMS keyring
      - `keyRing` - The name of the KMS keyring (often 'global')
      - `keyName` - The name of the key to use
      - `keyVersion` - Optional. The version of the key
        specified in `keyName`, if applicable

      **New in version:** 5.0

    `createKey()` requests
    that the KMS encrypt the data encryption key material
    using the specified CMK. If the CMK does not exist *or* if the
    autoEncryptionOpts configuration
    does not have sufficient privileges to use the CMK,
    `createKey()` returns an error.

    This parameter has no effect if `keyManagementService` is `local` 
    and can be safely omitted. 

* - `keyAltName`
  - array of strings
  - *Optional*

    The alternative name for the data encryption key. Use
    `keyAltName` to improve findability of a specific data
    encryption key, or as an analog to a comment. 

    The `getKeyVault()` method automatically creates a
    unique index  on the
    `keyAltNames` field with a partial index filter for only documents where
    `keyAltNames` exists.

* - `options`
  - document
  - *Optional*

    A document that specifies options for the new key.
    `options` has the following fields:

    - `masterKey`: the new master key to encrypt data.
    - `keyAltNames`: an array of alternate names, one per 
      master key.
    - `keyMaterial`: bindata used to create the key.

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
`KeyVault.createKey()` with each supported
KMS (Key Management Service) provider, see
Create a Data Key.

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

Retrieve the `keyVault` object and
use the `KeyVault.createKey()` method to 
create a new data encryption key using the locally managed key:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.createKey("local", ["data-encryption-key"])
```

If successful, `createKey()` returns the `UUID` of
the new data encryption key. To retrieve the new data encryption
key document from the key vault, either:

- Use `getKey()` to retrieve the created key by
  `UUID`.

  *-or-*

- Use `getKeyByAltName()` to retrieve the key by its 
  alternate name.
