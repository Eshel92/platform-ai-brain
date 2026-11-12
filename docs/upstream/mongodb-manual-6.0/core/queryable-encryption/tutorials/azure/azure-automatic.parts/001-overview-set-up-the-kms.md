<!-- Part 1 of 4 of core/queryable-encryption/tutorials/azure/azure-automatic.md (split because the page is big). -->

## Overview

This guide shows you how to build a Queryable Encryption enabled
application using Azure Key Vault.

After you complete the steps in this guide, you should have:

- A Customer Master Key hosted on an Azure Key Vault instance.
- A working client application that inserts encrypted documents
  using your Customer Master Key.


## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.

**See also:** Full Application

To see the complete code for the application you make in this guide,
select the tab corresponding to your programming language and follow
the provided link:

**shell:**

[Complete Mongosh Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/azure/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/azure/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/azure/reader/)

**java-sync:**

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/azure/reader/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/azure/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/azure/reader/)


## Set Up the KMS

**Step 1: Register your Application with Azure**

**Step 1: Log in to [Azure](https://azure.microsoft.com/en-us/features/azure-portal/).**

**Step 2: Register your Application with Azure Active Directory**

To register an application on Azure Active Directory,
follow Microsoft's official
[Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
Quick Start.

**Important:** Record your Credentials

Ensure you record the following credentials:

- **tenant id**
- **client id**
- **client secret**

You will need them to construct your `kmsProviders` object
later in this tutorial.

**Step 3: Create the Customer Master Key**

**Step 1: Create your Azure Key Vault and Customer Master Key**

To create a new Azure Key Vault instance and Customer Master Key,
follow Microsoft's official
[Set and retrieve a key from Azure Key Vault using the Azure portal](https://docs.microsoft.com/en-us/azure/key-vault/keys/quick-create-portal)
Quick Start.

**Important:** Record your Credentials

Ensure you record the following credentials:

- **Key Name**
- **Key Identifier** (referred to as `keyVaultEndpoint` later in this guide)
- **Key Version**

You will need them to construct your `dataKeyOpts` object
later in this tutorial.

**Step 2: Grant Permissions**

Grant your client application `wrap` and `unwrap` permissions
to the key.
