<!-- Part 1 of 5 of core/csfle/tutorials/aws/aws-automatic.md (split because the page is big). -->

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
