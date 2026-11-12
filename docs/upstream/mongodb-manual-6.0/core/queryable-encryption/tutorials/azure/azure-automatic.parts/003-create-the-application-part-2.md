<!-- Part 3 of 4 of core/queryable-encryption/tutorials/azure/azure-automatic.md (split because the page is big). -->

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

**Note:**

Rather than creating a raw BSON document, you can pass a struct with `bson` tags directly
to the driver for encoding.

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
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/azure/reader/insert_encrypted_document.js).

**nodejs:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/azure/reader/insert_encrypted_document.js).

**python:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/azure/reader/insert_encrypted_document.py).

**java-sync:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/azure/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**go:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/azure/reader/insert-encrypted-document.go).

**csharp:**

To view the complete code for inserting an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/azure/reader/QueryableEncryption/InsertEncryptedDocument.cs).

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
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/mongosh/azure/reader/insert_encrypted_document.js).

**nodejs:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/node/azure/reader/insert_encrypted_document.js).

**python:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/python/azure/reader/insert_encrypted_document.py).

**java-sync:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/java/azure/reader/src/main/java/com/mongodb/qe/InsertEncryptedDocument.java).

**go:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/go/azure/reader/insert-encrypted-document.go).

**csharp:**

To view the complete code for finding an encrypted document, see
[the Queryable Encryption sample application repository](https://github.com/mongodb-university/docs-in-use-encryption-examples/tree/main/queryable-encryption/dotnet/azure/reader/QueryableEncryption/InsertEncryptedDocument.cs).
