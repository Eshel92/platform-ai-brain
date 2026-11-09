<!-- Converted from field-level-encryption.txt (reStructuredText). Includes are inlined. -->

# Field Level Encryption

When working with a [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
or MongoDB Atlas cluster, you can use `mongosh` to configure Queryable Encryption or 
Client-Side Field Level Encryption and connect with encryption
support. Both Queryable Encryption and CSFLE use data encryption keys
for supporting encryption and decryption of field values, and store
this encryption key material in a Key Management Service (KMS).

`mongosh` supports the following KMS providers for use with
Queryable Encryption and CSFLE:

- Amazon Web Services KMS
- Azure Key Vault
- Google Cloud Platform KMS
- Locally Managed Keyfile

## Create a Data Encryption Key

The following procedure uses `mongosh` to create a data encryption key for
field level encryption.

Use the tabs below to select the KMS (Key Management Service)
appropriate for your deployment:

**aws-kms:**

**Step 1: Launch the `mongosh` Shell.**

Create a `mongosh` session without connecting to a running database
by using the `--nodb` option:

```javascript
mongosh --nodb
```

**Step 2: Create the Encryption Configuration.**

Configuring client-side field level encryption for the AWS KMS
requires an AWS Access Key ID and its associated Secret Access Key.
The AWS Access Key must correspond to an IAM user with all *List* and
*Read* permissions for the KMS service.

In `mongosh`, create a new
autoEncryptionOpts variable for storing the
client-side field level encryption configuration, which contains these
credentials:

```javascript
var autoEncryptionOpts = {
  "keyVaultNamespace" : "encryption.__dataKeys",
  "kmsProviders" : {
    "aws" : {
      "accessKeyId" : "YOUR_AWS_ACCESS_KEY_ID",
      "secretAccessKey" : "YOUR_AWS_SECRET_ACCESS_KEY"
    }
  }
}
```

Fill in the values for `YOUR_AWS_ACCESS_KEY_ID` and
`YOUR_AWS_SECRET_ACCESS_KEY` as appropriate.

**Step 3: Connect with Encryption Support.**

In `mongosh`, use the `Mongo()` constructor to
establish a database connection to the target cluster. Specify the
autoEncryptionOpts document as the second
parameter to the `Mongo()` constructor to configure
the connection for client-side field level encryption:

```javascript
csfleDatabaseConnection = Mongo(
  "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster",
  autoEncryptionOpts
)
```

Replace the `replaceMe.example.net` URI with
the connection string for the target cluster.

**Step 4: Create the Key Vault Object.**

Create the `keyVault` object using the `getKeyVault()` shell method:

```javascript
keyVault = csfleDatabaseConnection.getKeyVault();
```

**Step 5: Create the Encryption Key.**

Create the data encryption key using the
`createKey()` shell method:

```javascript
keyVault.createKey(
  "aws",
  { region: "regionname", key: "awsarn" },
  [ "keyAlternateName" ]
)
```

Where:

- The first parameter *must* be `"aws"` to specify the configured
  Amazon Web Services KMS.

- The second parameter *must* be a document containing the following:

  - the AWS region you are connecting to, such as `us-west-2`

  - the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
    to the AWS customer master key (CMK).

- The third parameter *may* be an array of one or more
  `keyAltNames` for the data encryption key. Each key alternate
  name *must* be unique. `getKeyVault()` creates a
  unique index on `keyAltNames` to
  enforce uniqueness on the field if one does not already exist. Key
  alternate names facilitate data encryption key findability.

If successful, `createKey()` returns
the UUID (Universally unique identifier) of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either:

- Use `getKey()` to retrieve the created
  key by its UUID (Universally unique identifier), or
- Use `getKeyByAltName()`  to
  retrieve the key by its alternate name, if specified.

**azure-vault:**

**Step 1: Launch the `mongosh` Shell.**

Create a `mongosh` session without connecting to a running database
by using the `--nodb` option:

```javascript
mongosh --nodb
```

**Step 2: Create the Encryption Configuration.**

Configuring client-side field level encryption for Azure Key Vault
requires a valid Tenant ID, Client ID, and Client Secret.

In `mongosh`, create a new
autoEncryptionOpts variable for storing the
client-side field level encryption configuration, which contains these
credentials:

```javascript
var autoEncryptionOpts = {
  "keyVaultNamespace" : "encryption.__dataKeys",
  "kmsProviders" : {
    "azure" : {
      "tenantId" : "YOUR_TENANT_ID",
      "clientId" : "YOUR_CLIENT_ID",
      "clientSecret" : "YOUR_CLIENT_SECRET"
    }
  }
}
```

Fill in the values for `YOUR_TENANT_ID`, `YOUR_CLIENT_ID`, and
`YOUR_CLIENT_SECRET` as appropriate.

**Step 3: Connect with Encryption Support.**

In `mongosh`, use the `Mongo()` constructor to
establish a database connection to the target cluster. Specify the
autoEncryptionOpts document as the second
parameter to the `Mongo()` constructor to configure
the connection for client-side field level encryption:

```javascript
csfleDatabaseConnection = Mongo(
  "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster",
  autoEncryptionOpts
)
```

Replace the `replaceMe.example.net` URI with
the connection string for the target cluster.

**Step 4: Create the Key Vault Object.**

Create the `keyVault` object using the `getKeyVault()` shell method:

```javascript
keyVault = csfleDatabaseConnection.getKeyVault();
```

**Step 5: Create the Encryption Key.**

Create the data encryption key using the
`createKey()` shell method:

```javascript
keyVault.createKey(
  "azure",
  { keyName: "keyvaultname", keyVaultEndpoint: "endpointname" },
  [ "keyAlternateName" ]
)
```

Where:

- The first parameter *must* be `"azure"` to specify the configured
  Azure Key Vault.

- The second parameter *must* be a document containing:

  - the name of your [Azure Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates#vault-name-and-object-name)
  - the DNS name of the Azure Key Vault to use (e.g.
    `my-key-vault.vault.azure.net`)

- The third parameter *may* be an array of one or more
  `keyAltNames` for the data encryption key. Each key alternate
  name *must* be unique. `getKeyVault()` creates a
  unique index on `keyAltNames` to
  enforce uniqueness on the field if one does not already exist. Key
  alternate names facilitate data encryption key findability.

If successful, `createKey()` returns
the UUID (Universally unique identifier) of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either:

- Use `getKey()` to retrieve the created
  key by its UUID (Universally unique identifier), or
- Use `getKeyByAltName()`  to
  retrieve the key by its alternate name, if specified.

**gcp-kms:**

**Step 1: Launch the `mongosh` Shell.**

Create a `mongosh` session without connecting to a running database
by using the `--nodb` option:

```javascript
mongosh --nodb
```

**Step 2: Create the Encryption Configuration.**

Configuring client-side field level encryption for the GCP KMS
requires your GCP Email and its associated Private Key.

In `mongosh`, create a new
autoEncryptionOpts variable for storing the
client-side field level encryption configuration, which contains these
credentials:

```javascript
var autoEncryptionOpts = {
  "keyVaultNamespace" : "encryption.__dataKeys",
  "kmsProviders" : {
    "gcp" : {
      "email" : "YOUR_GCP_EMAIL",
      "privateKey" : "YOUR_GCP_PRIVATEKEY"
    }
  }
}
```

Fill in the values for `YOUR_GCP_EMAIL` and
`YOUR_GCP_PRIVATEKEY` as appropriate.

**Step 3: Connect with Encryption Support.**

In `mongosh`, use the `Mongo()` constructor to
establish a database connection to the target cluster. Specify the
autoEncryptionOpts document as the second
parameter to the `Mongo()` constructor to configure
the connection for client-side field level encryption:

```javascript
csfleDatabaseConnection = Mongo(
  "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster",
  autoEncryptionOpts
)
```

Replace the `replaceMe.example.net` URI with
the connection string for the target cluster.

**Step 4: Create the Key Vault Object.**

Create the `keyVault` object using the `getKeyVault()` shell method:

```javascript
keyVault = csfleDatabaseConnection.getKeyVault();
```

**Step 5: Create the Encryption Key.**

Create the data encryption key using the
`createKey()` shell method:

```javascript
keyVault.createKey(
  "gcp",
  { projectId: "projectid",
    location: "locationname",
    keyRing: "keyringname",
    keyName: "keyname"
  },
  [ "keyAlternateName" ]
)
```

Where:

- The first parameter *must* be `"gcp"` to specify the configured
  Google Cloud KMS.

- The second parameter *must* be a document containing

  - `projectid` is the name of your GCP project, such as
    `my-project`
  - `locationname` is the location of the KMS keyring, such as
    `global`
  - `keyringname` is the name of the KMS keyring, such as
    `my-keyring`
  - `keyname` is the name of your key.

- The third parameter *may* be an array of one or more
  `keyAltNames` for the data encryption key. Each key alternate
  name *must* be unique. `getKeyVault()` creates a
  unique index on `keyAltNames` to
  enforce uniqueness on the field if one does not already exist. Key
  alternate names facilitate data encryption key findability.

If successful, `createKey()` returns
the UUID (Universally unique identifier) of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either:

- Use `getKey()` to retrieve the created
  key by its UUID (Universally unique identifier), or
- Use `getKeyByAltName()`  to
  retrieve the key by its alternate name, if specified.

**local-keyfile:**

**Step 1: Launch the `mongosh` Shell.**

Create a `mongosh` session without connecting to a running database
by using the `--nodb` option:

```javascript
mongosh --nodb
```

**Step 2: Generate an Encryption Key.**

To configure client-side field level encryption for a locally managed
key, you must specify a base64-encoded 96-byte string with no line
breaks. Run the following command in `mongosh` to generate a key
matching these requirements:

```javascript
crypto.randomBytes(96).toString('base64')
```

You will need this key in the next step.

**Step 3: Create the Encryption Configuration.**

In `mongosh`, create a new
autoEncryptionOpts variable for storing the
client-side field level encryption configuration, replacing
`MY_LOCAL_KEY` with the key generated in step 1:

```javascript
var autoEncryptionOpts = {
  "keyVaultNamespace" : "encryption.__dataKeys",
  "kmsProviders" : {
    "local" : {
      "key" : BinData(0, "MY_LOCAL_KEY")
    }
  }
}
```

**Step 4: Connect with Encryption Support.**

In `mongosh`, use the `Mongo()` constructor to
establish a database connection to the target cluster. Specify the
autoEncryptionOpts document as the second
parameter to the `Mongo()` constructor to configure
the connection for client-side field level encryption:

```javascript
csfleDatabaseConnection = Mongo(
  "mongodb://replaceMe.example.net:27017/?replicaSet=myMongoCluster",
  autoEncryptionOpts
)
```

**Step 5: Create the Key Vault Object.**

Create the `keyVault` object using the `getKeyVault()` shell method:

```javascript
keyVault = csfleDatabaseConnection.getKeyVault();
```

**Step 6: Create the Encryption Key.**

Create the data encryption key using the
`createKey()` shell method:

```javascript
keyVault.createKey(
  "local",
  [ "keyAlternateName" ]
)
```

Where:

- The first parameter *must* be `local` to specify the configured
  Locally Managed Key.

- The second parameter *may* be an array of one or more
  `keyAltNames` for the data encryption key. Each key alternate
  name *must* be unique. `getKeyVault()` creates a unique
  index on `keyAltNames` to enforce uniqueness on the field if
  one does not already exist. Key alternate names facilitate data
  encryption key findability.

If successful, `createKey()` returns
the UUID (Universally unique identifier) of the new data
encryption key. To retrieve the new data encryption key document from
the key vault, either:

- Use `getKey()` to retrieve the created
  key by its UUID (Universally unique identifier), or
- Use `getKeyByAltName()`  to
  retrieve the key by its alternate name, if specified.

**See also:**

- List of field level encryption shell methods
- Queryable Encryption
- Client-Side Field Level Encryption
