<!-- Converted from reference/method/KeyVault.createDataKey.txt (reStructuredText). Includes are inlined. -->

# KeyVault.createDataKey()

**`KeyVault.createDataKey(keyManagementService, customerMasterKey, ["keyAltName"])`**

Adds a data encryption key to the key vault associated to the
database connection. Client-Side Field Level Encryption uses data encryption keys
for supporting encryption and decryption of field values.

This method is an alias for
`createKey()`.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**See also:**

`createKey()`.
