<!-- Converted from reference/method/js-client-side-field-level-encryption.txt (reStructuredText). Includes are inlined. -->

# Client-Side Field Level Encryption Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

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

The following methods are for `mongosh`
*only*. For instructions on implementing client-side field level
encryption using a MongoDB driver, defer to the driver documentation. See 
field-level-encryption-drivers for a complete list of drivers with 
support for client-side field level encryption.

| Name | Description |
|---|---|
| `getKeyVault()` | Returns the key vault object for the current MongoDB connection. |
| `KeyVault.createKey()` | Creates a data encryption key for use with client-side field level encryption. |
| `KeyVault.deleteKey()` | Deletes the specified data encryption key from the key vault. |
| `KeyVault.getKey()` | Retreives the specified data encryption key from the key vault. |
| `KeyVault.getKeys()` | Retrieves all keys in the key vault. |
| `KeyVault.addKeyAlternateName()` | Associates a key alternative name to the specified data encryption key. |
| `KeyVault.removeKeyAlternateName()` | Removes a key alternative name from the specified data encryption key. |
| `KeyVault.rewrapManyDataKey()` | Decrypts multiple data keys and re-encrypts them with a new master key. |
| `KeyVault.getKeyByAltName()` | Retrieves keys with the specified key alternative name. |
| `getClientEncryption()` | Returns the client encryption object for supporting explicit encryption/decryption of fields. |
| `ClientEncryption.encrypt()` | Encrypts a field using a specified data encryption key and encryption algorithm. |
| `ClientEncryption.decrypt()` | Decrypts a field using the associated data encryption key and encryption algorithm. |
