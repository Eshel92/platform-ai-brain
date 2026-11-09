<!-- Converted from core/queryable-encryption/tutorials/explicit-encryption.txt (reStructuredText). Includes are inlined. -->

# Use Explicit Encryption

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

## Procedure

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```javascript
const fs = require("fs");
const crypto = require("crypto");
try {
  fs.writeFileSync("master-key.txt", crypto.randomBytes(96));
} catch (err) {
  console.error(err);
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

**Tip:** Generate a CMK from the Command Line

Use the following command to generate a CMK ({+cmk-long+})
from a Unix shell or PowerShell:

- Unix/macOS shell:

  ```sh
  echo $(head -c 96 /dev/urandom | base64 | tr -d '\n')
  ```

- PowerShell:

  ```none
  $r=[byte[]]::new(64);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);[Convert]::ToBase64String($r)
  ```

Save the output of the preceding command to a file named `customer-master-key.txt`.

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

```javascript
const uri = "<Your Connection String>";
const keyVaultClient = new MongoClient(uri);
await keyVaultClient.connect();
const keyVaultDB = keyVaultClient.db(keyVaultDatabase);
// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
await keyVaultDB.dropDatabase();
const keyVaultColl = keyVaultDB.collection(keyVaultCollection);
await keyVaultColl.createIndex(
  { keyAltNames: 1 },
  {
    unique: true,
    partialFilterExpression: { keyAltNames: { $exists: true } },
  }
);
```

**Step 3: Create your Data Encryption Keys and Encrypted Collection**

a. Read the Customer Master Key and Specify KMS Provider Settings

   Retrieve the contents of the Customer Master Key file that you generated
   in the Create a Customer Master Key step of this guide.

   Use the CMK ({+cmk-long+}) value in your KMS provider settings. The
   client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
   name to `local` to indicate that you are using a
   Local Key Provider.

   ```javascript
   const provider = "local";
   const path = "./master-key.txt";
   // WARNING: Do not use a local key file in a production application
   const localMasterKey = fs.readFileSync(path);
   const kmsProviders = {
     local: {
       key: localMasterKey,
     },
   };
   ```

#. Create your Data Encryption Keys

   Construct a client with your MongoDB connection string and Key Vault collection
   namespace, and create the Data Encryption Keys:

   **Note:** Key Vault Collection Namespace Permissions

   To complete this tutorial, the database user your application uses to connect to 
   MongoDB must have `dbAdmin` permissions on the following namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

   ```javascript
   const clientEnc = new ClientEncryption(keyVaultClient, {
     keyVaultNamespace: keyVaultNamespace,
     kmsProviders: kmsProviders,
   });
   const dek1 = await clientEnc.createDataKey(provider, {
     keyAltNames: ["dataKey1"],
   });
   const dek2 = await clientEnc.createDataKey(provider, {
     keyAltNames: ["dataKey2"],
   });
   ```

#. Create Your Encrypted Collection

   Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

   ```javascript
   const encryptedFieldsMap = {
     [`${secretDB}.${secretCollection}`]: {
       fields: [
         {
           keyId: dek1,
           path: "patientId",
           bsonType: "int",
           queries: { queryType: "equality" },
         },
         {
           keyId: dek2,
           path: "medications",
           bsonType: "array",
         },
       ],
     },
   };
   const extraOptions = {
     cryptSharedLibPath: "<path to FLE Shared Library>",
   };
   const encClient = new MongoClient(uri, {
     autoEncryption: {
       keyVaultNamespace,
       kmsProviders,
       extraOptions,
       encryptedFieldsMap,
     },
   });
   await encClient.connect();
   const newEncDB = encClient.db(secretDB);
   // Drop the encrypted collection in case you created this collection
   // in a previous run of this application.
   await newEncDB.dropDatabase();
   await newEncDB.createCollection(secretCollection);
   console.log("Created encrypted collection!");
   ```

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```javascript
   const eDB = "encryption";
   const eKV = "__keyVault";
   const keyVaultNamespace = `${eDB}.${eKV}`;
   const secretDB = "medicalRecords";
   const secretCollection = "patients";
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

   ```javascript
   const fs = require("fs");
   const path = "./master-key.txt";
   // WARNING: Do not use a local key file in a production application
   const localMasterKey = fs.readFileSync(path);
   const kmsProviders = {
     local: {
       key: localMasterKey,
     },
   };
   ```

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

   ```javascript
   const uri = "<Your MongoDB URI>";
   const unencryptedClient = new MongoClient(uri);
   await unencryptedClient.connect();
   const keyVaultClient = unencryptedClient.db(eDB).collection(eKV);
   const dek1 = await keyVaultClient.findOne({ keyAltNames: "dataKey1" });
   const dek2 = await keyVaultClient.findOne({ keyAltNames: "dataKey2" });
   ```

#. Specify the Path of the Automatic Encryption Shared Library

   ```javascript
   const extraOptions = {
     cryptSharedLibPath: "<path to crypt_shared library>",
   };
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

   ```javascript
   const encryptedClient = new MongoClient(uri, {
     autoEncryption: {
       kmsProviders: kmsProviders,
       keyVaultNamespace: keyVaultNamespace,
       bypassQueryAnalysis: true,
       keyVaultClient: unencryptedClient,
       extraOptions: extraOptions,
     },
   });
   await encryptedClient.connect();
   ```

   **Note:** Automatic Decryption

   We use a `MongoClient` instance with automatic encryption enabled
   to perform automatic decryption.

   To learn more about explicit encryption with automatic decryption,
   see the Fundamentals section. 

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

   ```javascript
   const encryption = new ClientEncryption(unencryptedClient, {
     keyVaultNamespace,
     kmsProviders,
   });
   ```

**Note:** Indexed and Unindexed Algorithms

To learn more about the indexed and unindexed algorithms in
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

```javascript
const patientId = 12345678;
const medications = ["Atorvastatin", "Levothyroxine"];

const indexedInsertPayload = await encryption.encrypt(patientId, {
  algorithm: "Indexed",
  keyId: dek1._id,
  contentionFactor: 1,
});
const unindexedInsertPayload = await encryption.encrypt(medications, {
  algorithm: "Unindexed",
  keyId: dek2._id,
});
const encryptedColl = encryptedClient
  .db(secretDB)
  .collection(secretCollection);
await encryptedColl.insertOne({
  firstName: "Jon",
  patientId: indexedInsertPayload,
  medications: unindexedInsertPayload,
});
```

When you insert a document, your Queryable Encryption enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": {
    "$oid": "6303e36053cc7ec2e6a630bd"
  },
  "firstName": "Jon",
  "patientId": {
    "$binary": {
      "base64": "BxLJUBmg703civqMz8ASsD4QEYeSneOGiiYHfLE77ELEkp1EC/fXPrKCNRQl2mAFddszqDJ0P3znKrq0DVMEvJoU6wa0Ra+U+JjNVr8NtJE+TpTLCannY5Av6iGfLAaiHbM/E8Ftz1YCQsArQwuNp3wIV/GJPLa2662xsyk0wz7F6IRGC3FlnxpN4UIFaHE1M7Y6kEnx3tEy5uJBvU4Sex7I2H0kqHthClH77Q6xHIHc8H9d6upvgnEbkKBCnmc24A2pSG/xZ7LBsV3j5aOboPISuN/lvg==",
      "subType": "06"
    }
  },
  "medications": {
    "$binary": {
      "base64": "BvOsveapfUxiuQxCMSM2fYIEyRlQaSqR+0NxlMarwurBflvoMz1FrSjSGgCVCpK8X+YrilP6Bac99kkaUmRJfjo4savxcjpOfEnUj5bHciPyfQBYmYF4PMLDtTTzGZpPilb9d5KgpIMBXxHi+dIcog==",
      "subType": "06"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "ZLPIpgxzXpHUGrvdIHetwmMagR+mqvuUj5nzXNGf/WM=",
        "subType": "00"
      }
    }
  ]
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

```javascript
const findPayload = await encryption.encrypt(patientId, {
  algorithm: "Indexed",
  keyId: dek1._id,
  queryType: "equality",
  contentionFactor: 1,
});

console.log("Finding a document with manually encrypted field:");
console.log(await encryptedColl.findOne({ patientId: findPayload }));
```

The output of the preceding code snippet should contain the following
document:

```json
{
  "__safeContent__": [
    {
      "Subtype": 0,
      "Data": "LfaIuWm9o30MIGrK7GGUoStJMSNOjRgbxy5q2TPiDes="
    }
  ],
  "_id": "6303a770857952ca5e363fd2",
  "firstName": "Jon",
  "medications": ["Atorvastatin", "Levothyroxine"],
  "patientId": 12345678
}
```

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```python
path = "master-key.txt"
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

**Tip:** Generate a CMK from the Command Line

Use the following command to generate a CMK ({+cmk-long+})
from a Unix shell or PowerShell:

- Unix/macOS shell:

  ```sh
  echo $(head -c 96 /dev/urandom | base64 | tr -d '\n')
  ```

- PowerShell:

  ```none
  $r=[byte[]]::new(64);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);[Convert]::ToBase64String($r)
  ```

Save the output of the preceding command to a file named `customer-master-key.txt`.

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

```python
connection_string = "<your connection string here>"

key_vault_coll = "__keyVault"
key_vault_db = "encryption"
key_vault_namespace = f"{key_vault_db}.{key_vault_coll}"
key_vault_client = MongoClient(connection_string)
# Drop the Key Vault Collection in case you created this collection
# in a previous run of this application.
key_vault_client.drop_database(key_vault_db)

key_vault_client[key_vault_db][key_vault_coll].create_index(
    [("keyAltNames", ASCENDING)],
    unique=True,
    partialFilterExpression={"keyAltNames": {"$exists": True}},
)
```

**Step 3: Create your Data Encryption Keys and Encrypted Collection**

a. Read the Customer Master Key and Specify KMS Provider Settings

   Retrieve the contents of the Customer Master Key file that you generated
   in the Create a Customer Master Key step of this guide.

   Use the CMK ({+cmk-long+}) value in your KMS provider settings. The
   client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
   name to `local` to indicate that you are using a
   Local Key Provider.

   ```python
   provider = "local"
   path = "./master-key.txt"
   # WARNING: Do not use a local key file in a production application
   with open(path, "rb") as f:
       local_master_key = f.read()
   kms_providers = {
       "local": {
           "key": local_master_key  # local_master_key variable from the previous step
       },
   }
   ```

#. Create your Data Encryption Keys

   Construct a client with your MongoDB connection string and Key Vault collection
   namespace, and create the Data Encryption Keys:

   **Note:** Key Vault Collection Namespace Permissions

   To complete this tutorial, the database user your application uses to connect to 
   MongoDB must have `dbAdmin` permissions on the following namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

   ```python
   client = MongoClient(connection_string)
   client_encryption = ClientEncryption(
       kms_providers,  # pass in the kms_providers variable from the previous step
       key_vault_namespace,
       client,
       CodecOptions(uuid_representation=STANDARD),
   )

   data_key_id_1 = client_encryption.create_data_key(provider, key_alt_names=["dataKey1"])
   data_key_id_2 = client_encryption.create_data_key(provider, key_alt_names=["dataKey2"])
   ```

#. Create Your Encrypted Collection

   Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

   ```python
   encrypted_db_name = "medicalRecords"
   encrypted_coll_name = "patients"
   encrypted_fields_map = {
       f"{encrypted_db_name}.{encrypted_coll_name}": {
           "fields": [
               {
                   "keyId": data_key_id_1,
                   "path": "patientId",
                   "bsonType": "int",
                   "queries": {"queryType": "equality"},
               },
               {
                   "keyId": data_key_id_2,
                   "path": "medications",
                   "bsonType": "array",
               },
           ],
       },
   }

   key_vault_namespace = "encryption.__keyVault"

   auto_encryption = AutoEncryptionOpts(
       kms_providers,
       key_vault_namespace,
       encrypted_fields_map=encrypted_fields_map,
       crypt_shared_lib_path="<path to FLE Shared Library>",
   )

   secure_client = MongoClient(connection_string, auto_encryption_opts=auto_encryption)
   # Drop the encrypted collection in case you created this collection
   # in a previous run of this application.
   secure_client.drop_database(encrypted_db_name)
   encrypted_db = secure_client[encrypted_db_name]
   encrypted_db.create_collection(encrypted_coll_name)
   print("Created encrypted collection!")
   ```

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```python
   key_vault_namespace = "encryption.__keyVault"
   key_vault_db_name, key_vault_coll_name = key_vault_namespace.split(".", 1)
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

   ```python
   path = "./master-key.txt"
   with open(path, "rb") as f:
       local_master_key = f.read()

   kms_providers = {
       "local": {
           "key": local_master_key  # local_master_key variable from the previous step
       },
   }
   ```

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

   ```python
   connection_string = "<your connection string here>"
   client = MongoClient(connection_string)
   key_vault = client[key_vault_db_name][key_vault_coll_name]

   data_key_id_1 = key_vault.find_one({"keyAltNames": "dataKey1"})["_id"]
   data_key_id_2 = key_vault.find_one({"keyAltNames": "dataKey2"})["_id"]
   ```

#. Specify the Path of the Automatic Encryption Shared Library

   ```python
   opts = AutoEncryptionOpts(
       kms_providers,
       key_vault.full_name,
       bypass_query_analysis=True,
       key_vault_client=client,
       crypt_shared_lib_path="<path to FLE Shared Library>",
   )
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

   ```python
   encrypted_client = MongoClient(connection_string, auto_encryption_opts=opts)
   db = encrypted_client.medicalRecords
   coll = db.patients
   ```

   **Note:** Automatic Decryption

   We use a `MongoClient` instance with automatic encryption enabled
   to perform automatic decryption.

   To learn more about explicit encryption with automatic decryption,
   see the Fundamentals section. 

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

   ```python
   client_encryption = ClientEncryption(
       kms_providers, key_vault_namespace, client, client.codec_options
   )
   ```

**Note:** Indexed and Unindexed Algorithms

To learn more about the indexed and unindexed algorithms in
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

```python
patientId = 12345678
medications = ["Atorvastatin", "Levothyroxine"]
indexed_insert_payload = client_encryption.encrypt(
    patientId, Algorithm.INDEXED, data_key_id_1, contention_factor=1
)
unindexed_insert_payload = client_encryption.encrypt(
    medications, Algorithm.UNINDEXED, data_key_id_2
)
coll.insert_one(
    {
        "firstName": "Jon",
        "patientId": indexed_insert_payload,
        "medications": unindexed_insert_payload,
    }
)
```

When you insert a document, your Queryable Encryption enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": {
    "$oid": "6303e36053cc7ec2e6a630bd"
  },
  "firstName": "Jon",
  "patientId": {
    "$binary": {
      "base64": "BxLJUBmg703civqMz8ASsD4QEYeSneOGiiYHfLE77ELEkp1EC/fXPrKCNRQl2mAFddszqDJ0P3znKrq0DVMEvJoU6wa0Ra+U+JjNVr8NtJE+TpTLCannY5Av6iGfLAaiHbM/E8Ftz1YCQsArQwuNp3wIV/GJPLa2662xsyk0wz7F6IRGC3FlnxpN4UIFaHE1M7Y6kEnx3tEy5uJBvU4Sex7I2H0kqHthClH77Q6xHIHc8H9d6upvgnEbkKBCnmc24A2pSG/xZ7LBsV3j5aOboPISuN/lvg==",
      "subType": "06"
    }
  },
  "medications": {
    "$binary": {
      "base64": "BvOsveapfUxiuQxCMSM2fYIEyRlQaSqR+0NxlMarwurBflvoMz1FrSjSGgCVCpK8X+YrilP6Bac99kkaUmRJfjo4savxcjpOfEnUj5bHciPyfQBYmYF4PMLDtTTzGZpPilb9d5KgpIMBXxHi+dIcog==",
      "subType": "06"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "ZLPIpgxzXpHUGrvdIHetwmMagR+mqvuUj5nzXNGf/WM=",
        "subType": "00"
      }
    }
  ]
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

```python
find_payload = client_encryption.encrypt(
    patientId,
    Algorithm.INDEXED,
    data_key_id_1,
    query_type=QueryType.EQUALITY,
    contention_factor=1,
)
doc = coll.find_one({"encryptedIndexed": find_payload})
print("\nReturned document:\n")
pprint.pprint(doc)
```

The output of the preceding code snippet should contain the following
document:

```json
{
  "__safeContent__": [
    {
      "Subtype": 0,
      "Data": "LfaIuWm9o30MIGrK7GGUoStJMSNOjRgbxy5q2TPiDes="
    }
  ],
  "_id": "6303a770857952ca5e363fd2",
  "firstName": "Jon",
  "medications": ["Atorvastatin", "Levothyroxine"],
  "patientId": 12345678
}
```

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```java
byte[] localMasterKeyWrite = new byte[96];
new SecureRandom().nextBytes(localMasterKeyWrite);
try (FileOutputStream stream = new FileOutputStream("master-key.txt")) {
    stream.write(localMasterKeyWrite);
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

**Tip:** Generate a CMK from the Command Line

Use the following command to generate a CMK ({+cmk-long+})
from a Unix shell or PowerShell:

- Unix/macOS shell:

  ```sh
  echo $(head -c 96 /dev/urandom | base64 | tr -d '\n')
  ```

- PowerShell:

  ```none
  $r=[byte[]]::new(64);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);[Convert]::ToBase64String($r)
  ```

Save the output of the preceding command to a file named `customer-master-key.txt`.

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

```java
String keyVaultDb = "encryption";
String keyVaultColl = "__keyVault";
MongoClient keyVaultClient = MongoClients.create(connectionString);

String encryptedDbName = "medicalRecords";
String encryptedCollName = "patients";

// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
keyVaultClient.getDatabase(keyVaultDb).getCollection(keyVaultColl).drop();

MongoCollection keyVaultCollection = keyVaultClient.getDatabase(keyVaultDb).getCollection(keyVaultColl);
IndexOptions indexOpts = new IndexOptions().partialFilterExpression(new BsonDocument("keyAltNames", new BsonDocument("$exists", new BsonBoolean(true) ))).unique(true);
keyVaultCollection.createIndex(new BsonDocument("keyAltNames", new BsonInt32(1)), indexOpts);
keyVaultClient.close();
```

**Step 3: Create your Data Encryption Keys and Encrypted Collection**

a. Read the Customer Master Key and Specify KMS Provider Settings

   Retrieve the contents of the Customer Master Key file that you generated
   in the Create a Customer Master Key step of this guide.

   Use the CMK ({+cmk-long+}) value in your KMS provider settings. The
   client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
   name to `local` to indicate that you are using a
   Local Key Provider.

   ```java
   String kmsProvider = "local";
   String path = "master-key.txt";

   byte[] localMasterKeyRead = new byte[96];

   try (FileInputStream fis = new FileInputStream(path)) {
       if (fis.read(localMasterKeyRead) < 96)
           throw new Exception("Expected to read 96 bytes from file");
   }
   Map<String, Object> keyMap = new HashMap<String, Object>();
   keyMap.put("key", localMasterKeyRead);

   Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
   kmsProviders.put("local", keyMap);
   ```

#. Create your Data Encryption Keys

   Construct a client with your MongoDB connection string and Key Vault collection
   namespace, and create the Data Encryption Keys:

   **Note:** Key Vault Collection Namespace Permissions

   To complete this tutorial, the database user your application uses to connect to 
   MongoDB must have `dbAdmin` permissions on the following namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

   ```java
   String keyVaultNamespace = keyVaultDb + "." + keyVaultColl;
   ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
           .keyVaultMongoClientSettings(MongoClientSettings.builder()
                   .applyConnectionString(new ConnectionString(connectionString))
                   .build())
           .keyVaultNamespace(keyVaultNamespace)
           .kmsProviders(kmsProviders)
           .build();
   ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
   List<String> keyAlts1 = new ArrayList<String>();
   keyAlts1.add("dataKey1");
   BsonBinary dataKeyId1 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
           .keyAltNames(keyAlts1));
   List<String> keyAlts2 = new ArrayList<String>();
   keyAlts2.add("dataKey2");
   BsonBinary dataKeyId2 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
           .keyAltNames(keyAlts2));
   ```

#. Create Your Encrypted Collection

   Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

   ```java
   String encryptedNameSpace = encryptedDbName + "." + encryptedCollName;
   BsonDocument encFields = new BsonDocument().append("fields",
           new BsonArray(Arrays.asList(
                   new BsonDocument().append("keyId", dataKeyId1)
                           .append("path", new BsonString("patientId"))
                           .append("bsonType", new BsonString("int"))
                           .append("queries", new BsonDocument().append("queryType", new BsonString("equality"))),
                   new BsonDocument().append("keyId", dataKeyId2)
                           .append("path", new BsonString("medications"))
                           .append("bsonType", new BsonString("array")),
                   )));
   Map<String, BsonDocument> encryptedFieldsMap = new HashMap<String, BsonDocument>();
   encryptedFieldsMap.put(encryptedNameSpace, encFields);

   Map<String, Object> extraOptions = new HashMap<String, Object>();
   extraOptions.put("cryptSharedLibPath", "<path to crypt_shared>");

   MongoClientSettings clientSettings = MongoClientSettings.builder()
           .applyConnectionString(new ConnectionString(connectionString))
           .autoEncryptionSettings(AutoEncryptionSettings.builder()
                   .keyVaultNamespace(keyVaultNamespace)
                   .kmsProviders(kmsProviders)
                   .encryptedFieldsMap(encryptedFieldsMap)
                   .extraOptions(extraOptions)
                   .build())
           .build();
   MongoClient mongoClientSecure = MongoClients.create(clientSettings);
   MongoDatabase encDb = mongoClientSecure.getDatabase(encryptedDbName);
   // Drop the encrypted collection in case you created this collection
   // in a previous run of this application.
   encDb.getCollection(encryptedCollName).drop();
   encDb.createCollection(encryptedCollName);
   ```

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```java
   String db = "medicalRecords";
   String coll = "patients";
   String keyVaultDb = "encryption";
   String keyVaultColl = "__keyVault";
   String keyVaultNamespace = String.format("%1$s.%2$s", keyVaultDb, keyVaultColl);
   String connectionString = "<Your MongoDB URI>";
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

   ```java
   String kmsProvider = "local";
   String path = "master-key.txt";
   byte[] localMasterKeyRead = new byte[96];
   try (FileInputStream fis = new FileInputStream(path)) {
       if (fis.read(localMasterKeyRead) < 96)
           throw new Exception("Expected to read 96 bytes from file");
   }
   Map<String, Object> keyMap = new HashMap<>();
   keyMap.put("key", localMasterKeyRead);
   Map<String, Map<String, Object>> kmsProviders = new HashMap<>();
   kmsProviders.put(kmsProvider, keyMap);
   ```

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

   ```java
   MongoClient client = MongoClients.create(connectionString);
   MongoCollection<Document> keyVaultClient = client.getDatabase(keyVaultDb).getCollection(keyVaultColl);
   BsonBinary dataKeyId1 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey1")).first().get("_id", Binary.class).getData());
   BsonBinary dataKeyId2 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey2")).first().get("_id", Binary.class).getData());
   ```

#. Specify the Path of the Automatic Encryption Shared Library

   ```java
   Map<String, Object> extraOptions = new HashMap<>();
   extraOptions.put("cryptSharedLibPath", "<path to crypt_shared library>");
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

   ```java
   MongoClientSettings clientSettings = MongoClientSettings.builder()
           .applyConnectionString(new ConnectionString(connectionString))
           .autoEncryptionSettings(AutoEncryptionSettings.builder()
                   .keyVaultNamespace(keyVaultNamespace)
                   .kmsProviders(kmsProviders)
                   .extraOptions(extraOptions)
                   .bypassQueryAnalysis(true)
                   .build())
           .build();
   MongoClient mongoClientSecure = MongoClients.create(clientSettings);
   ```

   **Note:** Automatic Decryption

   We use a `MongoClient` instance with automatic encryption enabled
   to perform automatic decryption.

   To learn more about explicit encryption with automatic decryption,
   see the Fundamentals section. 

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

   ```java
   ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
           .keyVaultMongoClientSettings(MongoClientSettings.builder()
                   .applyConnectionString(new ConnectionString(connectionString))
                   .build())
           .keyVaultNamespace(keyVaultNamespace)
           .kmsProviders(kmsProviders)
           .build();
   ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
   ```

**Note:** Indexed and Unindexed Algorithms

To learn more about the indexed and unindexed algorithms in
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

```java
BsonInt32 patientId = new BsonInt32(12345678);
ArrayList<BsonString> medications = new ArrayList<>();
medications.add(new BsonString("Atorvastatin"));
medications.add(new BsonString("Levothyroxine"));
BsonBinary indexedEncrypted = clientEncryption.encrypt(patientId, new EncryptOptions("Indexed").keyId(dataKeyId1).contentionFactor(1L));
BsonBinary unindexedEncrypted = clientEncryption.encrypt(new BsonArray(medications), new EncryptOptions("Unindexed").keyId(dataKeyId2));
MongoCollection<BsonDocument> collection = mongoClientSecure.getDatabase(db).getCollection(coll, BsonDocument.class);
collection.insertOne(new BsonDocument("firstName", new BsonString("Jon")).append("patientId", indexedEncrypted).append("medications", unindexedEncrypted));
```

When you insert a document, your Queryable Encryption enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": {
    "$oid": "6303e36053cc7ec2e6a630bd"
  },
  "firstName": "Jon",
  "patientId": {
    "$binary": {
      "base64": "BxLJUBmg703civqMz8ASsD4QEYeSneOGiiYHfLE77ELEkp1EC/fXPrKCNRQl2mAFddszqDJ0P3znKrq0DVMEvJoU6wa0Ra+U+JjNVr8NtJE+TpTLCannY5Av6iGfLAaiHbM/E8Ftz1YCQsArQwuNp3wIV/GJPLa2662xsyk0wz7F6IRGC3FlnxpN4UIFaHE1M7Y6kEnx3tEy5uJBvU4Sex7I2H0kqHthClH77Q6xHIHc8H9d6upvgnEbkKBCnmc24A2pSG/xZ7LBsV3j5aOboPISuN/lvg==",
      "subType": "06"
    }
  },
  "medications": {
    "$binary": {
      "base64": "BvOsveapfUxiuQxCMSM2fYIEyRlQaSqR+0NxlMarwurBflvoMz1FrSjSGgCVCpK8X+YrilP6Bac99kkaUmRJfjo4savxcjpOfEnUj5bHciPyfQBYmYF4PMLDtTTzGZpPilb9d5KgpIMBXxHi+dIcog==",
      "subType": "06"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "ZLPIpgxzXpHUGrvdIHetwmMagR+mqvuUj5nzXNGf/WM=",
        "subType": "00"
      }
    }
  ]
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

```java
BsonBinary findPayloadEncrypted = clientEncryption.encrypt(patientId, new EncryptOptions("Indexed").keyId(dataKeyId1).queryType("equality").contentionFactor(1L));
BsonDocument result = collection.find(eq("patientId", findPayloadEncrypted)).first();
System.out.println("Finding a document with manually encrypted field: " + result.toJson());
```

The output of the preceding code snippet should contain the following
document:

```json
{
  "__safeContent__": [
    {
      "Subtype": 0,
      "Data": "LfaIuWm9o30MIGrK7GGUoStJMSNOjRgbxy5q2TPiDes="
    }
  ],
  "_id": "6303a770857952ca5e363fd2",
  "firstName": "Jon",
  "medications": ["Atorvastatin", "Levothyroxine"],
  "patientId": 12345678
}
```

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```go
func localMasterKey() []byte {
	key := make([]byte, 96)
	if _, err := rand.Read(key); err != nil {
		log.Fatalf("Unable to create a random 96 byte data key: %v", err)
	}
	if err := ioutil.WriteFile("master-key.txt", key, 0644); err != nil {
		log.Fatalf("Unable to write key to file: %v", err)
	}
	return key
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

**Tip:** Generate a CMK from the Command Line

Use the following command to generate a CMK ({+cmk-long+})
from a Unix shell or PowerShell:

- Unix/macOS shell:

  ```sh
  echo $(head -c 96 /dev/urandom | base64 | tr -d '\n')
  ```

- PowerShell:

  ```none
  $r=[byte[]]::new(64);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);[Convert]::ToBase64String($r)
  ```

Save the output of the preceding command to a file named `customer-master-key.txt`.

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

**Important:**

When building or running the Golang code in this guide using
`go build` or `go run`, always include the `cse` build
constraint to enable Queryable Encryption. See the following shell
command for an example of including the build constraint:

```bash
go run -tags cse make-data-key.go
```

```go
uri := "<Your MongoDB URI>"
keyVaultClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri))
if err != nil {
	return fmt.Errorf("Connect error for regular client: %v", err)
}
defer func() {
	_ = keyVaultClient.Disconnect(context.TODO())
}()

keyVaultDb := "encryption"
keyVaultColl := "__keyVault"
keyVaultNamespace := keyVaultDb + "." + keyVaultColl
keyVaultIndex := mongo.IndexModel{
	Keys: bson.D{{"keyAltNames", 1}},
	Options: options.Index().
		SetUnique(true).
		SetPartialFilterExpression(bson.D{
			{"keyAltNames", bson.D{
				{"$exists", true},
			}},
		}),
}
// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
if err = keyVaultClient.Database(keyVaultDb).Collection(keyVaultColl).Drop(context.TODO()); err != nil {
	log.Fatalf("Collection.Drop error: %v", err)
}
_, err = keyVaultClient.Database(keyVaultDb).Collection(keyVaultColl).Indexes().CreateOne(context.TODO(), keyVaultIndex)
if err != nil {
	panic(err)
}
```

**Step 3: Create your Data Encryption Keys and Encrypted Collection**

a. Read the Customer Master Key and Specify KMS Provider Settings

   Retrieve the contents of the Customer Master Key file that you generated
   in the Create a Customer Master Key step of this guide.

   Use the CMK ({+cmk-long+}) value in your KMS provider settings. The
   client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
   name to `local` to indicate that you are using a
   Local Key Provider.

   ```go
   key, err := ioutil.ReadFile("master-key.txt")
   if err != nil {
   	log.Fatalf("Could not read the key from master-key.txt: %v", err)
   }
   provider := "local"
   kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
   ```

#. Create your Data Encryption Keys

   Construct a client with your MongoDB connection string and Key Vault collection
   namespace, and create the Data Encryption Keys:

   **Note:** Key Vault Collection Namespace Permissions

   To complete this tutorial, the database user your application uses to connect to 
   MongoDB must have `dbAdmin` permissions on the following namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

   ```go
   clientEncryptionOpts := options.ClientEncryption().SetKeyVaultNamespace(keyVaultNamespace).
   	SetKmsProviders(kmsProviders)
   clientEnc, err := mongo.NewClientEncryption(keyVaultClient, clientEncryptionOpts)
   if err != nil {
   	return fmt.Errorf("NewClientEncryption error %v", err)
   }
   defer func() {
   	_ = clientEnc.Close(context.TODO())
   }()
   dataKeyOpts1 := options.DataKey().
   	SetKeyAltNames([]string{"demoDataKey1"})
   dataKeyID1, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts1)
   if err != nil {
   	return fmt.Errorf("create data key error %v", err)
   }
   dataKeyOpts2 := options.DataKey().
   	SetKeyAltNames([]string{"demoDataKey2"})
   dataKeyID2, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts2)
   if err != nil {
   	return fmt.Errorf("create data key error %v", err)
   }
   ```

#. Create Your Encrypted Collection

   Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

   ```go
   dbName := "medicalRecords"
   collName := "patients"
   encNamespace := (dbName + "." + collName)

   encryptedFieldsMap := bson.M{
   	encNamespace: bson.M{
   		"fields": []bson.M{
   			{
   				"path":     "patientId",
   				"bsonType": "int",
   				"keyId":    dataKeyID1,
   				"queries": []bson.M{
   					{
   						"queryType": "equality",
   					},
   				},
   			},
   			{
   				"path":     "medications",
   				"bsonType": "array",
   				"keyId":    dataKeyID2,
   			},
   		},
   	},
   }
   extraOptions := map[string]interface{}{
   	"cryptSharedLibPath": "<Your Crypt Shared lib Path>",
   }

   autoEncryptionOpts := options.AutoEncryption().
   	SetKmsProviders(kmsProviders).
   	SetKeyVaultNamespace(keyVaultNamespace).
   	SetEncryptedFieldsMap(encryptedFieldsMap).
   	SetExtraOptions(extraOptions)
   secureClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOpts))
   if err != nil {
   	return fmt.Errorf("Connect error for encrypted client: %v", err)
   }
   defer func() {
   	_ = secureClient.Disconnect(context.TODO())
   }()
   // Drop the encrypted collection in case you created this collection
   // in a previous run of this application.
   if err = secureClient.Database(dbName).Collection(collName).Drop(context.TODO()); err != nil {
   	log.Fatalf("Collection.Drop error: %v", err)
   }
   err = secureClient.Database(dbName).CreateCollection(context.TODO(), collName)
   if err != nil {
   	return fmt.Errorf("Error creating collection: %v", err)
   }
   ```

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```go
   keyVaultColl := "__keyVault"
   keyVaultDb := "encryption"
   keyVaultNamespace := keyVaultDb + "." + keyVaultColl
   dbName := "medicalRecords"
   collName := "patients"
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

   ```go
   key, err := ioutil.ReadFile("master-key.txt")
   if err != nil {
   	log.Fatalf("Could not read the key from master-key.txt: %v", err)
   }
   kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
   ```

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

   ```go
   uri := "<Your MongoDB URI>"
   regularClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri))
   if err != nil {
   	panic(fmt.Errorf("Client connect error %v", err))
   }
   var foundDoc1 bson.M
   err = regularClient.Database(keyVaultDb).Collection(keyVaultColl).FindOne(context.TODO(), bson.D{{"keyAltNames", "demoDataKey1"}}).Decode(&foundDoc1)
   if err != nil {
   	panic(err)
   }
   var dataKeyID1 = foundDoc1["_id"].(primitive.Binary)
   var foundDoc2 bson.M
   err = regularClient.Database(keyVaultDb).Collection(keyVaultColl).FindOne(context.TODO(), bson.D{{"keyAltNames", "demoDataKey2"}}).Decode(&foundDoc2)
   if err != nil {
   	panic(err)
   }
   var dataKeyID2 = foundDoc2["_id"].(primitive.Binary)
   ```

#. Specify the Path of the Automatic Encryption Shared Library

   ```go
   extraOptions := map[string]interface{}{
   	"cryptSharedLibPath": "<path to crypt_shared library>",
   }
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

   ```go
   autoEncryptionOpts := options.AutoEncryption().
   	SetKmsProviders(kmsProviders).
   	SetKeyVaultNamespace(keyVaultNamespace).
   	SetExtraOptions(extraOptions).
   	SetBypassQueryAnalysis(true)
   secureClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOpts))
   if err != nil {
   	return fmt.Errorf("Connect error for encrypted client: %v", err)
   }
   defer func() {
   	_ = secureClient.Disconnect(context.TODO())
   }()
   var coll = secureClient.Database(dbName).Collection(collName)
   ```

   **Note:** Automatic Decryption

   We use a `MongoClient` instance with automatic encryption enabled
   to perform automatic decryption.

   To learn more about explicit encryption with automatic decryption,
   see the Fundamentals section. 

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

   ```go
   clientEncryptionOpts := options.ClientEncryption().SetKeyVaultNamespace(keyVaultNamespace).SetKmsProviders(kmsProviders)
   clientEnc, err := mongo.NewClientEncryption(regularClient, clientEncryptionOpts)
   if err != nil {
   	panic(fmt.Errorf("NewClientEncryption error %v", err))
   }
   defer func() {
   	_ = clientEnc.Close(context.TODO())
   }()
   ```

**Note:** Indexed and Unindexed Algorithms

To learn more about the indexed and unindexed algorithms in
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

```go
patientIdRawValueType, patientIdRawValueData, err := bson.MarshalValue(12345678)
if err != nil {
	panic(err)
}
patientIdRawValue := bson.RawValue{Type: patientIdRawValueType, Value: patientIdRawValueData}
patientIdEncryptionOpts := options.Encrypt().
	SetAlgorithm("Indexed").
	SetKeyID(dataKeyID1).
	SetContentionFactor(1)
patientIdEncryptedField, err := clientEnc.Encrypt(
	context.TODO(),
	patientIdRawValue,
	patientIdEncryptionOpts)
if err != nil {
	panic(err)
}
medicationsRawValueType, medicationsRawValueData, err := bson.MarshalValue([]string{"Atorvastatin", "Levothyroxine"})
if err != nil {
	panic(err)
}
medicationsRawValue := bson.RawValue{Type: medicationsRawValueType, Value: medicationsRawValueData}
medicationsEncryptionOpts := options.Encrypt().
	SetAlgorithm("Unindexed").
	SetKeyID(dataKeyID2)
medicationsEncryptedField, err := clientEnc.Encrypt(
	context.TODO(),
	medicationsRawValue,
	medicationsEncryptionOpts)
if err != nil {
	panic(err)
}
_, err = coll.InsertOne(
	context.TODO(),
	bson.D{{"firstName", "Jon"}, {"patientId", patientIdEncryptedField}, {"medications", medicationsEncryptedField}})
if err != nil {
	panic(err)
}
```

When you insert a document, your Queryable Encryption enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": {
    "$oid": "6303e36053cc7ec2e6a630bd"
  },
  "firstName": "Jon",
  "patientId": {
    "$binary": {
      "base64": "BxLJUBmg703civqMz8ASsD4QEYeSneOGiiYHfLE77ELEkp1EC/fXPrKCNRQl2mAFddszqDJ0P3znKrq0DVMEvJoU6wa0Ra+U+JjNVr8NtJE+TpTLCannY5Av6iGfLAaiHbM/E8Ftz1YCQsArQwuNp3wIV/GJPLa2662xsyk0wz7F6IRGC3FlnxpN4UIFaHE1M7Y6kEnx3tEy5uJBvU4Sex7I2H0kqHthClH77Q6xHIHc8H9d6upvgnEbkKBCnmc24A2pSG/xZ7LBsV3j5aOboPISuN/lvg==",
      "subType": "06"
    }
  },
  "medications": {
    "$binary": {
      "base64": "BvOsveapfUxiuQxCMSM2fYIEyRlQaSqR+0NxlMarwurBflvoMz1FrSjSGgCVCpK8X+YrilP6Bac99kkaUmRJfjo4savxcjpOfEnUj5bHciPyfQBYmYF4PMLDtTTzGZpPilb9d5KgpIMBXxHi+dIcog==",
      "subType": "06"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "ZLPIpgxzXpHUGrvdIHetwmMagR+mqvuUj5nzXNGf/WM=",
        "subType": "00"
      }
    }
  ]
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

```go
findPayloadRawValueType, findPayloadRawValueData, err := bson.MarshalValue(12345678)
if err != nil {
	panic(err)
}
findPayloadRawValue := bson.RawValue{Type: findPayloadRawValueType, Value: findPayloadRawValueData}
findPayloadEncryptionOpts := options.Encrypt().
	SetAlgorithm("Indexed").
	SetKeyID(dataKeyID1).
	SetQueryType("equality").
	SetContentionFactor(1)
findPayloadEncryptedField, err := clientEnc.Encrypt(
	context.TODO(),
	findPayloadRawValue,
	findPayloadEncryptionOpts)
if err != nil {
	panic(err)
}
var resultSecure bson.M
coll.FindOne(context.TODO(), bson.D{{"firstName", findPayloadEncryptedField}}).Decode(&resultSecure)
if err != nil {
	panic(err)
}
outputSecure, err := json.MarshalIndent(resultSecure, "", "    ")
if err != nil {
	panic(err)
}
fmt.Printf("\nFound document searching on explicitly encrypted field:\n%s\n", outputSecure)
```

The output of the preceding code snippet should contain the following
document:

```json
{
  "__safeContent__": [
    {
      "Subtype": 0,
      "Data": "LfaIuWm9o30MIGrK7GGUoStJMSNOjRgbxy5q2TPiDes="
    }
  ],
  "_id": "6303a770857952ca5e363fd2",
  "firstName": "Jon",
  "medications": ["Atorvastatin", "Levothyroxine"],
  "patientId": 12345678
}
```

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```csharp
using (var randomNumberGenerator = System.Security.Cryptography.RandomNumberGenerator.Create())
{
    var bytes = new byte[96];
    randomNumberGenerator.GetBytes(bytes);
    var localMasterKeyBase64Write = Convert.ToBase64String(bytes);
    File.WriteAllText("master-key.txt", localMasterKeyBase64Write);
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

**Tip:** Generate a CMK from the Command Line

Use the following command to generate a CMK ({+cmk-long+})
from a Unix shell or PowerShell:

- Unix/macOS shell:

  ```sh
  echo $(head -c 96 /dev/urandom | base64 | tr -d '\n')
  ```

- PowerShell:

  ```none
  $r=[byte[]]::new(64);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);[Convert]::ToBase64String($r)
  ```

Save the output of the preceding command to a file named `customer-master-key.txt`.

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

```csharp
var connectionString = "<Your MongoDB URI>";
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
var keyVaultClient = new MongoClient(connectionString);
var indexOptions = new CreateIndexOptions<BsonDocument>
{
    Unique = true,
    PartialFilterExpression = new BsonDocument
        {{"keyAltNames", new BsonDocument {{"$exists", new BsonBoolean(true)}}}}
};
var builder = Builders<BsonDocument>.IndexKeys;
var indexKeysDocument = builder.Ascending("keyAltNames");
var indexModel = new CreateIndexModel<BsonDocument>(indexKeysDocument, indexOptions);
var keyVaultDatabase = keyVaultClient.GetDatabase(keyVaultNamespace.DatabaseNamespace.DatabaseName);
// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
keyVaultDatabase.DropCollection(keyVaultNamespace.CollectionName);
var keyVaultCollection = keyVaultDatabase.GetCollection<BsonDocument>(keyVaultNamespace.CollectionName);
keyVaultCollection.Indexes.CreateOne(indexModel);
```

**Step 3: Create your Data Encryption Keys and Encrypted Collection**

a. Read the Customer Master Key and Specify KMS Provider Settings

   Retrieve the contents of the Customer Master Key file that you generated
   in the Create a Customer Master Key step of this guide.

   Use the CMK ({+cmk-long+}) value in your KMS provider settings. The
   client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
   name to `local` to indicate that you are using a
   Local Key Provider.

   ```csharp
   var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
   const string provider = "local";
   var localMasterKeyBase64Read = File.ReadAllText("master-key.txt");
   var localMasterKeyBytes = Convert.FromBase64String(localMasterKeyBase64Read);
   var localOptions = new Dictionary<string, object>
   {
       {"key", localMasterKeyBytes}
   };
   kmsProviders.Add(provider, localOptions);
   ```

#. Create your Data Encryption Keys

   Construct a client with your MongoDB connection string and Key Vault collection
   namespace, and create the Data Encryption Keys:

   **Note:** Key Vault Collection Namespace Permissions

   To complete this tutorial, the database user your application uses to connect to 
   MongoDB must have `dbAdmin` permissions on the following namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

   ```csharp
   var clientEncryptionOptions = new ClientEncryptionOptions(
       keyVaultClient,
       keyVaultNamespace,
       kmsProviders: kmsProviders
       );
   var clientEncryption = new ClientEncryption(clientEncryptionOptions);
   var dataKeyOptions1 = new DataKeyOptions(alternateKeyNames: new List<string> { "dataKey1" });
   var dataKeyOptions2 = new DataKeyOptions(alternateKeyNames: new List<string> { "dataKey2" });

   BsonBinaryData CreateKeyGetID(DataKeyOptions options)
   {
       var dateKeyGuid = clientEncryption.CreateDataKey(provider, options, CancellationToken.None);
       return new BsonBinaryData(dateKeyGuid, GuidRepresentation.Standard);
   }

   var dataKeyId1 = CreateKeyGetID(dataKeyOptions1);
   var dataKeyId2 = CreateKeyGetID(dataKeyOptions2);
   var dataKeyId3 = CreateKeyGetID(dataKeyOptions3);
   var dataKeyId4 = CreateKeyGetID(dataKeyOptions4);
   ```

#. Create Your Encrypted Collection

   Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

   ```csharp
   var encryptedCollectionNamespace = CollectionNamespace.FromFullName("medicalRecords.patients");
   var encryptedFieldsMap = new Dictionary<string, BsonDocument>
   {
       {
           encryptedCollectionNamespace.FullName, new BsonDocument
           {
               {
                   "fields", new BsonArray
                   {
                       new BsonDocument
                       {
                           {"keyId", dataKeyId1},
                           {"path", new BsonString("patientId")},
                           {"bsonType", new BsonString("int")},
                           {
                               "queries", new BsonDocument
                               {
                                   {"queryType", new BsonString("equality")}
                               }
                           }
                       },
                       new BsonDocument
                       {
                           {"keyId", dataKeyId2},
                           {"path", new BsonString("medications")},
                           {"bsonType", new BsonString("array")},
                       },
                   }
               }
           }
       }
   };

   var extraOptions = new Dictionary<string, object>()
   {
      { "cryptSharedLibPath", "<path to crypt_shared library>" },
   };

   var autoEncryptionOptions = new AutoEncryptionOptions(
       keyVaultNamespace,
       kmsProviders,
       encryptedFieldsMap: encryptedFieldsMap,
       extraOptions: extraOptions);

   var clientSettings = MongoClientSettings.FromConnectionString(connectionString);
   clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
   var secureClient = new MongoClient(clientSettings);
   var encryptedDatabase = secureClient.GetDatabase(encryptedCollectionNamespace.DatabaseNamespace.DatabaseName);
   // Drop the encrypted collection in case you created this collection
   // in a previous run of this application.
   encryptedDatabase.DropCollection(encryptedCollectionNamespace.CollectionName);
   encryptedDatabase.CreateCollection(encryptedCollectionNamespace.CollectionName);
   Console.WriteLine("Created encrypted collection!");
   ```

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```csharp
   var connectionString = "<Your MongoDB URI>";
   var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
   var coll = "patients";
   var db = "medicalRecords";
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

   ```csharp
   var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
   const string provider = "local";
   const string localMasterKeyPath = "master-key.txt";
   var localMasterKeyBase64Read = File.ReadAllText(localMasterKeyPath);
   var localMasterKeyBytes = Convert.FromBase64String(localMasterKeyBase64Read);
   var localOptions = new Dictionary<string, object>
   {
       {"key", localMasterKeyBytes}
   };
   kmsProviders.Add(provider, localOptions);
   ```

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

   ```csharp
   var regularClient = new MongoClient(connectionString);
   var keyVaultCollection = regularClient.GetDatabase(keyVaultNamespace.DatabaseNamespace.DatabaseName)
       .GetCollection<BsonDocument>(keyVaultNamespace.CollectionName);

   Guid GetKeyId(string altName)
   {
       var filter = Builders<BsonDocument>.Filter.Eq<BsonString>("keyAltNames", altName);
       return keyVaultCollection.Find(filter).First<BsonDocument>()["_id"].AsGuid;
   }

   var dataKeyId1 = GetKeyId("dataKey1");
   var dataKeyId2 = GetKeyId("dataKey2");
   ```

#. Specify the Path of the Automatic Encryption Shared Library

   ```csharp
   var extraOptions = new Dictionary<string, object>()
   {
       {"cryptSharedLibPath", "<path to crypt_shared library>"},
   };
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

   ```csharp
   var clientSettings = MongoClientSettings.FromConnectionString(connectionString);
   var autoEncryptionOptions = new AutoEncryptionOptions(
       keyVaultNamespace,
       kmsProviders,
       bypassQueryAnalysis: true,
       extraOptions: extraOptions);
   clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
   var secureClient = new MongoClient(clientSettings);
   var collection = secureClient.GetDatabase(db).GetCollection<BsonDocument>(coll);
   ```

   **Note:** Automatic Decryption

   We use a `MongoClient` instance with automatic encryption enabled
   to perform automatic decryption.

   To learn more about explicit encryption with automatic decryption,
   see the Fundamentals section. 

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

   ```csharp
   var clientEncryptionOptions = new ClientEncryptionOptions(
       keyVaultClient: regularClient,
       keyVaultNamespace: keyVaultNamespace,
       kmsProviders: kmsProviders
       );
   var clientEncryption = new ClientEncryption(clientEncryptionOptions);
   ```

**Note:** Indexed and Unindexed Algorithms

To learn more about the indexed and unindexed algorithms in
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

```csharp
var patientId = 12345678;
var medications = new BsonArray
        {
            new BsonString("Atorvastatin"),
            new BsonString("Levothyroxine")
        };
var indexedEncrypted = clientEncryption.Encrypt(
    patientId,
    new EncryptOptions(algorithm: "Indexed", keyId: dataKeyId1, contentionFactor: 1),
    CancellationToken.None);
var unindexedEncrypted = clientEncryption.Encrypt(
    medications,
    new EncryptOptions(algorithm: "Unindexed", keyId: dataKeyId2),
    CancellationToken.None);
collection.InsertOne(new BsonDocument { { "firstName", "Jon" }, { "patientId", indexedEncrypted }, { "medications", unindexedEncrypted } });
```

When you insert a document, your Queryable Encryption enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": {
    "$oid": "6303e36053cc7ec2e6a630bd"
  },
  "firstName": "Jon",
  "patientId": {
    "$binary": {
      "base64": "BxLJUBmg703civqMz8ASsD4QEYeSneOGiiYHfLE77ELEkp1EC/fXPrKCNRQl2mAFddszqDJ0P3znKrq0DVMEvJoU6wa0Ra+U+JjNVr8NtJE+TpTLCannY5Av6iGfLAaiHbM/E8Ftz1YCQsArQwuNp3wIV/GJPLa2662xsyk0wz7F6IRGC3FlnxpN4UIFaHE1M7Y6kEnx3tEy5uJBvU4Sex7I2H0kqHthClH77Q6xHIHc8H9d6upvgnEbkKBCnmc24A2pSG/xZ7LBsV3j5aOboPISuN/lvg==",
      "subType": "06"
    }
  },
  "medications": {
    "$binary": {
      "base64": "BvOsveapfUxiuQxCMSM2fYIEyRlQaSqR+0NxlMarwurBflvoMz1FrSjSGgCVCpK8X+YrilP6Bac99kkaUmRJfjo4savxcjpOfEnUj5bHciPyfQBYmYF4PMLDtTTzGZpPilb9d5KgpIMBXxHi+dIcog==",
      "subType": "06"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "ZLPIpgxzXpHUGrvdIHetwmMagR+mqvuUj5nzXNGf/WM=",
        "subType": "00"
      }
    }
  ]
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

```csharp
var findPayload = clientEncryption.Encrypt(
    patientId,
    new EncryptOptions(algorithm: "Indexed", keyId: dataKeyId1, queryType: "equality", contentionFactor: 1),
    CancellationToken.None);
var doc = collection.Find(new BsonDocument { { "patientId", findPayload } }).Single();
Console.WriteLine($"Encrypted document: {doc}");
```

The output of the preceding code snippet should contain the following
document:

```json
{
  "__safeContent__": [
    {
      "Subtype": 0,
      "Data": "LfaIuWm9o30MIGrK7GGUoStJMSNOjRgbxy5q2TPiDes="
    }
  ],
  "_id": "6303a770857952ca5e363fd2",
  "firstName": "Jon",
  "medications": ["Atorvastatin", "Levothyroxine"],
  "patientId": 12345678
}
```

## Learn More

To view a tutorial on using Queryable Encryption with a remote
KMS, see qe-tutorial-automatic-encryption.

To learn how Queryable Encryption works, see
qe-fundamentals-manual-encryption.

To learn more about the topics mentioned in this guide, see the
following links:

- qe-reference-keys-key-vaults
- qe-fundamentals-kms-providers
