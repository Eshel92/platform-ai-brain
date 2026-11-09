<!-- Converted from core/queryable-encryption/reference/qe-options-clients.txt (reStructuredText). Includes are inlined. -->

# MongoClient Options for Queryable Encryption

## Overview

On this page, you can learn about the Queryable Encryption-specific configuration options for
`MongoClient` instances.

## Automatic Encryption Options

**nodejs:**

The following table describes the structure of an `AutoEncryptionOptions` object:

| Property | Data Type | Required? | Description |
|---|---|---|---|
| `keyVaultNamespace` | `String` | Yes | The full namespace of the Key Vault collection. |
| `kmsProviders` | `Object` | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `kmsProviders` objects, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `bypassAutoEncryption` | `Boolean` | No | Specify `true` to bypass automatic encryption rules and perform explicit (manual) per-field encryption. |
| `bypassQueryAnalysis` | `Boolean` | No | Disables automatic analysis of outgoing commands. Specify `true` to use explicit encryption without the Automatic Encryption Shared Library. Defaults to `false` if not specified. |
| `encryptedFieldsMap` | `Object` | No | A schema that specifies which fields to automatically encrypt and the types of queries allowed on those fields. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `extraOptions` | `Object` | No | Configuration options for the encryption library. To use the Automatic Encryption Shared Library instead of `mongocryptd`, specify the full absolute or relative file path to the library file in the `cryptSharedLibPath` property of this object. If the driver can't load the Automatic Encryption Shared Library from this path, creating the `MongoClient` will fail. |
| `keyVaultClient` | `MongoClient` | No | Specifies the `MongoClient` that should connect to the MongoDB instance hosting your Key Vault collection. If you omit this option, the driver uses the current `MongoClient` instance. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `tlsOptions` | `Object` | No | The TLS options to use when connecting to the KMS provider. |

**Note:** API Documentation

For more information on these automatic encryption options, see the 
API documentation for the
[AutoEncryptionOptions](https://mongodb.github.io/node-mongodb-native/5.7/interfaces/AutoEncryptionOptions.html)
interface.

**shell:**

The following table describes the structure of an `AutoEncryptionOptions` object:

| Property | Data Type | Required? | Description |
|---|---|---|---|
| `keyVaultNamespace` | `String` | Yes | The full namespace of the Key Vault collection. |
| `kmsProviders` | `Object` | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `kmsProviders` objects, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `bypassAutoEncryption` | `Boolean` | No | Specify `true` to bypass automatic encryption rules and perform explicit (manual) per-field encryption. |
| `bypassQueryAnalysis` | `Boolean` | No | Disables automatic analysis of outgoing commands. Specify `true` to use explicit encryption without the Automatic Encryption Shared Library. |
| `encryptedFieldsMap` | `Object` | No | A schema that specifies which fields to automatically encrypt and the types of queries allowed on those fields. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `explicitEncryptionOnly` | `Boolean` | No | If you set `explicitEncryptionOnly` to `true`, the driver uses only explicit (manual) per-field encryption and removes automatic encryption settings from the connection. You must encrypt and decrypt field values manually using the `ClientEncryption` API. This option only works with CSFLE. |
| `keyVaultClient` | `MongoClient` | No | Specifies the `MongoClient` that should connect to the MongoDB instance hosting your Key Vault collection. If you omit this option, the driver uses the current `MongoClient` instance. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `tlsOptions` | `Object` | No | The TLS options to use when connecting to the KMS provider. |

**python:**

The following table describes the parameters of the `AutoEncryptionOpts` class:

| Parameter | Data Type | Required? | Description |
|---|---|---|---|
| `key_vault_namespace` | `String` | Yes | The full namespace of the Key Vault collection. |
| `kms_providers` | `Mapping[string, Any]` | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `kms_Providers` maps, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `bypass_auto_encryption` | `Boolean` | No | Specify `True` to bypass automatic encryption rules and perform explicit (manual) per-field encryption. |
| `bypass_query_analysis` | `Boolean` | No | Disables automatic analysis of outgoing commands. Specify `True` to use explicit encryption without the Automatic Encryption Shared Library. |
| `encrypted_fields_map` | `Mapping` | No | A schema that specifies which fields to automatically encrypt and the types of queries allowed on those fields. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `crypt_shared_lib_path` | `String` | No | Specify the full absolute or relative file path to the library file in the this parameter to use the Automatic Encryption Shared Library instead of `mongocryptd`, If the driver can't load the Automatic Encryption Shared Library from this path, it raises an error. |
| `crypt_shared_lib_required` | `Boolean` | No | If you specify `True`, the driver raises an error if `libmongocrypt` can't load the Automatic Encryption Shared Library. |
| `key_vault_client` | `MongoClient` | No | Specifies the `MongoClient` that should connect to the MongoDB instance hosting your Key Vault collection. If you omit this option, the driver uses the current `MongoClient` instance. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `kms_tls_options` | `Mapping[string, Any]` | No | The TLS options to use when connecting to the KMS provider. |
| `mongocryptd_uri` | `String` | No | The MongoDB URI used to connect to the local `mongocryptd` process, if using `mongocryptd` for encryption. |
| `mongocryptd_bypass_spawn` | `Boolean` | No | If you specify `True` for this parameter, the encrypted `MongoClient` does not attempt to spawn the `mongocryptd` process, if using `mongocryptd` for encryption. |
| `mongocryptd_spawn_path` | `String` | No | Used for spawning the `mongocryptd` process, if using `mongocryptd` for encryption. |
| `mongocryptd_spawn_args` | `String` | No | A list of string arguments to use when spawning the `mongocryptd` process, if using `mongocryptd` for encryption. |

**Note:** API Documentation

For more information on these automatic encryption options, see the 
API documentation for the
[AutoEncryptionOpts](https://pymongo.readthedocs.io/en/stable/api/pymongo/encryption_options.html#pymongo.encryption_options.AutoEncryptionOpts)
class.

**go:**

The following table describes the options in an `AutoEncryptionOptions` object:

| Option | Data Type | Required? | Description |
|---|---|---|---|
| `KeyVaultNamespace` | `String` | Yes | The full namespace of the Key Vault collection. |
| `KmsProviders` | `map[string]map[string]interface{}` | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `KmsProviders` objects, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `BypassAutoEncryption` | `*bool` | No | Specify `true` to bypass automatic encryption rules and perform explicit (manual) per-field encryption. |
| `BypassQueryAnalysis` | `*bool` | No | Disables automatic analysis of outgoing commands. Specify `true` to use explicit encryption without the Automatic Encryption Shared Library. |
| `EncryptedFieldsMap` | `map[string]interface{}` | No | A schema that specifies which fields to automatically encrypt and the types of queries allowed on those fields. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `ExtraOptions` | `map[string]interface{}` | No | Configuration options for the encryption library. To use the Automatic Encryption Shared Library instead of `mongocryptd`, specify the full absolute or relative file path to the library file in the `cryptSharedLibPath` property. If the driver can't load the Automatic Encryption Shared Library from this path, creating the `MongoClient` will fail. |
| `KeyVaultClientOptions` | `*ClientOptions` | No | Options for a new internal `mongo.Client` to connect to the MongoDB instance hosting your Key Vault collection. If you omit this option, the driver uses the current `MongoClient` instance. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `TlsConfig` | `map[string]*tls.Config` | No | The TLS options to use when connecting to the KMS provider. |

**Note:** API Documentation

For more information on these automatic encryption options, see the 
API documentation for the
[AutoEncryptionOptions](https://pkg.go.dev/go.mongodb.org/mongo-driver@v1.12.1/mongo/options#AutoEncryptionOptions)
type.

**csharp:**

The following table describes the properties in an `AutoEncryptionOptions` object:

| Property | Data Type | Required? | Description |
|---|---|---|---|
| `KeyVaultNamespace` | `CollectionNamespace` | Yes | The full namespace of the Key Vault collection. |
| `KmsProviders` | `IReadOnlyDictionary` | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `KmsProviders` objects, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `BypassAutoEncryption` | `Boolean` | No | Specify `true` to bypass automatic encryption rules and perform explicit (manual) per-field encryption. |
| `BypassQueryAnalysis` | `Boolean` | No | Disables automatic analysis of outgoing commands. Set this property to `true` to use explicit encryption without the Automatic Encryption Shared Library. |
| `EncryptedFieldsMap` | `IReadOnlyDictionary` | No | A schema that specifies which fields to automatically encrypt and the types of queries allowed on those fields. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `ExtraOptions` | `IReadOnlyDictionary` | No | Configuration options for the encryption library. To use the Automatic Encryption Shared Library instead of `mongocryptd`, specify the full absolute or relative file path to the library file in the `cryptSharedLibPath` property. If the driver can't load the Automatic Encryption Shared Library from this path, creating the `MongoClient` will fail. |
| `KeyVaultClient` | `IMongoClient` | No | Specifies the `MongoClient` that should connect to the MongoDB instance hosting your Key Vault collection. If you omit this option, the driver uses the current `MongoClient` instance. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `TlsOptions` | `IReadOnlyDictionary` | No | The TLS options to use when connecting to the KMS provider. |

**Note:** API Documentation

For more information on these automatic encryption options, see the 
API documentation for the [AutoEncryptionOptions](https://mongodb.github.io/mongo-csharp-driver/2.20/apidocs/html/T_MongoDB_Driver_Encryption_AutoEncryptionOptions.htm)
class.

**java-sync:**

The following table describes the methods available on the `AutoEncryptionSettings`
builder:

| Method | Data Type | Required? | Description |
|---|---|---|---|
| `keyVaultNamespace` | `String` | Yes | The full namespace of the Key Vault collection. |
| `kmsProviders` | `Map` | Yes | The Key Management System (KMS) used by Queryable Encryption for managing your Customer Master Keys (CMKs). To learn more about `kmsProviders` objects, see qe-fundamentals-kms-providers. To learn more about Customer Master Keys, see qe-reference-keys-key-vaults. |
| `bypassAutoEncryption` | `Boolean` | No | Specify `true` to bypass automatic encryption rules and perform explicit (manual) per-field encryption. |
| `bypassQueryAnalysis` | `Boolean` | No | Disables automatic analysis of outgoing commands. Specify `true` to use explicit encryption without the Automatic Encryption Shared Library. |
| `encryptedFieldsMap` | `Map` | No | A schema that specifies which fields to automatically encrypt and the types of queries allowed on those fields. To learn how to construct an encryption schema, see qe-fundamentals-encrypt-query. |
| `extraOptions` | `Map` | No | Configuration options for the encryption library. To use the Automatic Encryption Shared Library instead of `mongocryptd`, specify the full absolute or relative file path to the library file in the `cryptSharedLibPath` property. |
| `keyVaultMongoClientSettings` | `MongoClientSettings` | No | Settings for a new `MongoClient` instance to connect to the MongoDB instance hosting your Key Vault collection. If you omit this option, the driver uses the current `MongoClient` instance. To learn more about Key Vault collections, see qe-reference-key-vault. |
| `kmsProviderPropertySuppliers` | `Map` | No | Similar to the `kmsProviders()` method, but configures a `Supplier` for each property instead. |
| `kmsProviderSslContextMap` | `Map` | No | The SSL context to use for authentication. |

**Note:** API Documentation

For more information on these automatic encryption options, see the 
API documentation for the [AutoEncryptionSettings.Builder](https://mongodb.github.io/mongo-java-driver/4.10/apidocs/mongodb-driver-core/com/mongodb/AutoEncryptionSettings.Builder.html)
class.
