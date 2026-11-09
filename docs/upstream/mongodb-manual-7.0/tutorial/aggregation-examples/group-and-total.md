<!-- Converted from tutorial/aggregation-examples/group-and-total.txt (reStructuredText). Includes are inlined. -->

# Group and Total Data

This tutorial illustrates how to construct an aggregation pipeline,
perform the aggregation on a collection, and display the results using
the language of your choice.

## About This Task

This tutorial demonstrates how to group and analyze customer order data.
The results show the list of customers who purchased items in 2020 and
include each customer's order history for 2020.

The aggregation pipeline performs the following operations:

- Matches a subset of documents by a field value
- Groups documents by common field values
- Adds computated fields to each result document

## Before You Begin

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Shell.

----------

**shell:**

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-05-30T08:35:52Z"),
      value: 231,
   },
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-01-13T09:32:07Z"),
      value: 99,
   },
   {
      customer_id: "oranieri@warmmail.com",
      orderdate: new Date("2020-01-01T08:25:37Z"),
      value: 63,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2019-05-28T19:13:32Z"),
      value: 2,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2020-11-23T22:56:53Z"),
      value: 187,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2020-08-18T23:04:48Z"),
      value: 4,
   },
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-12-26T08:55:46Z"),
      value: 4,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2021-02-29T07:49:32Z"),
      value: 1024,
   },
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-10-03T13:49:44Z"),
      value: 102,
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [
   // Stage 1: Match orders in 2020
   { $match: {
      orderdate: {
         $gte: new Date("2020-01-01T00:00:00Z"),
         $lt: new Date("2021-01-01T00:00:00Z"),
      }
   } },

   // Stage 2: Sort orders by date
   { $sort: { orderdate: 1 } },

   // Stage 3: Group orders by email address
   { $group: {
      _id: "$customer_id",
      first_purchase_date: { $first: "$orderdate" },
      total_value: { $sum: "$value" },
      total_orders: { $sum: 1 },
      orders: { $push: 
         { 
            orderdate: "$orderdate", 
            value: "$value" 
         }
      }
   } },

   // Stage 4: Sort orders by first order date
   { $sort: { first_purchase_date: 1 } },

   // Stage 5: Display the customers' email addresses
   { $set: { customer_id: "$_id" } },

   // Stage 6: Remove unneeded fields
   { $unset: ["_id"] }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020. The result documents contain details on all orders
placed by a given customer, grouped by the customer's email
address.

```javascript
{
   first_purchase_date: ISODate("2020-01-01T08:25:37.000Z"),
   total_value: 63,
   total_orders: 1,
   orders: [ { orderdate: ISODate("2020-01-01T08:25:37.000Z"), value: 63 } ],
   customer_id: 'oranieri@warmmail.com'
}
{
   first_purchase_date: ISODate("2020-01-13T09:32:07.000Z"),
   total_value: 436,
   total_orders: 4,
   orders: [
      { orderdate: ISODate("2020-01-13T09:32:07.000Z"), value: 99 },
      { orderdate: ISODate("2020-05-30T08:35:52.000Z"), value: 231 },
      { orderdate: ISODate("2020-10-03T13:49:44.000Z"), value: 102 },
      { orderdate: ISODate("2020-12-26T08:55:46.000Z"), value: 4 }
   ],
   customer_id: 'elise_smith@myemail.com'
}
{
   first_purchase_date: ISODate("2020-08-18T23:04:48.000Z"),
   total_value: 191,
   total_orders: 2,
   orders: [
      { orderdate: ISODate("2020-08-18T23:04:48.000Z"), value: 4 },
      { orderdate: ISODate("2020-11-23T22:56:53.000Z"), value: 187 }
   ],
   customer_id: 'tj@wheresmyemail.com'
}
```

**python:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```python
orders_coll = agg_db["orders"]
orders_coll.delete_many({})

order_data = [
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 5, 30, 8, 35, 52),
        "value": 231,
    },
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 1, 13, 9, 32, 7),
        "value": 99,
    },
    {
        "customer_id": "oranieri@warmmail.com",
        "orderdate": datetime(2020, 1, 1, 8, 25, 37),
        "value": 63,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2019, 5, 28, 19, 13, 32),
        "value": 2,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2020, 11, 23, 22, 56, 53),
        "value": 187,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2020, 8, 18, 23, 4, 48),
        "value": 4,
    },
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 12, 26, 8, 55, 46),
        "value": 4,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2021, 2, 28, 7, 49, 32),
        "value": 1024,
    },
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 10, 3, 13, 49, 44),
        "value": 102,
    },
]

orders_coll.insert_many(order_data)
```

**Step 1: Add a match stage for orders in 2020.**

In your `Pipeline` instance, add a `$match` stage that matches
orders placed in 2020:

```python
pipeline.append(
    {
        "$match": {
            "orderdate": {
                "$gte": datetime(2020, 1, 1, 0, 0, 0),
                "$lt": datetime(2021, 1, 1, 0, 0, 0),
            }
        }
    }
)
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```python
pipeline.append({"$sort": {"orderdate": 1}})
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to group
orders by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```python
pipeline.append(
    {
        "$group": {
            "_id": "$customer_id",
            "first_purchase_date": {"$first": "$orderdate"},
            "total_value": {"$sum": "$value"},
            "total_orders": {"$sum": 1},
            "orders": {"$push": {"orderdate": "$orderdate", "value": "$value"}},
        }
    }
)
```

**Step 4: Add a sort stage to sort by first order date.**

Next, create another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```python
pipeline.append({"$sort": {"first_purchase_date": 1}})
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```python
pipeline.append({"$set": {"customer_id": "$_id"}})
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```python
pipeline.append({"$unset": ["_id"]})
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```python
aggregation_result = orders_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{'first_purchase_date': datetime.datetime(2020, 1, 1, 8, 25, 37), 'total_value': 63, 'total_orders': 1, 'orders': [{'orderdate': datetime.datetime(2020, 1, 1, 8, 25, 37), 'value': 63}], 'customer_id': 'oranieri@warmmail.com'}
{'first_purchase_date': datetime.datetime(2020, 1, 13, 9, 32, 7), 'total_value': 436, 'total_orders': 4, 'orders': [{'orderdate': datetime.datetime(2020, 1, 13, 9, 32, 7), 'value': 99}, {'orderdate': datetime.datetime(2020, 5, 30, 8, 35, 52), 'value': 231}, {'orderdate': datetime.datetime(2020, 10, 3, 13, 49, 44), 'value': 102}, {'orderdate': datetime.datetime(2020, 12, 26, 8, 55, 46), 'value': 4}], 'customer_id': 'elise_smith@myemail.com'}
{'first_purchase_date': datetime.datetime(2020, 8, 18, 23, 4, 48), 'total_value': 191, 'total_orders': 2, 'orders': [{'orderdate': datetime.datetime(2020, 8, 18, 23, 4, 48), 'value': 4}, {'orderdate': datetime.datetime(2020, 11, 23, 22, 56, 53), 'value': 187}], 'customer_id': 'tj@wheresmyemail.com'}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**java-sync:**

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

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```scala
val orders = aggDB.getCollection("orders")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

orders.insertMany(Seq(
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
    "value" -> 231),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-01-13T09:32:07"),
    "value" -> 99),
  Document("customer_id" -> "oranieri@warmmail.com",
    "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
    "value" -> 63),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
    "value" -> 2),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2020-11-23T22:56:53"),
    "value" -> 187),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2020-08-18T23:04:48"),
    "value" -> 4),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
    "value" -> 4),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2021-02-28T07:49:32"),
    "value" -> 1024),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-10-03T13:49:44"),
    "value" -> 102)
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```scala
Aggregates.filter(Filters.and(
  Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
  Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
)),
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```scala
Aggregates.sort(Sorts.ascending("orderdate")),
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

```scala
Aggregates.group(
  "$customer_id",
  Accumulators.first("first_purchase_date", "$orderdate"),
  Accumulators.sum("total_value", "$value"),
  Accumulators.sum("total_orders", 1),
  Accumulators.push("orders", Document("orderdate" -> "$orderdate", "value" -> "$value"))
),
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```scala
Aggregates.sort(Sorts.ascending("first_purchase_date")),
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```scala
Aggregates.set(Field("customer_id", "$_id")),
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```scala
Aggregates.unset("_id")
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date": {"$date": "2020-01-01T13:25:37Z"}, "total_value": 63, "total_orders": 1, "orders": [{"orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63}], "customer_id": "oranieri@warmmail.com"}
{"first_purchase_date": {"$date": "2020-01-13T14:32:07Z"}, "total_value": 436, "total_orders": 4, "orders": [{"orderdate": {"$date": "2020-01-13T14:32:07Z"}, "value": 99}, {"orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 231}, {"orderdate": {"$date": "2020-10-03T17:49:44Z"}, "value": 102}, {"orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 4}], "customer_id": "elise_smith@myemail.com"}
{"first_purchase_date": {"$date": "2020-08-19T03:04:48Z"}, "total_value": 191, "total_orders": 2, "orders": [{"orderdate": {"$date": "2020-08-19T03:04:48Z"}, "value": 4}, {"orderdate": {"$date": "2020-11-24T03:56:53Z"}, "value": 187}], "customer_id": "tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**csharp:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `CustomerId`
field, which contains customer email addresses.

First, create a C# class to model the data in the `orders`
collection:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public int Value { get; set; }
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```csharp
var orders = aggDB.GetCollection<Order>("orders");
orders.DeleteMany(Builders<Order>.Filter.Empty);

orders.InsertMany(new List<Order>
    {
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
            Value = 231
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-01-13T09:32:07Z"),
            Value = 99
        },
        new Order
        {
            CustomerId = "oranieri@warmmail.com",
            OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
            Value = 63
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
            Value = 2
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2020-11-23T22:56:53Z"),
            Value = 187
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2020-08-18T23:04:48Z"),
            Value = 4
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
            Value = 4
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2021-02-28T07:49:32Z"),
            Value = 1024
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-10-03T13:49:44Z"),
            Value = 102
        }
    });
```

**Step 1: Add a match stage for orders in 2020.**

First, start the aggregation on the `orders` collection and
chain a `$match` stage that matches orders placed in
2020:

```csharp
var results = orders.Aggregate()
    .Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
                o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `OrderDate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```csharp
.SortBy(o => o.OrderDate)
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to collect
order documents by the value of the `CustomerId` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `CustomerId`: the customer's email address (the grouping key)
- `FirstPurchaseDate`: the date of the customer's first purchase
- `TotalValue`: the total value of all the customer's purchases
- `TotalOrders`: the total number of the customer's purchases
- `Orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```csharp
.Group(
    o => o.CustomerId,
    g => new
    {
      CustomerId = g.Key,
      FirstPurchaseDate = g.First().OrderDate,
      TotalValue = g.Sum(i => i.Value),
      TotalOrders = g.Count(),
      Orders = g.Select(i => new { i.OrderDate, i.Value }).ToList()
    }
)
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `FirstPurchaseDate` field:

```csharp
.SortBy(c => c.FirstPurchaseDate)
.As<BsonDocument>();
```

The preceding code also converts the output documents to
`BsonDocument` instances for printing.

**Step 5: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "CustomerId" : "oranieri@warmmail.com", "FirstPurchaseDate" : { "$date" : "2020-01-01T08:25:37Z" }, "TotalValue" : 63, "TotalOrders" : 1, "Orders" : [{ "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63 }] }
{ "CustomerId" : "elise_smith@myemail.com", "FirstPurchaseDate" : { "$date" : "2020-01-13T09:32:07Z" }, "TotalValue" : 436, "TotalOrders" : 4, "Orders" : [{ "OrderDate" : { "$date" : "2020-01-13T09:32:07Z" }, "Value" : 99 }, { "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 231 }, { "OrderDate" : { "$date" : "2020-10-03T13:49:44Z" }, "Value" : 102 }, { "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 4 }] }
{ "CustomerId" : "tj@wheresmyemail.com", "FirstPurchaseDate" : { "$date" : "2020-08-18T23:04:48Z" }, "TotalValue" : 191, "TotalOrders" : 2, "Orders" : [{ "OrderDate" : { "$date" : "2020-08-18T23:04:48Z" }, "Value" : 4 }, { "OrderDate" : { "$date" : "2020-11-23T22:56:53Z" }, "Value" : 187 }] }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**c:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```c
mongoc_collection_t *orders = mongoc_client_get_collection(client, "agg_tutorials_db", "orders");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(orders, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 9;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1590825352000UL), // 2020-05-30T08:35:52Z
        "value", BCON_INT32(231));

    docs[1] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1578904327000UL), // 2020-01-13T09:32:07Z
        "value", BCON_INT32(99));

    docs[2] = BCON_NEW(
        "customer_id", BCON_UTF8("oranieri@warmmail.com"),
        "orderdate", BCON_DATE_TIME(1577865937000UL), // 2020-01-01T08:25:37Z
        "value", BCON_INT32(63));

    docs[3] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1559061212000UL), // 2019-05-28T19:13:32Z
        "value", BCON_INT32(2));

    docs[4] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1606171013000UL), // 2020-11-23T22:56:53Z
        "value", BCON_INT32(187));

    docs[5] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1597793088000UL), // 2020-08-18T23:04:48Z
        "value", BCON_INT32(4));

    docs[6] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1608963346000UL), // 2020-12-26T08:55:46Z
        "value", BCON_INT32(4));

    docs[7] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1614496172000UL), // 2021-02-28T07:49:32Z
        "value", BCON_INT32(1024));

    docs[8] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1601722184000UL), // 2020-10-03T13:49:44Z
        "value", BCON_INT32(102));

    bson_error_t error;
    if (!mongoc_collection_insert_many(orders, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(docs[i]);
    }
}
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches orders placed
in 2020:

```c
"{", "$match", "{",
"orderdate", "{",
"$gte", BCON_DATE_TIME(1577836800000UL), // Represents 2020-01-01T00:00:00Z
"$lt", BCON_DATE_TIME(1609459200000UL),  // Represents 2021-01-01T00:00:00Z
"}",
"}", "}",
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```c
"{", "$sort", "{", "orderdate", BCON_INT32(1), "}", "}",
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

```c
"{", "$group", "{",
"_id", BCON_UTF8("$customer_id"),
"first_purchase_date", "{", "$first", BCON_UTF8("$orderdate"), "}",
"total_value", "{", "$sum", BCON_UTF8("$value"), "}",
"total_orders", "{", "$sum", BCON_INT32(1), "}",
"orders", "{", "$push", "{",
"orderdate", BCON_UTF8("$orderdate"),
"value", BCON_UTF8("$value"),
"}", "}",
"}", "}",
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```c
"{", "$sort", "{", "first_purchase_date", BCON_INT32(1), "}", "}",
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```c
"{", "$set", "{", "customer_id", BCON_UTF8("$_id"), "}", "}",
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), "]", "}",
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(orders, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(orders);
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

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "first_purchase_date" : { "$date" : { "$numberLong" : "1577865937000" } }, "total_value" : { "$numberInt" : "63" }, "total_orders" : { "$numberInt" : "1" }, "orders" : [ { "orderdate" : { "$date" : { "$numberLong" : "1577865937000" } }, "value" : { "$numberInt" : "63" } } ], "customer_id" : "oranieri@warmmail.com" }
{ "first_purchase_date" : { "$date" : { "$numberLong" : "1578904327000" } }, "total_value" : { "$numberInt" : "436" }, "total_orders" : { "$numberInt" : "4" }, "orders" : [ { "orderdate" : { "$date" : { "$numberLong" : "1578904327000" } }, "value" : { "$numberInt" : "99" } }, { "orderdate" : { "$date" : { "$numberLong" : "1590825352000" } }, "value" : { "$numberInt" : "231" } }, { "orderdate" : { "$date" : { "$numberLong" : "1601722184000" } }, "value" : { "$numberInt" : "102" } }, { "orderdate" : { "$date" : { "$numberLong" : "1608963346000" } }, "value" : { "$numberInt" : "4" } } ], "customer_id" : "elise_smith@myemail.com" }
{ "first_purchase_date" : { "$date" : { "$numberLong" : "1597793088000" } }, "total_value" : { "$numberInt" : "191" }, "total_orders" : { "$numberInt" : "2" }, "orders" : [ { "orderdate" : { "$date" : { "$numberLong" : "1597793088000" } }, "value" : { "$numberInt" : "4" } }, { "orderdate" : { "$date" : { "$numberLong" : "1606171013000" } }, "value" : { "$numberInt" : "187" } } ], "customer_id" : "tj@wheresmyemail.com" }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**cpp:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```cpp
auto orders = db["orders"];

std::vector<bsoncxx::document::value> docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "value": 231
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1578901927},
        "value": 99
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137},
        "value": 63
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559076812},
        "value": 2
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1606172213},
        "value": 187
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1597794288},
        "value": 4
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1608972946000},
        "value": 4
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1614570572},
        "value": 1024
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1601722184000},
        "value": 102
    })")
};

auto result = orders.insert_many(docs); // Might throw an exception
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orderdate": {
        "$gte": {"$date": 1577836800},
        "$lt": {"$date": 1609459200000}
    }
})"));
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "orderdate": 1
})"));
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

```cpp
pipeline.group(bsoncxx::from_json(R"({
    "_id": "$customer_id",
    "first_purchase_date": {"$first": "$orderdate"},
    "total_value": {"$sum": "$value"},
    "total_orders": {"$sum": 1},
    "orders": {"$push": {
        "orderdate": "$orderdate",
        "value": "$value"
    }}
})"));
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "first_purchase_date": 1
})"));
```

**Step 5: Add an addFields stage to display the email address.**

Add an `$addFields` stage,
an alias for the `$set` stage, to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "customer_id": "$_id"
})"));
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id"]
})"));
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```cpp
auto cursor = orders.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "first_purchase_date" : { "$date" : "1970-01-19T06:17:41.137Z" }, "total_value" : 63,
"total_orders" : 1, "orders" : [ { "orderdate" : { "$date" : "1970-01-19T06:17:41.137Z" },
"value" : 63 } ], "customer_id" : "oranieri@warmmail.com" }
{ "first_purchase_date" : { "$date" : "1970-01-19T06:35:01.927Z" }, "total_value" : 436,
"total_orders" : 4, "orders" : [ { "orderdate" : { "$date" : "1970-01-19T06:35:01.927Z" },
"value" : 99 }, { "orderdate" : { "$date" : "2020-05-30T06:55:52Z" }, "value" : 231 },
{ "orderdate" : { "$date" : "2020-10-03T10:49:44Z" }, "value" : 102 }, { "orderdate" :
{ "$date" : "2020-12-26T08:55:46Z" }, "value" : 4 } ], "customer_id" : "elise_smith@myemail.com" }
{ "first_purchase_date" : { "$date" : "1970-01-19T11:49:54.288Z" }, "total_value" : 1215,
"total_orders" : 3, "orders" : [ { "orderdate" : { "$date" : "1970-01-19T11:49:54.288Z" },
"value" : 4 }, { "orderdate" : { "$date" : "1970-01-19T14:09:32.213Z" }, "value" : 187 },
{ "orderdate" : { "$date" : "1970-01-19T16:29:30.572Z" }, "value" : 1024 } ], "customer_id" : "tj@wheresmyemail.com" }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**nodejs:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```javascript
const orders = aggDB.collection("orders");
await orders.deleteMany({});

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    value: 231,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-01-13T09:32:07Z"),
    value: 99,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    value: 63,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    value: 2,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2020-11-23T22:56:53Z"),
    value: 187,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2020-08-18T23:04:48Z"),
    value: 4,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    value: 4,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2021-02-29T07:49:32Z"),
    value: 1024,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-10-03T13:49:44Z"),
    value: 102,
  },
]);
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```javascript
pipeline.push({
  $match: {
    orderdate: {
      $gte: new Date("2020-01-01T00:00:00Z"),
      $lt: new Date("2021-01-01T00:00:00Z"),
    },
  },
});
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```javascript
pipeline.push({
  $sort: {
    orderdate: 1,
  },
});
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to group
orders by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```javascript
pipeline.push({
  $group: {
    _id: "$customer_id",
    first_purchase_date: { $first: "$orderdate" },
    total_value: { $sum: "$value" },
    total_orders: { $sum: 1 },
    orders: {
      $push: {
        orderdate: "$orderdate",
        value: "$value",
      },
    },
  },
});
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```javascript
pipeline.push({
  $sort: {
    first_purchase_date: 1,
  },
});
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```javascript
pipeline.push({
  $set: {
    customer_id: "$_id",
  },
});
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```javascript
pipeline.push({ $unset: ["_id"] });
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```javascript
const aggregationResult = await orders.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  first_purchase_date: 2020-01-01T08:25:37.000Z,
  total_value: 63,
  total_orders: 1,
  orders: [ { orderdate: 2020-01-01T08:25:37.000Z, value: 63 } ],
  customer_id: 'oranieri@warmmail.com'
}
{
  first_purchase_date: 2020-01-13T09:32:07.000Z,
  total_value: 436,
  total_orders: 4,
  orders: [
    { orderdate: 2020-01-13T09:32:07.000Z, value: 99 },
    { orderdate: 2020-05-30T08:35:52.000Z, value: 231 },
    { orderdate: 2020-10-03T13:49:44.000Z, value: 102 },
    { orderdate: 2020-12-26T08:55:46.000Z, value: 4 }
  ],
  customer_id: 'elise_smith@myemail.com'
}
{
  first_purchase_date: 2020-08-18T23:04:48.000Z,
  total_value: 191,
  total_orders: 2,
  orders: [
    { orderdate: 2020-08-18T23:04:48.000Z, value: 4 },
    { orderdate: 2020-11-23T22:56:53.000Z, value: 187 }
  ],
  customer_id: 'tj@wheresmyemail.com'
}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**php:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$orders->deleteMany([]);

$orders->insertMany(
    [
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-05-30T08:35:52')),
            'value' => 231
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-13T09:32:07')),
            'value' => 99
        ],
        [
            'customer_id' => 'oranieri@warmmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-01T08:25:37')),
            'value' => 63
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2019-05-28T19:13:32')),
            'value' => 2
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-11-23T22:56:53')),
            'value' => 187
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-08-18T23:04:48')),
            'value' => 4
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-12-26T08:55:46')),
            'value' => 4
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2021-02-28T07:49:32')),
            'value' => 1024
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-10-03T13:49:44')),
            'value' => 102
        ]
    ]
);
```

**Step 1: Add a match stage for orders in 2020.**

In your `Pipeline` instance, add a `$match` stage that matches
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```php
Stage::sort(orderdate: Sort::Asc),
```

**Step 3: Add a group stage to group by email address.**

Outside of your `Pipeline` instance, create a `$group` stage in a factory
function to collect order documents by the value of the
`customer_id` field. In this stage, add aggregation operations
that create the following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```php
function groupByCustomerStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('customer_id'),
        first_purchase_date: Accumulator::first(
            Expression::arrayFieldPath('orderdate')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('value'),
        ),
        total_orders: Accumulator::sum(1),
        orders: Accumulator::push(
            object(
                orderdate: Expression::dateFieldPath('orderdate'),
                value: Expression::numberFieldPath('value'),
            ),
        ),
    );
}
```

Then, in your `Pipeline` instance, call the
`groupByCustomerStage()` function:

```php
function groupByCustomerStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('customer_id'),
        first_purchase_date: Accumulator::first(
            Expression::arrayFieldPath('orderdate')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('value'),
        ),
        total_orders: Accumulator::sum(1),
        orders: Accumulator::push(
            object(
                orderdate: Expression::dateFieldPath('orderdate'),
                value: Expression::numberFieldPath('value'),
            ),
        ),
    );
}
```

**Step 4: Add a sort stage to sort by first order date.**

Next, create another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```php
Stage::sort(first_purchase_date: Sort::Asc),
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```php
Stage::set(customer_id: Expression::stringFieldPath('_id')),
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```php
Stage::unset('_id')
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```php
$cursor = $orders->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1577867137000"
        }
    },
    "total_value": 63,
    "total_orders": 1,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1577867137000"
                }
            },
            "value": 63
        }
    ],
    "customer_id": "oranieri@warmmail.com"
}
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1578907927000"
        }
    },
    "total_value": 436,
    "total_orders": 4,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1578907927000"
                }
            },
            "value": 99
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1590827752000"
                }
            },
            "value": 231
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1601732984000"
                }
            },
            "value": 102
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1608972946000"
                }
            },
            "value": 4
        }
    ],
    "customer_id": "elise_smith@myemail.com"
}
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1597791888000"
        }
    },
    "total_value": 191,
    "total_orders": 2,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1597791888000"
                }
            },
            "value": 4
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1606172213000"
                }
            },
            "value": 187
        }
    ],
    "customer_id": "tj@wheresmyemail.com"
}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**ruby:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```ruby
orders = agg_db[:orders]
orders.delete_many({})

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      value: 231,

    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-01-13T09:32:07Z"),
      value: 99,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      value: 63,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      value: 2,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2020-11-23T22:56:53Z"),
      value: 187,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2020-08-18T23:04:48Z"),
      value: 4,
    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      value: 4,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2021-02-28T07:49:32Z"),
      value: 1024,
    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-10-03T13:49:44Z"),
      value: 102,
    },
  ]
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```ruby
{
  "$match": {
    orderdate: {
      "$gte": DateTime.parse("2020-01-01T00:00:00Z"),
      "$lt": DateTime.parse("2021-01-01T00:00:00Z"),
    },
  },
},
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```ruby
{
  "$sort": {
    orderdate: 1,
  },
},
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

```ruby
{
  "$group": {
    _id: "$customer_id",
    first_purchase_date: { "$first": "$orderdate" },
    total_value: { "$sum": "$value" },
    total_orders: { "$sum": 1 },
    orders: { "$push": {
      orderdate: "$orderdate",
      value: "$value",
    } },
  },
},
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```ruby
{
  "$sort": {
    first_purchase_date: 1,
  },
},
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```ruby
{
  "$set": {
    customer_id: "$_id",
  },
},
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```ruby
{ "$unset": ["_id"] },
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```ruby
aggregation_result = orders.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
ruby agg_tutorial.rb
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date"=>2020-01-01 08:25:37 UTC, "total_value"=>63, "total_orders"=>1, "orders"=>[{"orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63}], "customer_id"=>"oranieri@warmmail.com"}
{"first_purchase_date"=>2020-01-13 09:32:07 UTC, "total_value"=>436, "total_orders"=>4, "orders"=>[{"orderdate"=>2020-01-13 09:32:07 UTC, "value"=>99}, {"orderdate"=>2020-05-30 08:35:52 UTC, "value"=>231}, {"orderdate"=>2020-10-03 13:49:44 UTC, "value"=>102}, {"orderdate"=>2020-12-26 08:55:46 UTC, "value"=>4}], "customer_id"=>"elise_smith@myemail.com"}
{"first_purchase_date"=>2020-08-18 23:04:48 UTC, "total_value"=>191, "total_orders"=>2, "orders"=>[{"orderdate"=>2020-08-18 23:04:48 UTC, "value"=>4}, {"orderdate"=>2020-11-23 22:56:53 UTC, "value"=>187}], "customer_id"=>"tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**go:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

First, create a Go struct to model the data in the `orders`
collection:

```go
type Order struct {
	CustomerID string        `bson:"customer_id,omitempty"`
	OrderDate  bson.DateTime `bson:"orderdate"`
	Value      int           `bson:"value"`
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```go
orders := aggDB.Collection("orders")
orders.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 53, 0, time.UTC)),
		Value:      231,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 1, 13, 9, 32, 7, 0, time.UTC)),
		Value:      99,
	},
	Order{
		CustomerID: "oranieri@warmmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 1, 01, 8, 25, 37, 0, time.UTC)),
		Value:      63,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		Value:      2,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 11, 23, 22, 56, 53, 0, time.UTC)),
		Value:      187,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 8, 18, 23, 4, 48, 0, time.UTC)),
		Value:      4,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		Value:      4,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2021, 2, 29, 7, 49, 32, 0, time.UTC)),
		Value:      1024,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 10, 3, 13, 49, 44, 0, time.UTC)),
		Value:      102,
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "orderdate", Value: bson.D{
		{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
		{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
	}},
}}}
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```go
sortStage1 := bson.D{{Key: "$sort", Value: bson.D{
	{Key: "orderdate", Value: 1},
}}}
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

```go
groupStage := bson.D{{Key: "$group", Value: bson.D{
	{Key: "_id", Value: "$customer_id"},
	{Key: "first_purchase_date", Value: bson.D{{Key: "$first", Value: "$orderdate"}}},
	{Key: "total_value", Value: bson.D{{Key: "$sum", Value: "$value"}}},
	{Key: "total_orders", Value: bson.D{{Key: "$sum", Value: 1}}},
	{Key: "orders", Value: bson.D{{Key: "$push", Value: bson.D{
		{Key: "orderdate", Value: "$orderdate"},
		{Key: "value", Value: "$value"},
	}}}},
}}}
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```go
sortStage2 := bson.D{{Key: "$sort", Value: bson.D{
	{Key: "first_purchase_date", Value: 1},
}}}
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```go
setStage := bson.D{{Key: "$set", Value: bson.D{
	{Key: "customer_id", Value: "$_id"},
}}}
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id"}}}
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{matchStage, sortStage1, groupStage, setStage, sortStage2, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date":{"$date":"2020-01-01T08:25:37Z"},"total_value":63,"total_orders":1,"orders":[{"orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63}],"customer_id":"oranieri@warmmail.com"}
{"first_purchase_date":{"$date":"2020-01-13T09:32:07Z"},"total_value":436,"total_orders":4,"orders":[{"orderdate":{"$date":"2020-01-13T09:32:07Z"},"value":99},{"orderdate":{"$date":"2020-05-30T08:35:53Z"},"value":231},{"orderdate":{"$date":"2020-10-03T13:49:44Z"},"value":102},{"orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":4}],"customer_id":"elise_smith@myemail.com"}
{"first_purchase_date":{"$date":"2020-08-18T23:04:48Z"},"total_value":191,"total_orders":2,"orders":[{"orderdate":{"$date":"2020-08-18T23:04:48Z"},"value":4},{"orderdate":{"$date":"2020-11-23T22:56:53Z"},"value":187}],"customer_id":"tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**rust:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

First, create a Rust struct to model the data in the `orders`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    orderdate: DateTime,
    value: i32,
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```rust
let orders: Collection<Order> = agg_db.collection("orders");
orders.delete_many(doc! {}).await?;

let docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(53).build().unwrap(),
        value: 231,
    },
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(1).day(13).hour(9).minute(32).second(7).build().unwrap(),
        value: 99,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        value: 63,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        value: 2,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(11).day(23).hour(22).minute(56).second(53).build().unwrap(),
        value: 187,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(8).day(18).hour(23).minute(4).second(48).build().unwrap(),
        value: 4,
    },
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        value: 4,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2021).month(2).day(28).hour(7).minute(49).second(32).build().unwrap(),
        value: 1024,
    },
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(10).day(3).hour(13).minute(49).second(44).build().unwrap(),
        value: 102,
    },
];

orders.insert_many(docs).await?;
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```rust
pipeline.push(doc! {
    "$match": {
        "orderdate": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap(),
        }
    }
});
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```rust
pipeline.push(doc! {
    "$sort": {
        "orderdate": 1
    }
});
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

```rust
pipeline.push(doc! {
    "$group": {
        "_id": "$customer_id",
        "first_purchase_date": { "$first": "$orderdate" },
        "total_value": { "$sum": "$value" },
        "total_orders": { "$sum": 1 },
        "orders": {
            "$push": {
                "orderdate": "$orderdate",
                "value": "$value"
            }
        }
    }
});
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```rust
pipeline.push(doc! {
    "$sort": {
        "first_purchase_date": 1
    }
});
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```rust
pipeline.push(doc! {
    "$set": {
        "customer_id": "$_id"
    }
});
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```rust
pipeline.push(doc! {"$unset": ["_id"] });
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```rust
let mut cursor = orders.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document({"first_purchase_date": DateTime(2020-01-01 8:25:37.0 +00:00:00), "total_value": Int32(63), "total_orders": Int32(1),
"orders": Array([Document({"orderdate": DateTime(2020-01-01 8:25:37.0 +00:00:00), "value": Int32(63)})]), "customer_id": String("oranieri@warmmail.com")})

Document({"first_purchase_date": DateTime(2020-01-13 9:32:07.0 +00:00:00), "total_value": Int32(436), "total_orders": Int32(4),
"orders": Array([Document({"orderdate": DateTime(2020-01-13 9:32:07.0 +00:00:00), "value": Int32(99)}), Document({"orderdate":
DateTime(2020-05-30 8:35:53.0 +00:00:00), "value": Int32(231)}), Document({"orderdate": DateTime(2020-10-03 13:49:44.0 +00:00:00),
"value": Int32(102)}), Document({"orderdate": DateTime(2020-12-26 8:55:46.0 +00:00:00), "value": Int32(4)})]), "customer_id": String("elise_smith@myemail.com")})

Document({"first_purchase_date": DateTime(2020-08-18 23:04:48.0 +00:00:00), "total_value": Int32(191), "total_orders": Int32(2),
"orders": Array([Document({"orderdate": DateTime(2020-08-18 23:04:48.0 +00:00:00), "value": Int32(4)}), Document({"orderdate":
DateTime(2020-11-23 22:56:53.0 +00:00:00), "value": Int32(187)})]), "customer_id": String("tj@wheresmyemail.com")})
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to group documents and compute new fields.

**shell:**

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-05-30T08:35:52Z"),
      value: 231,
   },
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-01-13T09:32:07Z"),
      value: 99,
   },
   {
      customer_id: "oranieri@warmmail.com",
      orderdate: new Date("2020-01-01T08:25:37Z"),
      value: 63,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2019-05-28T19:13:32Z"),
      value: 2,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2020-11-23T22:56:53Z"),
      value: 187,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2020-08-18T23:04:48Z"),
      value: 4,
   },
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-12-26T08:55:46Z"),
      value: 4,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2021-02-29T07:49:32Z"),
      value: 1024,
   },
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-10-03T13:49:44Z"),
      value: 102,
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [
   // Stage 1: Match orders in 2020
   { $match: {
      orderdate: {
         $gte: new Date("2020-01-01T00:00:00Z"),
         $lt: new Date("2021-01-01T00:00:00Z"),
      }
   } },

   // Stage 2: Sort orders by date
   { $sort: { orderdate: 1 } },

   // Stage 3: Group orders by email address
   { $group: {
      _id: "$customer_id",
      first_purchase_date: { $first: "$orderdate" },
      total_value: { $sum: "$value" },
      total_orders: { $sum: 1 },
      orders: { $push: 
         { 
            orderdate: "$orderdate", 
            value: "$value" 
         }
      }
   } },

   // Stage 4: Sort orders by first order date
   { $sort: { first_purchase_date: 1 } },

   // Stage 5: Display the customers' email addresses
   { $set: { customer_id: "$_id" } },

   // Stage 6: Remove unneeded fields
   { $unset: ["_id"] }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020. The result documents contain details on all orders
placed by a given customer, grouped by the customer's email
address.

```javascript
{
   first_purchase_date: ISODate("2020-01-01T08:25:37.000Z"),
   total_value: 63,
   total_orders: 1,
   orders: [ { orderdate: ISODate("2020-01-01T08:25:37.000Z"), value: 63 } ],
   customer_id: 'oranieri@warmmail.com'
}
{
   first_purchase_date: ISODate("2020-01-13T09:32:07.000Z"),
   total_value: 436,
   total_orders: 4,
   orders: [
      { orderdate: ISODate("2020-01-13T09:32:07.000Z"), value: 99 },
      { orderdate: ISODate("2020-05-30T08:35:52.000Z"), value: 231 },
      { orderdate: ISODate("2020-10-03T13:49:44.000Z"), value: 102 },
      { orderdate: ISODate("2020-12-26T08:55:46.000Z"), value: 4 }
   ],
   customer_id: 'elise_smith@myemail.com'
}
{
   first_purchase_date: ISODate("2020-08-18T23:04:48.000Z"),
   total_value: 191,
   total_orders: 2,
   orders: [
      { orderdate: ISODate("2020-08-18T23:04:48.000Z"), value: 4 },
      { orderdate: ISODate("2020-11-23T22:56:53.000Z"), value: 187 }
   ],
   customer_id: 'tj@wheresmyemail.com'
}
```

**python:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```python
orders_coll = agg_db["orders"]
orders_coll.delete_many({})

order_data = [
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 5, 30, 8, 35, 52),
        "value": 231,
    },
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 1, 13, 9, 32, 7),
        "value": 99,
    },
    {
        "customer_id": "oranieri@warmmail.com",
        "orderdate": datetime(2020, 1, 1, 8, 25, 37),
        "value": 63,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2019, 5, 28, 19, 13, 32),
        "value": 2,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2020, 11, 23, 22, 56, 53),
        "value": 187,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2020, 8, 18, 23, 4, 48),
        "value": 4,
    },
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 12, 26, 8, 55, 46),
        "value": 4,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2021, 2, 28, 7, 49, 32),
        "value": 1024,
    },
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 10, 3, 13, 49, 44),
        "value": 102,
    },
]

orders_coll.insert_many(order_data)
```

**Step 1: Add a match stage for orders in 2020.**

In your `Pipeline` instance, add a `$match` stage that matches
orders placed in 2020:

```python
pipeline.append(
    {
        "$match": {
            "orderdate": {
                "$gte": datetime(2020, 1, 1, 0, 0, 0),
                "$lt": datetime(2021, 1, 1, 0, 0, 0),
            }
        }
    }
)
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```python
pipeline.append({"$sort": {"orderdate": 1}})
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to group
orders by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```python
pipeline.append(
    {
        "$group": {
            "_id": "$customer_id",
            "first_purchase_date": {"$first": "$orderdate"},
            "total_value": {"$sum": "$value"},
            "total_orders": {"$sum": 1},
            "orders": {"$push": {"orderdate": "$orderdate", "value": "$value"}},
        }
    }
)
```

**Step 4: Add a sort stage to sort by first order date.**

Next, create another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```python
pipeline.append({"$sort": {"first_purchase_date": 1}})
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```python
pipeline.append({"$set": {"customer_id": "$_id"}})
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```python
pipeline.append({"$unset": ["_id"]})
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```python
aggregation_result = orders_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{'first_purchase_date': datetime.datetime(2020, 1, 1, 8, 25, 37), 'total_value': 63, 'total_orders': 1, 'orders': [{'orderdate': datetime.datetime(2020, 1, 1, 8, 25, 37), 'value': 63}], 'customer_id': 'oranieri@warmmail.com'}
{'first_purchase_date': datetime.datetime(2020, 1, 13, 9, 32, 7), 'total_value': 436, 'total_orders': 4, 'orders': [{'orderdate': datetime.datetime(2020, 1, 13, 9, 32, 7), 'value': 99}, {'orderdate': datetime.datetime(2020, 5, 30, 8, 35, 52), 'value': 231}, {'orderdate': datetime.datetime(2020, 10, 3, 13, 49, 44), 'value': 102}, {'orderdate': datetime.datetime(2020, 12, 26, 8, 55, 46), 'value': 4}], 'customer_id': 'elise_smith@myemail.com'}
{'first_purchase_date': datetime.datetime(2020, 8, 18, 23, 4, 48), 'total_value': 191, 'total_orders': 2, 'orders': [{'orderdate': datetime.datetime(2020, 8, 18, 23, 4, 48), 'value': 4}, {'orderdate': datetime.datetime(2020, 11, 23, 22, 56, 53), 'value': 187}], 'customer_id': 'tj@wheresmyemail.com'}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**java-sync:**

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

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```scala
val orders = aggDB.getCollection("orders")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

orders.insertMany(Seq(
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
    "value" -> 231),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-01-13T09:32:07"),
    "value" -> 99),
  Document("customer_id" -> "oranieri@warmmail.com",
    "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
    "value" -> 63),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
    "value" -> 2),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2020-11-23T22:56:53"),
    "value" -> 187),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2020-08-18T23:04:48"),
    "value" -> 4),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
    "value" -> 4),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2021-02-28T07:49:32"),
    "value" -> 1024),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-10-03T13:49:44"),
    "value" -> 102)
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```scala
Aggregates.filter(Filters.and(
  Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
  Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
)),
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```scala
Aggregates.sort(Sorts.ascending("orderdate")),
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

```scala
Aggregates.group(
  "$customer_id",
  Accumulators.first("first_purchase_date", "$orderdate"),
  Accumulators.sum("total_value", "$value"),
  Accumulators.sum("total_orders", 1),
  Accumulators.push("orders", Document("orderdate" -> "$orderdate", "value" -> "$value"))
),
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```scala
Aggregates.sort(Sorts.ascending("first_purchase_date")),
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```scala
Aggregates.set(Field("customer_id", "$_id")),
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```scala
Aggregates.unset("_id")
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date": {"$date": "2020-01-01T13:25:37Z"}, "total_value": 63, "total_orders": 1, "orders": [{"orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63}], "customer_id": "oranieri@warmmail.com"}
{"first_purchase_date": {"$date": "2020-01-13T14:32:07Z"}, "total_value": 436, "total_orders": 4, "orders": [{"orderdate": {"$date": "2020-01-13T14:32:07Z"}, "value": 99}, {"orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 231}, {"orderdate": {"$date": "2020-10-03T17:49:44Z"}, "value": 102}, {"orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 4}], "customer_id": "elise_smith@myemail.com"}
{"first_purchase_date": {"$date": "2020-08-19T03:04:48Z"}, "total_value": 191, "total_orders": 2, "orders": [{"orderdate": {"$date": "2020-08-19T03:04:48Z"}, "value": 4}, {"orderdate": {"$date": "2020-11-24T03:56:53Z"}, "value": 187}], "customer_id": "tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**csharp:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `CustomerId`
field, which contains customer email addresses.

First, create a C# class to model the data in the `orders`
collection:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public int Value { get; set; }
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```csharp
var orders = aggDB.GetCollection<Order>("orders");
orders.DeleteMany(Builders<Order>.Filter.Empty);

orders.InsertMany(new List<Order>
    {
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
            Value = 231
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-01-13T09:32:07Z"),
            Value = 99
        },
        new Order
        {
            CustomerId = "oranieri@warmmail.com",
            OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
            Value = 63
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
            Value = 2
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2020-11-23T22:56:53Z"),
            Value = 187
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2020-08-18T23:04:48Z"),
            Value = 4
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
            Value = 4
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2021-02-28T07:49:32Z"),
            Value = 1024
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-10-03T13:49:44Z"),
            Value = 102
        }
    });
```

**Step 1: Add a match stage for orders in 2020.**

First, start the aggregation on the `orders` collection and
chain a `$match` stage that matches orders placed in
2020:

```csharp
var results = orders.Aggregate()
    .Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
                o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `OrderDate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```csharp
.SortBy(o => o.OrderDate)
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to collect
order documents by the value of the `CustomerId` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `CustomerId`: the customer's email address (the grouping key)
- `FirstPurchaseDate`: the date of the customer's first purchase
- `TotalValue`: the total value of all the customer's purchases
- `TotalOrders`: the total number of the customer's purchases
- `Orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```csharp
.Group(
    o => o.CustomerId,
    g => new
    {
      CustomerId = g.Key,
      FirstPurchaseDate = g.First().OrderDate,
      TotalValue = g.Sum(i => i.Value),
      TotalOrders = g.Count(),
      Orders = g.Select(i => new { i.OrderDate, i.Value }).ToList()
    }
)
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `FirstPurchaseDate` field:

```csharp
.SortBy(c => c.FirstPurchaseDate)
.As<BsonDocument>();
```

The preceding code also converts the output documents to
`BsonDocument` instances for printing.

**Step 5: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "CustomerId" : "oranieri@warmmail.com", "FirstPurchaseDate" : { "$date" : "2020-01-01T08:25:37Z" }, "TotalValue" : 63, "TotalOrders" : 1, "Orders" : [{ "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63 }] }
{ "CustomerId" : "elise_smith@myemail.com", "FirstPurchaseDate" : { "$date" : "2020-01-13T09:32:07Z" }, "TotalValue" : 436, "TotalOrders" : 4, "Orders" : [{ "OrderDate" : { "$date" : "2020-01-13T09:32:07Z" }, "Value" : 99 }, { "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 231 }, { "OrderDate" : { "$date" : "2020-10-03T13:49:44Z" }, "Value" : 102 }, { "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 4 }] }
{ "CustomerId" : "tj@wheresmyemail.com", "FirstPurchaseDate" : { "$date" : "2020-08-18T23:04:48Z" }, "TotalValue" : 191, "TotalOrders" : 2, "Orders" : [{ "OrderDate" : { "$date" : "2020-08-18T23:04:48Z" }, "Value" : 4 }, { "OrderDate" : { "$date" : "2020-11-23T22:56:53Z" }, "Value" : 187 }] }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**c:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```c
mongoc_collection_t *orders = mongoc_client_get_collection(client, "agg_tutorials_db", "orders");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(orders, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 9;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1590825352000UL), // 2020-05-30T08:35:52Z
        "value", BCON_INT32(231));

    docs[1] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1578904327000UL), // 2020-01-13T09:32:07Z
        "value", BCON_INT32(99));

    docs[2] = BCON_NEW(
        "customer_id", BCON_UTF8("oranieri@warmmail.com"),
        "orderdate", BCON_DATE_TIME(1577865937000UL), // 2020-01-01T08:25:37Z
        "value", BCON_INT32(63));

    docs[3] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1559061212000UL), // 2019-05-28T19:13:32Z
        "value", BCON_INT32(2));

    docs[4] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1606171013000UL), // 2020-11-23T22:56:53Z
        "value", BCON_INT32(187));

    docs[5] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1597793088000UL), // 2020-08-18T23:04:48Z
        "value", BCON_INT32(4));

    docs[6] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1608963346000UL), // 2020-12-26T08:55:46Z
        "value", BCON_INT32(4));

    docs[7] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1614496172000UL), // 2021-02-28T07:49:32Z
        "value", BCON_INT32(1024));

    docs[8] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1601722184000UL), // 2020-10-03T13:49:44Z
        "value", BCON_INT32(102));

    bson_error_t error;
    if (!mongoc_collection_insert_many(orders, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(docs[i]);
    }
}
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches orders placed
in 2020:

```c
"{", "$match", "{",
"orderdate", "{",
"$gte", BCON_DATE_TIME(1577836800000UL), // Represents 2020-01-01T00:00:00Z
"$lt", BCON_DATE_TIME(1609459200000UL),  // Represents 2021-01-01T00:00:00Z
"}",
"}", "}",
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```c
"{", "$sort", "{", "orderdate", BCON_INT32(1), "}", "}",
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

```c
"{", "$group", "{",
"_id", BCON_UTF8("$customer_id"),
"first_purchase_date", "{", "$first", BCON_UTF8("$orderdate"), "}",
"total_value", "{", "$sum", BCON_UTF8("$value"), "}",
"total_orders", "{", "$sum", BCON_INT32(1), "}",
"orders", "{", "$push", "{",
"orderdate", BCON_UTF8("$orderdate"),
"value", BCON_UTF8("$value"),
"}", "}",
"}", "}",
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```c
"{", "$sort", "{", "first_purchase_date", BCON_INT32(1), "}", "}",
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```c
"{", "$set", "{", "customer_id", BCON_UTF8("$_id"), "}", "}",
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), "]", "}",
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(orders, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(orders);
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

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "first_purchase_date" : { "$date" : { "$numberLong" : "1577865937000" } }, "total_value" : { "$numberInt" : "63" }, "total_orders" : { "$numberInt" : "1" }, "orders" : [ { "orderdate" : { "$date" : { "$numberLong" : "1577865937000" } }, "value" : { "$numberInt" : "63" } } ], "customer_id" : "oranieri@warmmail.com" }
{ "first_purchase_date" : { "$date" : { "$numberLong" : "1578904327000" } }, "total_value" : { "$numberInt" : "436" }, "total_orders" : { "$numberInt" : "4" }, "orders" : [ { "orderdate" : { "$date" : { "$numberLong" : "1578904327000" } }, "value" : { "$numberInt" : "99" } }, { "orderdate" : { "$date" : { "$numberLong" : "1590825352000" } }, "value" : { "$numberInt" : "231" } }, { "orderdate" : { "$date" : { "$numberLong" : "1601722184000" } }, "value" : { "$numberInt" : "102" } }, { "orderdate" : { "$date" : { "$numberLong" : "1608963346000" } }, "value" : { "$numberInt" : "4" } } ], "customer_id" : "elise_smith@myemail.com" }
{ "first_purchase_date" : { "$date" : { "$numberLong" : "1597793088000" } }, "total_value" : { "$numberInt" : "191" }, "total_orders" : { "$numberInt" : "2" }, "orders" : [ { "orderdate" : { "$date" : { "$numberLong" : "1597793088000" } }, "value" : { "$numberInt" : "4" } }, { "orderdate" : { "$date" : { "$numberLong" : "1606171013000" } }, "value" : { "$numberInt" : "187" } } ], "customer_id" : "tj@wheresmyemail.com" }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**cpp:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```cpp
auto orders = db["orders"];

std::vector<bsoncxx::document::value> docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "value": 231
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1578901927},
        "value": 99
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137},
        "value": 63
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559076812},
        "value": 2
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1606172213},
        "value": 187
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1597794288},
        "value": 4
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1608972946000},
        "value": 4
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1614570572},
        "value": 1024
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1601722184000},
        "value": 102
    })")
};

auto result = orders.insert_many(docs); // Might throw an exception
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orderdate": {
        "$gte": {"$date": 1577836800},
        "$lt": {"$date": 1609459200000}
    }
})"));
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "orderdate": 1
})"));
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

```cpp
pipeline.group(bsoncxx::from_json(R"({
    "_id": "$customer_id",
    "first_purchase_date": {"$first": "$orderdate"},
    "total_value": {"$sum": "$value"},
    "total_orders": {"$sum": 1},
    "orders": {"$push": {
        "orderdate": "$orderdate",
        "value": "$value"
    }}
})"));
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "first_purchase_date": 1
})"));
```

**Step 5: Add an addFields stage to display the email address.**

Add an `$addFields` stage,
an alias for the `$set` stage, to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "customer_id": "$_id"
})"));
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id"]
})"));
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```cpp
auto cursor = orders.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "first_purchase_date" : { "$date" : "1970-01-19T06:17:41.137Z" }, "total_value" : 63,
"total_orders" : 1, "orders" : [ { "orderdate" : { "$date" : "1970-01-19T06:17:41.137Z" },
"value" : 63 } ], "customer_id" : "oranieri@warmmail.com" }
{ "first_purchase_date" : { "$date" : "1970-01-19T06:35:01.927Z" }, "total_value" : 436,
"total_orders" : 4, "orders" : [ { "orderdate" : { "$date" : "1970-01-19T06:35:01.927Z" },
"value" : 99 }, { "orderdate" : { "$date" : "2020-05-30T06:55:52Z" }, "value" : 231 },
{ "orderdate" : { "$date" : "2020-10-03T10:49:44Z" }, "value" : 102 }, { "orderdate" :
{ "$date" : "2020-12-26T08:55:46Z" }, "value" : 4 } ], "customer_id" : "elise_smith@myemail.com" }
{ "first_purchase_date" : { "$date" : "1970-01-19T11:49:54.288Z" }, "total_value" : 1215,
"total_orders" : 3, "orders" : [ { "orderdate" : { "$date" : "1970-01-19T11:49:54.288Z" },
"value" : 4 }, { "orderdate" : { "$date" : "1970-01-19T14:09:32.213Z" }, "value" : 187 },
{ "orderdate" : { "$date" : "1970-01-19T16:29:30.572Z" }, "value" : 1024 } ], "customer_id" : "tj@wheresmyemail.com" }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**nodejs:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```javascript
const orders = aggDB.collection("orders");
await orders.deleteMany({});

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    value: 231,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-01-13T09:32:07Z"),
    value: 99,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    value: 63,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    value: 2,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2020-11-23T22:56:53Z"),
    value: 187,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2020-08-18T23:04:48Z"),
    value: 4,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    value: 4,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2021-02-29T07:49:32Z"),
    value: 1024,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-10-03T13:49:44Z"),
    value: 102,
  },
]);
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```javascript
pipeline.push({
  $match: {
    orderdate: {
      $gte: new Date("2020-01-01T00:00:00Z"),
      $lt: new Date("2021-01-01T00:00:00Z"),
    },
  },
});
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```javascript
pipeline.push({
  $sort: {
    orderdate: 1,
  },
});
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to group
orders by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```javascript
pipeline.push({
  $group: {
    _id: "$customer_id",
    first_purchase_date: { $first: "$orderdate" },
    total_value: { $sum: "$value" },
    total_orders: { $sum: 1 },
    orders: {
      $push: {
        orderdate: "$orderdate",
        value: "$value",
      },
    },
  },
});
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```javascript
pipeline.push({
  $sort: {
    first_purchase_date: 1,
  },
});
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```javascript
pipeline.push({
  $set: {
    customer_id: "$_id",
  },
});
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```javascript
pipeline.push({ $unset: ["_id"] });
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```javascript
const aggregationResult = await orders.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  first_purchase_date: 2020-01-01T08:25:37.000Z,
  total_value: 63,
  total_orders: 1,
  orders: [ { orderdate: 2020-01-01T08:25:37.000Z, value: 63 } ],
  customer_id: 'oranieri@warmmail.com'
}
{
  first_purchase_date: 2020-01-13T09:32:07.000Z,
  total_value: 436,
  total_orders: 4,
  orders: [
    { orderdate: 2020-01-13T09:32:07.000Z, value: 99 },
    { orderdate: 2020-05-30T08:35:52.000Z, value: 231 },
    { orderdate: 2020-10-03T13:49:44.000Z, value: 102 },
    { orderdate: 2020-12-26T08:55:46.000Z, value: 4 }
  ],
  customer_id: 'elise_smith@myemail.com'
}
{
  first_purchase_date: 2020-08-18T23:04:48.000Z,
  total_value: 191,
  total_orders: 2,
  orders: [
    { orderdate: 2020-08-18T23:04:48.000Z, value: 4 },
    { orderdate: 2020-11-23T22:56:53.000Z, value: 187 }
  ],
  customer_id: 'tj@wheresmyemail.com'
}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**php:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$orders->deleteMany([]);

$orders->insertMany(
    [
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-05-30T08:35:52')),
            'value' => 231
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-13T09:32:07')),
            'value' => 99
        ],
        [
            'customer_id' => 'oranieri@warmmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-01T08:25:37')),
            'value' => 63
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2019-05-28T19:13:32')),
            'value' => 2
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-11-23T22:56:53')),
            'value' => 187
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-08-18T23:04:48')),
            'value' => 4
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-12-26T08:55:46')),
            'value' => 4
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2021-02-28T07:49:32')),
            'value' => 1024
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-10-03T13:49:44')),
            'value' => 102
        ]
    ]
);
```

**Step 1: Add a match stage for orders in 2020.**

In your `Pipeline` instance, add a `$match` stage that matches
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```php
Stage::sort(orderdate: Sort::Asc),
```

**Step 3: Add a group stage to group by email address.**

Outside of your `Pipeline` instance, create a `$group` stage in a factory
function to collect order documents by the value of the
`customer_id` field. In this stage, add aggregation operations
that create the following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```php
function groupByCustomerStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('customer_id'),
        first_purchase_date: Accumulator::first(
            Expression::arrayFieldPath('orderdate')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('value'),
        ),
        total_orders: Accumulator::sum(1),
        orders: Accumulator::push(
            object(
                orderdate: Expression::dateFieldPath('orderdate'),
                value: Expression::numberFieldPath('value'),
            ),
        ),
    );
}
```

Then, in your `Pipeline` instance, call the
`groupByCustomerStage()` function:

```php
function groupByCustomerStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('customer_id'),
        first_purchase_date: Accumulator::first(
            Expression::arrayFieldPath('orderdate')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('value'),
        ),
        total_orders: Accumulator::sum(1),
        orders: Accumulator::push(
            object(
                orderdate: Expression::dateFieldPath('orderdate'),
                value: Expression::numberFieldPath('value'),
            ),
        ),
    );
}
```

**Step 4: Add a sort stage to sort by first order date.**

Next, create another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```php
Stage::sort(first_purchase_date: Sort::Asc),
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```php
Stage::set(customer_id: Expression::stringFieldPath('_id')),
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```php
Stage::unset('_id')
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```php
$cursor = $orders->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1577867137000"
        }
    },
    "total_value": 63,
    "total_orders": 1,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1577867137000"
                }
            },
            "value": 63
        }
    ],
    "customer_id": "oranieri@warmmail.com"
}
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1578907927000"
        }
    },
    "total_value": 436,
    "total_orders": 4,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1578907927000"
                }
            },
            "value": 99
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1590827752000"
                }
            },
            "value": 231
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1601732984000"
                }
            },
            "value": 102
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1608972946000"
                }
            },
            "value": 4
        }
    ],
    "customer_id": "elise_smith@myemail.com"
}
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1597791888000"
        }
    },
    "total_value": 191,
    "total_orders": 2,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1597791888000"
                }
            },
            "value": 4
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1606172213000"
                }
            },
            "value": 187
        }
    ],
    "customer_id": "tj@wheresmyemail.com"
}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**ruby:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```ruby
orders = agg_db[:orders]
orders.delete_many({})

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      value: 231,

    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-01-13T09:32:07Z"),
      value: 99,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      value: 63,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      value: 2,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2020-11-23T22:56:53Z"),
      value: 187,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2020-08-18T23:04:48Z"),
      value: 4,
    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      value: 4,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2021-02-28T07:49:32Z"),
      value: 1024,
    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-10-03T13:49:44Z"),
      value: 102,
    },
  ]
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```ruby
{
  "$match": {
    orderdate: {
      "$gte": DateTime.parse("2020-01-01T00:00:00Z"),
      "$lt": DateTime.parse("2021-01-01T00:00:00Z"),
    },
  },
},
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```ruby
{
  "$sort": {
    orderdate: 1,
  },
},
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

```ruby
{
  "$group": {
    _id: "$customer_id",
    first_purchase_date: { "$first": "$orderdate" },
    total_value: { "$sum": "$value" },
    total_orders: { "$sum": 1 },
    orders: { "$push": {
      orderdate: "$orderdate",
      value: "$value",
    } },
  },
},
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```ruby
{
  "$sort": {
    first_purchase_date: 1,
  },
},
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```ruby
{
  "$set": {
    customer_id: "$_id",
  },
},
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```ruby
{ "$unset": ["_id"] },
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```ruby
aggregation_result = orders.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
ruby agg_tutorial.rb
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date"=>2020-01-01 08:25:37 UTC, "total_value"=>63, "total_orders"=>1, "orders"=>[{"orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63}], "customer_id"=>"oranieri@warmmail.com"}
{"first_purchase_date"=>2020-01-13 09:32:07 UTC, "total_value"=>436, "total_orders"=>4, "orders"=>[{"orderdate"=>2020-01-13 09:32:07 UTC, "value"=>99}, {"orderdate"=>2020-05-30 08:35:52 UTC, "value"=>231}, {"orderdate"=>2020-10-03 13:49:44 UTC, "value"=>102}, {"orderdate"=>2020-12-26 08:55:46 UTC, "value"=>4}], "customer_id"=>"elise_smith@myemail.com"}
{"first_purchase_date"=>2020-08-18 23:04:48 UTC, "total_value"=>191, "total_orders"=>2, "orders"=>[{"orderdate"=>2020-08-18 23:04:48 UTC, "value"=>4}, {"orderdate"=>2020-11-23 22:56:53 UTC, "value"=>187}], "customer_id"=>"tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**go:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

First, create a Go struct to model the data in the `orders`
collection:

```go
type Order struct {
	CustomerID string        `bson:"customer_id,omitempty"`
	OrderDate  bson.DateTime `bson:"orderdate"`
	Value      int           `bson:"value"`
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```go
orders := aggDB.Collection("orders")
orders.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 53, 0, time.UTC)),
		Value:      231,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 1, 13, 9, 32, 7, 0, time.UTC)),
		Value:      99,
	},
	Order{
		CustomerID: "oranieri@warmmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 1, 01, 8, 25, 37, 0, time.UTC)),
		Value:      63,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		Value:      2,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 11, 23, 22, 56, 53, 0, time.UTC)),
		Value:      187,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 8, 18, 23, 4, 48, 0, time.UTC)),
		Value:      4,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		Value:      4,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2021, 2, 29, 7, 49, 32, 0, time.UTC)),
		Value:      1024,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 10, 3, 13, 49, 44, 0, time.UTC)),
		Value:      102,
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "orderdate", Value: bson.D{
		{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
		{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
	}},
}}}
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```go
sortStage1 := bson.D{{Key: "$sort", Value: bson.D{
	{Key: "orderdate", Value: 1},
}}}
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

```go
groupStage := bson.D{{Key: "$group", Value: bson.D{
	{Key: "_id", Value: "$customer_id"},
	{Key: "first_purchase_date", Value: bson.D{{Key: "$first", Value: "$orderdate"}}},
	{Key: "total_value", Value: bson.D{{Key: "$sum", Value: "$value"}}},
	{Key: "total_orders", Value: bson.D{{Key: "$sum", Value: 1}}},
	{Key: "orders", Value: bson.D{{Key: "$push", Value: bson.D{
		{Key: "orderdate", Value: "$orderdate"},
		{Key: "value", Value: "$value"},
	}}}},
}}}
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```go
sortStage2 := bson.D{{Key: "$sort", Value: bson.D{
	{Key: "first_purchase_date", Value: 1},
}}}
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```go
setStage := bson.D{{Key: "$set", Value: bson.D{
	{Key: "customer_id", Value: "$_id"},
}}}
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id"}}}
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{matchStage, sortStage1, groupStage, setStage, sortStage2, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date":{"$date":"2020-01-01T08:25:37Z"},"total_value":63,"total_orders":1,"orders":[{"orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63}],"customer_id":"oranieri@warmmail.com"}
{"first_purchase_date":{"$date":"2020-01-13T09:32:07Z"},"total_value":436,"total_orders":4,"orders":[{"orderdate":{"$date":"2020-01-13T09:32:07Z"},"value":99},{"orderdate":{"$date":"2020-05-30T08:35:53Z"},"value":231},{"orderdate":{"$date":"2020-10-03T13:49:44Z"},"value":102},{"orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":4}],"customer_id":"elise_smith@myemail.com"}
{"first_purchase_date":{"$date":"2020-08-18T23:04:48Z"},"total_value":191,"total_orders":2,"orders":[{"orderdate":{"$date":"2020-08-18T23:04:48Z"},"value":4},{"orderdate":{"$date":"2020-11-23T22:56:53Z"},"value":187}],"customer_id":"tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**rust:**

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

First, create a Rust struct to model the data in the `orders`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    orderdate: DateTime,
    value: i32,
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```rust
let orders: Collection<Order> = agg_db.collection("orders");
orders.delete_many(doc! {}).await?;

let docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(53).build().unwrap(),
        value: 231,
    },
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(1).day(13).hour(9).minute(32).second(7).build().unwrap(),
        value: 99,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        value: 63,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        value: 2,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(11).day(23).hour(22).minute(56).second(53).build().unwrap(),
        value: 187,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(8).day(18).hour(23).minute(4).second(48).build().unwrap(),
        value: 4,
    },
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        value: 4,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        orderdate: DateTime::builder().year(2021).month(2).day(28).hour(7).minute(49).second(32).build().unwrap(),
        value: 1024,
    },
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        orderdate: DateTime::builder().year(2020).month(10).day(3).hour(13).minute(49).second(44).build().unwrap(),
        value: 102,
    },
];

orders.insert_many(docs).await?;
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```rust
pipeline.push(doc! {
    "$match": {
        "orderdate": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap(),
        }
    }
});
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```rust
pipeline.push(doc! {
    "$sort": {
        "orderdate": 1
    }
});
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

```rust
pipeline.push(doc! {
    "$group": {
        "_id": "$customer_id",
        "first_purchase_date": { "$first": "$orderdate" },
        "total_value": { "$sum": "$value" },
        "total_orders": { "$sum": 1 },
        "orders": {
            "$push": {
                "orderdate": "$orderdate",
                "value": "$value"
            }
        }
    }
});
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```rust
pipeline.push(doc! {
    "$sort": {
        "first_purchase_date": 1
    }
});
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```rust
pipeline.push(doc! {
    "$set": {
        "customer_id": "$_id"
    }
});
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```rust
pipeline.push(doc! {"$unset": ["_id"] });
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```rust
let mut cursor = orders.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document({"first_purchase_date": DateTime(2020-01-01 8:25:37.0 +00:00:00), "total_value": Int32(63), "total_orders": Int32(1),
"orders": Array([Document({"orderdate": DateTime(2020-01-01 8:25:37.0 +00:00:00), "value": Int32(63)})]), "customer_id": String("oranieri@warmmail.com")})

Document({"first_purchase_date": DateTime(2020-01-13 9:32:07.0 +00:00:00), "total_value": Int32(436), "total_orders": Int32(4),
"orders": Array([Document({"orderdate": DateTime(2020-01-13 9:32:07.0 +00:00:00), "value": Int32(99)}), Document({"orderdate":
DateTime(2020-05-30 8:35:53.0 +00:00:00), "value": Int32(231)}), Document({"orderdate": DateTime(2020-10-03 13:49:44.0 +00:00:00),
"value": Int32(102)}), Document({"orderdate": DateTime(2020-12-26 8:55:46.0 +00:00:00), "value": Int32(4)})]), "customer_id": String("elise_smith@myemail.com")})

Document({"first_purchase_date": DateTime(2020-08-18 23:04:48.0 +00:00:00), "total_value": Int32(191), "total_orders": Int32(2),
"orders": Array([Document({"orderdate": DateTime(2020-08-18 23:04:48.0 +00:00:00), "value": Int32(4)}), Document({"orderdate":
DateTime(2020-11-23 22:56:53.0 +00:00:00), "value": Int32(187)})]), "customer_id": String("tj@wheresmyemail.com")})
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.
