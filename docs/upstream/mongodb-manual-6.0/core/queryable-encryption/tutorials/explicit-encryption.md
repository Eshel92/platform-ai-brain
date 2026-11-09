<!-- Converted from core/queryable-encryption/tutorials/explicit-encryption.txt (reStructuredText). Includes are inlined. -->

# Use Explicit Encryption

## Overview

This guide shows you how to encrypt a document with explicit encryption
and a MongoDB driver.

After completing this guide, you should be able to configure a driver to
encrypt fields in a document using explicit encryption. With this knowledge,
you should be able to create a client application that uses explicit encryption.
with automatic decryption.

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
select the tab corresponding to your preferred MongoDB driver and follow
the provided link:

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/exp/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/exp/reader/)

**java:**

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/exp/reader/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/exp/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/exp/reader/)

## Procedure

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```shell
openssl rand 96 > master-key.txt
```

**Note:** Use a Programming Language to Create a Customer Master Key

If you would rather use your preferred programming language to generate
your CMK ({+cmk-long+}), you can view code snippets demonstrating how to generate a
Customer Master Key in each of the supported languages of this
guide on [GitHub](https://github.com/mongodb/docs/tree/master/source/includes/quick-start/generate-master-key).

**Warning:** Do Not Use a Local Key File in Production

A local key file in your filesystem is insecure and is
**not recommended** for production. Instead,
you should store your Customer Master Keys in a remote
Key Management System
(KMS).

To learn how to use a remote KMS in your Queryable Encryption implementation,
see the qe-tutorial-automatic-encryption guide.

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` collection.

Select the tab corresponding to your preferred MongoDB driver:

**nodejs:**

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

key_vault_client[key_vault_db][key_vault_coll].create_index(
    [("keyAltNames", ASCENDING)],
    unique=True,
    partialFilterExpression={"keyAltNames": {"$exists": True}},
)
```

**java-sync:**

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

**csharp:**

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

**Step 1: Read the Customer Master Key and Specify KMS Provider Settings**

Retrieve the contents of the Customer Master Key file that you generated
in the Create a Customer Master Key step of this guide.

Pass the CMK ({+cmk-long+}) value to your KMS provider settings. The
client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
name to `local` to inform the driver you are using a
Local Key Provider.

Select the tab corresponding to your preferred MongoDB driver:

**nodejs:**

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

**python:**

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

**go:**

```go
key, err := ioutil.ReadFile("master-key.txt")
if err != nil {
	log.Fatalf("Could not read the key from master-key.txt: %v", err)
}
provider := "local"
kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
```

**csharp:**

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

**Step 2: Create your Data Encryption Keys**

Construct a client with your MongoDB connection string and Key Vault collection
namespace, and create the Data Encryption Keys:

**Note:** Key Vault Collection Namespace Permissions

The Key Vault collection is in the `encryption.__keyVault`
namespace. Ensure that the database user your application uses to connect
to MongoDB has ReadWrite
permissions on this namespace.

**nodejs:**

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

**python:**

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

**java-sync:**

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

**csharp:**

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

**Step 3: Create Your Encrypted Collection**

Use a Queryable Encryption enabled `MongoClient` instance to specify what
fields you must encrypt and create your encrypted collection:

**nodejs:**

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

**python:**

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
    schema_map=None,
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

**java-sync:**

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

**go:**

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

**csharp:**

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

**See also:** Complete Code

**nodejs:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/exp/reader/make_data_key.js).

**python:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/exp/reader/make_data_key.py).

**java-sync:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/exp/reader/src/main/java/com/mongodb/qe/MakeDataKey.java).

**go:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/exp/reader/make-data-key.go).

**csharp:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/exp/reader/QueryableEncryption/MakeDataKey.cs).

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

**Step 1: Specify the Key Vault Collection Namespace**

Specify `encryption.__keyVault` as the Key Vault collection
namespace.

**nodejs:**

```javascript
const eDB = "encryption";
const eKV = "__keyVault";
const keyVaultNamespace = `${eDB}.${eKV}`;
const secretDB = "medicalRecords";
const secretCollection = "patients";
```

**python:**

```python
key_vault_namespace = "encryption.__keyVault"
key_vault_db_name, key_vault_coll_name = key_vault_namespace.split(".", 1)
```

**java-sync:**

```java
String db = "medicalRecords";
String coll = "patients";
String keyVaultDb = "encryption";
String keyVaultColl = "__keyVault";
String keyVaultNamespace = String.format("%1$s.%2$s", keyVaultDb, keyVaultColl);
String connectionString = "<Your MongoDB URI>";
```

**go:**

```go
keyVaultColl := "__keyVault"
keyVaultDb := "encryption"
keyVaultNamespace := keyVaultDb + "." + keyVaultColl
dbName := "medicalRecords"
collName := "patients"
```

**csharp:**

```csharp
var connectionString = "<Your MongoDB URI>";
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
var coll = "patients";
var db = "medicalRecords";
```

**Step 2: Specify the Customer Master Key**

Specify the KMS provider and specify your Customer Master Key inline:

**nodejs:**

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

**java-sync:**

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

**go:**

```go
key, err := ioutil.ReadFile("master-key.txt")
if err != nil {
	log.Fatalf("Could not read the key from master-key.txt: %v", err)
}
kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
```

**csharp:**

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

**Step 3: Retrieve Data Encryption Keys**

Retrieve the Data Encryption Keys created in the
Create a Data Encryption Key
step of this guide:

**nodejs:**

```javascript
const uri = "<Your MongoDB URI>";
const unencryptedClient = new MongoClient(uri);
await unencryptedClient.connect();
const keyVaultClient = unencryptedClient.db(eDB).collection(eKV);
const dek1 = await keyVaultClient.findOne({ keyAltNames: "dataKey1" });
const dek2 = await keyVaultClient.findOne({ keyAltNames: "dataKey2" });
```

**python:**

```python
connection_string = "<your connection string here>"
client = MongoClient(connection_string)
key_vault = client[key_vault_db_name][key_vault_coll_name]

data_key_id_1 = key_vault.find_one({"keyAltNames": "dataKey1"})["_id"]
data_key_id_2 = key_vault.find_one({"keyAltNames": "dataKey2"})["_id"]
```

**java-sync:**

```java
MongoClient client = MongoClients.create(connectionString);
MongoCollection<Document> keyVaultClient = client.getDatabase(keyVaultDb).getCollection(keyVaultColl);
BsonBinary dataKeyId1 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey1")).first().get("_id", Binary.class).getData());
BsonBinary dataKeyId2 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey2")).first().get("_id", Binary.class).getData());
```

**go:**

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

**csharp:**

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

**Step 4: Specify the Path of the Automatic Encryption Shared Library**

**nodejs:**

```javascript
const extraOptions = {
  cryptSharedLibPath: "<path to crypt_shared library>",
};
```

**python:**

```python
opts = AutoEncryptionOpts(
    kms_providers,
    key_vault.full_name,
    bypass_query_analysis=True,
    key_vault_client=client,
    crypt_shared_lib_path="<path to FLE Shared Library>",
)
```

**java-sync:**

```java
Map<String, Object> extraOptions = new HashMap<>();
extraOptions.put("cryptSharedLibPath", "<path to crypt_shared library>");
```

**go:**

```go
extraOptions := map[string]interface{}{
	"cryptSharedLibPath": "<path to crypt_shared library>",
}
```

**csharp:**

```csharp
var extraOptions = new Dictionary<string, object>()
{
    {"cryptSharedLibPath", "<path to crypt_shared library>"},
};
```

**Tip:** Learn More

To learn more about the library referenced by this path,
see the qe-reference-shared-library page.

**Step 5: Create a MongoClient Object**

Instantiate a `MongoClient` object with the following
automatic encryption settings:

**nodejs:**

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

**python:**

```python
encrypted_client = MongoClient(connection_string, auto_encryption_opts=opts)
db = encrypted_client.medicalRecords
coll = db.patients
```

**java-sync:**

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

**go:**

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

**csharp:**

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

**Step 6: Create a ClientEncryption Object**

Instantiate a `ClientEncryption` object as follows:

**nodejs:**

```javascript
const encryption = new ClientEncryption(unencryptedClient, {
  keyVaultNamespace,
  kmsProviders,
});
```

**python:**

```python
client_encryption = ClientEncryption(
    kms_providers, key_vault_namespace, client, client.codec_options
)
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
ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
```

**go:**

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

**csharp:**

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
explicit encryption, see qe-fundadmentals-man-enc-algorithm-choice.

**Step 7: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert an encrypted document into the
`medicalRecords.patients` namespace using the following code
snippet:

**nodejs:**

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

**python:**

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

**java-sync:**

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

**go:**

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

**csharp:**

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

**See also:** Complete Code

**nodejs:**

To view the complete code to insert a document encrypted with explicit encryption, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/exp/reader/insert_encrypted_document.js).

**python:**

To view the complete code to insert a document encrypted with explicit encryption, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/exp/reader/insert_encrypted_document.py).

**java-sync:**

To view the complete code to insert a document encrypted with explicit encryption, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/exp/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**go:**

To view the complete code to insert a document encrypted with explicit encryption, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/exp/reader/insert-encrypted-document.go).

**csharp:**

To view the complete code to insert a document encrypted with explicit encryption, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/exp/reader/QueryableEncryption/InsertEncryptedDocument.cs).

**Step 8: Retrieve Your Encrypted Document**

Retrieve the encrypted document you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

**nodejs:**

```javascript
const findPayload = await encryption.encrypt(patientId, {
  algorithm: "Indexed",
  keyId: dek1._id,
  queryType: "equality",
  contentionFactor: 1,
});

console.log("Finding a document with manually encrypted field:");
```

**python:**

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

**java-sync:**

```java
BsonBinary findPayloadEncrypted = clientEncryption.encrypt(patientId, new EncryptOptions("Indexed").keyId(dataKeyId1).queryType("equality").contentionFactor(1L));
BsonDocument result = collection.find(eq("patientId", findPayloadEncrypted)).first();
System.out.println("Finding a document with manually encrypted field: " + result.toJson());
```

**go:**

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

**csharp:**

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

**See also:** Complete Code

**nodejs:**

To view the code to retrieve your encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/exp/reader/insert_encrypted_document.js).

**python:**

To view the code to retrieve your encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/exp/reader/insert_encrypted_document.py).

**java-sync:**

To view the code to retrieve your encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/exp/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**go:**

To view the code to retrieve your encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/exp/reader/insert-encrypted-document.go).

**csharp:**

To view the code to retrieve your encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/exp/reader/QueryableEncryption/InsertEncryptedDocument.cs).

## Learn More

To view a tutorial on using Queryable Encryption with a remote
KMS, see qe-tutorial-automatic-encryption.

To learn how Queryable Encryption works, see
qe-fundamentals-manual-encryption.

To learn more about the topics mentioned in this guide, see the
following links:

- qe-reference-keys-key-vaults
- qe-fundamentals-kms-providers
