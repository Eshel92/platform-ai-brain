<!-- Converted from core/queryable-encryption/fundamentals/manage-keys.txt (reStructuredText). Includes are inlined. -->

# Encryption Key Management

In this guide, you can learn how to manage your encryption keys with a
Key Management System (KMS ({+kms-long+})) in your Queryable Encryption enabled
application.

## Encryption Components

MongoDB uses the following components to perform Queryable Encryption:

- Data Encryption Keys (DEK ({+dek-long+}))s
- Customer Master Keys (CMK ({+cmk-long+}))s
- Key Vault collections
- Key Management System (KMS ({+kms-long+}))

To learn more about keys and key vaults, see
qe-reference-keys-key-vaults.

## Rotate Encryption Keys Using mongosh

You can rotate encryption keys using the 
`KeyVault.rewrapManyDataKey()` method. The `rewrapManyDataKey` 
method automatically decrypts multiple data keys and re-encrypts them 
using a specified Customer Master Key. It then updates the rotated keys 
in the key vault collection. This method allows you to rotate encryption 
keys based on two optional arguments:

- A query filter document used to specify 
  which keys to rotate. If no data key matches the given filter, no keys 
  are rotated. Omit the filter to rotate all keys in your key vault 
  collection.

- An object that represents a new CMK ({+cmk-long+}). Omit this object to rotate
  the data keys using their current CMKs.

The `rewrapManyDataKey` method has the following syntax:

```json
let keyVault = db.getMongo().getKeyVault()

keyVault.rewrapManyDataKey(
   { 
      "<Your custom filter>" 
   },
   {
      provider: "<KMS provider>",
      masterKey: {
         "<dataKeyOpts Key>" : "<dataKeyOpts Value>"
      }
   }
)
```

## Supported Key Management Services

Queryable Encryption supports the following Key Management System providers:

- Amazon Web Services KMS
- Azure Key Vault
- Google Cloud KMS
- Any KMIP Compliant Key Management System
- Local Key Provider (for testing only)

To learn more about these providers, including diagrams that show how
your application uses them to perform Queryable Encryption, see
qe-fundamentals-kms-providers.

### Reasons to Use a Remote KMS

Using a remote Key Management System to manage your Customer Master Key
has the following advantages over using your local filesystem to host
the CMK ({+cmk-long+}):

- Secure storage of the key with access auditing
- Reduced risk of access permission issues
- Availability and distribution of the key to remote clients
- Automated key backup and recovery
- Centralized encryption key lifecycle management

Additionally, for the following KMS ({+kms-long+}) providers, your
KMS ({+kms-long+}) remotely encrypts and decrypts your Data Encryption Key, ensuring
your Customer Master Key is never exposed to your Queryable Encryption enabled
application:

- Amazon Web Services KMS
- Azure Key Vault
- Google Cloud KMS

## Learn More

For tutorials detailing how to set up a Queryable Encryption enabled
application with each of the supported KMS ({+kms-long+}) providers, see the
following pages:

- qe-tutorial-automatic-aws
- qe-tutorial-automatic-azure
- qe-tutorial-automatic-gcp
