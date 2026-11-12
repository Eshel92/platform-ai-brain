<!-- Converted from core/queryable-encryption/quick-start.txt (reStructuredText). Includes are inlined. -->

# Queryable Encryption Quick Start

This tutorial shows you how to build an application that implements the 
MongoDB Queryable Encryption feature to automatically encrypt and decrypt document fields.

The tutorial includes the following sections:

- **Set Up Your Project**: Install the driver and encryption dependencies, 
  configure your environment variables, and create your project files with 
  the required application variables.
- **Configure Encryption**: Create a Customer Master Key (CMK ({+cmk-long+})),
  configure your KMS provider and automatic encryption settings, and
  create an encryption-enabled client and collection.
- **Perform Encrypted Operations**: Insert a document with encrypted
  fields, query on an encrypted field, and run the application to view
  the decrypted results.

Select your driver language in the drop-down menu to learn how to create an 
application that automatically encrypts and decrypts document fields.

**Important:** Do Not Use this Sample Application In Production

Because the instructions in this tutorial include storing an encryption key in an insecure
environment, you should not use an unmodified version of this
application in production. Using this application in production risks
unauthorized access to the encryption key or loss of the key needed to
decrypt your data. The purpose of this tutorial is to demonstrate how to use
Queryable Encryption without needing to set up a Key Management System.

You can use a Key Management System to securely store your encryption key in a production
environment. A KMS ({+kms-long+}) is a remote service that securely stores and manages your
encryption keys. To learn how to set up a Queryable Encryption enabled application that
uses a KMS ({+kms-long+}), see the Queryable Encryption Tutorials.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `quick-start.parts/`)

- `001-before-you-begin-set-up-your-project.md`: Before You Begin … Set Up Your Project
- `002-procedure-configure-encryption-perform-encrypted-o.md`: Procedure › Configure Encryption … Perform Encrypted Operations
- `003-procedure-set-up-your-project-configure-encryption.md`: Procedure › Set Up Your Project … Configure Encryption
- `004-procedure-perform-encrypted-operations-perform-enc.md`: Procedure › Perform Encrypted Operations … Perform Encrypted Operations
- `005-procedure-set-up-your-project-learn-more.md`: Procedure › Set Up Your Project … Learn More
