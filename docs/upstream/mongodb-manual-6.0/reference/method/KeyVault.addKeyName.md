<!-- Converted from reference/method/KeyVault.addKeyName.txt (reStructuredText). Includes are inlined. -->

# KeyVault.addKeyAltName()

**`KeyVault.addKeyAltName(UUID, keyAltName)`**

Adds the `keyAltName` to the `keyAltNames` array of the data
encryption key with `UUID`.

`keyAltName` *must* be unique among all keys in the key vault. 

Use the `getKeyVault()` method with a partial index filter on documents with `keyAltNames` to 
automatically create a unique index on 
the `keyAltNames` field.

This method is an alias for 
`addKeyAlternateName()`.

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

`addKeyAlternateName()`.
