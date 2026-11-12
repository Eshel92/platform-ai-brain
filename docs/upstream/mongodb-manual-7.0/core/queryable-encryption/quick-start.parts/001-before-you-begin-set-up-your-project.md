<!-- Part 1 of 5 of core/queryable-encryption/quick-start.md (split because the page is big). -->

## Before You Begin

Before you begin this tutorial, complete the following prerequisite steps:

#. Download the Automatic Encryption Shared Library from the MongoDB Download Center.
   Navigate to the MongoDB Enterprise Server Download section and 
   select the following options:

   - In the Version dropdown, select the version marked as `"current"`.
   - In the Platform dropdown, select your platform.
   - In the Package dropdown, select `crypt_shared`.

   Extract the archive and save the path to the shared library file for future use.

   **Note:** Query Analysis Component

   The Automatic Encryption Shared Library is a preferred alternative to `mongocryptd` and
   does not require spawning a new process to perform automatic encryption.
   This tutorial uses the Automatic Encryption Shared Library.

#. Configure a MongoDB Atlas cluster or a local replica set deployment, and save your
   connection string for future use. To learn more, see the unified-get-started
   tutorial.

   **Note:**

   MongoDB Community Edition doesn't support 
   Queryable Encryption with Automatic Encryption.

#. Ensure your database user has `dbAdmin` permissions on the following 
   namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

### Full Application Code

[Complete mongosh Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/mongosh/)

To view the complete code for the sample application, see
[Complete Node.js Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/node/)

**Tip:** Driver Integration Tutorials

To use the Mongoose library to implement Queryable Encryption,
see node-mongoose-qe in the Node.js driver documentation.

[Complete Python Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/python/)

**Tip:** Driver Integration Tutorials

To use Queryable Encryption in a Django application,
see django-qe in the Django MongoDB Backend documentation.

[Complete Java Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/java/)

[Complete Go Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/go/)

[Complete C# Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/csharp/)

[Complete Rust Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/rust/)

[Complete PHP Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/php/)

[Complete Ruby Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/ruby/)


## Procedure


### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Create your project directory.**

Create a directory named `shell-qe` to store your project files:

```bash
mkdir shell-qe
cd shell-qe
```

**Step 2: Set up your environment variables.**

In your `shell-qe` directory, create a `.envrc` file. The sample code 
in this tutorial references environment variables that you need to set in 
this `.envrc` file. 

Paste the following code into this file and replace the placeholder value 
with your own MongoDB deployment connection URI:

```bash
export MONGODB_URI="<Your MongoDB URI>"
```

After you create your `.envrc` file, run the following command to load 
the environment variables into your shell:

```bash
source .envrc
```

For more information on setting up environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/mongosh/README.md)  file included in 
the sample application on GitHub.

**Step 3: Create your main project file.**

In your `shell-qe` directory, create a file named `quickstart.js`.
Paste the following starter code into this file. The placeholder comments
indicate where you will add code in future steps of this tutorial:

```javascript
const fs = require("fs");
const crypto = require("crypto");

async function runExample() {

  // Paste application variables below

  // Paste code to generate CMK below

  // Paste code to retrieve CMK and specify KMS provider settings below

  // Paste automatic encryption options code below

  // Paste client configuration code below

  // Paste schema below

  // Paste code to create an encrypted collection below

  // Paste code to insert a document below

  // Paste code to query the document below
}

runExample();
```

**Step 4: Assign your application variables.**

Declare the required application variables by pasting the following code 
into your `quickstart.js` file under the ``// Paste application 
variables below`` comment. For this tutorial, set the 
`kmsProviderName` variable to `"local"`.

```javascript
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
const kmsProviderName = "<Your KMS Provider Name>";
const uri = process.env.MONGODB_URI; // Your connection URI
const keyVaultDatabaseName = "encryption";
const keyVaultCollectionName = "__keyVault";
const keyVaultNamespace = `${keyVaultDatabaseName}.${keyVaultCollectionName}`;
const encryptedDatabaseName = "medicalRecords";
const encryptedCollectionName = "patients";
```

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS used to store your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable. |
| `keyVaultDatabaseName` | The database where DEKs are stored. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection where DEKs are stored. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB where your DEKs are stored. Set this variable to the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database where encrypted data is stored. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection where encrypted data is stored. Set to `"patients"`. |


### Configure Encryption

After you set up your project, follow the steps in this section to create an
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `quickstart.js` file under the
`// Paste code to generate CMK below` comment. This code snippet creates
a 96-byte Customer Master Key and saves it to your filesystem as the
file `customer-master-key.txt`:

```javascript
customerMasterKeyPath = "customer-master-key.txt";
if (!fs.existsSync(customerMasterKeyPath)) {
  fs.writeFileSync(customerMasterKeyPath, crypto.randomBytes(96));
}
```

**Warning:** Do Not Use a Local Key File in Production

A local key file in your filesystem is insecure and is
**not recommended** for production. Instead,
you should store your Customer Master Keys in a remote
Key Management System
(KMS ({+kms-long+})).

To learn how to use a remote KMS ({+kms-long+}) in your Queryable Encryption implementation,
see the qe-tutorial-automatic-encryption guide.

**Step 2: Retrieve the Customer Master Key and specify the KMS provider settings.**

Paste the following code into your `quickstart.js` file under the
`// Paste code to retrieve CMK and specify KMS provider settings below`
comment to retrieve the contents of the `customer-master-key.txt` file
you generated in the previous step:

```javascript
// WARNING: Do not use a local key file in a production application
const localMasterKey = fs.readFileSync("./customer-master-key.txt");
kmsProviderCredentials = {
  local: {
    key: localMasterKey,
  },
};
```

This code sets the provider name to `local` to use a Local Key Provider
and uses the CMK ({+cmk-long+}) value from your KMS provider settings.

**Step 3: Set your automatic encryption options.**

Add the following code under the
`// Paste automatic encryption options code below` comment to create an
`autoEncryptionOptions` object that contains the following options:

- The namespace of your Key Vault collection
- The `kmsProviders` object, defined in the previous step

```javascript
const autoEncryptionOptions = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviderCredentials,
};
```

**Step 4: Create a client to set up an encrypted collection.**

Create a new client to encrypt and decrypt your collection. The client
uses your connection URI and automatic encryption options. Paste the
following code into your `quickstart.js` file, under the
`// Paste client configuration code below` comment:

```javascript
const encryptedClient = Mongo(uri, autoEncryptionOptions);
```

**Step 5: Specify fields to encrypt.**

To encrypt a field, add it to the encryption schema. To enable queries on a
field, add the `queries` property. Paste the following code under the
`// Paste schema below` comment:

```javascript
const encryptedFieldsMap = {
  encryptedFields: {
    fields: [
      {
        path: "patientRecord.ssn",
        bsonType: "string",
        queries: { queryType: "equality" },
      },
      {
        path: "patientRecord.billing",
        bsonType: "object",
      },
    ],
  },
};
```

**Note:**

In the previous code sample, both the `ssn` and `billing` fields
are encrypted. However, only the `ssn` field can be queried because
it contains the `queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `quickstart.js` file, under the
`// Paste code to create an encrypted collection below` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```javascript
const clientEncryption = encryptedClient.getClientEncryption()
```

Because you are using a local Customer Master Key, you don't need to provide
Customer Master Key credentials. Create a variable containing an empty object to
use in place of credentials when you create your encrypted collection.

```javascript
customerMasterKeyCredentials = {};
```

Create your encrypted collection by using the encryption helper method
accessed through the `ClientEncryption` class. This method automatically
generates data encryption keys for your encrypted fields and creates the
encrypted collection:

```javascript
await clientEncryption.createEncryptedCollection(
  encryptedDatabaseName,
  encryptedCollectionName,
  {
    provider: kmsProviderName,
    createCollectionOptions: encryptedFieldsMap,
    masterKey: customerMasterKeyCredentials,
  }
);
```


### Perform Encrypted Operations

After you configure your application and database connection, you can insert
and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

Paste the following code under the
`// Paste code to insert a document below` comment to create a
document that stores patient data and insert it into the `patients`
collection:

```javascript
const patientDocument = {
  patientName: "Jon Doe",
  patientId: 12345678,
  patientRecord: {
    ssn: "987-65-4320",
    billing: {
      type: "Visa",
      number: "4111111111111111",
    },
  },
};

const encryptedCollection = encryptedClient.getDB(encryptedDatabaseName).getCollection(encryptedCollectionName);

const insertResult = await encryptedCollection.insertOne(patientDocument);
```

**Step 2: Query on encrypted data.**

Add the following code to your `quickstart.js` file under the
`// Paste code to query the document below` comment:

```javascript
const findResult = await encryptedCollection.findOne({
  "patientRecord.ssn": "987-65-4320",
});
console.log(findResult);
```

**Step 3: Run your application.**

To start your application, run the following command from your project
directory:

```bash
mongosh -f quickstart.js
```

**Note:**

If your `mongosh` installation requires you to specify the path to 
your shared library, you can use the following command:

```bash
mongosh --cryptSharedLibPath "<path-to-shared-library>" -f quickstart.js
```

The output of the preceding code sample should look similar to the
following:

```json
{
  "_id": {
    "$oid": "648b384a722cb9b8392df76a"
  },
  "name": "Jon Doe",
  "record": {
    "ssn": "987-65-4320",
    "billing": {
      "type": "Visa",
      "number": "4111111111111111"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "L1NsYItk0Sg+oL66DBj6IYHbX7tveANQyrU2cvMzD9Y=",
        "subType": "00"
      }
    }
  ]
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.


### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Install dependencies.**

Create a directory named `nodeQE` to store your project
files. Run the following commands to navigate into the directory,
initialize your project, and install the required packages:

```bash
cd nodeQE
npm init -y
npm install mongodb-client-encryption dotenv
```

Then, open the generated `package.json` file. To use [ECMAScript modules](https://nodejs.org/api/esm.html#modules-ecmascript-modules),
the standard format for packaging JavaScript code for reuse, replace the
existing line that specifies the `"type"` field with the following line:

```json
"type": "module"
```

**Step 2: Set up your environment variables.**

In your `nodeQE` directory, create a `.env` file. The sample code in 
this tutorial references environment variables that you need to set in 
this `.env` file. Paste the following code into this file:

```text
MONGODB_URI="<Your MongoDB URI>"
SHARED_LIB_PATH="<Full path to your Automatic Encryption Shared Library>"
```

Replace the following placeholder values:

- `<Your MongoDB URI>`: Your MongoDB deployment connection URI.
- `<Full path to your Automatic Encryption Shared Library>`: The
  full path to your Automatic Encryption Shared Library, which resembles the following
  paths:

  - **macOS**: `/<crypt shared directory>/lib/mongo_crypt_v1.dylib`
  - **Linux**: `/<crypt shared directory>/lib/mongo_crypt_v1.so`
  - **Windows**: `C:\<crypt shared directory>\bin\mongo_crypt_v1.dll`

For more information on setting up environment variables, see the 
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/node/README.md)  file included in the 
sample application on GitHub.

**Step 3: Create your main project file.**

In your `nodeQE` directory, create a file named `quickstart.js`.
Paste the following starter code into this file. The placeholder comments
indicate where you will add code in future steps of this tutorial:

```javascript
import "dotenv/config";
import { existsSync, writeFileSync, readFileSync } from "node:fs";
import { randomBytes } from "node:crypto";
import { MongoClient } from "mongodb";
import { ClientEncryption } from "mongodb";

async function runExample() {

  // Paste application variables below

  // Paste code to generate CMK below

  // Paste code to retrieve CMK and specify KMS provider settings below 

  // Paste automatic encryption options code below

  // Paste client configuration code below

  // Paste schema below

  // Paste code to create an encrypted collection below

  // Paste code to insert a document below

  // Paste code to query the document below
}

runExample().catch(console.dir);
```

**Note:** Import ClientEncryption

When using the Node.js driver v6.0 and later, you must import
`ClientEncryption` from `mongodb`. 

For earlier driver versions, import `ClientEncryption` from
`mongodb-client-encryption`.

**Step 4: Assign your application variables.**

Declare the required application variables by pasting the following code into your
`quickstart.js` file under the `// Paste application variables below`
comment. For this tutorial, set the `kmsProviderName` variable to 
`"local"`.

```javascript
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
const kmsProviderName = "<Your KMS Provider Name>";

const uri = process.env.MONGODB_URI; // Your connection URI

const keyVaultDatabaseName = "encryption";
const keyVaultCollectionName = "__keyVault";
const keyVaultNamespace = `${keyVaultDatabaseName}.${keyVaultCollectionName}`;
const encryptedDatabaseName = "medicalRecords";
const encryptedCollectionName = "patients";
```

The following table describes each application variable in the code snippet:

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS used to store your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable. |
| `keyVaultDatabaseName` | The database where DEKs are stored. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection where DEKs are stored. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB where your DEKs are stored. Set this variable to the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database where encrypted data is stored. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection where encrypted data is stored. Set to `"patients"`. |
