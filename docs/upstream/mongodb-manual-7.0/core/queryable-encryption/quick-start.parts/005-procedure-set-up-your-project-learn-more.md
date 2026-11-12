<!-- Part 5 of 5 of core/queryable-encryption/quick-start.md (split because the page is big). -->

### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Create your .NET console project.**

Run the following commands to create a new .NET console project in a
directory named `CSharpQE`:

```bash
mkdir CSharpQE && cd CSharpQE
dotnet new console
```

**Step 2: Install dependencies.**

From your `CSharpQE` directory, run the following commands to install 
the MongoDB .NET/C# Driver and required packages:

```bash
dotnet add package MongoDB.Driver
dotnet add package MongoDB.Driver.Encryption
dotnet add package Microsoft.Extensions.Configuration.Json
```

**Step 3: Configure your application settings.**

In your `CSharpQE` directory, create a file named
`appsettings.json`. The sample code in this tutorial reads its
configuration from this file. Paste the following code into this file:

```json
{
    "MongoDbUri": "<Your MongoDB URI>",
    "CryptSharedLibPath": "<Full path to your Automatic Encryption Shared Library>"
}
```

Replace the following placeholder values:

- `<Your MongoDB URI>`: Your MongoDB deployment connection URI.
- `<Full path to your Automatic Encryption Shared Library>`: The
  full path to your Automatic Encryption Shared Library, which resembles the following
  paths:

  - **macOS**: `/<crypt shared directory>/lib/mongo_crypt_v1.dylib`
  - **Linux**: `/<crypt shared directory>/lib/mongo_crypt_v1.so`
  - **Windows**: `C:\<crypt shared directory>\bin\mongo_crypt_v1.dll`

**Tip:** appsettings.json Location

When you run the application, the `appsettings.json` file must be in
the same directory as the compiled executable. Add the following
`ItemGroup` to your `.csproj` file so that the
`CopyToOutputDirectory` setting automatically copies
`appsettings.json` to the output `bin` directory when you build:

```xml
<ItemGroup>
  <None Update="appsettings.json">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
  </None>
</ItemGroup>
```

For more information on setting up your configuration, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/csharp/README.md) file included in the
sample application on GitHub.

**Step 4: Create your data model classes.**

This tutorial uses separate classes as data models to represent the
document structure. In your `CSharpQE` directory, create a file
named `Patient.cs` and paste the following `Patient` class into
the file:

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

Then, create a file named `PatientRecord.cs` and paste the
following `PatientRecord` class into the file:

```csharp
public class PatientRecord
{
    public string Ssn { get; set; }
    public PatientBilling Billing { get; set; }
}
```

Finally, create a file named `PatientBilling.cs` and paste the
following `PatientBilling` class into the file:

```csharp
public class PatientBilling
{
    public string CardType { get; set; }
    public long CardNumber { get; set; }
}
```

**Step 5: Create your main project file.**

Replace the contents of the `Program.cs` file that was
generated in your `CSharpQE` directory with the following
code:

```csharp
﻿namespace QueryableEncryption;

public class Program
{
    public static async Task Main(string[] args)
    {
        await QueryableEncryptionTutorial.RunExample();
    }
}
```

The `Program.cs` file contains your main method, which calls the
code in your other project files to generate encryption keys and
perform encrypted operations.

**Step 6: Create your application file.**

In your `CSharpQE` directory, create a file named
`QueryableEncryptionTutorial.cs`. This file contains the main
Queryable Encryption workflow. Paste the following starter code into this file:

```csharp
using Microsoft.Extensions.Configuration;
using MongoDB.Bson;
using MongoDB.Bson.IO;
using MongoDB.Bson.Serialization.Conventions;
using MongoDB.Driver;
using MongoDB.Driver.Encryption;
using System.Security.Cryptography;

namespace QueryableEncryption;

public static class QueryableEncryptionTutorial
{
   public static async Task RunExample()
   {
      var camelCaseConvention = new ConventionPack { new CamelCaseElementNameConvention() };
      ConventionRegistry.Register("CamelCase", camelCaseConvention, type => true);

      // Paste application variables below

      // The helper code snippets you paste below read configuration
      // from this alias of your appSettings variable
      var _appSettings = appSettings;

      // Paste code to generate CMK below

      // Paste code to retrieve the CMK and specify KMS provider settings below

      // Paste automatic encryption options code below

      // Paste client configuration code below

      // Paste schema below

      // Paste code to create an encrypted collection below

      // Paste code to insert a document below

      // Paste code to query the document below

   }
}
```

The placeholder comments indicate where you add code in later steps
of this tutorial.

**Step 7: Assign your application variables.**

The code samples in this tutorial use the following variables to perform
the Queryable Encryption workflow. Paste the following code into the `RunExample()`
method of `QueryableEncryptionTutorial.cs`, under the
`// Paste application variables below` comment. For this tutorial, set 
the `kmsProviderName` variable to `"local"`.

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

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS that stores your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `keyVaultDatabaseName` | The database that stores your DEKs. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection that stores your DEKs. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB that stores your DEKs. Set this variable to a new `CollectionNamespace` object whose name is the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database that stores your encrypted data. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection that stores your encrypted data. Set to `"patients"`. |
| `uri` | Your MongoDB connection URI. Set with the `MongoDbUri` value in your `appsettings.json` file. |


### Configure Encryption

After you set up your project, follow the steps in this section to create an
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `QueryableEncryptionTutorial.cs` 
file under the `// Paste code to generate CMK below` comment. This code 
creates a 96-byte Customer Master Key and saves it to your filesystem as the 
file `customer-master-key.txt`:

```csharp
// Reuse the key from the customer-master-key.txt file if it exists
if (!File.Exists("customer-master-key.txt"))
{
    using var randomNumberGenerator = RandomNumberGenerator.Create();
    try
    {
        var bytes = new byte[96];
        randomNumberGenerator.GetBytes(bytes);
        var localCustomerMasterKeyBase64 = Convert.ToBase64String(bytes);
        File.WriteAllText("customer-master-key.txt", localCustomerMasterKeyBase64);
    }
    catch (Exception e)
    {
        throw new Exception("Unable to write Customer Master Key file due to the following error: " + e.Message);
    }
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

**Step 2: Retrieve the Customer Master Key and specify the KMS provider settings.**

Paste the following code under the ``// Paste code to retrieve the CMK and 
specify KMS provider settings below`` comment. This code retrieves the 
contents of the `customer-master-key.txt` file:

```csharp
// WARNING: Do not use a local key file in a production application
var kmsProviderCredentials = new Dictionary<string, IReadOnlyDictionary<string, object>>();
try
{
    var localCustomerMasterKeyBase64 = File.ReadAllText("customer-master-key.txt");
    var localCustomerMasterKeyBytes = Convert.FromBase64String(localCustomerMasterKeyBase64);

    var localOptions = new Dictionary<string, object>
    {
        { "key", localCustomerMasterKeyBytes }
    };

    kmsProviderCredentials.Add(kmsProvider, localOptions);
}
catch (Exception e)
{
    throw new Exception("Unable to read the Customer Master Key due to the following error: " + e.Message);
}
```

**Step 3: Set your automatic encryption options.**

Paste the following code under the ``// Paste automatic encryption options 
code below`` comment. This code snippet creates an 
`AutoEncryptionOptions` object that contains the following options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, defined in the previous step
- The `extraOptions` object, which contains the path to your
  Automatic Encryption Shared Library

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

**Step 4: Create a client to set up an encrypted collection.**

Paste the following code under the ``// Paste client configuration code 
below`` comment.

IMPORTANT: If you are using the .NET/C# driver version 3.0 or 
later, you must add the following code to your application before
you instantiate a new `MongoClient`:

```csharp
MongoClientSettings.Extensions.AddAutoEncryption(); // .NET/C# Driver v3.0 or later only
```

Then, instantiate a new `MongoClient`:

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(uri); 
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;

var encryptedClient = new MongoClient(clientSettings);
```

**Step 5: Specify fields to encrypt.**

To encrypt a field, add the field to the encryption schema. To enable queries 
on a field, add the `queries` property. Paste the following code under 
the `// Paste schema below` comment:

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

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `QueryableEncryptionTutorial.cs` 
file under the `// Paste code to create an encrypted collection below`
comment in the order shown. 

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```csharp
var clientEncryptionOptions = new ClientEncryptionOptions(
   keyVaultClient: encryptedClient,
   keyVaultNamespace: keyVaultNamespace,
   kmsProviders: kmsProviderCredentials
);
var clientEncryption = new ClientEncryption(clientEncryptionOptions);
```

Because you are using a local Customer Master Key, you don't need to provide
Customer Master Key credentials. Create a variable containing an empty object to
use in place of credentials when you create your encrypted collection:

```csharp
var customerMasterKeyCredentials = new BsonDocument();
```

To create your encrypted collection, use the `ClientEncryption` object's 
`CreateEncryptedCollection()` helper method. This method automatically
generates data encryption keys for your encrypted fields and creates the
encrypted collection:

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


### Perform Encrypted Operations

After you configure your application and database connection, you can insert
and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

To create a document that stores patient data and insert it into the 
`patients` collection, paste the following code under the 
`// Paste code to insert a document below` comment:

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

**Step 2: Query on encrypted data.**

Paste the following code under the ``// Paste code to query the document
below`` comment to retrieve an encrypted field value and print the
decrypted data:

```csharp
var ssnFilter = Builders<Patient>.Filter.Eq("patientRecord.ssn", patient.PatientRecord.Ssn);
var findResult = await encryptedCollection.Find(ssnFilter).FirstOrDefaultAsync();

Console.WriteLine(findResult.ToJson(new JsonWriterSettings { Indent = true }));
```

**Step 3: Run your application.**

To run the application, run the following command from your `CSharpQE` 
project directory:

```bash
dotnet run
```

The output of the preceding code sample should look similar to the
following:

```json
{ 
  "_id": {
    "$oid": "6a6281b43201828e23bbe897"
  },
  "patientName": "Jon Doe",
  "patientRecord": {
    "ssn": "987-65-4320",
    "billing": {
      "cardType": "Visa",
      "cardNumber": 4111111111111111 
    },
    "billAmount": 1500
  }
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.

In this tutorial, you created an application that automatically
encrypts and decrypts the `ssn` and `billing` fields in your
`patients` collection. Because your application uses an encrypted
client, the query returns the decrypted field values. A client that
is not configured with your encryption keys would see the encrypted
values for those fields instead.


## Learn More

To view a tutorial on production-ready Queryable Encryption with a remote
KMS, see qe-tutorial-automatic-encryption.

To learn how Queryable Encryption works, see
qe-fundamentals.

To learn more about the topics mentioned in this guide, see the
following links:

- Learn more about Queryable Encryption components on the
  Reference page.
- Learn how Customer Master Keys and Data Encryption Keys work on the
  qe-reference-keys-key-vaults page.
- See how KMS Providers manage your Queryable Encryption keys on the
  qe-fundamentals-kms-providers page.
