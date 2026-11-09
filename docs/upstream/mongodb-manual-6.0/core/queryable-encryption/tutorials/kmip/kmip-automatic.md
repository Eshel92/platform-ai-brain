<!-- Converted from core/queryable-encryption/tutorials/kmip/kmip-automatic.txt (reStructuredText). Includes are inlined. -->

# Use Automatic Queryable Encryption with KMIP

## Overview

This guide shows you how to build a Queryable Encryption (QE (Queryable Encryption))-enabled
application using a Key Management Interoperability Protocol
(KMIP)-compliant key provider.

After you complete the steps in this guide, you should have:

- A Customer Master Key hosted on a {+kmip-hover+}-compliant key provider.
- A working client application that inserts encrypted documents
  using your Customer Master Key.

## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.

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

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/kmip/reader/)

**shell:**

[Complete Mongosh Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/kmip/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/kmip/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/kmip/reader/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/kmip/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/kmip/reader/QueryableEncryption/)

## Set Up the KMS

**java-sync:**

```java
// You are viewing the Java synchronous driver code examples.
// Use the dropdown menu to select a different driver.
```

**shell:**

```javascript
// You are viewing the Mongosh driver code examples.
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

**Important:**

When building or running the Golang code in this guide using 
`go build` or `go run`, always include the `cse` build 
constraint to enable CSFLE. See the following shell
command for an example of including the build constraint:

```bash
go run -tags cse insert-encrypted-document.go
```

**Step 1: Configure your KMIP-Compliant Key Provider**

To connect a MongoDB driver client to your {+kmip-hover+}-compliant key provider, you must configure
your {+kmip-hover+}-compliant key provider such that it accepts your client's TLS certificate.

Consult the documentation for your {+kmip-hover+}-compliant key provider for
information on how to accept your client certificate.

**Step 2: Specify your Certificates**

Your client must connect to your {+kmip-hover+}-compliant key provider through TLS and present
a client certificate that your {+kmip-hover+}-compliant key provider accepts:

**java-sync:**

Specify the following Java system properties to configure your client's
TLS connection: 

```shell
-Djavax.net.ssl.keyStoreType=pkcs12
-Djavax.net.ssl.keyStore=<path to pkcs12 KeyStore containing your client certificate>
-Djavax.net.ssl.keyStorePassword=<KeyStore password>
```

**Note:** Configure Client With SSLContext

If you would rather configure your client application using an SSL context, use the 
[kmsProviderSslContextMap](https://mongodb.github.io/mongo-java-driver/{+java-driver-version+}/apidocs/mongodb-driver-core/com/mongodb/ClientEncryptionSettings.Builder.html#kmsProviderSslContextMap(java.util.Map))
method.

**shell:**

```javascript
const tlsOptions = {
  kmip: {
    tlsCAFile:
      "<path to file containing your Certificate Authority certificate>",
    tlsCertificateKeyFile: "<path to your client certificate file>",
  },
};
```

**nodejs:**

```javascript
const tlsOptions = {
  kmip: {
    tlsCAFile:
      "<path to file containing your Certificate Authority certificate>",
    tlsCertificateKeyFile: "<path to your client certificate file>",
  },
};
```

**python:**

```python
tls_options = {
    "kmip": {
        "tlsCAFile": "<path to file containing your Certificate Authority certificate>",
        "tlsCertificateKeyFile": "<path to your client certificate file>",
    }
}
```

**csharp:**

```csharp
var tlsOptions = new Dictionary<string, SslSettings>();
var sslSettings = new SslSettings();
var clientCertificate = new X509Certificate2("<path to your pkcs12 client certificate file>");
sslSettings.ClientCertificates = new List<X509Certificate>() {
    clientCertificate,
 };
tlsOptions.Add(provider, sslSettings);
```

**Important:**

Your client certificate must be in pcks12 format. You can convert
your certificate using openssl with the following command:

```shell
openssl pcks12 -export -out "<new pcks12 certificate>" -in "<certificate to convert>" \
-name "<new certificate name>" -password "<new certificate password>"
```

**go:**

```go
tlsConfig := make(map[string]*tls.Config)
tlsOpts := map[string]interface{}{
	"tlsCertificateKeyFile": "<path to your client certificate file>",
	"tlsCAFile":             "<path to file containing your Certificate Authority certificate>",
}
kmipConfig, err := options.BuildTLSConfig(tlsOpts)
tlsConfig["kmip"] = kmipConfig
```

**Important:**

You must use certificates with [ECDSA keys](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) 
when using the Go driver.

## Create the Application

Select the tab that corresponds to the MongoDB driver you are using in
your application to see relevant code samples.

**Step 1: Create a Unique Index on Your Key Vault Collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` collection.

Select the tab corresponding to your preferred MongoDB driver:

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

**Step 2: Create a Data Encryption Key**

**Step 1: Add your Endpoint**

Specify the URI endpoint of your {+kmip-hover+}-compliant key provider:

**java-sync:**

```java
String kmsProvider = "kmip";
Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
Map<String, Object> providerDetails = new HashMap<>();
providerDetails.put("endpoint", "<endpoint for your KMIP-compliant key provider>");
kmsProviders.put(kmsProvider, providerDetails);
```

**shell:**

```javascript
const provider = "kmip";
const kmsProviders = {
  kmip: {
    endpoint: "<endpoint for your KMIP-compliant key provider>",
  },
};
```

**nodejs:**

```javascript
const provider = "kmip";
const kmsProviders = {
  kmip: {
    endpoint: "<endpoint for your KMIP-compliant key provider>",
  },
};
```

**python:**

```python
provider = "kmip"
kms_providers = {
    provider: {"endpoint": "<endpoint for your KMIP-compliant key provider>"}
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var provider = "kmip";
var kmipKmsOptions = new Dictionary<string, object>
{
   { "endpoint", "<endpoint for your KMIP-compliant key provider>" },
};
kmsProviders.Add(provider, kmipKmsOptions);
```

**go:**

```go
provider := "kmip"
kmsProviders := map[string]map[string]interface{}{
	provider: {
		"endpoint": "<endpoint for your KMIP-compliant key provider>",
	},
}
```

**Step 2: Add Your Key Information**

The following code prompts your {+kmip-hover+}-compliant key provider to automatically generate a Customer Master Key:

**java-sync:**

```java
BsonDocument masterKeyProperties = new BsonDocument(); // an empty key object prompts your KMIP-compliant key provider to generate a new Customer Master Key
```

**shell:**

```javascript
const masterKey = {}; // an empty key object prompts your KMIP-compliant key provider to generate a new Customer Master Key
```

**nodejs:**

```javascript
const masterKey = {}; // an empty key object prompts your KMIP-compliant key provider to generate a new Customer Master Key
```

**python:**

```python
master_key = (
    {}
)  # an empty key object prompts your KMIP-compliant key provider to generate a new Customer Master Key
```

**csharp:**

```csharp
DataKeyOptions GetDataKeyOptions(List<string> altNames)
{
    var dataKeyOptions = new DataKeyOptions(
        alternateKeyNames: altNames,
        masterKey: new BsonDocument { } // an empty key object prompts your KMIP-compliant key provider to generate a new Customer Master Key
    );
    return dataKeyOptions;
}
```

**go:**

```go
masterKey := map[string]interface{}{} // an empty key object prompts your KMIP-compliant key provider to generate a new Customer Master Key
```

**Step 3: Generate your Data Encryption Keys**

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
List<String> keyAlts3 = new ArrayList<String>();
keyAlts3.add("dataKey3");
BsonBinary dataKeyId3 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
        .keyAltNames(keyAlts3));
List<String> keyAlts4 = new ArrayList<String>();
keyAlts4.add("dataKey4");
BsonBinary dataKeyId4 = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions()
        .keyAltNames(keyAlts4));
```

**shell:**

```javascript
const autoEncryptionOpts = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
  tlsOptions: tlsOptions,
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
  tlsOptions,
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
    kms_tls_options=tls_options,
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

**csharp:**

```csharp
var clientEncryptionOptions = new ClientEncryptionOptions(
    keyVaultClient,
    keyVaultNamespace,
    kmsProviders: kmsProviders,
    tlsOptions: tlsOptions
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

**go:**

```go
clientEncryptionOpts := options.ClientEncryption().SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviders).SetTLSConfig(tlsConfig)
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

**See also:** Complete Code

**java-sync:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/kmip/reader/src/main/java/com/mongodb/qe/MakeDataKey.java).

**shell:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/kmip/reader/make_data_key.js).

**nodejs:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/kmip/reader/make_data_key.js).

**python:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/kmip/reader/make_data_key.py).

**csharp:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/kmip/reader/QueryableEncryption/MakeDataKey.cs).

**go:**

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/kmip/reader/make-data-key.go).

**Step 4: Configure the MongoClient**

**Step 1: Specify the Key Vault Collection Namespace**

Specify `encryption.__keyVault` as the Key Vault collection
namespace.

**java-sync:**

```java
String keyVaultDb = "encryption";
String keyVaultColl = "__keyVault";
String keyVaultNamespace = keyVaultDb + "." + keyVaultColl;
```

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

**csharp:**

```csharp
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
```

**go:**

```go
keyVaultColl := "__keyVault"
keyVaultDb := "encryption"
keyVaultNamespace := keyVaultDb + "." + keyVaultColl
```

**Step 2: Specify your KMIP Endpoint**

Specify `kmip` in your `kmsProviders` object and enter
the URI endpoint of your {+kmip-hover+}-compliant key provider:

**java-sync:**

```java
String kmsProvider = "kmip";
Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
Map<String, Object> providerDetails = new HashMap<>();
providerDetails.put("endpoint", "<endpoint for your KMIP-compliant key provider>");
kmsProviders.put(kmsProvider, providerDetails);
```

**shell:**

```javascript
const provider = "kmip";
const kmsProviders = {
  kmip: {
    endpoint: "<endpoint for your KMIP-compliant key provider>",
  },
};
```

**nodejs:**

```javascript
const provider = "kmip";
const kmsProviders = {
  kmip: {
    endpoint: "<endpoint for your KMIP-compliant key provider>",
  },
};
```

**python:**

```python
provider = "kmip"
kms_providers = {
    provider: {"endpoint": "<endpoint for your KMIP-compliant key provider>"}
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var provider = "kmip";
var kmipKmsOptions = new Dictionary<string, object>
{
   { "endpoint", "<endpoint for your KMIP-compliant key provider>" },
};
kmsProviders.Add(provider, kmipKmsOptions);
```

**go:**

```go
provider := "kmip"
kmsProviders := map[string]map[string]interface{}{
	provider: {
		"endpoint": "<endpoint for your KMIP-compliant key provider>",
	},
}
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
```

**Tip:** Further Reading on Schemas

To view an in-depth description of how to construct the schema you use
in this step, see the csfle-fundamentals-create-schema guide.

To view a list of all supported encryption rules for your
encryption schemas, see the
csfle-reference-encryption-schemas guide.

**Step 4: Specify the Location of the Automatic Encryption Shared Library**

**shell:**

```none
// mongosh does not require you to specify the
// location of the Automatic Encryption Shared Library 
```

**nodejs:**

```javascript
const extraOptions = {
  cryptSharedLibPath: "<path to FLE Shared Library>",
};
```

**python:**

```python
auto_encryption = AutoEncryptionOpts(
    kms_providers,
    key_vault_namespace,
    encrypted_fields_map=encrypted_fields_map,
    kms_tls_options=tls_options,
    schema_map=None,
    crypt_shared_lib_path="<path to FLE Shared Library>",
)
```

**java-sync:**

```java
Map<String, Object> extraOptions = new HashMap<String, Object>();
extraOptions.put("cryptSharedLibPath", "<path to crypt_shared>");
```

**go:**

```go
extraOptions := map[string]interface{}{
	"cryptSharedLibPath": "<Your Crypt Shared lib Path>",
}
```

**csharp:**

```csharp
var extraOptions = new Dictionary<string, object>()
{
   { "cryptSharedLibPath", "<path to crypt_shared library>" },
};
```

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
                .encryptedFieldsMap(encryptedFieldsMap)
                .extraOptions(extraOptions)
                .build())
        .build();
MongoClient mongoClientSecure = MongoClients.create(clientSettings);
```

**shell:**

```javascript
const autoEncryptionOptions = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
  bypassQueryAnalysis: false,
  encryptedFieldsMap: encryptedFieldsMap,
  tlsOptions: tlsOptions,
};

const encryptedClient = Mongo(uri, autoEncryptionOptions);
const encryptedColl = encryptedClient
  .getDB(secretDB)
  .getCollection(secretColl);
const unencryptedColl = unencryptedClient
  .getDB(secretDB)
  .getCollection(secretColl);
```

**nodejs:**

```javascript
const encryptedClient = new MongoClient(uri, {
  autoEncryption: {
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders,
    extraOptions: extraOptions,
    encryptedFieldsMap: encryptedFieldsMap,
    tlsOptions,
  },
});
await encryptedClient.connect();
```

**python:**

```python
secure_client = MongoClient(connection_string, auto_encryption_opts=auto_encryption)
```

**csharp:**

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(connectionString);
var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace,
    kmsProviders,
    encryptedFieldsMap: encryptedFieldsMap,
    extraOptions: extraOptions,
    tlsOptions: tlsOptions
    );
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
var secureClient = new MongoClient(clientSettings);
```

**go:**

```go
autoEncryptionOpts := options.AutoEncryption().
	SetKmsProviders(kmsProviders).
	SetKeyVaultNamespace(keyVaultNamespace).
	SetEncryptedFieldsMap(encryptedFieldsMap).
	SetExtraOptions(extraOptions).SetTLSConfig(tlsConfig)
secureClient, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOpts))
if err != nil {
	return fmt.Errorf("Connect error for encrypted client: %v", err)
}
defer func() {
	_ = secureClient.Disconnect(context.TODO())
}()
```

**Step 6: Insert a Document with Encrypted Fields**

Use your QE (Queryable Encryption)-enabled
`MongoClient` instance to insert an encrypted document into the
`medicalRecords.patients` namespace using the following code
snippet:

**java-sync:**

```java
ArrayList<String> medications = new ArrayList<>();
medications.add("Atorvastatin");
medications.add("Levothyroxine");

Document patientRecord = new Document()
        .append("ssn", "987-65-4320")
        .append("billing", new Document().append("type", "Visa").append("number", "4111111111111111"));

Document patient = new Document()
        .append("firstName", "Jon")
        .append("lastName", "Doe")
        .append("patientId", 12345678)
        .append("address", "AB+")
        .append("medications", medications)
        .append("patientRecord", patientRecord);
mongoClientSecure.getDatabase(encryptedDbName).getCollection(encryptedCollName).insertOne(patient);
```

**shell:**

```javascript
encryptedColl.insertOne({
  firstName: "Jon",
  lastName: "Doe",
  patientId: 12345678,
  address: "157 Electric Ave.",
  patientRecord: {
    ssn: "987-65-4320",
    billing: {
      type: "Visa",
      number: "4111111111111111",
    },
  },
  medications: ["Atorvastatin", "Levothyroxine"],
});
```

**nodejs:**

```javascript
const encryptedColl = encryptedClient
  .db(secretDB)
  .collection(secretCollection);
await encryptedColl.insertOne({
  firstName: "Jon",
  lastName: "Doe",
  patientId: 12345678,
  address: "157 Electric Ave.",
  patientRecord: {
    ssn: "987-65-4320",
    billing: {
      type: "Visa",
      number: "4111111111111111",
    },
  },
  medications: ["Atorvastatin", "Levothyroxine"],
});
```

**python:**

```python
encrypted_coll = secure_client[encrypted_db_name][encrypted_coll_name]
encrypted_coll.insert_one(
    {
        "firstName": "Jon",
        "lastName": "Doe",
        "patientId": 12345678,
        "address": "157 Electric Ave.",
        "patientRecord": {
            "ssn": "987-65-4320",
            "billing": {
                "type": "Visa",
                "number": "4111111111111111",
            },
        },
        "medications": ["Atorvastatin", "Levothyroxine"],
    }
)
```

**csharp:**

```csharp
var sampleDocument = new BsonDocument
{
    {"firstName", "Jon"},
    {"lastName", "Doe"},
    {"patientId", 12345678},
    {"address", "157 Electric Ave."},
    {
        "medications", new BsonArray
        {
            new BsonString("Atorvastatin"),
            new BsonString("Levothyroxine")
        }
    },
    {
        "patientRecord", new BsonDocument
        {
            {"ssn", new BsonString("987-65-4320")},
            {
                "billing", new BsonDocument
                {
                    {"type", new BsonString("Visa")},
                    {"number", "4111111111111111"}
                }
            }
        }
    }
};

var secureCollection = secureClient.GetDatabase(encryptedCollectionNamespace.DatabaseNamespace.DatabaseName)
    .GetCollection<BsonDocument>(encryptedCollectionNamespace.CollectionName);
secureCollection.InsertOne(sampleDocument);
```

**go:**

```go
test_patient := map[string]interface{}{
	"firstName":   "Jon",
	"lastName":    "Doe",
	"patientId":   12345678,
	"address":     "157 Electric Ave.",
	"medications": []string{"Atorvastatin", "Levothyroxine"},
	"patientRecord": map[string]interface{}{
		"ssn": "987-65-4320",
		"billing": map[string]interface{}{
			"type":   "Visa",
			"number": "4111111111111111",
		},
	},
}
if _, err := secureClient.Database(dbName).Collection(collName).InsertOne(context.TODO(), test_patient); err != nil {
	return fmt.Errorf("InsertOne error: %v", err)
}
```

**Note:**

Rather than creating a raw BSON document, you can pass a struct with `bson` tags directly
to the driver for encoding.

When you insert a document, your Queryable Encryption-enabled client
encrypts the fields of your document such that it resembles the following:

```json
{
  "_id": { "$oid": "<_id value>" },
  "firstName": "Jon",
  "lastName": "Doe",
  "patientId": {
    "$binary": {
      "base64": "<ciphertext>",
      "subType": "06"
    }
  },
  "address": "157 Electric Ave.",
  "patientRecord": {
    "ssn": {
      "$binary": {
        "base64": "<ciphertext>",
        "subType": "06"
      }
    },
    "billing": {
      "$binary": {
        "base64": "<ciphertext>",
        "subType": "06"
      }
    }
  },
  "medications": {
    "$binary": {
      "base64": "<ciphertext>",
      "subType": "06"
    }
  },
  "__safeContent__": [
    {
      "$binary": {
        "base64": "<ciphertext>",
        "subType": "00"
      }
    },
    {
      "$binary": {
        "base64": "<ciphertext>",
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

**java-sync:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/kmip/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**shell:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/kmip/reader/insert_encrypted_document.js).

**nodejs:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/kmip/reader/insert_encrypted_document.js).

**python:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/kmip/reader/insert_encrypted_document.py).

**csharp:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/kmip/reader/QueryableEncryption/InsertEncryptedDocument.cs)

**go:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/kmip/reader/insert-encrypted-document.go).

**Step 7: Retrieve Your Encrypted Document**

Retrieve the encrypted document you inserted in the
Insert a Document with Encrypted Fields
step of this guide.

To show the functionality of QE (Queryable Encryption), the following code snippet queries for
your document with a client configured for automatic QE (Queryable Encryption) as well as
a client that is not configured for automatic QE (Queryable Encryption).

**java-sync:**

```java
System.out.println("Finding a document with regular (non-encrypted) client.");
Document docRegular = regularClient.getDatabase(encryptedDbName).getCollection(encryptedCollName).find(eq("firstName", "Jon")).first();
System.out.println(docRegular.toJson());
System.out.println("Finding a document with encrypted client, searching on an encrypted field");
Document docSecure = mongoClientSecure.getDatabase(encryptedDbName).getCollection(encryptedCollName).find(eq("patientRecord.ssn", "987-65-4320")).first();
System.out.println(docSecure.toJson());
```

**shell:**

```javascript
console.log("Finding a document with regular (non-encrypted) client.");
console.log(unencryptedColl.findOne({ firstName: /Jon/ }));
console.log(
  "Finding a document with encrypted client, searching on an encrypted field"
);
console.log(encryptedColl.findOne({ "patientRecord.ssn": "987-65-4320" }));
```

**nodejs:**

```javascript
console.log("Finding a document with regular (non-encrypted) client.");
console.log(await unencryptedColl.findOne({ firstName: /Jon/ }));
console.log(
  "Finding a document with encrypted client, searching on an encrypted field"
);
console.log(
  await encryptedColl.findOne({ "patientRecord.ssn": "987-65-4320" })
);
```

**python:**

```python
print("Finding a document with regular (non-encrypted) client.")
pprint.pprint(
    unencryptedClient[encrypted_db_name][encrypted_coll_name].find_one(
        {"firstName": "Jon"}
    )
)
print("Finding a document with encrypted client, searching on an encrypted field")
pprint.pprint(encrypted_coll.find_one({"patientRecord.ssn": "987-65-4320"}))
```

**csharp:**

```csharp
Console.WriteLine("Finding a document with regular (non-encrypted) client.");
var filter = Builders<BsonDocument>.Filter.Eq("firstName", "Jon");
var regularClientEncryptedCollection = regularClient.GetDatabase(encryptedCollectionNamespace.DatabaseNamespace.DatabaseName)
    .GetCollection<BsonDocument>(encryptedCollectionNamespace.CollectionName);
var regularResult = regularClientEncryptedCollection.Find(filter).First();
Console.WriteLine($"\n{regularResult}\n");
Console.WriteLine("Finding a document with encrypted client, searching on an encrypted field");
var encryptedFieldFilter = Builders<BsonDocument>.Filter.Eq("patientRecord.ssn", "987-65-4320");
var secureResult = secureCollection.Find(encryptedFieldFilter).First();
Console.WriteLine($"\n{secureResult}\n");
```

**go:**

```go
fmt.Println("Finding a document with regular (non-encrypted) client.")
var resultRegular bson.M
err = regularClient.Database(dbName).Collection(collName).FindOne(context.TODO(), bson.D{{"firstName", "Jon"}}).Decode(&resultRegular)
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
err = secureClient.Database(dbName).Collection(collName).FindOne(context.TODO(), bson.D{bson.E{"patientRecord.ssn", "987-65-4320"}}).Decode(&resultSecure)
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

```text
Finding a document with regular (non-encrypted) client.
{
  _id: new ObjectId("628eabeb37590e84ea742665"),
  firstName: 'Jon',
  lastName: 'Doe',
  patientId: new Binary(Buffer.from("0798810acc0f4f46c9a76883cee80fca12102e9ddcbcdae46a821fa108a8155a850f2d0919475b6531ada68973d436a199b537a05a98a708c36d2bfec4979d59cbe66878865ce19e392d3e4789d309bdacc336e32efcc851806ae0a41b355288c10d01e39147e1c40d919c41913a0c9d2d3fad0d0d1d2873c4fc82c6c22f27b517df5f3131b331b96ed16a7c5cf89e09082a2d898c2dcd73da91d08760ba74a70077b2d0fdbbe1eea75655a19fcc397812325ad40b102cbd16b8d36b22e11e3f93404f24a8ff68cfdec3c22b0e787cb30078a5227b2a", "hex"), 6),
  address: '157 Electric Ave.',
  patientRecord: {
    ssn: new Binary(Buffer.from("07e8b69630c32f4a00a542af768f8abcf50223edd812ff20b0ecb046ee1a9f5a0eef8d85d99cd26076411129942752516ee605c55aadce73f3d44d81ea6ddbbb8134b108a9deb40d8cab9cb4f08ef210ab0c9d2ea4347f9d235b861baf29751e60abcf059eb5c120305bd5ac05a4e07ac8ccfa6d37283f4cdbfeb7a8accb65b71857d486b5cf55e354d6a95e287d9e2dd65f3f9d9c4c9d0bdb1f26c4bd549d7be77db81796be293e08b2223bac67b212423c4e06568578b5bd7a3c33cedc1b291bcda0b27e005144d344563711a489f24b8e9b65bbb721d3a0e9d9b227a0cec0cbad", "hex"), 6),
    billing: new Binary(Buffer.from("06808ae69d4caa49cf90bb688f386f097f03f870a7b8fcebb1980c9ee5488b1f0f68558fc2163adcd92d00ea5f349f56ed34e7b391f54c48ed2760b4bde73022fc818dc7486a4e046b92ce9c82e00333c7779d9d6bb476713a20632b593b7de54812662cfc4d174d05451d3f4195514e12edba", "hex"), 6)
  },
  medications: new Binary(Buffer.from("06665ec15d38254dc4aa16da856789d33404f27bfea53e0d2fa4deaff166989ab33f469644d89c29112d33b41dbe54ec2d89c43f3de52cdc5d454e8694046216f533614fa7b42b7c5406d6518f7ed8f9e3ce52fda6c8b2146d0f8cc51e21a3467183697e1735a9f60c18e173c1916101", "hex"), 6),
  __safeContent__: [
    new Binary(Buffer.from("3044b134ad0f7c8a90dab1e05bb8b296a8ede540796bd7403ab47693cdba1b26", "hex"), 0),
    new Binary(Buffer.from("a22ddf9a5657cdd56bef72febbba44371899e6486962a1c07d682082c4e65712", "hex"), 0)
  ]
}
Finding a document with encrypted client, searching on an encrypted field
{
  _id: new ObjectId("628eaca1dcf9b63e2f43162d"),
  firstName: 'Jon',
  lastName: 'Doe',
  patientId: 12345678,
  address: '157 Electric Ave.',
  patientRecord: {
    ssn: '987-65-4320',
    billing: { type: 'Visa', number: '4111111111111111' }
  },
  medications: [ 'Atorvastatin', 'Levothyroxine' ],
  __safeContent__: [
    new Binary(Buffer.from("fbdc6cfe3b4659693650bfc60baced27dcb42b793efe09da0ded54d60a9d5a1f", "hex"), 0),
    new Binary(Buffer.from("0f92ff92bf904a858ef6fd5b1e508187f523e791f51d8b64596461b38ebb1791", "hex"), 0)
  ]
}
```

**See also:** Complete Code

**java-sync:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/kmip/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**shell:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/kmip/reader/insert_encrypted_document.js).

**nodejs:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/kmip/reader/insert_encrypted_document.js).

**python:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/kmip/reader/insert_encrypted_document.py).

**csharp:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/kmip/reader/QueryableEncryption/InsertEncryptedDocument.cs)

**go:**

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/kmip/reader/insert-encrypted-document.go).

## Learn More

To learn more about the topics mentioned in this guide, see the
following links:

- qe-reference-keys-key-vaults
- qe-fundamentals-kms-providers
