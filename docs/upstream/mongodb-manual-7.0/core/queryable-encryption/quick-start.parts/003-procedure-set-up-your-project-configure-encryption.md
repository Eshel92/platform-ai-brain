<!-- Part 3 of 5 of core/queryable-encryption/quick-start.md (split because the page is big). -->

### Set Up Your Project

Follow the steps in this section to create your project files and
assign the required configuration variables.

**Step 1: Install dependencies.**

This tutorial uses Apache Maven to manage dependencies. In an Integrated
Development Environment (IDE), create a new Maven project named 
`JavaQE`. Then, navigate to the `pom.xml` file and add the following 
dependencies:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.mongodb.tutorials</groupId>
  <artifactId>queryable-encryption-tutorial</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
  </properties>

  <dependencies>

    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-driver-sync</artifactId>
      <version>4.10.1</version>
    </dependency>
    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-driver-core</artifactId>
      <version>4.10.1</version>
    </dependency>
    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>bson</artifactId>
      <version>4.10.1</version>
    </dependency>

    <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-crypt</artifactId>
      <version>1.8.0</version>
    </dependency>

    <dependency>
      <groupId>io.github.cdimascio</groupId>
      <artifactId>dotenv-java</artifactId>
      <version>3.0.0</version>
    </dependency>

  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-assembly-plugin</artifactId>
        <version>3.6.0</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>single</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <archive>
            <manifest>
              <mainClass>com.mongodb.tutorials.qe.QueryableEncryptionTutorial</mainClass>
              <addClasspath>true</addClasspath>
            </manifest>
          </archive>
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
          </descriptorRefs>
          <appendAssemblyId>false</appendAssemblyId>
          <finalName>${project.artifactId}</finalName>
        </configuration>
      </plugin>
    </plugins>
    <finalName>${project.artifactId}</finalName>
  </build>
</project>
```

This code installs the MongoDB Java Sync Driver and the `mongodb-crypt` 
package, which provides the necessary classes for Queryable Encryption. It also installs
the `dotenv-java` package, which reads your credentials from a `.env`
file.

**Step 2: Set up your environment variables.**

In your `JavaQE` directory, create a file named `.env`. The
sample code in this tutorial reads its configuration from this
file. Paste the following code into this file:

```bash
# MongoDB connection uri and automatic encryption shared library path

MONGODB_URI="<Your MongoDB URI>"
SHARED_LIB_PATH="<Full path to your Automatic Encryption Shared Library>"
```

Replace the following placeholder values:

- `<Your MongoDB URI>`: Your MongoDB deployment connection URI.
- `<Full path to your Automatic Encryption Shared Library>`: The
  full path to your Automatic Encryption Shared Library, which resembles the following
  paths:

  - **macOS**: `/<crypt shared directory>/lib/mongo_crypt_v1.dylib`
  - **Linux**: `/<crypt shared directory>/lib/mongo_crypt_v1.so`
  - **Windows**: `C:\<crypt shared directory>\bin\mongo_crypt_v1.dll`

For more information on setting up your environment variables,
see the [README.md](https://github.com/mongodb/docs/tree/main/content/manual/v7.0/source/includes/qe-tutorials/java/README.md) file
included in the sample application on GitHub.

**Step 3: Create your data model classes.**

This tutorial uses Plain Old Java Objects (POJOs) as data models
to represent the document structure. In your
`src/main/java/com/mongodb/tutorials/qe/models` directory,
create a file named `Patient.java` and paste the following `Patient` 
class into the file:

```java
package com.mongodb.tutorials.qe.models;

import org.bson.types.ObjectId;

public class Patient {
    public ObjectId id;
    public String name;

    public PatientRecord patientRecord;

    public Patient() {
    }

    public Patient(String name, PatientRecord patientRecord) {
        this.name = name;
        this.patientRecord = patientRecord;
    }

    public ObjectId getId() {
        return id;
    }

    public void setId(ObjectId id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PatientRecord getPatientRecord() {
        return patientRecord;
    }

    public void setPatientRecord(PatientRecord patientRecord) {
        this.patientRecord = patientRecord;
    }

    @Override
    public String toString() {
        return "{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", patientRecord=" + patientRecord +
                '}';
    }
}
```

Then, create a file named `PatientRecord.java` and paste the following 
`PatientRecord` class into the file:

```java
package com.mongodb.tutorials.qe.models;

public class PatientRecord {
    public String ssn;
    public PatientBilling billing;

    public PatientRecord() {
    }

    public PatientRecord(String ssn, PatientBilling billing) {
        this.ssn = ssn;
        this.billing = billing;
    }

    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }

    public PatientBilling getBilling() {
        return billing;
    }

    public void setBilling(PatientBilling billing) {
        this.billing = billing;
    }

    @Override
    public String toString() {
        return "{" +
                "ssn='" + ssn + '\'' +
                ", billing=" + billing +
                '}';
    }
}
```

Finally, create a file named `PatientBilling.java` and paste the 
following `PatientBilling` class into the file:

```java
package com.mongodb.tutorials.qe.models;

public class PatientBilling {
    public String cardType;
    public String cardNumber;

    public PatientBilling() {
    }

    public PatientBilling(String cardType, String cardNumber) {
        this.cardType = cardType;
        this.cardNumber = cardNumber;
    }

    public String getCardType() {
        return cardType;
    }

    public void setCardType(String cardType) {
        this.cardType = cardType;
    }

    public String getCardNumber() {
        return cardNumber;
    }

    public void setCardNumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    @Override
    public String toString() {
        return "{" +
                "cardType='" + cardType + '\'' +
                ", cardNumber='" + cardNumber + '\'' +
                '}';
    }
}
```

To learn more about Java POJOs, see the [Plain Old Java Object](https://en.wikipedia.org/wiki/Plain_old_Java_object)
Wikipedia article.

**Step 4: Create your application file.**

In your `src/main/java/com/mongodb/tutorials/qe` directory,
create a file named `QueryableEncryptionTutorial.java`. This
file contains the main Queryable Encryption workflow. Paste the following
starter code into this file. The placeholder comments indicate
where you add code in later steps of this tutorial:

```java
package com.mongodb.tutorials.qe;

import com.mongodb.AutoEncryptionSettings;
import com.mongodb.ClientEncryptionSettings;
import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.CreateCollectionOptions;
import com.mongodb.client.model.CreateEncryptedCollectionParams;
import com.mongodb.client.result.InsertOneResult;
import com.mongodb.client.vault.ClientEncryption;
import com.mongodb.client.vault.ClientEncryptions;
import com.mongodb.tutorials.qe.models.Patient;
import com.mongodb.tutorials.qe.models.PatientBilling;
import com.mongodb.tutorials.qe.models.PatientRecord;
import io.github.cdimascio.dotenv.Dotenv;
import org.bson.BsonArray;
import org.bson.BsonDocument;
import org.bson.BsonNull;
import org.bson.BsonString;
import org.bson.codecs.configuration.CodecProvider;
import org.bson.codecs.configuration.CodecRegistry;
import org.bson.codecs.pojo.PojoCodecProvider;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static com.mongodb.MongoClientSettings.getDefaultCodecRegistry;
import static org.bson.codecs.configuration.CodecRegistries.fromProviders;
import static org.bson.codecs.configuration.CodecRegistries.fromRegistries;

public class QueryableEncryptionTutorial {

    // Loads values from your .env file
    // Later steps call getEnv() to read your configuration values
    static class QueryableEncryptionHelpers {
        private static final Dotenv dotEnv = Dotenv.configure()
                .directory("./.env")
                .load();

        public static String getEnv(String name) {
            return dotEnv.get(name);
        }
    }

    static String getEnv(String name) {
        return QueryableEncryptionHelpers.getEnv(name);
    }

    public static void main(String[] args) throws Exception {
        // Paste application variables below

        // Paste code to generate CMK below

        // Paste code to retrieve the CMK and specify KMS provider settings below

        // Paste automatic encryption options code below

        // Paste client settings code below

        try (MongoClient encryptedClient = MongoClients.create(clientSettings)) {

            // Paste schema below

            // Paste code to create an encrypted collection below

            // Paste code to insert a document below

            // Paste code to query the document below

        }
    }
}
```

**Step 5: Assign your application variables.**

The code samples in this tutorial use the following variables to
perform the Queryable Encryption workflow. Paste the following code into the
`main()` method of `QueryableEncryptionTutorial.java`, under
the `// Paste application variables below` comment. For this
tutorial, set the `kmsProviderName` variable to `"local"`:

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

| Variable | Description |
|---|---|
| `kmsProviderName` | The KMS that stores your Customer Master Key. For this tutorial, set this variable to `"local"`. |
| `uri` | Your MongoDB connection URI. Set with the `MONGODB_URI` environment variable in your `.env` file. |
| `keyVaultDatabaseName` | The database that stores your DEKs. Set to `"encryption"`. |
| `keyVaultCollectionName` | The collection that stores your DEKs. Set to `"__keyVault"`. |
| `keyVaultNamespace` | The namespace in MongoDB that stores your DEKs. Set this variable to the values of the `keyVaultDatabaseName` and `keyVaultCollectionName` variables, separated by a period. |
| `encryptedDatabaseName` | The database that stores your encrypted data. Set to `"medicalRecords"`. |
| `encryptedCollectionName` | The collection that stores your encrypted data. Set to `"patients"`. |


### Configure Encryption

After you set up your project, follow the steps in this section to
create an encryption key and configure your application for Queryable Encryption.

**Step 1: Create an encryption key.**

Paste the following code into your
`QueryableEncryptionTutorial.java` file under the
`// Paste code to generate CMK below` comment. This code
creates a 96-byte Customer Master Key and saves it to your filesystem as
the file `customer-master-key.txt`:

```java
// Reuse the key from the customer-master-key.txt file if it exists
if (!new File("./customer-master-key.txt").isFile()) {
    byte[] localCustomerMasterKey = new byte[96];
    new SecureRandom().nextBytes(localCustomerMasterKey);
    try (FileOutputStream stream = new FileOutputStream("customer-master-key.txt")) {
        stream.write(localCustomerMasterKey);
    } catch (Exception e) {
        throw new Exception("Unable to write Customer Master Key file due to the following error:" + e.getMessage());
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

Paste the following code under the ``// Paste code to retrieve
the CMK and specify KMS provider settings below`` comment. This
code retrieves the contents of the `customer-master-key.txt`
file and uses the CMK ({+cmk-long+}) value in your KMS provider
settings. Setting the provider name to `local` indicates that
you are using a Local Key Provider:

```java
byte[] localCustomerMasterKey = new byte[96];

try (FileInputStream fis = new FileInputStream("customer-master-key.txt")) {
    if (fis.read(localCustomerMasterKey) < 96)
        throw new Exception("Expected to read 96 bytes from the customer master key file");
} catch (Exception e) {
    throw new Exception("Unable to read the Customer Master Key due to the following error: " + e.getMessage());
}
Map<String, Object> keyMap = new HashMap<String, Object>();
keyMap.put("key", localCustomerMasterKey);

Map<String, Map<String, Object>> kmsProviderCredentials = new HashMap<String, Map<String, Object>>();
kmsProviderCredentials.put("local", keyMap);
```

**Step 3: Set your automatic encryption options.**

Paste the following code under the ``// Paste automatic
encryption options code below`` comment. This code creates an
`AutoEncryptionSettings` object that contains the following
options:

- The namespace of your Key Vault collection
- The `kmsProviderCredentials` object, defined in the previous
  step
- The `extraOptions` object, which contains the path to your
  Automatic Encryption Shared Library

```java
Map<String, Object> extraOptions = new HashMap<String, Object>();
extraOptions.put("cryptSharedLibPath", getEnv("SHARED_LIB_PATH")); // Path to your Automatic Encryption Shared Library

AutoEncryptionSettings autoEncryptionSettings = AutoEncryptionSettings.builder()
        .keyVaultNamespace(keyVaultNamespace)
        .kmsProviders(kmsProviderCredentials)
        .extraOptions(extraOptions)
        .build();
```

**Step 4: Create a client to set up an encrypted collection.**

To create a client that encrypts and decrypts data in your
collection, paste the following code under the ``// Paste client
settings code below`` comment. This code builds the
`clientSettings` object from your connection URI and your
automatic encryption options:

```java
MongoClientSettings clientSettings = MongoClientSettings.builder()
        .applyConnectionString(new ConnectionString(uri))
        .autoEncryptionSettings(autoEncryptionSettings)
        .build();
```

The `try` block in your starter code passes these settings to
`MongoClients.create()` to instantiate the encrypted client.

**Step 5: Specify fields to encrypt.**

To encrypt a field, add it to the encryption schema. To enable
queries on a field, add the `queries` property. Paste the
following code under the `// Paste schema below` comment:

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

**Note:**

The previous code sample encrypts both the `ssn` and `billing` fields. 
However, only the `ssn` field can be queried because it contains the 
`queries` property.

**Step 6: Create your encrypted collection.**

Add the following code blocks to your
`QueryableEncryptionTutorial.java` file under the ``// Paste
code to create an encrypted collection below`` comment in the
order shown.

First, instantiate a `ClientEncryption` object to access the
API for the encryption helper methods:

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

Because you are using a local Customer Master Key, you don't need to
provide Customer Master Key credentials. Create a variable containing an
empty object to use in place of credentials when you create your
encrypted collection:

```java
BsonDocument customerMasterKeyCredentials = new BsonDocument();
```

Create your encrypted collection by using the 
`createEncryptedCollection()` helper method accessed through the 
`ClientEncryption` class. This method automatically generates data 
encryption keys for your encrypted fields and creates the encrypted 
collection:

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
