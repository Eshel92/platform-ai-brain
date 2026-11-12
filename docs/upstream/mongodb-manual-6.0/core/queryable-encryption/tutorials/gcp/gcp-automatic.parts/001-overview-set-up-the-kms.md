<!-- Part 1 of 4 of core/queryable-encryption/tutorials/gcp/gcp-automatic.md (split because the page is big). -->

## Overview

This guide shows you how to build a Queryable Encryption enabled
application using Google Cloud Key Management Service.

After you complete the steps in this guide, you should have:

- A CMK ({+cmk-long+}) hosted on Google Cloud Key Management Service.
- A client application that inserts encrypted documents using your CMK ({+cmk-long+}).


## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.

**See also:** Full Application

To see the complete code for the application you make in this guide,
select the tab corresponding to your programming language and follow
the provided link:

**shell:**

[Complete Mongosh Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/gcp/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/gcp/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/gcp/reader/)

**java-sync:**

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/gcp/reader/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/gcp/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/gcp/reader/)


## Set Up the KMS

**Step 1: Register a GCP Service Account**

**Step 1: Register or log in to your existing account on [Google Cloud](https://cloud.google.com).**

**Step 2: Create a service account for your project**

To create a service account on Google Cloud, follow the
[Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating)
guide in Google's official documentation.

**Step 3: Add a service account key**

To add a service account key on Google Cloud, follow the
[Managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
guide in Google's official documentation.

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**Step 4: Create a GCP Customer Master Key**

**Step 1: Create a new Customer Master Key**

Create a key ring and a symmetric key by following the
[Create a key](https://cloud.google.com/kms/docs/creating-keys)
guide from Google's official documentation.

This key is your Customer Master Key (CMK ({+cmk-long+})).

Record the following details of your CMK ({+cmk-long+}) for use in a future
step of this tutorial.

| Field | Required | Description |
|---|---|---|
| key_name | Yes | Identifier for the CMK ({+cmk-long+}). |
| key_ring | Yes | Identifier for the group of keys your key belongs to. |
| key_version | No | The version of the named key. |
| location | Yes | Region specified for your key. |
| endpoint | No | The host and optional port of the Google Cloud KMS. The default value is `cloudkms.googleapis.com`. |
