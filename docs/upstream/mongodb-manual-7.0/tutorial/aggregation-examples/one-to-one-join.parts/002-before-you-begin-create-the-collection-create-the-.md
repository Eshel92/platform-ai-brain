<!-- Part 2 of 13 of tutorial/aggregation-examples/one-to-one-join.md (split because the page is big). -->

### Create the Collection

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```java
MongoCollection<Document> orders = aggDB.getCollection("orders");
MongoCollection<Document> products = aggDB.getCollection("products");

orders.deleteMany(Filters.empty());
products.deleteMany(Filters.empty());

orders.insertMany(
        Arrays.asList(
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-05-30T08:35:52"))
                        .append("product_id", "a1b2c3d4")
                        .append("value", 431.43),
                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2019-05-28T19:13:32"))
                        .append("product_id", "z9y8x7w6")
                        .append("value", 5.01),
                new Document("customer_id", "oranieri@warmmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-01-01T08:25:37"))
                        .append("product_id", "ff11gg22hh33")
                        .append("value", 63.13),
                new Document("customer_id", "jjones@tepidmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-12-26T08:55:46"))
                        .append("product_id", "a1b2c3d4")
                        .append("value", 429.65)
        )
);

products.insertMany(
        Arrays.asList(
                new Document("id", "a1b2c3d4")
                        .append("name", "Asus Laptop")
                        .append("category", "ELECTRONICS")
                        .append("description", "Good value laptop for students"),
                new Document("id", "z9y8x7w6")
                        .append("name", "The Day Of The Triffids")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),
                new Document("id", "ff11gg22hh33")
                        .append("name", "Morphy Richardds Food Mixer")
                        .append("category", "KITCHENWARE")
                        .append("description", "Luxury mixer turning good cakes into great"),
                new Document("id", "pqr678st")
                        .append("name", "Karcher Hose Set")
                        .append("category", "GARDEN")
                        .append("description", "Hose + nosels + winder for tidy storage")
        )
);
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```java
pipeline.add(Aggregates.match(Filters.and(
        Filters.gte("orderdate", LocalDateTime.parse("2020-01-01T00:00:00")),
        Filters.lt("orderdate", LocalDateTime.parse("2021-01-01T00:00:00"))
)));
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```java
pipeline.add(Aggregates.lookup(
        "products",
        "product_id",
        "id",
        "product_mapping"
));
```

**Step 3: Add set stages to create new document fields.**

Next, add two `$set`
stages to the pipeline.

The first `$set` stage sets the `product_mapping` field
to the first element in the `product_mapping` object
created in the previous `$lookup` stage.

The second `$set` stage creates two new fields, `product_name`
and `product_category`, from the values in the
`product_mapping` object field:

```java
pipeline.add(Aggregates.set(
        new Field<>(
                "product_mapping",
                new Document("$first", "$product_mapping")
        )
));

pipeline.add(Aggregates.set(
        new Field<>("product_name", "$product_mapping.name"),
        new Field<>("product_category", "$product_mapping.category")
));
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```java
pipeline.add(Aggregates.unset("_id", "product_id", "product_mapping"));
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```java
AggregateIterable<Document> aggregationResult = orders.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T08:35:52Z"}, "value": 431.43, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T08:25:37Z"}, "value": 63.13, "product_name": "Morphy Richardds Food Mixer", "product_category": "KITCHENWARE"}
{"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T08:55:46Z"}, "value": 429.65, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.


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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Kotlin data classes to model the data in the `orders` and `products`
collections:

```kotlin
@Serializable
data class Order(
    val customerID: String,
    @Contextual val orderDate: LocalDateTime,
    val productID: String,
    val value: Double
)

@Serializable
data class Product(
    val ID: String,
    val name: String,
    val category: String,
    val description: String
)
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```kotlin
val orders = aggDB.getCollection<Order>("orders")
val products = aggDB.getCollection<Product>("products")

orders.deleteMany(Filters.empty());
products.deleteMany(Filters.empty());

orders.insertMany(
    listOf(
        Order("elise_smith@myemail.com", LocalDateTime.parse("2020-05-30T08:35:52"), "a1b2c3d4", 431.43),
        Order("tj@wheresmyemail.com", LocalDateTime.parse("2019-05-28T19:13:32"), "z9y8x7w6", 5.01),
        Order("oranieri@warmmail.com", LocalDateTime.parse("2020-01-01T08:25:37"), "ff11gg22hh33", 63.13),
        Order("jjones@tepidmail.com", LocalDateTime.parse("2020-12-26T08:55:46"), "a1b2c3d4", 429.65)
    )
)

products.insertMany(
    listOf(
        Product("a1b2c3d4", "Asus Laptop", "ELECTRONICS", "Good value laptop for students"),
        Product("z9y8x7w6", "The Day Of The Triffids", "BOOKS", "Classic post-apocalyptic novel"),
        Product(
            "ff11gg22hh33",
            "Morphy Richardds Food Mixer",
            "KITCHENWARE",
            "Luxury mixer turning good cakes into great"
        ),
        Product("pqr678st", "Karcher Hose Set", "GARDEN", "Hose + nosels + winder for tidy storage")
    )
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.and(
            Filters.gte(
                Order::orderDate.name,
                LocalDateTime.parse("2020-01-01T00:00:00").toJavaLocalDateTime()
            ),
            Filters.lt(Order::orderDate.name, LocalDateTime.parse("2021-01-01T00:00:00").toJavaLocalDateTime())
        )
    )
)
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `productID` field in the `orders`
collection to the `ID` field in the `products` collection:

```kotlin
pipeline.add(
    Aggregates.lookup(
        "products",
        Order::productID.name,
        Product::ID.name,
        "product_mapping"
    )
)
```

**Step 3: Add set stages to create new document fields.**

Next, add two `$set`
stages to the pipeline.

The first `$set` stage sets the `product_mapping` field
to the first element in the `product_mapping` object
created in the previous `$lookup` stage.

The second `$set` stage creates two new fields, `product_name`
and `product_category`, from the values in the
`product_mapping` object field:

```kotlin
pipeline.add(
    Aggregates.set(Field("product_mapping", Document("\$first", "\$product_mapping")))
)

pipeline.add(
    Aggregates.set(
        Field("product_name", "\$product_mapping.name"),
        Field("product_category", "\$product_mapping.category")
    )
)
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```kotlin
pipeline.add(Aggregates.unset("_id", Order::productID.name, "product_mapping"))
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```kotlin
val aggregationResult = orders.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
Document{{customerID=elise_smith@myemail.com, orderDate=Sat May 30 04:35:52 EDT 2020, value=431.43, product_name=Asus Laptop, product_category=ELECTRONICS}}
Document{{customerID=oranieri@warmmail.com, orderDate=Wed Jan 01 03:25:37 EST 2020, value=63.13, product_name=Morphy Richardds Food Mixer, product_category=KITCHENWARE}}
Document{{customerID=jjones@tepidmail.com, orderDate=Sat Dec 26 03:55:46 EST 2020, value=429.65, product_name=Asus Laptop, product_category=ELECTRONICS}}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.


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
