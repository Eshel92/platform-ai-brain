<!-- Part 2 of 4 of core/queryable-encryption/tutorials/azure/azure-automatic.md (split because the page is big). -->

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` collection.

Select the tab corresponding to your preferred MongoDB driver:

**shell:**

```javascript
const uri = "<Your Connection String>";
const keyVaultClient = Mongo(uri);
const keyVaultDB = keyVaultClient.getDB(keyVaultDatabase);
// Drop the Key Vault Collection in case you created this collection
// in a previous run of this application.
keyVaultDB.dropDatabase();
keyVaultDB.createCollection(keyVaultCollection);

const keyVaultColl = keyVaultDB.getCollection(keyVaultCollection);
keyVaultColl.createIndex(
  { keyAltNames: 1 },
  {
    unique: true,
    partialFilterExpression: { keyAltNames: { $exists: true } },
  }
);
```

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
String connectionString = "<Your MongoDB URI>";
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

**Step 2: Create your Data Encryption Keys and Encrypted Collection**

**Step 1: Add your Azure Key Vault Credentials**

Add the service account credentials to your Queryable Encryption enabled client
code.

Select the tab corresponding to your preferred MongoDB driver:

**Tip:**

You recorded your Azure Key Vault credentials in the
in the Register Your Applitcation with Azure
step of this guide.

**shell:**

```javascript
const provider = "azure";
const kmsProviders = {
  azure: {
    tenantId: "<Your Tenant ID>",
    clientId: "<Your Client ID>",
    clientSecret: "<Your Client Secret>",
  },
};
```

**nodejs:**

```javascript
const provider = "azure";
const kmsProviders = {
  azure: {
    tenantId: "<Your Tenant ID>",
    clientId: "<Your Client ID>",
    clientSecret: "<Your Client Secret>",
  },
};
```

**python:**

```python
provider = "azure"
kms_providers = {
    provider: {
        "tenantId": "<Azure account organization>",
        "clientId": "<Azure client ID>",
        "clientSecret": "<Azure client secret>",
    }
}
```

**java-sync:**

```java
String kmsProvider = "azure";
Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
Map<String, Object> providerDetails = new HashMap<>();
providerDetails.put("tenantId", "<Azure account organization>");
providerDetails.put("clientId", "<Azure client ID>");
providerDetails.put("clientSecret", "<Azure client secret>");
kmsProviders.put(kmsProvider, providerDetails);
```

**go:**

```go
provider := "azure"
kmsProviders := map[string]map[string]interface{}{
	provider: {
		"tenantId":     "<Your Azure Tenant ID>",
		"clientId":     "<Your Azure Client ID>",
		"clientSecret": "<Your Azure Client Secret>",
	},
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
const string provider = "azure";
var azureKmsOptions = new Dictionary<string, object>
{
   { "tenantId", "<Your Azure Tenant ID>" },
   { "clientId", "<Your Azure Client ID>" },
   { "clientSecret", "<Your Azure Client Secret>" },
};
kmsProviders.Add(provider, azureKmsOptions);
```

**Tip:** Learn More

To learn more about the KMS provider object for Azure Key Vault, see
qe-reference-kms-providers-azure.

**Step 2: Add Your Key Information**

Update the following code to specify your Customer Master Key:

**Tip:**

You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
in the Create a Customer Master Key
step of this guide.

**shell:**

```javascript
const masterKey = {
  keyVaultEndpoint: "<Your Key Vault Endpoint>",
  keyName: "<Your Key Name>",
};
```

**nodejs:**

```javascript
const masterKey = {
  keyVaultEndpoint: "<Your Key Vault Endpoint>",
  keyName: "<Your Key Name>",
};
```

**python:**

```python
master_key = {
    "keyName": "<Azure key name>",
    "keyVersion": "<Azure key version>",
    "keyVaultEndpoint": "<Azure key vault endpoint/key identifier>",
}
```

**java-sync:**

```java
BsonDocument masterKeyProperties = new BsonDocument();
masterKeyProperties.put("provider", new BsonString(kmsProvider));
masterKeyProperties.put("keyName", new BsonString("<Azure key name>"));
masterKeyProperties.put("keyVaultEndpoint", new BsonString("<Azure key vault endpoint"));
```

**go:**

```go
masterKey := map[string]interface{}{
	"keyVaultEndpoint": "<Your Azure Key Vault Endpoint>",
	"keyName":          "<Your Azure Key Name>",
}
```

**csharp:**

```csharp
DataKeyOptions GetDataKeyOptions(List<string> altNames)
{
    kmsProviders.Add(provider, azureKmsOptions);
    var dataKeyOptions = new DataKeyOptions(
       alternateKeyNames: altNames,
       masterKey: new BsonDocument
       {
           { "keyName", "<Your Azure Key Name>" },
           { "keyVaultEndpoint", "<Your Azure Key Vault Endpoint>" },
       });
    return dataKeyOptions;
}
```

**Step 3: Create your Data Encryption Keys**

Construct a client with your MongoDB connection string and Key Vault collection
namespace, and create the Data Encryption Keys:

**Note:** Key Vault Collection Namespace Permissions

The Key Vault collection in this guide is the `__keyVault`
collection in the `encryption` database.
Ensure that the database user your application uses to connect
to MongoDB has [ReadWrite](https://www.mongodb.com/docs/manual/reference/built-in-roles/#readWrite)
permissions on the `encryption.__keyVault` namespace.

**shell:**

```javascript
const autoEncryptionOpts = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
};

const encClient = Mongo(uri, autoEncryptionOpts);
const keyVault = encClient.getKeyVault();

const dek1 = keyVault.createKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey1"],
});
const dek2 = keyVault.createKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey2"],
});
const dek3 = keyVault.createKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey3"],
});
const dek4 = keyVault.createKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey4"],
});
```

**nodejs:**

```javascript
const clientEnc = new ClientEncryption(keyVaultClient, {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
});
const dek1 = await clientEnc.createDataKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey1"],
});
const dek2 = await clientEnc.createDataKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey2"],
});
const dek3 = await clientEnc.createDataKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey3"],
});
const dek4 = await clientEnc.createDataKey(provider, {
  masterKey: masterKey,
  keyAltNames: ["dataKey4"],
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

data_key_id_1 = client_encryption.create_data_key(
    provider, master_key=master_key, key_alt_names=["dataKey1"]
)
data_key_id_2 = client_encryption.create_data_key(
    provider, master_key=master_key, key_alt_names=["dataKey2"]
)
data_key_id_3 = client_encryption.create_data_key(
    provider, master_key=master_key, key_alt_names=["dataKey3"]
)
data_key_id_4 = client_encryption.create_data_key(
    provider, master_key=master_key, key_alt_names=["dataKey4"]
)
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
        .masterKey(masterKeyProperties)
        .keyAltNames(keyAlts1));
List<String> keyAlts2 = new ArrayList<String>();
keyAlts2.add("dataKey2");
BsonBinary dataKeyId2 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
        .masterKey(masterKeyProperties)
        .keyAltNames(keyAlts2));
List<String> keyAlts3 = new ArrayList<String>();
keyAlts3.add("dataKey3");
BsonBinary dataKeyId3 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
        .masterKey(masterKeyProperties)
        .keyAltNames(keyAlts3));
List<String> keyAlts4 = new ArrayList<String>();
keyAlts4.add("dataKey4");
BsonBinary dataKeyId4 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
        .masterKey(masterKeyProperties)
        .keyAltNames(keyAlts4));
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
	SetMasterKey(masterKey).
	SetKeyAltNames([]string{"demoDataKey1"})
dataKeyID1, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts1)
if err != nil {
	return fmt.Errorf("create data key error %v", err)
}
dataKeyOpts2 := options.DataKey().
	SetMasterKey(masterKey).
	SetKeyAltNames([]string{"demoDataKey2"})
dataKeyID2, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts2)
if err != nil {
	return fmt.Errorf("create data key error %v", err)
}
dataKeyOpts3 := options.DataKey().
	SetMasterKey(masterKey).
	SetKeyAltNames([]string{"demoDataKey3"})
dataKeyID3, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts3)
if err != nil {
	return fmt.Errorf("create data key error %v", err)
}
dataKeyOpts4 := options.DataKey().
	SetMasterKey(masterKey).
	SetKeyAltNames([]string{"demoDataKey4"})
dataKeyID4, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts4)
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
var dataKeyOptions1 = GetDataKeyOptions(new List<string> { "dataKey1" });
var dataKeyOptions2 = GetDataKeyOptions(new List<string> { "dataKey2" });
var dataKeyOptions3 = GetDataKeyOptions(new List<string> { "dataKey3" });
var dataKeyOptions4 = GetDataKeyOptions(new List<string> { "dataKey4" });

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

**Step 4: Create Your Encrypted Collection**

Use a Queryable Encryption enabled `MongoClient` intance to specify what
fields you must encrypt and create your encrypted collection:

**shell:**

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
      {
        keyId: dek3,
        path: "patientRecord.ssn",
        bsonType: "string",
        queries: { queryType: "equality" },
      },
      {
        keyId: dek4,
        path: "patientRecord.billing",
        bsonType: "object",
      },
    ],
  },
};

try {
  const autoEncryptionOptions = {
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders,
    encryptedFieldsMap: encryptedFieldsMap,
  };

  const encClient = Mongo(uri, autoEncryptionOptions);
  const newEncDB = encClient.getDB(secretDB);
  // Drop the encrypted collection in case you created this collection
  // in a previous run of this application.
  newEncDB.dropDatabase();
  newEncDB.createCollection(secretCollection);
  console.log("Created encrypted collection!");
```

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
      {
        keyId: dek3,
        path: "patientRecord.ssn",
        bsonType: "string",
        queries: { queryType: "equality" },
      },
      {
        keyId: dek4,
        path: "patientRecord.billing",
        bsonType: "object",
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
            {
                "keyId": data_key_id_3,
                "path": "patientRecord.ssn",
                "bsonType": "string",
                "queries": {"queryType": "equality"},
            },
            {
                "keyId": data_key_id_4,
                "path": "patientRecord.billing",
                "bsonType": "object",
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
                new BsonDocument().append("keyId", dataKeyId3)
                        .append("path", new BsonString("patientRecord.ssn"))
                        .append("bsonType", new BsonString("string"))
                        .append("queries", new BsonDocument().append("queryType", new BsonString("equality"))),
                new BsonDocument().append("keyId", dataKeyId4)
                        .append("path", new BsonString("patientRecord.billing"))
                        .append("bsonType", new BsonString("object"))
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
			{
				"path":     "patientRecord.ssn",
				"bsonType": "string",
				"keyId":    dataKeyID3,
				"queries": []bson.M{
					{
						"queryType": "equality",
					},
				},
			},
			{
				"path":     "patientRecord.billing",
				"bsonType": "object",
				"keyId":    dataKeyID4,
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
                    new BsonDocument
                    {
                        {"keyId", dataKeyId3},
                        {"path", new BsonString("patientRecord.ssn")},
                        {"bsonType", new BsonString("string")},
                        {
                            "queries", new BsonDocument
                            {
                                {"queryType", new BsonString("equality")}
                            }
                        }
                    },
                    new BsonDocument
                    {
                        {"keyId", dataKeyId4},
                        {"path", new BsonString("patientRecord.billing")},
                        {"bsonType", new BsonString("object")},
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

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an Azure Key Vault, see
qe-reference-kms-providers-azure-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in Azure Key Vault, see
qe-kms-provider-object-azure and
qe-kms-datakeyopts-azure.

**See also:** Complete Code

**shell:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/azure/reader/make_data_key.js).

**nodejs:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/azure/reader/make_data_key.js).

**python:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/azure/reader/make_data_key.py).

**java-sync:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/azure/reader/src/main/java/com/mongodb/qe/MakeDataKey.java).

**go:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/azure/reader/make-data-key.go).

**csharp:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/azure/reader/QueryableEncryption/MakeDataKey.cs).

**Step 5: Configure your MongoClient for Encrypted Reads and Writes**

**Step 1: Specify the Key Vault Collection Namespace**

Specify `encryption.__keyVault` as the Key Vault collection
namespace.

**shell:**

```javascript
const keyVaultDB = "encryption";
const keyVaultColl = "__keyVault";
const keyVaultNamespace = `${keyVaultDB}.${keyVaultColl}`;
const secretDB = "medicalRecords";
const secretCollection = "patients";
```

**nodejs:**

```javascript
const eDB = "encryption";
const eKV = "__keyVault";
const keyVaultNamespace = `${eDB}.${eKV}`;
```

**python:**

```python
key_vault_db = "encryption"
key_vault_coll = "__keyVault"
key_vault_namespace = "encryption.__keyVault"
```

**java-sync:**

```java
String keyVaultDb = "encryption";
String keyVaultColl = "__keyVault";
String keyVaultNamespace = keyVaultDb + "." + keyVaultColl;
```

**go:**

```go
keyVaultColl := "__keyVault"
keyVaultDb := "encryption"
keyVaultNamespace := keyVaultDb + "." + keyVaultColl
```

**csharp:**

```csharp
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
```

**Step 2: Specify your Azure Credentials**

Specify the `azure` KMS provider and your Azure
credentials:

**shell:**

```javascript
const kmsProviders = {
  azure: {
    tenantId: "<Your Tenant ID>",
    clientId: "<Your Client ID>",
    clientSecret: "<Your Client Secret>",
  },
};
```

**nodejs:**

```javascript
const kmsProviders = {
  azure: {
    tenantId: "<Your Tenant ID>",
    clientId: "<Your Client ID>",
    clientSecret: "<Your Client Secret>",
  },
};
```

**python:**

```python
provider = "azure"
kms_providers = {
    provider: {
        "tenantId": "<Azure account organization>",
        "clientId": "<Azure client ID>",
        "clientSecret": "<Azure client secret>",
    }
}
```

**java-sync:**

```java
String kmsProvider = "azure";
Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
Map<String, Object> providerDetails = new HashMap<>();
providerDetails.put("tenantId", "<Azure account organization>");
providerDetails.put("clientId", "<Azure client ID>");
providerDetails.put("clientSecret", "<Azure client secret>");
kmsProviders.put(kmsProvider, providerDetails);
```

**go:**

```go
kmsProviders := map[string]map[string]interface{}{
	"azure": {
		"tenantId":     "<Your Azure Tenant ID>",
		"clientId":     "<Your Azure Client ID>",
		"clientSecret": "<Your Azure Client Secret>",
	},
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
const string provider = "azure";
var azureKmsOptions = new Dictionary<string, object>
{
   { "tenantId", "<Your Azure Tenant ID>" },
   { "clientId", "<Your Azure Client ID>" },
   { "clientSecret", "<Your Azure Client Secret>" },
};
kmsProviders.Add(provider, azureKmsOptions);
```

**Step 3: Create an Encrypted Fields Map For Your Collection**

**shell:**

```javascript
const uri = "<Your Connection String>";
const unencryptedClient = Mongo(uri);
const autoEncryptionOpts = { kmsProviders, keyVaultNamespace };

const encClient = Mongo(uri, autoEncryptionOpts);
const keyVault = encClient.getKeyVault();
const keyVaultClient = unencryptedClient
  .getDB(keyVaultDB)
  .getCollection(keyVaultColl);

const dek1 = keyVaultClient.findOne({ keyAltNames: "dataKey1" });
const dek2 = keyVaultClient.findOne({ keyAltNames: "dataKey2" });
const dek3 = keyVaultClient.findOne({ keyAltNames: "dataKey3" });
const dek4 = keyVaultClient.findOne({ keyAltNames: "dataKey4" });

const secretDB = "medicalRecords";
const secretColl = "patients";

const encryptedFieldsMap = {
  [`${secretDB}.${secretColl}`]: {
    fields: [
      {
        keyId: dek1._id,
        path: "patientId",
        bsonType: "int",
        queries: { queryType: "equality" },
      },
      {
        keyId: dek2._id,
        path: "medications",
        bsonType: "array",
      },
      {
        keyId: dek3._id,
        path: "patientRecord.ssn",
        bsonType: "string",
        queries: { queryType: "equality" },
      },
      {
        keyId: dek4._id,
        path: "patientRecord.billing",
        bsonType: "object",
      },
    ],
  },
};
```

**nodejs:**

```javascript
const uri = "<Your Connection String>";
const unencryptedClient = new MongoClient(uri);
await unencryptedClient.connect();
const keyVaultClient = unencryptedClient.db(eDB).collection(eKV);

const dek1 = await keyVaultClient.findOne({ keyAltNames: "dataKey1" });
const dek2 = await keyVaultClient.findOne({ keyAltNames: "dataKey2" });
const dek3 = await keyVaultClient.findOne({ keyAltNames: "dataKey3" });
const dek4 = await keyVaultClient.findOne({ keyAltNames: "dataKey4" });

const secretDB = "medicalRecords";
const secretCollection = "patients";

const encryptedFieldsMap = {
  [`${secretDB}.${secretCollection}`]: {
    fields: [
      {
        keyId: dek1._id,
        path: "patientId",
        bsonType: "int",
        queries: { queryType: "equality" },
      },
      {
        keyId: dek2._id,
        path: "medications",
        bsonType: "array",
      },
      {
        keyId: dek3._id,
        path: "patientRecord.ssn",
        bsonType: "string",
        queries: { queryType: "equality" },
      },
      {
        keyId: dek4._id,
        path: "patientRecord.billing",
        bsonType: "object",
      },
    ],
  },
};
```

**python:**

```python
connection_string = "<your connection string here>"

unencryptedClient = MongoClient(connection_string)
keyVaultClient = unencryptedClient[key_vault_db][key_vault_coll]
data_key_id_1 = keyVaultClient.find_one({"keyAltNames": "dataKey1"})["_id"]
data_key_id_2 = keyVaultClient.find_one({"keyAltNames": "dataKey2"})["_id"]
data_key_id_3 = keyVaultClient.find_one({"keyAltNames": "dataKey3"})["_id"]
data_key_id_4 = keyVaultClient.find_one({"keyAltNames": "dataKey4"})["_id"]

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
            {
                "keyId": data_key_id_3,
                "path": "patientRecord.ssn",
                "bsonType": "string",
                "queries": {"queryType": "equality"},
            },
            {
                "keyId": data_key_id_4,
                "path": "patientRecord.billing",
                "bsonType": "object",
            },
        ],
    },
}
```

**java-sync:**

```java
MongoClient regularClient = MongoClients.create(connectionString);

MongoCollection<Document> keyVaultClient = regularClient.getDatabase(keyVaultDb).getCollection(keyVaultColl);

BsonBinary dataKeyId1 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey1")).first().get("_id", Binary.class).getData());
BsonBinary dataKeyId2 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey2")).first().get("_id", Binary.class).getData());
BsonBinary dataKeyId3 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey3")).first().get("_id", Binary.class).getData());
BsonBinary dataKeyId4 = new BsonBinary(BsonBinarySubType.UUID_STANDARD, keyVaultClient.find(eq("keyAltNames", "dataKey4")).first().get("_id", Binary.class).getData());

BsonDocument encFields = new BsonDocument().append("fields",
        new BsonArray(Arrays.asList(
                new BsonDocument().append("keyId", dataKeyId1)
                        .append("path", new BsonString("patientId"))
                        .append("bsonType", new BsonString("int"))
                        .append("queries", new BsonDocument().append("queryType", new BsonString("equality"))),
                new BsonDocument().append("keyId", dataKeyId2)
                        .append("path", new BsonString("medications"))
                        .append("bsonType", new BsonString("array")),
                new BsonDocument().append("keyId", dataKeyId3)
                        .append("path", new BsonString("patientRecord.ssn"))
                        .append("bsonType", new BsonString("string"))
                        .append("queries", new BsonDocument().append("queryType", new BsonString("equality"))),
                new BsonDocument().append("keyId", dataKeyId4)
                        .append("path", new BsonString("patientRecord.billing"))
                        .append("bsonType", new BsonString("object")))));
Map<String, BsonDocument> encryptedFieldsMap = new HashMap<String, BsonDocument>();
encryptedFieldsMap.put(encryptedNameSpace, encFields);
```

**go:**

```go
regularClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri))
if err != nil {
	return fmt.Errorf("Connect error for regular client: %v", err)
}
defer func() {
	_ = regularClient.Disconnect(context.TODO())
}()

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
var foundDoc3 bson.M
err = regularClient.Database(keyVaultDb).Collection(keyVaultColl).FindOne(context.TODO(), bson.D{{"keyAltNames", "demoDataKey3"}}).Decode(&foundDoc3)
if err != nil {
	panic(err)
}
var dataKeyID3 = foundDoc3["_id"].(primitive.Binary)
var foundDoc4 bson.M
err = regularClient.Database(keyVaultDb).Collection(keyVaultColl).FindOne(context.TODO(), bson.D{{"keyAltNames", "demoDataKey4"}}).Decode(&foundDoc4)
if err != nil {
	panic(err)
}
var dataKeyID4 = foundDoc4["_id"].(primitive.Binary)

encryptedFieldsMap := bson.M{
	"medicalRecords.patients": bson.M{
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
			{
				"path":     "patientRecord.ssn",
				"bsonType": "string",
				"keyId":    dataKeyID3,
				"queries": []bson.M{
					{
						"queryType": "equality",
					},
				},
			},
			{
				"path":     "patientRecord.billing",
				"bsonType": "object",
				"keyId":    dataKeyID4,
			},
		},
	},
}
```

**csharp:**

```csharp
var regularClient = new MongoClient(connectionString);
var keyVaultCollection = regularClient.GetDatabase(keyVaultNamespace.DatabaseNamespace.DatabaseName)
    .GetCollection<BsonDocument>(keyVaultNamespace.CollectionName);

BsonBinaryData GetKeyId(string altName)
{
    var filter = Builders<BsonDocument>.Filter.Eq<BsonString>("keyAltNames", altName);
    return keyVaultCollection.Find(filter).First<BsonDocument>()["_id"].AsBsonBinaryData;
}

var dataKeyId1 = GetKeyId("dataKey1");
var dataKeyId2 = GetKeyId("dataKey2");
var dataKeyId3 = GetKeyId("dataKey3");
var dataKeyId4 = GetKeyId("dataKey4");

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
