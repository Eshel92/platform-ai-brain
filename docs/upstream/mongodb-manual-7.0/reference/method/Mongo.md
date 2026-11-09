<!-- Converted from reference/method/Mongo.txt (reStructuredText). Includes are inlined. -->

# Mongo() (mongosh method)

## Description

**`Mongo(host, autoEncryptionOpts, api)`**

JavaScript constructor to instantiate a database connection from
`mongosh` or from a JavaScript file.

The `Mongo()` method has the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `host` | string | *Optional*. The host, either in the form of `<host>` or `<host><:port>`. If omitted, `Mongo` instantiates a connection to the localhost interface on the default port `27017`. |
| `autoEncryptionOpts` | document | *Optional*. Configuration parameters for enabling security-in-use-encryption. `autoEncryptionOpts` overrides the existing in-use encryption configuration of the database connection. If omitted, `Mongo()` inherits the in-use encryption configuration of the current database connection. See autoEncryptionOpts for usage and syntax details. |
| `api` | document | *Optional*. Configuration options for enabling the Stable API. See mongo-api-options for usage and syntax details. |

**See also:**

`Mongo.getDB()` and `db.getMongo()`

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## `AutoEncryptionOpts`

The `autoEncryptionOpts` document specifies
configuration options for security-in-use-encryption.
If your database connection has an existing in-use encryption configuration,
`autoEncryptionOpts` overrides that configuration. MongoDB provides two approaches
to In-Use Encryption: manual-csfle-feature and qe-manual-feature-qe. 

For example, starting `mongosh`
with client-side field level encryption command-line options enables
client-side encryption for that connection. New database connections
created using `Mongo()` inherit the encryption settings *unless*
`Mongo()` includes `autoEncryptionOpts`.

The `autoEncryptionOpts` document has the following
syntax: 

```none
{
  "keyVaultClient" : <object>,
  "keyVaultNamespace" : "<string>",
  "kmsProviders" : <object>,
  "schemaMap" : <object>,
  "bypassAutoEncryption" : <boolean>,
  "tlsOptions": <object>,
  "encryptedFieldsMap": <object>
}
```

The `autoEncryptionOpts` document takes the
following parameters:

* - Parameter

  - Type

  - Description

* - `keyVaultClient`

  - `Mongo()` connection object.

  - *(Optional)* The MongoDB cluster hosting the key vault
    collection.

    Specify a `Mongo()` connection object pointing to the
    cluster:

    ```javascript
    var keyVaultClient = Mongo(<MongoDB URI>);

    var autoEncryptionOptions = {
      "keyVaultClient" : keyVaultClient,
      "keyVaultNamespace" : "<database>.<collection>",
      "kmsProviders" : { ... }
    }
    ```

    If `keyVaultClient` is omitted, the `host` specified to the
    `Mongo()` object containing the
    `autoEncryptionOpts` document is used as the
    key vault host.

* - `keyVaultNamespace`

  - string

  - *(Required)* The full namespace of the key vault
    collection.

* - `kmsProviders`

  - document

  - *(Required)*  The Key Management Service (KMS) used by client-side field level
    encryption for managing a Customer Master Key (CMK). Client-side
    field level encryption uses the CMK for encrypting and decrypting
    data encryption keys.

    Client-Side Field Level Encryption supports the following KMS
    providers:

    - Amazon Web Services KMS
    - Azure Key Vault
    - Google Cloud Platform KMS
    - Locally Managed Key

    If possible, consider defining the credentials provided in
    `kmsProviders` as environment variables, and then passing them
    to `mongosh` using the `--eval` option. This minimizes the chances of credentials
    leaking into logs. See
    Create a Data Key for examples of
    this approach for each supported KMS.

    Amazon Web Services KMS

      IMPORTANT: For AWS KMS support, use `mongosh`,
      or the MongoDB 4.2.2 or later legacy `mongo` shell. The 4.2.0 and
      4.2.1 legacy `mongo` shell do not support the AWS KMS service due
      to an unexpected change in the KMS response object. See
      SERVER-44721 for more information.

      Specify the `aws` document to `kmsProviders` with the
      following fields:

      ```json
      "kmsProviders" : {
         "aws" : {
           "accessKeyId" : "AWSAccessKeyId",
           "secretAccessKey" : "AWSSecretAccessKey"
         }
       }
      ```

      The specified `accessKeyId` must correspond to an IAM user
      with all `List` and `Read` permissions for the KMS service.

    Azure Key Vault
      Specify the `azure` document to `kmsProviders` with  the
      following fields:

      ```json
      "kmsProviders" : {
        "azure" : {
          "tenantId" : "AzureTenantId",
          "clientId" : "AzureClientId",
          "clientSecret" : "AzureClientSecret"
        }
      }
      ```

      **New in version:** 5.0

    Google Cloud KMS
      Specify the `gcp` document to `kmsProviders` with  the
      following fields:

      ```json
      "kmsProviders" : {
        "gcp" : {
          "email" : "GCPEmail",
          "privateKey" : "GCPPrivateKey"
        }
      }
      ```

      **New in version:** 5.0

    Locally Managed Key
      Specify the `local` document to `kmsProviders` with  the
      following field:

      ```json
      "kmsProviders" : {
        "local" : {
           "key" : BinData(0, "<96 byte base-64 encoded key>")
        }
      }
      ```

      The specified `key` *must* be a base64-encoded
      96-byte string with no newline characters.

* - `schemaMap`

  - document

  - *(Optional)* The automatic client-side field level encryption
    rules specified using the JSON schema Draft 4 standard syntax and
    encryption-specific keywords. This option is mutually exclusive
    with `explicitEncryptionOnly`. If a collection is present on both the
    `schemaMap` and the `encryptedFieldsMap`, `libmongocrypt` errors on initialization.

    For complete documentation, see
    csfle-fundamentals-create-schema.

* - `bypassAutoEncryption`

  - boolean

  - *(Optional)* Specify `true` to bypass automatic client-side field
    level encryption rules and perform explicit (manual) per-field
    encryption.

* - `bypassQueryAnalysis`

  - boolean

  - *(Optional)* Specify `true` to use explicit encryption on
    indexed fields without the `crypt_shared` library. For details,
    see qe-reference-mongo-client.

* - `explicitEncryptionOnly`
  - boolean 
  - *(Optional)* Specify `true` to use neither automatic encryption
    nor automatic decryption. You can use `getKeyVault()` and
    `getClientEncryption()` to perform explicit
    encryption. This option is mutually exclusive with `schemaMap`.
    If omitted, defaults to `false`.

* - `tlsOptions`
  - object 
  - *(Optional)* The path to the TLS client certificate and private key file in PEM format
    (`tlsCertificateKeyFile`), TLS client certificate and private key file password
    (`tlsCertificateKeyFilePassword`), or TLS certificate authority file
    (`tlsCAFile`) to use to connect to the KMS in PEM format. To learn more 
    about these options, see 
    [TLS Options](https://www.mongodb.com/docs/mongodb-shell/reference/options/#tls-options). 

* - `encryptedFieldsMap`

  - document

  - *(Optional)* The map of collection namespaces to `encryptedFields` documents.
    `encryptedFields` is a BSON document that describes the Queryable Encryption encrypted
    fields. If a collection is present on both the
    `schemaMap` and the `encryptedFieldsMap`, `libmongocrypt` errors on
    initialization.

    To learn more about encrypted fields in Queryable Encryption, see 
    Specify Fields for Encryption.

## `api`

The `api` parameter specifies configuration options for the 
Stable API. You can enable or disable optional
behavior using the following options:

* - Option
  - Type
  - Description

* - `version`
  - string
  - Specifies the API Version. `"1"` is
    currently the only supported version.

* - `strict`
  - boolean 
  - If `true`:
       - Using a command that is not part of the declared API 
         version returns an APIStrictError 
         error.

       - Indexes that are unsupported 
         by the Stable API are ignored by the 
         query planner.

    If you specify `strict`, you must also specify `version`.  

    If not specified, defaults to `false`. 

* - `deprecationErrors`
  - boolean
  - If `true`, using a command or behavior that is deprecated 
    in the specified API version returns an 
    APIDeprecationError. If you specify
    `deprecationErrors`, you must also specify `version`.

    If not specified, defaults to `false`. 
  

The `api` parameter has the following syntax:

```javascript
{ api: { version: <string>, strict: <boolean>, deprecationErrors: <boolean> } }
```

## Examples

### Connect to a MongoDB Cluster

The following operation creates a new connection object from within a
`mongosh` session:

```javascript
cluster = Mongo("mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster")
```

Issue operations against the `cluster` object to interact with the
`mymongo.example.net:27017` cluster:

```javascript
myDB = cluster.getDB("myDB"); //returns the database object
myColl = myDB.getCollection("myColl"); // returns the collection object
```

### Connect to a Cluster with Client-Side Encryption Enabled

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

Issue operations against the `cluster` object to interact with the
`mymongo.example.net:27017` cluster and perform explicit encryption:

```javascript
// returns the database object
myDB = cluster.getDB("myDB");

// returns the collection object
myColl = myDB.getCollection("myColl");

// returns object for managing data encryption keys
keyVault = cluster.getKeyVault();

// returns object for explicit encryption/decryption
clientEncryption = cluster.getClientEncryption();
```

See in-use-encryption-methods for
a complete list of client-side field level encryption methods.

### Connect to a Cluster with Automatic Client-Side Encryption Enabled

To configure client-side field level encryption for a locally managed
key:

- generate a base64-encoded 96-byte string with no line breaks
- use `mongosh` to load the key

```bash
export TEST_LOCAL_KEY=$(echo "$(head -c 96 /dev/urandom | base64 | tr -d '\n')")

mongosh --nodb
```

The following operation creates a new connection object from within a
`mongosh` session. The
autoEncryptionOpts option specifies
the required options for enabling automatic client-side encryption on the `hr.employees` collection:

```javascript
var autoEncryptionOpts = {
  "keyVaultNamespace" : "encryption.__dataKeys",
  "kmsProviders" : {
    "local" : {
      "key" : BinData(0, process.env["TEST_LOCAL_KEY"])
    }
  },
  schemaMap : {
    "hr.employees" : {
      "bsonType": "object",
      "properties" : {
        "taxid" : {
          "encrypt" : {
            "keyId" : [UUID("bffb361b-30d3-42c0-b7a4-d24a272b72e3")],
            "bsonType" : "string",
            "algorithm" : "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
          }
        },
        "taxid-short": {
          "encrypt": {
            "keyId": [UUID("33408ee9-e499-43f9-89fe-5f8533870617")],
            "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
            "bsonType": "string"
          }
        }
      }
    }
  }
}

cluster = Mongo(
  "mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster",
  autoEncryptionOpts
)
```

Issue operations against the `cluster` object to interact with the
`mymongo.example.net:27017` cluster and utilize automatic encryption:

```javascript
// returns the database object
myDB = cluster.getDB("myDB");

// returns the collection object
myColl = myDB.getCollection("myColl");

myColl.insertOne(
  {
    "name" : "J Doe",
    "taxid" : "123-45-6789",
    "taxid-short" : "6789"
  }
)
```

The specified automatic encryption rules encrypt the `taxid` and
`taxid-short` fields using the specified data encryption key and
algorithm. Only clients configured for the correct KMS *and* access to
the specified data encryption key can decrypt the field.

See in-use-encryption-methods for
a complete list of client-side field level encryption methods.

### Connect to a Cluster with the Stable API Enabled

The following operation creates a new connection object from within a
`mongosh` session. The mongo-api-options option 
enables Stable API V1 and specifies that you cannot 
run deprecated command or commands outside of the Stable API.

```javascript
cluster = Mongo(
  "mongodb://mymongo.example.net:27017/?replicaSet=myMongoCluster", 
   null, 
   { api: { version: "1", strict: true, deprecationErrors: true } }
)
```

To interact with the `mymongo.example.net:27017` cluster, issue
operations against the `cluster` object. For a full list of Stable API
commands, see api-v1-command-list.
