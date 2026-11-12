<!-- Part 1 of 3 of core/queryable-encryption/quick-start.md (split because the page is big). -->

## Overview

This guide shows you how to encrypt a document with automatic
Queryable Encryption and a MongoDB driver.

After completing this guide, you should have the following knowledge
and software:

- Knowledge of the steps to configure a driver to encrypt fields in a
  document.
- A working, but not production-ready, client application that
  utilizes automatic Queryable Encryption.

**Important:** Do Not Use this Application In Production

Since this example application stores an encryption key on your
application's filesystem, you risk unauthorized access to the key or
loss of the key to decrypt your data.

To view a tutorial that demonstrates how to create a
Queryable Encryption enabled application that uses a remote Key Management System, see
qe-tutorial-automatic-encryption.


## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.

**See also:** Full Application

To see the complete code for the application you make in this guide,
select the tab corresponding to your programming language and follow
the provided link:

**shell:**

[Complete mongosh Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/local/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/local/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/local/reader/)

**java:**

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/local/reader/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/local/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/local/reader/)
