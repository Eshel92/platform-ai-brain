<!-- Part 2 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```java
MongoCollection<Document> orders = aggDB.getCollection("orders");
orders.deleteMany(Filters.empty());

orders.insertMany(
        Arrays.asList(
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-05-30T08:35:52"))
                        .append("value", 231),
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-01-13T09:32:07"))
                        .append("value", 99),
                new Document("customer_id", "oranieri@warmmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-01-01T08:25:37"))
                        .append("value", 63),
                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2019-05-28T19:13:32"))
                        .append("value", 2),
                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-11-23T22:56:53"))
                        .append("value", 187),
                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-08-18T23:04:48"))
                        .append("value", 4),
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-12-26T08:55:46"))
                        .append("value", 4),
                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2021-02-28T07:49:32"))
                        .append("value", 1024),
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-10-03T13:49:44"))
                        .append("value", 102)
        )
);
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```java
pipeline.add(Aggregates.match(Filters.and(
        Filters.gte("orderdate", LocalDateTime.parse("2020-01-01T00:00:00")),
        Filters.lt("orderdate", LocalDateTime.parse("2021-01-01T00:00:00"))
)));
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```java
pipeline.add(Aggregates.sort(Sorts.ascending("orderdate")));
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to collect
order documents by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```java
pipeline.add(Aggregates.group(
        "$customer_id",
        Accumulators.first("first_purchase_date", "$orderdate"),
        Accumulators.sum("total_value", "$value"),
        Accumulators.sum("total_orders", 1),
        Accumulators.push("orders",
                new Document("orderdate", "$orderdate")
                        .append("value", "$value")
        )
));
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```java
pipeline.add(Aggregates.sort(Sorts.ascending("first_purchase_date")));
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```java
pipeline.add(Aggregates.set(new Field<>("customer_id", "$_id")));
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```java
pipeline.add(Aggregates.unset("_id"));
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```java
AggregateIterable<Document> aggregationResult = orders.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date": {"$date": "2020-01-01T08:25:37Z"}, "total_value": 63, "total_orders": 1, "orders": [{"orderdate": {"$date": "2020-01-01T08:25:37Z"}, "value": 63}], "customer_id": "oranieri@warmmail.com"}
{"first_purchase_date": {"$date": "2020-01-13T09:32:07Z"}, "total_value": 436, "total_orders": 4, "orders": [{"orderdate": {"$date": "2020-01-13T09:32:07Z"}, "value": 99}, {"orderdate": {"$date": "2020-05-30T08:35:52Z"}, "value": 231}, {"orderdate": {"$date": "2020-10-03T13:49:44Z"}, "value": 102}, {"orderdate": {"$date": "2020-12-26T08:55:46Z"}, "value": 4}], "customer_id": "elise_smith@myemail.com"}
{"first_purchase_date": {"$date": "2020-08-18T23:04:48Z"}, "total_value": 191, "total_orders": 2, "orders": [{"orderdate": {"$date": "2020-08-18T23:04:48Z"}, "value": 4}, {"orderdate": {"$date": "2020-11-23T22:56:53Z"}, "value": 187}], "customer_id": "tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**kotlin-coroutine:**


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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

First, create a Kotlin data class to model the data in the `orders`
collection:

```kotlin
@Serializable
data class Order(
    val customerID: String,
    @Contextual val orderDate: LocalDateTime,
    val value: Int
)
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```kotlin
val orders = aggDB.getCollection<Order>("orders")
orders.deleteMany(Filters.empty())

orders.insertMany(
    listOf(
        Order("elise_smith@myemail.com", LocalDateTime.parse("2020-05-30T08:35:52"), 231),
        Order("elise_smith@myemail.com", LocalDateTime.parse("2020-01-13T09:32:07"), 99),
        Order("oranieri@warmmail.com", LocalDateTime.parse("2020-01-01T08:25:37"), 63),
        Order("tj@wheresmyemail.com", LocalDateTime.parse("2019-05-28T19:13:32"), 2),
        Order("tj@wheresmyemail.com", LocalDateTime.parse("2020-11-23T22:56:53"), 187),
        Order("tj@wheresmyemail.com", LocalDateTime.parse("2020-08-18T23:04:48"), 4),
        Order("elise_smith@myemail.com", LocalDateTime.parse("2020-12-26T08:55:46"), 4),
        Order("tj@wheresmyemail.com", LocalDateTime.parse("2021-02-28T07:49:32"), 1024),
        Order("elise_smith@myemail.com", LocalDateTime.parse("2020-10-03T13:49:44"), 102)
    )
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.and(
            Filters.gte(Order::orderDate.name, LocalDateTime.parse("2020-01-01T00:00:00").toJavaLocalDateTime()),
            Filters.lt(Order::orderDate.name, LocalDateTime.parse("2021-01-01T00:00:00").toJavaLocalDateTime())
        )
    )
)
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderDate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```kotlin
pipeline.add(Aggregates.sort(Sorts.ascending(Order::orderDate.name)))
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to collect
order documents by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```kotlin
pipeline.add(
    Aggregates.group(
        "\$${Order::customerID.name}",
        Accumulators.first("first_purchase_date", "\$${Order::orderDate.name}"),
        Accumulators.sum("total_value", "\$${Order::value.name}"),
        Accumulators.sum("total_orders", 1),
        Accumulators.push(
            "orders",
            Document("orderdate", "\$${Order::orderDate.name}")
                .append("value", "\$${Order::value.name}")
        )
    )
)
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```kotlin
pipeline.add(Aggregates.sort(Sorts.ascending("first_purchase_date")))
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```kotlin
pipeline.add(Aggregates.set(Field("customer_id", "\$_id")))
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```kotlin
pipeline.add(Aggregates.unset("_id"))
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```kotlin
val aggregationResult = orders.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document{{first_purchase_date=Wed Jan 01 03:25:37 EST 2020, total_value=63, total_orders=1, orders=[Document{{orderdate=Wed Jan 01 03:25:37 EST 2020, value=63}}], customer_id=oranieri@warmmail.com}}
Document{{first_purchase_date=Mon Jan 13 04:32:07 EST 2020, total_value=436, total_orders=4, orders=[Document{{orderdate=Mon Jan 13 04:32:07 EST 2020, value=99}}, Document{{orderdate=Sat May 30 04:35:52 EDT 2020, value=231}}, Document{{orderdate=Sat Oct 03 09:49:44 EDT 2020, value=102}}, Document{{orderdate=Sat Dec 26 03:55:46 EST 2020, value=4}}], customer_id=elise_smith@myemail.com}}
Document{{first_purchase_date=Tue Aug 18 19:04:48 EDT 2020, total_value=191, total_orders=2, orders=[Document{{orderdate=Tue Aug 18 19:04:48 EDT 2020, value=4}}, Document{{orderdate=Mon Nov 23 17:56:53 EST 2020, value=187}}], customer_id=tj@wheresmyemail.com}}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**scala:**


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
