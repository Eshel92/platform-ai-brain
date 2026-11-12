<!-- Part 3 of 4 of core/queryable-encryption/tutorials/explicit-encryption.md (split because the page is big). -->

Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

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

The output from the code in this section should resemble the following:

```text
Created encrypted collection!
```

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```go
   keyVaultColl := "__keyVault"
   keyVaultDb := "encryption"
   keyVaultNamespace := keyVaultDb + "." + keyVaultColl
   dbName := "medicalRecords"
   collName := "patients"
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

   ```go
   key, err := ioutil.ReadFile("master-key.txt")
   if err != nil {
   	log.Fatalf("Could not read the key from master-key.txt: %v", err)
   }
   kmsProviders := map[string]map[string]interface{}{"local": {"key": key}}
   ```

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

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

#. Specify the Path of the Automatic Encryption Shared Library

   ```go
   extraOptions := map[string]interface{}{
   	"cryptSharedLibPath": "<path to crypt_shared library>",
   }
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

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

   **Note:** Automatic Decryption

   We use a `MongoClient` instance with automatic encryption enabled
   to perform automatic decryption.

   To learn more about explicit encryption with automatic decryption,
   see the Fundamentals section. 

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

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

**Note:** Indexed and Unindexed Algorithms

To learn more about the indexed and unindexed algorithms in
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

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

**Step 1: Create a Customer Master Key**

You must create a Customer Master Key (CMK ({+cmk-long+})) to perform Queryable Encryption.

Create a 96-byte Customer Master Key and save it to the
file `master-key.txt`:

```csharp
using (var randomNumberGenerator = System.Security.Cryptography.RandomNumberGenerator.Create())
{
    var bytes = new byte[96];
    randomNumberGenerator.GetBytes(bytes);
    var localMasterKeyBase64Write = Convert.ToBase64String(bytes);
    File.WriteAllText("master-key.txt", localMasterKeyBase64Write);
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

**Step 2: Create a Unique Index on your Key Vault collection**

Create a unique index on the `keyAltNames` field in your
`encryption.__keyVault` namespace.

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

a. Read the Customer Master Key and Specify KMS Provider Settings

   Retrieve the contents of the Customer Master Key file that you generated
   in the Create a Customer Master Key step of this guide.

   Use the CMK ({+cmk-long+}) value in your KMS provider settings. The
   client uses these settings to discover the CMK ({+cmk-long+}). Set the provider
   name to `local` to indicate that you are using a
   Local Key Provider.

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

#. Create your Data Encryption Keys

   Construct a client with your MongoDB connection string and Key Vault collection
   namespace, and create the Data Encryption Keys:

   **Note:** Key Vault Collection Namespace Permissions

   To complete this tutorial, the database user your application uses to connect to 
   MongoDB must have `dbAdmin` permissions on the following namespaces:

   - `encryption.__keyVault`
   - `medicalRecords` database

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

#. Create Your Encrypted Collection

   Use a Queryable Encryption enabled `MongoClient` instance to specify what
   fields you must encrypt and create your encrypted collection:

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

**Step 4: Configure your MongoClient for Encrypted Reads and Writes**

a. Specify the Key Vault Collection Namespace

   Specify `encryption.__keyVault` as the Key Vault collection
   namespace.

   ```csharp
   var connectionString = "<Your MongoDB URI>";
   var keyVaultNamespace = CollectionNamespace.FromFullName("encryption.__keyVault");
   var coll = "patients";
   var db = "medicalRecords";
   ```

#. Specify the Customer Master Key

   Specify the KMS provider and specify your Customer Master Key inline:

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

#. Retrieve Data Encryption Keys 

   Retrieve the Data Encryption Keys created in the
   Create a Data Encryption Key
   step of this guide:

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

#. Specify the Path of the Automatic Encryption Shared Library

   ```csharp
   var extraOptions = new Dictionary<string, object>()
   {
       {"cryptSharedLibPath", "<path to crypt_shared library>"},
   };
   ```

   **Tip:** Learn More

   To learn more about the library referenced by this path,
   see the qe-reference-shared-library page.

#. Create a MongoClient Object

   Instantiate a `MongoClient` object with the following
   automatic encryption settings:

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

#. Create a ClientEncryption Object

   Instantiate a `ClientEncryption` object as follows:

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
explicit encryption, see qe-fundamentals-man-enc-algorithm-choice.

**Step 5: Insert a Document with Encrypted Fields**

Use your Queryable Encryption enabled
`MongoClient` instance to insert a document with encrypted fields into the
`medicalRecords.patients` namespace using the following code
snippet:

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

**Step 6: Retrieve Your Document with Encrypted Fields**

Retrieve the document with encrypted fields you inserted in the
Insert a Document with Encrypted Fields
step of this guide through a query on an encrypted field:

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
