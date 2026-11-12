<!-- Part 2 of 5 of core/queryable-encryption/quick-start.md (split because the page is big). -->

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
