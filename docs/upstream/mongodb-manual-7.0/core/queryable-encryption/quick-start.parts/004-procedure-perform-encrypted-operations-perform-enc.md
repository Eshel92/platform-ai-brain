<!-- Part 4 of 5 of core/queryable-encryption/quick-start.md (split because the page is big). -->

### Perform Encrypted Operations

After you configure your application and database connection, you can
insert and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

Add the following code blocks under the ``// Paste code to insert
a document below`` comment in the order shown.

First, configure your application to use the POJO classes that
you created:

```java
CodecProvider pojoCodecProvider = PojoCodecProvider.builder().automatic(true).build();
CodecRegistry pojoCodecRegistry = fromRegistries(getDefaultCodecRegistry(), fromProviders(pojoCodecProvider));
```

Then, create an instance of a `Patient` that describes a
patient's personal information and use the encrypted client to
insert it into the `patients` collection:

```java
MongoDatabase encryptedDb = encryptedClient.getDatabase(encryptedDatabaseName).withCodecRegistry(pojoCodecRegistry);
MongoCollection<Patient> collection = encryptedDb.getCollection(encryptedCollectionName, Patient.class);

PatientBilling patientBilling = new PatientBilling("Visa", "4111111111111111");
PatientRecord patientRecord = new PatientRecord("987-65-4320", patientBilling);
Patient patientDocument = new Patient("Jon Doe", patientRecord);

InsertOneResult result = collection.insertOne(patientDocument);
```

**Step 2: Query on encrypted data.**

Paste the following code under the ``// Paste code to query the
document below`` comment to execute a find query on an encrypted
field and print the decrypted data:

```java
Patient findResult = collection.find(
    new BsonDocument()
            .append("patientRecord.ssn", new BsonString("987-65-4320")))
            .first();

System.out.println(findResult);
```

**Step 3: Compile and run your application.**

To compile and run your application, run the following commands
from your `JavaQE` directory:

```bash
mvn clean package
java -jar target/queryable-encryption-tutorial.jar
```

The driver decrypts the encrypted fields automatically when it
returns the document. The output resembles the following:

```none
{id=648b384a722cb9b8392df76a, name='Jon Doe', patientRecord={ssn='987-65-4320', billing={cardType='Visa', cardNumber='4111111111111111'}, billAmount=1500}}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.


### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Install libmongocrypt 1.8.0 or later**

For instructions on how to install `libmongocrypt`, select your 
operating system and the Go driver on the qe-install 
page.

**Step 2: Install dependencies.**

Create a directory named `go-qe` to store your project files. Run the
following commands to navigate into the directory, initialize your
project, and install the required packages:

```bash
cd go-qe
go mod init go-qe
go get go.mongodb.org/mongo-driver/v2/mongo
go get github.com/joho/godotenv
```

**Step 3: Set up your environment variables.**

In your `go-qe` directory, create a `.env` file. The sample code in
this tutorial references environment variables that you need to set in
this `.env` file. Paste the following code into this file:

```bash
# MongoDB replica set connection URI
export MONGODB_URI="<Your MongoDB Connection URI>"

# MongoDB Automatic Encryption Shared Library 
export SHARED_LIB_PATH="<Full path to your Automatic Encryption Shared Library>"
```

Replace the following placeholder values:

- `<Your MongoDB URI>`: Your MongoDB deployment connection URI.
- `<Full path to your Automatic Encryption Shared Library>`: The
  full path to your Automatic Encryption Shared Library, which resembles the following
  paths:

  - **macOS**: `/<crypt shared directory>/lib/mongo_crypt_v1.dylib`
  - **Linux**: `/<crypt shared directory>/lib/mongo_crypt_v1.so`
  - **Windows**: `C:\<crypt shared directory>\bin\mongo_crypt_v1.dll`

For more information on setting up environment variables, see the
[README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/go/README.md)  file included in the
sample application on GitHub.

**Step 4: Create your data model file.**

This Go tutorial uses structs to represent the document structure. In your ]
`go-qe` directory, create a file named `models.go`
and paste the following code into this file:

```go
package main

/*
	This file contains a sample data model you can use
	to serialize data you store in MongoDB and deserialize
	your retrieved data from MongoDB.
*/

// start-patient-document
type PatientDocument struct {
	PatientName   string        `bson:"patientName"`
	PatientID     int32         `bson:"patientId"`
	PatientRecord PatientRecord `bson:"patientRecord"`
}

// end-patient-document

// start-patient-record
type PatientRecord struct {
	SSN     string      `bson:"ssn"`
	Billing PaymentInfo `bson:"billing"`
}

// end-patient-record

// start-payment-info
type PaymentInfo struct {
	Type   string `bson:"type"`
	Number string `bson:"number"`
}

// end-payment-info
```

**Step 5: Create your main project file.**

In your `go-qe` directory, create a file named `main.go`. Paste the
following starter code into this file. The placeholder comments indicate
where you will add code in future steps of this tutorial:

```go
package main

import (
    "context"
    "crypto/rand"
    "encoding/json"
    "fmt"
    "os"

    "github.com/joho/godotenv"
    "go.mongodb.org/mongo-driver/v2/bson"
    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

func main() {

    if err := godotenv.Load(".env"); err != nil {
        panic("Error loading .env file")
    }

    // Paste application variables below

    // Paste code to generate CMK below

    // Paste code to retrieve CMK and specify KMS provider settings below

    // Paste automatic encryption options code below

    // Paste client configuration code below

    // Paste JSON schema below

    // Paste code to create an encrypted collection below

    // Paste code to insert a document below

    // Paste code to query the document below
}
```

**Step 6: Assign your application variables.**

Declare the required application variables by pasting the following code 
into your `main.go` file under the ``// Paste application variables 
below` comment. For this tutorial, set the `kmsProviderName`` variable to 
`"local"`.

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

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS that stores your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable. |
| `keyVaultDatabaseName` | The database that stores your DEKs. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection that stores your DEKs. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB that stores your DEKs. Set this variable to the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database that stores your encrypted data. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection that stores your encrypted data. Set to `"patients"`. |


### Configure Encryption

After you set up your project, follow the steps in this section to create an
encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your `main.go` file under the
`// Paste code to generate CMK below` comment. This code snippet creates
a 96-byte Customer Master Key and saves it to your filesystem as the
file `customer-master-key.txt`:

```go
key := make([]byte, 96)
if _, err := rand.Read(key); err != nil {
	panic(fmt.Sprintf("Unable to create a random 96 byte data key: %v\n", err))
}
if err := os.WriteFile("customer-master-key.txt", key, 0644); err != nil {
	panic(fmt.Sprintf("Unable to write key to file: %v\n", err))
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

Paste the following code into your `main.go` file under the
`// Paste code to retrieve CMK and specify KMS provider settings below`
comment to retrieve the contents of the `customer-master-key.txt` file:

```go
key, err := os.ReadFile("customer-master-key.txt")
if err != nil {
	panic(fmt.Sprintf("Could not read the Customer Master Key: %v", err))
}
kmsProviderCredentials := map[string]map[string]interface{}{"local": {"key": key}}
```

This code sets the provider name to `local` to use a Local Key Provider
and uses the CMK ({+cmk-long+}) value from your KMS provider settings.

**Step 3: Set your automatic encryption options.**

Add the following code under the
`// Paste automatic encryption options code below` comment to create an
`AutoEncryption` object that contains the following options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, defined in the previous step
- The `cryptSharedLibraryPath` object, which contains the path to your
  Automatic Encryption Shared Library

```go
cryptSharedLibraryPath := map[string]interface{}{
	"cryptSharedLibPath": os.Getenv("SHARED_LIB_PATH"), // Path to your Automatic Encryption Shared Library
}

autoEncryptionOptions := options.AutoEncryption().
	SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviderCredentials).
	SetExtraOptions(cryptSharedLibraryPath)
```

**Step 4: Create a client to set up an encrypted collection.**

Create a new client to encrypt and decrypt your collection. The client
uses your connection URI and automatic encryption options. Paste the
following code into your `main.go` file, under the
`// Paste client configuration code below` comment:

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

**Step 5: Specify fields to encrypt.**

To encrypt a field, add it to the encryption schema. To enable queries on a
field, add the `queries` property. Paste the following code under the
`// Paste JSON schema below` comment:

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

**Note:**

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your `main.go` file, under the
`// Paste code to create an encrypted collection below` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the API for the
encryption helper methods:

```go
clientEncryptionOpts := options.ClientEncryption().
	SetKeyVaultNamespace(keyVaultNamespace).
	SetKmsProviders(kmsProviderCredentials)

clientEncryption, err := mongo.NewClientEncryption(encryptedClient, clientEncryptionOpts)
if err != nil {
	panic(fmt.Sprintf("Unable to create a ClientEncryption instance due to the following error: %s\n", err))
}
```

Because you are using a local Customer Master Key, you don't need to provide
Customer Master Key credentials. Create a variable containing an empty object to
use in place of credentials when you create your encrypted collection:

```go
customerMasterKey := map[string]string{}
```

To create your encrypted collection, use the `ClientEncryption` object's 
`CreateEncryptedCollection()` helper method. This method automatically
generates data encryption keys for your encrypted fields and creates the
encrypted collection:

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


### Perform Encrypted Operations

After you configure your application and database connection, you can insert
and query encrypted documents.

**Step 1: Insert a document with encrypted fields.**

Paste the following code under the
`// Paste code to insert a document below` comment to create a
document that stores patient data and insert it into the `patients`
collection:

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

**Step 2: Query on encrypted data.**

Add the following code to your `main.go` file under the
`// Paste code to query the document below` comment:

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

**Step 3: Compile and run your application.**

To compile and run your application, run the following commands from your 
project directory:

```bash
go build -tags cse 
./go-qe
```

The output of the preceding code sample should look similar to the
following:

```json
{
    "PatientName": "Jon Doe",
    "PatientID": 12345678,
    "PatientRecord": {
        "SSN": "987-65-4320",
        "Billing": {
            "Type": "Visa",
            "Number": "4111111111111111"
        },
        "BillAmount": 1500
    }
}
```

**Warning:** Do not Modify the __safeContent__ Field

The `__safeContent__` field is essential to Queryable Encryption. Do not modify
the contents of this field.
