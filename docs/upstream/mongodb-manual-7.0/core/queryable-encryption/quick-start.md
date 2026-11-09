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

### Configure Encryption

After you set up your project, follow the steps in this section to create an 
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `quickstart.js` file under the 
`// Paste code to generate CMK below` comment. This code snippet creates 
a 96-byte Customer Master Key and saves it to your filesystem as the
file `customer-master-key.txt`:

```javascript
if (!existsSync("./customer-master-key.txt")) {
  try {
    writeFileSync("customer-master-key.txt", randomBytes(96));
  } catch (err) {
    throw new Error(
      `Unable to write Customer Master Key to file due to the following error: ${err}`
    );
  }
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
const localMasterKey = readFileSync("./customer-master-key.txt");
kmsProviders = {
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
`autoEncryptionOptions` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviders` object, defined in the previous step
- The `sharedLibraryPathOptions` object, which contains the path to
  your Automatic Encryption Shared Library

```javascript
const extraOptions = {
  cryptSharedLibPath: process.env.SHARED_LIB_PATH, // Path to your Automatic Encryption Shared Library
};

const autoEncryptionOptions = {
  keyVaultNamespace,
  kmsProviders,
  extraOptions,
};
```

**Step 4: Create a client to set up an encrypted collection.**

Create a new client to encrypt and decrypt your collection. The client
uses your connection URI and automatic encryption options. Paste the 
following code into your `quickstart.js` file, under the 
`// Paste client configuration code below` comment:

```javascript
const encryptedClient = new MongoClient(uri, {
  autoEncryption: autoEncryptionOptions,
});
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

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `quickstart.js` file, under the
`// Paste code to create an encrypted collection below` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```javascript
const clientEncryption = new ClientEncryption(encryptedClient, autoEncryptionOptions);
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
  encryptedDatabase,
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

const encryptedCollection = encryptedClient
  .db(encryptedDatabaseName)
  .collection(encryptedCollectionName);

const result = await encryptedCollection.insertOne(patientDocument);
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
node quickstart.js
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

Create a directory named `python-qe` to store your project
files. Run the following commands to navigate into the directory
and create a virtual environment:

```bash
cd python-qe
python3 -m venv venv
source venv/bin/activate
```

Then, install the required packages:

```bash
python3 -m pip install pymongo pymongocrypt python-dotenv
```

**Step 2: Set up your environment variables.**

In your `python-qe` directory, create a `.env` file. The sample code 
in this tutorial references environment variables that you need to set in
this `.env` file. Paste the following code into this file:

```text
export MONGODB_URI="<Your MongoDB URI>"
export SHARED_LIB_PATH="<Full path to your Automatic Encryption Shared Library>"
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
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/python/README.md)  file included in the
sample application on GitHub.

**Step 3: Create your main project file.**

In your `python-qe` directory, create a file named `quickstart.py`.
Paste the following starter code into this file. The placeholder comments
indicate where you will add code in future steps of this tutorial:

```python
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.encryption import ClientEncryption
from pymongo.encryption_options import AutoEncryptionOpts
from bson.codec_options import CodecOptions
from bson.binary import STANDARD

load_dotenv()

# Paste application variables below

# Paste code to generate CMK below

# Paste code to retrieve CMK and specify KMS provider settings below

# Paste automatic encryption options code below

# Paste client configuration code below

# Paste schema below

# Paste code to create an encrypted collection below

# Paste code to insert a document below

# Paste code to query the document below
```

**Step 4: Assign your application variables.**

Declare the required application variables by pasting the following code into your
`quickstart.py` file under the `# Paste application variables below`
comment. For this tutorial, set the `kms_provider_name` variable to 
`"local"`.

```python
# KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
kms_provider_name = "<KMS provider name>"
uri = os.environ.get("MONGODB_URI", "mongodb://127.0.0.1:27017")  # Your connection URI
key_vault_database_name = "encryption"
key_vault_collection_name = "__keyVault"
key_vault_namespace = f"{key_vault_database_name}.{key_vault_collection_name}"
encrypted_database_name = "medicalRecords"
encrypted_collection_name = "patients"
```

The following table describes each application variable in the code snippet:

| Variable | Description |
|---|---|
| `kms_provider_name` | The KMS used to store your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable. |
| `key_vault_database_name` | The database where DEKs are stored. Set to `"encryption"`. |
| `key_vault_collection_name` | The collection where DEKs are stored. Set to `"__keyVault"`. |
| `key_vault_namespace` | The namespace in MongoDB where your DEKs are stored. Set this variable to the values of the `key_vault_database_name` and `key_vault_collection_name` variables, separated by a period. |
| `encrypted_database_name` | The database where encrypted data is stored. Set to `"medicalRecords"`. |
| `encrypted_collection_name` | The collection where encrypted data is stored. Set to `"patients"`. |

### Configure Encryption

After you set up your project, follow the steps in this section to create an
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `quickstart.py` file under the
`# Paste code to generate CMK below` comment. This code snippet creates
a 96-byte Customer Master Key and saves it to your filesystem as the
file `customer-master-key.txt`:

```python
path = "customer-master-key.txt"
file_bytes = os.urandom(96)
with open(path, "wb") as f:
    f.write(file_bytes)
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

Paste the following code into your `quickstart.py` file under the
`# Paste code to retrieve CMK and specify KMS provider settings below`
comment to retrieve the contents of the `customer-master-key.txt` file
you generated in the previous step:

```python
path = "./customer-master-key.txt"
with open(path, "rb") as f:
    local_master_key = f.read()
    kms_provider_credentials = {
        "local": {
            "key": local_master_key
        },
    }
```

This code sets the provider name to `local` to use a Local Key Provider
and uses the CMK ({+cmk-long+}) value from your KMS provider settings.

**Step 3: Set your automatic encryption options.**

Add the following code under the
`# Paste automatic encryption options code below` comment to create an
`AutoEncryptionOpts` object that contains the following options:

- The `kms_provider_credentials` object, defined in the previous step
- The namespace of your Key Vault collection
- The path to your Automatic Encryption Shared Library

```python
auto_encryption_options = AutoEncryptionOpts(
    kms_provider_credentials,
    key_vault_namespace,
    crypt_shared_lib_path=os.environ['SHARED_LIB_PATH'] # Path to your Automatic Encryption Shared Library>
)
```

**Step 4: Create a client to set up an encrypted collection.**

Create a new client to encrypt and decrypt your collection. The client
uses your connection URI and automatic encryption options. Paste the
following code into your `quickstart.py` file, under the
`# Paste client configuration code below` comment:

```python
encrypted_client = MongoClient(
    uri, auto_encryption_opts=auto_encryption_options)
```

**Step 5: Specify fields to encrypt.**

To encrypt a field, add it to the encryption schema. To enable queries on a
field, add the `queries` property. Paste the following code under the
`# Paste schema below` comment:

```python
encrypted_fields_map = {
    "fields": [
        {
            "path": "patientRecord.ssn",
            "bsonType": "string",
            "queries": [{"queryType": "equality"}]
        },
        {
            "path": "patientRecord.billing",
            "bsonType": "object",
        }
    ]
}
```

**Note:**

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `quickstart.py` file, under the
`# Paste code to create an encrypted collection below` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```python
client_encryption = ClientEncryption(
    kms_providers=kms_provider_credentials,
    key_vault_namespace=key_vault_namespace,
    key_vault_client=encrypted_client,
    codec_options=CodecOptions(uuid_representation=STANDARD)
)
```

Because you are using a local Customer Master Key, you don't need to provide
Customer Master Key credentials. Create a variable containing an empty object to
use in place of credentials when you create your encrypted collection.

```python
customer_master_key_credentials = {}
```

Create your encrypted collection by using the encryption helper method
accessed through the `ClientEncryption` class. This method automatically
generates data encryption keys for your encrypted fields and creates the
encrypted collection:

```python
client_encryption.create_encrypted_collection(
    encrypted_client[encrypted_database_name],
    encrypted_collection_name,
    encrypted_fields_map,
    kms_provider_name,
    customer_master_key_credentials,
)
```

### Perform Encrypted Operations

After you configure your application and database connection, you can insert
and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

Paste the following code under the
`# Paste code to insert a document below` comment to create a
document that stores patient data and insert it into the `patients`
collection:

```python
patient_document = {
    "patientName": "Jon Doe",
    "patientId": 12345678,
    "patientRecord": {
        "ssn": "987-65-4320",
        "billing": {
            "type": "Visa",
            "number": "4111111111111111",
        },
    },
}

encrypted_collection = encrypted_client[encrypted_database_name][encrypted_collection_name]

result = encrypted_collection.insert_one(patient_document)
```

**Step 2: Query on encrypted data.**

Add the following code to your `quickstart.py` file under the
`# Paste code to query the document below` comment:

```python
find_result = encrypted_collection.find_one({
    "patientRecord.ssn": "987-65-4320"
})

print(find_result)
```

**Step 3: Run your application.**

To start your application, run the following command from your project
directory:

```bash
python3 quickstart.py
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

This tutorial uses Apache Maven to manage dependencies. In an Integrated
Development Environment (IDE), create a new Maven project named 
`JavaQE`. Then, navigate to the `pom.xml` file and add the following 
dependencies:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.mongodb.tutorials</groupId>
  <artifactId>queryable-encryption-tutorial</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
  </properties>

  <dependencies>

    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-driver-sync</artifactId>
      <version>4.10.1</version>
    </dependency>
    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-driver-core</artifactId>
      <version>4.10.1</version>
    </dependency>
    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>bson</artifactId>
      <version>4.10.1</version>
    </dependency>

    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-crypt</artifactId>
      <version>1.8.0</version>
    </dependency>

    <dependency>
      <groupId>io.github.cdimascio</groupId>
      <artifactId>dotenv-java</artifactId>
      <version>3.0.0</version>
    </dependency>

  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-assembly-plugin</artifactId>
        <version>3.6.0</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>single</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <archive>
            <manifest>
              <mainClass>com.mongodb.tutorials.qe.QueryableEncryptionTutorial</mainClass>
              <addClasspath>true</addClasspath>
            </manifest>
          </archive>
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
          </descriptorRefs>
          <appendAssemblyId>false</appendAssemblyId>
          <finalName>${project.artifactId}</finalName>
        </configuration>
      </plugin>
    </plugins>
    <finalName>${project.artifactId}</finalName>
  </build>
</project>
```

This code installs the MongoDB Java Sync Driver and the `mongodb-crypt` 
package, which provides the necessary classes for Queryable Encryption. It also installs
the `dotenv-java` package, which reads your credentials from a `.env`
file.

**Step 2: Set up your environment variables.**

In your `JavaQE` directory, create a file named `.env`. The
sample code in this tutorial reads its configuration from this
file. Paste the following code into this file:

```bash
# MongoDB connection uri and automatic encryption shared library path

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

For more information on setting up your environment variables,
see the [README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/java/README.md) file
included in the sample application on GitHub.

**Step 3: Create your data model classes.**

This tutorial uses Plain Old Java Objects (POJOs) as data models
to represent the document structure. In your
`src/main/java/com/mongodb/tutorials/qe/models` directory,
create a file named `Patient.java` and paste the following `Patient` 
class into the file:

```java
package com.mongodb.tutorials.qe.models;

import org.bson.types.ObjectId;

public class Patient {
    public ObjectId id;
    public String name;

    public PatientRecord patientRecord;

    public Patient() {
    }

    public Patient(String name, PatientRecord patientRecord) {
        this.name = name;
        this.patientRecord = patientRecord;
    }

    public ObjectId getId() {
        return id;
    }

    public void setId(ObjectId id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PatientRecord getPatientRecord() {
        return patientRecord;
    }

    public void setPatientRecord(PatientRecord patientRecord) {
        this.patientRecord = patientRecord;
    }

    @Override
    public String toString() {
        return "{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", patientRecord=" + patientRecord +
                '}';
    }
}
```

Then, create a file named `PatientRecord.java` and paste the following 
`PatientRecord` class into the file:

```java
package com.mongodb.tutorials.qe.models;

public class PatientRecord {
    public String ssn;
    public PatientBilling billing;

    public PatientRecord() {
    }

    public PatientRecord(String ssn, PatientBilling billing) {
        this.ssn = ssn;
        this.billing = billing;
    }

    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }

    public PatientBilling getBilling() {
        return billing;
    }

    public void setBilling(PatientBilling billing) {
        this.billing = billing;
    }

    @Override
    public String toString() {
        return "{" +
                "ssn='" + ssn + '\'' +
                ", billing=" + billing +
                '}';
    }
}
```

Finally, create a file named `PatientBilling.java` and paste the 
following `PatientBilling` class into the file:

```java
package com.mongodb.tutorials.qe.models;

public class PatientBilling {
    public String cardType;
    public String cardNumber;

    public PatientBilling() {
    }

    public PatientBilling(String cardType, String cardNumber) {
        this.cardType = cardType;
        this.cardNumber = cardNumber;
    }

    public String getCardType() {
        return cardType;
    }

    public void setCardType(String cardType) {
        this.cardType = cardType;
    }

    public String getCardNumber() {
        return cardNumber;
    }

    public void setCardNumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    @Override
    public String toString() {
        return "{" +
                "cardType='" + cardType + '\'' +
                ", cardNumber='" + cardNumber + '\'' +
                '}';
    }
}
```

To learn more about Java POJOs, see the [Plain Old Java Object](https://en.wikipedia.org/wiki/Plain_old_Java_object)
Wikipedia article.

**Step 4: Create your application file.**

In your `src/main/java/com/mongodb/tutorials/qe` directory,
create a file named `QueryableEncryptionTutorial.java`. This
file contains the main Queryable Encryption workflow. Paste the following
starter code into this file. The placeholder comments indicate
where you add code in later steps of this tutorial:

```java
package com.mongodb.tutorials.qe;

import com.mongodb.AutoEncryptionSettings;
import com.mongodb.ClientEncryptionSettings;
import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.CreateCollectionOptions;
import com.mongodb.client.model.CreateEncryptedCollectionParams;
import com.mongodb.client.result.InsertOneResult;
import com.mongodb.client.vault.ClientEncryption;
import com.mongodb.client.vault.ClientEncryptions;
import com.mongodb.tutorials.qe.models.Patient;
import com.mongodb.tutorials.qe.models.PatientBilling;
import com.mongodb.tutorials.qe.models.PatientRecord;
import io.github.cdimascio.dotenv.Dotenv;
import org.bson.BsonArray;
import org.bson.BsonDocument;
import org.bson.BsonNull;
import org.bson.BsonString;
import org.bson.codecs.configuration.CodecProvider;
import org.bson.codecs.configuration.CodecRegistry;
import org.bson.codecs.pojo.PojoCodecProvider;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static com.mongodb.MongoClientSettings.getDefaultCodecRegistry;
import static org.bson.codecs.configuration.CodecRegistries.fromProviders;
import static org.bson.codecs.configuration.CodecRegistries.fromRegistries;

public class QueryableEncryptionTutorial {

    // Loads values from your .env file
    // Later steps call getEnv() to read your configuration values
    static class QueryableEncryptionHelpers {
        private static final Dotenv dotEnv = Dotenv.configure()
                .directory("./.env")
                .load();

        public static String getEnv(String name) {
            return dotEnv.get(name);
        }
    }

    static String getEnv(String name) {
        return QueryableEncryptionHelpers.getEnv(name);
    }

    public static void main(String[] args) throws Exception {
        // Paste application variables below

        // Paste code to generate CMK below

        // Paste code to retrieve the CMK and specify KMS provider settings below

        // Paste automatic encryption options code below

        // Paste client settings code below

        try (MongoClient encryptedClient = MongoClients.create(clientSettings)) {

            // Paste schema below

            // Paste code to create an encrypted collection below

            // Paste code to insert a document below

            // Paste code to query the document below

        }
    }
}
```

**Step 5: Assign your application variables.**

The code samples in this tutorial use the following variables to
perform the Queryable Encryption workflow. Paste the following code into the
`main()` method of `QueryableEncryptionTutorial.java`, under
the `// Paste application variables below` comment. For this
tutorial, set the `kmsProviderName` variable to `"local"`:

```java
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
String kmsProviderName = "<KMS provider name>";
String uri = QueryableEncryptionHelpers.getEnv("MONGODB_URI"); // Your connection URI
String keyVaultDatabaseName = "encryption";
String keyVaultCollectionName = "__keyVault";
String keyVaultNamespace = keyVaultDatabaseName + "." + keyVaultCollectionName;
String encryptedDatabaseName = "medicalRecords";
String encryptedCollectionName = "patients";
```

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS that stores your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable in your `.env` file. |
| `keyVaultDatabaseName` | The database that stores your DEKs. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection that stores your DEKs. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB that stores your DEKs. Set this variable to the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database that stores your encrypted data. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection that stores your encrypted data. Set to `"patients"`. |

### Configure Encryption

After you set up your project, follow the steps in this section to
create an encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your
`QueryableEncryptionTutorial.java` file under the
`// Paste code to generate CMK below` comment. This code
creates a 96-byte Customer Master Key and saves it to your filesystem as
the file `customer-master-key.txt`:

```java
// Reuse the key from the customer-master-key.txt file if it exists
if (!new File("./customer-master-key.txt").isFile()) {
    byte[] localCustomerMasterKey = new byte[96];
    new SecureRandom().nextBytes(localCustomerMasterKey);
    try (FileOutputStream stream = new FileOutputStream("customer-master-key.txt")) {
        stream.write(localCustomerMasterKey);
    } catch (Exception e) {
        throw new Exception("Unable to write Customer Master Key file due to the following error:" + e.getMessage());
    }
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

Paste the following code under the ``// Paste code to retrieve
the CMK and specify KMS provider settings below`` comment. This
code retrieves the contents of the `customer-master-key.txt`
file and uses the CMK ({+cmk-long+}) value in your KMS provider
settings. Setting the provider name to `local` indicates that
you are using a Local Key Provider:

```java
byte[] localCustomerMasterKey = new byte[96];

try (FileInputStream fis = new FileInputStream("customer-master-key.txt")) {
    if (fis.read(localCustomerMasterKey) < 96)
        throw new Exception("Expected to read 96 bytes from the customer master key file");
} catch (Exception e) {
    throw new Exception("Unable to read the Customer Master Key due to the following error: " + e.getMessage());
}
Map<String, Object> keyMap = new HashMap<String, Object>();
keyMap.put("key", localCustomerMasterKey);

Map<String, Map<String, Object>> kmsProviderCredentials = new HashMap<String, Map<String, Object>>();
kmsProviderCredentials.put("local", keyMap);
```

**Step 3: Set your automatic encryption options.**

Paste the following code under the ``// Paste automatic
encryption options code below`` comment. This code creates an
`AutoEncryptionSettings` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, defined in the previous
  step
- The `extraOptions` object, which contains the path to your
  Automatic Encryption Shared Library

```java
Map<String, Object> extraOptions = new HashMap<String, Object>();
extraOptions.put("cryptSharedLibPath", getEnv("SHARED_LIB_PATH")); // Path to your Automatic Encryption Shared Library

AutoEncryptionSettings autoEncryptionSettings = AutoEncryptionSettings.builder()
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviderCredentials)
        .extraOptions(extraOptions)
        .build();
```

**Step 4: Create a client to set up an encrypted collection.**

To create a client that encrypts and decrypts data in your
collection, paste the following code under the ``// Paste client
settings code below`` comment. This code builds the
`clientSettings` object from your connection URI and your
automatic encryption options:

```java
MongoClientSettings clientSettings = MongoClientSettings.builder()
        .applyConnectionString(new ConnectionString(uri))
        .autoEncryptionSettings(autoEncryptionSettings)
        .build();
```

The `try` block in your starter code passes these settings to
`MongoClients.create()` to instantiate the encrypted client.

**Step 5: Specify fields to encrypt.**

To encrypt a field, add it to the encryption schema. To enable
queries on a field, add the `queries` property. Paste the
following code under the `// Paste schema below` comment:

```java
BsonDocument encryptedFieldsMap = new BsonDocument().append("fields",
        new BsonArray(Arrays.asList(
                new BsonDocument()
                        .append("keyId", new BsonNull())
                        .append("path", new BsonString("patientRecord.ssn"))
                        .append("bsonType", new BsonString("string"))
                        .append("queries", new BsonDocument()
                                .append("queryType", new BsonString("equality"))),
                new BsonDocument()
                        .append("keyId", new BsonNull())
                        .append("path", new BsonString("patientRecord.billing"))
                        .append("bsonType", new BsonString("object")))));
```

**Note:**

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your
`QueryableEncryptionTutorial.java` file under the ``// Paste
code to create an encrypted collection below`` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the
API for the encryption helper methods:

```java
ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
        .keyVaultMongoClientSettings(MongoClientSettings.builder()
                .applyConnectionString(new ConnectionString(uri))
                .build())
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviderCredentials)
        .build();
ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
```

Because you are using a local Customer Master Key, you don't need to
provide Customer Master Key credentials. Create a variable containing an
empty object to use in place of credentials when you create your
encrypted collection:

```java
BsonDocument customerMasterKeyCredentials = new BsonDocument();
```

Create your encrypted collection by using the 
`createEncryptedCollection()` helper method accessed through the 
`ClientEncryption` class. This method automatically generates data 
encryption keys for your encrypted fields and creates the encrypted 
collection:

```java
CreateCollectionOptions createCollectionOptions = new CreateCollectionOptions().encryptedFields(encryptedFieldsMap);

CreateEncryptedCollectionParams encryptedCollectionParams = new CreateEncryptedCollectionParams(kmsProviderName);
encryptedCollectionParams.masterKey(customerMasterKeyCredentials);

try {
    clientEncryption.createEncryptedCollection(
            encryptedClient.getDatabase(encryptedDatabaseName),
            encryptedCollectionName,
            createCollectionOptions,
            encryptedCollectionParams);
} 
catch (Exception e) {
    throw new Exception("Unable to create encrypted collection due to the following error: " + e.getMessage());
}
```

### Perform Encrypted Operations

After you configure your application and database connection, you can
insert and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

Add the following code blocks under the ``// Paste code to insert
a document below`` comment in the order shown.

First, configure your application to use the POJO classes that
you created:

```java
CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
CodecRegistry pojoCodecRegistry = fromRegistries(getDefaultCodecRegistry(), fromProviders(pojoCodecProvider));
```

Then, create an instance of a `Patient` that describes a
patient's personal information and use the encrypted client to
insert it into the `patients` collection:

```java
MongoDatabase encryptedDb = encryptedClient.getDatabase(encryptedDatabaseName).withCodecRegistry(pojoCodecRegistry);
MongoCollection<Patient> collection = encryptedDb.getCollection(encryptedCollectionName, Patient.class);

PatientBilling patientBilling = new PatientBilling("Visa", "4111111111111111");
PatientRecord patientRecord = new PatientRecord("987-65-4320", patientBilling);
Patient patientDocument = new Patient("Jon Doe", patientRecord);

InsertOneResult result = collection.insertOne(patientDocument);
```

**Step 2: Query on encrypted data.**

Paste the following code under the ``// Paste code to query the
document below`` comment to execute a find query on an encrypted
field and print the decrypted data:

```java
Patient findResult = collection.find(
    new BsonDocument()
            .append("patientRecord.ssn", new BsonString("987-65-4320")))
            .first();

System.out.println(findResult);
```

**Step 3: Compile and run your application.**

To compile and run your application, run the following commands
from your `JavaQE` directory:

```bash
mvn clean package
java -jar target/queryable-encryption-tutorial.jar
```

The driver decrypts the encrypted fields automatically when it
returns the document. The output resembles the following:

```none
{id=648b384a722cb9b8392df76a, name='Jon Doe', patientRecord={ssn='987-65-4320', billing={cardType='Visa', cardNumber='4111111111111111'}, billAmount=1500}}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Install libmongocrypt 1.8.0 or later**

For instructions on how to install `libmongocrypt`, select your 
operating system and the Go driver on the qe-install 
page.

**Step 2: Install dependencies.**

Create a directory named `go-qe` to store your project files. Run the
following commands to navigate into the directory, initialize your
project, and install the required packages:

```bash
cd go-qe
go mod init go-qe
go get go.mongodb.org/mongo-driver/v2/mongo
go get github.com/joho/godotenv
```

**Step 3: Set up your environment variables.**

In your `go-qe` directory, create a `.env` file. The sample code in
this tutorial references environment variables that you need to set in
this `.env` file. Paste the following code into this file:

```bash
# MongoDB replica set connection URI
export MONGODB_URI="<Your MongoDB Connection URI>"

# MongoDB Automatic Encryption Shared Library 
export SHARED_LIB_PATH="<Full path to your Automatic Encryption Shared Library>"
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
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/go/README.md)  file included in the
sample application on GitHub.

**Step 4: Create your data model file.**

This Go tutorial uses structs to represent the document structure. In your ]
`go-qe` directory, create a file named `models.go`
and paste the following code into this file:

```go
package main

/*
	This file contains a sample data model you can use
	to serialize data you store in MongoDB and deserialize
	your retrieved data from MongoDB.
*/

// start-patient-document
type PatientDocument struct {
	PatientName   string        `bson:"patientName"`
	PatientID     int32         `bson:"patientId"`
	PatientRecord PatientRecord `bson:"patientRecord"`
}

// end-patient-document

// start-patient-record
type PatientRecord struct {
	SSN     string      `bson:"ssn"`
	Billing PaymentInfo `bson:"billing"`
}

// end-patient-record

// start-payment-info
type PaymentInfo struct {
	Type   string `bson:"type"`
	Number string `bson:"number"`
}

// end-payment-info
```

**Step 5: Create your main project file.**

In your `go-qe` directory, create a file named `main.go`. Paste the
following starter code into this file. The placeholder comments indicate
where you will add code in future steps of this tutorial:

```go
package main

import (
    "context"
    "crypto/rand"
    "encoding/json"
    "fmt"
    "os"

    "github.com/joho/godotenv"
    "go.mongodb.org/mongo-driver/v2/bson"
    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

func main() {

    if err := godotenv.Load(".env"); err != nil {
        panic("Error loading .env file")
    }

    // Paste application variables below

    // Paste code to generate CMK below

    // Paste code to retrieve CMK and specify KMS provider settings below

    // Paste automatic encryption options code below

    // Paste client configuration code below

    // Paste JSON schema below

    // Paste code to create an encrypted collection below

    // Paste code to insert a document below

    // Paste code to query the document below
}
```

**Step 6: Assign your application variables.**

Declare the required application variables by pasting the following code 
into your `main.go` file under the ``// Paste application variables 
below` comment. For this tutorial, set the `kmsProviderName`` variable to 
`"local"`.

```go
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
kmsProviderName := "<KMS provider name>"
uri := os.Getenv("MONGODB_URI") // Your connection URI
keyVaultDatabaseName := "encryption"
keyVaultCollectionName := "__keyVault"
keyVaultNamespace := keyVaultDatabaseName + "." + keyVaultCollectionName
encryptedDatabaseName := "medicalRecords"
encryptedCollectionName := "patients"
```

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS that stores your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable. |
| `keyVaultDatabaseName` | The database that stores your DEKs. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection that stores your DEKs. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB that stores your DEKs. Set this variable to the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database that stores your encrypted data. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection that stores your encrypted data. Set to `"patients"`. |

### Configure Encryption

After you set up your project, follow the steps in this section to create an
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `main.go` file under the
`// Paste code to generate CMK below` comment. This code snippet creates
a 96-byte Customer Master Key and saves it to your filesystem as the
file `customer-master-key.txt`:

```go
key := make([]byte, 96)
if _, err := rand.Read(key); err != nil {
	panic(fmt.Sprintf("Unable to create a random 96 byte data key: %v\n", err))
}
if err := os.WriteFile("customer-master-key.txt", key, 0644); err != nil {
	panic(fmt.Sprintf("Unable to write key to file: %v\n", err))
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

Paste the following code into your `main.go` file under the
`// Paste code to retrieve CMK and specify KMS provider settings below`
comment to retrieve the contents of the `customer-master-key.txt` file:

```go
key, err := os.ReadFile("customer-master-key.txt")
if err != nil {
	panic(fmt.Sprintf("Could not read the Customer Master Key: %v", err))
}
kmsProviderCredentials := map[string]map[string]interface{}{"local": {"key": key}}
```

This code sets the provider name to `local` to use a Local Key Provider
and uses the CMK ({+cmk-long+}) value from your KMS provider settings.

**Step 3: Set your automatic encryption options.**

Add the following code under the
`// Paste automatic encryption options code below` comment to create an
`AutoEncryption` object that contains the following options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, defined in the previous step
- The `cryptSharedLibraryPath` object, which contains the path to your
  Automatic Encryption Shared Library

```go
cryptSharedLibraryPath := map[string]interface{}{
	"cryptSharedLibPath": os.Getenv("SHARED_LIB_PATH"), // Path to your Automatic Encryption Shared Library
}

autoEncryptionOptions := options.AutoEncryption().
	SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviderCredentials).
	SetExtraOptions(cryptSharedLibraryPath)
```

**Step 4: Create a client to set up an encrypted collection.**

Create a new client to encrypt and decrypt your collection. The client
uses your connection URI and automatic encryption options. Paste the
following code into your `main.go` file, under the
`// Paste client configuration code below` comment:

```go
encryptedClient, err := mongo.Connect(
	context.TODO(),
	options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOptions),
)
if err != nil {
	panic(fmt.Sprintf("Unable to connect to MongoDB: %v\n", err))
}
defer func() {
	_ = encryptedClient.Disconnect(context.TODO())
}()
```

**Step 5: Specify fields to encrypt.**

To encrypt a field, add it to the encryption schema. To enable queries on a
field, add the `queries` property. Paste the following code under the
`// Paste JSON schema below` comment:

```go
encryptedFieldsMap := bson.M{
	"fields": []bson.M{
		bson.M{
			"keyId":    nil,
			"path":     "patientRecord.ssn",
			"bsonType": "string",
			"queries": []bson.M{
				{
					"queryType": "equality",
				},
			},
		},
		bson.M{
			"keyId":    nil,
			"path":     "patientRecord.billing",
			"bsonType": "object",
		},
	},
}
```

**Note:**

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `main.go` file, under the
`// Paste code to create an encrypted collection below` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```go
clientEncryptionOpts := options.ClientEncryption().
	SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviderCredentials)

clientEncryption, err := mongo.NewClientEncryption(encryptedClient, clientEncryptionOpts)
if err != nil {
	panic(fmt.Sprintf("Unable to create a ClientEncryption instance due to the following error: %s\n", err))
}
```

Because you are using a local Customer Master Key, you don't need to provide
Customer Master Key credentials. Create a variable containing an empty object to
use in place of credentials when you create your encrypted collection:

```go
customerMasterKey := map[string]string{}
```

To create your encrypted collection, use the `ClientEncryption` object's 
`CreateEncryptedCollection()` helper method. This method automatically
generates data encryption keys for your encrypted fields and creates the
encrypted collection:

```go
createCollectionOptions := options.CreateCollection().SetEncryptedFields(encryptedFieldsMap)
_, _, err =
	clientEncryption.CreateEncryptedCollection(
		context.TODO(),
		encryptedClient.Database(encryptedDatabaseName),
		encryptedCollectionName,
		createCollectionOptions,
		kmsProviderName,
		customerMasterKey,
	)
```

### Perform Encrypted Operations

After you configure your application and database connection, you can insert
and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

Paste the following code under the
`// Paste code to insert a document below` comment to create a
document that stores patient data and insert it into the `patients`
collection:

```go
patientDocument := &PatientDocument{
	PatientName: "John Doe",
	PatientID:   12345678,
	PatientRecord: PatientRecord{
		SSN: "987-65-4320",
		Billing: PaymentInfo{
			Type:   "Visa",
			Number: "4111111111111111",
		},
	},
}

coll := encryptedClient.Database(encryptedDatabaseName).Collection(encryptedCollectionName)

_, err = coll.InsertOne(context.TODO(), patientDocument)
if err != nil {
	panic(fmt.Sprintf("Unable to insert the patientDocument: %s", err))
}
```

**Step 2: Query on encrypted data.**

Add the following code to your `main.go` file under the
`// Paste code to query the document below` comment:

```go
var findResult PatientDocument
err = coll.FindOne(
	context.TODO(),
	bson.M{"patientRecord.ssn": "987-65-4320"},
).Decode(&findResult)
if err != nil {
	fmt.Print("Unable to find the document\n")
} else {
	output, _ := json.MarshalIndent(findResult, "", "    ")
	fmt.Printf("%s\n", output)
}
```

**Step 3: Compile and run your application.**

To compile and run your application, run the following commands from your 
project directory:

```bash
go build -tags cse 
./go-qe
```

The output of the preceding code sample should look similar to the
following:

```json
{
    "PatientName": "Jon Doe",
    "PatientID": 12345678,
    "PatientRecord": {
        "SSN": "987-65-4320",
        "Billing": {
            "Type": "Visa",
            "Number": "4111111111111111"
        },
        "BillAmount": 1500
    }
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Create your .NET console project.**

Run the following commands to create a new .NET console project in a
directory named `CSharpQE`:

```bash
mkdir CSharpQE && cd CSharpQE
dotnet new console
```

**Step 2: Install dependencies.**

From your `CSharpQE` directory, run the following commands to install 
the MongoDB .NET/C# Driver and required packages:

```bash
dotnet add package MongoDB.Driver
dotnet add package MongoDB.Driver.Encryption
dotnet add package Microsoft.Extensions.Configuration.Json
```

**Step 3: Configure your application settings.**

In your `CSharpQE` directory, create a file named
`appsettings.json`. The sample code in this tutorial reads its
configuration from this file. Paste the following code into this file:

```json
{
    "MongoDbUri": "<Your MongoDB URI>",
    "CryptSharedLibPath": "<Full path to your Automatic Encryption Shared Library>"
}
```

Replace the following placeholder values:

- `<Your MongoDB URI>`: Your MongoDB deployment connection URI.
- `<Full path to your Automatic Encryption Shared Library>`: The
  full path to your Automatic Encryption Shared Library, which resembles the following
  paths:

  - **macOS**: `/<crypt shared directory>/lib/mongo_crypt_v1.dylib`
  - **Linux**: `/<crypt shared directory>/lib/mongo_crypt_v1.so`
  - **Windows**: `C:\<crypt shared directory>\bin\mongo_crypt_v1.dll`

**Tip:** appsettings.json Location

When you run the application, the `appsettings.json` file must be in
the same directory as the compiled executable. Add the following
`ItemGroup` to your `.csproj` file so that the
`CopyToOutputDirectory` setting automatically copies
`appsettings.json` to the output `bin` directory when you build:

```xml
<ItemGroup>
  <None Update="appsettings.json">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup>
```

For more information on setting up your configuration, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/csharp/README.md) file included in the
sample application on GitHub.

**Step 4: Create your data model classes.**

This tutorial uses separate classes as data models to represent the
document structure. In your `CSharpQE` directory, create a file
named `Patient.cs` and paste the following `Patient` class into
the file:

```csharp
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

[BsonIgnoreExtraElements]
public class Patient
{
    public ObjectId Id { get; set; }
    public string Name { get; set; }
    public PatientRecord Record { get; set; }
}
```

Then, create a file named `PatientRecord.cs` and paste the
following `PatientRecord` class into the file:

```csharp
public class PatientRecord
{
    public string Ssn { get; set; }
    public PatientBilling Billing { get; set; }
}
```

Finally, create a file named `PatientBilling.cs` and paste the
following `PatientBilling` class into the file:

```csharp
public class PatientBilling
{
    public string CardType { get; set; }
    public long CardNumber { get; set; }
}
```

**Step 5: Create your main project file.**

Replace the contents of the `Program.cs` file that was
generated in your `CSharpQE` directory with the following
code:

```csharp
﻿namespace QueryableEncryption;

public class Program
{
    public static async Task Main(string[] args)
    {
        await QueryableEncryptionTutorial.RunExample();
    }
}
```

The `Program.cs` file contains your main method, which calls the
code in your other project files to generate encryption keys and
perform encrypted operations.

**Step 6: Create your application file.**

In your `CSharpQE` directory, create a file named
`QueryableEncryptionTutorial.cs`. This file contains the main
Queryable Encryption workflow. Paste the following starter code into this file:

```csharp
using Microsoft.Extensions.Configuration;
using MongoDB.Bson;
using MongoDB.Bson.IO;
using MongoDB.Bson.Serialization.Conventions;
using MongoDB.Driver;
using MongoDB.Driver.Encryption;
using System.Security.Cryptography;

namespace QueryableEncryption;

public static class QueryableEncryptionTutorial
{
   public static async Task RunExample()
   {
      var camelCaseConvention = new ConventionPack { new CamelCaseElementNameConvention() };
      ConventionRegistry.Register("CamelCase", camelCaseConvention, type => true);

      // Paste application variables below

      // The helper code snippets you paste below read configuration
      // from this alias of your appSettings variable
      var _appSettings = appSettings;

      // Paste code to generate CMK below

      // Paste code to retrieve the CMK and specify KMS provider settings below

      // Paste automatic encryption options code below

      // Paste client configuration code below

      // Paste schema below

      // Paste code to create an encrypted collection below

      // Paste code to insert a document below

      // Paste code to query the document below

   }
}
```

The placeholder comments indicate where you add code in later steps
of this tutorial.

**Step 7: Assign your application variables.**

The code samples in this tutorial use the following variables to perform
the Queryable Encryption workflow. Paste the following code into the `RunExample()`
method of `QueryableEncryptionTutorial.cs`, under the
`// Paste application variables below` comment. For this tutorial, set 
the `kmsProviderName` variable to `"local"`.

```csharp
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
const string kmsProviderName = "<your KMS provider name>";
const string keyVaultDatabaseName = "encryption";
const string keyVaultCollectionName = "__keyVault";
var keyVaultNamespace =
    CollectionNamespace.FromFullName($"{keyVaultDatabaseName}.{keyVaultCollectionName}");
const string encryptedDatabaseName = "medicalRecords";
const string encryptedCollectionName = "patients";
var appSettings = new ConfigurationBuilder().AddJsonFile("appsettings.json").Build();
var uri = appSettings["MongoDbUri"];
```

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS that stores your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `keyVaultDatabaseName` | The database that stores your DEKs. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection that stores your DEKs. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB that stores your DEKs. Set this variable to a new `CollectionNamespace` object whose name is the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database that stores your encrypted data. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection that stores your encrypted data. Set to `"patients"`. |
| `uri` | Your MongoDB connection URI. Set with the `MongoDbUri` value in your `appsettings.json` file. |

### Configure Encryption

After you set up your project, follow the steps in this section to create an
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `QueryableEncryptionTutorial.cs` 
file under the `// Paste code to generate CMK below` comment. This code 
creates a 96-byte Customer Master Key and saves it to your filesystem as the 
file `customer-master-key.txt`:

```csharp
// Reuse the key from the customer-master-key.txt file if it exists
if (!File.Exists("customer-master-key.txt"))
{
    using var randomNumberGenerator = RandomNumberGenerator.Create();
    try
    {
        var bytes = new byte[96];
        randomNumberGenerator.GetBytes(bytes);
        var localCustomerMasterKeyBase64 = Convert.ToBase64String(bytes);
        File.WriteAllText("customer-master-key.txt", localCustomerMasterKeyBase64);
    }
    catch (Exception e)
    {
        throw new Exception("Unable to write Customer Master Key file due to the following error: " + e.Message);
    }
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

Paste the following code under the ``// Paste code to retrieve the CMK and 
specify KMS provider settings below`` comment. This code retrieves the 
contents of the `customer-master-key.txt` file:

```csharp
// WARNING: Do not use a local key file in a production application
var kmsProviderCredentials = new Dictionary<string, IReadOnlyDictionary<string, object>>();
try
{
    var localCustomerMasterKeyBase64 = File.ReadAllText("customer-master-key.txt");
    var localCustomerMasterKeyBytes = Convert.FromBase64String(localCustomerMasterKeyBase64);

    var localOptions = new Dictionary<string, object>
    {
        { "key", localCustomerMasterKeyBytes }
    };

    kmsProviderCredentials.Add(kmsProvider, localOptions);
}
catch (Exception e)
{
    throw new Exception("Unable to read the Customer Master Key due to the following error: " + e.Message);
}
```

**Step 3: Set your automatic encryption options.**

Paste the following code under the ``// Paste automatic encryption options 
code below`` comment. This code snippet creates an 
`AutoEncryptionOptions` object that contains the following options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, defined in the previous step
- The `extraOptions` object, which contains the path to your
  Automatic Encryption Shared Library

```csharp
var extraOptions = new Dictionary<string, object>
{
    { "cryptSharedLibPath", _appSettings["CryptSharedLibPath"] } // Path to your Automatic Encryption Shared Library
};

var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace,
    kmsProviderCredentials,
    extraOptions: extraOptions);
```

**Step 4: Create a client to set up an encrypted collection.**

Paste the following code under the ``// Paste client configuration code 
below`` comment.

IMPORTANT: If you are using the .NET/C# driver version 3.0 or 
later, you must add the following code to your application before
you instantiate a new `MongoClient`:

```csharp
MongoClientSettings.Extensions.AddAutoEncryption(); // .NET/C# Driver v3.0 or later only
```

Then, instantiate a new `MongoClient`:

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(uri); 
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;

var encryptedClient = new MongoClient(clientSettings);
```

**Step 5: Specify fields to encrypt.**

To encrypt a field, add the field to the encryption schema. To enable queries 
on a field, add the `queries` property. Paste the following code under 
the `// Paste schema below` comment:

```csharp
var encryptedFields = new BsonDocument
{
    {
        "fields", new BsonArray
        {
            new BsonDocument
            {
                { "keyId", BsonNull.Value },
                { "path", "record.ssn" },
                { "bsonType", "string" },
                { "queries", new BsonDocument("queryType", "equality") }
            },
            new BsonDocument
            {
                { "keyId", BsonNull.Value },
                { "path", "record.billing" },
                { "bsonType", "object" }
            }
        }
    }
};
```

**Note:**

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `QueryableEncryptionTutorial.cs` 
file under the `// Paste code to create an encrypted collection below`
comment in the order shown. 

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```csharp
var clientEncryptionOptions = new ClientEncryptionOptions(
   keyVaultClient: encryptedClient,
   keyVaultNamespace: keyVaultNamespace,
   kmsProviders: kmsProviderCredentials
);
var clientEncryption = new ClientEncryption(clientEncryptionOptions);
```

Because you are using a local Customer Master Key, you don't need to provide
Customer Master Key credentials. Create a variable containing an empty object to
use in place of credentials when you create your encrypted collection:

```csharp
var customerMasterKeyCredentials = new BsonDocument();
```

To create your encrypted collection, use the `ClientEncryption` object's 
`CreateEncryptedCollection()` helper method. This method automatically
generates data encryption keys for your encrypted fields and creates the
encrypted collection:

```csharp
var patientDatabase = encryptedClient.GetDatabase(encryptedDatabaseName);
patientDatabase.DropCollection(encryptedCollectionName); // Ensure the collection is dropped before creating a new one
try
{
    var createCollectionOptions = new CreateCollectionOptions<Patient>
    {
        EncryptedFields = encryptedFields
    };

    clientEncryption.CreateEncryptedCollection(patientDatabase,
        encryptedCollectionName,
        createCollectionOptions,
        kmsProviderName,
        customerMasterKeyCredentials);
}
catch (Exception e)
{
    throw new Exception("Unable to create encrypted collection due to the following error: " + e.Message);
}
```

### Perform Encrypted Operations

After you configure your application and database connection, you can insert
and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

To create a document that stores patient data and insert it into the 
`patients` collection, paste the following code under the 
`// Paste code to insert a document below` comment:

```csharp
var patient = new Patient
{
    Name = "Jon Doe",
    Id = new ObjectId(),
    Record = new PatientRecord
    {
        Ssn = "987-65-4320",
        Billing = new PatientBilling
        {
            CardType = "Visa",
            CardNumber = 4111111111111111
        }
    }
};

var encryptedCollection = encryptedClient.GetDatabase(encryptedDatabaseName).
    GetCollection<Patient>(encryptedCollectionName);

await encryptedCollection.InsertOneAsync(patient);
```

**Step 2: Query on encrypted data.**

Paste the following code under the ``// Paste code to query the document
below`` comment to retrieve an encrypted field value and print the
decrypted data:

```csharp
var ssnFilter = Builders<Patient>.Filter.Eq("patientRecord.ssn", patient.PatientRecord.Ssn);
var findResult = await encryptedCollection.Find(ssnFilter).FirstOrDefaultAsync();

Console.WriteLine(findResult.ToJson(new JsonWriterSettings { Indent = true }));
```

**Step 3: Run your application.**

To run the application, run the following command from your `CSharpQE` 
project directory:

```bash
dotnet run
```

The output of the preceding code sample should look similar to the
following:

```json
{ 
  "_id": {
    "$oid": "6a6281b43201828e23bbe897"
  },
  "patientName": "Jon Doe",
  "patientRecord": {
    "ssn": "987-65-4320",
    "billing": {
      "cardType": "Visa",
      "cardNumber": 4111111111111111 
    },
    "billAmount": 1500
  }
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

In this tutorial, you created an application that automatically
encrypts and decrypts the `ssn` and `billing` fields in your
`patients` collection. Because your application uses an encrypted
client, the query returns the decrypted field values. A client that
is not configured with your encryption keys would see the encrypted
values for those fields instead.

## Learn More

To view a tutorial on production-ready Queryable Encryption with a remote
KMS, see qe-tutorial-automatic-encryption.

To learn how Queryable Encryption works, see
qe-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Learn more about Queryable Encryption components on the
  Reference page.
- Learn how Customer Master Keys and Data Encryption Keys work on the
  qe-reference-keys-key-vaults page.
- See how KMS Providers manage your Queryable Encryption keys on the
  qe-fundamentals-kms-providers page.
