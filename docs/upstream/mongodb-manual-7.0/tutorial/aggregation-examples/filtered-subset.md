<!-- Converted from tutorial/aggregation-examples/filtered-subset.txt (reStructuredText). Includes are inlined. -->

# Filter Data in an Aggregation Pipeline

This tutorial illustrates how to construct an aggregation pipeline,
perform the aggregation on a collection, and display the results using
the language of your choice.

## About This Task

The aggregation pipeline in this tutorial performs the following
operations:

- Matches a subset of documents by a field value
- Formats result documents

## Before You Begin

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The aggregation selects documents based on whether their field values
match specified criteria.

**Step 1: Run the aggregation pipeline.**

```javascript
db.movies.aggregate( [
   // Stage 1: Match documents with the Drama genre
   { $match: { genres: "Drama" } },

   // Stage 2: Sort documents from oldest to newest
   { $sort: { year: 1 } },

   // Stage 3: Limit the results to 3 documents
   { $limit: 3 },

   // Stage 4: Project only the fields needed for the result
   { $project: { _id: 0, title: 1, year: 1, directors: 1, runtime: 1 } }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregated results contain three documents. The documents
represent the three oldest movies in the `Drama` genre,
ordered from oldest to newest. The results include only the
`title`, `year`, `directors`, and `runtime` fields.

```javascript
[
  {
    runtime: 14,
    title: 'A Corner in Wheat',
    directors: [
      'D.W. Griffith'
    ],
    year: 1909
  },
  {
    runtime: 88,
    title: 'Traffic in Souls',
    directors: [
      'George Loane Tucker'
    ],
    year: 1913
  },
  {
    runtime: 65,
    title: 'In the Land of the Head Hunters',
    directors: [
      'Edward S. Curtis'
    ],
    year: 1914
  }
]
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Python app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install PyMongo and connect to MongoDB,
see the [Get Started with PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
tutorial.

To learn more about performing aggregations in PyMongo, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.py`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```python
# Modify imports for each tutorial as needed.
from pymongo import MongoClient

# Replace the placeholder with your connection string.
uri = "<connection string>"
client = MongoClient(uri)

try:
    agg_db = client["agg_tutorials_db"]

    # Get a reference to relevant collections.
    # ... some_coll = agg_db["some_coll"]
    # ... another_coll = agg_db["another_coll"]

    # Delete any existing documents in collections if needed.
    # ... some_coll.delete_many({})

    # Insert sample data into the collection or collections.
    # ... some_coll.insert_many(...)

    # Create an empty pipeline array.
    pipeline = []

    # Add code to create pipeline stages.
    # ... pipeline.append({...})

    # Run the aggregation.
    # ... aggregation_result = ...

    # Print the aggregation results.
    for document in aggregation_result:
        print(document)

finally:
    client.close()
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```php
uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```python
person_coll = agg_db["persons"]
person_coll.delete_many({})

person_data = [
    {
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": datetime(1972, 1, 13, 9, 32, 7),
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj",
        },
    },
    {
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": datetime(1985, 5, 12, 23, 14, 30),
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo",
        },
    },
    {
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": datetime(1991, 11, 23, 16, 53, 56),
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington",
        },
    },
    {
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": datetime(1941, 4, 7, 22, 11, 52),
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville",
        },
    },
    {
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": datetime(1959, 7, 6, 17, 35, 45),
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge",
        },
    },
    {
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": datetime(1998, 12, 26, 13, 13, 55),
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford",
        },
    },
]

person_coll.insert_many(person_data)
```

**Step 1: Add a match stage for people who are engineers.**

In your `Pipeline` instance, create a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```python
pipeline.append({"$match": {"vocation": "ENGINEER"}})
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```python
pipeline.append({"$sort": {"dateofbirth": -1}})
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```python
pipeline.append({"$limit": 3})
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```python
pipeline.append({"$unset": ["_id", "address"]})
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```python
aggregation_result = person_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{'person_id': '7363626383', 'firstname': 'Carl', 'lastname': 'Simmons', 'dateofbirth': datetime.datetime(1998, 12, 26, 13, 13, 55), 'vocation': 'ENGINEER'}
{'person_id': '1723338115', 'firstname': 'Olive', 'lastname': 'Ranieri', 'dateofbirth': datetime.datetime(1985, 5, 12, 23, 14, 30), 'gender': 'FEMALE', 'vocation': 'ENGINEER'}
{'person_id': '6392529400', 'firstname': 'Elise', 'lastname': 'Smith', 'dateofbirth': datetime.datetime(1972, 1, 13, 9, 32, 7), 'vocation': 'ENGINEER'}
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Java app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Get Started with the Java Driver guide`.

To learn more about performing aggregations in the Java Sync Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`AggTutorial.java`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```java
package org.example;

// Modify imports for each tutorial as needed.
import com.mongodb.client.*;
import com.mongodb.client.model.Aggregates;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Sorts;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AggTutorial {
    public static void main( String[] args ) {

        // Replace the placeholder with your connection string.
        String uri = "<connection string>";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            MongoDatabase aggDB = mongoClient.getDatabase("agg_tutorials_db");

            // Get a reference to relevant collections.
            // ... MongoCollection<Document> someColl = ...
            // ... MongoCollection<Document> anotherColl = ...

            // Delete any existing documents in collections if needed.
            // ... someColl.deleteMany(Filters.empty());

            // Insert sample data into the collection or collections.   
            // ... someColl.insertMany(...);

            // Create an empty pipeline array.
            List<Bson> pipeline = new ArrayList<>();

            // Add code to create pipeline stages.
            // ... pipeline.add(...);

            // Run the aggregation.
            // ... AggregateIterable<Document> aggregationResult = someColl.aggregate(pipeline);

            // Print the aggregation results.
            for (Document document : aggregationResult) {
                System.out.println(document.toJson());
            }
        }
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Java Sync Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```java
String uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```java
MongoCollection<Document> persons = aggDB.getCollection("persons");
persons.deleteMany(Filters.empty());

persons.insertMany(
        Arrays.asList(
                new Document("person_id", "6392529400")
                        .append("firstname", "Elise")
                        .append("lastname", "Smith")
                        .append("dateofbirth", LocalDateTime.parse("1972-01-13T09:32:07"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 5625)
                                .append("street", "Tipa Circle")
                                .append("city", "Wojzinmoj")),
                new Document("person_id", "1723338115")
                        .append("firstname", "Olive")
                        .append("lastname", "Ranieri")
                        .append("dateofbirth", LocalDateTime.parse("1985-05-12T23:14:30"))
                        .append("gender", "FEMALE")
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 9303)
                                .append("street", "Mele Circle")
                                .append("city", "Tobihbo")),
                new Document("person_id", "8732762874")
                        .append("firstname", "Toni")
                        .append("lastname", "Jones")
                        .append("dateofbirth", LocalDateTime.parse("1991-11-23T16:53:56"))
                        .append("vocation", "POLITICIAN")
                        .append("address", new Document("number", 1)
                                .append("street", "High Street")
                                .append("city", "Upper Abbeywoodington")),
                new Document("person_id", "7363629563")
                        .append("firstname", "Bert")
                        .append("lastname", "Gooding")
                        .append("dateofbirth", LocalDateTime.parse("1941-04-07T22:11:52"))
                        .append("vocation", "FLORIST")
                        .append("address", new Document("number", 13)
                                .append("street", "Upper Bold Road")
                                .append("city", "Redringtonville")),
                new Document("person_id", "1029648329")
                        .append("firstname", "Sophie")
                        .append("lastname", "Celements")
                        .append("dateofbirth", LocalDateTime.parse("1959-07-06T17:35:45"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 5)
                                .append("street", "Innings Close")
                                .append("city", "Basilbridge")),
                new Document("person_id", "7363626383")
                        .append("firstname", "Carl")
                        .append("lastname", "Simmons")
                        .append("dateofbirth", LocalDateTime.parse("1998-12-26T13:13:55"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 187)
                                .append("street", "Hillside Road")
                                .append("city", "Kenningford"))
        )
);
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```java
pipeline.add(Aggregates.match(Filters.eq("vocation", "ENGINEER")));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```java
pipeline.add(Aggregates.sort(Sorts.descending("dateofbirth")));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```java
pipeline.add(Aggregates.limit(3));
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```java
pipeline.add(Aggregates.unset("_id", "address"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```java
AggregateIterable<Document> aggregationResult = persons.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id": "7363626383", "firstname": "Carl", "lastname": "Simmons", "dateofbirth": {"$date": "1998-12-26T13:13:55Z"}, "vocation": "ENGINEER"}
{"person_id": "1723338115", "firstname": "Olive", "lastname": "Ranieri", "dateofbirth": {"$date": "1985-05-12T23:14:30Z"}, "gender": "FEMALE", "vocation": "ENGINEER"}
{"person_id": "6392529400", "firstname": "Elise", "lastname": "Smith", "dateofbirth": {"$date": "1972-01-13T09:32:07Z"}, "vocation": "ENGINEER"}
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Kotlin app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Kotlin Driver Quick Start guide`.

To learn more about performing aggregations in the Kotlin Driver, see the
`Aggregation guide`.

In addition to the driver, you must also add the following dependencies
to your `build.gradle.kts` file and reload your project:

```kotlin
dependencies {
    // Implements Kotlin serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.5.1")
    // Implements Kotlin date and time handling
    implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.1")
}
```

After you install the driver, create a file called
`AggTutorial.kt`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```kotlin
package org.example

// Modify imports for each tutorial as needed.
import com.mongodb.client.model.*
import com.mongodb.kotlin.client.coroutine.MongoClient
import kotlinx.coroutines.runBlocking
import kotlinx.datetime.LocalDateTime
import kotlinx.datetime.toJavaLocalDateTime
import kotlinx.serialization.Contextual
import kotlinx.serialization.Serializable
import org.bson.Document
import org.bson.conversions.Bson

// Define data classes.
@Serializable
data class MyClass(
    ...
)

suspend fun main() {
    // Replace the placeholder with your connection string.
    val uri = "<connection string>"

    MongoClient.create(uri).use { mongoClient ->
        val aggDB = mongoClient.getDatabase("agg_tutorials_db")

        // Get a reference to relevant collections.
        // ... val someColl = ...

        // Delete any existing documents in collections if needed.
        // ... someColl.deleteMany(empty())

        // Insert sample data into the collection or collections.
        // ... someColl.insertMany( ... )

        // Create an empty pipeline.
        val pipeline = mutableListOf<Bson>()

        // Add code to create pipeline stages.
        // ... pipeline.add(...)

        // Run the aggregation.
        // ... val aggregationResult = someColl.aggregate<Document>(pipeline)

        // Print the aggregation results.
        aggregationResult.collect { println(it) }
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Connect to your Cluster`
step of the Kotlin Driver Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```java
val uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Kotlin data classes to model the data in the `persons`
collection:

```kotlin
@Serializable
data class Address(
    val number: Int,
    val street: String,
    val city: String
)

@Serializable
data class Person(
    val personID: String,
    val firstname: String,
    val lastname: String,
    @Contextual val dateOfBirth: LocalDateTime,
    val vocation: String,
    val address: Address,
    val gender: String? = null
)
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```kotlin
val persons = aggDB.getCollection<Person>("persons")
persons.deleteMany(Filters.empty())

persons.insertMany(
    listOf(
        Person(
            "6392529400",
            "Elise",
            "Smith",
            LocalDateTime.parse("1972-01-13T09:32:07"),
            "ENGINEER",
            Address(5625, "Tipa Circle", "Wojzinmoj")
        ),
        Person(
            "1723338115",
            "Olive",
            "Ranieri",
            LocalDateTime.parse("1985-05-12T23:14:30"),
            "ENGINEER",
            Address(9303, "Mele Circle", "Tobihbo"),
            "FEMALE"
        ),
        Person(
            "8732762874",
            "Toni",
            "Jones",
            LocalDateTime.parse("1991-11-23T16:53:56"),
            "POLITICIAN",
            Address(1, "High Street", "Upper Abbeywoodington")
        ),
        Person(
            "7363629563",
            "Bert",
            "Gooding",
            LocalDateTime.parse("1941-04-07T22:11:52"),
            "FLORIST",
            Address(13, "Upper Bold Road", "Redringtonville")
        ),
        Person(
            "1029648329",
            "Sophie",
            "Celements",
            LocalDateTime.parse("1959-07-06T17:35:45"),
            "ENGINEER",
            Address(5, "Innings Close", "Basilbridge")
        ),
        Person(
            "7363626383",
            "Carl",
            "Simmons",
            LocalDateTime.parse("1998-12-26T13:13:55"),
            "ENGINEER",
            Address(187, "Hillside Road", "Kenningford")
        )
    )
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```kotlin
pipeline.add(Aggregates.match(Filters.eq(Person::vocation.name, "ENGINEER")))
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateOfBirth` field to
list the youngest people first:

```kotlin
pipeline.add(Aggregates.sort(Sorts.descending(Person::dateOfBirth.name)))
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```kotlin
pipeline.add(Aggregates.limit(3))
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```kotlin
pipeline.add(Aggregates.unset("_id", Person::address.name))
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```kotlin
val aggregationResult = persons.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
Document{{personID=7363626383, firstname=Carl, lastname=Simmons, dateOfBirth=Sat Dec 26 08:13:55 EST 1998, vocation=ENGINEER}}
Document{{personID=1723338115, firstname=Olive, lastname=Ranieri, dateOfBirth=Sun May 12 19:14:30 EDT 1985, vocation=ENGINEER, gender=FEMALE}}
Document{{personID=6392529400, firstname=Elise, lastname=Smith, dateOfBirth=Thu Jan 13 04:32:07 EST 1972, vocation=ENGINEER}}
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Scala app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with the Scala Driver](https://www.mongodb.com/docs/languages/scala/scala-driver/current/get-started/)
guide.

To learn more about performing aggregations in the Scala Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/scala/scala-driver/current/aggregation/).

After you install the driver, create a file called
`AggTutorial.scala`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```scala
package org.example;

// Modify imports for each tutorial as needed.
import org.mongodb.scala.MongoClient
import org.mongodb.scala.bson.Document
import org.mongodb.scala.model.{Accumulators, Aggregates, Field, Filters, Variable}

import java.text.SimpleDateFormat

object FilteredSubset {

  def main(args: Array[String]): Unit = {

    // Replace the placeholder with your connection string.
    val uri = "<connection string>"
    val mongoClient = MongoClient(uri)
    Thread.sleep(1000)

    val aggDB = mongoClient.getDatabase("agg_tutorials_db")

    // Get a reference to relevant collections.
    // ... val someColl = aggDB.getCollection("someColl")
    // ... val anotherColl = aggDB.getCollection("anotherColl")

    // Delete any existing documents in collections if needed.
    // ... someColl.deleteMany(Filters.empty()).subscribe(...)

    // If needed, create the date format template.
    val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

    // Insert sample data into the collection or collections.
    // ... someColl.insertMany(...).subscribe(...)

    Thread.sleep(1000)

    // Add code to create pipeline stages within the Seq.
    // ... val pipeline = Seq(...)

    // Run the aggregation and print the results.
    // ... someColl.aggregate(pipeline).subscribe(...)

    Thread.sleep(1000)
    mongoClient.close()
  }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/scala/scala-driver/current/get-started/#create-a-connection-string)
step of the Scala Driver Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string
assignment resembles the following:

```scala
val uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```scala
val persons = aggDB.getCollection("persons")

persons.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

persons.insertMany(Seq(
  Document(
    "person_id" -> "6392529400",
    "firstname" -> "Elise",
    "lastname" -> "Smith",
    "dateofbirth" -> dateFormat.parse("1972-01-13T09:32:07"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 5625,
      "street" -> "Tipa Circle",
      "city" -> "Wojzinmoj"
    )
  ),
  Document(
    "person_id" -> "1723338115",
    "firstname" -> "Olive",
    "lastname" -> "Ranieri",
    "dateofbirth" -> dateFormat.parse("1985-05-12T23:14:30"),
    "gender" -> "FEMALE",
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 9303,
      "street" -> "Mele Circle",
      "city" -> "Tobihbo"
    )
  ),
  Document(
    "person_id" -> "8732762874",
    "firstname" -> "Toni",
    "lastname" -> "Jones",
    "dateofbirth" -> dateFormat.parse("1991-11-23T16:53:56"),
    "vocation" -> "POLITICIAN",
    "address" -> Document(
      "number" -> 1,
      "street" -> "High Street",
      "city" -> "Upper Abbeywoodington"
    )
  ),
  Document(
    "person_id" -> "7363629563",
    "firstname" -> "Bert",
    "lastname" -> "Gooding",
    "dateofbirth" -> dateFormat.parse("1941-04-07T22:11:52"),
    "vocation" -> "FLORIST",
    "address" -> Document(
      "number" -> 13,
      "street" -> "Upper Bold Road",
      "city" -> "Redringtonville"
    )
  ),
  Document(
    "person_id" -> "1029648329",
    "firstname" -> "Sophie",
    "lastname" -> "Celements",
    "dateofbirth" -> dateFormat.parse("1959-07-06T17:35:45"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 5,
      "street" -> "Innings Close",
      "city" -> "Basilbridge"
    )
  ),
  Document(
    "person_id" -> "7363626383",
    "firstname" -> "Carl",
    "lastname" -> "Simmons",
    "dateofbirth" -> dateFormat.parse("1998-12-26T13:13:55"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 187,
      "street" -> "Hillside Road",
      "city" -> "Kenningford"
    )
  )
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```scala
Aggregates.filter(Filters.equal("vocation", "ENGINEER")),
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```scala
Aggregates.sort(Sorts.descending("dateofbirth")),
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```scala
Aggregates.limit(3),
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```scala
Aggregates.unset("_id", "address")
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```scala
persons.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id": "7363626383", "firstname": "Carl", "lastname": "Simmons", "dateofbirth": {"$date": "1998-12-26T18:13:55Z"}, "vocation": "ENGINEER"}
{"person_id": "1723338115", "firstname": "Olive", "lastname": "Ranieri", "dateofbirth": {"$date": "1985-05-13T03:14:30Z"}, "gender": "FEMALE", "vocation": "ENGINEER"}
{"person_id": "6392529400", "firstname": "Elise", "lastname": "Smith", "dateofbirth": {"$date": "1972-01-13T14:32:07Z"}, "vocation": "ENGINEER"}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new C#/.NET app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `C#/.NET Driver Quick Start guide`.

To learn more about performing aggregations in the C#/.NET Driver, see the
`Aggregation guide`.

After you install the driver, paste the following code into your
`Program.cs` file to create an app template for the aggregation
tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```csharp
using MongoDB.Driver;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

// Define data model classes.
// ... public class MyClass { ... }

// Replace the placeholder with your connection string.
var uri = "<connection string>";
var client = new MongoClient(uri);
var aggDB = client.GetDatabase("agg_tutorials_db");

// Get a reference to relevant collections.
// ... var someColl = aggDB.GetCollection<MyClass>("someColl");
// ... var anotherColl = aggDB.GetCollection<MyClass>("anotherColl");

// Delete any existing documents in collections if needed.
// ... someColl.DeleteMany(Builders<MyClass>.Filter.Empty);

// Insert sample data into the collection or collections.
// ... someColl.InsertMany(new List<MyClass> { ... });

// Add code to chain pipeline stages to the Aggregate() method.
// ... var results = someColl.Aggregate().Match(...);

// Print the aggregation results.
foreach (var result in results.ToList())
{
  Console.WriteLine(result);
}
```

For every tutorial, you must replace the connection string placeholder
with your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Set Up a Free Cluster in Atlas`
step of the C# Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```csharp
var uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create C# classes to model the data in the `persons`
collection:

```csharp
public class Person
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string PersonId { get; set; }
  public string FirstName { get; set; }
  public string LastName { get; set; }
  public DateTime DateOfBirth { get; set; }
  [BsonIgnoreIfNull]
  public string? Gender { get; set; }
  public string Vocation { get; set; }
  public Address Address { get; set; }
}

public class Address
{
  public int Number { get; set; }
  public string Street { get; set; }
  public string City { get; set; }
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```csharp
var persons = aggDB.GetCollection<Person>("persons");
persons.DeleteMany(Builders<Person>.Filter.Empty);

persons.InsertMany(new List<Person>
    {
        new Person
        {
            PersonId = "6392529400",
            FirstName = "Elise",
            LastName = "Smith",
            DateOfBirth = DateTime.Parse("1972-01-13T09:32:07Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 5625,
                Street = "Tipa Circle",
                City = "Wojzinmoj"
            }
        },
        new Person
        {
            PersonId = "1723338115",
            FirstName = "Olive",
            LastName = "Ranieri",
            DateOfBirth = DateTime.Parse("1985-05-12T23:14:30Z"),
            Gender = "FEMALE",
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 9303,
                Street = "Mele Circle",
                City = "Tobihbo"
            }
        },
        new Person
        {
            PersonId = "8732762874",
            FirstName = "Toni",
            LastName = "Jones",
            DateOfBirth = DateTime.Parse("1991-11-23T16:53:56Z"),
            Vocation = "POLITICIAN",
            Address = new Address
            {
                Number = 1,
                Street = "High Street",
                City = "Upper Abbeywoodington"
            }
        },
        new Person
        {
            PersonId = "7363629563",
            FirstName = "Bert",
            LastName = "Gooding",
            DateOfBirth = DateTime.Parse("1941-04-07T22:11:52Z"),
            Vocation = "FLORIST",
            Address = new Address
            {
                Number = 13,
                Street = "Upper Bold Road",
                City = "Redringtonville"
            }
        },
        new Person
        {
            PersonId = "1029648329",
            FirstName = "Sophie",
            LastName = "Celements",
            DateOfBirth = DateTime.Parse("1959-07-06T17:35:45Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 5,
                Street = "Innings Close",
                City = "Basilbridge"
            }
        },
        new Person
        {
            PersonId = "7363626383",
            FirstName = "Carl",
            LastName = "Simmons",
            DateOfBirth = DateTime.Parse("1998-12-26T13:13:55Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 187,
                Street = "Hillside Road",
                City = "Kenningford"
            }
        }
    });
```

**Step 1: Add a match stage for people who are engineers.**

First, start the aggregation on the `persons` collection and
chain a `$match` stage that finds documents in which the
value of the `Vocation` field is `"ENGINEER"`:

```csharp
var results = persons.Aggregate()
    .Match(p => p.Vocation == "ENGINEER")
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `DateOfBirth` field to
list the youngest people first:

```csharp
.Sort(Builders<Person>.Sort.Descending(p => p.DateOfBirth))
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit` stage to the pipeline to output
only the first three documents in the results.

```csharp
.Limit(3)
```

**Step 4: Add a projection stage to remove unneeded fields.**

Finally, add a `$project` stage. The
`$project` stage excludes unnecessary fields from the result
documents:

```csharp
.Project(Builders<Person>.Projection
    .Exclude(p => p.Address)
    .Exclude(p => p.Id)
);
```

**Step 5: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `Address`
fields.

```none
{ "PersonId" : "7363626383", "FirstName" : "Carl", "LastName" : "Simmons", "DateOfBirth" : { "$date" : "1998-12-26T13:13:55Z" }, "Vocation" : "ENGINEER" }
{ "PersonId" : "1723338115", "FirstName" : "Olive", "LastName" : "Ranieri", "DateOfBirth" : { "$date" : "1985-05-12T23:14:30Z" }, "Gender" : "FEMALE", "Vocation" : "ENGINEER" }
{ "PersonId" : "6392529400", "FirstName" : "Elise", "LastName" : "Smith", "DateOfBirth" : { "$date" : "1972-01-13T09:32:07Z" }, "Vocation" : "ENGINEER" }
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new C app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with the C Driver guide](https://www.mongodb.com/docs/languages/c/c-driver/current/get-started/).

To learn more about performing aggregations in the C Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/c/c-driver/current/aggregation/).

After you install the driver, create a file called
`agg-tutorial.c`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```c
#include <stdio.h>
#include <bson/bson.h>
#include <mongoc/mongoc.h>

int main(void)
{
    mongoc_init();

    // Replace the placeholder with your connection string.
    char *uri = "<connection string>";
    mongoc_client_t* client = mongoc_client_new(uri);

    // Get a reference to relevant collections.
    // ... mongoc_collection_t *some_coll = mongoc_client_get_collection(client, "agg_tutorials_db", "some_coll");
    // ... mongoc_collection_t *another_coll = mongoc_client_get_collection(client, "agg_tutorials_db", "another_coll");

    // Delete any existing documents in collections if needed.
    // ... {
    // ...     bson_t *filter = bson_new();
    // ...     bson_error_t error;
    // ...     if (!mongoc_collection_delete_many(some_coll, filter, NULL, NULL, &error))
    // ...     {
    // ...         fprintf(stderr, "Delete error: %s\n", error.message);
    // ...     }
    // ...     bson_destroy(filter);
    // ... }

    // Insert sample data into the collection or collections.
    // ... {
    // ...     size_t num_docs = ...;
    // ...     bson_t *docs[num_docs];
    // ... 
    // ...     docs[0] = ...;
    // ... 
    // ...     bson_error_t error;
    // ...     if (!mongoc_collection_insert_many(some_coll, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    // ...     {
    // ...         fprintf(stderr, "Insert error: %s\n", error.message);
    // ...     }
    // ... 
    // ...     for (int i = 0; i < num_docs; i++)
    // ...     {
    // ...         bson_destroy(docs[i]);
    // ...     }
    // ... }

    {
        const bson_t *doc;

        // Add code to create pipeline stages.
        bson_t *pipeline = BCON_NEW("pipeline", "[",
        // ... Add pipeline stages here.
        "]");

        // Run the aggregation.
        // ... mongoc_cursor_t *results = mongoc_collection_aggregate(some_coll, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

        bson_destroy(pipeline);

        // Print the aggregation results.
        while (mongoc_cursor_next(results, &doc))
        {
            char *str = bson_as_canonical_extended_json(doc, NULL);
            printf("%s\n", str);
            bson_free(str);
        }
        bson_error_t error;
        if (mongoc_cursor_error(results, &error))
        {
            fprintf(stderr, "Aggregation error: %s\n", error.message);
        }

        mongoc_cursor_destroy(results);
    }

    // Clean up resources.
    // ... mongoc_collection_destroy(some_coll);
    mongoc_client_destroy(client);
    mongoc_cleanup();

    return EXIT_SUCCESS;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/c/c-driver/current/get-started/#create-a-connection-string)
step of the C Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```c
char *uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```c
mongoc_collection_t *persons = mongoc_client_get_collection(client, "agg_tutorials_db", "persons");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(persons, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 6;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "person_id", "6392529400",
        "firstname", "Elise",
        "lastname", "Smith",
        "dateofbirth", BCON_DATE_TIME(653616727000UL), // 1972-01-13T09:32:07Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(5625),
        "street", "Tipa Circle",
        "city", "Wojzinmoj",
        "}");

    docs[1] = BCON_NEW(
        "person_id", "1723338115",
        "firstname", "Olive",
        "lastname", "Ranieri",
        "dateofbirth", BCON_DATE_TIME(485113500000UL), // 1985-05-12T23:14:30Z
        "gender", "FEMALE",
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(9303),
        "street", "Mele Circle",
        "city", "Tobihbo",
        "}");

    docs[2] = BCON_NEW(
        "person_id", "8732762874",
        "firstname", "Toni",
        "lastname", "Jones",
        "dateofbirth", BCON_DATE_TIME(690559710000UL), // 1991-11-23T16:53:56Z
        "vocation", "POLITICIAN",
        "address", "{",
        "number", BCON_INT32(1),
        "street", "High Street",
        "city", "Upper Abbeywoodington",
        "}");

    docs[3] = BCON_NEW(
        "person_id", "7363629563",
        "firstname", "Bert",
        "lastname", "Gooding",
        "dateofbirth", BCON_DATE_TIME(449595112000UL), // 1941-04-07T22:11:52Z
        "vocation", "FLORIST",
        "address", "{",
        "number", BCON_INT32(13),
        "street", "Upper Bold Road",
        "city", "Redringtonville",
        "}");

    docs[4] = BCON_NEW(
        "person_id", "1029648329",
        "firstname", "Sophie",
        "lastname", "Celements",
        "dateofbirth", BCON_DATE_TIME(316265745000UL), // 1959-07-06T17:35:45Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(5),
        "street", "Innings Close",
        "city", "Basilbridge",
        "}");

    docs[5] = BCON_NEW(
        "person_id", "7363626383",
        "firstname", "Carl",
        "lastname", "Simmons",
        "dateofbirth", BCON_DATE_TIME(915250045000UL), // 1998-12-26T13:13:55Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(187),
        "street", "Hillside Road",
        "city", "Kenningford",
        "}");

    bson_error_t error;
    if (!mongoc_collection_insert_many(persons, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(docs[i]);
    }
}
```

**Step 1: Add a match stage for people who are engineers.**

In your pipeline, create a `$match` stage
that finds documents in which the value of the `vocation` field
is `"ENGINEER"`:

```c
"{", "$match", "{", "vocation", BCON_UTF8("ENGINEER"), "}", "}",
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```c
"{", "$sort", "{", "dateofbirth", BCON_INT32(-1), "}", "}",
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```c
"{", "$limit", BCON_INT32(3), "}",
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("address"), "]", "}",
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(persons, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(persons);
```

Finally, run the following commands in your shell to generate and
run the executable:

```bash
gcc -o aggc agg-tutorial.c $(pkg-config --libs --cflags libmongoc-1.0)
./aggc
```

**Tip:**

If you encounter connection errors by running the preceding
commands in one call, you can run them separately.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : { "$numberLong" : "915250045000" } }, "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : { "$numberLong" : "653616727000" } }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : { "$numberLong" : "485113500000" } }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new C++ app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with C++](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/get-started/)
tutorial.

To learn more about using the C++ driver, see the [API documentation](https://mongocxx.org/api/current/).

To learn more about performing aggregations in the C++ Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/aggregation/).

After you install the driver, create a file called
`agg-tutorial.cpp`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```cpp
#include <iostream>
#include <bsoncxx/builder/basic/document.hpp>
#include <bsoncxx/builder/basic/kvp.hpp>
#include <bsoncxx/json.hpp>
#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/pipeline.hpp>
#include <mongocxx/uri.hpp>
#include <chrono>

using bsoncxx::builder::basic::kvp;
using bsoncxx::builder::basic::make_document;
using bsoncxx::builder::basic::make_array;

int main() {
   mongocxx::instance instance;

   // Replace the placeholder with your connection string.
   mongocxx::uri uri("<connection string>");
   mongocxx::client client(uri);

   auto db = client["agg_tutorials_db"];
   // Delete existing data in the database, if necessary.
   db.drop();

   // Get a reference to relevant collections.
   // ... auto some_coll = db["..."];
   // ... auto another_coll = db["..."];

   // Insert sample data into the collection or collections.
   // ... some_coll.insert_many(docs);

   // Create an empty pipelne.
   mongocxx::pipeline pipeline;

   // Add code to create pipeline stages.
   // pipeline.match(make_document(...));

   // Run the aggregation and print the results.
   auto cursor = orders.aggregate(pipeline);
   for (auto&& doc : cursor) {
      std::cout << bsoncxx::to_json(doc, bsoncxx::ExtendedJsonMode::k_relaxed) << std::endl;
   }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/get-started/#create-a-connection-string)
step of the C++ Get Started tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```cpp
mongocxx::uri uri{"mongodb+srv://mongodb-example:27017"};
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```cpp
auto persons = db["persons"];

std::vector<bsoncxx::document::value> docs = {
    bsoncxx::from_json(R"({
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": {"$date": 620947927},
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": {"$date": 485529270000},
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": {"$date": 690978836000},
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": {"$date": -88368048000},
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": {"$date": -31561935000},
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": {"$date": 915148835000},
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford"
        }
    })")
};

auto result = persons.insert_many(docs); // Might throw an exception
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "vocation": "ENGINEER"
})"));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "dateofbirth": -1
})"));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```cpp
pipeline.limit(3);
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "address"]
})"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```cpp
auto cursor = persons.aggregate(pipeline);
```

Finally, run the following commands in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : "1999-01-01T00:00:35Z" }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : "1985-05-21T13:14:30Z" }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : "1970-01-08T04:29:07.927Z" }, "vocation" : "ENGINEER" }
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Node.js app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Node.js Driver Quick Start guide`.

To learn more about performing aggregations in the Node.js Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.js`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```javascript
const { MongoClient } = require("mongodb");

// Replace the placeholder with your connection string.
const uri = "<connection string>";
const client = new MongoClient(uri);

async function run() {
  try {
    const aggDB = client.db("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... const someColl =
    // ... const anotherColl =

    // Delete any existing documents in collections.
    // ... await someColl.deleteMany({});

    // Insert sample data into the collection or collections.
    // ... const someData = [ ... ];
    // ... await someColl.insertMany(someData);

    // Create an empty pipeline array.
    const pipeline = [];

    // Add code to create pipeline stages.
    // ... pipeline.push({ ... })

    // Run the aggregation.
    // ... const aggregationResult = ...

    // Print the aggregation results.
    for await (const document of aggregationResult) {
      console.log(document);
    }
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Node.js Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```javascript
const uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```javascript
const persons = aggDB.collection("persons");
await persons.deleteMany({});

await persons.insertMany([
  {
    person_id: "6392529400",
    firstname: "Elise",
    lastname: "Smith",
    dateofbirth: new Date("1972-01-13T09:32:07Z"),
    vocation: "ENGINEER",
    address: {
      number: 5625,
      street: "Tipa Circle",
      city: "Wojzinmoj",
    },
  },
  {
    person_id: "1723338115",
    firstname: "Olive",
    lastname: "Ranieri",
    dateofbirth: new Date("1985-05-12T23:14:30Z"),
    gender: "FEMALE",
    vocation: "ENGINEER",
    address: {
      number: 9303,
      street: "Mele Circle",
      city: "Tobihbo",
    },
  },
  {
    person_id: "8732762874",
    firstname: "Toni",
    lastname: "Jones",
    dateofbirth: new Date("1991-11-23T16:53:56Z"),
    vocation: "POLITICIAN",
    address: {
      number: 1,
      street: "High Street",
      city: "Upper Abbeywoodington",
    },
  },
  {
    person_id: "7363629563",
    firstname: "Bert",
    lastname: "Gooding",
    dateofbirth: new Date("1941-04-07T22:11:52Z"),
    vocation: "FLORIST",
    address: {
      number: 13,
      street: "Upper Bold Road",
      city: "Redringtonville",
    },
  },
  {
    person_id: "1029648329",
    firstname: "Sophie",
    lastname: "Celements",
    dateofbirth: new Date("1959-07-06T17:35:45Z"),
    vocation: "ENGINEER",
    address: {
      number: 5,
      street: "Innings Close",
      city: "Basilbridge",
    },
  },
  {
    person_id: "7363626383",
    firstname: "Carl",
    lastname: "Simmons",
    dateofbirth: new Date("1998-12-26T13:13:55Z"),
    vocation: "ENGINEER",
    address: {
      number: 187,
      street: "Hillside Road",
      city: "Kenningford",
    },
  },
]);
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```javascript
pipeline.push({
  $match: {
    vocation: "ENGINEER",
  },
});
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```javascript
pipeline.push({
  $sort: {
    dateofbirth: -1,
  },
});
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```javascript
pipeline.push({
  $limit: 3,
});
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```javascript
pipeline.push({
  $unset: ["_id", "address"],
});
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```javascript
const aggregationResult = await persons.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```javascript
{
  person_id: '7363626383',
  firstname: 'Carl',
  lastname: 'Simmons',
  dateofbirth: 1998-12-26T13:13:55.000Z,
  vocation: 'ENGINEER'
}
{
  person_id: '1723338115',
  firstname: 'Olive',
  lastname: 'Ranieri',
  dateofbirth: 1985-05-12T23:14:30.000Z,
  gender: 'FEMALE',
  vocation: 'ENGINEER'
}
{
  person_id: '6392529400',
  firstname: 'Elise',
  lastname: 'Smith',
  dateofbirth: 1972-01-13T09:32:07.000Z,
  vocation: 'ENGINEER'
}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new PHP app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the PHP library and connect to MongoDB,
see the [Get Started with the PHP Library](https://www.mongodb.com/docs/php-library/current/get-started/)
tutorial.

To learn more about performing aggregations in the PHP library, see the
[Aggregation guide](https://www.mongodb.com/docs/php-library/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.php`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```php
<?php

require 'vendor/autoload.php';

// Modify imports for each tutorial as needed.
use MongoDB\Client;
use MongoDB\BSON\UTCDateTime;
use MongoDB\Builder\Pipeline;
use MongoDB\Builder\Stage;
use MongoDB\Builder\Type\Sort;
use MongoDB\Builder\Query;
use MongoDB\Builder\Expression;
use MongoDB\Builder\Accumulator;

use function MongoDB\object;

// Replace the placeholder with your connection string.
$uri = '<connection string>';
$client = new Client($uri);

// Get a reference to relevant collections.
// ... $someColl = $client->agg_tutorials_db->someColl;
// ... $anotherColl = $client->agg_tutorials_db->anotherColl;

// Delete any existing documents in collections if needed.
// ... $someColl->deleteMany([]);

// Insert sample data into the collection or collections.
// ... $someColl->insertMany(...);

// Add code to create pipeline stages within the Pipeline instance.
// ... $pipeline = new Pipeline(...);

// Run the aggregation.
// ... $cursor = $someColl->aggregate($pipeline);

// Print the aggregation results.
foreach ($cursor as $doc) {
    echo json_encode($doc, JSON_PRETTY_PRINT), PHP_EOL;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```php
$uri = 'mongodb+srv://mongodb-example:27017';
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```php
$persons = $client->agg_tutorials_db->persons;
$persons->deleteMany([]);

$persons->insertMany(
    [
        [
            'person_id' => '6392529400',
            'firstname' => 'Elise',
            'lastname' => 'Smith',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1972-01-13T09:32:07')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 5625, 'Street' => 'Tipa Circle', 'city' => 'Wojzinmoj'],
        ],
        [
            'person_id' => '1723338115',
            'firstname' => 'Olive',
            'lastname' => 'Ranieri',
            'gender' => 'FEMALE',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1985-05-12T23:14:30')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 9303, 'street' => 'Mele Circle', 'city' => 'Tobihbo'],
        ],
        [
            'person_id' => '8732762874',
            'firstname' => 'Toni',
            'lastname' => 'Jones',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1991-11-23T16:53:56')),
            'vocation' => 'POLITICIAN',
            'address' => ['number' => 1, 'street' => 'High Street', 'city' => 'Upper Abbeywoodington'],
        ],
        [
            'person_id' => '7363629563',
            'firstname' => 'Bert',
            'lastname' => 'Gooding',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1941-04-07T22:11:52')),
            'vocation' => 'FLORIST',
            'address' => ['number' => 13, 'street' => 'Upper Bold Road', 'city' => 'Redringtonville'],
        ],
        [
            'person_id' => '1029648329',
            'firstname' => 'Sophie',
            'lastname' => 'Celements',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1959-07-06T17:35:45')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 5, 'street' => 'Innings Close', 'city' => 'Basilbridge'],
        ],
        [
            'person_id' => '7363626383',
            'firstname' => 'Carl',
            'lastname' => 'Simmons',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1998-12-26T13:13:55')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 187, 'street' => 'Hillside Road', 'city' => 'Kenningford'],
        ]
    ]
);
```

**Step 1: Add a match stage for people who are engineers.**

In your `Pipeline` instance, create a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```php
Stage::match(vocation: 'ENGINEER'),
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```php
Stage::sort(dateofbirth: Sort::Desc),
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```php
Stage::limit(3),
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```php
Stage::unset('_id', 'address')
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```php
$cursor = $persons->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{
    "person_id": "7363626383",
    "firstname": "Carl",
    "lastname": "Simmons",
    "dateofbirth": {
        "$date": {
            "$numberLong": "914678035000"
        }
    },
    "vocation": "ENGINEER"
}
{
    "person_id": "1723338115",
    "firstname": "Olive",
    "lastname": "Ranieri",
    "gender": "FEMALE",
    "dateofbirth": {
        "$date": {
            "$numberLong": "484787670000"
        }
    },
    "vocation": "ENGINEER"
}
{
    "person_id": "6392529400",
    "firstname": "Elise",
    "lastname": "Smith",
    "dateofbirth": {
        "$date": {
            "$numberLong": "64143127000"
        }
    },
    "vocation": "ENGINEER"
}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Ruby app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the Ruby Driver and connect to MongoDB,
see the [Get Started with the Ruby Driver guide](https://www.mongodb.com/docs/ruby-driver/upcoming/get-started/).

To learn more about performing aggregations in the Ruby Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/ruby-driver/upcoming/aggregation/).

After you install the driver, create a file called
`agg_tutorial.rb`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```ruby
# typed: strict
require 'mongo'
require 'bson'

# Replace the placeholder with your connection string.
uri = "<connection string>"

Mongo::Client.new(uri) do |client|

  agg_db = client.use('agg_tutorials_db')

  # Get a reference to relevant collections.
  # ... some_coll = agg_db[:some_coll]

  # Delete any existing documents in collections if needed.
  # ... some_coll.delete_many({})

  # Insert sample data into the collection or collections.
  # ... some_coll.insert_many( ... )

  # Add code to create pipeline stages within the array.
  # ... pipeline = [ ... ]

  # Run the aggregation.
  # ... aggregation_result = some_coll.aggregate(pipeline)

  # Print the aggregation results.
  aggregation_result.each do |doc|
    puts doc
  end

end
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/ruby-driver/upcoming/get-started/create-a-connection-string/)
step of the Ruby Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```ruby
uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```ruby
persons = agg_db[:persons]
persons.delete_many({})

persons.insert_many(
  [
    {
      person_id: "6392529400",
      firstname: "Elise",
      lastname: "Smith",
      dateofbirth: DateTime.parse("1972-01-13T09:32:07Z"),
      vocation: "ENGINEER",
      address: {
        number: 5625,
        street: "Tipa Circle",
        city: "Wojzinmoj",
      },
    },
    {
      person_id: "1723338115",
      firstname: "Olive",
      lastname: "Ranieri",
      dateofbirth: DateTime.parse("1985-05-12T23:14:30Z"),
      gender: "FEMALE",
      vocation: "ENGINEER",
      address: {
        number: 9303,
        street: "Mele Circle",
        city: "Tobihbo",
      },
    },
    {
      person_id: "8732762874",
      firstname: "Toni",
      lastname: "Jones",
      dateofbirth: DateTime.parse("1991-11-23T16:53:56Z"),
      vocation: "POLITICIAN",
      address: {
        number: 1,
        street: "High Street",
        city: "Upper Abbeywoodington",
      },
    },
    {
      person_id: "7363629563",
      firstname: "Bert",
      lastname: "Gooding",
      dateofbirth: DateTime.parse("1941-04-07T22:11:52Z"),
      vocation: "FLORIST",
      address: {
        number: 13,
        street: "Upper Bold Road",
        city: "Redringtonville",
      },
    },
    {
      person_id: "1029648329",
      firstname: "Sophie",
      lastname: "Celements",
      dateofbirth: DateTime.parse("1959-07-06T17:35:45Z"),
      vocation: "ENGINEER",
      address: {
        number: 5,
        street: "Innings Close",
        city: "Basilbridge",
      },
    },
    {
      person_id: "7363626383",
      firstname: "Carl",
      lastname: "Simmons",
      dateofbirth: DateTime.parse("1998-12-26T13:13:55Z"),
      vocation: "ENGINEER",
      address: {
        number: 187,
        street: "Hillside Road",
        city: "Kenningford",
      },
    },
  ]
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```ruby
{ "$match": { "vocation": "ENGINEER" } },
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```ruby
{ "$sort": { "dateofbirth": -1 } },
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```ruby
{ "$limit": 3 },
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```ruby
{ "$unset": ["_id", "address"] },
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```ruby
aggregation_result = persons.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.rb
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id"=>"7363626383", "firstname"=>"Carl", "lastname"=>"Simmons", "dateofbirth"=>1998-12-26 13:13:55 UTC, "vocation"=>"ENGINEER"}
{"person_id"=>"1723338115", "firstname"=>"Olive", "lastname"=>"Ranieri", "dateofbirth"=>1985-05-12 23:14:30 UTC, "gender"=>"FEMALE", "vocation"=>"ENGINEER"}
{"person_id"=>"6392529400", "firstname"=>"Elise", "lastname"=>"Smith", "dateofbirth"=>1972-01-13 09:32:07 UTC, "vocation"=>"ENGINEER"}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Go app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Go Driver Quick Start guide`.

To learn more about performing aggregations in the Go Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.go`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "go.mongodb.org/mongo-driver/v2/bson"
    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

// Define structs.
// type MyStruct struct { ... }

func main() {
    // Replace the placeholder with your connection string.
    const uri = "<connection string>"

    client, err := mongo.Connect(options.Client().ApplyURI(uri))
    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err = client.Disconnect(context.TODO()); err != nil {
            log.Fatal(err)
        }
    }()

    aggDB := client.Database("agg_tutorials_db")

    // Get a reference to relevant collections.
    // ... someColl := aggDB.Collection("...")
    // ... anotherColl := aggDB.Collection("...")

    // Delete any existing documents in collections if needed.
    // ... someColl.DeleteMany(context.TODO(), bson.D{})

    // Insert sample data into the collection or collections.   
    // ... _, err = someColl.InsertMany(...)

    // Add code to create pipeline stages.
    // ... myStage := bson.D{{...}}

    // Create a pipeline that includes the stages.
    // ... pipeline := mongo.Pipeline{...}

    // Run the aggregation.
    // ... cursor, err := someColl.Aggregate(context.TODO(), pipeline)

    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err := cursor.Close(context.TODO()); err != nil {
            log.Fatalf("failed to close cursor: %v", err)
        }
    }()

    // Decode the aggregation results.
    var results []bson.D
    if err = cursor.All(context.TODO(), &results); err != nil {
        log.Fatalf("failed to decode results: %v", err)
    }

    // Print the aggregation results.
    for _, result := range results {
        res, _ := bson.MarshalExtJSON(result, false, false)
        fmt.Println(string(res))
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a MongoDB Cluster`
step of the Go Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```go
const uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Go structs to model the data in the `persons`
collection:

```go
type Person struct {
	PersonID    string        `bson:"person_id"`
	Firstname   string        `bson:"firstname"`
	Lastname    string        `bson:"lastname"`
	Gender      string        `bson:"gender,omitempty"`
	DateOfBirth bson.DateTime `bson:"dateofbirth"`
	Vocation    string        `bson:"vocation"`
	Address     Address       `bson:"address"`
}

type Address struct {
	Number int
	Street string
	City   string
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```go
persons := aggDB.Collection("persons")
persons.DeleteMany(context.TODO(), bson.D{})

_, err = persons.InsertMany(context.TODO(), []interface{}{
	Person{
		PersonID:    "6392529400",
		Firstname:   "Elise",
		Lastname:    "Smith",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1972, 1, 13, 9, 32, 7, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 5625, Street: "Tipa Circle", City: "Wojzinmoj"},
	},
	Person{
		PersonID:    "1723338115",
		Firstname:   "Olive",
		Lastname:    "Ranieri",
		Gender:      "FEMALE",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1985, 5, 12, 23, 14, 30, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 9303, Street: "Mele Circle", City: "Tobihbo"},
	},
	Person{
		PersonID:    "8732762874",
		Firstname:   "Toni",
		Lastname:    "Jones",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1991, 11, 23, 16, 53, 56, 0, time.UTC)),
		Vocation:    "POLITICIAN",
		Address:     Address{Number: 1, Street: "High Street", City: "Upper Abbeywoodington"},
	},
	Person{
		PersonID:    "7363629563",
		Firstname:   "Bert",
		Lastname:    "Gooding",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1941, 4, 7, 22, 11, 52, 0, time.UTC)),
		Vocation:    "FLORIST",
		Address:     Address{Number: 13, Street: "Upper Bold Road", City: "Redringtonville"},
	},
	Person{
		PersonID:    "1029648329",
		Firstname:   "Sophie",
		Lastname:    "Celements",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1959, 7, 6, 17, 35, 45, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 5, Street: "Innings Close", City: "Basilbridge"},
	},
	Person{
		PersonID:    "7363626383",
		Firstname:   "Carl",
		Lastname:    "Simmons",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1998, 12, 26, 13, 13, 55, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 187, Street: "Hillside Road", City: "Kenningford"},
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{{Key: "vocation", Value: "ENGINEER"}}}}
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```go
sortStage := bson.D{{Key: "$sort", Value: bson.D{{Key: "dateofbirth", Value: -1}}}}
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```go
limitStage := bson.D{{Key: "$limit", Value: 3}}
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id", "address"}}}
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```go
pipeline := mongo.Pipeline{matchStage, sortStage, limitStage, unsetStage}
cursor, err := persons.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id":"7363626383","firstname":"Carl","lastname":"Simmons","dateofbirth":{"$date":"1998-12-26T13:13:55Z"},"vocation":"ENGINEER"}
{"person_id":"1723338115","firstname":"Olive","lastname":"Ranieri","gender":"FEMALE","dateofbirth":{"$date":"1985-05-12T23:14:30Z"},"vocation":"ENGINEER"}
{"person_id":"6392529400","firstname":"Elise","lastname":"Smith","dateofbirth":{"$date":"1972-01-13T09:32:07Z"},"vocation":"ENGINEER"}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Rust app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Rust Driver Quick Start guide`.

To learn more about performing aggregations in the Rust Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg-tutorial.rs`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```rust
use mongodb::{
    bson::{doc, Document},
    options::ClientOptions,
    Client,
};
use futures::stream::TryStreamExt;
use std::error::Error;

// Define structs.
// #[derive(Debug, Serialize, Deserialize)]
// struct MyStruct { ... }

#[tokio::main]
async fn main() mongodb::error::Result<()> {
    // Replace the placeholder with your connection string.
    let uri = "<connection string>";
    let client = Client::with_uri_str(uri).await?;

    let agg_db = client.database("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... let some_coll: Collection<T> = agg_db.collection("...");
    // ... let another_coll: Collection<T> = agg_db.collection("...");

    // Delete any existing documents in collections if needed.
    // ... some_coll.delete_many(doc! {}).await?;

    // Insert sample data into the collection or collections.
    // ... some_coll.insert_many(vec![...]).await?;

    // Create an empty pipeline.
    let mut pipeline = Vec::new();

    // Add code to create pipeline stages.
    // pipeline.push(doc! { ... });

    // Run the aggregation and print the results.
    let mut results = some_coll.aggregate(pipeline).await?;
    while let Some(result) = results.try_next().await? {
       println!("{:?}\n", result);
    }
    Ok(())
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Rust Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```rust
let uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Rust structs to model the data in the `persons`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Address {
    number: i32,
    street: String,
    city: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Person {
    person_id: String,
    firstname: String,
    lastname: String,
    dateofbirth: DateTime,
    vocation: String,
    address: Address,
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```rust
let persons: Collection<Person> = agg_db.collection("persons");
persons.delete_many(doc! {}).await?;

let data = vec![
    Person {
        person_id: "6392529400".to_string(),
        firstname: "Elise".to_string(),
        lastname: "Smith".to_string(),
        dateofbirth: DateTime::builder().year(1972).month(1).day(13).hour(9).minute(32).second(7).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 5625,
            street: "Tipa Circle".to_string(),
            city: "Wojzinmoj".to_string(),
        },
    },
    Person {
        person_id: "1723338115".to_string(),
        firstname: "Olive".to_string(),
        lastname: "Ranieri".to_string(),
        gender: "FEMALE".to_string(),
        dateofbirth: DateTime::builder().year(1985).month(5).day(12).hour(23).minute(14).second(30).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 9303,
            street: "Mele Circle".to_string(),
            city: "Tobihbo".to_string(),
        },
    },
    Person {
        person_id: "8732762874".to_string(),
        firstname: "Toni".to_string(),
        lastname: "Jones".to_string(),
        dateofbirth: DateTime::builder().year(1991).month(11).day(23).hour(16).minute(53).second(56).build().unwrap(),
        vocation: "POLITICIAN".to_string(),
        address: Address {
            number: 1,
            street: "High Street".to_string(),
            city: "Upper Abbeywoodington".to_string(),
        },
    },
    Person {
        person_id: "7363629563".to_string(),
        firstname: "Bert".to_string(),
        lastname: "Gooding".to_string(),
        dateofbirth: DateTime::builder().year(1941).month(4).day(7).hour(22).minute(11).second(52).build().unwrap(),
        vocation: "FLORIST".to_string(),
        address: Address {
            number: 13,
            street: "Upper Bold Road".to_string(),
            city: "Redringtonville".to_string(),
        },
    },
    Person {
        person_id: "1029648329".to_string(),
        firstname: "Sophie".to_string(),
        lastname: "Celements".to_string(),
        dateofbirth: DateTime::builder().year(1959).month(7).day(6).hour(17).minute(35).second(45).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 5,
            street: "Innings Close".to_string(),
            city: "Basilbridge".to_string(),
        },
    },
    Person {
        person_id: "7363626383".to_string(),
        firstname: "Carl".to_string(),
        lastname: "Simmons".to_string(),
        dateofbirth: DateTime::builder().year(1998).month(12).day(26).hour(13).minute(13).second(55).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 187,
            street: "Hillside Road".to_string(),
            city: "Kenningford".to_string(),
        },
    },
];

persons.insert_many(data).await?;
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```rust
pipeline.push(doc! { "$match": { "vocation": "ENGINEER" } });
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```rust
pipeline.push(doc! { "$sort": { "dateofbirth": -1 } });
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```rust
pipeline.push(doc! { "$limit": 3 });
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```rust
pipeline.push(doc! { "$unset": ["_id", "address"] });
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```rust
let mut cursor = persons.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
Document({"person_id": String("7363626383"), "firstname": String("Carl"), "lastname": String("Simmons"), "dateofbirth": DateTime(1998-12-26 13:13:55.0 +00:00:00), "vocation": String("ENGINEER")})

Document({"person_id": String("1723338115"), "firstname": String("Olive"), "lastname": String("Ranieri"), "gender": String("FEMALE"), "dateofbirth": DateTime(1985-05-12 23:14:30.0 +00:00:00), "vocation": String("ENGINEER")})

Document({"person_id": String("6392529400"), "firstname": String("Elise"), "lastname": String("Smith"), "dateofbirth": DateTime(1972-01-13 9:32:07.0 +00:00:00), "vocation": String("ENGINEER")})
```

## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to filter for a specific subset of documents.

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The aggregation selects documents based on whether their field values
match specified criteria.

**Step 1: Run the aggregation pipeline.**

```javascript
db.movies.aggregate( [
   // Stage 1: Match documents with the Drama genre
   { $match: { genres: "Drama" } },

   // Stage 2: Sort documents from oldest to newest
   { $sort: { year: 1 } },

   // Stage 3: Limit the results to 3 documents
   { $limit: 3 },

   // Stage 4: Project only the fields needed for the result
   { $project: { _id: 0, title: 1, year: 1, directors: 1, runtime: 1 } }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregated results contain three documents. The documents
represent the three oldest movies in the `Drama` genre,
ordered from oldest to newest. The results include only the
`title`, `year`, `directors`, and `runtime` fields.

```javascript
[
  {
    runtime: 14,
    title: 'A Corner in Wheat',
    directors: [
      'D.W. Griffith'
    ],
    year: 1909
  },
  {
    runtime: 88,
    title: 'Traffic in Souls',
    directors: [
      'George Loane Tucker'
    ],
    year: 1913
  },
  {
    runtime: 65,
    title: 'In the Land of the Head Hunters',
    directors: [
      'Edward S. Curtis'
    ],
    year: 1914
  }
]
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Python app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install PyMongo and connect to MongoDB,
see the [Get Started with PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
tutorial.

To learn more about performing aggregations in PyMongo, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.py`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```python
# Modify imports for each tutorial as needed.
from pymongo import MongoClient

# Replace the placeholder with your connection string.
uri = "<connection string>"
client = MongoClient(uri)

try:
    agg_db = client["agg_tutorials_db"]

    # Get a reference to relevant collections.
    # ... some_coll = agg_db["some_coll"]
    # ... another_coll = agg_db["another_coll"]

    # Delete any existing documents in collections if needed.
    # ... some_coll.delete_many({})

    # Insert sample data into the collection or collections.
    # ... some_coll.insert_many(...)

    # Create an empty pipeline array.
    pipeline = []

    # Add code to create pipeline stages.
    # ... pipeline.append({...})

    # Run the aggregation.
    # ... aggregation_result = ...

    # Print the aggregation results.
    for document in aggregation_result:
        print(document)

finally:
    client.close()
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```php
uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```python
person_coll = agg_db["persons"]
person_coll.delete_many({})

person_data = [
    {
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": datetime(1972, 1, 13, 9, 32, 7),
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj",
        },
    },
    {
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": datetime(1985, 5, 12, 23, 14, 30),
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo",
        },
    },
    {
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": datetime(1991, 11, 23, 16, 53, 56),
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington",
        },
    },
    {
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": datetime(1941, 4, 7, 22, 11, 52),
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville",
        },
    },
    {
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": datetime(1959, 7, 6, 17, 35, 45),
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge",
        },
    },
    {
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": datetime(1998, 12, 26, 13, 13, 55),
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford",
        },
    },
]

person_coll.insert_many(person_data)
```

**Step 1: Add a match stage for people who are engineers.**

In your `Pipeline` instance, create a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```python
pipeline.append({"$match": {"vocation": "ENGINEER"}})
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```python
pipeline.append({"$sort": {"dateofbirth": -1}})
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```python
pipeline.append({"$limit": 3})
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```python
pipeline.append({"$unset": ["_id", "address"]})
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```python
aggregation_result = person_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{'person_id': '7363626383', 'firstname': 'Carl', 'lastname': 'Simmons', 'dateofbirth': datetime.datetime(1998, 12, 26, 13, 13, 55), 'vocation': 'ENGINEER'}
{'person_id': '1723338115', 'firstname': 'Olive', 'lastname': 'Ranieri', 'dateofbirth': datetime.datetime(1985, 5, 12, 23, 14, 30), 'gender': 'FEMALE', 'vocation': 'ENGINEER'}
{'person_id': '6392529400', 'firstname': 'Elise', 'lastname': 'Smith', 'dateofbirth': datetime.datetime(1972, 1, 13, 9, 32, 7), 'vocation': 'ENGINEER'}
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Java app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Get Started with the Java Driver guide`.

To learn more about performing aggregations in the Java Sync Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`AggTutorial.java`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```java
package org.example;

// Modify imports for each tutorial as needed.
import com.mongodb.client.*;
import com.mongodb.client.model.Aggregates;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Sorts;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AggTutorial {
    public static void main( String[] args ) {

        // Replace the placeholder with your connection string.
        String uri = "<connection string>";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            MongoDatabase aggDB = mongoClient.getDatabase("agg_tutorials_db");

            // Get a reference to relevant collections.
            // ... MongoCollection<Document> someColl = ...
            // ... MongoCollection<Document> anotherColl = ...

            // Delete any existing documents in collections if needed.
            // ... someColl.deleteMany(Filters.empty());

            // Insert sample data into the collection or collections.   
            // ... someColl.insertMany(...);

            // Create an empty pipeline array.
            List<Bson> pipeline = new ArrayList<>();

            // Add code to create pipeline stages.
            // ... pipeline.add(...);

            // Run the aggregation.
            // ... AggregateIterable<Document> aggregationResult = someColl.aggregate(pipeline);

            // Print the aggregation results.
            for (Document document : aggregationResult) {
                System.out.println(document.toJson());
            }
        }
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Java Sync Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```java
String uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```java
MongoCollection<Document> persons = aggDB.getCollection("persons");
persons.deleteMany(Filters.empty());

persons.insertMany(
        Arrays.asList(
                new Document("person_id", "6392529400")
                        .append("firstname", "Elise")
                        .append("lastname", "Smith")
                        .append("dateofbirth", LocalDateTime.parse("1972-01-13T09:32:07"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 5625)
                                .append("street", "Tipa Circle")
                                .append("city", "Wojzinmoj")),
                new Document("person_id", "1723338115")
                        .append("firstname", "Olive")
                        .append("lastname", "Ranieri")
                        .append("dateofbirth", LocalDateTime.parse("1985-05-12T23:14:30"))
                        .append("gender", "FEMALE")
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 9303)
                                .append("street", "Mele Circle")
                                .append("city", "Tobihbo")),
                new Document("person_id", "8732762874")
                        .append("firstname", "Toni")
                        .append("lastname", "Jones")
                        .append("dateofbirth", LocalDateTime.parse("1991-11-23T16:53:56"))
                        .append("vocation", "POLITICIAN")
                        .append("address", new Document("number", 1)
                                .append("street", "High Street")
                                .append("city", "Upper Abbeywoodington")),
                new Document("person_id", "7363629563")
                        .append("firstname", "Bert")
                        .append("lastname", "Gooding")
                        .append("dateofbirth", LocalDateTime.parse("1941-04-07T22:11:52"))
                        .append("vocation", "FLORIST")
                        .append("address", new Document("number", 13)
                                .append("street", "Upper Bold Road")
                                .append("city", "Redringtonville")),
                new Document("person_id", "1029648329")
                        .append("firstname", "Sophie")
                        .append("lastname", "Celements")
                        .append("dateofbirth", LocalDateTime.parse("1959-07-06T17:35:45"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 5)
                                .append("street", "Innings Close")
                                .append("city", "Basilbridge")),
                new Document("person_id", "7363626383")
                        .append("firstname", "Carl")
                        .append("lastname", "Simmons")
                        .append("dateofbirth", LocalDateTime.parse("1998-12-26T13:13:55"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 187)
                                .append("street", "Hillside Road")
                                .append("city", "Kenningford"))
        )
);
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```java
pipeline.add(Aggregates.match(Filters.eq("vocation", "ENGINEER")));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```java
pipeline.add(Aggregates.sort(Sorts.descending("dateofbirth")));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```java
pipeline.add(Aggregates.limit(3));
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```java
pipeline.add(Aggregates.unset("_id", "address"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```java
AggregateIterable<Document> aggregationResult = persons.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id": "7363626383", "firstname": "Carl", "lastname": "Simmons", "dateofbirth": {"$date": "1998-12-26T13:13:55Z"}, "vocation": "ENGINEER"}
{"person_id": "1723338115", "firstname": "Olive", "lastname": "Ranieri", "dateofbirth": {"$date": "1985-05-12T23:14:30Z"}, "gender": "FEMALE", "vocation": "ENGINEER"}
{"person_id": "6392529400", "firstname": "Elise", "lastname": "Smith", "dateofbirth": {"$date": "1972-01-13T09:32:07Z"}, "vocation": "ENGINEER"}
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Kotlin app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Kotlin Driver Quick Start guide`.

To learn more about performing aggregations in the Kotlin Driver, see the
`Aggregation guide`.

In addition to the driver, you must also add the following dependencies
to your `build.gradle.kts` file and reload your project:

```kotlin
dependencies {
    // Implements Kotlin serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-core:1.5.1")
    // Implements Kotlin date and time handling
    implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.6.1")
}
```

After you install the driver, create a file called
`AggTutorial.kt`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```kotlin
package org.example

// Modify imports for each tutorial as needed.
import com.mongodb.client.model.*
import com.mongodb.kotlin.client.coroutine.MongoClient
import kotlinx.coroutines.runBlocking
import kotlinx.datetime.LocalDateTime
import kotlinx.datetime.toJavaLocalDateTime
import kotlinx.serialization.Contextual
import kotlinx.serialization.Serializable
import org.bson.Document
import org.bson.conversions.Bson

// Define data classes.
@Serializable
data class MyClass(
    ...
)

suspend fun main() {
    // Replace the placeholder with your connection string.
    val uri = "<connection string>"

    MongoClient.create(uri).use { mongoClient ->
        val aggDB = mongoClient.getDatabase("agg_tutorials_db")

        // Get a reference to relevant collections.
        // ... val someColl = ...

        // Delete any existing documents in collections if needed.
        // ... someColl.deleteMany(empty())

        // Insert sample data into the collection or collections.
        // ... someColl.insertMany( ... )

        // Create an empty pipeline.
        val pipeline = mutableListOf<Bson>()

        // Add code to create pipeline stages.
        // ... pipeline.add(...)

        // Run the aggregation.
        // ... val aggregationResult = someColl.aggregate<Document>(pipeline)

        // Print the aggregation results.
        aggregationResult.collect { println(it) }
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Connect to your Cluster`
step of the Kotlin Driver Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```java
val uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Kotlin data classes to model the data in the `persons`
collection:

```kotlin
@Serializable
data class Address(
    val number: Int,
    val street: String,
    val city: String
)

@Serializable
data class Person(
    val personID: String,
    val firstname: String,
    val lastname: String,
    @Contextual val dateOfBirth: LocalDateTime,
    val vocation: String,
    val address: Address,
    val gender: String? = null
)
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```kotlin
val persons = aggDB.getCollection<Person>("persons")
persons.deleteMany(Filters.empty())

persons.insertMany(
    listOf(
        Person(
            "6392529400",
            "Elise",
            "Smith",
            LocalDateTime.parse("1972-01-13T09:32:07"),
            "ENGINEER",
            Address(5625, "Tipa Circle", "Wojzinmoj")
        ),
        Person(
            "1723338115",
            "Olive",
            "Ranieri",
            LocalDateTime.parse("1985-05-12T23:14:30"),
            "ENGINEER",
            Address(9303, "Mele Circle", "Tobihbo"),
            "FEMALE"
        ),
        Person(
            "8732762874",
            "Toni",
            "Jones",
            LocalDateTime.parse("1991-11-23T16:53:56"),
            "POLITICIAN",
            Address(1, "High Street", "Upper Abbeywoodington")
        ),
        Person(
            "7363629563",
            "Bert",
            "Gooding",
            LocalDateTime.parse("1941-04-07T22:11:52"),
            "FLORIST",
            Address(13, "Upper Bold Road", "Redringtonville")
        ),
        Person(
            "1029648329",
            "Sophie",
            "Celements",
            LocalDateTime.parse("1959-07-06T17:35:45"),
            "ENGINEER",
            Address(5, "Innings Close", "Basilbridge")
        ),
        Person(
            "7363626383",
            "Carl",
            "Simmons",
            LocalDateTime.parse("1998-12-26T13:13:55"),
            "ENGINEER",
            Address(187, "Hillside Road", "Kenningford")
        )
    )
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```kotlin
pipeline.add(Aggregates.match(Filters.eq(Person::vocation.name, "ENGINEER")))
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateOfBirth` field to
list the youngest people first:

```kotlin
pipeline.add(Aggregates.sort(Sorts.descending(Person::dateOfBirth.name)))
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```kotlin
pipeline.add(Aggregates.limit(3))
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```kotlin
pipeline.add(Aggregates.unset("_id", Person::address.name))
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```kotlin
val aggregationResult = persons.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
Document{{personID=7363626383, firstname=Carl, lastname=Simmons, dateOfBirth=Sat Dec 26 08:13:55 EST 1998, vocation=ENGINEER}}
Document{{personID=1723338115, firstname=Olive, lastname=Ranieri, dateOfBirth=Sun May 12 19:14:30 EDT 1985, vocation=ENGINEER, gender=FEMALE}}
Document{{personID=6392529400, firstname=Elise, lastname=Smith, dateOfBirth=Thu Jan 13 04:32:07 EST 1972, vocation=ENGINEER}}
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Scala app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with the Scala Driver](https://www.mongodb.com/docs/languages/scala/scala-driver/current/get-started/)
guide.

To learn more about performing aggregations in the Scala Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/scala/scala-driver/current/aggregation/).

After you install the driver, create a file called
`AggTutorial.scala`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```scala
package org.example;

// Modify imports for each tutorial as needed.
import org.mongodb.scala.MongoClient
import org.mongodb.scala.bson.Document
import org.mongodb.scala.model.{Accumulators, Aggregates, Field, Filters, Variable}

import java.text.SimpleDateFormat

object FilteredSubset {

  def main(args: Array[String]): Unit = {

    // Replace the placeholder with your connection string.
    val uri = "<connection string>"
    val mongoClient = MongoClient(uri)
    Thread.sleep(1000)

    val aggDB = mongoClient.getDatabase("agg_tutorials_db")

    // Get a reference to relevant collections.
    // ... val someColl = aggDB.getCollection("someColl")
    // ... val anotherColl = aggDB.getCollection("anotherColl")

    // Delete any existing documents in collections if needed.
    // ... someColl.deleteMany(Filters.empty()).subscribe(...)

    // If needed, create the date format template.
    val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

    // Insert sample data into the collection or collections.
    // ... someColl.insertMany(...).subscribe(...)

    Thread.sleep(1000)

    // Add code to create pipeline stages within the Seq.
    // ... val pipeline = Seq(...)

    // Run the aggregation and print the results.
    // ... someColl.aggregate(pipeline).subscribe(...)

    Thread.sleep(1000)
    mongoClient.close()
  }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/scala/scala-driver/current/get-started/#create-a-connection-string)
step of the Scala Driver Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string
assignment resembles the following:

```scala
val uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```scala
val persons = aggDB.getCollection("persons")

persons.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

persons.insertMany(Seq(
  Document(
    "person_id" -> "6392529400",
    "firstname" -> "Elise",
    "lastname" -> "Smith",
    "dateofbirth" -> dateFormat.parse("1972-01-13T09:32:07"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 5625,
      "street" -> "Tipa Circle",
      "city" -> "Wojzinmoj"
    )
  ),
  Document(
    "person_id" -> "1723338115",
    "firstname" -> "Olive",
    "lastname" -> "Ranieri",
    "dateofbirth" -> dateFormat.parse("1985-05-12T23:14:30"),
    "gender" -> "FEMALE",
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 9303,
      "street" -> "Mele Circle",
      "city" -> "Tobihbo"
    )
  ),
  Document(
    "person_id" -> "8732762874",
    "firstname" -> "Toni",
    "lastname" -> "Jones",
    "dateofbirth" -> dateFormat.parse("1991-11-23T16:53:56"),
    "vocation" -> "POLITICIAN",
    "address" -> Document(
      "number" -> 1,
      "street" -> "High Street",
      "city" -> "Upper Abbeywoodington"
    )
  ),
  Document(
    "person_id" -> "7363629563",
    "firstname" -> "Bert",
    "lastname" -> "Gooding",
    "dateofbirth" -> dateFormat.parse("1941-04-07T22:11:52"),
    "vocation" -> "FLORIST",
    "address" -> Document(
      "number" -> 13,
      "street" -> "Upper Bold Road",
      "city" -> "Redringtonville"
    )
  ),
  Document(
    "person_id" -> "1029648329",
    "firstname" -> "Sophie",
    "lastname" -> "Celements",
    "dateofbirth" -> dateFormat.parse("1959-07-06T17:35:45"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 5,
      "street" -> "Innings Close",
      "city" -> "Basilbridge"
    )
  ),
  Document(
    "person_id" -> "7363626383",
    "firstname" -> "Carl",
    "lastname" -> "Simmons",
    "dateofbirth" -> dateFormat.parse("1998-12-26T13:13:55"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 187,
      "street" -> "Hillside Road",
      "city" -> "Kenningford"
    )
  )
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```scala
Aggregates.filter(Filters.equal("vocation", "ENGINEER")),
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```scala
Aggregates.sort(Sorts.descending("dateofbirth")),
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```scala
Aggregates.limit(3),
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```scala
Aggregates.unset("_id", "address")
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```scala
persons.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id": "7363626383", "firstname": "Carl", "lastname": "Simmons", "dateofbirth": {"$date": "1998-12-26T18:13:55Z"}, "vocation": "ENGINEER"}
{"person_id": "1723338115", "firstname": "Olive", "lastname": "Ranieri", "dateofbirth": {"$date": "1985-05-13T03:14:30Z"}, "gender": "FEMALE", "vocation": "ENGINEER"}
{"person_id": "6392529400", "firstname": "Elise", "lastname": "Smith", "dateofbirth": {"$date": "1972-01-13T14:32:07Z"}, "vocation": "ENGINEER"}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new C#/.NET app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `C#/.NET Driver Quick Start guide`.

To learn more about performing aggregations in the C#/.NET Driver, see the
`Aggregation guide`.

After you install the driver, paste the following code into your
`Program.cs` file to create an app template for the aggregation
tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```csharp
using MongoDB.Driver;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

// Define data model classes.
// ... public class MyClass { ... }

// Replace the placeholder with your connection string.
var uri = "<connection string>";
var client = new MongoClient(uri);
var aggDB = client.GetDatabase("agg_tutorials_db");

// Get a reference to relevant collections.
// ... var someColl = aggDB.GetCollection<MyClass>("someColl");
// ... var anotherColl = aggDB.GetCollection<MyClass>("anotherColl");

// Delete any existing documents in collections if needed.
// ... someColl.DeleteMany(Builders<MyClass>.Filter.Empty);

// Insert sample data into the collection or collections.
// ... someColl.InsertMany(new List<MyClass> { ... });

// Add code to chain pipeline stages to the Aggregate() method.
// ... var results = someColl.Aggregate().Match(...);

// Print the aggregation results.
foreach (var result in results.ToList())
{
  Console.WriteLine(result);
}
```

For every tutorial, you must replace the connection string placeholder
with your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Set Up a Free Cluster in Atlas`
step of the C# Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```csharp
var uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create C# classes to model the data in the `persons`
collection:

```csharp
public class Person
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string PersonId { get; set; }
  public string FirstName { get; set; }
  public string LastName { get; set; }
  public DateTime DateOfBirth { get; set; }
  [BsonIgnoreIfNull]
  public string? Gender { get; set; }
  public string Vocation { get; set; }
  public Address Address { get; set; }
}

public class Address
{
  public int Number { get; set; }
  public string Street { get; set; }
  public string City { get; set; }
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```csharp
var persons = aggDB.GetCollection<Person>("persons");
persons.DeleteMany(Builders<Person>.Filter.Empty);

persons.InsertMany(new List<Person>
    {
        new Person
        {
            PersonId = "6392529400",
            FirstName = "Elise",
            LastName = "Smith",
            DateOfBirth = DateTime.Parse("1972-01-13T09:32:07Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 5625,
                Street = "Tipa Circle",
                City = "Wojzinmoj"
            }
        },
        new Person
        {
            PersonId = "1723338115",
            FirstName = "Olive",
            LastName = "Ranieri",
            DateOfBirth = DateTime.Parse("1985-05-12T23:14:30Z"),
            Gender = "FEMALE",
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 9303,
                Street = "Mele Circle",
                City = "Tobihbo"
            }
        },
        new Person
        {
            PersonId = "8732762874",
            FirstName = "Toni",
            LastName = "Jones",
            DateOfBirth = DateTime.Parse("1991-11-23T16:53:56Z"),
            Vocation = "POLITICIAN",
            Address = new Address
            {
                Number = 1,
                Street = "High Street",
                City = "Upper Abbeywoodington"
            }
        },
        new Person
        {
            PersonId = "7363629563",
            FirstName = "Bert",
            LastName = "Gooding",
            DateOfBirth = DateTime.Parse("1941-04-07T22:11:52Z"),
            Vocation = "FLORIST",
            Address = new Address
            {
                Number = 13,
                Street = "Upper Bold Road",
                City = "Redringtonville"
            }
        },
        new Person
        {
            PersonId = "1029648329",
            FirstName = "Sophie",
            LastName = "Celements",
            DateOfBirth = DateTime.Parse("1959-07-06T17:35:45Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 5,
                Street = "Innings Close",
                City = "Basilbridge"
            }
        },
        new Person
        {
            PersonId = "7363626383",
            FirstName = "Carl",
            LastName = "Simmons",
            DateOfBirth = DateTime.Parse("1998-12-26T13:13:55Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 187,
                Street = "Hillside Road",
                City = "Kenningford"
            }
        }
    });
```

**Step 1: Add a match stage for people who are engineers.**

First, start the aggregation on the `persons` collection and
chain a `$match` stage that finds documents in which the
value of the `Vocation` field is `"ENGINEER"`:

```csharp
var results = persons.Aggregate()
    .Match(p => p.Vocation == "ENGINEER")
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `DateOfBirth` field to
list the youngest people first:

```csharp
.Sort(Builders<Person>.Sort.Descending(p => p.DateOfBirth))
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit` stage to the pipeline to output
only the first three documents in the results.

```csharp
.Limit(3)
```

**Step 4: Add a projection stage to remove unneeded fields.**

Finally, add a `$project` stage. The
`$project` stage excludes unnecessary fields from the result
documents:

```csharp
.Project(Builders<Person>.Projection
    .Exclude(p => p.Address)
    .Exclude(p => p.Id)
);
```

**Step 5: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `Address`
fields.

```none
{ "PersonId" : "7363626383", "FirstName" : "Carl", "LastName" : "Simmons", "DateOfBirth" : { "$date" : "1998-12-26T13:13:55Z" }, "Vocation" : "ENGINEER" }
{ "PersonId" : "1723338115", "FirstName" : "Olive", "LastName" : "Ranieri", "DateOfBirth" : { "$date" : "1985-05-12T23:14:30Z" }, "Gender" : "FEMALE", "Vocation" : "ENGINEER" }
{ "PersonId" : "6392529400", "FirstName" : "Elise", "LastName" : "Smith", "DateOfBirth" : { "$date" : "1972-01-13T09:32:07Z" }, "Vocation" : "ENGINEER" }
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new C app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with the C Driver guide](https://www.mongodb.com/docs/languages/c/c-driver/current/get-started/).

To learn more about performing aggregations in the C Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/c/c-driver/current/aggregation/).

After you install the driver, create a file called
`agg-tutorial.c`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```c
#include <stdio.h>
#include <bson/bson.h>
#include <mongoc/mongoc.h>

int main(void)
{
    mongoc_init();

    // Replace the placeholder with your connection string.
    char *uri = "<connection string>";
    mongoc_client_t* client = mongoc_client_new(uri);

    // Get a reference to relevant collections.
    // ... mongoc_collection_t *some_coll = mongoc_client_get_collection(client, "agg_tutorials_db", "some_coll");
    // ... mongoc_collection_t *another_coll = mongoc_client_get_collection(client, "agg_tutorials_db", "another_coll");

    // Delete any existing documents in collections if needed.
    // ... {
    // ...     bson_t *filter = bson_new();
    // ...     bson_error_t error;
    // ...     if (!mongoc_collection_delete_many(some_coll, filter, NULL, NULL, &error))
    // ...     {
    // ...         fprintf(stderr, "Delete error: %s\n", error.message);
    // ...     }
    // ...     bson_destroy(filter);
    // ... }

    // Insert sample data into the collection or collections.
    // ... {
    // ...     size_t num_docs = ...;
    // ...     bson_t *docs[num_docs];
    // ... 
    // ...     docs[0] = ...;
    // ... 
    // ...     bson_error_t error;
    // ...     if (!mongoc_collection_insert_many(some_coll, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    // ...     {
    // ...         fprintf(stderr, "Insert error: %s\n", error.message);
    // ...     }
    // ... 
    // ...     for (int i = 0; i < num_docs; i++)
    // ...     {
    // ...         bson_destroy(docs[i]);
    // ...     }
    // ... }

    {
        const bson_t *doc;

        // Add code to create pipeline stages.
        bson_t *pipeline = BCON_NEW("pipeline", "[",
        // ... Add pipeline stages here.
        "]");

        // Run the aggregation.
        // ... mongoc_cursor_t *results = mongoc_collection_aggregate(some_coll, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

        bson_destroy(pipeline);

        // Print the aggregation results.
        while (mongoc_cursor_next(results, &doc))
        {
            char *str = bson_as_canonical_extended_json(doc, NULL);
            printf("%s\n", str);
            bson_free(str);
        }
        bson_error_t error;
        if (mongoc_cursor_error(results, &error))
        {
            fprintf(stderr, "Aggregation error: %s\n", error.message);
        }

        mongoc_cursor_destroy(results);
    }

    // Clean up resources.
    // ... mongoc_collection_destroy(some_coll);
    mongoc_client_destroy(client);
    mongoc_cleanup();

    return EXIT_SUCCESS;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/c/c-driver/current/get-started/#create-a-connection-string)
step of the C Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```c
char *uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```c
mongoc_collection_t *persons = mongoc_client_get_collection(client, "agg_tutorials_db", "persons");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(persons, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 6;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "person_id", "6392529400",
        "firstname", "Elise",
        "lastname", "Smith",
        "dateofbirth", BCON_DATE_TIME(653616727000UL), // 1972-01-13T09:32:07Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(5625),
        "street", "Tipa Circle",
        "city", "Wojzinmoj",
        "}");

    docs[1] = BCON_NEW(
        "person_id", "1723338115",
        "firstname", "Olive",
        "lastname", "Ranieri",
        "dateofbirth", BCON_DATE_TIME(485113500000UL), // 1985-05-12T23:14:30Z
        "gender", "FEMALE",
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(9303),
        "street", "Mele Circle",
        "city", "Tobihbo",
        "}");

    docs[2] = BCON_NEW(
        "person_id", "8732762874",
        "firstname", "Toni",
        "lastname", "Jones",
        "dateofbirth", BCON_DATE_TIME(690559710000UL), // 1991-11-23T16:53:56Z
        "vocation", "POLITICIAN",
        "address", "{",
        "number", BCON_INT32(1),
        "street", "High Street",
        "city", "Upper Abbeywoodington",
        "}");

    docs[3] = BCON_NEW(
        "person_id", "7363629563",
        "firstname", "Bert",
        "lastname", "Gooding",
        "dateofbirth", BCON_DATE_TIME(449595112000UL), // 1941-04-07T22:11:52Z
        "vocation", "FLORIST",
        "address", "{",
        "number", BCON_INT32(13),
        "street", "Upper Bold Road",
        "city", "Redringtonville",
        "}");

    docs[4] = BCON_NEW(
        "person_id", "1029648329",
        "firstname", "Sophie",
        "lastname", "Celements",
        "dateofbirth", BCON_DATE_TIME(316265745000UL), // 1959-07-06T17:35:45Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(5),
        "street", "Innings Close",
        "city", "Basilbridge",
        "}");

    docs[5] = BCON_NEW(
        "person_id", "7363626383",
        "firstname", "Carl",
        "lastname", "Simmons",
        "dateofbirth", BCON_DATE_TIME(915250045000UL), // 1998-12-26T13:13:55Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(187),
        "street", "Hillside Road",
        "city", "Kenningford",
        "}");

    bson_error_t error;
    if (!mongoc_collection_insert_many(persons, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(docs[i]);
    }
}
```

**Step 1: Add a match stage for people who are engineers.**

In your pipeline, create a `$match` stage
that finds documents in which the value of the `vocation` field
is `"ENGINEER"`:

```c
"{", "$match", "{", "vocation", BCON_UTF8("ENGINEER"), "}", "}",
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```c
"{", "$sort", "{", "dateofbirth", BCON_INT32(-1), "}", "}",
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```c
"{", "$limit", BCON_INT32(3), "}",
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("address"), "]", "}",
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(persons, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(persons);
```

Finally, run the following commands in your shell to generate and
run the executable:

```bash
gcc -o aggc agg-tutorial.c $(pkg-config --libs --cflags libmongoc-1.0)
./aggc
```

**Tip:**

If you encounter connection errors by running the preceding
commands in one call, you can run them separately.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : { "$numberLong" : "915250045000" } }, "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : { "$numberLong" : "653616727000" } }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : { "$numberLong" : "485113500000" } }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
```

### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new C++ app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with C++](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/get-started/)
tutorial.

To learn more about using the C++ driver, see the [API documentation](https://mongocxx.org/api/current/).

To learn more about performing aggregations in the C++ Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/aggregation/).

After you install the driver, create a file called
`agg-tutorial.cpp`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```cpp
#include <iostream>
#include <bsoncxx/builder/basic/document.hpp>
#include <bsoncxx/builder/basic/kvp.hpp>
#include <bsoncxx/json.hpp>
#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/pipeline.hpp>
#include <mongocxx/uri.hpp>
#include <chrono>

using bsoncxx::builder::basic::kvp;
using bsoncxx::builder::basic::make_document;
using bsoncxx::builder::basic::make_array;

int main() {
   mongocxx::instance instance;

   // Replace the placeholder with your connection string.
   mongocxx::uri uri("<connection string>");
   mongocxx::client client(uri);

   auto db = client["agg_tutorials_db"];
   // Delete existing data in the database, if necessary.
   db.drop();

   // Get a reference to relevant collections.
   // ... auto some_coll = db["..."];
   // ... auto another_coll = db["..."];

   // Insert sample data into the collection or collections.
   // ... some_coll.insert_many(docs);

   // Create an empty pipelne.
   mongocxx::pipeline pipeline;

   // Add code to create pipeline stages.
   // pipeline.match(make_document(...));

   // Run the aggregation and print the results.
   auto cursor = orders.aggregate(pipeline);
   for (auto&& doc : cursor) {
      std::cout << bsoncxx::to_json(doc, bsoncxx::ExtendedJsonMode::k_relaxed) << std::endl;
   }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/get-started/#create-a-connection-string)
step of the C++ Get Started tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```cpp
mongocxx::uri uri{"mongodb+srv://mongodb-example:27017"};
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```cpp
auto persons = db["persons"];

std::vector<bsoncxx::document::value> docs = {
    bsoncxx::from_json(R"({
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": {"$date": 620947927},
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": {"$date": 485529270000},
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": {"$date": 690978836000},
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": {"$date": -88368048000},
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": {"$date": -31561935000},
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": {"$date": 915148835000},
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford"
        }
    })")
};

auto result = persons.insert_many(docs); // Might throw an exception
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "vocation": "ENGINEER"
})"));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "dateofbirth": -1
})"));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```cpp
pipeline.limit(3);
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "address"]
})"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```cpp
auto cursor = persons.aggregate(pipeline);
```

Finally, run the following commands in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : "1999-01-01T00:00:35Z" }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : "1985-05-21T13:14:30Z" }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : "1970-01-08T04:29:07.927Z" }, "vocation" : "ENGINEER" }
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Node.js app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Node.js Driver Quick Start guide`.

To learn more about performing aggregations in the Node.js Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.js`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```javascript
const { MongoClient } = require("mongodb");

// Replace the placeholder with your connection string.
const uri = "<connection string>";
const client = new MongoClient(uri);

async function run() {
  try {
    const aggDB = client.db("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... const someColl =
    // ... const anotherColl =

    // Delete any existing documents in collections.
    // ... await someColl.deleteMany({});

    // Insert sample data into the collection or collections.
    // ... const someData = [ ... ];
    // ... await someColl.insertMany(someData);

    // Create an empty pipeline array.
    const pipeline = [];

    // Add code to create pipeline stages.
    // ... pipeline.push({ ... })

    // Run the aggregation.
    // ... const aggregationResult = ...

    // Print the aggregation results.
    for await (const document of aggregationResult) {
      console.log(document);
    }
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Node.js Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```javascript
const uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```javascript
const persons = aggDB.collection("persons");
await persons.deleteMany({});

await persons.insertMany([
  {
    person_id: "6392529400",
    firstname: "Elise",
    lastname: "Smith",
    dateofbirth: new Date("1972-01-13T09:32:07Z"),
    vocation: "ENGINEER",
    address: {
      number: 5625,
      street: "Tipa Circle",
      city: "Wojzinmoj",
    },
  },
  {
    person_id: "1723338115",
    firstname: "Olive",
    lastname: "Ranieri",
    dateofbirth: new Date("1985-05-12T23:14:30Z"),
    gender: "FEMALE",
    vocation: "ENGINEER",
    address: {
      number: 9303,
      street: "Mele Circle",
      city: "Tobihbo",
    },
  },
  {
    person_id: "8732762874",
    firstname: "Toni",
    lastname: "Jones",
    dateofbirth: new Date("1991-11-23T16:53:56Z"),
    vocation: "POLITICIAN",
    address: {
      number: 1,
      street: "High Street",
      city: "Upper Abbeywoodington",
    },
  },
  {
    person_id: "7363629563",
    firstname: "Bert",
    lastname: "Gooding",
    dateofbirth: new Date("1941-04-07T22:11:52Z"),
    vocation: "FLORIST",
    address: {
      number: 13,
      street: "Upper Bold Road",
      city: "Redringtonville",
    },
  },
  {
    person_id: "1029648329",
    firstname: "Sophie",
    lastname: "Celements",
    dateofbirth: new Date("1959-07-06T17:35:45Z"),
    vocation: "ENGINEER",
    address: {
      number: 5,
      street: "Innings Close",
      city: "Basilbridge",
    },
  },
  {
    person_id: "7363626383",
    firstname: "Carl",
    lastname: "Simmons",
    dateofbirth: new Date("1998-12-26T13:13:55Z"),
    vocation: "ENGINEER",
    address: {
      number: 187,
      street: "Hillside Road",
      city: "Kenningford",
    },
  },
]);
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```javascript
pipeline.push({
  $match: {
    vocation: "ENGINEER",
  },
});
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```javascript
pipeline.push({
  $sort: {
    dateofbirth: -1,
  },
});
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```javascript
pipeline.push({
  $limit: 3,
});
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```javascript
pipeline.push({
  $unset: ["_id", "address"],
});
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```javascript
const aggregationResult = await persons.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```javascript
{
  person_id: '7363626383',
  firstname: 'Carl',
  lastname: 'Simmons',
  dateofbirth: 1998-12-26T13:13:55.000Z,
  vocation: 'ENGINEER'
}
{
  person_id: '1723338115',
  firstname: 'Olive',
  lastname: 'Ranieri',
  dateofbirth: 1985-05-12T23:14:30.000Z,
  gender: 'FEMALE',
  vocation: 'ENGINEER'
}
{
  person_id: '6392529400',
  firstname: 'Elise',
  lastname: 'Smith',
  dateofbirth: 1972-01-13T09:32:07.000Z,
  vocation: 'ENGINEER'
}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new PHP app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the PHP library and connect to MongoDB,
see the [Get Started with the PHP Library](https://www.mongodb.com/docs/php-library/current/get-started/)
tutorial.

To learn more about performing aggregations in the PHP library, see the
[Aggregation guide](https://www.mongodb.com/docs/php-library/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.php`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```php
<?php

require 'vendor/autoload.php';

// Modify imports for each tutorial as needed.
use MongoDB\Client;
use MongoDB\BSON\UTCDateTime;
use MongoDB\Builder\Pipeline;
use MongoDB\Builder\Stage;
use MongoDB\Builder\Type\Sort;
use MongoDB\Builder\Query;
use MongoDB\Builder\Expression;
use MongoDB\Builder\Accumulator;

use function MongoDB\object;

// Replace the placeholder with your connection string.
$uri = '<connection string>';
$client = new Client($uri);

// Get a reference to relevant collections.
// ... $someColl = $client->agg_tutorials_db->someColl;
// ... $anotherColl = $client->agg_tutorials_db->anotherColl;

// Delete any existing documents in collections if needed.
// ... $someColl->deleteMany([]);

// Insert sample data into the collection or collections.
// ... $someColl->insertMany(...);

// Add code to create pipeline stages within the Pipeline instance.
// ... $pipeline = new Pipeline(...);

// Run the aggregation.
// ... $cursor = $someColl->aggregate($pipeline);

// Print the aggregation results.
foreach ($cursor as $doc) {
    echo json_encode($doc, JSON_PRETTY_PRINT), PHP_EOL;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```php
$uri = 'mongodb+srv://mongodb-example:27017';
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```php
$persons = $client->agg_tutorials_db->persons;
$persons->deleteMany([]);

$persons->insertMany(
    [
        [
            'person_id' => '6392529400',
            'firstname' => 'Elise',
            'lastname' => 'Smith',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1972-01-13T09:32:07')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 5625, 'Street' => 'Tipa Circle', 'city' => 'Wojzinmoj'],
        ],
        [
            'person_id' => '1723338115',
            'firstname' => 'Olive',
            'lastname' => 'Ranieri',
            'gender' => 'FEMALE',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1985-05-12T23:14:30')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 9303, 'street' => 'Mele Circle', 'city' => 'Tobihbo'],
        ],
        [
            'person_id' => '8732762874',
            'firstname' => 'Toni',
            'lastname' => 'Jones',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1991-11-23T16:53:56')),
            'vocation' => 'POLITICIAN',
            'address' => ['number' => 1, 'street' => 'High Street', 'city' => 'Upper Abbeywoodington'],
        ],
        [
            'person_id' => '7363629563',
            'firstname' => 'Bert',
            'lastname' => 'Gooding',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1941-04-07T22:11:52')),
            'vocation' => 'FLORIST',
            'address' => ['number' => 13, 'street' => 'Upper Bold Road', 'city' => 'Redringtonville'],
        ],
        [
            'person_id' => '1029648329',
            'firstname' => 'Sophie',
            'lastname' => 'Celements',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1959-07-06T17:35:45')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 5, 'street' => 'Innings Close', 'city' => 'Basilbridge'],
        ],
        [
            'person_id' => '7363626383',
            'firstname' => 'Carl',
            'lastname' => 'Simmons',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1998-12-26T13:13:55')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 187, 'street' => 'Hillside Road', 'city' => 'Kenningford'],
        ]
    ]
);
```

**Step 1: Add a match stage for people who are engineers.**

In your `Pipeline` instance, create a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```php
Stage::match(vocation: 'ENGINEER'),
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```php
Stage::sort(dateofbirth: Sort::Desc),
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```php
Stage::limit(3),
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```php
Stage::unset('_id', 'address')
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```php
$cursor = $persons->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{
    "person_id": "7363626383",
    "firstname": "Carl",
    "lastname": "Simmons",
    "dateofbirth": {
        "$date": {
            "$numberLong": "914678035000"
        }
    },
    "vocation": "ENGINEER"
}
{
    "person_id": "1723338115",
    "firstname": "Olive",
    "lastname": "Ranieri",
    "gender": "FEMALE",
    "dateofbirth": {
        "$date": {
            "$numberLong": "484787670000"
        }
    },
    "vocation": "ENGINEER"
}
{
    "person_id": "6392529400",
    "firstname": "Elise",
    "lastname": "Smith",
    "dateofbirth": {
        "$date": {
            "$numberLong": "64143127000"
        }
    },
    "vocation": "ENGINEER"
}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Ruby app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the Ruby Driver and connect to MongoDB,
see the [Get Started with the Ruby Driver guide](https://www.mongodb.com/docs/ruby-driver/upcoming/get-started/).

To learn more about performing aggregations in the Ruby Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/ruby-driver/upcoming/aggregation/).

After you install the driver, create a file called
`agg_tutorial.rb`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```ruby
# typed: strict
require 'mongo'
require 'bson'

# Replace the placeholder with your connection string.
uri = "<connection string>"

Mongo::Client.new(uri) do |client|

  agg_db = client.use('agg_tutorials_db')

  # Get a reference to relevant collections.
  # ... some_coll = agg_db[:some_coll]

  # Delete any existing documents in collections if needed.
  # ... some_coll.delete_many({})

  # Insert sample data into the collection or collections.
  # ... some_coll.insert_many( ... )

  # Add code to create pipeline stages within the array.
  # ... pipeline = [ ... ]

  # Run the aggregation.
  # ... aggregation_result = some_coll.aggregate(pipeline)

  # Print the aggregation results.
  aggregation_result.each do |doc|
    puts doc
  end

end
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/ruby-driver/upcoming/get-started/create-a-connection-string/)
step of the Ruby Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```ruby
uri = "mongodb+srv://mongodb-example:27017"
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```ruby
persons = agg_db[:persons]
persons.delete_many({})

persons.insert_many(
  [
    {
      person_id: "6392529400",
      firstname: "Elise",
      lastname: "Smith",
      dateofbirth: DateTime.parse("1972-01-13T09:32:07Z"),
      vocation: "ENGINEER",
      address: {
        number: 5625,
        street: "Tipa Circle",
        city: "Wojzinmoj",
      },
    },
    {
      person_id: "1723338115",
      firstname: "Olive",
      lastname: "Ranieri",
      dateofbirth: DateTime.parse("1985-05-12T23:14:30Z"),
      gender: "FEMALE",
      vocation: "ENGINEER",
      address: {
        number: 9303,
        street: "Mele Circle",
        city: "Tobihbo",
      },
    },
    {
      person_id: "8732762874",
      firstname: "Toni",
      lastname: "Jones",
      dateofbirth: DateTime.parse("1991-11-23T16:53:56Z"),
      vocation: "POLITICIAN",
      address: {
        number: 1,
        street: "High Street",
        city: "Upper Abbeywoodington",
      },
    },
    {
      person_id: "7363629563",
      firstname: "Bert",
      lastname: "Gooding",
      dateofbirth: DateTime.parse("1941-04-07T22:11:52Z"),
      vocation: "FLORIST",
      address: {
        number: 13,
        street: "Upper Bold Road",
        city: "Redringtonville",
      },
    },
    {
      person_id: "1029648329",
      firstname: "Sophie",
      lastname: "Celements",
      dateofbirth: DateTime.parse("1959-07-06T17:35:45Z"),
      vocation: "ENGINEER",
      address: {
        number: 5,
        street: "Innings Close",
        city: "Basilbridge",
      },
    },
    {
      person_id: "7363626383",
      firstname: "Carl",
      lastname: "Simmons",
      dateofbirth: DateTime.parse("1998-12-26T13:13:55Z"),
      vocation: "ENGINEER",
      address: {
        number: 187,
        street: "Hillside Road",
        city: "Kenningford",
      },
    },
  ]
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```ruby
{ "$match": { "vocation": "ENGINEER" } },
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```ruby
{ "$sort": { "dateofbirth": -1 } },
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```ruby
{ "$limit": 3 },
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```ruby
{ "$unset": ["_id", "address"] },
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```ruby
aggregation_result = persons.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.rb
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id"=>"7363626383", "firstname"=>"Carl", "lastname"=>"Simmons", "dateofbirth"=>1998-12-26 13:13:55 UTC, "vocation"=>"ENGINEER"}
{"person_id"=>"1723338115", "firstname"=>"Olive", "lastname"=>"Ranieri", "dateofbirth"=>1985-05-12 23:14:30 UTC, "gender"=>"FEMALE", "vocation"=>"ENGINEER"}
{"person_id"=>"6392529400", "firstname"=>"Elise", "lastname"=>"Smith", "dateofbirth"=>1972-01-13 09:32:07 UTC, "vocation"=>"ENGINEER"}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Go app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Go Driver Quick Start guide`.

To learn more about performing aggregations in the Go Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.go`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "go.mongodb.org/mongo-driver/v2/bson"
    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

// Define structs.
// type MyStruct struct { ... }

func main() {
    // Replace the placeholder with your connection string.
    const uri = "<connection string>"

    client, err := mongo.Connect(options.Client().ApplyURI(uri))
    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err = client.Disconnect(context.TODO()); err != nil {
            log.Fatal(err)
        }
    }()

    aggDB := client.Database("agg_tutorials_db")

    // Get a reference to relevant collections.
    // ... someColl := aggDB.Collection("...")
    // ... anotherColl := aggDB.Collection("...")

    // Delete any existing documents in collections if needed.
    // ... someColl.DeleteMany(context.TODO(), bson.D{})

    // Insert sample data into the collection or collections.   
    // ... _, err = someColl.InsertMany(...)

    // Add code to create pipeline stages.
    // ... myStage := bson.D{{...}}

    // Create a pipeline that includes the stages.
    // ... pipeline := mongo.Pipeline{...}

    // Run the aggregation.
    // ... cursor, err := someColl.Aggregate(context.TODO(), pipeline)

    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err := cursor.Close(context.TODO()); err != nil {
            log.Fatalf("failed to close cursor: %v", err)
        }
    }()

    // Decode the aggregation results.
    var results []bson.D
    if err = cursor.All(context.TODO(), &results); err != nil {
        log.Fatalf("failed to decode results: %v", err)
    }

    // Print the aggregation results.
    for _, result := range results {
        res, _ := bson.MarshalExtJSON(result, false, false)
        fmt.Println(string(res))
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a MongoDB Cluster`
step of the Go Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```go
const uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Go structs to model the data in the `persons`
collection:

```go
type Person struct {
	PersonID    string        `bson:"person_id"`
	Firstname   string        `bson:"firstname"`
	Lastname    string        `bson:"lastname"`
	Gender      string        `bson:"gender,omitempty"`
	DateOfBirth bson.DateTime `bson:"dateofbirth"`
	Vocation    string        `bson:"vocation"`
	Address     Address       `bson:"address"`
}

type Address struct {
	Number int
	Street string
	City   string
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```go
persons := aggDB.Collection("persons")
persons.DeleteMany(context.TODO(), bson.D{})

_, err = persons.InsertMany(context.TODO(), []interface{}{
	Person{
		PersonID:    "6392529400",
		Firstname:   "Elise",
		Lastname:    "Smith",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1972, 1, 13, 9, 32, 7, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 5625, Street: "Tipa Circle", City: "Wojzinmoj"},
	},
	Person{
		PersonID:    "1723338115",
		Firstname:   "Olive",
		Lastname:    "Ranieri",
		Gender:      "FEMALE",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1985, 5, 12, 23, 14, 30, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 9303, Street: "Mele Circle", City: "Tobihbo"},
	},
	Person{
		PersonID:    "8732762874",
		Firstname:   "Toni",
		Lastname:    "Jones",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1991, 11, 23, 16, 53, 56, 0, time.UTC)),
		Vocation:    "POLITICIAN",
		Address:     Address{Number: 1, Street: "High Street", City: "Upper Abbeywoodington"},
	},
	Person{
		PersonID:    "7363629563",
		Firstname:   "Bert",
		Lastname:    "Gooding",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1941, 4, 7, 22, 11, 52, 0, time.UTC)),
		Vocation:    "FLORIST",
		Address:     Address{Number: 13, Street: "Upper Bold Road", City: "Redringtonville"},
	},
	Person{
		PersonID:    "1029648329",
		Firstname:   "Sophie",
		Lastname:    "Celements",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1959, 7, 6, 17, 35, 45, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 5, Street: "Innings Close", City: "Basilbridge"},
	},
	Person{
		PersonID:    "7363626383",
		Firstname:   "Carl",
		Lastname:    "Simmons",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1998, 12, 26, 13, 13, 55, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 187, Street: "Hillside Road", City: "Kenningford"},
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{{Key: "vocation", Value: "ENGINEER"}}}}
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```go
sortStage := bson.D{{Key: "$sort", Value: bson.D{{Key: "dateofbirth", Value: -1}}}}
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```go
limitStage := bson.D{{Key: "$limit", Value: 3}}
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id", "address"}}}
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```go
pipeline := mongo.Pipeline{matchStage, sortStage, limitStage, unsetStage}
cursor, err := persons.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id":"7363626383","firstname":"Carl","lastname":"Simmons","dateofbirth":{"$date":"1998-12-26T13:13:55Z"},"vocation":"ENGINEER"}
{"person_id":"1723338115","firstname":"Olive","lastname":"Ranieri","gender":"FEMALE","dateofbirth":{"$date":"1985-05-12T23:14:30Z"},"vocation":"ENGINEER"}
{"person_id":"6392529400","firstname":"Elise","lastname":"Smith","dateofbirth":{"$date":"1972-01-13T09:32:07Z"},"vocation":"ENGINEER"}
```

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Rust app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Rust Driver Quick Start guide`.

To learn more about performing aggregations in the Rust Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg-tutorial.rs`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```rust
use mongodb::{
    bson::{doc, Document},
    options::ClientOptions,
    Client,
};
use futures::stream::TryStreamExt;
use std::error::Error;

// Define structs.
// #[derive(Debug, Serialize, Deserialize)]
// struct MyStruct { ... }

#[tokio::main]
async fn main() mongodb::error::Result<()> {
    // Replace the placeholder with your connection string.
    let uri = "<connection string>";
    let client = Client::with_uri_str(uri).await?;

    let agg_db = client.database("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... let some_coll: Collection<T> = agg_db.collection("...");
    // ... let another_coll: Collection<T> = agg_db.collection("...");

    // Delete any existing documents in collections if needed.
    // ... some_coll.delete_many(doc! {}).await?;

    // Insert sample data into the collection or collections.
    // ... some_coll.insert_many(vec![...]).await?;

    // Create an empty pipeline.
    let mut pipeline = Vec::new();

    // Add code to create pipeline stages.
    // pipeline.push(doc! { ... });

    // Run the aggregation and print the results.
    let mut results = some_coll.aggregate(pipeline).await?;
    while let Some(result) = results.try_next().await? {
       println!("{:?}\n", result);
    }
    Ok(())
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Rust Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```rust
let uri = "mongodb+srv://mongodb-example:27017";
```

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Rust structs to model the data in the `persons`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Address {
    number: i32,
    street: String,
    city: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Person {
    person_id: String,
    firstname: String,
    lastname: String,
    dateofbirth: DateTime,
    vocation: String,
    address: Address,
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```rust
let persons: Collection<Person> = agg_db.collection("persons");
persons.delete_many(doc! {}).await?;

let data = vec![
    Person {
        person_id: "6392529400".to_string(),
        firstname: "Elise".to_string(),
        lastname: "Smith".to_string(),
        dateofbirth: DateTime::builder().year(1972).month(1).day(13).hour(9).minute(32).second(7).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 5625,
            street: "Tipa Circle".to_string(),
            city: "Wojzinmoj".to_string(),
        },
    },
    Person {
        person_id: "1723338115".to_string(),
        firstname: "Olive".to_string(),
        lastname: "Ranieri".to_string(),
        gender: "FEMALE".to_string(),
        dateofbirth: DateTime::builder().year(1985).month(5).day(12).hour(23).minute(14).second(30).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 9303,
            street: "Mele Circle".to_string(),
            city: "Tobihbo".to_string(),
        },
    },
    Person {
        person_id: "8732762874".to_string(),
        firstname: "Toni".to_string(),
        lastname: "Jones".to_string(),
        dateofbirth: DateTime::builder().year(1991).month(11).day(23).hour(16).minute(53).second(56).build().unwrap(),
        vocation: "POLITICIAN".to_string(),
        address: Address {
            number: 1,
            street: "High Street".to_string(),
            city: "Upper Abbeywoodington".to_string(),
        },
    },
    Person {
        person_id: "7363629563".to_string(),
        firstname: "Bert".to_string(),
        lastname: "Gooding".to_string(),
        dateofbirth: DateTime::builder().year(1941).month(4).day(7).hour(22).minute(11).second(52).build().unwrap(),
        vocation: "FLORIST".to_string(),
        address: Address {
            number: 13,
            street: "Upper Bold Road".to_string(),
            city: "Redringtonville".to_string(),
        },
    },
    Person {
        person_id: "1029648329".to_string(),
        firstname: "Sophie".to_string(),
        lastname: "Celements".to_string(),
        dateofbirth: DateTime::builder().year(1959).month(7).day(6).hour(17).minute(35).second(45).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 5,
            street: "Innings Close".to_string(),
            city: "Basilbridge".to_string(),
        },
    },
    Person {
        person_id: "7363626383".to_string(),
        firstname: "Carl".to_string(),
        lastname: "Simmons".to_string(),
        dateofbirth: DateTime::builder().year(1998).month(12).day(26).hour(13).minute(13).second(55).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 187,
            street: "Hillside Road".to_string(),
            city: "Kenningford".to_string(),
        },
    },
];

persons.insert_many(data).await?;
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```rust
pipeline.push(doc! { "$match": { "vocation": "ENGINEER" } });
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```rust
pipeline.push(doc! { "$sort": { "dateofbirth": -1 } });
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```rust
pipeline.push(doc! { "$limit": 3 });
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```rust
pipeline.push(doc! { "$unset": ["_id", "address"] });
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```rust
let mut cursor = persons.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
Document({"person_id": String("7363626383"), "firstname": String("Carl"), "lastname": String("Simmons"), "dateofbirth": DateTime(1998-12-26 13:13:55.0 +00:00:00), "vocation": String("ENGINEER")})

Document({"person_id": String("1723338115"), "firstname": String("Olive"), "lastname": String("Ranieri"), "gender": String("FEMALE"), "dateofbirth": DateTime(1985-05-12 23:14:30.0 +00:00:00), "vocation": String("ENGINEER")})

Document({"person_id": String("6392529400"), "firstname": String("Elise"), "lastname": String("Smith"), "dateofbirth": DateTime(1972-01-13 9:32:07.0 +00:00:00), "vocation": String("ENGINEER")})
```
