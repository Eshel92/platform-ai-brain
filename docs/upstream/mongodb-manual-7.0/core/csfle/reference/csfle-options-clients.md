<!-- Converted from core/csfle/reference/csfle-options-clients.txt (reStructuredText). Includes are inlined. -->

# CSFLE-Specific MongoClient Options

## Overview

View information about the Client-Side Field Level Encryption (CSFLE)-specific
configuration options for `MongoClient` instances.

## AutoEncryptionOpts

Pass an `autoEncryptionOpts` object to your `MongoClient`
instance to specify CSFLE-specific options.

The following table describes the structure of an
`autoEncryptionOpts` object:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `keyVaultClient` | `MongoClient` | No | A `MongoClient` instance configured to connect to the MongoDB instance hosting your Key Vault collection. If you omit the `keyVaultClient` option, the MongoDB instance specified to your `MongoClient` instance containing the `autoEncryptionOpts` configuration is used as the host of your Key Vault collection. To learn more about Key Vault collections, see csfle-reference-key-vault. |
| `keyVaultNamespace` | String | Yes | The full namespace of the Key Vault collection. |
| `kmsProviders` | Object | Yes | The Key Management System (KMS) used by Client-Side Field Level Encryption for managing your Customer Master Keys (CMKs). To learn more about `kmsProviders` objects, see csfle-reference-kms-providers. To learn more about Customer Master Keys, see csfle-reference-keys-key-vaults. |
| `tlsOptions` | Object | No | An object that maps Key Management System provider names to TLS configuration options. To learn more about TLS options see: tls-mongod-options. To learn more about TLS see: transport-encryption. |
| `schemaMap` | Object | No | An encryption schema. To learn how to construct an encryption schema, see csfle-fundamentals-create-schema. For complete documentation of encryption schemas, see csfle-reference-encryption-schemas. |
| `bypassAutoEncryption` | Boolean | No | Specify `true` to bypass automatic Client-Side Field Level Encryption rules and perform explicit encryption. `bypassAutoEncryption` does not disable automatic decryption. To learn more about this option, see csfle-fundamentals-manual-encryption-automatic-decryption. |

## Example

To view a code-snippet demonstrating how to use
`autoEncryptionOpts` to configure your
`MongoClient` instance, select the tab corresponding to your driver:

**java-sync:**

```java
MongoClientSettings clientSettings = MongoClientSettings.builder()
    .applyConnectionString(new ConnectionString("mongodb://localhost:27017"))
    .autoEncryptionSettings(AutoEncryptionSettings.builder()
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviders)
        .schemaMap(schemaMap)
        .extraOptions(extraOptions)
        .build())
    .build();

MongoClient mongoClient = MongoClients.create(clientSettings);
```

**nodejs:**

```javascript
const secureClient = new MongoClient(connectionString, {
  monitorCommands: true,
  autoEncryption: {
    keyVaultNamespace,
    kmsProviders,
    schemaMap: patientSchema,
    extraOptions: extraOptions,
  },
});
```

**python:**

```python
fle_opts = AutoEncryptionOpts(
  kms_providers,
  key_vault_namespace,
  schema_map=patient_schema,
  **extra_options
)
client = MongoClient(connection_string, auto_encryption_opts=fle_opts)
```

**csharp:**

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(_connectionString);
var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders,
    schemaMap: schemaMap,
    extraOptions: extraOptions);
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
var client = new MongoClient(clientSettings);
```

**go:**

```go
autoEncryptionOpts := options.AutoEncryption().
	SetKmsProviders(provider.Credentials()).
	SetKeyVaultNamespace(keyVaultNamespace).
	SetSchemaMap(schemaMap).
	SetExtraOptions(extraOptions)
client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOpts))
```

**shell:**

```javascript
var autoEncryptionOpts =
{
   "keyVaultNamespace" : "<database>.<collection>",
   "kmsProviders" : { ... },
   "schemaMap" : { ... }
}

cluster = Mongo(
  "<Your Connection String>",
  autoEncryptionOpts
);
```

**Tip:** Environment Variables

If possible, consider defining the credentials provided in
`kmsProviders` as environment variables, and then passing them
to `mongosh` using the `--eval` option. This minimizes the chances of credentials
leaking into logs.
