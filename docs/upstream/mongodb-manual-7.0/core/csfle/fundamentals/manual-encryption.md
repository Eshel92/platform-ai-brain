<!-- Converted from core/csfle/fundamentals/manual-encryption.txt (reStructuredText). Includes are inlined. -->

# CSFLE Explicit Encryption

## Overview

Learn how to use the **explicit encryption** mechanism of Client-Side Field Level Encryption
(CSFLE).

Explicit encryption is a mechanism in which you specify how to encrypt
and decrypt fields in your document for each operation you perform on
your database.

Explicit encryption is available in the following MongoDB products
of version 4.2 or later:

- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas

## Use Explicit Encryption

To use explicit encryption you must perform the following actions in your
CSFLE-enabled application:

- csfle-fundamentals-manual-encryption-client-enc
- csfle-fundamentals-manual-encryption-update-operations
- Manually
  or
  Automatically
  Decrypt Fields in Your Documents

### Create a ClientEncryption Instance

To use explicit encryption, you must create a `ClientEncryption`
instance. `ClientEncryption` is an abstraction used across drivers and
`mongosh` that encapsulates the Key Vault collection
and KMS ({+kms-long+}) operations involved in explicit encryption.

To create a `ClientEncryption` instance, you must specify
the following information:

- A `MongoClient` instance with access to your Key Vault collection
- The namespace of your Key Vault collection
- A `kmsProviders` object configured with access to the
  KMS ({+kms-long+}) provider hosting your Customer Master Key

For more `ClientEncryption` options, see csfle-reference-mongo-client. 

To view code snippets that show how to create a `ClientEncryption`
instance, see the csfle-fundamentals-manual-encryption-example
section of this guide.

### Encrypt Fields in Read and Write Operations

You must update read and write operations throughout your application
such that your application encrypts fields before performing
read and write operations.

To encrypt fields, use the `encrypt` method of your `ClientEncryption`
instance.

To view code snippets that show how to use the `encrypt` method,
see the csfle-fundamentals-manual-encryption-example
section of this guide.

### Manual Decryption

You can decrypt your encrypted fields manually or automatically when
using explicit encryption.

To decrypt your fields manually, use the `decrypt` method of your
`ClientEncryption` instance.

To view code snippets that show how to use the `decrypt` method,
see the csfle-fundamentals-manual-encryption-example
section of this guide.

### Automatic Decryption

To decrypt your fields automatically, configure your
`MongoClient` instance as follows:

- Specify your Key Vault collection
- Specify a `kmsProviders` object
- If you use MongoDB Community Server, set the `bypassAutoEncryption`
  option to `True`

**Note:** Automatic Decryption is Available in MongoDB Community Server

Although automatic encryption requires MongoDB Enterprise or MongoDB
Atlas, automatic decryption is available in the following MongoDB
products:

- MongoDB Community Server
- MongoDB Enterprise Advanced
- MongoDB Atlas

To view a code snippet demonstrating how to enable automatic decryption,
select the tab corresponding to your preferred language:

```java
MongoClientSettings clientSettings = MongoClientSettings.builder()
.applyConnectionString(new ConnectionString(connectionString))
.autoEncryptionSettings(AutoEncryptionSettings.builder()
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviders).bypassAutoEncryption(true)
        .build())
.build();
MongoClient mongoClient = MongoClients.create(clientSettings);
```

```javascript
const client = new MongoClient(connectionString, {
  monitorCommands: true,
  autoEncryption: {
    keyVaultNamespace,
    kmsProviders,
    bypassAutoEncryption: true,
  },
});
```

```python
auto_encryption_opts = AutoEncryptionOpts(
    kms_providers=kms_providers,
    key_vault_namespace=key_vault_namespace,
    bypass_auto_encryption=True,
)
client = MongoClient(auto_encryption_opts=auto_encryption_opts)
```

```csharp
var clientSettings = MongoClientSettings.FromConnectionString(connectionString);
var autoEncryptionOptions = new AutoEncryptionOptions(
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders,
    bypassAutoEncryption: true);
clientSettings.AutoEncryptionOptions = autoEncryptionOptions;
var client = new MongoClient(clientSettings);
```

```go
autoEncryptionOpts := options.AutoEncryption().
	SetKmsProviders(kmsProviders).
	SetKeyVaultNamespace(KeyVaultNamespace).
	SetBypassAutoEncryption(true)
client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(URI).SetAutoEncryptionOptions(autoEncryptionOpts))
if err != nil {
	return fmt.Errorf("Connect error for encrypted client: %v", err)
}
defer func() {
	_ = client.Disconnect(context.TODO())
}()
```

```javascript
var autoEncryptionOpts = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
  bypassAutoEncryption: true,
};
var encryptedClient = Mongo(
  connectionString,
  autoEncryptionOpts
);
```

## Example

Assume you want to insert documents with the following structure into
your MongoDB instance:

```json
{
  "name": "<name of person>",
  "age": <age of person>,
  "favorite-foods": ["<array of foods>"]
}
```

**Step 1: Create a MongoClient Instance**

In this example, you use the same `MongoClient` instance to access your
Key Vault collection and to read and write encrypted data.

The following code snippets show how to create a `MongoClient` instance:

**java-sync:**

```java
MongoClient client = MongoClients.create(connectionString);
```

**nodejs:**

```javascript
const client = new MongoClient(connectionString);
```

**python:**

```python
client = MongoClient(your_connection_uri)
```

**csharp:**

```csharp
var client = new MongoClient(connectionString);
```

**go:**

```go
client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(URI))
if err != nil {
	panic(fmt.Errorf("Client connect error %v", err))
}
```

**shell:**

```javascript
const autoEncryptionOpts = {
  keyVaultNamespace: keyVaultNamespace,
  kmsProviders: kmsProviders,
};
const encryptedClient = Mongo(connectionString, autoEncryptionOpts);
```

**Step 2: Create a ClientEncryption Instance**

The following code snippets show how to create a `ClientEncryption`
instance:

**java-sync:**

```java
MongoCollection<Document> collection = client.getDatabase(db).getCollection(coll);
ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
        .keyVaultMongoClientSettings(MongoClientSettings.builder()
                .applyConnectionString(new ConnectionString(connectionString))
                .build())
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviders)
        .build();
ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
```

**nodejs:**

```javascript
const collection = client.db(db).collection(coll);
const encryption = new ClientEncryption(client, {
  keyVaultNamespace,
  kmsProviders,
});
```

**python:**

```python
coll = client.employees.foods
client_encryption = ClientEncryption(
    kms_providers,
    "encryption.___keyVault",
    client,
    coll.codec_options,
)
```

**Note:** CodecOptions

The MongoDB Python driver requires that you specify the
`CodecOptions` with which you would like to encrypt and
decrypt your documents.

Specify the `CodecOptions` you have configured on the
`MongoClient`, `Database`, or `Collection` with which
you are writing encrypted and decrypted application data to MongoDB.

**csharp:**

```csharp
var collection = client.GetDatabase(db).GetCollection<BsonDocument>(coll);
var clientEncryptionOptions = new ClientEncryptionOptions(
    keyVaultClient: client,
    keyVaultNamespace: keyVaultNamespace,
    kmsProviders: kmsProviders);
var clientEncryption = new ClientEncryption(clientEncryptionOptions);
```

**go:**

```go
coll := client.Database(DbName).Collection(CollName)
clientEncryptionOpts := options.ClientEncryption().SetKeyVaultNamespace(KeyVaultNamespace).SetKmsProviders(kmsProviders)
clientEnc, err := mongo.NewClientEncryption(client, clientEncryptionOpts)
if err != nil {
	panic(fmt.Errorf("NewClientEncryption error %v", err))
}
defer func() {
	_ = clientEnc.Close(context.TODO())
}()
```

**shell:**

```javascript
const clientEncryption = encryptedClient.getClientEncryption();
```

**Step 3: Encrypt Fields and Insert**

You want to encrypt the fields of your document using the
following algorithms:

| Field Name | Encryption Algorithm | BSON Type of Field |
|---|---|---|
| `name` | Deterministic | String |
| `age` | No encryption | Int |
| `favorite-foods` | Random | Array |

The following code snippets show how to manually encrypt the fields in
your document and insert your document into MongoDB:

**java-sync:**

**Note:**

The `dataKeyId` variable in the following examples refers to a
Data Encryption Key (DEK). To learn how to generate a DEK with your Local Key
Provider, see the Quick Start. To learn how to create a 
DEK with a specific Key Management System, see csfle-tutorials.

```java
BsonBinary encryptedName = clientEncryption.encrypt(new BsonString("Greg"), new EncryptOptions("AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic").keyId(dataKeyId));
BsonBinary encryptedFoods = clientEncryption.encrypt(new BsonArray().parse("[\"Grapes\", \"Foods\"]"), new EncryptOptions("AEAD_AES_256_CBC_HMAC_SHA_512-Random").keyId(dataKeyId));
collection.insertOne(new Document("name", encryptedName).append("foods", encryptedFoods).append("age", 83));
```

**nodejs:**

**Note:**

The `dataKeyId` variable in the following examples refers to a
Data Encryption Key (DEK). To learn how to generate a DEK with your Local Key
Provider, see the Quick Start. To learn how to create a 
DEK with a specific Key Management System, see csfle-tutorials.

```javascript
encryptedName = await encryption.encrypt("Greg", {
  algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
  keyId: dataKeyId,
});
encryptedFoods = await encryption.encrypt(["Cheese", "Grapes"], {
  algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Random",
  keyId: dataKeyId,
});
await collection.insertOne({
  name: encryptedName,
  age: 83,
  foods: encryptedFoods,
});
```

**python:**

**Note:**

The `data_key_id` variable in the following examples refers to a
Data Encryption Key (DEK). To learn how to generate a DEK with your Local Key
Provider, see the Quick Start. To learn how to create a 
DEK with a specific Key Management System, see csfle-tutorials.

```python
encrypted_name = client_encryption.encrypt(
    "Greg",
    Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
    key_id=data_key_id,
)
encrypted_foods = client_encryption.encrypt(
    ["Cheese", "Grapes"],
    Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Random,
    key_id=data_key_id,
)
coll.insert_one({"name": encrypted_name, "age": 83, "foods": encrypted_foods})
```

**csharp:**

**Note:**

The `dataKeyId` variable in the following examples refers to a
Data Encryption Key (DEK). To learn how to generate a DEK with your Local Key
Provider, see the Quick Start. To learn how to create a 
DEK with a specific Key Management System, see csfle-tutorials.

```csharp
var encryptedName = clientEncryption.Encrypt(
    "Greg",
    new EncryptOptions(algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic", keyId: dataKeyId),
    CancellationToken.None);
var encryptedFoods = clientEncryption.Encrypt(
    new BsonArray { "Cheese", "Grapes" },
    new EncryptOptions(algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Random", keyId: dataKeyId),
    CancellationToken.None);
collection.InsertOne(new BsonDocument { { "name", encryptedName }, { "age", 83 }, { "foods", encryptedFoods } });
```

**go:**

**Note:**

The `dataKeyId` variable in the following examples refers to a
Data Encryption Key (DEK). To learn how to generate a DEK with your Local Key
Provider, see the Quick Start. To learn how to create a 
DEK with a specific Key Management System, see csfle-tutorials.

```go
nameRawValueType, nameRawValueData, err := bson.MarshalValue("Greg")
if err != nil {
	panic(err)
}
nameRawValue := bson.RawValue{Type: nameRawValueType, Value: nameRawValueData}
nameEncryptionOpts := options.Encrypt().
	SetAlgorithm("AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic").
	SetKeyID(dataKeyId)
nameEncryptedField, err := clientEnc.Encrypt(
	context.TODO(),
	nameRawValue,
	nameEncryptionOpts)
if err != nil {
	panic(err)
}
foodsRawValueType, foodsRawValueData, err := bson.MarshalValue(bson.A{"Grapes", "Cheese"})
if err != nil {
	panic(err)
}
foodsRawValue := bson.RawValue{Type: foodsRawValueType, Value: foodsRawValueData}
encryptionOpts := options.Encrypt().
	SetAlgorithm("AEAD_AES_256_CBC_HMAC_SHA_512-Random").
	SetKeyID(dataKeyId)
foodsEncryptedField, err := clientEnc.Encrypt(
	context.TODO(),
	foodsRawValue,
	encryptionOpts)
if err != nil {
	panic(err)
}

_, err = coll.InsertOne(
	context.TODO(),
	bson.D{{"name", nameEncryptedField}, {"foods", foodsEncryptedField}, {"age", 83}})
if err != nil {
	panic(err)
}
```

**shell:**

**Note:**

The `dataKeyId` variable in the following examples refers to a
Data Encryption Key (DEK). To learn how to generate a DEK with your Local Key
Provider, see the Quick Start. To learn how to create a 
DEK with a specific Key Management System, see csfle-tutorials.

```javascript
const encName = clientEncryption.encrypt(
  dataKeyId,
  "Greg",
  "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
);
const encFoods = clientEncryption.encrypt(
  dataKeyId,
  ["Cheese", "Grapes"],
  "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
);
db.getSiblingDB(database).getCollection(collection).insertOne({
  name: encName,
  foods: encFoods,
});
```

**Step 4: Retrieve Document and Decrypt Fields**

The following code snippets show how to retrieve your inserted document
and manually decrypt the encrypted fields:

**java-sync:**

```java
BsonBinary encryptedNameQuery = clientEncryption.encrypt(new BsonString("Greg"), new EncryptOptions("AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic").keyId(dataKeyId));
Document result = collection.find(eq("name", encryptedNameQuery)).first();
System.out.println("Encrypted Document: " + result.toJson());
result.replace("name", clientEncryption.decrypt(new BsonBinary(result.get("name", Binary.class).getData())));
result.replace("foods", clientEncryption.decrypt(new BsonBinary(result.get("foods", Binary.class).getData())));
System.out.println("Decrypted Document: " + result.toJson());
```

**nodejs:**

```javascript
queryEncryptedName = await encryption.encrypt("Greg", {
  algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic",
  keyId: dataKeyId,
});
let doc = await collection.findOne({ name: queryEncryptedName });
console.log("Encrypted Document: ", doc);
doc.name = encryption.decrypt(doc.name);
doc.foods = encryption.decrypt(doc.foods);
console.log("Decrypted document: ", doc);
```

**python:**

```python
name_to_query = "Greg"
encrypted_name_to_query = client_encryption.encrypt(
    name_to_query,
    Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
    key_id=data_key_id,
)
doc = client.employees.foods.find_one({"name": encrypted_name_to_query})
print("Encrypted document: %s" % (doc,))
doc["name"] = client_encryption.decrypt(doc["name"])
doc["foods"] = client_encryption.decrypt(doc["foods"])
print("Decrypted document: %s" % (doc,))
```

**csharp:**

```csharp
var nameToQuery = "Greg";
var encryptedNameToQuery = clientEncryption.Encrypt(
    nameToQuery,
    new EncryptOptions(algorithm: "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic", keyId: dataKeyId),
    CancellationToken.None);
var doc = collection.Find(new BsonDocument { { "name", encryptedNameToQuery } }).Single();
Console.WriteLine($"Encrypted document: {doc}");
doc["name"] = clientEncryption.Decrypt(doc["name"].AsBsonBinaryData, CancellationToken.None);
doc["foods"] = clientEncryption.Decrypt(doc["foods"].AsBsonBinaryData, CancellationToken.None);
Console.WriteLine($"Decrypted field: {doc}");
```

**go:**

```go
nameQueryRawValueType, nameQueryRawValueData, err := bson.MarshalValue("Greg")
if err != nil {
	panic(err)
}
nameQueryRawValue := bson.RawValue{Type: nameQueryRawValueType, Value: nameQueryRawValueData}
nameQueryEncryptionOpts := options.Encrypt().
	SetAlgorithm("AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic").
	SetKeyID(dataKeyId)
nameQueryEncryptedField, err := clientEnc.Encrypt(
	context.TODO(),
	nameQueryRawValue,
	nameQueryEncryptionOpts)
if err != nil {
	panic(err)
}
var result bson.M
err = coll.FindOne(
	context.TODO(),
	bson.D{{"name", nameQueryEncryptedField}}).Decode(&result)
if err != nil {
	if err == mongo.ErrNoDocuments {
		return
	}
	panic(err)
}
fmt.Printf("Encrypted Document: %s\n", result)
nameDecrypted, err := clientEnc.Decrypt(
	context.TODO(),
	result["name"].(primitive.Binary))
foodsDecrypted, err := clientEnc.Decrypt(
	context.TODO(),
	result["foods"].(primitive.Binary))
result["foods"] = foodsDecrypted
result["name"] = nameDecrypted
fmt.Printf("Decrypted Document: %s\n", result)
```

**shell:**

```javascript
const encNameQuery = clientEncryption.encrypt(
  dataKeyId,
  "Greg",
  "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
);
let doc = db.getSiblingDB(database).getCollection(collection).findOne({
  name: encNameQuery,
});
console.log(doc);
doc.name = clientEncryption.decrypt(doc.name);
doc.foods = clientEncryption.decrypt(doc.foods);
console.log(doc);
```

## Server-Side Field Level Encryption Enforcement

MongoDB supports using schema validation to enforce encryption of specific fields
in a collection.

A client performing Client-Side Field Level Encryption with the explicit encryption
mechanism on a MongoDB instance configured to enforce encryption
of certain fields must encrypt those fields as specified on
the MongoDB instance.

To learn how to set up server-side CSFLE
enforcement, see csfle-reference-server-side-schema.

## Learn More

To learn more about Key Vault collections, Data Encryption Keys, and Customer Master Keys,
see csfle-reference-keys-key-vaults.

To learn more about KMS ({+kms-long+}) providers and `kmsProviders` objects,
see csfle-reference-kms-providers.
