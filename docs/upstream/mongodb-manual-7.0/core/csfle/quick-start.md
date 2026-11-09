<!-- Converted from core/csfle/quick-start.txt (reStructuredText). Includes are inlined. -->

# CSFLE Quick Start

## Overview

This guide shows you how to encrypt a document with automatic
Client-Side Field Level Encryption (CSFLE) and a MongoDB driver.

After completing this guide, you should have the following knowledge
and software:

- Knowledge of the steps to configure a driver to encrypt fields in a
  document.
- A working, but not production-ready, client application that
  utilizes automatic Client-Side Field Level Encryption.

**Important:** Do Not Use this Application In Production

Since this example application stores an encryption key on your
application's filesystem, you risk unauthorized access to the key or
loss of the key to decrypt your data.

To view a tutorial that demonstrates how to create a production-ready
CSFLE-enabled application, see
csfle-tutorial-automatic-encryption.

## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the csfle-install page.

Select the programming language for which you want to see code examples for
from the Select your language dropdown menu on the right side of
the page.

**See also:** Full Application

To view the complete runnable application code for this tutorial, go to the
following link:

**java-sync:**

[Complete Java Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/local/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/local/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/local/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/local/reader/CSFLE/)

**go:**

[Complete Go Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/local/reader/)

## Procedure

**java-sync:**

```java
// You are viewing the Java synchronous driver code examples.
// Use the dropdown menu to select a different driver.
```

**nodejs:**

```javascript
// You are viewing the Node.js driver code examples.
// Use the dropdown menu to select a different driver.
```

**python:**

```python
# You are viewing the Python driver code examples.
# Use the dropdown menu to select a different driver.
```

**csharp:**

```csharp
// You are viewing the .NET/C# driver code examples.
// Use the dropdown menu to select a different driver.
```

**go:**

```go
// You are viewing the Golang driver code examples.
// Use the dropdown menu to select a different driver.
```

**Important:**

When building or running the Golang code in this guide using 
`go build` or `go run`, always include the `cse` build 
constraint to enable CSFLE. See the following shell
command for an example of including the build constraint:

```bash
go run -tags cse insert-encrypted-document.go
```

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform CSFLE.

Create a 96-byte Customer Master Key and save it in your **Local Key Provider**,
which is your filesystem,
as the file `master-key.txt`:

**shell:**

```javascript
const fs = require("fs");
const crypto = require("crypto");
try {
  fs.writeFileSync("master-key.txt", crypto.randomBytes(96));
} catch (err) {
  console.error(err);
}
```

**python:**

```python
import os

path = "master-key.txt"
file_bytes = os.urandom(96)
with open(path, "wb") as f:
    f.write(file_bytes)
```

**java-sync:**

```java
byte[] localMasterKeyWrite = new byte[96];
new SecureRandom().nextBytes(localMasterKeyWrite);
try (FileOutputStream stream = new FileOutputStream("master-key.txt")) {
    stream.write(localMasterKeyWrite);
}
```

**go:**

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

**csharp:**

```csharp
using (var randomNumberGenerator = System.Security.Cryptography.RandomNumberGenerator.Create())
{
    var bytes = new byte[96];
    randomNumberGenerator.GetBytes(bytes);
    var localMasterKeyBase64Write = Convert.ToBase64String(bytes);
    Console.WriteLine(localMasterKeyBase64Write);
    File.WriteAllText("master-key.txt", localMasterKeyBase64Write);
}
```

**Warning:** Do Not Use the Local Key Provider in Production

The Local Key Provider is an insecure method of storage and is
**not recommended** for production. Instead,
you should store your Customer Master Keys in a remote
Key Management System
(KMS).

To learn how to use a remote KMS in your CSFLE implementation,
see the csfle-tutorial-automatic-encryption guide.

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

**See also:** Complete Code

**java-sync:**

To view the complete code for making a Customer Master Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/local/reader/src/main/java/com/mongodb/csfle/MakeDataKey.java).

**nodejs:**

To view the complete code for making a Customer Master Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/local/reader/make_data_key.js).

**python:**

To view the complete code for making a Customer Master Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/local/reader/make_data_key.py).

**csharp:**

To view the complete code for making a Customer Master Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/local/reader/CSFLE/MakeDataKey.cs).

**go:**

To view the complete code for making a Customer Master Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/local/reader/make-data-key.go).

**Step 2: Create a Unique Index on your Key Vault collection**

Create a partial unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace. This index should have a 
`partialFilterExpression` for documents where `keyAltNames` exists.

Client-Side Field Level Encryption depends on server-enforced uniqueness of key alternate names.

Select the tab corresponding to your preferred MongoDB driver:

**nodejs:**

```javascript
const uri = "<Your Connection String>";
const keyVaultDatabase = "encryption";
const keyVaultCollection = "__keyVault";
const keyVaultNamespace = `${keyVaultDatabase}.${keyVaultCollection}`;
const keyVaultClient = new MongoClient(uri);
await keyVaultClient.connect();
const keyVaultDB = keyVaultClient.db(keyVaultDatabase);
// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
await keyVaultDB.dropDatabase();
// Drop the database storing your encrypted fields as all
// the DEKs encrypting those fields were deleted in the preceding line.
await keyVaultClient.db("medicalRecords").dropDatabase();
const keyVaultColl = keyVaultDB.collection(keyVaultCollection);
await keyVaultColl.createIndex(
  { keyAltNames: 1 },
  {
    unique: true,
    partialFilterExpression: { keyAltNames: { $exists: true } },
  }
);
```

**python:**

```python
connection_string = "<your connection string here>"

key_vault_coll = "__keyVault"
key_vault_db = "encryption"
key_vault_namespace = f"{key_vault_db}.{key_vault_coll}"
key_vault_client = MongoClient(connection_string)
# Drop the Key Vault Collection in case you created this collection
# in a previous run of this application.
key_vault_client.drop_database(key_vault_db)
# Drop the database storing your encrypted fields as all
# the DEKs encrypting those fields were deleted in the preceding line.
key_vault_client["medicalRecords"].drop_collection("patients")
key_vault_client[key_vault_db][key_vault_coll].create_index(
    [("keyAltNames", ASCENDING)],
    unique=True,
    partialFilterExpression={"keyAltNames": {"$exists": True}},
)
```

**java-sync:**

```java
String connectionString = "<Your MongoDB URI>";
String keyVaultDb = "encryption";
String keyVaultColl = "__keyVault";
String keyVaultNamespace = keyVaultDb + "." + keyVaultColl;
MongoClient keyVaultClient = MongoClients.create(connectionString);

// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
keyVaultClient.getDatabase(keyVaultDb).getCollection(keyVaultColl).drop();
// Drop the database storing your encrypted fields as all
// the DEKs encrypting those fields were deleted in the preceding line.
keyVaultClient.getDatabase("medicalRecords").getCollection("patients").drop();

MongoCollection keyVaultCollection = keyVaultClient.getDatabase(keyVaultDb).getCollection(keyVaultColl);
IndexOptions indexOpts = new IndexOptions().partialFilterExpression(new BsonDocument("keyAltNames", new BsonDocument("$exists", new BsonBoolean(true) ))).unique(true);
keyVaultCollection.createIndex(new BsonDocument("keyAltNames", new BsonInt32(1)), indexOpts);
keyVaultClient.close();
```

**go:**

```go
uri := "<Your MongoDB URI>"
keyVaultClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri))
if err != nil {
	return fmt.Errorf("Connect error for regular client: %v", err)
}
defer func() {
	_ = keyVaultClient.Disconnect(context.TODO())
}()

keyVaultColl := "__keyVault"
keyVaultDb := "encryption"
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
// Drop the database storing your encrypted fields as all
// the DEKs encrypting those fields were deleted in the preceding line.
if err = keyVaultClient.Database("medicalRecords").Collection("patients").Drop(context.TODO()); err != nil {
	log.Fatalf("Collection.Drop error: %v", err)
}
_, err = keyVaultClient.Database(keyVaultDb).Collection(keyVaultColl).Indexes().CreateOne(context.TODO(), keyVaultIndex)
if err != nil {
	panic(err)
}
```

**csharp:**

```csharp
var connectionString = "<Your MongoDB URI>";
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
var keyVaultClient = new MongoClient(connectionString);
var indexOptions = new CreateIndexOptions<BsonDocument>();
indexOptions.Unique = true;
indexOptions.PartialFilterExpression = new BsonDocument { { "keyAltNames", new BsonDocument { { "$exists", new BsonBoolean(true) } } } };
var builder = Builders<BsonDocument>.IndexKeys;
var indexKeysDocument = builder.Ascending("keyAltNames");
var indexModel = new CreateIndexModel<BsonDocument>(indexKeysDocument, indexOptions);
var keyVaultDatabase = keyVaultClient.GetDatabase(keyVaultNamespace.DatabaseNamespace.ToString());
// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.  
keyVaultDatabase.DropCollection(keyVaultNamespace.CollectionName);
// Drop the database storing your encrypted fields as all
// the DEKs encrypting those fields were deleted in the preceding line.
keyVaultClient.GetDatabase("medicalRecords").DropCollection("patients");
var keyVaultCollection = keyVaultDatabase.GetCollection<BsonDocument>(keyVaultNamespace.CollectionName.ToString());
keyVaultCollection.Indexes.CreateOne(indexModel);
```

**Step 3: Create a Data Encryption Key**

**Step 1: Read the Customer Master Key and Specify KMS Provider Settings**

Retrieve the contents of the Customer Master Key file that you generated
in the Create a Customer Master Key step of this guide.

Pass the CMK ({+cmk-long+}) value to your KMS provider settings. The
client uses these settings to discover the CMK ({+cmk-long+}). As
you are using the Local Key Provider, set the provider name to
`local`.

**java-sync:**

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

**nodejs:**

```javascript
const provider = "local";
const path = "./master-key.txt";
const localMasterKey = fs.readFileSync(path);
const kmsProviders = {
  local: {
    key: localMasterKey,
  },
};
```

**python:**

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

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var provider = "local";
string localMasterKeyBase64Read = File.ReadAllText("master-key.txt");
var localMasterKeyBytes = Convert.FromBase64String(localMasterKeyBase64Read);
var localOptions = new Dictionary<string, object>
{
    { "key", localMasterKeyBytes }
};
kmsProviders.Add("local", localOptions);
```

**go:**

```go
key, err := ioutil.ReadFile("master-key.txt")
if err != nil {
	log.Fatalf("Could not read the key from master-key.txt: %v", err)
}
provider := "local"
kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
```

**Step 2: Create a Data Encryption Key**

Construct a client with your MongoDB connection string and Key Vault collection
namespace, and create a Data Encryption Key:

**Note:** Key Vault Collection Namespace Permissions

To complete this tutorial, the database user your application uses to connect to 
MongoDB must have `dbAdmin` permissions on the following namespaces:

- `encryption.__keyVault`
- `medicalRecords` database

**go:**

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
dataKeyOpts := options.DataKey()

dataKeyID, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts)
if err != nil {
	return fmt.Errorf("create data key error %v", err)
}

fmt.Printf("DataKeyId [base64]: %s\n", base64.StdEncoding.EncodeToString(dataKeyID.Data))
```

**java-sync:**

```java
ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
        .keyVaultMongoClientSettings(MongoClientSettings.builder()
                .applyConnectionString(new ConnectionString(connectionString))
                .build())
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviders)
        .build();

MongoClient regularClient = MongoClients.create(connectionString);

ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
BsonBinary dataKeyId = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions());
String base64DataKeyId = Base64.getEncoder().encodeToString(dataKeyId.getData());
System.out.println("DataKeyId [base64]: " + base64DataKeyId);
clientEncryption.close();
```

**nodejs:**

```javascript
const client = new MongoClient(uri);
await client.connect();

const encryption = new ClientEncryption(client, {
  keyVaultNamespace,
  kmsProviders,
});
const key = await encryption.createDataKey(provider);
console.log("DataKeyId [base64]: ", key.toString("base64"));
await keyVaultClient.close();
await client.close();
```

**Note:** Import ClientEncryption

When using the Node.js driver v6.0 and later, you must import
`ClientEncryption` from `mongodb`. 

For earlier driver versions, import `ClientEncryption` from
`mongodb-client-encryption`.

**python:**

```python
key_vault_database = "encryption"
key_vault_collection = "__keyVault"
key_vault_namespace = f"{key_vault_database}.{key_vault_collection}"

client = MongoClient(connection_string)
client_encryption = ClientEncryption(
    kms_providers,  # pass in the kms_providers variable from the previous step
    key_vault_namespace,
    client,
    CodecOptions(uuid_representation=STANDARD),
)
data_key_id = client_encryption.create_data_key("local")

base_64_data_key_id = base64.b64encode(data_key_id)
print("DataKeyId [base64]: ", base_64_data_key_id)
```

**csharp:**

```csharp
var clientEncryptionOptions = new ClientEncryptionOptions(
    keyVaultClient: keyVaultClient,
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders
    );

var clientEncryption = new ClientEncryption(clientEncryptionOptions);
var dataKeyOptions = new DataKeyOptions();
var dataKeyId = clientEncryption.CreateDataKey(provider, dataKeyOptions, CancellationToken.None);
var dataKeyIdBase64 = Convert.ToBase64String(GuidConverter.ToBytes(dataKeyId, GuidRepresentation.Standard));
Console.WriteLine($"DataKeyId [base64]: {dataKeyIdBase64}");
```

The output from the code above should resemble the following:

```none
DataKeyId [base64]: 3k13WkSZSLy7kwAAP4HDyQ==
```

**See also:** Complete Code

**java-sync:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/local/reader/src/main/java/com/mongodb/csfle/MakeDataKey.java).

**nodejs:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/local/reader/make_data_key.js).

**python:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/local/reader/make_data_key.py).

**csharp:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/local/reader/CSFLE/MakeDataKey.cs).

**go:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/local/reader/make-data-key.go).

**Step 3: Configure the MongoClient**

**Step 1: Specify the Key Vault Collection Namespace**

Specify `encryption.__keyVault` as the Key Vault collection
namespace.

**java-sync:**

```java
String keyVaultNamespace = "encryption.__keyVault";
```

**nodejs:**

```javascript
const keyVaultNamespace = "encryption.__keyVault";
```

**python:**

```python
key_vault_namespace = "encryption.__keyVault"
```

**csharp:**

```csharp
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
```

**go:**

```go
keyVaultNamespace := "encryption.__keyVault"
```

**Step 2: Specify the Local Customer Master Key**

Specify the KMS provider and specify your key inline:

**java-sync:**

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

**nodejs:**

```javascript
const fs = require("fs");
const provider = "local";
const path = "./master-key.txt";
const localMasterKey = fs.readFileSync(path);
const kmsProviders = {
  local: {
    key: localMasterKey,
  },
};
```

**python:**

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

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var provider = "local";
var localMasterKeyPath = "master-key.txt";
string localMasterKeyBase64Read = File.ReadAllText(localMasterKeyPath);
var localMasterKeyBytes = Convert.FromBase64String(localMasterKeyBase64Read);
var localOptions = new Dictionary<string, object>
{
    { "key", localMasterKeyBytes }
};
kmsProviders.Add(provider, localOptions);
```

**go:**

```go
key, err := ioutil.ReadFile("master-key.txt")
if err != nil {
	log.Fatalf("Could not read the key from master-key.txt: %v", err)
}
kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
```

**Step 3: Create an Encryption Schema For Your Collection**

**Tip:** Add Your Data Encryption Key Base64 ID

Make sure to update the following code to include your Base64
DEK ({+dek-long+}) ID. You received this value in the
Generate your Data Encryption Key step of this
guide.

**java-sync:**

```java
String dekId = "<paste-base-64-encoded-data-encryption-key-id>>";
Document jsonSchema = new Document().append("bsonType", "object").append("encryptMetadata",
        new Document().append("keyId", new ArrayList<>((Arrays.asList(new Document().append("$binary", new Document()
                .append("base64", dekId)
                .append("subType", "04")))))))
        .append("properties", new Document()
                .append("ssn", new Document().append("encrypt", new Document()
                        .append("bsonType", "int")
                        .append("algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic")))
                .append("bloodType", new Document().append("encrypt", new Document()
                        .append("bsonType", "string")
                        .append("algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Random")))
                .append("medicalRecords", new Document().append("encrypt", new Document()
                        .append("bsonType", "array")
                        .append("algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Random")))
                .append("insurance", new Document()
                        .append("bsonType", "object")
                        .append("properties",
                                new Document().append("policyNumber", new Document().append("encrypt", new Document()
                                        .append("bsonType", "int")
                                        .append("algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"))))));
HashMap<String, BsonDocument> schemaMap = new HashMap<String, BsonDocument>();
schemaMap.put("medicalRecords.patients", BsonDocument.parse(jsonSchema.toJson()));
```

**nodejs:**

```javascript
dataKey = "<Your base64 DEK ID>";
const schema = {
  bsonType: "object",
  encryptMetadata: {
    keyId: [new Binary(Buffer.from(dataKey, "base64"), 4)],
  },
  properties: {
    insurance: {
      bsonType: "object",
      properties: {
        policyNumber: {
          encrypt: {
            bsonType: "int",
            algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
          },
        },
      },
    },
    medicalRecords: {
      encrypt: {
        bsonType: "array",
        algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
      },
    },
    bloodType: {
      encrypt: {
        bsonType: "string",
        algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
      },
    },
    ssn: {
      encrypt: {
        bsonType: "int",
        algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
      },
    },
  },
};

var patientSchema = {};
patientSchema[namespace] = schema;
```

**python:**

```python
dek_id = b"<paste-base-64-encoded-data-encryption-key-id>"
json_schema = {
    "bsonType": "object",
    "encryptMetadata": {"keyId": [Binary(base64.b64decode(dek_id), UUID_SUBTYPE)]},
    "properties": {
        "insurance": {
            "bsonType": "object",
            "properties": {
                "policyNumber": {
                    "encrypt": {
                        "bsonType": "int",
                        "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
                    }
                }
            },
        },
        "medicalRecords": {
            "encrypt": {
                "bsonType": "array",
                "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
            }
        },
        "bloodType": {
            "encrypt": {
                "bsonType": "string",
                "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
            }
        },
        "ssn": {
            "encrypt": {
                "bsonType": "int",
                "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
            }
        },
    },
}

patient_schema = {"medicalRecords.patients": json_schema}
```

**csharp:**

```csharp
var keyId = "<Your base64 DEK ID here>";
var schema = new BsonDocument
{
   { "bsonType", "object" },
   {
       "encryptMetadata",
       new BsonDocument("keyId", new BsonArray(new[] { new BsonBinaryData(Convert.FromBase64String(keyId), BsonBinarySubType.UuidStandard) }))
   },
   {
       "properties",
       new BsonDocument
       {
           {
               "ssn", new BsonDocument
               {
                   {
                       "encrypt", new BsonDocument
                       {
                           { "bsonType", "int" },
                           { "algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic" }
                       }
                   }
               }
           },
           {
               "bloodType", new BsonDocument
               {
                   {
                       "encrypt", new BsonDocument
                       {
                           { "bsonType", "string" },
                           { "algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Random" }
                       }
                   }
               }
           },
           {
               "medicalRecords", new BsonDocument
               {
                   {
                       "encrypt", new BsonDocument
                       {
                           { "bsonType", "array" },
                           { "algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Random" }
                       }
                   }
               }
           },
           {
               "insurance", new BsonDocument
               {
                   { "bsonType", "object" },
                   {
                       "properties", new BsonDocument
                       {
                           {
                               "policyNumber", new BsonDocument
                               {
                                   {
                                       "encrypt", new BsonDocument
                                       {
                                           { "bsonType", "int" },
                                           { "algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic" }
                                       }
                                   }
                               }
                           }
                       }
                   }
               }
           }
       }
   }
};
var schemaMap = new Dictionary<string, BsonDocument>();
schemaMap.Add(dbNamespace, schema);
```

**go:**

```go
dek_id := "<Your Base64 DEK ID>"
schema_template := `{
	"bsonType": "object",
	"encryptMetadata": {
		"keyId": [
			{
				"$binary": {
					"base64": "%s",
					"subType": "04"
				}
			}
		]
	},
	"properties": {
		"insurance": {
			"bsonType": "object",
			"properties": {
				"policyNumber": {
					"encrypt": {
						"bsonType": "int",
						"algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
					}
				}
			}
		},
		"medicalRecords": {
			"encrypt": {
				"bsonType": "array",
				"algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
			}
		},
		"bloodType": {
			"encrypt": {
				"bsonType": "string",
				"algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
			}
		},
		"ssn": {
			"encrypt": {
				"bsonType": "int",
				"algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
			}
		}
	}
}`
schema := fmt.Sprintf(schema_template, dek_id)
var schemaDoc bson.Raw
if err := bson.UnmarshalExtJSON([]byte(schema), true, &schemaDoc); err != nil {
	return fmt.Errorf("UnmarshalExtJSON error: %v", err)
}
schemaMap := map[string]interface{}{
	dbName + "." + collName: schemaDoc,
}
```

**Step 4: Specify the Location of the Automatic Encryption Shared Library**

**java-sync:**

```java
Map<String, Object> extraOptions = new HashMap<String, Object>();
extraOptions.put("cryptSharedLibPath", "<Full path to your Automatic Encryption Shared Library>"));
```

**nodejs:**

```javascript
const extraOptions = {
  cryptSharedLibPath: "<Full path to your Automatic Encryption Shared Library>",
};
```

**python:**

```python
extra_options = {
    "cryptSharedLibPath": "<Full path to your Automatic Encryption Shared Library>"
}
```

**csharp:**

```csharp
var mongoBinariesPath = "<Full path to your Automatic Encryption Shared Library>";
var extraOptions = new Dictionary<string, object>()
{
   { "cryptSharedLibPath", mongoBinariesPath },
};
```

**go:**

```go
extraOptions := map[string]interface{}{
	"cryptSharedLibPath": "<Full path to your Automatic Encryption Shared Library>",
}
```

**Note:** Automatic Encryption Options

The automatic encryption options provide configuration
information to the Automatic Encryption Shared Library,
which modifies the application's behavior when accessing encrypted fields.

To learn more about the Automatic Encryption Shared Library, see
the csfle-reference-shared-library page.

**Step 5: Create the MongoClient**

Instantiate a MongoDB client object with the following
automatic encryption settings:

**java-sync:**

```java
MongoClientSettings clientSettings = MongoClientSettings.builder()
    .applyConnectionString(new ConnectionString(connectionString))
    .autoEncryptionSettings(AutoEncryptionSettings.builder()
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviders)
        .schemaMap(schemaMap)
        .extraOptions(extraOptions)
        .build())
    .build();

MongoClient mongoClientSecure = MongoClients.create(clientSettings);
```

**nodejs:**

```javascript
const secureClient = new MongoClient(connectionString, {
  autoEncryption: {
    keyVaultNamespace,
    kmsProviders,
    schemaMap: patientSchema,
    extraOptions: extraOptions,
  },
});
```

**python:**

```python
fle_opts = AutoEncryptionOpts(
    kms_providers, key_vault_namespace, schema_map=patient_schema, **extra_options
)
secureClient = MongoClient(connection_string, auto_encryption_opts=fle_opts)
```

**csharp:**

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(connectionString);
var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders,
    schemaMap: schemaMap,
    extraOptions: extraOptions
    );
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
var secureClient = new MongoClient(clientSettings);
```

**go:**

```go
autoEncryptionOpts := options.AutoEncryption().
	SetKmsProviders(kmsProviders).
	SetKeyVaultNamespace(keyVaultNamespace).
	SetSchemaMap(schemaMap).
	SetExtraOptions(extraOptions)
secureClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOpts))
if err != nil {
	return fmt.Errorf("Connect error for encrypted client: %v", err)
}
defer func() {
	_ = secureClient.Disconnect(context.TODO())
}()
```

**Step 6: Insert a Document with Encrypted Fields**

Use your CSFLE-enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

**java-sync:**

```java
ArrayList<Document> medicalRecords = new ArrayList<>();
medicalRecords.add(new Document().append("weight", "180"));
medicalRecords.add(new Document().append("bloodPressure", "120/80"));

Document insurance = new Document()
.append("policyNumber", 123142)
.append("provider",  "MaestCare");

Document patient = new Document()
    .append("name", "Jon Doe")
    .append("ssn", 241014209)
    .append("bloodType", "AB+")
    .append("medicalRecords", medicalRecords)
    .append("insurance", insurance);
mongoClientSecure.getDatabase(recordsDb).getCollection(recordsColl).insertOne(patient);
```

**nodejs:**

```javascript
try {
  const writeResult = await secureClient
    .db(db)
    .collection(coll)
    .insertOne({
      name: "Jon Doe",
      ssn: 241014209,
      bloodType: "AB+",
      medicalRecords: [{ weight: 180, bloodPressure: "120/80" }],
      insurance: {
        policyNumber: 123142,
        provider: "MaestCare",
      },
    });
} catch (writeError) {
  console.error("writeError occurred:", writeError);
}
```

**python:**

```python
def insert_patient(
    collection, name, ssn, blood_type, medical_records, policy_number, provider
):
    insurance = {"policyNumber": policy_number, "provider": provider}
    doc = {
        "name": name,
        "ssn": ssn,
        "bloodType": blood_type,
        "medicalRecords": medical_records,
        "insurance": insurance,
    }
    collection.insert_one(doc)

medical_record = [{"weight": 180, "bloodPressure": "120/80"}]
insert_patient(
    secureClient.medicalRecords.patients,
    "Jon Doe",
    241014209,
    "AB+",
    medical_record,
    123142,
    "MaestCare",
)
```

**csharp:**

```csharp
var sampleDocFields = new BsonDocument
{
    { "name", "Jon Doe" },
    { "ssn", 145014000 },
    { "bloodType", "AB-" },
    {
        "medicalRecords", new BsonArray
        {
            new BsonDocument("weight", 180),
            new BsonDocument("bloodPressure", "120/80")
        }
    },
    {
        "insurance", new BsonDocument
        {
            { "policyNumber", 123142 },
            { "provider", "MaestCare" }
        }
    }
};

// Construct an auto-encrypting client
var secureCollection = secureClient.GetDatabase(db).GetCollection<BsonDocument>(coll);

// Insert a document into the collection
secureCollection.InsertOne(sampleDocFields);
```

**go:**

```go
test_patient := map[string]interface{}{
	"name":      "Jon Doe",
	"ssn":       241014209,
	"bloodType": "AB+",
	"medicalRecords": []map[string]interface{}{{
		"weight":        180,
		"bloodPressure": "120/80",
	}},
	"insurance": map[string]interface{}{
		"provider":     "MaestCare",
		"policyNumber": 123142,
	},
}
if _, err := secureClient.Database(dbName).Collection(collName).InsertOne(context.TODO(), test_patient); err != nil {
	return fmt.Errorf("InsertOne error: %v", err)
}
```

**Note:**

Rather than creating a raw BSON document, you can pass a struct with `bson` tags directly
to the driver for encoding.

When you insert a document, your CSFLE-enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": { "$oid": "<_id of your document>" },
  "name": "Jon Doe",
  "ssn": {
    "$binary": "<cipher-text>",
    "$type": "6"
  },
  "bloodType": {
    "$binary": "<cipher-text>",
    "$type": "6"
  },
  "medicalRecords": {
    "$binary": "<cipher-text>",
    "$type": "6"
  },
  "insurance": {
    "provider": "MaestCare",
    "policyNumber": {
      "$binary": "<cipher-text>",
      "$type": "6"
    }
  }
}
```

**See also:** Complete Code

**java-sync:**

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/local/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

**nodejs:**

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/local/reader/insert_encrypted_document.js).

**python:**

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/local/reader/insert_encrypted_document.py).

**csharp:**

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/local/reader/CSFLE/InsertEncryptedDocument.cs)

**go:**

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/local/reader/insert-encrypted-document.go).

**Step 7: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide.

To show the functionality of CSFLE, the following code snippet queries for
your document with a client configured for automatic CSFLE as well as
a client that is not configured for automatic CSFLE.

**java-sync:**

```java
System.out.println("Finding a document with regular (non-encrypted) client.");
Document docRegular = mongoClientRegular.getDatabase(recordsDb).getCollection(recordsColl).find(eq("name", "Jon Doe")).first();
System.out.println(docRegular.toJson());

System.out.println("Finding a document with encrypted client, searching on an encrypted field");
Document docSecure = mongoClientSecure.getDatabase(recordsDb).getCollection(recordsColl).find(eq("ssn", 241014209)).first();
System.out.println(docSecure.toJson());
```

**nodejs:**

```javascript
console.log("Finding a document with regular (non-encrypted) client.");
console.log(
  await regularClient.db(db).collection(coll).findOne({ name: /Jon/ })
);

console.log(
  "Finding a document with encrypted client, searching on an encrypted field"
);
console.log(
  await secureClient.db(db).collection(coll).findOne({ ssn: "241014209" })
);
```

**python:**

```python
print("Finding a document with regular (non-encrypted) client.")
result = regularClient.medicalRecords.patients.find_one({"name": "Jon Doe"})
pprint.pprint(result)

print("Finding a document with encrypted client, searching on an encrypted field")
pprint.pprint(secureClient.medicalRecords.patients.find_one({"ssn": 241014209}))
```

**csharp:**

```csharp
Console.WriteLine("Finding a document with regular (non-encrypted) client.");
var filter = Builders<BsonDocument>.Filter.Eq("name", "Jon Doe");
var regularResult = regularCollection.Find(filter).Limit(1).ToList()[0];
Console.WriteLine($"\n{regularResult}\n");

Console.WriteLine("Finding a document with encrypted client, searching on an encrypted field");
var ssnFilter = Builders<BsonDocument>.Filter.Eq("ssn", 145014000);
var secureResult = secureCollection.Find(ssnFilter).Limit(1).First();
Console.WriteLine($"\n{secureResult}\n");
```

**go:**

```go
fmt.Println("Finding a document with regular (non-encrypted) client.")
var resultRegular bson.M
err = regularClient.Database(dbName).Collection(collName).FindOne(context.TODO(), bson.D{{"name", "Jon Doe"}}).Decode(&resultRegular)
if err != nil {
	panic(err)
}
outputRegular, err := json.MarshalIndent(resultRegular, "", "    ")
if err != nil {
	panic(err)
}
fmt.Printf("%s\n", outputRegular)

fmt.Println("Finding a document with encrypted client, searching on an encrypted field")
var resultSecure bson.M
err = secureClient.Database(dbName).Collection(collName).FindOne(context.TODO(), bson.D{{"ssn", "241014209"}}).Decode(&resultSecure)
if err != nil {
	panic(err)
}
outputSecure, err := json.MarshalIndent(resultSecure, "", "    ")
if err != nil {
	panic(err)
}
fmt.Printf("%s\n", outputSecure)
```

The output of the preceding code snippet should look like this:

```json
Finding a document with regular (non-encrypted) client.

{
  _id: new ObjectId("629a452e0861b3130887103a"),
  name: 'Jon Doe',
  ssn: new Binary(Buffer.from("0217482732d8014cdd9ffdd6e2966e5e7910c20697e5f4fa95710aafc9153f0a3dc769c8a132a604b468732ff1f4d8349ded3244b59cbfb41444a210f28b21ea1b6c737508d9d30e8baa30c1d8070c4d5e26", "hex"), 6),
  bloodType: new Binary(Buffer.from("0217482732d8014cdd9ffdd6e2966e5e79022e238536dfd8caadb4d7751ac940e0f195addd7e5c67b61022d02faa90283ab69e02303c7e4001d1996128428bf037dea8bbf59fbb20c583cbcff2bf3e2519b4", "hex"), 6),
  'key-id': 'demo-data-key',
  medicalRecords: new Binary(Buffer.from("0217482732d8014cdd9ffdd6e2966e5e790405163a3207cff175455106f57eef14e5610c49a99bcbd14a7db9c5284e45e3ee30c149354015f941440bf54725d6492fb3b8704bc7c411cff6c868e4e13c58233c3d5ed9593eca4e4d027d76d3705b6d1f3b3c9e2ceee195fd944b553eb27eee69e5e67c338f146f8445995664980bf0", "hex"), 6),
  insurance: {
    policyNumber: new Binary(Buffer.from("0217482732d8014cdd9ffdd6e2966e5e79108decd85c05be3fec099e015f9d26d9234605dc959cc1a19b63072f7ffda99db38c7b487de0572a03b2139ac3ee163bcc40c8508f366ce92a5dd36e38b3c742f7", "hex"), 6),
    provider: 'MaestCare'
  }
}

Finding a document with encrypted client, searching on an encrypted field

{
  _id: new ObjectId("629a452e0861b3130887103a"),
  name: 'Jon Doe',
  ssn: 241014209,
  bloodType: 'AB+',
  'key-id': 'demo-data-key',
  medicalRecords: [ { weight: 180, bloodPressure: '120/80' } ],
  insurance: { policyNumber: 123142, provider: 'MaestCare' }
}
```

**See also:** Complete Code

**java-sync:**

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/local/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

**nodejs:**

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/local/reader/insert_encrypted_document.js).

**python:**

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/local/reader/insert_encrypted_document.py).

**csharp:**

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/local/reader/CSFLE/InsertEncryptedDocument.cs)

**go:**

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/local/reader/insert-encrypted-document.go).

## Learn More

To view a tutorial on production-ready CSFLE with a remote
KMS, see csfle-tutorial-automatic-encryption.

To learn how CSFLE works, see
csfle-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Customer Master Keys
- Key Management System providers
- Data Encryption Keys
- Key Vault collections
- Encryption Schemas
- mongocryptd
- CSFLE-specific MongoClient settings
- Automatic CSFLE Writes
