<!-- Converted from core/queryable-encryption/reference/qe-options-clients.txt (reStructuredText). Includes are inlined. -->

# MongoClient Options for Queryable Encryption

## Overview

View information about the Queryable Encryption specific
configuration options for `MongoClient` instances.

## AutoEncryptionOpts

Pass an `AutoEncryptionOpts` object to your `MongoClient`
instance to specify Queryable Encryption specific options.

The following table describes the structure of an
`AutoEncryptionOpts` object:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `keyVaultClient` | `MongoClient` | No | A `MongoClient` instance configured to connect to the MongoDB instance hosting your Key Vault collection. If you omit the `keyVaultClient` option, the MongoDB instance specified to your `MongoClient` instance containing the `AutoEncryptionOpts` configuration is used as the host of your Key Vault collection. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `keyVaultNamespace` | String | Yes | The full namespace of the Key Vault collection. |
| `kmsProviders` | Object | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `kmsProviders` objects, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `encryptedFieldsMap` | Object | No | An encryption schema. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `bypassQueryAnalysis` | Boolean | No | Disables automatic analysis of outgoing commands. Set `bypassQueryAnalysis` to `true` to use explicit encryption on indexed fields without the `crypt_shared` library. Defaults to `false` if not specified. |

## Example

To view a code-snippet demonstrating how to use
`AutoEncryptionOpts` to configure your
`MongoClient` instance, select the tab corresponding to your driver:

**nodejs:**

```javascript
const secureClient = new MongoClient(connectionString, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  monitorCommands: true,
  autoEncryption: {
    keyVaultNamespace,
    kmsProviders,
    bypassQueryAnalysis, // optional - defaults to false
    encryptedFieldsMap: patientSchema,
    extraOptions: extraOptions,
  },
});
```

**shell:**

```javascript
var AutoEncryptionOpts =
{
   "keyVaultClient" : keyVaultClient,
   "keyVaultNamespace" : "<database>.<collection>",
   "kmsProviders" : { ... },
   "bypassQueryAnalysis": "<boolean value>", // optional - defaults to false
   "encryptedFieldsMap" : { ... }
}

cluster = Mongo(
  "mongodb://myhostexample.net:27017/?replicaSet=myReplicaSet",
  AutoEncryptionOpts
);
```

**Tip:** Environment Variables

If possible, consider defining the credentials provided in
`kmsProviders` as environment variables, and then passing them
to `mongosh` using the `--eval` option. This minimizes the chances of credentials
leaking into logs.

To learn about additional options for configuring Automatic Encryption Shared Library,
see qe-reference-shared-library-configuration.
