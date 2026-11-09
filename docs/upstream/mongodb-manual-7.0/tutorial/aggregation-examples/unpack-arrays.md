<!-- Converted from tutorial/aggregation-examples/unpack-arrays.txt (reStructuredText). Includes are inlined. -->

# Unwind Arrays and Group Data

This tutorial illustrates how to construct an aggregation pipeline,
perform the aggregation on a collection, and display the results using
the language of your choice.

## About This Task

This tutorial demonstrates how to create insights from customer order
data. The results show the list of products ordered that cost more than
$15. Each document contains the number of units sold and the total
sale value for each product.

The aggregation pipeline performs the following operations:

- Unwinds an array field into separate documents
- Matches a subset of documents by a field value
- Groups documents by common field values
- Adds computed fields to each result document

## Before You Begin

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      order_id: 6363763262239,
      products: [
         {
            prod_id: "abc12345",
            name: "Asus Laptop",
            price: 431
         },
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 22
         }
      ]
   },
   {
      order_id: 1197372932325,
      products: [
         {
            prod_id: "abc12345",
            name: "Asus Laptop",
            price: 429
         }
      ]
   },
   {
      order_id: 9812343774839,
      products: [
         {
            prod_id: "pqr88223",
            name: "Morphy Richards Food Mixer",
            price: 431
         },
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 21
         }
      ]
   },
   {
      order_id: 4433997244387,
      products: [
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 23
         },
         {
            prod_id: "jkl77336",
            name: "Picky Pencil Sharpener",
            price: 1
         },
         {
            prod_id: "xyz11228",
            name: "Russell Hobbs Chrome Kettle",
            price: 16
         }
      ]
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [ 

   // Stage 1: Unwind the array of product orders
   { $unwind: { path: "$products" } },

   // Stage 2: Match products that cost more than $15
   { $match: { "products.price": { $gt: 15 } } },

   // Stage 3: Group products by product type
   { $group:
      {
         _id: "$products.prod_id",
         product: { $first: "$products.name"  },
         total_value: { $sum: "$products.price" },
         quantity: { $sum: 1 }
      }
   },

   // Stage 4: Display the product ID
   { $set: { product_id: "$_id" } },

   // Stage 5: Remove unneeded fields
   { $unset: [ "_id"] }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  product: 'Asus Laptop',
  total_value: 860,
  quantity: 2,
  product_id: 'abc12345'
}
{
  product: 'Morphy Richards Food Mixer',
  total_value: 431,
  quantity: 1,
  product_id: 'pqr88223'
}
{
  product: 'Russell Hobbs Chrome Kettle',
  total_value: 16,
  quantity: 1,
  product_id: 'xyz11228'
}
{
  product: 'Karcher Hose Set',
  total_value: 66,
  quantity: 3,
  product_id: 'def45678'
}
```

**Note:**

If you run this example, the order of documents in your results
might differ from the order of documents on this page because the
aggregation pipeline does not contain a sort stage. 

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```python
orders_coll = agg_db["orders"]
orders_coll.delete_many({})

order_data = [
    {
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22,
            },
        ],
    },
    {
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429,
            }
        ],
    },
    {
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21,
            },
        ],
    },
    {
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23,
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1,
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16,
            },
        ],
    },
]

orders_coll.insert_many(order_data)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```python
pipeline.append({"$unwind": {"path": "$products"}})
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```python
pipeline.append({"$match": {"products.price": {"$gt": 15}}})
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```python
pipeline.append(
    {
        "$group": {
            "_id": "$products.prod_id",
            "product": {"$first": "$products.name"},
            "total_value": {"$sum": "$products.price"},
            "quantity": {"$sum": 1},
        }
    }
)
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```python
pipeline.append({"$set": {"product_id": "$_id"}})
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```python
pipeline.append({"$unset": ["_id"]})
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{'product': 'Morphy Richards Food Mixer', 'total_value': 431, 'quantity': 1, 'product_id': 'pqr88223'}
{'product': 'Asus Laptop', 'total_value': 860, 'quantity': 2, 'product_id': 'abc12345'}
{'product': 'Russell Hobbs Chrome Kettle', 'total_value': 16, 'quantity': 1, 'product_id': 'xyz11228'}
{'product': 'Karcher Hose Set', 'total_value': 66, 'quantity': 3, 'product_id': 'def45678'}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```java
MongoCollection<Document> orders = aggDB.getCollection("orders");
orders.deleteMany(Filters.empty());

orders.insertMany(
        Arrays.asList(
                new Document("order_id", 6363763262239f)
                        .append("products", Arrays.asList(
                                new Document("prod_id", "abc12345")
                                        .append("name", "Asus Laptop")
                                        .append("price", 431),
                                new Document("prod_id", "def45678")
                                        .append("name", "Karcher Hose Set")
                                        .append("price", 22)
                        )),
                new Document("order_id", 1197372932325f)
                        .append("products", Collections.singletonList(
                                new Document("prod_id", "abc12345")
                                        .append("name", "Asus Laptop")
                                        .append("price", 429)
                        )),
                new Document("order_id", 9812343774839f)
                        .append("products", Arrays.asList(
                                new Document("prod_id", "pqr88223")
                                        .append("name", "Morphy Richards Food Mixer")
                                        .append("price", 431),
                                new Document("prod_id", "def45678")
                                        .append("name", "Karcher Hose Set")
                                        .append("price", 21)
                                )),
                new Document("order_id", 4433997244387f)
                        .append("products", Arrays.asList(
                                new Document("prod_id", "def45678")
                                        .append("name", "Karcher Hose Set")
                                        .append("price", 23),
                                new Document("prod_id", "jkl77336")
                                        .append("name", "Picky Pencil Sharpener")
                                        .append("price", 1),
                                new Document("prod_id", "xyz11228")
                                        .append("name", "Russell Hobbs Chrome Kettle")
                                        .append("price", 16)
                                ))
        )
);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```java
pipeline.add(Aggregates.unwind("$products"));
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```java
pipeline.add(Aggregates.match(
        Filters.gt("products.price", 15)
));
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```java
pipeline.add(Aggregates.group(
        "$products.prod_id",
        Accumulators.first("product", "$products.name"),
        Accumulators.sum("total_value", "$products.price"),
        Accumulators.sum("quantity", 1)
));
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```java
pipeline.add(Aggregates.set(new Field<>("product_id", "$_id")));
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```java
pipeline.add(Aggregates.unset("_id"));
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```java
AggregateIterable<Document> aggregationResult = orders.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product": "Asus Laptop", "total_value": 860, "quantity": 2, "product_id": "abc12345"}
{"product": "Russell Hobbs Chrome Kettle", "total_value": 16, "quantity": 1, "product_id": "xyz11228"}
{"product": "Karcher Hose Set", "total_value": 66, "quantity": 3, "product_id": "def45678"}
{"product": "Morphy Richards Food Mixer", "total_value": 431, "quantity": 1, "product_id": "pqr88223"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Kotlin data classes to model the data in the `orders`
collection:

```kotlin
@Serializable
data class Order(
    val orderID: Float,
    val products: List<Product>
)

@Serializable
data class Product(
    val prodID: String,
    val name: String,
    val price: Int
)
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```kotlin
val orders = aggDB.getCollection<Order>("orders")
orders.deleteMany(Filters.empty())

orders.insertMany(
    listOf(
        Order(
            6363763262239f, listOf(
                Product("abc12345", "Asus Laptop", 431),
                Product("def45678", "Karcher Hose Set", 22)
            )
        ),
        Order(
            1197372932325f, listOf(
                Product("abc12345", "Asus Laptop", 429)
            )
        ),
        Order(
            9812343774839f, listOf(
                Product("pqr88223", "Morphy Richards Food Mixer", 431),
                Product("def45678", "Karcher Hose Set", 21)
            )
        ),
        Order(
            4433997244387f, listOf(
                Product("def45678", "Karcher Hose Set", 23),
                Product("jkl77336", "Picky Pencil Sharpener", 1),
                Product("xyz11228", "Russell Hobbs Chrome Kettle", 16)
            )
        )
    )
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```kotlin
pipeline.add(
    Aggregates.unwind("\$${Order::products.name}")
)
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.gt("${Order::products.name}.${Product::price.name}", 15)
    )
)
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prodID` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```kotlin
pipeline.add(
    Aggregates.group(
        "\$${Order::products.name}.${Product::prodID.name}",
        Accumulators.first("product", "\$${Order::products.name}.${Product::name.name}"),
        Accumulators.sum("total_value", "\$${Order::products.name}.${Product::price.name}"),
        Accumulators.sum("quantity", 1)
    )
)
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```kotlin
pipeline.add(Aggregates.set(Field("product_id", "\$_id")))
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```kotlin
pipeline.add(Aggregates.unset("_id"))
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```kotlin
val aggregationResult = orders.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document{{product=Russell Hobbs Chrome Kettle, total_value=16, quantity=1, product_id=xyz11228}}
Document{{product=Karcher Hose Set, total_value=66, quantity=3, product_id=def45678}}
Document{{product=Morphy Richards Food Mixer, total_value=431, quantity=1, product_id=pqr88223}}
Document{{product=Asus Laptop, total_value=860, quantity=2, product_id=abc12345}}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```scala
val orders = aggDB.getCollection("orders")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

orders.insertMany(Seq(
  Document(
    "order_id" -> 6363763262239L,
    "products" -> Seq(
      Document(
        "prod_id" -> "abc12345",
        "name" -> "Asus Laptop",
        "price" -> 431
      ),
      Document(
        "prod_id" -> "def45678",
        "name" -> "Karcher Hose Set",
        "price" -> 22
      )
    )
  ),
  Document(
    "order_id" -> 1197372932325L,
    "products" -> Seq(
      Document(
        "prod_id" -> "abc12345",
        "name" -> "Asus Laptop",
        "price" -> 429
      )
    )
  ),
  Document(
    "order_id" -> 9812343774839L,
    "products" -> Seq(
      Document(
        "prod_id" -> "pqr88223",
        "name" -> "Morphy Richards Food Mixer",
        "price" -> 431
      ),
      Document(
        "prod_id" -> "def45678",
        "name" -> "Karcher Hose Set",
        "price" -> 21
      )
    )
  ),
  Document(
    "order_id" -> 4433997244387L,
    "products" -> Seq(
      Document(
        "prod_id" -> "def45678",
        "name" -> "Karcher Hose Set",
        "price" -> 23
      ),
      Document(
        "prod_id" -> "jkl77336",
        "name" -> "Picky Pencil Sharpener",
        "price" -> 1
      ),
      Document(
        "prod_id" -> "xyz11228",
        "name" -> "Russell Hobbs Chrome Kettle",
        "price" -> 16
      )
    )
  )
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```scala
Aggregates.unwind("$products"),
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```scala
Aggregates.filter(Filters.gt("products.price", 15)),
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```scala
Aggregates.group(
  "$products.prod_id",
  Accumulators.first("product", "$products.name"),
  Accumulators.sum("total_value", "$products.price"),
  Accumulators.sum("quantity", 1)
),
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```scala
Aggregates.set(Field("product_id", "$_id")),
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```scala
Aggregates.unset("_id")
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product": "Morphy Richards Food Mixer", "total_value": 431, "quantity": 1, "product_id": "pqr88223"}
{"product": "Karcher Hose Set", "total_value": 66, "quantity": 3, "product_id": "def45678"}
{"product": "Russell Hobbs Chrome Kettle", "total_value": 16, "quantity": 1, "product_id": "xyz11228"}
{"product": "Asus Laptop", "total_value": 860, "quantity": 2, "product_id": "abc12345"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create C# classes to model the data in the `orders`
collection:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public long OrderId { get; set; }
  public List<Product> Products { get; set; }
}

public class OrderUnwound
{
  public long OrderId { get; set; }
  public Product Products { get; set; }
}

public class Product
{
  public string ProductId { get; set; }
  public string Name { get; set; }
  public int Price { get; set; }
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
            OrderId = 6363763262239L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "abc12345",
                    Name = "Asus Laptop",
                    Price = 431
                },
                new Product
                {
                    ProductId = "def45678",
                    Name = "Karcher Hose Set",
                    Price = 22
                }
            }
        },
        new Order
        {
            OrderId = 1197372932325L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "abc12345",
                    Name = "Asus Laptop",
                    Price = 429
                }
            }
        },
        new Order
        {
            OrderId = 9812343774839L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "pqr88223",
                    Name = "Morphy Richards Food Mixer",
                    Price = 431
                },
                new Product
                {
                    ProductId = "def45678",
                    Name = "Karcher Hose Set",
                    Price = 21
                }
            }
        },
        new Order
        {
            OrderId = 4433997244387L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "def45678",
                    Name = "Karcher Hose Set",
                    Price = 23
                },
                new Product
                {
                    ProductId = "jkl77336",
                    Name = "Picky Pencil Sharpener",
                    Price = 1
                },
                new Product
                {
                    ProductId = "xyz11228",
                    Name = "Russell Hobbs Chrome Kettle",
                    Price = 16
                }
            }
        }
    });
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, start the aggregation on the `orders` collection and
chain an `$unwind` stage to separate the
entries in the `Products` array into individual documents:

```csharp
var results = orders.Aggregate()
    .Unwind<Order, OrderUnwound>(o => o.Products)
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `Products.Price` value greater than `15`:

```csharp
.Match(o => o.Products.Price > 15)
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `ProductId` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `ProductId`: the product ID (the grouping key)
- `Product`: the product name
- `TotalValue`: the total value of all the sales of the product
- `Quantity`: the number of orders for the product

```csharp
.Group(
    id: o => o.Products.ProductId,
    group: g => new
    {
      ProductId = g.Key,
      Product = g.First().Products.Name,
      TotalValue = g.Sum(o => o.Products.Price),
      Quantity = g.Count(),
    }
);
```

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ ProductId = pqr88223, Product = Morphy Richards Food Mixer, TotalValue = 431, Quantity = 1 }
{ ProductId = xyz11228, Product = Russell Hobbs Chrome Kettle, TotalValue = 16, Quantity = 1 }
{ ProductId = abc12345, Product = Asus Laptop, TotalValue = 860, Quantity = 2 }
{ ProductId = def45678, Product = Karcher Hose Set, TotalValue = 66, Quantity = 3 }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

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
    size_t num_docs = 4;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "order_id", BCON_INT64(6363763262239),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("abc12345"),
        "name", BCON_UTF8("Asus Laptop"),
        "price", BCON_INT32(431),
        "}",
        "{",
        "prod_id", BCON_UTF8("def45678"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "price", BCON_INT32(22),
        "}",
        "]");

    docs[1] = BCON_NEW(
        "order_id", BCON_INT64(1197372932325),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("abc12345"),
        "name", BCON_UTF8("Asus Laptop"),
        "price", BCON_INT32(429),
        "}",
        "]");

    docs[2] = BCON_NEW(
        "order_id", BCON_INT64(9812343774839),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("pqr88223"),
        "name", BCON_UTF8("Morphy Richards Food Mixer"),
        "price", BCON_INT32(431),
        "}",
        "{",
        "prod_id", BCON_UTF8("def45678"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "price", BCON_INT32(21),
        "}",
        "]");

    docs[3] = BCON_NEW(
        "order_id", BCON_INT64(4433997244387),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("def45678"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "price", BCON_INT32(23),
        "}",
        "{",
        "prod_id", BCON_UTF8("jkl77336"),
        "name", BCON_UTF8("Picky Pencil Sharpener"),
        "price", BCON_INT32(1),
        "}",
        "{",
        "prod_id", BCON_UTF8("xyz11228"),
        "name", BCON_UTF8("Russell Hobbs Chrome Kettle"),
        "price", BCON_INT32(16),
        "}",
        "]");

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

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```c
"{", "$unwind", "{", "path", BCON_UTF8("$products"), "}", "}",
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```c
"{", "$match", "{", "products.price", "{", "$gt", BCON_INT32(15), "}", "}", "}",
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```c
"{", "$group", "{",
"_id", BCON_UTF8("$products.prod_id"),
"product", "{", "$first", BCON_UTF8("$products.name"), "}",
"total_value", "{", "$sum", BCON_UTF8("$products.price"), "}",
"quantity", "{", "$sum", BCON_INT32(1), "}",
"}", "}",
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```c
"{", "$set", "{", "product_id", BCON_UTF8("$_id"), "}", "}",
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), "]", "}",
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "product" : "Asus Laptop", "total_value" : { "$numberInt" : "860" }, "quantity" : { "$numberInt" : "2" }, "product_id" : "abc12345" }
{ "product" : "Karcher Hose Set", "total_value" : { "$numberInt" : "66" }, "quantity" : { "$numberInt" : "3" }, "product_id" : "def45678" }
{ "product" : "Morphy Richards Food Mixer", "total_value" : { "$numberInt" : "431" }, "quantity" : { "$numberInt" : "1" }, "product_id" : "pqr88223" }
{ "product" : "Russell Hobbs Chrome Kettle", "total_value" : { "$numberInt" : "16" }, "quantity" : { "$numberInt" : "1" }, "product_id" : "xyz11228" }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```cpp
auto orders = db["orders"];

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16
            }
        ]
    })")
};
orders.insert_many(order_docs); // Might throw an exception
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```cpp
pipeline.unwind("$products");
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "products.price": { "$gt": 15 }
})"));
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```cpp
pipeline.group(bsoncxx::from_json(R"({
    "_id": "$products.prod_id",
    "product": { "$first": "$products.name" },
    "total_value": { "$sum": "$products.price" },
    "quantity": { "$sum": 1 }
})"));
```

**Step 4: Add an addFields stage to display the product ID.**

Add an `$addFields` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_id": "$_id"
})"));
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id"]
})"));
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "product" : "Karcher Hose Set", "total_value" : 66, "quantity" : 3, "product_id" : "def45678" }
{ "product" : "Asus Laptop", "total_value" : 860, "quantity" : 2, "product_id" : "abc12345" }
{ "product" : "Morphy Richards Food Mixer", "total_value" : 431, "quantity" : 1, "product_id" : "pqr88223" }
{ "product" : "Russell Hobbs Chrome Kettle", "total_value" : 16, "quantity" : 1, "product_id" : "xyz11228" }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```javascript
const orders = aggDB.collection("orders");
await orders.deleteMany({});

await orders.insertMany([
  {
    order_id: 6363763262239,
    products: [
      {
        prod_id: "abc12345",
        name: "Asus Laptop",
        price: 431,
      },
      {
        prod_id: "def45678",
        name: "Karcher Hose Set",
        price: 22,
      },
    ],
  },
  {
    order_id: 1197372932325,
    products: [
      {
        prod_id: "abc12345",
        name: "Asus Laptop",
        price: 429,
      },
    ],
  },
  {
    order_id: 9812343774839,
    products: [
      {
        prod_id: "pqr88223",
        name: "Morphy Richards Food Mixer",
        price: 431,
      },
      {
        prod_id: "def45678",
        name: "Karcher Hose Set",
        price: 21,
      },
    ],
  },
  {
    order_id: 4433997244387,
    products: [
      {
        prod_id: "def45678",
        name: "Karcher Hose Set",
        price: 23,
      },
      {
        prod_id: "jkl77336",
        name: "Picky Pencil Sharpener",
        price: 1,
      },
      {
        prod_id: "xyz11228",
        name: "Russell Hobbs Chrome Kettle",
        price: 16,
      },
    ],
  },
]);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```javascript
pipeline.push({
  $unwind: {
    path: "$products",
  },
});
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```javascript
pipeline.push({
  $match: {
    "products.price": {
      $gt: 15,
    },
  },
});
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```javascript
pipeline.push({
  $group: {
    _id: "$products.prod_id",
    product: { $first: "$products.name" },
    total_value: { $sum: "$products.price" },
    quantity: { $sum: 1 },
  },
});
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```javascript
pipeline.push({
  $set: {
    product_id: "$_id",
  },
});
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```javascript
pipeline.push({ $unset: ["_id"] });
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  product: 'Asus Laptop',
  total_value: 860,
  quantity: 2,
  product_id: 'abc12345'
}
{
  product: 'Morphy Richards Food Mixer',
  total_value: 431,
  quantity: 1,
  product_id: 'pqr88223'
}
{
  product: 'Russell Hobbs Chrome Kettle',
  total_value: 16,
  quantity: 1,
  product_id: 'xyz11228'
}
{
  product: 'Karcher Hose Set',
  total_value: 66,
  quantity: 3,
  product_id: 'def45678'
}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$orders->deleteMany([]);

$orders->insertMany(
    [
        [
            'order_id' => 6363763262239,
            'products' => [
                [
                    'prod_id' => 'abc12345',
                    'name' => 'Asus Laptop',
                    'price' => 431,
                ],
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 22,
                ],
            ],
        ],
        [
            'order_id' => 1197372932325,
            'products' => [
                [
                    'prod_id' => 'abc12345',
                    'name' => 'Asus Laptop',
                    'price' => 429,
                ],
            ],
        ],
        [
            'order_id' => 9812343774839,
            'products' => [
                [
                    'prod_id' => 'pqr88223',
                    'name' => 'Morphy Richards Food Mixer',
                    'price' => 431,
                ],
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 21,
                ],
            ],
        ],
        [
            'order_id' => 4433997244387,
            'products' => [
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 23,
                ],
                [
                    'prod_id' => 'jkl77336',
                    'name' => 'Picky Pencil Sharpener',
                    'price' => 1,
                ],
                [
                    'prod_id' => 'xyz11228',
                    'name' => 'Russell Hobbs Chrome Kettle',
                    'price' => 16,
                ],
            ],
        ]
    ]
);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```php
Stage::unwind(
    path: Expression::arrayFieldPath('products')
),
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```php
Stage::match(
    ['products.price' => Query::gt(15)]
),
```

**Step 3: Add a group stage to group by product type.**

Outside of your `Pipeline` instance, create a `$group` stage in a factory
function to collect order documents by the value of the
`prod_id` field. In this stage, add aggregation operations that
create the following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```php
function groupByProductStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('products.prod_id'),
        product: Accumulator::first(
            Expression::stringFieldPath('products.name')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('products.price'),
        ),
        quantity: Accumulator::sum(1)
    );
}
```

Then, in your `Pipeline` instance, call the
`groupByProductStage()` function:

```php
function groupByProductStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('products.prod_id'),
        product: Accumulator::first(
            Expression::stringFieldPath('products.name')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('products.price'),
        ),
        quantity: Accumulator::sum(1)
    );
}
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```php
Stage::set(product_id: Expression::stringFieldPath('_id')),
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```php
Stage::unset('_id')
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{
    "product": "Russell Hobbs Chrome Kettle",
    "total_value": 16,
    "quantity": 1,
    "product_id": "xyz11228"
}
{
    "product": "Asus Laptop",
    "total_value": 860,
    "quantity": 2,
    "product_id": "abc12345"
}
{
    "product": "Karcher Hose Set",
    "total_value": 66,
    "quantity": 3,
    "product_id": "def45678"
}
{
    "product": "Morphy Richards Food Mixer",
    "total_value": 431,
    "quantity": 1,
    "product_id": "pqr88223"
}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```ruby
orders = agg_db[:orders]
orders.delete_many({})

orders.insert_many(
  [
    {
      order_id: 6363763262239,
      products: [
        {
          prod_id: "abc12345",
          name: "Asus Laptop",
          price: 431,
        },
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 22,
        },
      ],
    },
    {
      order_id: 1197372932325,
      products: [
        {
          prod_id: "abc12345",
          name: "Asus Laptop",
          price: 429,
        },
      ],
    },
    {
      order_id: 9812343774839,
      products: [
        {
          prod_id: "pqr88223",
          name: "Morphy Richards Food Mixer",
          price: 431,
        },
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 21,
        },
      ],
    },
    {
      order_id: 4433997244387,
      products: [
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 23,
        },
        {
          prod_id: "jkl77336",
          name: "Picky Pencil Sharpener",
          price: 1,
        },
        {
          prod_id: "xyz11228",
          name: "Russell Hobbs Chrome Kettle",
          price: 16,
        },
      ],
    },
  ]
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```ruby
{
  "$unwind": {
    path: "$products",
  },
},
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```ruby
{
  "$match": {
    "products.price": {
      "$gt": 15,
    },
  },
},
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```ruby
{
  "$group": {
    _id: "$products.prod_id",
    product: { "$first": "$products.name" },
    total_value: { "$sum": "$products.price" },
    quantity: { "$sum": 1 },
  },
},
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```ruby
{
  "$set": {
    product_id: "$_id",
  },
},
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```ruby
{ "$unset": ["_id"] },
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product"=>"Asus Laptop", "total_value"=>860, "quantity"=>2, "product_id"=>"abc12345"}
{"product"=>"Russell Hobbs Chrome Kettle", "total_value"=>16, "quantity"=>1, "product_id"=>"xyz11228"}
{"product"=>"Karcher Hose Set", "total_value"=>66, "quantity"=>3, "product_id"=>"def45678"}
{"product"=>"Morphy Richards Food Mixer", "total_value"=>431, "quantity"=>1, "product_id"=>"pqr88223"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Go structs to model the data in the `orders`
collection:

```go
type Order struct {
	OrderID  int       `bson:"order_id"`
	Products []Product `bson:"products"`
}

type Product struct {
	ProductID string `bson:"prod_id"`
	Name      string `bson:"name"`
	Price     int    `bson:"price"`
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```go
orders := aggDB.Collection("orders")
orders.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		OrderID: 6363763262239,
		Products: []Product{
			{ProductID: "abc12345", Name: "Asus Laptop", Price: 431},
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 22},
		},
	},
	Order{
		OrderID: 1197372932325,
		Products: []Product{
			{ProductID: "abc12345", Name: "Asus Laptop", Price: 429},
		},
	},
	Order{
		OrderID: 9812343774839,
		Products: []Product{
			{ProductID: "pqr88223", Name: "Morphy Richards Food Mixer", Price: 431},
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 21},
		},
	},
	Order{
		OrderID: 4433997244387,
		Products: []Product{
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 23},
			{ProductID: "jkl77336", Name: "Picky Pencil Sharpene", Price: 1},
			{ProductID: "xyz11228", Name: "Russell Hobbs Chrome Kettle", Price: 16},
		},
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```go
unwindStage := bson.D{{Key: "$unwind", Value: bson.D{
	{Key: "path", Value: "$products"},
}}}
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "products.price", Value: bson.D{{Key: "$gt", Value: 15}}},
}}}
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```go
groupStage := bson.D{{Key: "$group", Value: bson.D{
	{Key: "_id", Value: "$products.prod_id"},
	{Key: "product", Value: bson.D{{Key: "$first", Value: "$products.name"}}},
	{Key: "total_value", Value: bson.D{{Key: "$sum", Value: "$products.price"}}},
	{Key: "quantity", Value: bson.D{{Key: "$sum", Value: 1}}},
}}}
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```go
setStage := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_id", Value: "$_id"},
}}}
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id"}}}
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{unwindStage, matchStage, groupStage, setStage, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product":"Morphy Richards Food Mixer","total_value":431,"quantity":1,"product_id":"pqr88223"}
{"product":"Russell Hobbs Chrome Kettle","total_value":16,"quantity":1,"product_id":"xyz11228"}
{"product":"Karcher Hose Set","total_value":66,"quantity":3,"product_id":"def45678"}
{"product":"Asus Laptop","total_value":860,"quantity":2,"product_id":"abc12345"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Rust structs to model the data in the `orders`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Product {
    prod_id: String,
    name: String,
    price: i32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Order {
    order_id: i64,
    products: Vec<Product>,
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```rust
let orders_coll: Collection<Order> = agg_db.collection("orders");
orders.delete_many(doc! {}).await?;

let orders = vec![
    Order {
        order_id: 6363763262239,
        products: vec![
            Product {
                prod_id: "abc12345".to_string(),
                name: "Asus Laptop".to_string(),
                price: 431,
            },
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 22,
            },
        ],
    },
    Order {
        order_id: 1197372932325,
        products: vec![Product {
            prod_id: "abc12345".to_string(),
            name: "Asus Laptop".to_string(),
            price: 429,
        }],
    },
    Order {
        order_id: 9812343774839,
        products: vec![
            Product {
                prod_id: "pqr88223".to_string(),
                name: "Morphy Richards Food Mixer".to_string(),
                price: 431,
            },
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 21,
            },
        ],
    },
    Order {
        order_id: 4433997244387,
        products: vec![
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 23,
            },
            Product {
                prod_id: "jkl77336".to_string(),
                name: "Picky Pencil Sharpene".to_string(),
                price: 1,
            },
            Product {
                prod_id: "xyz11228".to_string(),
                name: "Russell Hobbs Chrome Kettle".to_string(),
                price: 16,
            },
        ],
    },
];

orders_coll.insert_many(orders).await?;
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```rust
pipeline.push(doc! {
    "$unwind": {
        "path": "$products"
    }
});
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```rust
pipeline.push(doc! {
    "$match": {
        "products.price": { "$gt": 15 }
    }
});
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```rust
pipeline.push(doc! {
    "$group": {
        "_id": "$products.prod_id",
        "product": { "$first": "$products.name" },
        "total_value": { "$sum": "$products.price" },
        "quantity": { "$sum": 1 }
    }
});
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`prod_id` field from the values in the `_id` field
that were set during the `$group` stage:

```rust
pipeline.push(doc! {
    "$set": {
        "prod_id": "$_id"
    }
});
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```rust
pipeline.push(doc! {
    "$unset": ["_id"]
});
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```rust
let mut cursor = orders_coll.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document({"product": String("Russell Hobbs Chrome Kettle"), "total_value": Int32(16), "quantity": Int32(1),
"prod_id": String("xyz11228")})

Document({"product": String("Morphy Richards Food Mixer"), "total_value": Int32(431), "quantity": Int32(1),
"prod_id": String("pqr88223")})

Document({"product": String("Karcher Hose Set"), "total_value": Int32(66), "quantity": Int32(3),
"prod_id": String("def45678")})

Document({"product": String("Asus Laptop"), "total_value": Int32(860), "quantity": Int32(2),
"prod_id": String("abc12345")})
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to unpack array fields into separate documents and compute new
values based on groups of common values.

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      order_id: 6363763262239,
      products: [
         {
            prod_id: "abc12345",
            name: "Asus Laptop",
            price: 431
         },
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 22
         }
      ]
   },
   {
      order_id: 1197372932325,
      products: [
         {
            prod_id: "abc12345",
            name: "Asus Laptop",
            price: 429
         }
      ]
   },
   {
      order_id: 9812343774839,
      products: [
         {
            prod_id: "pqr88223",
            name: "Morphy Richards Food Mixer",
            price: 431
         },
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 21
         }
      ]
   },
   {
      order_id: 4433997244387,
      products: [
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 23
         },
         {
            prod_id: "jkl77336",
            name: "Picky Pencil Sharpener",
            price: 1
         },
         {
            prod_id: "xyz11228",
            name: "Russell Hobbs Chrome Kettle",
            price: 16
         }
      ]
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [ 

   // Stage 1: Unwind the array of product orders
   { $unwind: { path: "$products" } },

   // Stage 2: Match products that cost more than $15
   { $match: { "products.price": { $gt: 15 } } },

   // Stage 3: Group products by product type
   { $group:
      {
         _id: "$products.prod_id",
         product: { $first: "$products.name"  },
         total_value: { $sum: "$products.price" },
         quantity: { $sum: 1 }
      }
   },

   // Stage 4: Display the product ID
   { $set: { product_id: "$_id" } },

   // Stage 5: Remove unneeded fields
   { $unset: [ "_id"] }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  product: 'Asus Laptop',
  total_value: 860,
  quantity: 2,
  product_id: 'abc12345'
}
{
  product: 'Morphy Richards Food Mixer',
  total_value: 431,
  quantity: 1,
  product_id: 'pqr88223'
}
{
  product: 'Russell Hobbs Chrome Kettle',
  total_value: 16,
  quantity: 1,
  product_id: 'xyz11228'
}
{
  product: 'Karcher Hose Set',
  total_value: 66,
  quantity: 3,
  product_id: 'def45678'
}
```

**Note:**

If you run this example, the order of documents in your results
might differ from the order of documents on this page because the
aggregation pipeline does not contain a sort stage. 

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```python
orders_coll = agg_db["orders"]
orders_coll.delete_many({})

order_data = [
    {
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22,
            },
        ],
    },
    {
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429,
            }
        ],
    },
    {
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21,
            },
        ],
    },
    {
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23,
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1,
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16,
            },
        ],
    },
]

orders_coll.insert_many(order_data)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```python
pipeline.append({"$unwind": {"path": "$products"}})
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```python
pipeline.append({"$match": {"products.price": {"$gt": 15}}})
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```python
pipeline.append(
    {
        "$group": {
            "_id": "$products.prod_id",
            "product": {"$first": "$products.name"},
            "total_value": {"$sum": "$products.price"},
            "quantity": {"$sum": 1},
        }
    }
)
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```python
pipeline.append({"$set": {"product_id": "$_id"}})
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```python
pipeline.append({"$unset": ["_id"]})
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{'product': 'Morphy Richards Food Mixer', 'total_value': 431, 'quantity': 1, 'product_id': 'pqr88223'}
{'product': 'Asus Laptop', 'total_value': 860, 'quantity': 2, 'product_id': 'abc12345'}
{'product': 'Russell Hobbs Chrome Kettle', 'total_value': 16, 'quantity': 1, 'product_id': 'xyz11228'}
{'product': 'Karcher Hose Set', 'total_value': 66, 'quantity': 3, 'product_id': 'def45678'}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```java
MongoCollection<Document> orders = aggDB.getCollection("orders");
orders.deleteMany(Filters.empty());

orders.insertMany(
        Arrays.asList(
                new Document("order_id", 6363763262239f)
                        .append("products", Arrays.asList(
                                new Document("prod_id", "abc12345")
                                        .append("name", "Asus Laptop")
                                        .append("price", 431),
                                new Document("prod_id", "def45678")
                                        .append("name", "Karcher Hose Set")
                                        .append("price", 22)
                        )),
                new Document("order_id", 1197372932325f)
                        .append("products", Collections.singletonList(
                                new Document("prod_id", "abc12345")
                                        .append("name", "Asus Laptop")
                                        .append("price", 429)
                        )),
                new Document("order_id", 9812343774839f)
                        .append("products", Arrays.asList(
                                new Document("prod_id", "pqr88223")
                                        .append("name", "Morphy Richards Food Mixer")
                                        .append("price", 431),
                                new Document("prod_id", "def45678")
                                        .append("name", "Karcher Hose Set")
                                        .append("price", 21)
                                )),
                new Document("order_id", 4433997244387f)
                        .append("products", Arrays.asList(
                                new Document("prod_id", "def45678")
                                        .append("name", "Karcher Hose Set")
                                        .append("price", 23),
                                new Document("prod_id", "jkl77336")
                                        .append("name", "Picky Pencil Sharpener")
                                        .append("price", 1),
                                new Document("prod_id", "xyz11228")
                                        .append("name", "Russell Hobbs Chrome Kettle")
                                        .append("price", 16)
                                ))
        )
);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```java
pipeline.add(Aggregates.unwind("$products"));
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```java
pipeline.add(Aggregates.match(
        Filters.gt("products.price", 15)
));
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```java
pipeline.add(Aggregates.group(
        "$products.prod_id",
        Accumulators.first("product", "$products.name"),
        Accumulators.sum("total_value", "$products.price"),
        Accumulators.sum("quantity", 1)
));
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```java
pipeline.add(Aggregates.set(new Field<>("product_id", "$_id")));
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```java
pipeline.add(Aggregates.unset("_id"));
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```java
AggregateIterable<Document> aggregationResult = orders.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product": "Asus Laptop", "total_value": 860, "quantity": 2, "product_id": "abc12345"}
{"product": "Russell Hobbs Chrome Kettle", "total_value": 16, "quantity": 1, "product_id": "xyz11228"}
{"product": "Karcher Hose Set", "total_value": 66, "quantity": 3, "product_id": "def45678"}
{"product": "Morphy Richards Food Mixer", "total_value": 431, "quantity": 1, "product_id": "pqr88223"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Kotlin data classes to model the data in the `orders`
collection:

```kotlin
@Serializable
data class Order(
    val orderID: Float,
    val products: List<Product>
)

@Serializable
data class Product(
    val prodID: String,
    val name: String,
    val price: Int
)
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```kotlin
val orders = aggDB.getCollection<Order>("orders")
orders.deleteMany(Filters.empty())

orders.insertMany(
    listOf(
        Order(
            6363763262239f, listOf(
                Product("abc12345", "Asus Laptop", 431),
                Product("def45678", "Karcher Hose Set", 22)
            )
        ),
        Order(
            1197372932325f, listOf(
                Product("abc12345", "Asus Laptop", 429)
            )
        ),
        Order(
            9812343774839f, listOf(
                Product("pqr88223", "Morphy Richards Food Mixer", 431),
                Product("def45678", "Karcher Hose Set", 21)
            )
        ),
        Order(
            4433997244387f, listOf(
                Product("def45678", "Karcher Hose Set", 23),
                Product("jkl77336", "Picky Pencil Sharpener", 1),
                Product("xyz11228", "Russell Hobbs Chrome Kettle", 16)
            )
        )
    )
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```kotlin
pipeline.add(
    Aggregates.unwind("\$${Order::products.name}")
)
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.gt("${Order::products.name}.${Product::price.name}", 15)
    )
)
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prodID` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```kotlin
pipeline.add(
    Aggregates.group(
        "\$${Order::products.name}.${Product::prodID.name}",
        Accumulators.first("product", "\$${Order::products.name}.${Product::name.name}"),
        Accumulators.sum("total_value", "\$${Order::products.name}.${Product::price.name}"),
        Accumulators.sum("quantity", 1)
    )
)
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```kotlin
pipeline.add(Aggregates.set(Field("product_id", "\$_id")))
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```kotlin
pipeline.add(Aggregates.unset("_id"))
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```kotlin
val aggregationResult = orders.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document{{product=Russell Hobbs Chrome Kettle, total_value=16, quantity=1, product_id=xyz11228}}
Document{{product=Karcher Hose Set, total_value=66, quantity=3, product_id=def45678}}
Document{{product=Morphy Richards Food Mixer, total_value=431, quantity=1, product_id=pqr88223}}
Document{{product=Asus Laptop, total_value=860, quantity=2, product_id=abc12345}}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```scala
val orders = aggDB.getCollection("orders")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

orders.insertMany(Seq(
  Document(
    "order_id" -> 6363763262239L,
    "products" -> Seq(
      Document(
        "prod_id" -> "abc12345",
        "name" -> "Asus Laptop",
        "price" -> 431
      ),
      Document(
        "prod_id" -> "def45678",
        "name" -> "Karcher Hose Set",
        "price" -> 22
      )
    )
  ),
  Document(
    "order_id" -> 1197372932325L,
    "products" -> Seq(
      Document(
        "prod_id" -> "abc12345",
        "name" -> "Asus Laptop",
        "price" -> 429
      )
    )
  ),
  Document(
    "order_id" -> 9812343774839L,
    "products" -> Seq(
      Document(
        "prod_id" -> "pqr88223",
        "name" -> "Morphy Richards Food Mixer",
        "price" -> 431
      ),
      Document(
        "prod_id" -> "def45678",
        "name" -> "Karcher Hose Set",
        "price" -> 21
      )
    )
  ),
  Document(
    "order_id" -> 4433997244387L,
    "products" -> Seq(
      Document(
        "prod_id" -> "def45678",
        "name" -> "Karcher Hose Set",
        "price" -> 23
      ),
      Document(
        "prod_id" -> "jkl77336",
        "name" -> "Picky Pencil Sharpener",
        "price" -> 1
      ),
      Document(
        "prod_id" -> "xyz11228",
        "name" -> "Russell Hobbs Chrome Kettle",
        "price" -> 16
      )
    )
  )
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```scala
Aggregates.unwind("$products"),
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```scala
Aggregates.filter(Filters.gt("products.price", 15)),
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```scala
Aggregates.group(
  "$products.prod_id",
  Accumulators.first("product", "$products.name"),
  Accumulators.sum("total_value", "$products.price"),
  Accumulators.sum("quantity", 1)
),
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```scala
Aggregates.set(Field("product_id", "$_id")),
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```scala
Aggregates.unset("_id")
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product": "Morphy Richards Food Mixer", "total_value": 431, "quantity": 1, "product_id": "pqr88223"}
{"product": "Karcher Hose Set", "total_value": 66, "quantity": 3, "product_id": "def45678"}
{"product": "Russell Hobbs Chrome Kettle", "total_value": 16, "quantity": 1, "product_id": "xyz11228"}
{"product": "Asus Laptop", "total_value": 860, "quantity": 2, "product_id": "abc12345"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create C# classes to model the data in the `orders`
collection:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public long OrderId { get; set; }
  public List<Product> Products { get; set; }
}

public class OrderUnwound
{
  public long OrderId { get; set; }
  public Product Products { get; set; }
}

public class Product
{
  public string ProductId { get; set; }
  public string Name { get; set; }
  public int Price { get; set; }
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
            OrderId = 6363763262239L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "abc12345",
                    Name = "Asus Laptop",
                    Price = 431
                },
                new Product
                {
                    ProductId = "def45678",
                    Name = "Karcher Hose Set",
                    Price = 22
                }
            }
        },
        new Order
        {
            OrderId = 1197372932325L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "abc12345",
                    Name = "Asus Laptop",
                    Price = 429
                }
            }
        },
        new Order
        {
            OrderId = 9812343774839L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "pqr88223",
                    Name = "Morphy Richards Food Mixer",
                    Price = 431
                },
                new Product
                {
                    ProductId = "def45678",
                    Name = "Karcher Hose Set",
                    Price = 21
                }
            }
        },
        new Order
        {
            OrderId = 4433997244387L,
            Products = new List<Product>
            {
                new Product
                {
                    ProductId = "def45678",
                    Name = "Karcher Hose Set",
                    Price = 23
                },
                new Product
                {
                    ProductId = "jkl77336",
                    Name = "Picky Pencil Sharpener",
                    Price = 1
                },
                new Product
                {
                    ProductId = "xyz11228",
                    Name = "Russell Hobbs Chrome Kettle",
                    Price = 16
                }
            }
        }
    });
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, start the aggregation on the `orders` collection and
chain an `$unwind` stage to separate the
entries in the `Products` array into individual documents:

```csharp
var results = orders.Aggregate()
    .Unwind<Order, OrderUnwound>(o => o.Products)
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `Products.Price` value greater than `15`:

```csharp
.Match(o => o.Products.Price > 15)
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `ProductId` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `ProductId`: the product ID (the grouping key)
- `Product`: the product name
- `TotalValue`: the total value of all the sales of the product
- `Quantity`: the number of orders for the product

```csharp
.Group(
    id: o => o.Products.ProductId,
    group: g => new
    {
      ProductId = g.Key,
      Product = g.First().Products.Name,
      TotalValue = g.Sum(o => o.Products.Price),
      Quantity = g.Count(),
    }
);
```

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ ProductId = pqr88223, Product = Morphy Richards Food Mixer, TotalValue = 431, Quantity = 1 }
{ ProductId = xyz11228, Product = Russell Hobbs Chrome Kettle, TotalValue = 16, Quantity = 1 }
{ ProductId = abc12345, Product = Asus Laptop, TotalValue = 860, Quantity = 2 }
{ ProductId = def45678, Product = Karcher Hose Set, TotalValue = 66, Quantity = 3 }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

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
    size_t num_docs = 4;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "order_id", BCON_INT64(6363763262239),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("abc12345"),
        "name", BCON_UTF8("Asus Laptop"),
        "price", BCON_INT32(431),
        "}",
        "{",
        "prod_id", BCON_UTF8("def45678"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "price", BCON_INT32(22),
        "}",
        "]");

    docs[1] = BCON_NEW(
        "order_id", BCON_INT64(1197372932325),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("abc12345"),
        "name", BCON_UTF8("Asus Laptop"),
        "price", BCON_INT32(429),
        "}",
        "]");

    docs[2] = BCON_NEW(
        "order_id", BCON_INT64(9812343774839),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("pqr88223"),
        "name", BCON_UTF8("Morphy Richards Food Mixer"),
        "price", BCON_INT32(431),
        "}",
        "{",
        "prod_id", BCON_UTF8("def45678"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "price", BCON_INT32(21),
        "}",
        "]");

    docs[3] = BCON_NEW(
        "order_id", BCON_INT64(4433997244387),
        "products", "[",
        "{",
        "prod_id", BCON_UTF8("def45678"),
        "name", BCON_UTF8("Karcher Hose Set"),
        "price", BCON_INT32(23),
        "}",
        "{",
        "prod_id", BCON_UTF8("jkl77336"),
        "name", BCON_UTF8("Picky Pencil Sharpener"),
        "price", BCON_INT32(1),
        "}",
        "{",
        "prod_id", BCON_UTF8("xyz11228"),
        "name", BCON_UTF8("Russell Hobbs Chrome Kettle"),
        "price", BCON_INT32(16),
        "}",
        "]");

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

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```c
"{", "$unwind", "{", "path", BCON_UTF8("$products"), "}", "}",
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```c
"{", "$match", "{", "products.price", "{", "$gt", BCON_INT32(15), "}", "}", "}",
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```c
"{", "$group", "{",
"_id", BCON_UTF8("$products.prod_id"),
"product", "{", "$first", BCON_UTF8("$products.name"), "}",
"total_value", "{", "$sum", BCON_UTF8("$products.price"), "}",
"quantity", "{", "$sum", BCON_INT32(1), "}",
"}", "}",
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```c
"{", "$set", "{", "product_id", BCON_UTF8("$_id"), "}", "}",
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), "]", "}",
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "product" : "Asus Laptop", "total_value" : { "$numberInt" : "860" }, "quantity" : { "$numberInt" : "2" }, "product_id" : "abc12345" }
{ "product" : "Karcher Hose Set", "total_value" : { "$numberInt" : "66" }, "quantity" : { "$numberInt" : "3" }, "product_id" : "def45678" }
{ "product" : "Morphy Richards Food Mixer", "total_value" : { "$numberInt" : "431" }, "quantity" : { "$numberInt" : "1" }, "product_id" : "pqr88223" }
{ "product" : "Russell Hobbs Chrome Kettle", "total_value" : { "$numberInt" : "16" }, "quantity" : { "$numberInt" : "1" }, "product_id" : "xyz11228" }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```cpp
auto orders = db["orders"];

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16
            }
        ]
    })")
};
orders.insert_many(order_docs); // Might throw an exception
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```cpp
pipeline.unwind("$products");
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "products.price": { "$gt": 15 }
})"));
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```cpp
pipeline.group(bsoncxx::from_json(R"({
    "_id": "$products.prod_id",
    "product": { "$first": "$products.name" },
    "total_value": { "$sum": "$products.price" },
    "quantity": { "$sum": 1 }
})"));
```

**Step 4: Add an addFields stage to display the product ID.**

Add an `$addFields` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_id": "$_id"
})"));
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id"]
})"));
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "product" : "Karcher Hose Set", "total_value" : 66, "quantity" : 3, "product_id" : "def45678" }
{ "product" : "Asus Laptop", "total_value" : 860, "quantity" : 2, "product_id" : "abc12345" }
{ "product" : "Morphy Richards Food Mixer", "total_value" : 431, "quantity" : 1, "product_id" : "pqr88223" }
{ "product" : "Russell Hobbs Chrome Kettle", "total_value" : 16, "quantity" : 1, "product_id" : "xyz11228" }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```javascript
const orders = aggDB.collection("orders");
await orders.deleteMany({});

await orders.insertMany([
  {
    order_id: 6363763262239,
    products: [
      {
        prod_id: "abc12345",
        name: "Asus Laptop",
        price: 431,
      },
      {
        prod_id: "def45678",
        name: "Karcher Hose Set",
        price: 22,
      },
    ],
  },
  {
    order_id: 1197372932325,
    products: [
      {
        prod_id: "abc12345",
        name: "Asus Laptop",
        price: 429,
      },
    ],
  },
  {
    order_id: 9812343774839,
    products: [
      {
        prod_id: "pqr88223",
        name: "Morphy Richards Food Mixer",
        price: 431,
      },
      {
        prod_id: "def45678",
        name: "Karcher Hose Set",
        price: 21,
      },
    ],
  },
  {
    order_id: 4433997244387,
    products: [
      {
        prod_id: "def45678",
        name: "Karcher Hose Set",
        price: 23,
      },
      {
        prod_id: "jkl77336",
        name: "Picky Pencil Sharpener",
        price: 1,
      },
      {
        prod_id: "xyz11228",
        name: "Russell Hobbs Chrome Kettle",
        price: 16,
      },
    ],
  },
]);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```javascript
pipeline.push({
  $unwind: {
    path: "$products",
  },
});
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```javascript
pipeline.push({
  $match: {
    "products.price": {
      $gt: 15,
    },
  },
});
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```javascript
pipeline.push({
  $group: {
    _id: "$products.prod_id",
    product: { $first: "$products.name" },
    total_value: { $sum: "$products.price" },
    quantity: { $sum: 1 },
  },
});
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```javascript
pipeline.push({
  $set: {
    product_id: "$_id",
  },
});
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```javascript
pipeline.push({ $unset: ["_id"] });
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  product: 'Asus Laptop',
  total_value: 860,
  quantity: 2,
  product_id: 'abc12345'
}
{
  product: 'Morphy Richards Food Mixer',
  total_value: 431,
  quantity: 1,
  product_id: 'pqr88223'
}
{
  product: 'Russell Hobbs Chrome Kettle',
  total_value: 16,
  quantity: 1,
  product_id: 'xyz11228'
}
{
  product: 'Karcher Hose Set',
  total_value: 66,
  quantity: 3,
  product_id: 'def45678'
}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$orders->deleteMany([]);

$orders->insertMany(
    [
        [
            'order_id' => 6363763262239,
            'products' => [
                [
                    'prod_id' => 'abc12345',
                    'name' => 'Asus Laptop',
                    'price' => 431,
                ],
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 22,
                ],
            ],
        ],
        [
            'order_id' => 1197372932325,
            'products' => [
                [
                    'prod_id' => 'abc12345',
                    'name' => 'Asus Laptop',
                    'price' => 429,
                ],
            ],
        ],
        [
            'order_id' => 9812343774839,
            'products' => [
                [
                    'prod_id' => 'pqr88223',
                    'name' => 'Morphy Richards Food Mixer',
                    'price' => 431,
                ],
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 21,
                ],
            ],
        ],
        [
            'order_id' => 4433997244387,
            'products' => [
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 23,
                ],
                [
                    'prod_id' => 'jkl77336',
                    'name' => 'Picky Pencil Sharpener',
                    'price' => 1,
                ],
                [
                    'prod_id' => 'xyz11228',
                    'name' => 'Russell Hobbs Chrome Kettle',
                    'price' => 16,
                ],
            ],
        ]
    ]
);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```php
Stage::unwind(
    path: Expression::arrayFieldPath('products')
),
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```php
Stage::match(
    ['products.price' => Query::gt(15)]
),
```

**Step 3: Add a group stage to group by product type.**

Outside of your `Pipeline` instance, create a `$group` stage in a factory
function to collect order documents by the value of the
`prod_id` field. In this stage, add aggregation operations that
create the following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```php
function groupByProductStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('products.prod_id'),
        product: Accumulator::first(
            Expression::stringFieldPath('products.name')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('products.price'),
        ),
        quantity: Accumulator::sum(1)
    );
}
```

Then, in your `Pipeline` instance, call the
`groupByProductStage()` function:

```php
function groupByProductStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('products.prod_id'),
        product: Accumulator::first(
            Expression::stringFieldPath('products.name')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('products.price'),
        ),
        quantity: Accumulator::sum(1)
    );
}
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```php
Stage::set(product_id: Expression::stringFieldPath('_id')),
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```php
Stage::unset('_id')
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{
    "product": "Russell Hobbs Chrome Kettle",
    "total_value": 16,
    "quantity": 1,
    "product_id": "xyz11228"
}
{
    "product": "Asus Laptop",
    "total_value": 860,
    "quantity": 2,
    "product_id": "abc12345"
}
{
    "product": "Karcher Hose Set",
    "total_value": 66,
    "quantity": 3,
    "product_id": "def45678"
}
{
    "product": "Morphy Richards Food Mixer",
    "total_value": 431,
    "quantity": 1,
    "product_id": "pqr88223"
}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```ruby
orders = agg_db[:orders]
orders.delete_many({})

orders.insert_many(
  [
    {
      order_id: 6363763262239,
      products: [
        {
          prod_id: "abc12345",
          name: "Asus Laptop",
          price: 431,
        },
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 22,
        },
      ],
    },
    {
      order_id: 1197372932325,
      products: [
        {
          prod_id: "abc12345",
          name: "Asus Laptop",
          price: 429,
        },
      ],
    },
    {
      order_id: 9812343774839,
      products: [
        {
          prod_id: "pqr88223",
          name: "Morphy Richards Food Mixer",
          price: 431,
        },
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 21,
        },
      ],
    },
    {
      order_id: 4433997244387,
      products: [
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 23,
        },
        {
          prod_id: "jkl77336",
          name: "Picky Pencil Sharpener",
          price: 1,
        },
        {
          prod_id: "xyz11228",
          name: "Russell Hobbs Chrome Kettle",
          price: 16,
        },
      ],
    },
  ]
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```ruby
{
  "$unwind": {
    path: "$products",
  },
},
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```ruby
{
  "$match": {
    "products.price": {
      "$gt": 15,
    },
  },
},
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```ruby
{
  "$group": {
    _id: "$products.prod_id",
    product: { "$first": "$products.name" },
    total_value: { "$sum": "$products.price" },
    quantity: { "$sum": 1 },
  },
},
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```ruby
{
  "$set": {
    product_id: "$_id",
  },
},
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```ruby
{ "$unset": ["_id"] },
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product"=>"Asus Laptop", "total_value"=>860, "quantity"=>2, "product_id"=>"abc12345"}
{"product"=>"Russell Hobbs Chrome Kettle", "total_value"=>16, "quantity"=>1, "product_id"=>"xyz11228"}
{"product"=>"Karcher Hose Set", "total_value"=>66, "quantity"=>3, "product_id"=>"def45678"}
{"product"=>"Morphy Richards Food Mixer", "total_value"=>431, "quantity"=>1, "product_id"=>"pqr88223"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Go structs to model the data in the `orders`
collection:

```go
type Order struct {
	OrderID  int       `bson:"order_id"`
	Products []Product `bson:"products"`
}

type Product struct {
	ProductID string `bson:"prod_id"`
	Name      string `bson:"name"`
	Price     int    `bson:"price"`
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```go
orders := aggDB.Collection("orders")
orders.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		OrderID: 6363763262239,
		Products: []Product{
			{ProductID: "abc12345", Name: "Asus Laptop", Price: 431},
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 22},
		},
	},
	Order{
		OrderID: 1197372932325,
		Products: []Product{
			{ProductID: "abc12345", Name: "Asus Laptop", Price: 429},
		},
	},
	Order{
		OrderID: 9812343774839,
		Products: []Product{
			{ProductID: "pqr88223", Name: "Morphy Richards Food Mixer", Price: 431},
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 21},
		},
	},
	Order{
		OrderID: 4433997244387,
		Products: []Product{
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 23},
			{ProductID: "jkl77336", Name: "Picky Pencil Sharpene", Price: 1},
			{ProductID: "xyz11228", Name: "Russell Hobbs Chrome Kettle", Price: 16},
		},
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```go
unwindStage := bson.D{{Key: "$unwind", Value: bson.D{
	{Key: "path", Value: "$products"},
}}}
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "products.price", Value: bson.D{{Key: "$gt", Value: 15}}},
}}}
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```go
groupStage := bson.D{{Key: "$group", Value: bson.D{
	{Key: "_id", Value: "$products.prod_id"},
	{Key: "product", Value: bson.D{{Key: "$first", Value: "$products.name"}}},
	{Key: "total_value", Value: bson.D{{Key: "$sum", Value: "$products.price"}}},
	{Key: "quantity", Value: bson.D{{Key: "$sum", Value: 1}}},
}}}
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```go
setStage := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_id", Value: "$_id"},
}}}
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id"}}}
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{unwindStage, matchStage, groupStage, setStage, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product":"Morphy Richards Food Mixer","total_value":431,"quantity":1,"product_id":"pqr88223"}
{"product":"Russell Hobbs Chrome Kettle","total_value":16,"quantity":1,"product_id":"xyz11228"}
{"product":"Karcher Hose Set","total_value":66,"quantity":3,"product_id":"def45678"}
{"product":"Asus Laptop","total_value":860,"quantity":2,"product_id":"abc12345"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.

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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Rust structs to model the data in the `orders`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Product {
    prod_id: String,
    name: String,
    price: i32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Order {
    order_id: i64,
    products: Vec<Product>,
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```rust
let orders_coll: Collection<Order> = agg_db.collection("orders");
orders.delete_many(doc! {}).await?;

let orders = vec![
    Order {
        order_id: 6363763262239,
        products: vec![
            Product {
                prod_id: "abc12345".to_string(),
                name: "Asus Laptop".to_string(),
                price: 431,
            },
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 22,
            },
        ],
    },
    Order {
        order_id: 1197372932325,
        products: vec![Product {
            prod_id: "abc12345".to_string(),
            name: "Asus Laptop".to_string(),
            price: 429,
        }],
    },
    Order {
        order_id: 9812343774839,
        products: vec![
            Product {
                prod_id: "pqr88223".to_string(),
                name: "Morphy Richards Food Mixer".to_string(),
                price: 431,
            },
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 21,
            },
        ],
    },
    Order {
        order_id: 4433997244387,
        products: vec![
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 23,
            },
            Product {
                prod_id: "jkl77336".to_string(),
                name: "Picky Pencil Sharpene".to_string(),
                price: 1,
            },
            Product {
                prod_id: "xyz11228".to_string(),
                name: "Russell Hobbs Chrome Kettle".to_string(),
                price: 16,
            },
        ],
    },
];

orders_coll.insert_many(orders).await?;
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```rust
pipeline.push(doc! {
    "$unwind": {
        "path": "$products"
    }
});
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```rust
pipeline.push(doc! {
    "$match": {
        "products.price": { "$gt": 15 }
    }
});
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```rust
pipeline.push(doc! {
    "$group": {
        "_id": "$products.prod_id",
        "product": { "$first": "$products.name" },
        "total_value": { "$sum": "$products.price" },
        "quantity": { "$sum": 1 }
    }
});
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`prod_id` field from the values in the `_id` field
that were set during the `$group` stage:

```rust
pipeline.push(doc! {
    "$set": {
        "prod_id": "$_id"
    }
});
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```rust
pipeline.push(doc! {
    "$unset": ["_id"]
});
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```rust
let mut cursor = orders_coll.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document({"product": String("Russell Hobbs Chrome Kettle"), "total_value": Int32(16), "quantity": Int32(1),
"prod_id": String("xyz11228")})

Document({"product": String("Morphy Richards Food Mixer"), "total_value": Int32(431), "quantity": Int32(1),
"prod_id": String("pqr88223")})

Document({"product": String("Karcher Hose Set"), "total_value": Int32(66), "quantity": Int32(3),
"prod_id": String("def45678")})

Document({"product": String("Asus Laptop"), "total_value": Int32(860), "quantity": Int32(2),
"prod_id": String("abc12345")})
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.
