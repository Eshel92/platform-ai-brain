<!-- Converted from core/queryable-encryption/tutorials/aws/aws-automatic.txt (reStructuredText). Includes are inlined. -->

# Use Automatic Queryable Encryption with AWS

## Overview

This guide shows you how to build a Queryable Encryption enabled
application using Amazon Web Services (AWS) KMS ({+kms-long+}).

After you complete the steps in this guide, you should have:

- A Customer Master Key hosted on an AWS KMS instance.
- A working client application that inserts encrypted documents
  using your Customer Master Key.

## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.

**See also:** Full Application

To see the complete code for the application you make in this guide,
select the tab corresponding to your programming language and follow
the provided link:

**shell:**

[Complete Mongosh Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/aws/reader/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/aws/reader/)

**python:**

[Complete Python Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/aws/reader/)

**java-sync:**

[Complete Java Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/aws/reader/)

**go:**

[Complete Go Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/aws/reader/)

**csharp:**

[Complete C# Application](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/aws/reader/)

## Set Up the KMS

**Step 1: Create the Customer Master Key**

**Step 1: Log in to your [AWS Management Console](https://aws.amazon.com/console/).**

**Step 2: Navigate to the [AWS KMS Console](https://aws.amazon.com/kms/).**

**Step 3: Create your Customer Master Key**

Create a new symmetric key by following the official AWS
documentation on
[Creating symmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk).
The key you create is your Customer Master Key.
Choose a name and description that helps you identify it;
these fields do not affect the functionality or configuration of your CMK ({+cmk-long+}).

In the Usage Permissions step of the key generation
process, apply the following default key policy that enables
Identity and Access Management (IAM (Identity and Access Management)) policies to
grant access to your Customer Master Key:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "<ARN of your AWS account principal>"
      },
      "Action": "kms:*",
      "Resource": "*"
    }
  ]
}
```

**Important:**

Record the Amazon Resource Name (ARN (Amazon Resource Name)) and Region of
your Customer Master Key. You will use these in later steps of this guide.

**Tip:** Learn More

To learn more about your Customer Master Keys, see
qe-reference-keys-key-vaults.

To learn more about key policies, see
[Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)
in the official AWS documentation.

**Step 4: Create an AWS IAM User**

**Step 1: Navigate to the [AWS IAM Console](https://aws.amazon.com/iam/).**

**Step 2: Create an IAM User**

Create a new programmatic IAM (Identity and Access Management)
user in the AWS management console by
following the official AWS documentation on
[Adding a User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).
You will use this IAM (Identity and Access Management) user as a service account for your Queryable Encryption enabled application.
Your application authenticates with AWS KMS using the IAM (Identity and Access Management)
user to encrypt and decrypt your Data Encryption Keys (DEKs) with your Customer Master Key
(CMK).

**Important:** Record your Credentials

Ensure you record the following IAM (Identity and Access Management) credentials in the final
step of creating your IAM (Identity and Access Management) user:

- **access key ID**
- **secret access key**

You have one opportunity to record these credentials. If you do
not record these credentials during this step, you must create
another IAM (Identity and Access Management) user.

**Step 3: Grant Permissions**

Grant your IAM (Identity and Access Management) user `kms:Encrypt` and `kms:Decrypt` permissions for
your remote master key.

**Important:**

The new client IAM (Identity and Access Management) user *should not* have administrative permissions
for the master key. To keep your data secure, follow the
[principle of least privilege](https://en.wikipedia.org/w/index.php?title=Principle_of_least_privilege&oldid=1080333157).

The following inline policy allows an IAM (Identity and Access Management) user to encrypt and decrypt
with the Customer Master Key with the least privileges possible:

**Note:** Remote Master Key ARN

The following policy requires the ARN (Amazon Resource Name) of the key you generate in the
Create the Master Key step of this guide.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["kms:Decrypt", "kms:Encrypt"],
      "Resource": "<the Amazon Resource Name (ARN) of your remote master key>"
    }
  ]
}
```

To apply the preceding policy to your IAM (Identity and Access Management) user, follow the
[Adding IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console)
guide in the AWS documentation.

**Important:** Authenticate with IAM Roles in Production

When deploying your Queryable Encryption enabled application to a production environment,
authenticate your application through an IAM (Identity and Access Management) role
instead of an IAM (Identity and Access Management) user.

To authenticate with an IAM (Identity and Access Management) role, specify your temporary
IAM (Identity and Access Management) role credentials in your KMS provider
object as follows:

```json
{
    "accessKeyId":"<temporary access key ID>",
    "secretAccessKey":"<temporary secret access key>",
    "sessionToken":"<temporary session token>"
}
```

You can get your temporary IAM (Identity and Access Management) role credentials
through the following mechanisms:

- [Call AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
- [Retrieve Credentials from EC2 Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#instance-metadata-security-credentials)

Your application must include logic to get new temporary credentials
and recreate your Queryable Encryption enabled `MongoClient` instance when each set of
temporary credentials expires.

To learn more about IAM (Identity and Access Management) roles, see the following
pages in the official AWS documentation:

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [When to create an IAM role (instead of a user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_which-to-choose_role)

To learn how to get temporary credentials and assume a role in each of
the languages supported in this guide, see the following `AssumeRole`
runnable examples in the AWS documentation:

- [Java](https://docs.aws.amazon.com/code-samples/latest/catalog/javav2-sts-src-main-java-com-example-sts-AssumeRole.java.html)
- [NodeJS](https://docs.aws.amazon.com/code-samples/latest/catalog/javascriptv3-sts-src-sts_assumerole.js.html)
- [Python](https://docs.aws.amazon.com/code-samples/latest/catalog/python-sts-sts_temporary_credentials-assume_role_mfa.py.html)
  (example uses multi-factor authentication)
- [C#](https://docs.aws.amazon.com/code-samples/latest/catalog/dotnetv3-STS-AssumeRole-AssumeRoleExample-AssumeRole.cs.html)
- [Go](https://docs.aws.amazon.com/code-samples/latest/catalog/go-sts-TakeRole-TakeRole.go.html)

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

**Step 1: Add your AWS KMS Credentials**

Add the service account credentials to your Queryable Encryption enabled client
code.

Select the tab corresponding to your preferred MongoDB driver:

**Tip:**

You created and recorded your Access Key ID and Secret Access Key
in the Create an IAM User
step of this guide.

**shell:**

```javascript
const provider = "aws";
const kmsProviders = {
  aws: {
    accessKeyId: "<Your AWS Access Key ID>",
    secretAccessKey: "<Your AWS Secret Access Key>",
  },
};
```

**nodejs:**

```javascript
const provider = "aws";
const kmsProviders = {
  aws: {
    accessKeyId: "<Your AWS Access Key ID>",
    secretAccessKey: "<Your AWS Secret Access Key>",
  },
};
```

**python:**

```python
provider = "aws"
kms_providers = {
    provider: {
        "accessKeyId": "<IAM User Access Key ID>",
        "secretAccessKey": "<IAM User Secret Access Key>",
    }
}
```

**java-sync:**

```java
Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
String kmsProvider = "aws";
Map<String, Object> providerDetails = new HashMap<>();
providerDetails.put("accessKeyId", new BsonString("<IAM User Access Key ID>"));
providerDetails.put("secretAccessKey", new BsonString("<IAM User Secret Access Key>"));
kmsProviders.put(kmsProvider, providerDetails);
```

**go:**

```go
provider := "aws"
kmsProviders := map[string]map[string]interface{}{
	provider: {
		"accessKeyId":     "<Your AWS Access Key ID>",
		"secretAccessKey": "<Your AWS Secret Access Key>",
	},
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
const string provider = "aws";
var awsKmsOptions = new Dictionary<string, object>
{
   { "accessKeyId", "<Your AWS Access Key ID>" },
   { "secretAccessKey", "<Your AWS Secret Access Key>" }
};
kmsProviders.Add(provider, awsKmsOptions);
```

**Tip:** Learn More

To learn more about the KMS provider object for AWS, see
qe-reference-kms-providers-aws.

**Step 2: Add Your Key Information**

Update the following code to specify your Customer Master Key:

**Tip:**

You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
in the Create a Customer Master Key
step of this guide.

**shell:**

```javascript
const masterKey = {
  key: "<Your AWS Key ARN>",
  region: "<Your AWS Key Region>",
};
```

**nodejs:**

```javascript
const masterKey = {
  key: "<Your AWS Key ARN>",
  region: "<Your AWS Key Region>",
};
```

**python:**

```python
master_key = {"region": "<Master Key AWS Region>", "key": "<Master Key ARN>"}
```

**java-sync:**

```java
masterKeyProperties.put("provider", new BsonString(kmsProvider));
masterKeyProperties.put("key", new BsonString("<Master Key ARN>"));
masterKeyProperties.put("region", new BsonString("<Master Key AWS Region>"));
```

**go:**

```go
masterKey := map[string]interface{}{
	"key":    "<Your AWS Key ARN>",
	"region": "<Your AWS Key Region>",
}
```

**csharp:**

```csharp
DataKeyOptions GetDataKeyOptions(List<string> altNames)
{
    var dataKeyOptions = new DataKeyOptions(
       alternateKeyNames: altNames,
       masterKey: new BsonDocument
       {
           { "region", "<Your AWS Key Region>" },
           { "key", "<Your AWS Key ARN>" },
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

Use a Queryable Encryption enabled `MongoClient` instance to specify what
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

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an AWS KMS, see
qe-reference-kms-providers-aws-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in AWS KMS, see
qe-kms-datakeyopts-aws.

**See also:** Complete Code

**shell:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/aws/reader/make_data_key.js).

**nodejs:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/aws/reader/make_data_key.js).

**python:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/aws/reader/make_data_key.py).

**java-sync:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/aws/reader/src/main/java/com/mongodb/qe/MakeDataKey.java).

**go:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/aws/reader/make-data-key.go).

**csharp:**

To view the complete code for making a Data Encryption Key, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/aws/reader/QueryableEncryption/MakeDataKey.cs).

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

**go:**

```go
keyVaultColl := "__keyVault"
keyVaultDb := "encryption"
keyVaultNamespace := keyVaultDb + "." + keyVaultColl
```

**java-sync:**

```java
String keyVaultDb = "encryption";
String keyVaultColl = "__keyVault";
String keyVaultNamespace = keyVaultDb + "." + keyVaultColl;
```

**csharp:**

```csharp
var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
```

**Step 2: Specify your AWS Credentials**

Specify the `aws` KMS provider and your IAM (Identity and Access Management) user
credentials:

**Tip:**

You created and recorded your Access Key ID and Secret Access Key
in the Create an IAM User
step of this guide.

**shell:**

```javascript
const kmsProviders = {
  aws: {
    accessKeyId: "<Your AWS Access Key ID>",
    secretAccessKey: "<Your AWS Secret Access Key>",
  },
};
```

**nodejs:**

```javascript
const kmsProviders = {
  aws: {
    accessKeyId: "<Your AWS Access Key ID>",
    secretAccessKey: "<Your AWS Secret Access Key>",
  },
};
```

**python:**

```python
provider = "aws"
kms_providers = {
    provider: {
        "accessKeyId": "<IAM User Access Key ID>",
        "secretAccessKey": "<IAM User Secret Access Key>",
    }
}
```

**java-sync:**

```java
Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
String kmsProvider = "aws";
Map<String, Object> providerDetails = new HashMap<>();
providerDetails.put("accessKeyId", "<IAM User Access Key ID>");
providerDetails.put("secretAccessKey", "<IAM User Secret Access Key>");
kmsProviders.put(kmsProvider, providerDetails);
```

**go:**

```go
kmsProviders := map[string]map[string]interface{}{
	"aws": {
		"accessKeyId":     "<Your AWS Access Key ID>",
		"secretAccessKey": "<Your AWS Secret Access Key>",
	},
}
```

**csharp:**

```csharp
var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
const string provider = "aws";
var awsKmsOptions = new Dictionary<string, object>
{
   { "accessKeyId", "<Your AWS Access Key ID>" },
   { "secretAccessKey", "<Your AWS Secret Access Key>" }
};
kmsProviders.Add(provider, awsKmsOptions);
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

**Note:** Automatic Encryption Options

The automatic encryption options provide configuration
information to the Automatic Encryption Shared Library,
which modifies the application's behavior when accessing encrypted fields.

To learn more about the Automatic Encryption Shared Library, see
the qe-reference-shared-library page.

**Step 5: Create the MongoClient**

Instantiate a MongoDB client object with the following
automatic encryption settings:

**shell:**

```javascript
const autoEncryptionOptions = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
  bypassQueryAnalysis: false,
  encryptedFieldsMap: encryptedFieldsMap,
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
  },
});
await encryptedClient.connect();
```

**python:**

```python
secure_client = MongoClient(connection_string, auto_encryption_opts=auto_encryption)
```

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

**go:**

```go
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
```

**csharp:**

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(connectionString);
var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace,
    kmsProviders,
    encryptedFieldsMap: encryptedFieldsMap,
    extraOptions: extraOptions
    );
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
var secureClient = new MongoClient(clientSettings);
```

**Step 6: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert an encrypted document into the
`medicalRecords.patients` namespace using the following code
snippet:

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

When you insert a document, your Queryable Encryption enabled client
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

**shell:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/aws/reader/insert_encrypted_document.js).

**nodejs:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/aws/reader/insert_encrypted_document.js).

**python:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/aws/reader/insert_encrypted_document.py).

**java-sync:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/aws/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**go:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/aws/reader/insert-encrypted-document.go).

**csharp:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/aws/reader/QueryableEncryption/InsertEncryptedDocument.cs).

**Step 7: Retrieve Your Encrypted Document**

Retrieve the encrypted document you inserted in the
Insert a Document with Encrypted Fields
step of this guide.

To show the functionality of Queryable Encryption, the following code snippet queries for
your document with a client configured for automatic Queryable Encryption as well as
a client that is not configured for automatic Queryable Encryption.

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

**java-sync:**

```java
System.out.println("Finding a document with regular (non-encrypted) client.");
Document docRegular = regularClient.getDatabase(encryptedDbName).getCollection(encryptedCollName).find(eq("firstName", "Jon")).first();
System.out.println(docRegular.toJson());
System.out.println("Finding a document with encrypted client, searching on an encrypted field");
Document docSecure = mongoClientSecure.getDatabase(encryptedDbName).getCollection(encryptedCollName).find(eq("patientRecord.ssn", "987-65-4320")).first();
System.out.println(docSecure.toJson());
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

**shell:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/aws/reader/insert_encrypted_document.js).

**nodejs:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/aws/reader/insert_encrypted_document.js).

**python:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/aws/reader/insert_encrypted_document.py).

**java-sync:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/aws/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**go:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/aws/reader/insert-encrypted-document.go).

**csharp:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/aws/reader/QueryableEncryption/InsertEncryptedDocument.cs).

## Learn More

To learn how Queryable Encryption works, see
qe-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Learn more about Queryable Encryption components on the Reference page.
- Learn how Customer Master Keys and Data Encryption Keys work on the qe-reference-keys-key-vaults page.
- See how KMS Providers manage your Queryable Encryption keys on the qe-fundamentals-kms-providers page.
