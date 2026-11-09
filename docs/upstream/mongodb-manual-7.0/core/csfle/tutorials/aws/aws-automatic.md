<!-- Converted from core/csfle/tutorials/aws/aws-automatic.txt (reStructuredText). Includes are inlined. -->

# Use Automatic Client-Side Field Level Encryption with AWS

This guide shows you how to build a Client-Side Field Level Encryption (CSFLE)-enabled
application using Amazon Web Services (AWS) KMS ({+kms-long+}).

After you complete the steps in this guide, you should have:

- A Customer Master Key hosted on an AWS KMS instance.
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

### Full Application Code

[Complete Java Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/aws/reader/)

## Set Up the KMS

```java
// You are viewing the Java synchronous driver code examples.
// Use the dropdown menu to select a different driver.
```

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
csfle-reference-keys-key-vaults.

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
You will use this IAM (Identity and Access Management) user as a service account for your CSFLE-enabled application.
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

When deploying your CSFLE-enabled application to a production environment,
authenticate your application by using an IAM (Identity and Access Management) role
instead of an IAM (Identity and Access Management) user.

To learn more about IAM (Identity and Access Management) roles, see the following
pages in the official AWS documentation:

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [When to create an IAM role (instead of a user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_which-to-choose_role)

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

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

**Step 2: Create a New Data Encryption Key**

a. Add your AWS KMS Credentials

   Add the service account credentials to your CSFLE-enabled client
   code.

   ```java
   Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
   String kmsProvider = "aws";
   Map<String, Object> providerDetails = new HashMap<>();
   providerDetails.put("accessKeyId", new BsonString("<IAM User Access Key ID>"));
   providerDetails.put("secretAccessKey", new BsonString("<IAM User Secret Access Key>"));
   kmsProviders.put(kmsProvider, providerDetails);
   ```

   **Tip:**

   To learn how to provide your AWS credentials without directly specifying them
   as shown in the preceding code example, see the `Java MONGODB-AWS documentation`.

#. Add Your Key Information

   Update the following code to specify your Customer Master Key:

   **Tip:**

   You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
   in the Create a Customer Master Key step of this guide.

   ```java
   masterKeyProperties.put("provider", new BsonString(kmsProvider));
   masterKeyProperties.put("key", new BsonString("<Master Key ARN>"));
   masterKeyProperties.put("region", new BsonString("<Master Key AWS Region>"));
   ```

#. Generate your Data Encryption Key

   Generate your Data Encryption Key using the variables declared in step one of this tutorial.

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

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an AWS KMS, see
csfle-reference-kms-providers-aws-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in AWS KMS, see
csfle-kms-datakeyopts-aws.

**See also:** Complete Code

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/aws/reader/src/main/java/com/mongodb/csfle/MakeDataKey.java).

**Step 3: Configure the MongoClient**

**Tip:**

Follow the remaining steps in this tutorial in a separate file
from the one created in the previous steps.

To view the complete code for this file, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/aws/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```java
   String keyVaultNamespace = "encryption.__keyVault";
   ```

#. Specify your AWS Credentials

   Specify the `aws` KMS provider and your IAM (Identity and Access Management) user
   credentials:

   ```java
   Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
   String kmsProvider = "aws";
   Map<String, Object> providerDetails = new HashMap<>();
   providerDetails.put("accessKeyId", "<IAM User Access Key ID>");
   providerDetails.put("secretAccessKey", "<IAM User Secret Access Key>");
   kmsProviders.put(kmsProvider, providerDetails);
   ```

   **Important:** Reminder: Authenticate with IAM Roles in Production

   To use an IAM (Identity and Access Management) role instead of an IAM (Identity and Access Management) user 
   to authenticate your application,
   specify an empty object for your credentials in your KMS provider
   object. This instructs the driver to automatically retrieve the credentials
   from the environment:

   ```java
   kmsProviderCredentials.put("aws", new HashMap<>());
   ```

   You cannot automatically retrieve credentials if you are using a named KMS provider.

#. Create an Encryption Schema For Your Collection

   **Tip:** Add Your Data Encryption Key Base64 ID

   Make sure to update the following code to include your Base64
   DEK ({+dek-long+}) ID. You received this value in the
   Generate your Data Encryption Key step of this
   guide.

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

#. Specify the Location of the Automatic Encryption Shared Library

   ```java
   Map<String, Object> extraOptions = new HashMap<String, Object>();
   extraOptions.put("cryptSharedLibPath", "<Full path to your Automatic Encryption Shared Library>"));
   ```

   **Note:** Automatic Encryption Options

   The automatic encryption options provide configuration
   information to the Automatic Encryption Shared Library,
   which modifies the application's behavior when accessing encrypted fields.

   To learn more about the Automatic Encryption Shared Library, see
   the csfle-reference-shared-library page.

#. Create the MongoClient

   Instantiate a MongoDB client object with the following automatic
   encryption settings that use the variables declared in the previous steps:

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

**Step 4: Insert a Document with Encrypted Fields**

Use your CSFLE-enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

To view the complete code for inserting an encrypted document, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/aws/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

**Step 5: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields step of this guide.

To show the functionality of CSFLE, the following code snippet queries for
your document with a client configured for automatic CSFLE as well as
a client that is not configured for automatic CSFLE.

```java
System.out.println("Finding a document with regular (non-encrypted) client.");
Document docRegular = mongoClientRegular.getDatabase(recordsDb).getCollection(recordsColl).find(eq("name", "Jon Doe")).first();
System.out.println(docRegular.toJson());

System.out.println("Finding a document with encrypted client, searching on an encrypted field");
Document docSecure = mongoClientSecure.getDatabase(recordsDb).getCollection(recordsColl).find(eq("ssn", 241014209)).first();
System.out.println(docSecure.toJson());
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

To view the complete code for finding an encrypted document, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/java/aws/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java).

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

### Full Application Code

[Complete Node.js Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/aws/reader/)

## Set Up the KMS

```javascript
// You are viewing the Node.js driver code examples.
// Use the dropdown menu to select a different driver.
```

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
csfle-reference-keys-key-vaults.

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
You will use this IAM (Identity and Access Management) user as a service account for your CSFLE-enabled application.
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

When deploying your CSFLE-enabled application to a production environment,
authenticate your application by using an IAM (Identity and Access Management) role
instead of an IAM (Identity and Access Management) user.

To learn more about IAM (Identity and Access Management) roles, see the following
pages in the official AWS documentation:

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [When to create an IAM role (instead of a user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_which-to-choose_role)

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

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

**Step 2: Create a New Data Encryption Key**

a. Add your AWS KMS Credentials

   Add the service account credentials to your CSFLE-enabled client
   code.

   ```javascript
   const provider = "aws";
   const kmsProviders = {
     aws: {
       accessKeyId: "<Your AWS Access Key ID>",
       secretAccessKey: "<Your AWS Secret Access Key>",
     },
   };
   ```

#. Add Your Key Information

   Update the following code to specify your Customer Master Key:

   **Tip:**

   You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
   in the Create a Customer Master Key step of this guide.

   ```javascript
   const mongodb = require("mongodb");
   const { MongoClient, Binary, ClientEncryption } = mongodb;

   // start-kmsproviders
   const provider = "aws";
   const kmsProviders = {
     aws: {
       accessKeyId: "<Your AWS Access Key ID>",
       secretAccessKey: "<Your AWS Secret Access Key>",
     },
   };
   // end-kmsproviders

   // start-datakeyopts
   const masterKey = {
     key: "<Your AWS Key ARN>",
     region: "<Your AWS Key Region>",
   };
   ```

#. Generate your Data Encryption Key

   ```javascript
   const client = new MongoClient(uri);
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

   **Note:** Import ClientEncryption

   When using the Node.js driver v6.0 and later, you must import
   `ClientEncryption` from `mongodb`. 

   For earlier driver versions, import `ClientEncryption` from
   `mongodb-client-encryption`.

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an AWS KMS, see
csfle-reference-kms-providers-aws-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in AWS KMS, see
csfle-kms-datakeyopts-aws.

**See also:** Complete Code

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/aws/reader/make_data_key.js).

**Step 3: Configure the MongoClient**

**Tip:**

Follow the remaining steps in this tutorial in a separate file
from the one created in the previous steps.

To view the complete code for this file, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/aws/reader/insert_encrypted_document.js).

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```javascript
   const keyVaultNamespace = "encryption.__keyVault";
   ```

#. Specify your AWS Credentials

   Specify the `aws` KMS provider and your IAM (Identity and Access Management) user
   credentials:

   ```javascript
   const kmsProviders = {
     aws: {
       accessKeyId: "<Your AWS Access Key ID>",
       secretAccessKey: "<Your AWS Secret Access Key>",
     },
   };
   ```

   **Important:** Reminder: Authenticate with IAM Roles in Production

   To use an IAM (Identity and Access Management) role instead of an IAM (Identity and Access Management) user 
   to authenticate your application,
   specify an empty object for your credentials in your KMS provider
   object. This instructs the driver to automatically retrieve the credentials
   from the environment:

   ```javascript
   kmsProviders = {
     aws: { }
   };
   ```

   You cannot automatically retrieve credentials if you are using a named KMS provider.

#. Create an Encryption Schema For Your Collection

   **Tip:** Add Your Data Encryption Key Base64 ID

   Make sure to update the following code to include your Base64
   DEK ({+dek-long+}) ID. You received this value in the
   Generate your Data Encryption Key step of this
   guide.

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

#. Specify the Location of the Automatic Encryption Shared Library

   ```javascript
   const extraOptions = {
     cryptSharedLibPath: "<Full path to your Automatic Encryption Shared Library>",
   };
   ```

   **Note:** Automatic Encryption Options

   The automatic encryption options provide configuration
   information to the Automatic Encryption Shared Library,
   which modifies the application's behavior when accessing encrypted fields.

   To learn more about the Automatic Encryption Shared Library, see
   the csfle-reference-shared-library page.

#. Create the MongoClient

   Instantiate a MongoDB client object with the following automatic
   encryption settings that use the variables declared in the previous steps:

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

**Step 4: Insert a Document with Encrypted Fields**

Use your CSFLE-enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/aws/reader/insert_encrypted_document.js).

**Step 5: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields step of this guide.

To show the functionality of CSFLE, the following code snippet queries for
your document with a client configured for automatic CSFLE as well as
a client that is not configured for automatic CSFLE.

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

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/node/aws/reader/insert_encrypted_document.js).

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

### Full Application Code

[Complete Python Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/aws/reader/)

## Set Up the KMS

```python
# You are viewing the Python driver code examples.
# Use the dropdown menu to select a different driver.
```

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
csfle-reference-keys-key-vaults.

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
You will use this IAM (Identity and Access Management) user as a service account for your CSFLE-enabled application.
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

When deploying your CSFLE-enabled application to a production environment,
authenticate your application by using an IAM (Identity and Access Management) role
instead of an IAM (Identity and Access Management) user.

To learn more about IAM (Identity and Access Management) roles, see the following
pages in the official AWS documentation:

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [When to create an IAM role (instead of a user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_which-to-choose_role)

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

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
# Drop the database storing your encrypted fields as all
# the DEKs encrypting those fields were deleted in the preceding line.
key_vault_client["medicalRecords"].drop_collection("patients")
key_vault_client[key_vault_db][key_vault_coll].create_index(
    [("keyAltNames", ASCENDING)],
    unique=True,
    partialFilterExpression={"keyAltNames": {"$exists": True}},
)
```

**Step 2: Create a New Data Encryption Key**

a. Add your AWS KMS Credentials

   Add the service account credentials to your CSFLE-enabled client
   code.

   ```python
   provider = "aws"
   kms_providers = {
       provider: {
           "accessKeyId": "<IAM User Access Key ID>",
           "secretAccessKey": "<IAM User Secret Access Key>",
       }
   }
   ```

#. Add Your Key Information

   Update the following code to specify your Customer Master Key:

   **Tip:**

   You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
   in the Create a Customer Master Key step of this guide.

   ```python
   master_key = {"region": "<Master Key AWS Region>", "key": "<Master Key ARN>"}
   ```

#. Generate your Data Encryption Key

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

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an AWS KMS, see
csfle-reference-kms-providers-aws-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in AWS KMS, see
csfle-kms-datakeyopts-aws.

**See also:** Complete Code

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/aws/reader/make_data_key.py).

**Step 3: Configure the MongoClient**

**Tip:**

Follow the remaining steps in this tutorial in a separate file
from the one created in the previous steps.

To view the complete code for this file, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/aws/reader/insert_encrypted_document.py).

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```python
   key_vault_namespace = "encryption.__keyVault"
   ```

#. Specify your AWS Credentials

   Specify the `aws` KMS provider and your IAM (Identity and Access Management) user
   credentials:

   ```python
   provider = "aws"
   kms_providers = {
       "aws": {
           "accessKeyId": "<IAM User Access Key ID>",
           "secretAccessKey": "<IAM User Secret Access Key>",
       }
   }
   ```

   **Important:** Reminder: Authenticate with IAM Roles in Production

   To use an IAM (Identity and Access Management) role instead of an IAM (Identity and Access Management) user 
   to authenticate your application,
   specify an empty object for your credentials in your KMS provider
   object. This instructs the driver to automatically retrieve the credentials
   from the environment:

   ```python
   kms_provider_credentials = {
     "aws": { }
   }
   ```

   You cannot automatically retrieve credentials if you are using a named KMS provider.

#. Create an Encryption Schema For Your Collection

   **Tip:** Add Your Data Encryption Key Base64 ID

   Make sure to update the following code to include your Base64
   DEK ({+dek-long+}) ID. You received this value in the
   Generate your Data Encryption Key step of this
   guide.

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

#. Specify the Location of the Automatic Encryption Shared Library

   ```python
   extra_options = {
       "cryptSharedLibPath": "<Full path to your Automatic Encryption Shared Library>"
   }
   ```

   **Note:** Automatic Encryption Options

   The automatic encryption options provide configuration
   information to the Automatic Encryption Shared Library,
   which modifies the application's behavior when accessing encrypted fields.

   To learn more about the Automatic Encryption Shared Library, see
   the csfle-reference-shared-library page.

#. Create the MongoClient

   Instantiate a MongoDB client object with the following automatic
   encryption settings that use the variables declared in the previous steps:

   ```python
   fle_opts = AutoEncryptionOpts(
       kms_providers, key_vault_namespace, schema_map=patient_schema, **extra_options
   )
   secureClient = MongoClient(connection_string, auto_encryption_opts=fle_opts)
   ```

**Step 4: Insert a Document with Encrypted Fields**

Use your CSFLE-enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/aws/reader/insert_encrypted_document.py).

**Step 5: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields step of this guide.

To show the functionality of CSFLE, the following code snippet queries for
your document with a client configured for automatic CSFLE as well as
a client that is not configured for automatic CSFLE.

```python
print("Finding a document with regular (non-encrypted) client.")
result = regularClient.medicalRecords.patients.find_one({"name": "Jon Doe"})
pprint.pprint(result)

print("Finding a document with encrypted client, searching on an encrypted field")
pprint.pprint(secureClient.medicalRecords.patients.find_one({"ssn": 241014209}))
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

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/python/aws/reader/insert_encrypted_document.py).

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

### Full Application Code

[Complete C# Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/)

## Set Up the KMS

```csharp
// You are viewing the .NET/C# driver code examples.
// Use the dropdown menu to select a different driver.
```

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
csfle-reference-keys-key-vaults.

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
You will use this IAM (Identity and Access Management) user as a service account for your CSFLE-enabled application.
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

When deploying your CSFLE-enabled application to a production environment,
authenticate your application by using an IAM (Identity and Access Management) role
instead of an IAM (Identity and Access Management) user.

To learn more about IAM (Identity and Access Management) roles, see the following
pages in the official AWS documentation:

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [When to create an IAM role (instead of a user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_which-to-choose_role)

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

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

a. Add your AWS KMS Credentials

   Add the service account credentials to your CSFLE-enabled client
   code.

   ```csharp
   var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
   var provider = "aws";
   var awsKmsOptions = new Dictionary<string, object>
   {
      { "accessKeyId", "<Your AWS Access Key ID>" },
      { "secretAccessKey", "<Your AWS Secret Access Key>" }
   };
   kmsProviders.Add(provider, awsKmsOptions);
   ```

#. Add Your Key Information

   Update the following code to specify your Customer Master Key:

   **Tip:**

   You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
   in the Create a Customer Master Key step of this guide.

   ```csharp
   var dataKeyOptions = new DataKeyOptions(
      masterKey: new BsonDocument
      {
          { "region", "<Your AWS Key Region>" },
          { "key", "<Your AWS Key ARN>" },
      });
   ```

#. Generate your Data Encryption Key

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

**Tip:** Learn More

To view a diagram showing how your client application creates your
Data Encryption Key when using an AWS KMS, see
csfle-reference-kms-providers-aws-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in AWS KMS, see
csfle-kms-datakeyopts-aws.

**See also:** Complete Code

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/MakeDataKey.cs)

**Step 3: Configure the MongoClient**

**Tip:**

Follow the remaining steps in this tutorial in a separate file
from the one created in the previous steps.

To view the complete code for this file, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/InsertEncryptedDocument.cs)

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```csharp
   var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
   ```

#. Specify your AWS Credentials

   Specify the `aws` KMS provider and your IAM (Identity and Access Management) user
   credentials:

   ```csharp
   var kmsProviders = new Dictionary<string, IReadOnlyDictionary<string, object>>();
   var provider = "aws";
   var awsKmsOptions = new Dictionary<string, object>
   {
      { "accessKeyId", "<Your AWS Access Key ID>" },
      { "secretAccessKey", "<Your AWS Secret Access Key>" }
   };
   kmsProviders.Add(provider, awsKmsOptions);
   ```

   **Important:** Reminder: Authenticate with IAM Roles in Production

   To use an IAM (Identity and Access Management) role instead of an IAM (Identity and Access Management) user 
   to authenticate your application,
   specify an empty object for your credentials in your KMS provider
   object. This instructs the driver to automatically retrieve the credentials
   from the environment:

   ```csharp
   kmsProviderCredentials.Add("aws", new Dictionary<string, object>);  
   ```

   You cannot automatically retrieve credentials if you are using a named KMS provider.

#. Create an Encryption Schema For Your Collection

   **Tip:** Add Your Data Encryption Key Base64 ID

   Make sure to update the following code to include your Base64
   DEK ({+dek-long+}) ID. You received this value in the
   Generate your Data Encryption Key step of this
   guide.

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

#. Specify the Location of the Automatic Encryption Shared Library

   ```csharp
   var mongoBinariesPath = "<Full path to your Automatic Encryption Shared Library>";
   var extraOptions = new Dictionary<string, object>()
   {
      { "cryptSharedLibPath", mongoBinariesPath },
   };
   ```

   **Note:** Automatic Encryption Options

   The automatic encryption options provide configuration
   information to the Automatic Encryption Shared Library,
   which modifies the application's behavior when accessing encrypted fields.

   To learn more about the Automatic Encryption Shared Library, see
   the csfle-reference-shared-library page.

#. Create the MongoClient

   Instantiate a MongoDB client object with the following automatic
   encryption settings that use the variables declared in the previous steps:

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

**Step 4: Insert a Document with Encrypted Fields**

Use your CSFLE-enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/InsertEncryptedDocument.cs)

**Step 5: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields step of this guide.

To show the functionality of CSFLE, the following code snippet queries for
your document with a client configured for automatic CSFLE as well as
a client that is not configured for automatic CSFLE.

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

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/InsertEncryptedDocument.cs)

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

### Full Application Code

[Complete Go Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/aws/reader/)

## Set Up the KMS

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
csfle-reference-keys-key-vaults.

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
You will use this IAM (Identity and Access Management) user as a service account for your CSFLE-enabled application.
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

When deploying your CSFLE-enabled application to a production environment,
authenticate your application by using an IAM (Identity and Access Management) role
instead of an IAM (Identity and Access Management) user.

To learn more about IAM (Identity and Access Management) roles, see the following
pages in the official AWS documentation:

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [When to create an IAM role (instead of a user)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_which-to-choose_role)

## Create the Application

**Step 1: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

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

**Step 2: Create a New Data Encryption Key**

a. Add your AWS KMS Credentials

   Add the service account credentials to your CSFLE-enabled client
   code.

   ```go
   provider := "aws"
   kmsProviders := map[string]map[string]interface{}{
   	provider: {
   		"accessKeyId":     "<Your AWS Access Key ID>",
   		"secretAccessKey": "<Your AWS Secret Access Key>",
   	},
   }
   ```

#. Add Your Key Information

   Update the following code to specify your Customer Master Key:

   **Tip:**

   You recorded your Customer Master Key's ARN (Amazon Resource Name) and Region
   in the Create a Customer Master Key step of this guide.

   ```go
   masterKey := map[string]interface{}{
   	"key":    "<Your AWS Key ARN>",
   	"region": "<Your AWS Key Region>",
   }
   ```

#. Generate your Data Encryption Key

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
Data Encryption Key when using an AWS KMS, see
csfle-reference-kms-providers-aws-architecture.

To learn more about the options for creating a Data Encryption Key
encrypted with a Customer Master Key hosted in AWS KMS, see
csfle-kms-datakeyopts-aws.

**See also:** Complete Code

To view the complete code for making a Data Encryption Key, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/aws/reader/make-data-key.go).

**Step 3: Configure the MongoClient**

**Tip:**

Follow the remaining steps in this tutorial in a separate file
from the one created in the previous steps.

To view the complete code for this file, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/aws/reader/insert-encrypted-document.go).

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```go
   keyVaultNamespace := "encryption.__keyVault"
   ```

#. Specify your AWS Credentials

   Specify the `aws` KMS provider and your IAM (Identity and Access Management) user
   credentials:

   ```go
   kmsProviders := map[string]map[string]interface{}{
   	"aws": {
   		"accessKeyId":     "<Your AWS Access Key ID>",
   		"secretAccessKey": "<Your AWS Secret Access Key>",
   	},
   }
   ```

   **Important:** Reminder: Authenticate with IAM Roles in Production

   To use an IAM (Identity and Access Management) role instead of an IAM (Identity and Access Management) user 
   to authenticate your application,
   specify an empty object for your credentials in your KMS provider
   object. This instructs the driver to automatically retrieve the credentials
   from the environment:

   ```go
   kmsProviderCredentials := map[string]map[string]interface{}{
     "aws": { },
   }
   ```

   You cannot automatically retrieve credentials if you are using a named KMS provider.

#. Create an Encryption Schema For Your Collection

   **Tip:** Add Your Data Encryption Key Base64 ID

   Make sure to update the following code to include your Base64
   DEK ({+dek-long+}) ID. You received this value in the
   Generate your Data Encryption Key step of this
   guide.

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

#. Specify the Location of the Automatic Encryption Shared Library

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

#. Create the MongoClient

   Instantiate a MongoDB client object with the following automatic
   encryption settings that use the variables declared in the previous steps:

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

**Step 4: Insert a Document with Encrypted Fields**

Use your CSFLE-enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

To view the complete code for inserting a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/aws/reader/insert-encrypted-document.go).

**Step 5: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields step of this guide.

To show the functionality of CSFLE, the following code snippet queries for
your document with a client configured for automatic CSFLE as well as
a client that is not configured for automatic CSFLE.

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

To view the complete code for finding a document with encrypted fields, see
[our Github repository](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/generated/in-use-encryption/csfle/go/aws/reader/insert-encrypted-document.go).

## Learn More

To learn how CSFLE works, see
csfle-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Learn more about CSFLE components on the Reference page.
- Learn how Customer Master Keys and Data Encryption Keys work on the csfle-reference-keys-key-vaults page
- See how KMS Providers manage your CSFLE keys on the csfle-reference-kms-providers page.
