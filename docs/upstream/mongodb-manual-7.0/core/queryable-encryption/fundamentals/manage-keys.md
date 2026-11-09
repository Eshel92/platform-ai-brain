<!-- Converted from core/queryable-encryption/fundamentals/manage-keys.txt (reStructuredText). Includes are inlined. -->

# Rotate and Rewrap Encryption Keys

In this guide, you can learn how to manage your encryption keys with a
Key Management System (KMS ({+kms-long+})) in your application.

## Overview

This procedure shows you how to rotate encryption keys for Queryable Encryption using
`mongosh`. Rotating DEKs consists of rewrapping them with a
new Customer Master Key, so the terms "rotate" and "rewrap" are sometimes used interchangeably.

After completing this guide, you should be able to rotate your
Customer Master Key (CMK ({+cmk-long+})) on your Key Management System, and then rewrap 
existing DEKs in your Key Vault collection with your new
CMK ({+cmk-long+}).

**Warning:**

As you rotate keys, confirm that they aren't used to encrypt any
other keys or data before deleting them. Keep your previous
CMK ({+cmk-long+}) enabled on your KMS ({+kms-long+}) until you rewrap every
DEK ({+dek-long+}) that uses it. If you delete a DEK ({+dek-long+}), all fields
encrypted with that DEK ({+dek-long+}) become permanently unreadable. If
you delete a CMK ({+cmk-long+}), all fields encrypted with a DEK ({+dek-long+})
using that CMK ({+cmk-long+}) become permanently unreadable.

### Related Information

For a detailed explanation of the concepts included in this procedure,
refer to the topics below.

To learn more about keys and key vaults, see
qe-reference-keys-key-vaults.
To view a list of supported KMS ({+kms-long+}) providers, see the
qe-fundamentals-kms-providers page.

For tutorials detailing how to set up a Queryable Encryption enabled
application with each of the supported KMS ({+kms-long+}) providers, see the
following pages:

- qe-tutorial-automatic-aws
- qe-tutorial-automatic-azure
- qe-tutorial-automatic-gcp

## Procedure

**Step 1: Rotate your Customer Master Key on your Key Management System**

The process for rotating your CMK ({+cmk-long+}) depends on your
KMS ({+kms-long+}) provider. For details, refer to your key provider's
documentation:

- AWS: [Rotating AWS KMS Keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
- Azure: [Configure cryptographic key auto-rotation in Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/keys/how-to-configure-key-rotation)
- GCP: [Rotate a key](https://cloud.google.com/kms/docs/rotate-key)

Once you rotate the CMK ({+cmk-long+}), MongoDB uses it to wrap all new
DEKs. To re-wrap existing DEKs, continue to the following steps.

**Step 2: Rotate your Data Encryption Keys using `KeyVault.rewrapManyDataKey()`**

The `KeyVault.rewrapManyDataKey()` method automatically
decrypts multiple Data Encryption Keys and re-encrypts them using the
specified CMK ({+cmk-long+}). It then updates the keys in the 
Key Vault collection.

The method has the following syntax:

```javascript
let keyVault = db.getMongo().getKeyVault()

keyVault.rewrapManyDataKey(
   { 
      "<Query filter document>" 
   },
   {
      provider: "<KMS provider>",
      masterKey: {
         "<dataKeyOpts Key>" : "<dataKeyOpts Value>"
      }
   }
)
```

#. Specify a query filter document to select the keys to rotate, or omit the argument to rotate all keys in the Key Vault collection

   If you specify a query filter document, but no keys match, then no keys rotate.

#. Specify the KMS ({+kms-long+}) provider

#. Specify the `masterKey` using the new CMK ({+cmk-long+}), 
   or omit the argument to rotate keys using their existing CMK ({+cmk-long+})

Your DEKs themselves are left unchanged after re-wrapping them
with the new CMK ({+cmk-long+}). The key rotation process is seamless, and does
not interrupt your application.
