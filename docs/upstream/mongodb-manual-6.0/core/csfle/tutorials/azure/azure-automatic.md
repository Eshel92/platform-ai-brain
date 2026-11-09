<!-- Converted from core/csfle/tutorials/azure/azure-automatic.txt (reStructuredText). Includes are inlined. -->

# Use Automatic Client-Side Field Level Encryption with Azure

## Overview

This guide shows you how to build a Client-Side Field Level Encryption (CSFLE)-enabled
application using Azure Key Vault.

After you complete the steps in this guide, you should have:

- A Customer Master Key hosted on an Azure Key Vault instance.
- A working client application that inserts encrypted documents
  using your Customer Master Key.

## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the csfle-install page.

Throughout this guide, code examples use placeholder text. 
Before you run the examples, substitute your own values for 
these placeholders.

For example:

```go
dek_id := "<Your Base64 DEK ID>"
```

You would replace everything between quotes with your DEK ({+dek-long+}) ID.

```go
dek_id := "abc123"
```

Select the programming language for which you want to see code examples for
from the Select your language dropdown menu on the right side of
the page.

**See also:** Full Application

To view the complete runnable application code for this tutorial, go to the
following link:

**java-sync:**

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/java/azure/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/node/azure/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/python/azure/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/dotnet/azure/reader/CSFLE/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/go/azure/reader/)

## Set Up the KMS

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
// You are viewing the C# driver code examples.
// Use the dropdown menu to select a different driver.
```

**go:**

```go
// You are viewing the Golang driver code examples.
// Use the dropdown menu to select a different driver.
```

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

**Note:**

The Customer Master Key should have an RSA key size of 2048 or 4096 
bits.

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

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` collection.

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

**Step 2: Create a New Data Encryption Key**

**Step 1: Add your Azure Key Vault Credentials**

Add the service account credentials to your CSFLE-enabled client
code.

**Tip:**

You recorded your Azure Key Vault credentials in the
in the Register Your Applitcation with Azure
step of this guide.

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

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var provider = "azure";
var azureKmsOptions = new Dictionary<string, object>
{
   { "tenantId", "<Your Azure Tenant ID>" },
   { "clientId", "<Your Azure Client ID>" },
   { "clientSecret", "<Your Azure Client Secret>" },
};
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

**Tip:** Learn More

To learn more about the KMS provider object for Azure Key Vault, see
csfle-reference-kms-providers-azure.

**Step 2: Add Your Key Information**

Update the following code to specify your Customer Master Key:

**Tip:**

You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
in the Create a Customer Master Key
step of this guide.

**java-sync:**

```java
BsonDocument masterKeyProperties = new BsonDocument();
masterKeyProperties.put("provider", new BsonString(kmsProvider));
masterKeyProperties.put("keyName", new BsonString("<Azure key name>"));
masterKeyProperties.put("keyVaultEndpoint", new BsonString("<Azure key vault endpoint"));
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

**csharp:**

```csharp
kmsProviders.Add(provider, azureKmsOptions);
var dataKeyOptions = new DataKeyOptions(
masterKey: new BsonDocument
{
   { "keyName", "<Your Azure Key Name>" },
   { "keyVaultEndpoint", "<Your Azure Key Vault Endpoint>" },
});
```

**go:**

```go
masterKey := map[string]interface{}{
	"keyVaultEndpoint": "<Your Azure Key Vault Endpoint>",
	"keyName":          "<Your Azure Key Name>",
}
```

**Step 3: Generate your Data Encryption Key**

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
BsonBinary dataKeyId = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions().masterKey(masterKeyProperties));
String base64DataKeyId = Base64.getEncoder().encodeToString(dataKeyId.getData());
System.out.println("DataKeyId [base64]: " + base64DataKeyId);
clientEncryption.close();
```

**nodejs:**

```javascript
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
await client.connect();

const encryption = new ClientEncryption(client, {
  keyVaultNamespace,
  kmsProviders,
});
const key = await encryption.createDataKey(provider, {
  masterKey: masterKey,
});
console.log("DataKeyId [base64]: ", key.toString("base64"));
await keyVaultClient.close();
await client.close();
```

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
data_key_id = client_encryption.create_data_key(provider, master_key)

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
var dataKeyId = clientEncryption.CreateDataKey(provider, dataKeyOptions, CancellationToken.None);
var dataKeyIdBase64 = Convert.ToBase64String(GuidConverter.ToBytes(dataKeyId, GuidRepresentation.Standard));
Console.WriteLine($"DataKeyId [base64]: {dataKeyIdBase64}");
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
dataKeyOpts := options.DataKey().
	SetMasterKey(masterKey)

dataKeyID, err := clientEnc.CreateDataKey(context.TODO(), provider, dataKeyOpts)
if err != nil {
	return fmt.Errorf("create data key error %v", err)
}

fmt.Printf("DataKeyId [base64]: %s\n", base64.StdEncoding.EncodeToString(dataKeyID.Data))
```

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an Azure Key Vault, see
csfle-reference-kms-providers-azure-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in Azure Key Vault, see
csfle-kms-provider-object-azure and
csfle-kms-datakeyopts-azure.

**See also:** Complete Code

**java-sync:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/java/azure/reader/src/main/java/com/mongodb/csfle/MakeDataKey.java).

**nodejs:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/node/azure/reader/make_data_key.js).

**python:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/python/azure/reader/make_data_key.py).

**csharp:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/dotnet/azure/reader/CSFLE/MakeDataKey.cs)

**go:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/go/azure/reader/make-data-key.go).

**Step 4: Configure the MongoClient**

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

**Step 2: Specify your Azure Credentials**

Specify the `azure` KMS provider and your Azure
credentials:

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
    "azure": {
        "tenantId": "<Azure account organization>",
        "clientId": "<Azure client ID>",
        "clientSecret": "<Azure client secret>",
    }
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var provider = "azure";
var azureKmsOptions = new Dictionary<string, object>
{
   { "tenantId", "<Your Azure Tenant ID>" },
   { "clientId", "<Your Azure Client ID>" },
   { "clientSecret", "<Your Azure Client Secret>" },
};
kmsProviders.Add(provider, azureKmsOptions);
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
  useNewUrlParser: true,
  useUnifiedTopology: true,
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
`MongoClient` instance to insert an encrypted document into the
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

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/java/azure/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

**nodejs:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/node/azure/reader/insert_encrypted_document.js).

**python:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/python/azure/reader/insert_encrypted_document.py).

**csharp:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/dotnet/azure/reader/CSFLE/InsertEncryptedDocument.cs)

**go:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/go/azure/reader/insert-encrypted-document.go).

**Step 7: Retrieve Your Encrypted Document**

Retrieve the encrypted document you inserted in the
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

To view the complete code for finding an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/java/azure/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

**nodejs:**

To view the complete code for finding an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/node/azure/reader/insert_encrypted_document.js).

**python:**

To view the complete code for finding an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/python/azure/reader/insert_encrypted_document.py).

**csharp:**

To view the complete code for finding an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/dotnet/azure/reader/CSFLE/InsertEncryptedDocument.cs)

**go:**

To view the complete code for finding an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/csfle/go/azure/reader/insert-encrypted-document.go).

## Learn More

To learn how CSFLE works, see
csfle-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Learn more about CSFLE components on the Reference page.
- Learn how Customer Master Keys and Data Encryption Keys work on the csfle-reference-keys-key-vaults page
- See how KMS Providers manage your CSFLE keys on the csfle-reference-kms-providers page.
