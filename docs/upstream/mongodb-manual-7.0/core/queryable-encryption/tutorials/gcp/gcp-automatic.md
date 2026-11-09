<!-- Converted from core/queryable-encryption/tutorials/gcp/gcp-automatic.txt (reStructuredText). Includes are inlined. -->

# Use Automatic Queryable Encryption with GCP

## Overview

This guide shows you how to build an application that implements the MongoDB
Queryable Encryption feature to automatically encrypt and decrypt document fields and use
Google Cloud Key Management Service for key management.

After you complete the steps in this guide, you should have:

- A CMK ({+cmk-long+}) managed by Google Cloud Key Management Service
- A working client application that inserts documents with encrypted fields
  using your CMK ({+cmk-long+})

**Tip:** Customer Master Keys

To learn more about the Customer Master Key, read the
qe-reference-keys-key-vaults
documentation.

## Before You Get Started

To complete and run the code in this guide, you need to set up your
development environment as shown in the qe-install page.

**See also:** Full Application

To see the complete code for this sample application,
select the tab corresponding to your programming language and follow
the provided link. Each sample application repository includes a
`README.md` file that you can use to learn how to set up your environment
and run the application.

**shell:**

[Complete mongosh Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/mongosh/)

**nodejs:**

[Complete Node.js Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/node/)

**python:**

[Complete Python Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/python/)

**java-sync:**

[Complete Java Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/java/)

**go:**

[Complete Go Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/go/)

**csharp:**

[Complete C# Application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/csharp/)

## Set Up the KMS

**Step 1: Register a GCP (Google Cloud Platform) Service Account**

**Step 1: Register or log in to your existing account on [Google Cloud](https://cloud.google.com).**

**Step 2: Create a service account for your project**

To create a service account on Google Cloud, follow the
[Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating)
guide in Google's official documentation.

**Step 3: Add a service account key**

To add a service account key on Google Cloud, follow the
[Managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
guide in Google's official documentation.

**shell:**

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**nodejs:**

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**python:**

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**java-sync:**

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Unless you are using an
attached service account, make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**go:**

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**csharp:**

**Important:**

When creating your service account key, you receive a one-time
download of the private key information. Make sure to download this
file in either the PKCS12 or JSON format for use later in this
tutorial.

**Step 4: Create a GCP (Google Cloud Platform) Customer Master Key**

**Step 1: Create a new Customer Master Key**

Create a key ring and a symmetric key by following the
[Create a key](https://cloud.google.com/kms/docs/creating-keys)
guide from Google's official documentation.

This key is your Customer Master Key (CMK ({+cmk-long+})).

Record the following details of your CMK ({+cmk-long+}) for use in a future
step of this tutorial.

| Field | Required | Description |
|---|---|---|
| key_name | Yes | Identifier for the CMK ({+cmk-long+}). |
| key_ring | Yes | Identifier for the group of keys your key belongs to. |
| key_version | No | The version of the named key. |
| location | Yes | Region specified for your key. |
| endpoint | No | The host and optional port of the Google Cloud KMS. The default value is `cloudkms.googleapis.com`. |

## Create the Application

**Step 1: Assign Your Application Variables**

The code samples in this tutorial use the following variables to perform
the Queryable Encryption workflow:

**shell:**

- **kmsProviderName** - The KMS you're using to store your Customer Master Key.
  Set this variable to `"gcp"` for this tutorial.
- **uri** - Your MongoDB deployment connection URI. Set your connection
  URI in the `MONGODB_URI` environment variable or replace the value
  directly.
- **keyVaultDatabaseName** - The database in MongoDB where your data
  encryption keys (DEKs) will be stored. Set this variable
  to `"encryption"`.
- **keyVaultCollectionName** - The collection in MongoDB where your DEKs
  will be stored. Set this variable to `"__keyVault"`.
- **keyVaultNamespace** - The namespace in MongoDB where your DEKs will
  be stored. Set this variable to the values of the `keyVaultDatabaseName`
  and `keyVaultCollectionName` variables, separated by a period.
- **encryptedDatabaseName** - The database in MongoDB where your encrypted
  data will be stored. Set this variable to `"medicalRecords"`.
- **encryptedCollectionName** - The collection in MongoDB where your encrypted
  data will be stored. Set this variable to `"patients"`.

You can declare these variables by using the following code:

```javascript
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
const kmsProviderName = "<Your KMS Provider Name>";
const uri = process.env.MONGODB_URI; // Your connection URI
const keyVaultDatabaseName = "encryption";
const keyVaultCollectionName = "__keyVault";
const keyVaultNamespace = `${keyVaultDatabaseName}.${keyVaultCollectionName}`;
const encryptedDatabaseName = "medicalRecords";
const encryptedCollectionName = "patients";
```

**nodejs:**

- **kmsProviderName** - The KMS you're using to store your Customer Master Key.
  Set this variable to `"gcp"` for this tutorial.
- **uri** - Your MongoDB deployment connection URI. Set your connection
  URI in the `MONGODB_URI` environment variable or replace the value
  directly.
- **keyVaultDatabaseName** - The database in MongoDB where your data
  encryption keys (DEKs) will be stored. Set this variable
  to `"encryption"`.
- **keyVaultCollectionName** - The collection in MongoDB where your DEKs
  will be stored. Set this variable to `"__keyVault"`.
- **keyVaultNamespace** - The namespace in MongoDB where your DEKs will
  be stored. Set this variable to the values of the `keyVaultDatabaseName`
  and `keyVaultCollectionName` variables, separated by a period.
- **encryptedDatabaseName** - The database in MongoDB where your encrypted
  data will be stored. Set this variable to `"medicalRecords"`.
- **encryptedCollectionName** - The collection in MongoDB where your encrypted
  data will be stored. Set this variable to `"patients"`.

You can declare these variables by using the following code:

```javascript
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
const kmsProviderName = "<Your KMS Provider Name>";

const uri = process.env.MONGODB_URI; // Your connection URI

const keyVaultDatabaseName = "encryption";
const keyVaultCollectionName = "__keyVault";
const keyVaultNamespace = `${keyVaultDatabaseName}.${keyVaultCollectionName}`;
const encryptedDatabaseName = "medicalRecords";
const encryptedCollectionName = "patients";
```

**python:**

- **kms_provider_name** - The KMS you're using to store your Customer Master Key.
  Set this variable to `"gcp"` for this tutorial.
- **uri** - Your MongoDB deployment connection URI. Set your connection
  URI in the `MONGODB_URI` environment variable or replace the value
  directly.
- **key_vault_database_name** - The database in MongoDB where your data
  encryption keys (DEKs) will be stored. Set this variable
  to `"encryption"`.
- **key_vault_collection_name** - The collection in MongoDB where your DEKs
  will be stored. Set this variable to `"__keyVault"`.
- **key_vault_namespace** - The namespace in MongoDB where your DEKs will
  be stored. Set this variable to the values of the `key_vault_database_name`
  and `key_vault_collection_name` variables, separated by a period.
- **encrypted_database_name** - The database in MongoDB where your encrypted
  data will be stored. Set this variable to `"medicalRecords"`.
- **encrypted_collection_name** - The collection in MongoDB where your encrypted
  data will be stored. Set this variable to `"patients"`.

You can declare these variables by using the following code:

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

**java-sync:**

- **kmsProviderName** - The KMS you're using to store your Customer Master Key.
  Set this variable to `"gcp"` for this tutorial.
- **uri** - Your MongoDB deployment connection URI. Set your connection
  URI in the `MONGODB_URI` environment variable or replace the value
  directly.
- **keyVaultDatabaseName** - The database in MongoDB where your data
  encryption keys (DEKs) will be stored. Set this variable
  to `"encryption"`.
- **keyVaultCollectionName** - The collection in MongoDB where your DEKs
  will be stored. Set this variable to `"__keyVault"`.
- **keyVaultNamespace** - The namespace in MongoDB where your DEKs will
  be stored. Set this variable to the values of the `keyVaultDatabaseName`
  and `keyVaultCollectionName` variables, separated by a period.
- **encryptedDatabaseName** - The database in MongoDB where your encrypted
  data will be stored. Set this variable to `"medicalRecords"`.
- **encryptedCollectionName** - The collection in MongoDB where your encrypted
  data will be stored. Set this variable to `"patients"`.

You can declare these variables by using the following code:

```java
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
String kmsProviderName = "<KMS provider name>";
String uri = QueryableEncryptionHelpers.getEnv("MONGODB_URI"); // Your connection URI
String keyVaultDatabaseName = "encryption";
String keyVaultCollectionName = "__keyVault";
String keyVaultNamespace = keyVaultDatabaseName + "." + keyVaultCollectionName;
String encryptedDatabaseName = "medicalRecords";
String encryptedCollectionName = "patients";
```

**go:**

- **kmsProviderName** - The KMS you're using to store your Customer Master Key.
  Set this variable to `"gcp"` for this tutorial.
- **uri** - Your MongoDB deployment connection URI. Set your connection
  URI in the `MONGODB_URI` environment variable or replace the value
  directly.
- **keyVaultDatabaseName** - The database in MongoDB where your data
  encryption keys (DEKs) will be stored. Set this variable
  to `"encryption"`.
- **keyVaultCollectionName** - The collection in MongoDB where your DEKs
  will be stored. Set this variable to `"__keyVault"`.
- **keyVaultNamespace** - The namespace in MongoDB where your DEKs will
  be stored. Set this variable to the values of the `keyVaultDatabaseName`
  and `keyVaultCollectionName` variables, separated by a period.
- **encryptedDatabaseName** - The database in MongoDB where your encrypted
  data will be stored. Set this variable to `"medicalRecords"`.
- **encryptedCollectionName** - The collection in MongoDB where your encrypted
  data will be stored. Set this variable to `"patients"`.

You can declare these variables by using the following code:

```go
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
kmsProviderName := "<KMS provider name>"
uri := os.Getenv("MONGODB_URI") // Your connection URI
keyVaultDatabaseName := "encryption"
keyVaultCollectionName := "__keyVault"
keyVaultNamespace := keyVaultDatabaseName + "." + keyVaultCollectionName
encryptedDatabaseName := "medicalRecords"
encryptedCollectionName := "patients"
```

**csharp:**

- **kmsProviderName** - The KMS you're using to store your Customer Master Key.
  Set this value to `"gcp"` for this tutorial.
- **keyVaultDatabaseName** - The database in MongoDB where your data
  encryption keys (DEKs) will be stored. Set the value of `keyVaultDatabaseName`
  to `"encryption"`.
- **keyVaultCollectionName** - The collection in MongoDB where your DEKs
  will be stored. Set the value of `keyVaultCollectionName` to `"__keyVault"`.
- **keyVaultNamespace** - The namespace in MongoDB where your DEKs will
  be stored. Set `keyVaultNamespace` to a new `CollectionNamespace` object whose name
  is the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables,
  separated by a period.
- **encryptedDatabaseName** - The database in MongoDB where your encrypted
  data will be stored. Set the value of `encryptedDatabaseName` to `"medicalRecords"`.
- **encryptedCollectionName** - The collection in MongoDB where your encrypted
  data will be stored. Set the value of `encryptedCollectionName` to `"patients"`.
- **uri** - Your MongoDB deployment connection URI. Set your connection
  URI in the `appsettings.json` file or replace the value
  directly.

You can declare these variables by using the following code:

```csharp
// KMS provider name should be one of the following: "aws", "gcp", "azure", "kmip" or "local"
const string kmsProviderName = "<your KMS provider name>";
const string keyVaultDatabaseName = "encryption";
const string keyVaultCollectionName = "__keyVault";
var keyVaultNamespace =
    CollectionNamespace.FromFullName($"{keyVaultDatabaseName}.{keyVaultCollectionName}");
const string encryptedDatabaseName = "medicalRecords";
const string encryptedCollectionName = "patients";
var appSettings = new ConfigurationBuilder().AddJsonFile("appsettings.json").Build();
var uri = appSettings["MongoDbUri"];
```

**Important:** Key Vault Collection Namespace Permissions

The Key Vault collection is in the `encryption.__keyVault`
namespace. Ensure that the database user your application uses to connect
to MongoDB has ReadWrite
permissions on this namespace.

**shell:**

**Tip:** Environment Variables

The sample code in this tutorial references environment variables that
you need to set. Alternatively, you can replace the values directly in
the code.

To learn how you can setup these environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/node/README.md) file
included in the sample application on GitHub.

**nodejs:**

**Tip:** Environment Variables

The sample code in this tutorial references environment variables that
you need to set. Alternatively, you can replace the values directly in
the code.

To learn how you can setup these environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/node/README.md) file
included in the sample application on GitHub.

**python:**

**Tip:** Environment Variables

The sample code in this tutorial references environment variables that
you need to set. Alternatively, you can replace the values directly in
the code.

To learn how you can setup these environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/python/README.md) file
included in the sample application on GitHub.

**java-sync:**

**Tip:** Environment Variables

The sample code in this tutorial references environment variables that
you need to set. Alternatively, you can replace the values directly in
the code.

To learn how you can setup these environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/java/README.md) file
included in the sample application on GitHub.

**go:**

**Tip:** Environment Variables

The sample code in this tutorial references environment variables that
you need to set. Alternatively, you can replace the values directly in
the code.

To learn how you can setup these environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/go/README.md) file
included in the sample application on GitHub.

**csharp:**

**Tip:** Environment Variables

The sample code in this tutorial references environment variables that
you need to set. Alternatively, you can replace the values directly in
the code.

To learn how you can setup these environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/csharp/README.md) file
included in the sample application on GitHub.

**Step 2: Create your Encrypted Collection**

**Step 1: Add Your Google Cloud Key Management Service Credentials**

Create a variable containing your Google Cloud Key Management Service credentials with the
following structure:

**shell:**

```javascript
kmsProviderCredentials = {
  gcp: {
    email: process.env["GCP_EMAIL"], // Your GCP email
    privateKey: process.env["GCP_PRIVATE_KEY"], // Your GCP private key
  },
};
```

**nodejs:**

```javascript
kmsProviders = {
  gcp: {
    email: process.env.GCP_EMAIL, // Your GCP email
    privateKey: process.env.GCP_PRIVATE_KEY, // Your GCP private key
  },
};
```

**python:**

```python
kms_provider_credentials = {
    "gcp": {
        "email": os.environ['GCP_EMAIL'], # Your GCP email
        "privateKey": os.environ['GCP_PRIVATE_KEY'] # Your GCP private key
    }
}
```

**java-sync:**

```java
Map<String, Object> kmsProviderDetails = new HashMap<>();
kmsProviderDetails.put("email", getEnv("GCP_EMAIL")); // Your GCP email
kmsProviderDetails.put("privateKey", getEnv("GCP_PRIVATE_KEY")); // Your GCP private key

Map<String, Map<String, Object>> kmsProviderCredentials = new HashMap<String, Map<String, Object>>();
kmsProviderCredentials.put("gcp", kmsProviderDetails);
```

**go:**

```go
kmsProviderCredentials := map[string]map[string]interface{}{
	"gcp": {
		"email":      os.Getenv("GCP_EMAIL"),       // GCP email
		"privateKey": os.Getenv("GCP_PRIVATE_KEY"), // GCP private key
	},
}
```

**csharp:**

```csharp
var kmsProviderCredentials = new Dictionary<string, IReadOnlyDictionary<string, object>>();
var kmsOptions = new Dictionary<string, object>
{
    { "email", _appSettings["Gcp:Email"] }, // Your GCP email
    { "privateKey", _appSettings["Gcp:PrivateKey"] } // Your GCP private key
};
kmsProviderCredentials.Add(kmsProvider, kmsOptions);
```

**Step 2: Add your Customer Master Key Credentials**

Create a variable containing your Customer Master Key credentials with the
following structure. Use the credentials you recorded
in the Create a new Customer Master Key
step of this tutorial.

**shell:**

```javascript
customerMasterKeyCredentials = {
  projectId: process.env["GCP_PROJECT_ID"], // Your GCP Project ID
  location: process.env["GCP_LOCATION"], // Your GCP Key Location
  keyRing: process.env["GCP_KEY_RING"], //  Your GCP Key Ring
  keyName: process.env["GCP_KEY_NAME"], // Your GCP Key Name
};
```

**nodejs:**

```javascript
customerMasterKeyCredentials = {
  projectId: process.env.GCP_PROJECT_ID, // Your GCP Project ID
  location: process.env.GCP_LOCATION, // Your GCP Key Location
  keyRing: process.env.GCP_KEY_RING, //  Your GCP Key Ring
  keyName: process.env.GCP_KEY_NAME, // Your GCP Key Name
};
```

**python:**

```python
customer_master_key_credentials = {
    "projectId": os.environ['GCP_PROJECT_ID'], # Your GCP email
    "location": os.environ['GCP_LOCATION'],  # Your GCP private key
    "keyRing": os.environ['GCP_KEY_RING'],  # Your GCP private key
    "keyName": os.environ['GCP_KEY_NAME']  # Your GCP private key
}
```

**java-sync:**

```java
BsonDocument customerMasterKeyCredentials = new BsonDocument();
customerMasterKeyCredentials.put("provider", new BsonString(kmsProviderName));
customerMasterKeyCredentials.put("projectId", new BsonString(getEnv("GCP_PROJECT_ID"))); // Your GCP Project ID
customerMasterKeyCredentials.put("location", new BsonString(getEnv("GCP_LOCATION"))); // Your GCP Key Location
customerMasterKeyCredentials.put("keyRing", new BsonString(getEnv("GCP_KEY_RING"))); // Your GCP Key Ring
customerMasterKeyCredentials.put("keyName", new BsonString(getEnv("GCP_KEY_NAME"))); // Your GCP Key Name
```

**go:**

```go
customerMasterKeyCredentials := map[string]string{
	"projectId": os.Getenv("GCP_PROJECT_ID"), // Your GCP Project ID
	"location":  os.Getenv("GCP_LOCATION"),   // Your GCP Key Location
	"keyRing":   os.Getenv("GCP_KEY_RING"),   // Your GCP Key Ring
	"keyName":   os.Getenv("GCP_KEY_NAME"),   // Your GCP Key Name
}
```

**csharp:**

```csharp
var customerMasterKeyCredentials = new BsonDocument
{
    { "projectId", _appSettings["Gcp:ProjectId"] }, // Your GCP Project ID
    { "location", _appSettings["Gcp:Location"] }, // Your GCP Key Location
    { "keyRing", _appSettings["Gcp:KeyRing"] }, // Your GCP Key Ring
    { "keyName", _appSettings["Gcp:KeyName"] } // Your GCP Key Name
};
```

**Step 3: Set Your Automatic Encryption Options**

**shell:**

Create an `autoEncryptionOptions` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, which contains your Google Cloud Key Management Service
  credentials

```javascript
const autoEncryptionOptions = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviderCredentials,
};
```

**nodejs:**

Create an `autoEncryptionOptions` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviders` object, which contains your
  Google Cloud Key Management Service credentials
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

**python:**

Create an `AutoEncryptionOpts` object that contains the following
options:

- The `kms_provider_credentials` object, which contains your
  Google Cloud Key Management Service credentials
- The namespace of your Key Vault collection
- The path to your Automatic Encryption Shared Library

```python
auto_encryption_options = AutoEncryptionOpts(
    kms_provider_credentials,
    key_vault_namespace,
    crypt_shared_lib_path=os.environ['SHARED_LIB_PATH'] # Path to your Automatic Encryption Shared Library>
)
```

**java-sync:**

Create an `AutoEncryptionSettings` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, which contains your
  Google Cloud Key Management Service credentials
- The `extraOptions` object, which contains the path to
  your Automatic Encryption Shared Library

```java
Map<String, Object> extraOptions = new HashMap<String, Object>();
extraOptions.put("cryptSharedLibPath", getEnv("SHARED_LIB_PATH")); // Path to your Automatic Encryption Shared Library

AutoEncryptionSettings autoEncryptionSettings = AutoEncryptionSettings.builder()
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviderCredentials)
        .extraOptions(extraOptions)
        .build();
```

**go:**

Create an `AutoEncryption` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, which contains your
  Google Cloud Key Management Service credentials
- The `cryptSharedLibraryPath` object, which contains the path to
  your Automatic Encryption Shared Library

```go
cryptSharedLibraryPath := map[string]interface{}{
	"cryptSharedLibPath": os.Getenv("SHARED_LIB_PATH"), // Path to your Automatic Encryption Shared Library
}

autoEncryptionOptions := options.AutoEncryption().
	SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviderCredentials).
	SetExtraOptions(cryptSharedLibraryPath)
```

**csharp:**

Create an `AutoEncryptionOptions` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, which contains your
  Google Cloud Key Management Service credentials
- The `extraOptions` object, which contains the path to
  your Automatic Encryption Shared Library

```csharp
var extraOptions = new Dictionary<string, object>
{
    { "cryptSharedLibPath", _appSettings["CryptSharedLibPath"] } // Path to your Automatic Encryption Shared Library
};

var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace,
    kmsProviderCredentials,
    extraOptions: extraOptions);
```

**Note:** Automatic Encryption Options

The automatic encryption options provide configuration
information to the Automatic Encryption Shared Library,
which modifies the application's behavior when accessing encrypted fields.

To learn more about the Automatic Encryption Shared Library, see
the qe-reference-shared-library page.

**Step 4: Create a Client to Set Up an Encrypted Collection**

To create a client used to encrypt and decrypt data in
your collection, instantiate a new `MongoClient` by using your
connection URI and your automatic encryption options.

**shell:**

```javascript
const encryptedClient = Mongo(uri, autoEncryptionOptions);
```

**nodejs:**

```javascript
const encryptedClient = new MongoClient(uri, {
  autoEncryption: autoEncryptionOptions,
});
```

**python:**

```python
encrypted_client = MongoClient(
    uri, auto_encryption_opts=auto_encryption_options)
```

**java-sync:**

```java
MongoClientSettings clientSettings = MongoClientSettings.builder()
        .applyConnectionString(new ConnectionString(uri))
        .autoEncryptionSettings(autoEncryptionSettings)
        .build();

try (MongoClient encryptedClient = MongoClients.create(clientSettings)) {
```

**go:**

```go
encryptedClient, err := mongo.Connect(
	context.TODO(),
	options.Client().ApplyURI(uri).SetAutoEncryptionOptions(autoEncryptionOptions),
)
if err != nil {
	panic(fmt.Sprintf("Unable to connect to MongoDB: %v\n", err))
}
defer func() {
	_ = encryptedClient.Disconnect(context.TODO())
}()
```

**csharp:**

```csharp
MongoClientSettings.Extensions.AddAutoEncryption(); // .NET/C# Driver v3.0 or later only
var clientSettings = MongoClientSettings.FromConnectionString(uri);
clientSettings.AutoEncryptionOptions = qeHelpers.GetAutoEncryptionOptions(
    keyVaultNamespace,
    kmsProviderCredentials);
var encryptedClient = new MongoClient(clientSettings);
```

**Step 5: Specify Fields to Encrypt**

To encrypt a field, add it to the encryption schema.
To enable queries on a field, add the "queries"
property. Create the encryption schema as follows:

**shell:**

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

**nodejs:**

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

**python:**

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

**java-sync:**

```java
BsonDocument encryptedFieldsMap = new BsonDocument().append("fields",
        new BsonArray(Arrays.asList(
                new BsonDocument()
                        .append("keyId", new BsonNull())
                        .append("path", new BsonString("patientRecord.ssn"))
                        .append("bsonType", new BsonString("string"))
                        .append("queries", new BsonDocument()
                                .append("queryType", new BsonString("equality"))),
                new BsonDocument()
                        .append("keyId", new BsonNull())
                        .append("path", new BsonString("patientRecord.billing"))
                        .append("bsonType", new BsonString("object")))));
```

**go:**

```go
encryptedFieldsMap := bson.M{
	"fields": []bson.M{
		bson.M{
			"keyId":    nil,
			"path":     "patientRecord.ssn",
			"bsonType": "string",
			"queries": []bson.M{
				{
					"queryType": "equality",
				},
			},
		},
		bson.M{
			"keyId":    nil,
			"path":     "patientRecord.billing",
			"bsonType": "object",
		},
	},
}
```

**csharp:**

```csharp
var encryptedFields = new BsonDocument
{
    {
        "fields", new BsonArray
        {
            new BsonDocument
            {
                { "keyId", BsonNull.Value },
                { "path", "record.ssn" },
                { "bsonType", "string" },
                { "queries", new BsonDocument("queryType", "equality") }
            },
            new BsonDocument
            {
                { "keyId", BsonNull.Value },
                { "path", "record.billing" },
                { "bsonType", "object" }
            }
        }
    }
};
```

**Note:**

In the previous code sample, both the "ssn" and
"billing" fields are encrypted, but only the "ssn"
field can be queried.

**Step 6: Create the Collection**

Instantiate `ClientEncryption` to access the API for the
encryption helper methods.

**shell:**

```javascript
const clientEncryption = encryptedClient.getClientEncryption()
```

**nodejs:**

```javascript
const clientEncryption = new ClientEncryption(encryptedClient, autoEncryptionOptions);
```

**python:**

```python
client_encryption = ClientEncryption(
    kms_providers=kms_provider_credentials,
    key_vault_namespace=key_vault_namespace,
    key_vault_client=encrypted_client,
    codec_options=CodecOptions(uuid_representation=STANDARD)
)
```

**java-sync:**

```java
ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
        .keyVaultMongoClientSettings(MongoClientSettings.builder()
                .applyConnectionString(new ConnectionString(uri))
                .build())
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviderCredentials)
        .build();
ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
```

**go:**

```go
clientEncryptionOpts := options.ClientEncryption().
	SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviderCredentials)

clientEncryption, err := mongo.NewClientEncryption(encryptedClient, clientEncryptionOpts)
if err != nil {
	panic(fmt.Sprintf("Unable to create a ClientEncryption instance due to the following error: %s\n", err))
}
```

**csharp:**

```csharp
var clientEncryptionOptions = new ClientEncryptionOptions(
    keyVaultClient: keyVaultClient,
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviderCredentials
);
var clientEncryption = new ClientEncryption(clientEncryptionOptions);
```

**shell:**

Create your encrypted collection by using the encryption
helper method accessed through the `ClientEncryption` class.
This method automatically generates data encryption keys for your
encrypted fields and creates the encrypted collection:

```javascript
await clientEncryption.createEncryptedCollection(
  encryptedDatabaseName,
  encryptedCollectionName,
  {
    provider: kmsProviderName,
    createCollectionOptions: encryptedFieldsMap,
    masterKey: customerMasterKeyCredentials,
  }
);
```

**nodejs:**

**Note:** Import ClientEncryption

When using the Node.js driver v6.0 and later, you must import
`ClientEncryption` from `mongodb`. 

For earlier driver versions, import `ClientEncryption` from
`mongodb-client-encryption`.

Create your encrypted collection by using the encryption
helper method accessed through the `ClientEncryption` class.
This method automatically generates data encryption keys for your
encrypted fields and creates the encrypted collection:

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

**Tip:** Database vs. Database Name

The method that creates the encrypted collection requires a reference
to a database *object* rather than the database *name*. You can
obtain this reference by using a method on your client object.

**python:**

Create your encrypted collection by using the encryption
helper method accessed through the `ClientEncryption` class.
This method automatically generates data encryption keys for your
encrypted fields and creates the encrypted collection:

```python
client_encryption.create_encrypted_collection(
    encrypted_client[encrypted_database_name],
    encrypted_collection_name,
    encrypted_fields_map,
    kms_provider_name,
    customer_master_key_credentials,
)
```

**Tip:** Database vs. Database Name

The method that creates the encrypted collection requires a reference
to a database *object* rather than the database *name*. You can
obtain this reference by using a method on your client object.

**java-sync:**

Create your encrypted collection by using the encryption
helper method accessed through the `ClientEncryption` class.
This method automatically generates data encryption keys for your
encrypted fields and creates the encrypted collection:

```java
CreateCollectionOptions createCollectionOptions = new CreateCollectionOptions().encryptedFields(encryptedFieldsMap);

CreateEncryptedCollectionParams encryptedCollectionParams = new CreateEncryptedCollectionParams(kmsProviderName);
encryptedCollectionParams.masterKey(customerMasterKeyCredentials);

try {
    clientEncryption.createEncryptedCollection(
            encryptedClient.getDatabase(encryptedDatabaseName),
            encryptedCollectionName,
            createCollectionOptions,
            encryptedCollectionParams);
} 
catch (Exception e) {
    throw new Exception("Unable to create encrypted collection due to the following error: " + e.getMessage());
}
```

**Tip:** Database vs. Database Name

The method that creates the encrypted collection requires a reference
to a database *object* rather than the database *name*. You can
obtain this reference by using a method on your client object.

**go:**

The Golang version of this tutorial uses data models to
represent the document structure. Add the following
structs to your project to represent the data in your
collection:

```go
type PatientDocument struct {
	PatientName   string        `bson:"patientName"`
	PatientID     int32         `bson:"patientId"`
	PatientRecord PatientRecord `bson:"patientRecord"`
}
```

```go
type PatientRecord struct {
	SSN     string      `bson:"ssn"`
	Billing PaymentInfo `bson:"billing"`
}
```

```go
type PaymentInfo struct {
	Type   string `bson:"type"`
	Number string `bson:"number"`
}
```

After you've added these classes, create your encrypted
collection by using the encryption helper method accessed
through the `ClientEncryption` class.
This method automatically generates data encryption keys for your
encrypted fields and creates the encrypted collection:

```go
createCollectionOptions := options.CreateCollection().SetEncryptedFields(encryptedFieldsMap)
_, _, err =
	clientEncryption.CreateEncryptedCollection(
		context.TODO(),
		encryptedClient.Database(encryptedDatabaseName),
		encryptedCollectionName,
		createCollectionOptions,
		kmsProviderName,
		customerMasterKey,
	)
```

**Tip:** Database vs. Database Name

The method that creates the encrypted collection requires a reference
to a database *object* rather than the database *name*. You can
obtain this reference by using a method on your client object.

**csharp:**

The C# version of this tutorial uses separate classes as data models
to represent the document structure.
Add the following `Patient`, `PatientRecord`, and `PatientBilling`
classes to your project:

```csharp
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

[BsonIgnoreExtraElements]
public class Patient
{
    public ObjectId Id { get; set; }
    public string Name { get; set; }
    public PatientRecord Record { get; set; }
}
```

```csharp
public class PatientRecord
{
    public string Ssn { get; set; }
    public PatientBilling Billing { get; set; }
}
```

```csharp
public class PatientBilling
{
    public string CardType { get; set; }
    public long CardNumber { get; set; }
}
```

After you've added these classes, create your encrypted collection by
using the encryption helper method accessed through the
`ClientEncryption` class.
This method automatically generates data encryption keys for your
encrypted fields and creates the encrypted collection:

```csharp
var patientDatabase = encryptedClient.GetDatabase(encryptedDatabaseName);
patientDatabase.DropCollection(encryptedCollectionName); // Ensure the collection is dropped before creating a new one
try
{
    var createCollectionOptions = new CreateCollectionOptions<Patient>
    {
        EncryptedFields = encryptedFields
    };

    clientEncryption.CreateEncryptedCollection(patientDatabase,
        encryptedCollectionName,
        createCollectionOptions,
        kmsProviderName,
        customerMasterKeyCredentials);
}
catch (Exception e)
{
    throw new Exception("Unable to create encrypted collection due to the following error: " + e.Message);
}
```

**Tip:** Database vs. Database Name

The method that creates the encrypted collection requires a reference
to a database *object* rather than the database *name*. You can
obtain this reference by using a method on your client object.

**Step 7: Insert a Document with Encrypted Fields**

**shell:**

Create a sample document that describes a patient's personal information.
Use the encrypted client to insert it into the `patients` collection,
as shown in the following example:

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

const encryptedCollection = encryptedClient.getDB(encryptedDatabaseName).getCollection(encryptedCollectionName);

const insertResult = await encryptedCollection.insertOne(patientDocument);
```

**nodejs:**

Create a sample document that describes a patient's personal information.
Use the encrypted client to insert it into the `patients` collection,
as shown in the following example:

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

**python:**

Create a sample document that describes a patient's personal information.
Use the encrypted client to insert it into the `patients` collection,
as shown in the following example:

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

**java-sync:**

This tutorial uses POJOs as data models
to represent the document structure. To set up your application to
use POJOs, add the following code:

```java
CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
CodecRegistry pojoCodecRegistry = fromRegistries(getDefaultCodecRegistry(), fromProviders(pojoCodecProvider));
```

To learn more about Java POJOs, see the [Plain Old Java Object wikipedia article](https://en.wikipedia.org/wiki/Plain_old_Java_object).

This tutorial uses the following POJOs:

- `Patient`
- `PatientRecord`
- `PatientBilling`

You can view these classes in the [models package of the complete Java application](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/java/src/main/java/com/mongodb/tutorials/qe/models).

Add these POJO classes to your application. Then, create an instance
of a `Patient` that describes a patient's personal information. Use
the encrypted client to insert it into the `patients` collection,
as shown in the following example:

```java
MongoDatabase encryptedDb = encryptedClient.getDatabase(encryptedDatabaseName).withCodecRegistry(pojoCodecRegistry);
MongoCollection<Patient> collection = encryptedDb.getCollection(encryptedCollectionName, Patient.class);

PatientBilling patientBilling = new PatientBilling("Visa", "4111111111111111");
PatientRecord patientRecord = new PatientRecord("987-65-4320", patientBilling);
Patient patientDocument = new Patient("Jon Doe", patientRecord);

InsertOneResult result = collection.insertOne(patientDocument);
```

**go:**

Create a sample document that describes a patient's personal information.
Use the encrypted client to insert it into the `patients` collection,
as shown in the following example:

```go
patientDocument := &PatientDocument{
	PatientName: "John Doe",
	PatientID:   12345678,
	PatientRecord: PatientRecord{
		SSN: "987-65-4320",
		Billing: PaymentInfo{
			Type:   "Visa",
			Number: "4111111111111111",
		},
	},
}

coll := encryptedClient.Database(encryptedDatabaseName).Collection(encryptedCollectionName)

_, err = coll.InsertOne(context.TODO(), patientDocument)
if err != nil {
	panic(fmt.Sprintf("Unable to insert the patientDocument: %s", err))
}
```

**csharp:**

Create a sample document that describes a patient's personal information.
Use the encrypted client to insert it into the `patients` collection,
as shown in the following example:

```csharp
var patient = new Patient
{
    Name = "Jon Doe",
    Id = new ObjectId(),
    Record = new PatientRecord
    {
        Ssn = "987-65-4320",
        Billing = new PatientBilling
        {
            CardType = "Visa",
            CardNumber = 4111111111111111
        }
    }
};

var encryptedCollection = encryptedClient.GetDatabase(encryptedDatabaseName).
    GetCollection<Patient>(encryptedCollectionName);

await encryptedCollection.InsertOneAsync(patient);
```

**Step 8: Query on an Encrypted Field**

The following code sample executes a find query on an encrypted field and
prints the decrypted data:

**shell:**

```javascript
const findResult = await encryptedCollection.findOne({
  "patientRecord.ssn": "987-65-4320",
});
console.log(findResult);
```

**nodejs:**

```javascript
const findResult = await encryptedCollection.findOne({
  "patientRecord.ssn": "987-65-4320",
});
console.log(findResult);
```

**python:**

```python
find_result = encrypted_collection.find_one({
    "patientRecord.ssn": "987-65-4320"
})

print(find_result)
```

**java-sync:**

```java
Patient findResult = collection.find(
    new BsonDocument()
            .append("patientRecord.ssn", new BsonString("987-65-4320")))
            .first();

System.out.println(findResult);
```

**go:**

```go
var findResult PatientDocument
err = coll.FindOne(
	context.TODO(),
	bson.M{"patientRecord.ssn": "987-65-4320"},
).Decode(&findResult)
if err != nil {
	fmt.Print("Unable to find the document\n")
} else {
	output, _ := json.MarshalIndent(findResult, "", "    ")
	fmt.Printf("%s\n", output)
}
```

**csharp:**

```csharp
var ssnFilter = Builders<Patient>.Filter.Eq("patientRecord.ssn", patient.PatientRecord.Ssn);
var findResult = await encryptedCollection.Find(ssnFilter).FirstOrDefaultAsync();

Console.WriteLine(findResult.ToJson(new JsonWriterSettings { Indent = true }));
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

## Learn More

To learn how Queryable Encryption works, see
qe-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Learn more about Queryable Encryption components on the Reference page.
- Learn how Customer Master Keys and Data Encryption Keys work on the qe-reference-keys-key-vaults page.
- See how KMS Providers manage your Queryable Encryption keys on the qe-fundamentals-kms-providers page.
