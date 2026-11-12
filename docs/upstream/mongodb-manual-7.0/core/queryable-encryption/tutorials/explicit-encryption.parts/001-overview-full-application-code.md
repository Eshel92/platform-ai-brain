<!-- Part 1 of 4 of core/queryable-encryption/tutorials/explicit-encryption.md (split because the page is big). -->

## Overview

This guide shows you how to encrypt a document with explicit encryption
and a MongoDB driver.

After completing this guide, you can configure a driver to
encrypt fields in a document using explicit encryption. With this knowledge,
you can create a client application that uses explicit encryption.
with automatic decryption.

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


## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.


## Full Application Code

To see the complete code for the sample application, select your programming
language in the language selector.

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/exp/reader/)

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/exp/reader/)

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/exp/reader/)

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/exp/reader/)

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/exp/reader/)
