<!-- Converted from tutorial/aggregation-examples/one-to-one-join.txt (reStructuredText). Includes are inlined. -->

# Perform One-to-One Joins

This tutorial illustrates how to construct an aggregation pipeline,
perform the aggregation on a collection, and display the results using
the language of your choice.

## About This Task

This tutorial demonstrates how to combine data from a collection that
describes product information with another collection that describes
customer orders. The results show a list of all orders placed in 2020
and includes the product details associated with each order.

This aggregation performs a one-to-one join. A one-to-one join occurs
when a document in one collection has a field value that matches a
single document in another collection that has the same field value. The
aggregation matches these documents on the field value and combines
information from both sources into one result.

**Note:**

A one-to-one join does not require the documents to have a one-to-one
relationship. To learn more about this data relationship,
see the Wikipedia entry about One-to-one (data model).

## Before You Begin

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-05-30T08:35:52Z"),
      product_id: "a1b2c3d4",
      value: 431.43
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2019-05-28T19:13:32Z"),
      product_id: "z9y8x7w6",
      value: 5.01
   },
   {
      customer_id: "oranieri@warmmail.com",
      orderdate: new Date("2020-01-01T08:25:37Z"),
      product_id: "ff11gg22hh33",
      value: 63.13
   },
   {
      customer_id: "jjones@tepidmail.com",
      orderdate: new Date("2020-12-26T08:55:46Z"),
      product_id: "a1b2c3d4",
      value: 429.65
   }
] )
```

```javascript
db.products.deleteMany({})

db.products.insertMany( [
   {
      p_id: "a1b2c3d4",
      name: "Asus Laptop",
      category: "ELECTRONICS",
      description: "Good value laptop for students"
   },
   {
      p_id: "z9y8x7w6",
      name: "The Day Of The Triffids",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel"
   },
   {
      p_id: "ff11gg22hh33",
      name: "Morphy Richardds Food Mixer",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great"
   },
   {
      p_id: "pqr678st",
      name: "Karcher Hose Set",
      category: "GARDEN",
      description: "Hose + nosels + winder for tidy storage"
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [ 

   // Stage 1: Match orders that were placed in 2020
   { $match: {
      orderdate: {
         $gte: new Date("2020-01-01T00:00:00Z"),
         $lt: new Date("2021-01-01T00:00:00Z")
      } 
   } }, 

   // Stage 2: Link the collections 
   { $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "p_id",
      as: "product_mapping"
   } },

   // Stage 3: Create new document fields
   { $set: {
      product_mapping: { $first: "$product_mapping" }
   } },
   { $set: {
      product_name: "$product_mapping.name",
      product_category: "$product_mapping.category"
   } },

   // Stage 4: Remove unneeded fields
   { $unset: ["_id", "product_id", "product_mapping"] }
] )
```

In this example, the `$lookup` stage always outputs a
`product_mapping` array that contains one document. The `$set`
stage after the `$lookup` stage uses `$first` to extract the
document from the `product_mapping` array. If you use this
pipeline in a setting where the `$lookup` stage outputs an array
of more than one document, consider using an explicit ``{ $limit:
1 }` stage in the `$lookup`` stage. 

**Note:**

If a supporting index on the `foreignField` does not exist, a
`$lookup` operation that performs an equality match with a single
join will likely have poor performance. For more information,
see  and Lookup Performance Considerations and
manual-create-an-index. 

**Step 2: Interpret the aggregation results.**

The aggregated results contain three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```javascript
{
   customer_id: 'elise_smith@myemail.com',
   orderdate: ISODate('2020-05-30T08:35:52.000Z'),
   value: 431.43,
   product_name: 'Asus Laptop',
   product_category: 'ELECTRONICS'
}
{
   customer_id: 'oranieri@warmmail.com',
   orderdate: ISODate('2020-01-01T08:25:37.000Z'),
   value: 63.13,
   product_name: 'Morphy Richardds Food Mixer',
   product_category: 'KITCHENWARE'
}
{
   customer_id: 'jjones@tepidmail.com',
   orderdate: ISODate('2020-12-26T08:55:46.000Z'),
   value: 429.65,
   product_name: 'Asus Laptop',
   product_category: 'ELECTRONICS'
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products` collection
joined by matching the `product_id` field present in each original
document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```python
orders_coll = agg_db["orders"]
products_coll = agg_db["products"]

orders_coll.delete_many({})
products_coll.delete_many({})

order_data = [
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 5, 30, 8, 35, 52),
        "product_id": "a1b2c3d4",
        "value": 431.43,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2019, 5, 28, 19, 13, 32),
        "product_id": "z9y8x7w6",
        "value": 5.01,
    },
    {
        "customer_id": "oranieri@warmmail.com",
        "orderdate": datetime(2020, 1, 1, 8, 25, 37),
        "product_id": "ff11gg22hh33",
        "value": 63.13,
    },
    {
        "customer_id": "jjones@tepidmail.com",
        "orderdate": datetime(2020, 12, 26, 8, 55, 46),
        "product_id": "a1b2c3d4",
        "value": 429.65,
    },
]

orders_coll.insert_many(order_data)

product_data = [
    {
        "id": "a1b2c3d4",
        "name": "Asus Laptop",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students",
    },
    {
        "id": "z9y8x7w6",
        "name": "The Day Of The Triffids",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel",
    },
    {
        "id": "ff11gg22hh33",
        "name": "Morphy Richardds Food Mixer",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great",
    },
    {
        "id": "pqr678st",
        "name": "Karcher Hose Set",
        "category": "GARDEN",
        "description": "Hose + nosels + winder for tidy storage",
    },
]

products_coll.insert_many(product_data)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```python
pipeline.append(
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "id",
            "as": "product_mapping",
        }
    }
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

```python
pipeline.extend(
    [
        {"$set": {"product_mapping": {"$first": "$product_mapping"}}},
        {
            "$set": {
                "product_name": "$product_mapping.name",
                "product_category": "$product_mapping.category",
            }
        },
    ]
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

```python
pipeline.append({"$unset": ["_id", "product_id", "product_mapping"]})
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{'customer_id': 'elise_smith@myemail.com', 'orderdate': datetime.datetime(2020, 5, 30, 8, 35, 52), 'value': 431.43, 'product_name': 'Asus Laptop', 'product_category': 'ELECTRONICS'}
{'customer_id': 'oranieri@warmmail.com', 'orderdate': datetime.datetime(2020, 1, 1, 8, 25, 37), 'value': 63.13, 'product_name': 'Morphy Richardds Food Mixer', 'product_category': 'KITCHENWARE'}
{'customer_id': 'jjones@tepidmail.com', 'orderdate': datetime.datetime(2020, 12, 26, 8, 55, 46), 'value': 429.65, 'product_name': 'Asus Laptop', 'product_category': 'ELECTRONICS'}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

```scala
val orders = aggDB.getCollection("orders")
val products = aggDB.getCollection("products")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

products.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

orders.insertMany(
  Seq(
    Document(
      "customer_id" -> "elise_smith@myemail.com",
      "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
      "product_id" -> "a1b2c3d4",
      "value" -> 431.43
    ),
    Document(
      "customer_id" -> "tj@wheresmyemail.com",
      "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
      "product_id" -> "z9y8x7w6",
      "value" -> 5.01
    ),
    Document(
      "customer_id" -> "oranieri@warmmail.com",
      "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
      "product_id" -> "ff11gg22hh33",
      "value" -> 63.13
    ),
    Document(
      "customer_id" -> "jjones@tepidmail.com",
      "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
      "product_id" -> "a1b2c3d4",
      "value" -> 429.65
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

products.insertMany(
  Seq(
    Document(
      "id" -> "a1b2c3d4",
      "name" -> "Asus Laptop",
      "category" -> "ELECTRONICS",
      "description" -> "Good value laptop for students"
    ),
    Document(
      "id" -> "z9y8x7w6",
      "name" -> "The Day Of The Triffids",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "id" -> "ff11gg22hh33",
      "name" -> "Morphy Richardds Food Mixer",
      "category" -> "KITCHENWARE",
      "description" -> "Luxury mixer turning good cakes into great"
    ),
    Document(
      "id" -> "pqr678st",
      "name" -> "Karcher Hose Set",
      "category" -> "GARDEN",
      "description" -> "Hose + nosels + winder for tidy storage"
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```scala
Aggregates.filter(Filters.and(
  Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
  Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
)),
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```scala
Aggregates.lookup(
  "products",
  "product_id",
  "id",
  "product_mapping"
),
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

```scala
Aggregates.set(Field("product_mapping", Document("$first" -> "$product_mapping"))),
Aggregates.set(
  Field("product_name", "$product_mapping.name"),
  Field("product_category", "$product_mapping.category")
),
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```scala
Aggregates.unset("_id", "product_id", "product_mapping")
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe(
    (doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"),
  )
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 431.43, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63.13, "product_name": "Morphy Richardds Food Mixer", "product_category": "KITCHENWARE"}
{"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 429.65, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `ProductId` field
that exists in documents in both collections.

First, create C# classes to model the data in the `orders` and `products`
collections:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public string ProductId { get; set; }
  public double Value { get; set; }
}

public class Product
{
  [BsonId]
  public string Id { get; set; }
  public string Name { get; set; }
  public string Category { get; set; }
  public string Description { get; set; }
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```csharp
var orders = aggDB.GetCollection<Order>("orders");
var products = aggDB.GetCollection<Product>("products");
orders.DeleteMany(Builders<Order>.Filter.Empty);
products.DeleteMany(Builders<Product>.Filter.Empty);

orders.InsertMany(new List<Order>
{
    new Order
    {
        CustomerId = "elise_smith@myemail.com",
        OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
        ProductId = "a1b2c3d4",
        Value = 431.43
    },
    new Order
    {
        CustomerId = "tj@wheresmyemail.com",
        OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
        ProductId = "z9y8x7w6",
        Value = 5.01
    },
    new Order
    {
        CustomerId = "oranieri@warmmail.com",
        OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
        ProductId = "ff11gg22hh33",
        Value = 63.13
    },
    new Order
    {
        CustomerId = "jjones@tepidmail.com",
        OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
        ProductId = "a1b2c3d4",
        Value = 429.65
    }
});

products.InsertMany(new List<Product>
{
    new Product
    {
        Id = "a1b2c3d4",
        Name = "Asus Laptop",
        Category = "ELECTRONICS",
        Description = "Good value laptop for students"
    },
    new Product
    {
        Id = "z9y8x7w6",
        Name = "The Day Of The Triffids",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Id = "ff11gg22hh33",
        Name = "Morphy Richardds Food Mixer",
        Category = "KITCHENWARE",
        Description = "Luxury mixer turning good cakes into great"
    },
    new Product
    {
        Id = "pqr678st",
        Name = "Karcher Hose Set",
        Category = "GARDEN",
        Description = "Hose + nosels + winder for tidy storage"
    }
});
```

**Step 1: Add a match stage for orders in 2020.**

First, start the aggregation on the `orders` collection and
chain a `$match` stage that matches orders placed in 2020:

```csharp
var results = orders.Aggregate()
    .Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
                o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `ProductId` field in the `orders`
collection to the `Id` field in the `products` collection:

```csharp
.Lookup<Product, Order>(
    foreignCollectionName: "products",
    localField: "ProductId",
    foreignField: "Id",
    @as: "ProductMapping"
)
```

**Step 3: Add a projection stage to create new document fields and omit unneeded fields.**

Next, add a `$project` stage to the pipeline.

The `$project` stage creates two new fields, `ProductName`
and `ProductCategory`, from the first entries of the respective
values in the `ProductMapping` object field. The stage also
specifies which fields to include and exclude from the output documents:

```csharp
.Project(new BsonDocument
    {
        { "ProductName", new BsonDocument("$first", "$ProductMapping.Name") },
        { "ProductCategory", new BsonDocument("$first", "$ProductMapping.Category") },
        { "OrderDate", 1 },
        { "CustomerId", 1 },
        { "Value", 1 },
        { "_id", 0 },
    });
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from
this element.

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`ProductName` and `ProductCategory` of the ordered product:

```none
{ "CustomerId" : "elise_smith@myemail.com", "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 431.43000000000001, "ProductName" : "Asus Laptop", "ProductCategory" : "ELECTRONICS" }
{ "CustomerId" : "oranieri@warmmail.com", "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63.130000000000003, "ProductName" : "Morphy Richardds Food Mixer", "ProductCategory" : "KITCHENWARE" }
{ "CustomerId" : "jjones@tepidmail.com", "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 429.64999999999998, "ProductName" : "Asus Laptop", "ProductCategory" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `ProductId` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```c
mongoc_collection_t *orders = mongoc_client_get_collection(client, "agg_tutorials_db", "orders");
mongoc_collection_t *products = mongoc_client_get_collection(client, "agg_tutorials_db", "products");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(orders, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    if (!mongoc_collection_delete_many(products, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 4;
    bson_t *order_docs[num_docs];

    order_docs[0] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1590822952000UL), // 2020-05-30T08:35:52Z
        "product_id", BCON_UTF8("a1b2c3d4"),
        "value", BCON_DOUBLE(431.43));

    order_docs[1] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1559063612000UL), // 2019-05-28T19:13:32Z
        "product_id", BCON_UTF8("z9y8x7w6"),
        "value", BCON_DOUBLE(5.01));

    order_docs[2] = BCON_NEW(
        "customer_id", BCON_UTF8("oranieri@warmmail.com"),
        "orderdate", BCON_DATE_TIME(1577869537000UL), // 2020-01-01T08:25:37Z
        "product_id", BCON_UTF8("ff11gg22hh33"),
        "value", BCON_DOUBLE(63.13));

    order_docs[3] = BCON_NEW(
        "customer_id", BCON_UTF8("jjones@tepidmail.com"),
        "orderdate", BCON_DATE_TIME(1608976546000UL), // 2020-12-26T08:55:46Z
        "product_id", BCON_UTF8("a1b2c3d4"),
        "value", BCON_DOUBLE(429.65));

    bson_error_t error;
    if (!mongoc_collection_insert_many(orders, (const bson_t **)order_docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(order_docs[i]);
    }
}

{
    size_t num_docs = 4;
    bson_t *product_docs[num_docs];

    product_docs[0] = BCON_NEW(
        "id", BCON_UTF8("a1b2c3d4"),
        "name", BCON_UTF8("Asus Laptop"),
        "category", BCON_UTF8("ELECTRONICS"),
        "description", BCON_UTF8("Good value laptop for students"));

    product_docs[1] = BCON_NEW(
        "id", BCON_UTF8("z9y8x7w6"),
        "name", BCON_UTF8("The Day Of The Triffids"),
        "category", BCON_UTF8("BOOKS"),
        "description", BCON_UTF8("Classic post-apocalyptic novel"));

    product_docs[2] = BCON_NEW(
        "id", BCON_UTF8("ff11gg22hh33"),
        "name", BCON_UTF8("Morphy Richardds Food Mixer"),
        "category", BCON_UTF8("KITCHENWARE"),
        "description", BCON_UTF8("Luxury mixer turning good cakes into great"));

    product_docs[3] = BCON_NEW(
        "id", BCON_UTF8("pqr678st"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "category", BCON_UTF8("GARDEN"),
        "description", BCON_UTF8("Hose + nosels + winder for tidy storage"));

    bson_error_t error;
    if (!mongoc_collection_insert_many(products, (const bson_t **)product_docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(product_docs[i]);
    }
}
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```c
"{", "$match", "{",
"orderdate", "{",
"$gte", BCON_DATE_TIME(1577836800000UL),
"$lt", BCON_DATE_TIME(1609459200000UL),
"}",
"}", "}",
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```c
"{", "$lookup", "{",
"from", BCON_UTF8("products"),
"localField", BCON_UTF8("product_id"),
"foreignField", BCON_UTF8("id"),
"as", BCON_UTF8("product_mapping"),
"}", "}",
```

**Step 3: Add set stages to create new document fields.**

Next, add two `$set` stages to the pipeline.

The first `$set` stage sets the `product_mapping` field
to the first element in the `product_mapping` object
created in the previous `$lookup` stage. 

The second `$set` stage creates two new fields, `product_name`
and `product_category`, from the values in the
`product_mapping` object field:

```c
"{", "$set", "{", "product_mapping", "{", "$first", BCON_UTF8("$product_mapping"), "}", "}", "}",
"{", "$set", "{",
"product_name", BCON_UTF8("$product_mapping.name"),
"product_category", BCON_UTF8("$product_mapping.category"),
"}", "}",
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from
this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("product_id"), BCON_UTF8("product_mapping"), "]", "}",
```

**Step 5: Run the aggregation pipeline.**

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
mongoc_collection_destroy(products);
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
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{ "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : { "$numberLong" : "1590822952000" } }, "value" : { "$numberDouble" : "431.43000000000000682" }, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
{ "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : { "$numberLong" : "1577869537000" } }, "value" : { "$numberDouble" : "63.130000000000002558" }, "product_name" : "Morphy Richardds Food Mixer", "product_category" : "KITCHENWARE" }
{ "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" : { "$numberLong" : "1608976546000" } }, "value" : { "$numberDouble" : "429.64999999999997726" }, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```cpp
auto orders = db["orders"];
auto products = db["products"];

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "product_id": "a1b2c3d4",
        "value": 431.43
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559062412},
        "product_id": "z9y8x7w6",
        "value": 5.01
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137},
        "product_id": "ff11gg22hh33",
        "value": 63.13
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "jjones@tepidmail.com",
        "orderdate": {"$date": 1608972946000},
        "product_id": "a1b2c3d4",
        "value": 429.65
    })")
};

orders.insert_many(order_docs); // Might throw an exception

std::vector<bsoncxx::document::value> product_docs = {
    bsoncxx::from_json(R"({
        "id": "a1b2c3d4",
        "name": "Asus Laptop",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students"
    })"),
    bsoncxx::from_json(R"({
        "id": "z9y8x7w6",
        "name": "The Day Of The Triffids",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "id": "ff11gg22hh33",
        "name": "Morphy Richardds Food Mixer",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great"
    })"),
    bsoncxx::from_json(R"({
        "id": "pqr678st",
        "name": "Karcher Hose Set",
        "category": "GARDEN",
        "description": "Hose + nosels + winder for tidy storage"
    })")
};

products.insert_many(product_docs); // Might throw an exception
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orderdate": {
        "$gte": {"$date": 1577836800},
        "$lt": {"$date": 1609459200000}
    }
})"));
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```cpp
pipeline.lookup(bsoncxx::from_json(R"({
    "from": "products",
    "localField": "product_id",
    "foreignField": "id",
    "as": "product_mapping"
})"));
```

**Step 3: Add addFields stages to create new document fields.**

Next, add two `$addFields`
stages to the pipeline.

The first `$addFields` stage sets the `product_mapping` field
to the first element in the `product_mapping` object
created in the previous `$lookup` stage. 

The second `$addFields` stage creates two new fields, `product_name`
and `product_category`, from the values in the
`product_mapping` object field:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_mapping": {"$first": "$product_mapping"}
})"));
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_name": "$product_mapping.name",
    "product_category": "$product_mapping.category"
})"));
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "product_id", "product_mapping"]
})"));
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{ "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : "2020-05-30T06:55:52Z" },
"value" : 431.43000000000000682, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
{ "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : "1970-01-19T06:17:41.137Z" },
"value" : 63.130000000000002558, "product_name" : "Morphy Richardds Food Mixer", "product_category" : "KITCHENWARE" }
{ "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" : "2020-12-26T08:55:46Z" },
"value" : 429.64999999999997726, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```javascript
const orders = aggDB.collection("orders");
const products = aggDB.collection("products");

await orders.deleteMany({});
await products.deleteMany({});

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    product_id: "a1b2c3d4",
    value: 431.43,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    product_id: "z9y8x7w6",
    value: 5.01,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    product_id: "ff11gg22hh33",
    value: 63.13,
  },
  {
    customer_id: "jjones@tepidmail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    product_id: "a1b2c3d4",
    value: 429.65,
  },
]);

await products.insertMany([
  {
    id: "a1b2c3d4",
    name: "Asus Laptop",
    category: "ELECTRONICS",
    description: "Good value laptop for students",
  },
  {
    id: "z9y8x7w6",
    name: "The Day Of The Triffids",
    category: "BOOKS",
    description: "Classic post-apocalyptic novel",
  },
  {
    id: "ff11gg22hh33",
    name: "Morphy Richardds Food Mixer",
    category: "KITCHENWARE",
    description: "Luxury mixer turning good cakes into great",
  },
  {
    id: "pqr678st",
    name: "Karcher Hose Set",
    category: "GARDEN",
    description: "Hose + nosels + winder for tidy storage",
  },
]);
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```javascript
pipeline.push({
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "id",
    as: "product_mapping",
  },
});
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

```javascript
pipeline.push(
  {
    $set: {
      product_mapping: { $first: "$product_mapping" },
    },
  },
  {
    $set: {
      product_name: "$product_mapping.name",
      product_category: "$product_mapping.category",
    },
  }
);
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```javascript
pipeline.push({ $unset: ["_id", "product_id", "product_mapping"] });
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```javascript
{
  customer_id: 'elise_smith@myemail.com',
  orderdate: 2020-05-30T08:35:52.000Z,
  value: 431.43,
  product_name: 'Asus Laptop',
  product_category: 'ELECTRONICS'
}
{
  customer_id: 'oranieri@warmmail.com',
  orderdate: 2020-01-01T08:25:37.000Z,
  value: 63.13,
  product_name: 'Morphy Richardds Food Mixer',
  product_category: 'KITCHENWARE'
}
{
  customer_id: 'jjones@tepidmail.com',
  orderdate: 2020-12-26T08:55:46.000Z,
  value: 429.65,
  product_name: 'Asus Laptop',
  product_category: 'ELECTRONICS'
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$products = $client->agg_tutorials_db->products;

$orders->deleteMany([]);
$products->deleteMany([]);

$orders->insertMany(
    [
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-05-30T08:35:52')),
            'product_id' => 'a1b2c3d4',
            'value' => 431.43
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2019-05-28T19:13:32')),
            'product_id' => 'z9y8x7w6',
            'value' => 5.01
        ],
        [
            'customer_id' => 'oranieri@warmmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-01T08:25:37')),
            'product_id' => 'ff11gg22hh33',
            'value' => 63.13,
        ],
        [
            'customer_id' => 'jjones@tepidmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-12-26T08:55:46')),
            'product_id' => 'a1b2c3d4',
            'value' => 429.65
        ],
    ]
);

$products->insertMany(
    [
        [
            'id' => 'a1b2c3d4',
            'name' => 'Asus Laptop',
            'category' => 'ELECTRONICS',
            'description' => 'Good value laptop for students',
        ],
        [
            'id' => 'z9y8x7w6',
            'name' => 'The Day Of The Triffids',
            'category' => 'BOOKS',
            'description' => 'Classic post-apocalyptic novel',
        ],
        [
            'id' => 'ff11gg22hh33',
            'name' => 'Morphy Richardds Food Mixer',
            'category' => 'KITCHENWARE',
            'description' => 'Luxury mixer turning good cakes into great',
        ],
        [
            'id' => 'pqr678st',
            'name' => 'Karcher Hose Set',
            'category' => 'GARDEN',
            'description' => 'Hose + nosels + winder for tidy storage',
        ],
    ]
);
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

**Step 2: Add a lookup stage to link the collections.**

Outside of your `Pipeline` instance, create a `$lookup` stage in a factory
function. The`$lookup` stage joins the `product_id` field in
the `orders` collection to the `id` field in the `products`
collection:

```php
function lookupProductsStage()
{
    return Stage::lookup(
        from: 'products',
        localField: 'product_id',
        foreignField: 'id',
        as: 'product_mapping',
    );
}
```

Then, in your `Pipeline` instance, call the
`lookupProductsStage()` function:

```php
function lookupProductsStage()
{
    return Stage::lookup(
        from: 'products',
        localField: 'product_id',
        foreignField: 'id',
        as: 'product_mapping',
    );
}
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

```php
Stage::set(
    product_mapping: Expression::first(
        Expression::arrayFieldPath('product_mapping')
    )
),
Stage::set(
    product_name: Expression::stringFieldPath('product_mapping.name'),
    product_category: Expression::stringFieldPath('product_mapping.category')
),
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```php
Stage::unset('_id', 'product_id', 'product_mapping')
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{
    "customer_id": "elise_smith@myemail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1590827752000"
        }
    },
    "value": 431.43,
    "product_name": "Asus Laptop",
    "product_category": "ELECTRONICS"
}
{
    "customer_id": "oranieri@warmmail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1577867137000"
        }
    },
    "value": 63.13,
    "product_name": "Morphy Richardds Food Mixer",
    "product_category": "KITCHENWARE"
}
{
    "customer_id": "jjones@tepidmail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1608972946000"
        }
    },
    "value": 429.65,
    "product_name": "Asus Laptop",
    "product_category": "ELECTRONICS"
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```ruby
orders = agg_db[:orders]
products = agg_db[:products]

orders.delete_many({})
products.delete_many({})

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      product_id: "a1b2c3d4",
      value: 431.43,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      product_id: "z9y8x7w6",
      value: 5.01,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      product_id: "ff11gg22hh33",
      value: 63.13,
    },
    {
      customer_id: "jjones@tepidmail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      product_id: "a1b2c3d4",
      value: 429.65,
    },
  ]
)

products.insert_many(
  [
    {
      id: "a1b2c3d4",
      name: "Asus Laptop",
      category: "ELECTRONICS",
      description: "Good value laptop for students",
    },
    {
      id: "z9y8x7w6",
      name: "The Day Of The Triffids",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      id: "ff11gg22hh33",
      name: "Morphy Richardds Food Mixer",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great",
    },
    {
      id: "pqr678st",
      name: "Karcher Hose Set",
      category: "GARDEN",
      description: "Hose + nosels + winder for tidy storage",
    },
  ]
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```ruby
{
  "$lookup": {
    from: "products",
    localField: "product_id",
    foreignField: "id",
    as: "product_mapping",
  },
},
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

```ruby
{
  "$set": {
    product_mapping: { "$first": "$product_mapping" },
  },
},
{
  "$set": {
    product_name: "$product_mapping.name",
    product_category: "$product_mapping.category",
  },
},
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```ruby
{ "$unset": ["_id", "product_id", "product_mapping"] },
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id"=>"elise_smith@myemail.com", "orderdate"=>2020-05-30 08:35:52 UTC, "value"=>431.43, "product_name"=>"Asus Laptop", "product_category"=>"ELECTRONICS"}
{"customer_id"=>"oranieri@warmmail.com", "orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63.13, "product_name"=>"Morphy Richardds Food Mixer", "product_category"=>"KITCHENWARE"}
{"customer_id"=>"jjones@tepidmail.com", "orderdate"=>2020-12-26 08:55:46 UTC, "value"=>429.65, "product_name"=>"Asus Laptop", "product_category"=>"ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Go structs to model the data in the `orders` and `products`
collections:

```go
type Order struct {
	CustomerID string        `bson:"customer_id"`
	OrderDate  bson.DateTime `bson:"orderdate"`
	ProductID  string        `bson:"product_id"`
	Value      float32       `bson:"value"`
}

type Product struct {
	ID          string `bson:"id"`
	Name        string `bson:"name"`
	Category    string `bson:"category"`
	Description string `bson:"description"`
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```go
orders := aggDB.Collection("orders")
products := aggDB.Collection("products")
orders.DeleteMany(context.TODO(), bson.D{})
products.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 52, 0, time.UTC)),
		ProductID:  "a1b2c3d4",
		Value:      431.43,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		ProductID:  "z9y8x7w6",
		Value:      5.01,
	},
	Order{
		CustomerID: "oranieri@warmmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 01, 01, 8, 25, 37, 0, time.UTC)),
		ProductID:  "ff11gg22hh33",
		Value:      63.13,
	},
	Order{
		CustomerID: "jjones@tepidmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		ProductID:  "a1b2c3d4",
		Value:      429.65,
	},
})
if err != nil {
	log.Fatal(err)
}

_, err = products.InsertMany(context.TODO(), []interface{}{
	Product{
		ID:          "a1b2c3d4",
		Name:        "Asus Laptop",
		Category:    "ELECTRONICS",
		Description: "Good value laptop for students",
	},
	Product{
		ID:          "z9y8x7w6",
		Name:        "The Day Of The Triffids",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		ID:          "ff11gg22hh33",
		Name:        "Morphy Richardds Food Mixer",
		Category:    "KITCHENWARE",
		Description: "Luxury mixer turning good cakes into great",
	},
	Product{
		ID:          "pqr678st",
		Name:        "Karcher Hose Set",
		Category:    "GARDEN",
		Description: "Hose + nosels + winder for tidy storage",
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "orderdate", Value: bson.D{
		{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
		{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
	}},
}}}
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```go
lookupStage := bson.D{{Key: "$lookup", Value: bson.D{
	{Key: "from", Value: "products"},
	{Key: "localField", Value: "product_id"},
	{Key: "foreignField", Value: "id"},
	{Key: "as", Value: "product_mapping"},
}}}
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

```go
setStage1 := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_mapping", Value: bson.D{{Key: "$first", Value: "$product_mapping"}}},
}}}

setStage2 := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_name", Value: "$product_mapping.name"},
	{Key: "product_category", Value: "$product_mapping.category"},
}}}
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id", "product_id", "product_mapping"}}}
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{matchStage, lookupStage, setStage1, setStage2, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id":"elise_smith@myemail.com","orderdate":{"$date":"2020-05-30T08:35:52Z"},"value":431.42999267578125,"product_name":"Asus Laptop","product_category":"ELECTRONICS"}
{"customer_id":"oranieri@warmmail.com","orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63.130001068115234,"product_name":"Morphy Richardds Food Mixer","product_category":"KITCHENWARE"}
{"customer_id":"jjones@tepidmail.com","orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":429.6499938964844,"product_name":"Asus Laptop","product_category":"ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Rust structs to model the data in the `orders` and `products`
collections:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    order_date: DateTime,
    product_id: String,
    value: f32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Product {
    id: String,
    name: String,
    category: String,
    description: String,
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```rust
let orders: Collection<Order> = agg_db.collection("orders");
let products: Collection<Product> = agg_db.collection("products");

orders.delete_many(doc! {}).await?;
products.delete_many(doc! {}).await?;

let order_docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(52).build().unwrap(),
        product_id: "a1b2c3d4".to_string(),
        value: 431.43,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        order_date: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        product_id: "z9y8x7w6".to_string(),
        value: 5.01,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        product_id: "ff11gg22hh33".to_string(),
        value: 63.13,
    },
    Order {
        customer_id: "jjones@tepidmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        product_id: "a1b2c3d4".to_string(),
        value: 429.65,
    },
];
orders.insert_many(order_docs).await?;

let product_docs = vec![
    Product {
        id: "a1b2c3d4".to_string(),
        name: "Asus Laptop".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Good value laptop for students".to_string(),
    },
    Product {
        id: "z9y8x7w6".to_string(),
        name: "The Day Of The Triffids".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        id: "ff11gg22hh33".to_string(),
        name: "Morphy Richardds Food Mixer".to_string(),
        category: "KITCHENWARE".to_string(),
        description: "Luxury mixer turning good cakes into great".to_string(),
    },
    Product {
        id: "pqr678st".to_string(),
        name: "Karcher Hose Set".to_string(),
        category: "GARDEN".to_string(),
        description: "Hose + nosels + winder for tidy storage".to_string(),
    },
];
products.insert_many(product_docs).await?;
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```rust
pipeline.push(doc! {
    "$match": {
        "order_date": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap()
        }
    }
});
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```rust
pipeline.push(doc! {
    "$lookup": {
        "from": "products",
        "localField": "product_id",
        "foreignField": "id",
        "as": "product_mapping"
    }
});
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

```rust
pipeline.push(doc! {
    "$set": {
        "product_mapping": { "$first": "$product_mapping" }
    }
});

pipeline.push(doc! {
    "$set": {
        "product_name": "$product_mapping.name",
        "product_category": "$product_mapping.category"
    }
});
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```rust
pipeline.push(doc! {
    "$unset": ["_id", "product_id", "product_mapping"]
});
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
Document({"customer_id": String("elise_smith@myemail.com"), "order_date": DateTime(2020-05-30 8:35:52.0 +00:00:00),
"value": Double(431.42999267578125), "product_name": String("Asus Laptop"), "product_category": String("ELECTRONICS")})

Document({"customer_id": String("oranieri@warmmail.com"), "order_date": DateTime(2020-01-01 8:25:37.0 +00:00:00),
"value": Double(63.130001068115234), "product_name": String("Morphy Richardds Food Mixer"), "product_category": String("KITCHENWARE")})

Document({"customer_id": String("jjones@tepidmail.com"), "order_date": DateTime(2020-12-26 8:55:46.0 +00:00:00),
"value": Double(429.6499938964844), "product_name": String("Asus Laptop"), "product_category": String("ELECTRONICS")})
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to join collections on a single common field.

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-05-30T08:35:52Z"),
      product_id: "a1b2c3d4",
      value: 431.43
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2019-05-28T19:13:32Z"),
      product_id: "z9y8x7w6",
      value: 5.01
   },
   {
      customer_id: "oranieri@warmmail.com",
      orderdate: new Date("2020-01-01T08:25:37Z"),
      product_id: "ff11gg22hh33",
      value: 63.13
   },
   {
      customer_id: "jjones@tepidmail.com",
      orderdate: new Date("2020-12-26T08:55:46Z"),
      product_id: "a1b2c3d4",
      value: 429.65
   }
] )
```

```javascript
db.products.deleteMany({})

db.products.insertMany( [
   {
      p_id: "a1b2c3d4",
      name: "Asus Laptop",
      category: "ELECTRONICS",
      description: "Good value laptop for students"
   },
   {
      p_id: "z9y8x7w6",
      name: "The Day Of The Triffids",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel"
   },
   {
      p_id: "ff11gg22hh33",
      name: "Morphy Richardds Food Mixer",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great"
   },
   {
      p_id: "pqr678st",
      name: "Karcher Hose Set",
      category: "GARDEN",
      description: "Hose + nosels + winder for tidy storage"
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [ 

   // Stage 1: Match orders that were placed in 2020
   { $match: {
      orderdate: {
         $gte: new Date("2020-01-01T00:00:00Z"),
         $lt: new Date("2021-01-01T00:00:00Z")
      } 
   } }, 

   // Stage 2: Link the collections 
   { $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "p_id",
      as: "product_mapping"
   } },

   // Stage 3: Create new document fields
   { $set: {
      product_mapping: { $first: "$product_mapping" }
   } },
   { $set: {
      product_name: "$product_mapping.name",
      product_category: "$product_mapping.category"
   } },

   // Stage 4: Remove unneeded fields
   { $unset: ["_id", "product_id", "product_mapping"] }
] )
```

In this example, the `$lookup` stage always outputs a
`product_mapping` array that contains one document. The `$set`
stage after the `$lookup` stage uses `$first` to extract the
document from the `product_mapping` array. If you use this
pipeline in a setting where the `$lookup` stage outputs an array
of more than one document, consider using an explicit ``{ $limit:
1 }` stage in the `$lookup`` stage. 

**Note:**

If a supporting index on the `foreignField` does not exist, a
`$lookup` operation that performs an equality match with a single
join will likely have poor performance. For more information,
see  and Lookup Performance Considerations and
manual-create-an-index. 

**Step 2: Interpret the aggregation results.**

The aggregated results contain three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```javascript
{
   customer_id: 'elise_smith@myemail.com',
   orderdate: ISODate('2020-05-30T08:35:52.000Z'),
   value: 431.43,
   product_name: 'Asus Laptop',
   product_category: 'ELECTRONICS'
}
{
   customer_id: 'oranieri@warmmail.com',
   orderdate: ISODate('2020-01-01T08:25:37.000Z'),
   value: 63.13,
   product_name: 'Morphy Richardds Food Mixer',
   product_category: 'KITCHENWARE'
}
{
   customer_id: 'jjones@tepidmail.com',
   orderdate: ISODate('2020-12-26T08:55:46.000Z'),
   value: 429.65,
   product_name: 'Asus Laptop',
   product_category: 'ELECTRONICS'
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products` collection
joined by matching the `product_id` field present in each original
document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```python
orders_coll = agg_db["orders"]
products_coll = agg_db["products"]

orders_coll.delete_many({})
products_coll.delete_many({})

order_data = [
    {
        "customer_id": "elise_smith@myemail.com",
        "orderdate": datetime(2020, 5, 30, 8, 35, 52),
        "product_id": "a1b2c3d4",
        "value": 431.43,
    },
    {
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": datetime(2019, 5, 28, 19, 13, 32),
        "product_id": "z9y8x7w6",
        "value": 5.01,
    },
    {
        "customer_id": "oranieri@warmmail.com",
        "orderdate": datetime(2020, 1, 1, 8, 25, 37),
        "product_id": "ff11gg22hh33",
        "value": 63.13,
    },
    {
        "customer_id": "jjones@tepidmail.com",
        "orderdate": datetime(2020, 12, 26, 8, 55, 46),
        "product_id": "a1b2c3d4",
        "value": 429.65,
    },
]

orders_coll.insert_many(order_data)

product_data = [
    {
        "id": "a1b2c3d4",
        "name": "Asus Laptop",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students",
    },
    {
        "id": "z9y8x7w6",
        "name": "The Day Of The Triffids",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel",
    },
    {
        "id": "ff11gg22hh33",
        "name": "Morphy Richardds Food Mixer",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great",
    },
    {
        "id": "pqr678st",
        "name": "Karcher Hose Set",
        "category": "GARDEN",
        "description": "Hose + nosels + winder for tidy storage",
    },
]

products_coll.insert_many(product_data)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```python
pipeline.append(
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "id",
            "as": "product_mapping",
        }
    }
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

```python
pipeline.extend(
    [
        {"$set": {"product_mapping": {"$first": "$product_mapping"}}},
        {
            "$set": {
                "product_name": "$product_mapping.name",
                "product_category": "$product_mapping.category",
            }
        },
    ]
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

```python
pipeline.append({"$unset": ["_id", "product_id", "product_mapping"]})
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{'customer_id': 'elise_smith@myemail.com', 'orderdate': datetime.datetime(2020, 5, 30, 8, 35, 52), 'value': 431.43, 'product_name': 'Asus Laptop', 'product_category': 'ELECTRONICS'}
{'customer_id': 'oranieri@warmmail.com', 'orderdate': datetime.datetime(2020, 1, 1, 8, 25, 37), 'value': 63.13, 'product_name': 'Morphy Richardds Food Mixer', 'product_category': 'KITCHENWARE'}
{'customer_id': 'jjones@tepidmail.com', 'orderdate': datetime.datetime(2020, 12, 26, 8, 55, 46), 'value': 429.65, 'product_name': 'Asus Laptop', 'product_category': 'ELECTRONICS'}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

```scala
val orders = aggDB.getCollection("orders")
val products = aggDB.getCollection("products")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

products.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

orders.insertMany(
  Seq(
    Document(
      "customer_id" -> "elise_smith@myemail.com",
      "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
      "product_id" -> "a1b2c3d4",
      "value" -> 431.43
    ),
    Document(
      "customer_id" -> "tj@wheresmyemail.com",
      "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
      "product_id" -> "z9y8x7w6",
      "value" -> 5.01
    ),
    Document(
      "customer_id" -> "oranieri@warmmail.com",
      "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
      "product_id" -> "ff11gg22hh33",
      "value" -> 63.13
    ),
    Document(
      "customer_id" -> "jjones@tepidmail.com",
      "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
      "product_id" -> "a1b2c3d4",
      "value" -> 429.65
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

products.insertMany(
  Seq(
    Document(
      "id" -> "a1b2c3d4",
      "name" -> "Asus Laptop",
      "category" -> "ELECTRONICS",
      "description" -> "Good value laptop for students"
    ),
    Document(
      "id" -> "z9y8x7w6",
      "name" -> "The Day Of The Triffids",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "id" -> "ff11gg22hh33",
      "name" -> "Morphy Richardds Food Mixer",
      "category" -> "KITCHENWARE",
      "description" -> "Luxury mixer turning good cakes into great"
    ),
    Document(
      "id" -> "pqr678st",
      "name" -> "Karcher Hose Set",
      "category" -> "GARDEN",
      "description" -> "Hose + nosels + winder for tidy storage"
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```scala
Aggregates.filter(Filters.and(
  Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
  Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
)),
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```scala
Aggregates.lookup(
  "products",
  "product_id",
  "id",
  "product_mapping"
),
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

```scala
Aggregates.set(Field("product_mapping", Document("$first" -> "$product_mapping"))),
Aggregates.set(
  Field("product_name", "$product_mapping.name"),
  Field("product_category", "$product_mapping.category")
),
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```scala
Aggregates.unset("_id", "product_id", "product_mapping")
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe(
    (doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"),
  )
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 431.43, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63.13, "product_name": "Morphy Richardds Food Mixer", "product_category": "KITCHENWARE"}
{"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 429.65, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `ProductId` field
that exists in documents in both collections.

First, create C# classes to model the data in the `orders` and `products`
collections:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public string ProductId { get; set; }
  public double Value { get; set; }
}

public class Product
{
  [BsonId]
  public string Id { get; set; }
  public string Name { get; set; }
  public string Category { get; set; }
  public string Description { get; set; }
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```csharp
var orders = aggDB.GetCollection<Order>("orders");
var products = aggDB.GetCollection<Product>("products");
orders.DeleteMany(Builders<Order>.Filter.Empty);
products.DeleteMany(Builders<Product>.Filter.Empty);

orders.InsertMany(new List<Order>
{
    new Order
    {
        CustomerId = "elise_smith@myemail.com",
        OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
        ProductId = "a1b2c3d4",
        Value = 431.43
    },
    new Order
    {
        CustomerId = "tj@wheresmyemail.com",
        OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
        ProductId = "z9y8x7w6",
        Value = 5.01
    },
    new Order
    {
        CustomerId = "oranieri@warmmail.com",
        OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
        ProductId = "ff11gg22hh33",
        Value = 63.13
    },
    new Order
    {
        CustomerId = "jjones@tepidmail.com",
        OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
        ProductId = "a1b2c3d4",
        Value = 429.65
    }
});

products.InsertMany(new List<Product>
{
    new Product
    {
        Id = "a1b2c3d4",
        Name = "Asus Laptop",
        Category = "ELECTRONICS",
        Description = "Good value laptop for students"
    },
    new Product
    {
        Id = "z9y8x7w6",
        Name = "The Day Of The Triffids",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Id = "ff11gg22hh33",
        Name = "Morphy Richardds Food Mixer",
        Category = "KITCHENWARE",
        Description = "Luxury mixer turning good cakes into great"
    },
    new Product
    {
        Id = "pqr678st",
        Name = "Karcher Hose Set",
        Category = "GARDEN",
        Description = "Hose + nosels + winder for tidy storage"
    }
});
```

**Step 1: Add a match stage for orders in 2020.**

First, start the aggregation on the `orders` collection and
chain a `$match` stage that matches orders placed in 2020:

```csharp
var results = orders.Aggregate()
    .Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
                o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `ProductId` field in the `orders`
collection to the `Id` field in the `products` collection:

```csharp
.Lookup<Product, Order>(
    foreignCollectionName: "products",
    localField: "ProductId",
    foreignField: "Id",
    @as: "ProductMapping"
)
```

**Step 3: Add a projection stage to create new document fields and omit unneeded fields.**

Next, add a `$project` stage to the pipeline.

The `$project` stage creates two new fields, `ProductName`
and `ProductCategory`, from the first entries of the respective
values in the `ProductMapping` object field. The stage also
specifies which fields to include and exclude from the output documents:

```csharp
.Project(new BsonDocument
    {
        { "ProductName", new BsonDocument("$first", "$ProductMapping.Name") },
        { "ProductCategory", new BsonDocument("$first", "$ProductMapping.Category") },
        { "OrderDate", 1 },
        { "CustomerId", 1 },
        { "Value", 1 },
        { "_id", 0 },
    });
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from
this element.

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`ProductName` and `ProductCategory` of the ordered product:

```none
{ "CustomerId" : "elise_smith@myemail.com", "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 431.43000000000001, "ProductName" : "Asus Laptop", "ProductCategory" : "ELECTRONICS" }
{ "CustomerId" : "oranieri@warmmail.com", "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63.130000000000003, "ProductName" : "Morphy Richardds Food Mixer", "ProductCategory" : "KITCHENWARE" }
{ "CustomerId" : "jjones@tepidmail.com", "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 429.64999999999998, "ProductName" : "Asus Laptop", "ProductCategory" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `ProductId` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```c
mongoc_collection_t *orders = mongoc_client_get_collection(client, "agg_tutorials_db", "orders");
mongoc_collection_t *products = mongoc_client_get_collection(client, "agg_tutorials_db", "products");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(orders, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    if (!mongoc_collection_delete_many(products, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 4;
    bson_t *order_docs[num_docs];

    order_docs[0] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1590822952000UL), // 2020-05-30T08:35:52Z
        "product_id", BCON_UTF8("a1b2c3d4"),
        "value", BCON_DOUBLE(431.43));

    order_docs[1] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1559063612000UL), // 2019-05-28T19:13:32Z
        "product_id", BCON_UTF8("z9y8x7w6"),
        "value", BCON_DOUBLE(5.01));

    order_docs[2] = BCON_NEW(
        "customer_id", BCON_UTF8("oranieri@warmmail.com"),
        "orderdate", BCON_DATE_TIME(1577869537000UL), // 2020-01-01T08:25:37Z
        "product_id", BCON_UTF8("ff11gg22hh33"),
        "value", BCON_DOUBLE(63.13));

    order_docs[3] = BCON_NEW(
        "customer_id", BCON_UTF8("jjones@tepidmail.com"),
        "orderdate", BCON_DATE_TIME(1608976546000UL), // 2020-12-26T08:55:46Z
        "product_id", BCON_UTF8("a1b2c3d4"),
        "value", BCON_DOUBLE(429.65));

    bson_error_t error;
    if (!mongoc_collection_insert_many(orders, (const bson_t **)order_docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(order_docs[i]);
    }
}

{
    size_t num_docs = 4;
    bson_t *product_docs[num_docs];

    product_docs[0] = BCON_NEW(
        "id", BCON_UTF8("a1b2c3d4"),
        "name", BCON_UTF8("Asus Laptop"),
        "category", BCON_UTF8("ELECTRONICS"),
        "description", BCON_UTF8("Good value laptop for students"));

    product_docs[1] = BCON_NEW(
        "id", BCON_UTF8("z9y8x7w6"),
        "name", BCON_UTF8("The Day Of The Triffids"),
        "category", BCON_UTF8("BOOKS"),
        "description", BCON_UTF8("Classic post-apocalyptic novel"));

    product_docs[2] = BCON_NEW(
        "id", BCON_UTF8("ff11gg22hh33"),
        "name", BCON_UTF8("Morphy Richardds Food Mixer"),
        "category", BCON_UTF8("KITCHENWARE"),
        "description", BCON_UTF8("Luxury mixer turning good cakes into great"));

    product_docs[3] = BCON_NEW(
        "id", BCON_UTF8("pqr678st"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "category", BCON_UTF8("GARDEN"),
        "description", BCON_UTF8("Hose + nosels + winder for tidy storage"));

    bson_error_t error;
    if (!mongoc_collection_insert_many(products, (const bson_t **)product_docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(product_docs[i]);
    }
}
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```c
"{", "$match", "{",
"orderdate", "{",
"$gte", BCON_DATE_TIME(1577836800000UL),
"$lt", BCON_DATE_TIME(1609459200000UL),
"}",
"}", "}",
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```c
"{", "$lookup", "{",
"from", BCON_UTF8("products"),
"localField", BCON_UTF8("product_id"),
"foreignField", BCON_UTF8("id"),
"as", BCON_UTF8("product_mapping"),
"}", "}",
```

**Step 3: Add set stages to create new document fields.**

Next, add two `$set` stages to the pipeline.

The first `$set` stage sets the `product_mapping` field
to the first element in the `product_mapping` object
created in the previous `$lookup` stage. 

The second `$set` stage creates two new fields, `product_name`
and `product_category`, from the values in the
`product_mapping` object field:

```c
"{", "$set", "{", "product_mapping", "{", "$first", BCON_UTF8("$product_mapping"), "}", "}", "}",
"{", "$set", "{",
"product_name", BCON_UTF8("$product_mapping.name"),
"product_category", BCON_UTF8("$product_mapping.category"),
"}", "}",
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from
this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("product_id"), BCON_UTF8("product_mapping"), "]", "}",
```

**Step 5: Run the aggregation pipeline.**

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
mongoc_collection_destroy(products);
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
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{ "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : { "$numberLong" : "1590822952000" } }, "value" : { "$numberDouble" : "431.43000000000000682" }, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
{ "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : { "$numberLong" : "1577869537000" } }, "value" : { "$numberDouble" : "63.130000000000002558" }, "product_name" : "Morphy Richardds Food Mixer", "product_category" : "KITCHENWARE" }
{ "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" : { "$numberLong" : "1608976546000" } }, "value" : { "$numberDouble" : "429.64999999999997726" }, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```cpp
auto orders = db["orders"];
auto products = db["products"];

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "product_id": "a1b2c3d4",
        "value": 431.43
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559062412},
        "product_id": "z9y8x7w6",
        "value": 5.01
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137},
        "product_id": "ff11gg22hh33",
        "value": 63.13
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "jjones@tepidmail.com",
        "orderdate": {"$date": 1608972946000},
        "product_id": "a1b2c3d4",
        "value": 429.65
    })")
};

orders.insert_many(order_docs); // Might throw an exception

std::vector<bsoncxx::document::value> product_docs = {
    bsoncxx::from_json(R"({
        "id": "a1b2c3d4",
        "name": "Asus Laptop",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students"
    })"),
    bsoncxx::from_json(R"({
        "id": "z9y8x7w6",
        "name": "The Day Of The Triffids",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "id": "ff11gg22hh33",
        "name": "Morphy Richardds Food Mixer",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great"
    })"),
    bsoncxx::from_json(R"({
        "id": "pqr678st",
        "name": "Karcher Hose Set",
        "category": "GARDEN",
        "description": "Hose + nosels + winder for tidy storage"
    })")
};

products.insert_many(product_docs); // Might throw an exception
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orderdate": {
        "$gte": {"$date": 1577836800},
        "$lt": {"$date": 1609459200000}
    }
})"));
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```cpp
pipeline.lookup(bsoncxx::from_json(R"({
    "from": "products",
    "localField": "product_id",
    "foreignField": "id",
    "as": "product_mapping"
})"));
```

**Step 3: Add addFields stages to create new document fields.**

Next, add two `$addFields`
stages to the pipeline.

The first `$addFields` stage sets the `product_mapping` field
to the first element in the `product_mapping` object
created in the previous `$lookup` stage. 

The second `$addFields` stage creates two new fields, `product_name`
and `product_category`, from the values in the
`product_mapping` object field:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_mapping": {"$first": "$product_mapping"}
})"));
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_name": "$product_mapping.name",
    "product_category": "$product_mapping.category"
})"));
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "product_id", "product_mapping"]
})"));
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{ "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : "2020-05-30T06:55:52Z" },
"value" : 431.43000000000000682, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
{ "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : "1970-01-19T06:17:41.137Z" },
"value" : 63.130000000000002558, "product_name" : "Morphy Richardds Food Mixer", "product_category" : "KITCHENWARE" }
{ "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" : "2020-12-26T08:55:46Z" },
"value" : 429.64999999999997726, "product_name" : "Asus Laptop", "product_category" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```javascript
const orders = aggDB.collection("orders");
const products = aggDB.collection("products");

await orders.deleteMany({});
await products.deleteMany({});

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    product_id: "a1b2c3d4",
    value: 431.43,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    product_id: "z9y8x7w6",
    value: 5.01,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    product_id: "ff11gg22hh33",
    value: 63.13,
  },
  {
    customer_id: "jjones@tepidmail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    product_id: "a1b2c3d4",
    value: 429.65,
  },
]);

await products.insertMany([
  {
    id: "a1b2c3d4",
    name: "Asus Laptop",
    category: "ELECTRONICS",
    description: "Good value laptop for students",
  },
  {
    id: "z9y8x7w6",
    name: "The Day Of The Triffids",
    category: "BOOKS",
    description: "Classic post-apocalyptic novel",
  },
  {
    id: "ff11gg22hh33",
    name: "Morphy Richardds Food Mixer",
    category: "KITCHENWARE",
    description: "Luxury mixer turning good cakes into great",
  },
  {
    id: "pqr678st",
    name: "Karcher Hose Set",
    category: "GARDEN",
    description: "Hose + nosels + winder for tidy storage",
  },
]);
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```javascript
pipeline.push({
  $lookup: {
    from: "products",
    localField: "product_id",
    foreignField: "id",
    as: "product_mapping",
  },
});
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

```javascript
pipeline.push(
  {
    $set: {
      product_mapping: { $first: "$product_mapping" },
    },
  },
  {
    $set: {
      product_name: "$product_mapping.name",
      product_category: "$product_mapping.category",
    },
  }
);
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```javascript
pipeline.push({ $unset: ["_id", "product_id", "product_mapping"] });
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```javascript
{
  customer_id: 'elise_smith@myemail.com',
  orderdate: 2020-05-30T08:35:52.000Z,
  value: 431.43,
  product_name: 'Asus Laptop',
  product_category: 'ELECTRONICS'
}
{
  customer_id: 'oranieri@warmmail.com',
  orderdate: 2020-01-01T08:25:37.000Z,
  value: 63.13,
  product_name: 'Morphy Richardds Food Mixer',
  product_category: 'KITCHENWARE'
}
{
  customer_id: 'jjones@tepidmail.com',
  orderdate: 2020-12-26T08:55:46.000Z,
  value: 429.65,
  product_name: 'Asus Laptop',
  product_category: 'ELECTRONICS'
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$products = $client->agg_tutorials_db->products;

$orders->deleteMany([]);
$products->deleteMany([]);

$orders->insertMany(
    [
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-05-30T08:35:52')),
            'product_id' => 'a1b2c3d4',
            'value' => 431.43
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2019-05-28T19:13:32')),
            'product_id' => 'z9y8x7w6',
            'value' => 5.01
        ],
        [
            'customer_id' => 'oranieri@warmmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-01T08:25:37')),
            'product_id' => 'ff11gg22hh33',
            'value' => 63.13,
        ],
        [
            'customer_id' => 'jjones@tepidmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-12-26T08:55:46')),
            'product_id' => 'a1b2c3d4',
            'value' => 429.65
        ],
    ]
);

$products->insertMany(
    [
        [
            'id' => 'a1b2c3d4',
            'name' => 'Asus Laptop',
            'category' => 'ELECTRONICS',
            'description' => 'Good value laptop for students',
        ],
        [
            'id' => 'z9y8x7w6',
            'name' => 'The Day Of The Triffids',
            'category' => 'BOOKS',
            'description' => 'Classic post-apocalyptic novel',
        ],
        [
            'id' => 'ff11gg22hh33',
            'name' => 'Morphy Richardds Food Mixer',
            'category' => 'KITCHENWARE',
            'description' => 'Luxury mixer turning good cakes into great',
        ],
        [
            'id' => 'pqr678st',
            'name' => 'Karcher Hose Set',
            'category' => 'GARDEN',
            'description' => 'Hose + nosels + winder for tidy storage',
        ],
    ]
);
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

**Step 2: Add a lookup stage to link the collections.**

Outside of your `Pipeline` instance, create a `$lookup` stage in a factory
function. The`$lookup` stage joins the `product_id` field in
the `orders` collection to the `id` field in the `products`
collection:

```php
function lookupProductsStage()
{
    return Stage::lookup(
        from: 'products',
        localField: 'product_id',
        foreignField: 'id',
        as: 'product_mapping',
    );
}
```

Then, in your `Pipeline` instance, call the
`lookupProductsStage()` function:

```php
function lookupProductsStage()
{
    return Stage::lookup(
        from: 'products',
        localField: 'product_id',
        foreignField: 'id',
        as: 'product_mapping',
    );
}
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

```php
Stage::set(
    product_mapping: Expression::first(
        Expression::arrayFieldPath('product_mapping')
    )
),
Stage::set(
    product_name: Expression::stringFieldPath('product_mapping.name'),
    product_category: Expression::stringFieldPath('product_mapping.category')
),
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```php
Stage::unset('_id', 'product_id', 'product_mapping')
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{
    "customer_id": "elise_smith@myemail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1590827752000"
        }
    },
    "value": 431.43,
    "product_name": "Asus Laptop",
    "product_category": "ELECTRONICS"
}
{
    "customer_id": "oranieri@warmmail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1577867137000"
        }
    },
    "value": 63.13,
    "product_name": "Morphy Richardds Food Mixer",
    "product_category": "KITCHENWARE"
}
{
    "customer_id": "jjones@tepidmail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1608972946000"
        }
    },
    "value": 429.65,
    "product_name": "Asus Laptop",
    "product_category": "ELECTRONICS"
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```ruby
orders = agg_db[:orders]
products = agg_db[:products]

orders.delete_many({})
products.delete_many({})

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      product_id: "a1b2c3d4",
      value: 431.43,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      product_id: "z9y8x7w6",
      value: 5.01,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      product_id: "ff11gg22hh33",
      value: 63.13,
    },
    {
      customer_id: "jjones@tepidmail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      product_id: "a1b2c3d4",
      value: 429.65,
    },
  ]
)

products.insert_many(
  [
    {
      id: "a1b2c3d4",
      name: "Asus Laptop",
      category: "ELECTRONICS",
      description: "Good value laptop for students",
    },
    {
      id: "z9y8x7w6",
      name: "The Day Of The Triffids",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      id: "ff11gg22hh33",
      name: "Morphy Richardds Food Mixer",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great",
    },
    {
      id: "pqr678st",
      name: "Karcher Hose Set",
      category: "GARDEN",
      description: "Hose + nosels + winder for tidy storage",
    },
  ]
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```ruby
{
  "$lookup": {
    from: "products",
    localField: "product_id",
    foreignField: "id",
    as: "product_mapping",
  },
},
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

```ruby
{
  "$set": {
    product_mapping: { "$first": "$product_mapping" },
  },
},
{
  "$set": {
    product_name: "$product_mapping.name",
    product_category: "$product_mapping.category",
  },
},
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```ruby
{ "$unset": ["_id", "product_id", "product_mapping"] },
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id"=>"elise_smith@myemail.com", "orderdate"=>2020-05-30 08:35:52 UTC, "value"=>431.43, "product_name"=>"Asus Laptop", "product_category"=>"ELECTRONICS"}
{"customer_id"=>"oranieri@warmmail.com", "orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63.13, "product_name"=>"Morphy Richardds Food Mixer", "product_category"=>"KITCHENWARE"}
{"customer_id"=>"jjones@tepidmail.com", "orderdate"=>2020-12-26 08:55:46 UTC, "value"=>429.65, "product_name"=>"Asus Laptop", "product_category"=>"ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Go structs to model the data in the `orders` and `products`
collections:

```go
type Order struct {
	CustomerID string        `bson:"customer_id"`
	OrderDate  bson.DateTime `bson:"orderdate"`
	ProductID  string        `bson:"product_id"`
	Value      float32       `bson:"value"`
}

type Product struct {
	ID          string `bson:"id"`
	Name        string `bson:"name"`
	Category    string `bson:"category"`
	Description string `bson:"description"`
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```go
orders := aggDB.Collection("orders")
products := aggDB.Collection("products")
orders.DeleteMany(context.TODO(), bson.D{})
products.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 52, 0, time.UTC)),
		ProductID:  "a1b2c3d4",
		Value:      431.43,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		ProductID:  "z9y8x7w6",
		Value:      5.01,
	},
	Order{
		CustomerID: "oranieri@warmmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 01, 01, 8, 25, 37, 0, time.UTC)),
		ProductID:  "ff11gg22hh33",
		Value:      63.13,
	},
	Order{
		CustomerID: "jjones@tepidmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		ProductID:  "a1b2c3d4",
		Value:      429.65,
	},
})
if err != nil {
	log.Fatal(err)
}

_, err = products.InsertMany(context.TODO(), []interface{}{
	Product{
		ID:          "a1b2c3d4",
		Name:        "Asus Laptop",
		Category:    "ELECTRONICS",
		Description: "Good value laptop for students",
	},
	Product{
		ID:          "z9y8x7w6",
		Name:        "The Day Of The Triffids",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		ID:          "ff11gg22hh33",
		Name:        "Morphy Richardds Food Mixer",
		Category:    "KITCHENWARE",
		Description: "Luxury mixer turning good cakes into great",
	},
	Product{
		ID:          "pqr678st",
		Name:        "Karcher Hose Set",
		Category:    "GARDEN",
		Description: "Hose + nosels + winder for tidy storage",
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "orderdate", Value: bson.D{
		{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
		{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
	}},
}}}
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```go
lookupStage := bson.D{{Key: "$lookup", Value: bson.D{
	{Key: "from", Value: "products"},
	{Key: "localField", Value: "product_id"},
	{Key: "foreignField", Value: "id"},
	{Key: "as", Value: "product_mapping"},
}}}
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

```go
setStage1 := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_mapping", Value: bson.D{{Key: "$first", Value: "$product_mapping"}}},
}}}

setStage2 := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_name", Value: "$product_mapping.name"},
	{Key: "product_category", Value: "$product_mapping.category"},
}}}
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id", "product_id", "product_mapping"}}}
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{matchStage, lookupStage, setStage1, setStage2, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id":"elise_smith@myemail.com","orderdate":{"$date":"2020-05-30T08:35:52Z"},"value":431.42999267578125,"product_name":"Asus Laptop","product_category":"ELECTRONICS"}
{"customer_id":"oranieri@warmmail.com","orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63.130001068115234,"product_name":"Morphy Richardds Food Mixer","product_category":"KITCHENWARE"}
{"customer_id":"jjones@tepidmail.com","orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":429.6499938964844,"product_name":"Asus Laptop","product_category":"ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.

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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Rust structs to model the data in the `orders` and `products`
collections:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    order_date: DateTime,
    product_id: String,
    value: f32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Product {
    id: String,
    name: String,
    category: String,
    description: String,
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```rust
let orders: Collection<Order> = agg_db.collection("orders");
let products: Collection<Product> = agg_db.collection("products");

orders.delete_many(doc! {}).await?;
products.delete_many(doc! {}).await?;

let order_docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(52).build().unwrap(),
        product_id: "a1b2c3d4".to_string(),
        value: 431.43,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        order_date: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        product_id: "z9y8x7w6".to_string(),
        value: 5.01,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        product_id: "ff11gg22hh33".to_string(),
        value: 63.13,
    },
    Order {
        customer_id: "jjones@tepidmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        product_id: "a1b2c3d4".to_string(),
        value: 429.65,
    },
];
orders.insert_many(order_docs).await?;

let product_docs = vec![
    Product {
        id: "a1b2c3d4".to_string(),
        name: "Asus Laptop".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Good value laptop for students".to_string(),
    },
    Product {
        id: "z9y8x7w6".to_string(),
        name: "The Day Of The Triffids".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        id: "ff11gg22hh33".to_string(),
        name: "Morphy Richardds Food Mixer".to_string(),
        category: "KITCHENWARE".to_string(),
        description: "Luxury mixer turning good cakes into great".to_string(),
    },
    Product {
        id: "pqr678st".to_string(),
        name: "Karcher Hose Set".to_string(),
        category: "GARDEN".to_string(),
        description: "Hose + nosels + winder for tidy storage".to_string(),
    },
];
products.insert_many(product_docs).await?;
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```rust
pipeline.push(doc! {
    "$match": {
        "order_date": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap()
        }
    }
});
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```rust
pipeline.push(doc! {
    "$lookup": {
        "from": "products",
        "localField": "product_id",
        "foreignField": "id",
        "as": "product_mapping"
    }
});
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

```rust
pipeline.push(doc! {
    "$set": {
        "product_mapping": { "$first": "$product_mapping" }
    }
});

pipeline.push(doc! {
    "$set": {
        "product_name": "$product_mapping.name",
        "product_category": "$product_mapping.category"
    }
});
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```rust
pipeline.push(doc! {
    "$unset": ["_id", "product_id", "product_mapping"]
});
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
Document({"customer_id": String("elise_smith@myemail.com"), "order_date": DateTime(2020-05-30 8:35:52.0 +00:00:00),
"value": Double(431.42999267578125), "product_name": String("Asus Laptop"), "product_category": String("ELECTRONICS")})

Document({"customer_id": String("oranieri@warmmail.com"), "order_date": DateTime(2020-01-01 8:25:37.0 +00:00:00),
"value": Double(63.130001068115234), "product_name": String("Morphy Richardds Food Mixer"), "product_category": String("KITCHENWARE")})

Document({"customer_id": String("jjones@tepidmail.com"), "order_date": DateTime(2020-12-26 8:55:46.0 +00:00:00),
"value": Double(429.6499938964844), "product_name": String("Asus Laptop"), "product_category": String("ELECTRONICS")})
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.
