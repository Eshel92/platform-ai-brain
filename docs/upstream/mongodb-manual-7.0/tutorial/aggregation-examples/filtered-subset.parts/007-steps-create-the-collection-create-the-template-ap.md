<!-- Part 7 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

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
