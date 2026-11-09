<!-- Converted from tutorial/aggregation-examples/multi-field-join.txt (reStructuredText). Includes are inlined. -->

# Perform Multi-Field Joins

This tutorial illustrates how to construct an aggregation pipeline,
perform the aggregation on a collection, and display the results using
the language of your choice. 

## About This Task

This tutorial demonstrates how to combine data from a collection that
describes product information with another collection that describes
customer orders. The results show a list of products ordered in 2020
and details about each order.

This aggregation performs a multi-field join by using `$lookup`. A
multi-field join occurs when there are multiple corresponding fields in
the documents of two collections. The aggregation matches these
documents on the corresponding fields and combines information from both
into one document.

## Before You Begin

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples or select
MongoDB Shell.

----------

**shell:**

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `orders` and `products` collections, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-05-30T08:35:52Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 431.43,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2019-05-28T19:13:32Z"),
      product_name: "The Day Of The Triffids",
      product_variation: "2nd Edition",
      value: 5.01,
   },
   {
      customer_id: "oranieri@warmmail.com",
      orderdate: new Date("2020-01-01T08:25:37Z"),
      product_name: "Morphy Richards Food Mixer",
      product_variation: "Deluxe",
      value: 63.13,
   },
   {
      customer_id: "jjones@tepidmail.com",
      orderdate: new Date("2020-12-26T08:55:46Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 429.65,
   }
] )
```

```javascript
db.products.deleteMany({})

db.products.insertMany( [
   {
      name: "Asus Laptop",
      variation: "Ultra HD",
      category: "ELECTRONICS",
      description: "Great for watching movies"
   },
   {
      name: "Asus Laptop",
      variation: "Standard Display",
      category: "ELECTRONICS",
      description: "Good value laptop for students"
   },
   {
      name: "The Day Of The Triffids",
      variation: "1st Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel"
   },
   {
      name: "The Day Of The Triffids",
      variation: "2nd Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel"
   },
   {
      name: "Morphy Richards Food Mixer",
      variation: "Deluxe",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great"
   }
] )
```

**Step 1: Create an embedded pipeline to use in the lookup stage.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The `$lookup` stage contains an embedded
pipeline to configure the join.

```javascript
embedded_pl = [
   // Stage 1: Match the values of two fields on each side of the join
   // The $eq filter uses aliases for the name and variation fields set
   { $match: {
      $expr: {
         $and: [
            { $eq: ["$product_name", "$$prdname"] },
            { $eq: ["$product_variation", "$$prdvartn"] }
         ]
      }
   } },

   // Stage 2: Match orders placed in 2020
   { $match: {
      orderdate: {
         $gte: new Date("2020-01-01T00:00:00Z"),
         $lt: new Date("2021-01-01T00:00:00Z")
      }
   } },

   // Stage 3: Remove unneeded fields from the orders collection side of the join
   { $unset: ["_id", "product_name", "product_variation"] }
]
```

**Step 2: Run the aggregation pipeline.**

```javascript
db.products.aggregate( [
   // Use the embedded pipeline in a lookup stage
   { $lookup: {
         from: "orders",
         let: {
            prdname: "$name",
            prdvartn: "$variation"
         },
         pipeline: embedded_pl,
         as: "orders"
   } },

   // Match products ordered in 2020
   { $match: { orders: { $ne: [] } } },

   // Remove unneeded fields
   { $unset: ["_id", "description"] }
] )
```

**Step 3: Interpret the aggregation results.**

The aggregated results contain two documents. The documents
represent products ordered 2020. Each document contains an
`orders` array field that lists details about each order for
that product.

```javascript
{
   name: 'Asus Laptop',
   variation: 'Standard Display',
   category: 'ELECTRONICS',
   orders: [
      {
         customer_id: 'elise_smith@myemail.com',
         orderdate: ISODate('2020-05-30T08:35:52.000Z'),
         value: 431.43
      },
      {
         customer_id: 'jjones@tepidmail.com',
         orderdate: ISODate('2020-12-26T08:55:46.000Z'),
         value: 429.65
      }
   ]
}
{
   name: 'Morphy Richards Food Mixer',
   variation: 'Deluxe',
   category: 'KITCHENWARE',
   orders: [
      {
         customer_id: 'oranieri@warmmail.com',
         orderdate: ISODate('2020-01-01T08:25:37.000Z'),
         value: 63.13
      }
   ]
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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```python
products_coll = agg_db["products"]
orders_coll = agg_db["orders"]

products_coll.delete_many({})

products_data = [
    {
        "name": "Asus Laptop",
        "variation": "Ultra HD",
        "category": "ELECTRONICS",
        "description": "Great for watching movies",
    },
    {
        "name": "Asus Laptop",
        "variation": "Standard Display",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students",
    },
    {
        "name": "The Day Of The Triffids",
        "variation": "1st Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel",
    },
    {
        "name": "The Day Of The Triffids",
        "variation": "2nd Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel",
    },
    {
        "name": "Morphy Richards Food Mixer",
        "variation": "Deluxe",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great",
    },
]

products_coll.insert_many(products_data)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```python
embedded_pl = [
    {
        "$match": {
            "$expr": {
                "$and": [
                    {"$eq": ["$product_name", "$$prdname"]},
                    {"$eq": ["$product_variation", "$$prdvartn"]},
                ]
            }
        }
    }
]
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```python
embedded_pl.append(
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```python
embedded_pl.append({"$unset": ["_id", "product_name", "product_variation"]})
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```python
pipeline.append(
    {
        "$lookup": {
            "from": "orders",
            "let": {"prdname": "$name", "prdvartn": "$variation"},
            "pipeline": embedded_pl,
            "as": "orders",
        }
    }
)
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```python
pipeline.append({"$match": {"orders": {"$ne": []}}})
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```python
pipeline.append({"$unset": ["_id", "description"]})
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```python
aggregation_result = products_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{'name': 'Asus Laptop', 'variation': 'Standard Display', 'category': 'ELECTRONICS', 'orders': [{'customer_id': 'elise_smith@myemail.com', 'orderdate': datetime.datetime(2020, 5, 30, 8, 35, 52), 'value': 431.43}, {'customer_id': 'jjones@tepidmail.com', 'orderdate': datetime.datetime(2020, 12, 26, 8, 55, 46), 'value': 429.65}]}
{'name': 'Morphy Richards Food Mixer', 'variation': 'Deluxe', 'category': 'KITCHENWARE', 'orders': [{'customer_id': 'oranieri@warmmail.com', 'orderdate': datetime.datetime(2020, 1, 1, 8, 25, 37), 'value': 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```java
MongoCollection<Document> products = aggDB.getCollection("products");
MongoCollection<Document> orders = aggDB.getCollection("orders");

products.deleteMany(Filters.empty());
orders.deleteMany(Filters.empty());

products.insertMany(
        Arrays.asList(
                new Document("name", "Asus Laptop")
                        .append("variation", "Ultra HD")
                        .append("category", "ELECTRONICS")
                        .append("description", "Great for watching movies"),

                new Document("name", "Asus Laptop")
                        .append("variation", "Standard Display")
                        .append("category", "ELECTRONICS")
                        .append("description", "Good value laptop for students"),

                new Document("name", "The Day Of The Triffids")
                        .append("variation", "1st Edition")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),

                new Document("name", "The Day Of The Triffids")
                        .append("variation", "2nd Edition")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),

                new Document("name", "Morphy Richards Food Mixer")
                        .append("variation", "Deluxe")
                        .append("category", "KITCHENWARE")
                        .append("description", "Luxury mixer turning good cakes into great")
        )
);

orders.insertMany(
        Arrays.asList(
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-05-30T08:35:52"))
                        .append("product_name", "Asus Laptop")
                        .append("product_variation", "Standard Display")
                        .append("value", 431.43),

                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2019-05-28T19:13:32"))
                        .append("product_name", "The Day Of The Triffids")
                        .append("product_variation", "2nd Edition")
                        .append("value", 5.01),

                new Document("customer_id", "oranieri@warmmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-01-01T08:25:37"))
                        .append("product_name", "Morphy Richards Food Mixer")
                        .append("product_variation", "Deluxe")
                        .append("value", 63.13),

                new Document("customer_id", "jjones@tepidmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-12-26T08:55:46"))
                        .append("product_name", "Asus Laptop")
                        .append("product_variation", "Standard Display")
                        .append("value", 429.65)
        )
);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```java
List<Bson> embeddedPipeline = new ArrayList<>();

embeddedPipeline.add(Aggregates.match(
        Filters.expr(
                Filters.and(
                        new Document("$eq", Arrays.asList("$product_name", "$$prdname")),
                        new Document("$eq", Arrays.asList("$product_variation", "$$prdvartn"))
                )
        )
));
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```java
embeddedPipeline.add(Aggregates.match(Filters.and(
        Filters.gte("orderdate", LocalDateTime.parse("2020-01-01T00:00:00")),
        Filters.lt("orderdate", LocalDateTime.parse("2021-01-01T00:00:00"))
)));
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```java
embeddedPipeline.add(Aggregates.unset("_id", "product_name", "product_variation"));
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```java
pipeline.add(Aggregates.lookup(
        "orders",
        Arrays.asList(
                new Variable<>("prdname", "$name"),
                new Variable<>("prdvartn", "$variation")
        ),
        embeddedPipeline,
        "orders"
));
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```java
pipeline.add(Aggregates.match(
        Filters.ne("orders", new ArrayList<>())
));
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```java
pipeline.add(Aggregates.unset("_id", "description"));
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```java
AggregateIterable<Document> aggregationResult = products.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name": "Asus Laptop", "variation": "Standard Display", "category": "ELECTRONICS", "orders": [{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T08:35:52Z"}, "value": 431.43}, {"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T08:55:46Z"}, "value": 429.65}]}
{"name": "Morphy Richards Food Mixer", "variation": "Deluxe", "category": "KITCHENWARE", "orders": [{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T08:25:37Z"}, "value": 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**kotlin-coroutine:**

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

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

First, create Kotlin data classes to model the data in the `products`
and `orders` collections:

```kotlin
@Serializable
data class Product(
    val name: String,
    val variation: String,
    val category: String,
    val description: String
)

@Serializable
data class Order(
    val customerID: String,
    @Contextual val orderDate: LocalDateTime,
    val productName: String,
    val productVariation: String,
    val value: Double
)
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```kotlin
val products = aggDB.getCollection<Product>("products")
val orders = aggDB.getCollection<Order>("orders")

products.deleteMany(Filters.empty());
orders.deleteMany(Filters.empty());

products.insertMany(
    listOf(
        Product("Asus Laptop", "Ultra HD", "ELECTRONICS", "Great for watching movies"),
        Product("Asus Laptop", "Standard Display", "ELECTRONICS", "Good value laptop for students"),
        Product("The Day Of The Triffids", "1st Edition", "BOOKS", "Classic post-apocalyptic novel"),
        Product("The Day Of The Triffids", "2nd Edition", "BOOKS", "Classic post-apocalyptic novel"),
        Product(
            "Morphy Richards Food Mixer",
            "Deluxe",
            "KITCHENWARE",
            "Luxury mixer turning good cakes into great"
        )
    )
)

orders.insertMany(
    listOf(
        Order(
            "elise_smith@myemail.com",
            LocalDateTime.parse("2020-05-30T08:35:52"),
            "Asus Laptop",
            "Standard Display",
            431.43
        ),
        Order(
            "tj@wheresmyemail.com",
            LocalDateTime.parse("2019-05-28T19:13:32"),
            "The Day Of The Triffids",
            "2nd Edition",
            5.01
        ),
        Order(
            "oranieri@warmmail.com",
            LocalDateTime.parse("2020-01-01T08:25:37"),
            "Morphy Richards Food Mixer",
            "Deluxe",
            63.13
        ),
        Order(
            "jjones@tepidmail.com",
            LocalDateTime.parse("2020-12-26T08:55:46"),
            "Asus Laptop",
            "Standard Display",
            429.65
        )
    )
)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```kotlin
val embeddedPipeline = mutableListOf<Bson>()

embeddedPipeline.add(
    Aggregates.match(
        Filters.expr(
            Document(
                "\$and", listOf(
                    Document("\$eq", listOf("\$${Order::productName.name}", "$\$prdname")),
                    Document("\$eq", listOf("\$${Order::productVariation.name}", "$\$prdvartn"))
                )
            )
        )
    )
)
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```kotlin
embeddedPipeline.add(
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```kotlin
embeddedPipeline.add(Aggregates.unset("_id", Order::productName.name, Order::productVariation.name))
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```kotlin
pipeline.add(
    Aggregates.lookup(
        "orders",
        listOf(
            Variable("prdname", "\$${Product::name.name}"),
            Variable("prdvartn", "\$${Product::variation.name}")
        ),
        embeddedPipeline,
        "orders"
    )
)
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.ne("orders", mutableListOf<Document>())
    )
)
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```kotlin
pipeline.add(Aggregates.unset("_id", "description"))
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```kotlin
val aggregationResult = products.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
Document{{name=Asus Laptop, variation=Standard Display, category=ELECTRONICS, orders=[Document{{customerID=elise_smith@myemail.com, orderDate=Sat May 30 04:35:52 EDT 2020, value=431.43}}, Document{{customerID=jjones@tepidmail.com, orderDate=Sat Dec 26 03:55:46 EST 2020, value=429.65}}]}}
Document{{name=Morphy Richards Food Mixer, variation=Deluxe, category=KITCHENWARE, orders=[Document{{customerID=oranieri@warmmail.com, orderDate=Wed Jan 01 03:25:37 EST 2020, value=63.13}}]}}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```scala
val products = aggDB.getCollection("products")
val orders = aggDB.getCollection("orders")

products.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

products.insertMany(
  Seq(
    Document(
      "name" -> "Asus Laptop",
      "variation" -> "Ultra HD",
      "category" -> "ELECTRONICS",
      "description" -> "Great for watching movies"
    ),
    Document(
      "name" -> "Asus Laptop",
      "variation" -> "Standard Display",
      "category" -> "ELECTRONICS",
      "description" -> "Good value laptop for students"
    ),
    Document(
      "name" -> "The Day Of The Triffids",
      "variation" -> "1st Edition",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "name" -> "The Day Of The Triffids",
      "variation" -> "2nd Edition",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "name" -> "Morphy Richards Food Mixer",
      "variation" -> "Deluxe",
      "category" -> "KITCHENWARE",
      "description" -> "Luxury mixer turning good cakes into great"
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

orders.insertMany(
  Seq(
    Document(
      "customer_id" -> "elise_smith@myemail.com",
      "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
      "product_name" -> "Asus Laptop",
      "product_variation" -> "Standard Display",
      "value" -> 431.43
    ),
    Document(
      "customer_id" -> "tj@wheresmyemail.com",
      "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
      "product_name" -> "The Day Of The Triffids",
      "product_variation" -> "2nd Edition",
      "value" -> 5.01
    ),
    Document(
      "customer_id" -> "oranieri@warmmail.com",
      "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
      "product_name" -> "Morphy Richards Food Mixer",
      "product_variation" -> "Deluxe",
      "value" -> 63.13
    ),
    Document(
      "customer_id" -> "jjones@tepidmail.com",
      "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
      "product_name" -> "Asus Laptop",
      "product_variation" -> "Standard Display",
      "value" -> 429.65
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```scala
Aggregates.filter(
  Filters.expr(
    Filters.and(
      Document("$eq" -> Seq("$product_name", "$$prdname")),
      Document("$eq" -> Seq("$product_variation", "$$prdvartn"))
    )
  )
),
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```scala
Aggregates.filter(
  Filters.and(
    Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
    Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
  )
),
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```scala
Aggregates.unset("_id", "product_name", "product_variation"),
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```scala
Aggregates.lookup(
  "orders",
  Seq(
    Variable("prdname", "$name"),
    Variable("prdvartn", "$variation"),
  ),
  embeddedPipeline,
  "orders"
),
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```scala
Aggregates.filter(Filters.ne("orders", Seq())),
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```scala
Aggregates.unset("_id", "description")
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```scala
products.aggregate(pipeline)
  .subscribe(
    (doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"),
  )
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name": "Asus Laptop", "variation": "Standard Display", "category": "ELECTRONICS", "orders": [{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 431.43}, {"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 429.65}]}
{"name": "Morphy Richards Food Mixer", "variation": "Deluxe", "category": "KITCHENWARE", "orders": [{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `Name` and
`Variation` fields in documents in the `products` collection, corresponding
to the `ProductName` and `ProductVariation` fields in documents in the
`orders` collection.

First, create C# classes to model the data in the `products` and `orders`
collections:

```csharp
public class Product
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string Name { get; set; }
  public string Variation { get; set; }
  public string Category { get; set; }
  public string Description { get; set; }
}

public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public string ProductName { get; set; }
  public string ProductVariation { get; set; }
  public double Value { get; set; }
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```csharp
var products = aggDB.GetCollection<Product>("products");
var orders = aggDB.GetCollection<Order>("orders");
products.DeleteMany(Builders<Product>.Filter.Empty);
orders.DeleteMany(Builders<Order>.Filter.Empty);

products.InsertMany(new List<Product>
{
    new Product
    {
        Name = "Asus Laptop",
        Variation = "Ultra HD",
        Category = "ELECTRONICS",
        Description = "Great for watching movies"
    },
    new Product
    {
        Name = "Asus Laptop",
        Variation = "Standard Display",
        Category = "ELECTRONICS",
        Description = "Good value laptop for students"
    },
    new Product
    {
        Name = "The Day Of The Triffids",
        Variation = "1st Edition",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Name = "The Day Of The Triffids",
        Variation = "2nd Edition",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Name = "Morphy Richards Food Mixer",
        Variation = "Deluxe",
        Category = "KITCHENWARE",
        Description = "Luxury mixer turning good cakes into great"
    }
});

orders.InsertMany(new List<Order>
{
    new Order
    {
        CustomerId = "elise_smith@myemail.com",
        OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
        ProductName = "Asus Laptop",
        ProductVariation = "Standard Display",
        Value = 431.43
    },
    new Order
    {
        CustomerId = "tj@wheresmyemail.com",
        OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
        ProductName = "The Day Of The Triffids",
        ProductVariation = "2nd Edition",
        Value = 5.01
    },
    new Order
    {
        CustomerId = "oranieri@warmmail.com",
        OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
        ProductName = "Morphy Richards Food Mixer",
        ProductVariation = "Deluxe",
        Value = 63.13
    },
    new Order
    {
        CustomerId = "jjones@tepidmail.com",
        OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
        ProductName = "Asus Laptop",
        ProductVariation = "Standard Display",
        Value = 429.65
    }
});
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to
join the `orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Instantiate the embedded pipeline, then chain a `$match`
stage to match the values of two fields on each side of the join.
Note that the following code uses aliases for the `Name` and
`Variation` fields set when creating the $lookup stage:

```csharp
var embeddedPipeline = new EmptyPipelineDefinition<Order>()
    .Match(new BsonDocument("$expr",
        new BsonDocument("$and", new BsonArray
        {
                new BsonDocument("$eq", new BsonArray { "$ProductName", "$$prdname" }),
                new BsonDocument("$eq", new BsonArray { "$ProductVariation", "$$prdvartn" })
        })))
```

Within the embedded pipeline, add another `$match`
stage to match orders placed in 2020:

```csharp
.Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
            o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

Within the embedded pipeline, add a `$project` stage to
remove unneeded fields from the `orders` collection side of the join:

```csharp
.Project(Builders<Order>.Projection
        .Exclude(o => o.Id)
        .Exclude(o => o.ProductName)
        .Exclude(o => o.ProductVariation));
```

After the embedded pipeline is completed, start the main
aggregation on the `products` collection and chain the
`$lookup` stage. Configure this stage to store the processed
lookup fields in an array field called `Orders`:

```csharp
var results = products.Aggregate()
    .Lookup<Order, BsonDocument, IEnumerable<BsonDocument>, BsonDocument>(
        foreignCollection: orders,
        let: new BsonDocument { { "prdname", "$Name" }, { "prdvartn", "$Variation" } },
        lookupPipeline: embeddedPipeline,
        "Orders"
    )
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `Orders` array created in the previous step:

```csharp
.Match(Builders<BsonDocument>.Filter.Ne("Orders", new BsonArray()))
```

**Step 3: Add a projection stage to remove unneeded fields.**

Finally, add a `$project` stage. The
`$project` stage removes the `_id` and `Description`
fields from the result documents:

```csharp
.Project(Builders<BsonDocument>.Projection
    .Exclude("_id")
    .Exclude("Description")
);
```

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `Orders` array field that lists details
about each order for that product:

```none
{ "Name" : "Asus Laptop", "Variation" : "Standard Display", "Category" : "ELECTRONICS", "Orders" : [{ "CustomerId" : "elise_smith@myemail.com", "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 431.43000000000001 }, { "CustomerId" : "jjones@tepidmail.com", "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 429.64999999999998 }] }
{ "Name" : "Morphy Richards Food Mixer", "Variation" : "Deluxe", "Category" : "KITCHENWARE", "Orders" : [{ "CustomerId" : "oranieri@warmmail.com", "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63.130000000000003 }] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```c
mongoc_collection_t *products = mongoc_client_get_collection(client, "agg_tutorials_db", "products");
mongoc_collection_t *orders = mongoc_client_get_collection(client, "agg_tutorials_db", "orders");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(products, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    if (!mongoc_collection_delete_many(orders, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 5;
    bson_t *product_docs[num_docs];

    product_docs[0] = BCON_NEW(
        "name", BCON_UTF8("Asus Laptop"),
        "variation", BCON_UTF8("Ultra HD"),
        "category", BCON_UTF8("ELECTRONICS"),
        "description", BCON_UTF8("Great for watching movies"));

    product_docs[1] = BCON_NEW(
        "name", BCON_UTF8("Asus Laptop"),
        "variation", BCON_UTF8("Standard Display"),
        "category", BCON_UTF8("ELECTRONICS"),
        "description", BCON_UTF8("Good value laptop for students"));

    product_docs[2] = BCON_NEW(
        "name", BCON_UTF8("The Day Of The Triffids"),
        "variation", BCON_UTF8("1st Edition"),
        "category", BCON_UTF8("BOOKS"),
        "description", BCON_UTF8("Classic post-apocalyptic novel"));

    product_docs[3] = BCON_NEW(
        "name", BCON_UTF8("The Day Of The Triffids"),
        "variation", BCON_UTF8("2nd Edition"),
        "category", BCON_UTF8("BOOKS"),
        "description", BCON_UTF8("Classic post-apocalyptic novel"));

    product_docs[4] = BCON_NEW(
        "name", BCON_UTF8("Morphy Richards Food Mixer"),
        "variation", BCON_UTF8("Deluxe"),
        "category", BCON_UTF8("KITCHENWARE"),
        "description", BCON_UTF8("Luxury mixer turning good cakes into great"));

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

{
    size_t num_docs = 4;
    bson_t *order_docs[num_docs];

    order_docs[0] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1590822952000UL), // 2020-05-30T08:35:52Z
        "product_name", BCON_UTF8("Asus Laptop"),
        "product_variation", BCON_UTF8("Standard Display"),
        "value", BCON_DOUBLE(431.43));

    order_docs[1] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1559063612000UL), // 2019-05-28T19:13:32Z
        "product_name", BCON_UTF8("The Day Of The Triffids"),
        "product_variation", BCON_UTF8("2nd Edition"),
        "value", BCON_DOUBLE(5.01));

    order_docs[2] = BCON_NEW(
        "customer_id", BCON_UTF8("oranieri@warmmail.com"),
        "orderdate", BCON_DATE_TIME(1577869537000UL), // 2020-01-01T08:25:37Z
        "product_name", BCON_UTF8("Morphy Richards Food Mixer"),
        "product_variation", BCON_UTF8("Deluxe"),
        "value", BCON_DOUBLE(63.13));

    order_docs[3] = BCON_NEW(
        "customer_id", BCON_UTF8("jjones@tepidmail.com"),
        "orderdate", BCON_DATE_TIME(1608976546000UL), // 2020-12-26T08:55:46Z
        "product_name", BCON_UTF8("Asus Laptop"),
        "product_variation", BCON_UTF8("Standard Display"),
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
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to
join the `orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Create the embedded pipeline, then add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```c
bson_t embedded_pipeline;
bson_array_builder_t *bab = bson_array_builder_new();

bson_array_builder_append_document(bab, BCON_NEW(
                                            "$match", "{",
                                            "$expr", "{", "$and",
                                            "[",
                                            "{", "$eq", "[", BCON_UTF8("$product_name"), BCON_UTF8("$$prdname"), "]", "}",
                                            "{", "$eq", "[", BCON_UTF8("$product_variation"), BCON_UTF8("$$prdvartn"), "]", "}",
                                            "]",
                                            "}",
                                            "}"));
```

Within the embedded pipeline, add another `$match` stage
to match orders placed in 2020:

```c
bson_array_builder_append_document(bab, BCON_NEW(
                                            "$match", "{", "orderdate",
                                            "{",
                                            "$gte", BCON_DATE_TIME(1577836800000UL),
                                            "$lt", BCON_DATE_TIME(1609459200000UL),
                                            "}",
                                            "}"));
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```c
bson_array_builder_append_document(bab, BCON_NEW(
                                            "$unset",
                                            "[", BCON_UTF8("_id"), BCON_UTF8("product_name"), BCON_UTF8("product_variation"),
                                            "]"));

// Builds the embedded pipeline array and cleans up resources
bson_array_builder_build(bab, &embedded_pipeline);
bson_array_builder_destroy(bab);
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```c
"{", "$lookup", "{",
"from", BCON_UTF8("orders"),
"let", "{",
"prdname", BCON_UTF8("$name"),
"prdvartn", BCON_UTF8("$variation"),
"}",
"pipeline", BCON_ARRAY(&embedded_pipeline),
"as", BCON_UTF8("orders"),
"}", "}",
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```c
"{",
"$match", "{",
"orders", "{", "$ne", "[", "]", "}",
"}", "}",
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("description"), "]", "}",
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(products, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(&embedded_pipeline);
bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(products);
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

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{ "name" : "Asus Laptop", "variation" : "Standard Display", "category" : "ELECTRONICS", "orders" : [ { "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : { "$numberLong" : "1590822952000" } }, "value" : { "$numberDouble" : "431.43000000000000682" } }, { "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" : { "$numberLong" : "1608976546000" } }, "value" : { "$numberDouble" : "429.64999999999997726" } } ] }
{ "name" : "Morphy Richards Food Mixer", "variation" : "Deluxe", "category" : "KITCHENWARE", "orders" : [ { "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : { "$numberLong" : "1577869537000" } }, "value" : { "$numberDouble" : "63.130000000000002558" } } ] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```cpp
auto products = db["products"];
auto orders = db["orders"];

std::vector<bsoncxx::document::value> product_docs = {
    bsoncxx::from_json(R"({
        "name": "Asus Laptop",
        "variation": "Ultra HD",
        "category": "ELECTRONICS",
        "description": "Great for watching movies"
    })"),
    bsoncxx::from_json(R"({
        "name": "Asus Laptop",
        "variation": "Standard Display",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students"
    })"),
    bsoncxx::from_json(R"({
        "name": "The Day Of The Triffids",
        "variation": "1st Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "name": "The Day Of The Triffids",
        "variation": "2nd Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "name": "Morphy Richards Food Mixer",
        "variation": "Deluxe",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great"
    })")
};

products.insert_many(product_docs); // Might throw an exception

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "product_name": "Asus Laptop",
        "product_variation": "Standard Display",
        "value": 431.43
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559062412000},
        "product_name": "The Day Of The Triffids",
        "product_variation": "2nd Edition",
        "value": 5.01
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137000},
        "product_name": "Morphy Richards Food Mixer",
        "product_variation": "Deluxe",
        "value": 63.13
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "jjones@tepidmail.com",
        "orderdate": {"$date": 1608972946000},
        "product_name": "Asus Laptop",
        "product_variation": "Standard Display",
        "value": 429.65
    })")
};

orders.insert_many(order_docs); // Might throw an exception
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```cpp
auto embed_match_stage1 = bsoncxx::from_json(R"({
    "$match": {
        "$expr": {
            "$and": [
                { "$eq": ["$product_name", "$$prdname"] },
                { "$eq": ["$product_variation", "$$prdvartn"] }
            ]
        }
    }
})");
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```cpp
auto embed_match_stage2 = bsoncxx::from_json(R"({
    "$match": {
        "orderdate": {
            "$gte": { "$date": 1577836800000 },
            "$lt": { "$date": 1609459200000 }
        }
    }
})");
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```cpp
auto embed_unset_stage = bsoncxx::from_json(R"({
    "$unset": ["_id", "product_name", "product_variation"]
})");
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```cpp
pipeline.lookup(make_document(
    kvp("from", "orders"),
    kvp("let", make_document(
        kvp("prdname", "$name"),
        kvp("prdvartn", "$variation")
    )),
    kvp("pipeline", make_array(embed_match_stage1, embed_match_stage2, embed_unset_stage)),
    kvp("as", "orders")
));
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orders": { "$ne": [] }
})"));
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "description"]
})"));
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```cpp
auto cursor = products.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{ "name" : "Asus Laptop", "variation" : "Standard Display", "category" : "ELECTRONICS",
"orders" : [ { "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : "2020-05-30T06:55:52Z" },
"value" : 431.43000000000000682 }, { "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" :
"2020-12-26T08:55:46Z" }, "value" : 429.64999999999997726 } ] }
{ "name" : "Morphy Richards Food Mixer", "variation" : "Deluxe", "category" : "KITCHENWARE",
"orders" : [ { "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : "2020-01-01T06:45:37Z" },
"value" : 63.130000000000002558 } ] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```javascript
const products = aggDB.collection("products");
const orders = aggDB.collection("orders");

await products.deleteMany({});
await orders.deleteMany({});

await products.insertMany([
  {
    name: "Asus Laptop",
    variation: "Ultra HD",
    category: "ELECTRONICS",
    description: "Great for watching movies",
  },
  {
    name: "Asus Laptop",
    variation: "Standard Display",
    category: "ELECTRONICS",
    description: "Good value laptop for students",
  },
  {
    name: "The Day Of The Triffids",
    variation: "1st Edition",
    category: "BOOKS",
    description: "Classic post-apocalyptic novel",
  },
  {
    name: "The Day Of The Triffids",
    variation: "2nd Edition",
    category: "BOOKS",
    description: "Classic post-apocalyptic novel",
  },
  {
    name: "Morphy Richards Food Mixer",
    variation: "Deluxe",
    category: "KITCHENWARE",
    description: "Luxury mixer turning good cakes into great",
  },
]);

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    product_name: "Asus Laptop",
    product_variation: "Standard Display",
    value: 431.43,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    product_name: "The Day Of The Triffids",
    product_variation: "2nd Edition",
    value: 5.01,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    product_name: "Morphy Richards Food Mixer",
    product_variation: "Deluxe",
    value: 63.13,
  },
  {
    customer_id: "jjones@tepidmail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    product_name: "Asus Laptop",
    product_variation: "Standard Display",
    value: 429.65,
  },
]);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```javascript
const embedded_pl = [];

embedded_pl.push({
  $match: {
    $expr: {
      $and: [
        { $eq: ["$product_name", "$$prdname"] },
        { $eq: ["$product_variation", "$$prdvartn"] },
      ],
    },
  },
});
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```javascript
embedded_pl.push({
  $match: {
    orderdate: {
      $gte: new Date("2020-01-01T00:00:00Z"),
      $lt: new Date("2021-01-01T00:00:00Z"),
    },
  },
});
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```javascript
embedded_pl.push({
  $unset: ["_id", "product_name", "product_variation"],
});
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```javascript
pipeline.push({
  $lookup: {
    from: "orders",
    let: {
      prdname: "$name",
      prdvartn: "$variation",
    },
    pipeline: embedded_pl,
    as: "orders",
  },
});
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```javascript
pipeline.push({
  $match: {
    orders: { $ne: [] },
  },
});
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```javascript
pipeline.push({
  $unset: ["_id", "description"],
});
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```javascript
const aggregationResult = await products.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```javascript
{
  name: 'Asus Laptop',
  variation: 'Standard Display',
  category: 'ELECTRONICS',
  orders: [
    {
      customer_id: 'elise_smith@myemail.com',
      orderdate: 2020-05-30T08:35:52.000Z,
      value: 431.43
    },
    {
      customer_id: 'jjones@tepidmail.com',
      orderdate: 2020-12-26T08:55:46.000Z,
      value: 429.65
    }
  ]
}
{
  name: 'Morphy Richards Food Mixer',
  variation: 'Deluxe',
  category: 'KITCHENWARE',
  orders: [
    {
      customer_id: 'oranieri@warmmail.com',
      orderdate: 2020-01-01T08:25:37.000Z,
      value: 63.13
    }
  ]
}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**php:**

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

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```php
$products = $client->agg_tutorials_db->products;
$orders = $client->agg_tutorials_db->orders;

$products->deleteMany([]);
$orders->deleteMany([]);

$products->insertMany(
    [
        [
            'name' => "Asus Laptop",
            'variation' => "Ultra HD",
            'category' => "ELECTRONICS",
            'description' => "Great for watching movies"
        ],
        [
            'name' => "Asus Laptop",
            'variation' => "Standard Display",
            'category' => "ELECTRONICS",
            'description' => "Good value laptop for students"
        ],
        [
            'name' => "The Day Of The Triffids",
            'variation' => "1st Edition",
            'category' => "BOOKS",
            'description' => "Classic post-apocalyptic novel"
        ],
        [
            'name' => "The Day Of The Triffids",
            'variation' => "2nd Edition",
            'category' => "BOOKS",
            'description' => "Classic post-apocalyptic novel"
        ],
        [
            'name' => "Morphy Richards Food Mixer",
            'variation' => "Deluxe",
            'category' => "KITCHENWARE",
            'description' => "Luxury mixer turning good cakes into great"
        ]
    ]
);

$orders->insertMany(
    [
        [
            'customer_id' => "elise_smith@myemail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-05-30T08:35:52"))),
            'product_name' => "Asus Laptop",
            'product_variation' => "Standard Display",
            'value' => 431.43
        ],
        [
            'customer_id' => "tj@wheresmyemail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2019-05-28T19:13:32"))),
            'product_name' => "The Day Of The Triffids",
            'product_variation' => "2nd Edition",
            'value' => 5.01
        ],
        [
            'customer_id' => "oranieri@warmmail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-01-01T08:25:37"))),
            'product_name' => "Morphy Richards Food Mixer",
            'product_variation' => "Deluxe",
            'value' => 63.13
        ],
        [
            'customer_id' => "jjones@tepidmail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-12-26T08:55:46"))),
            'product_name' => "Asus Laptop",
            'product_variation' => "Standard Display",
            'value' => 429.65
        ]
    ]
);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join. First, create the
embedded pipeline:

```php
$embeddedPipeline = new Pipeline(
    // Add stages within embedded pipeline.
};
```

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```php
Stage::match(
    Query::expr(
        Expression::and(
            Expression::eq(
                Expression::stringFieldPath('product_name'),
                Expression::variable('prdname')
            ),
            Expression::eq(
                Expression::stringFieldPath('product_variation'),
                Expression::variable('prdvartn')
            ),
        )
    )
),
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```php
Stage::unset('_id', 'product_name', 'product_variation')
```

Next, outside of your `Pipeline` instances, create the
`$lookup` stage in a factory function. Configure this stage to
store the processed lookup fields in an array field called `orders`:

```php
function lookupOrdersStage(Pipeline $embeddedPipeline)
{
    return Stage::lookup(
        from: 'orders',
        let: object(
            prdname: Expression::stringFieldPath('name'),
            prdvartn: Expression::stringFieldPath('variation'),
        ),
        pipeline: $embeddedPipeline,
        as: 'orders',
    );
}
```

Then, in your main `Pipeline` instance, call the
`lookupOrdersStage()` function:

```php
lookupOrdersStage($embeddedPipeline),
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```php
Stage::match(
    orders: Query::ne([])
),
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```php
Stage::unset('_id', 'description')
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```php
$cursor = $products->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{
    "name": "Asus Laptop",
    "variation": "Standard Display",
    "category": "ELECTRONICS",
    "orders": [
        {
            "customer_id": "elise_smith@myemail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1590827752000"
                }
            },
            "value": 431.43
        },
        {
            "customer_id": "jjones@tepidmail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1608972946000"
                }
            },
            "value": 429.65
        }
    ]
}
{
    "name": "Morphy Richards Food Mixer",
    "variation": "Deluxe",
    "category": "KITCHENWARE",
    "orders": [
        {
            "customer_id": "oranieri@warmmail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1577867137000"
                }
            },
            "value": 63.13
        }
    ]
}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```ruby
products = agg_db[:products]
orders = agg_db[:orders]

products.delete_many({})
orders.delete_many({})

products.insert_many(
  [
    {
      name: "Asus Laptop",
      variation: "Ultra HD",
      category: "ELECTRONICS",
      description: "Great for watching movies",
    },
    {
      name: "Asus Laptop",
      variation: "Standard Display",
      category: "ELECTRONICS",
      description: "Good value laptop for students",
    },
    {
      name: "The Day Of The Triffids",
      variation: "1st Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      name: "The Day Of The Triffids",
      variation: "2nd Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      name: "Morphy Richards Food Mixer",
      variation: "Deluxe",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great",
    },
  ]
)

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 431.43,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      product_name: "The Day Of The Triffids",
      product_variation: "2nd Edition",
      value: 5.01,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      product_name: "Morphy Richards Food Mixer",
      product_variation: "Deluxe",
      value: 63.13,
    },
    {
      customer_id: "jjones@tepidmail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 429.65,
    },
  ]
)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```ruby
{
  "$match": {
    "$expr": {
      "$and": [
        { "$eq": ["$product_name", "$$prdname"] },
        { "$eq": ["$product_variation", "$$prdvartn"] },
      ],
    },
  },
},
```

Within the embedded pipeline, add another `$match` stage to match
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```ruby
{
  "$unset": ["_id", "product_name", "product_variation"],
},
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```ruby
{
  "$lookup": {
    from: "orders",
    let: {
      prdname: "$name",
      prdvartn: "$variation",
    },
    pipeline: embedded_pipeline,
    as: "orders",
  },
},
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```ruby
{
  "$match": {
    orders: { "$ne": [] },
  },
},
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```ruby
{
  "$unset": ["_id", "description"],
},
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```ruby
aggregation_result = products.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
ruby agg_tutorial.rb
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name"=>"Asus Laptop", "variation"=>"Standard Display", "category"=>"ELECTRONICS", "orders"=>[{"customer_id"=>"elise_smith@myemail.com", "orderdate"=>2020-05-30 08:35:52 UTC, "value"=>431.43}, {"customer_id"=>"jjones@tepidmail.com", "orderdate"=>2020-12-26 08:55:46 UTC, "value"=>429.65}]}
{"name"=>"Morphy Richards Food Mixer", "variation"=>"Deluxe", "category"=>"KITCHENWARE", "orders"=>[{"customer_id"=>"oranieri@warmmail.com", "orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

First, create Go structs to model the data in the `products` and `orders`
collections:

```go
type Product struct {
	Name        string
	Variation   string
	Category    string
	Description string
}

type Order struct {
	CustomerID       string        `bson:"customer_id"`
	OrderDate        bson.DateTime `bson:"orderdate"`
	ProductName      string        `bson:"product_name"`
	ProductVariation string        `bson:"product_variation"`
	Value            float32       `bson:"value"`
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```go
products := aggDB.Collection("products")
orders := aggDB.Collection("orders")
products.DeleteMany(context.TODO(), bson.D{})
orders.DeleteMany(context.TODO(), bson.D{})

_, err = products.InsertMany(context.TODO(), []interface{}{
	Product{
		Name:        "Asus Laptop",
		Variation:   "Ultra HD",
		Category:    "ELECTRONICS",
		Description: "Great for watching movies",
	},
	Product{
		Name:        "Asus Laptop",
		Variation:   "Standard Display",
		Category:    "ELECTRONICS",
		Description: "Good value laptop for students",
	},
	Product{
		Name:        "The Day Of The Triffids",
		Variation:   "1st Edition",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		Name:        "The Day Of The Triffids",
		Variation:   "2nd Edition",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		Name:        "Morphy Richards Food Mixer",
		Variation:   "Deluxe",
		Category:    "KITCHENWARE",
		Description: "Luxury mixer turning good cakes into great",
	},
})
if err != nil {
	log.Fatal(err)
}

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID:       "elise_smith@myemail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 52, 0, time.UTC)),
		ProductName:      "Asus Laptop",
		ProductVariation: "Standard Display",
		Value:            431.43,
	},
	Order{
		CustomerID:       "tj@wheresmyemail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		ProductName:      "The Day Of The Triffids",
		ProductVariation: "2nd Edition",
		Value:            5.01,
	},
	Order{
		CustomerID:       "oranieri@warmmail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 1, 1, 8, 25, 37, 0, time.UTC)),
		ProductName:      "Morphy Richards Food Mixer",
		ProductVariation: "Deluxe",
		Value:            63.13,
	},
	Order{
		CustomerID:       "jjones@tepidmail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		ProductName:      "Asus Laptop",
		ProductVariation: "Standard Display",
		Value:            429.65,
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```go
embeddedMatchStage1 := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "$expr", Value: bson.D{
			{Key: "$and", Value: bson.A{
				bson.D{{Key: "$eq", Value: bson.A{"$product_name", "$$prdname"}}},
				bson.D{{Key: "$eq", Value: bson.A{"$product_variation", "$$prdvartn"}}},
			}},
		}},
	}},
}
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```go
embeddedMatchStage2 := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "orderdate", Value: bson.D{
			{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
			{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
		}},
	}},
}
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```go
embeddedUnsetStage := bson.D{
	{Key: "$unset", Value: bson.A{"_id", "product_name", "product_variation"}},
}
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```go
embeddedPipeline := mongo.Pipeline{embeddedMatchStage1, embeddedMatchStage2, embeddedUnsetStage}

lookupStage := bson.D{
	{Key: "$lookup", Value: bson.D{
		{Key: "from", Value: "orders"},
		{Key: "let", Value: bson.D{
			{Key: "prdname", Value: "$name"},
			{Key: "prdvartn", Value: "$variation"},
		}},
		{Key: "pipeline", Value: embeddedPipeline},
		{Key: "as", Value: "orders"},
	}},
}
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```go
matchStage := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "orders", Value: bson.D{{Key: "$ne", Value: bson.A{}}}},
	}},
}
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```go
unsetStage := bson.D{
	{Key: "$unset", Value: bson.A{"_id", "description"}},
}
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```go
pipeline := mongo.Pipeline{lookupStage, matchStage, unsetStage}
cursor, err := products.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name":"Asus Laptop","variation":"Standard Display","category":"ELECTRONICS","orders":[{"customer_id":"elise_smith@myemail.com","orderdate":{"$date":"2020-05-30T08:35:52Z"},"value":431.42999267578125},{"customer_id":"jjones@tepidmail.com","orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":429.6499938964844}]}
{"name":"Morphy Richards Food Mixer","variation":"Deluxe","category":"KITCHENWARE","orders":[{"customer_id":"oranieri@warmmail.com","orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63.130001068115234}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

First, create Rust structs to model the data in the `products` and `orders`
collections:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Product {
    name: String,
    variation: String,
    category: String,
    description: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    order_date: DateTime,
    product_name: String,
    product_variation: String,
    value: f32,
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```rust
let products: Collection<Product> = agg_db.collection("products");
let orders: Collection<Order> = agg_db.collection("orders");

products.delete_many(doc! {}).await?;
orders.delete_many(doc! {}).await?;

let product_docs = vec![
    Product {
        name: "Asus Laptop".to_string(),
        variation: "Ultra HD".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Great for watching movies".to_string(),
    },
    Product {
        name: "Asus Laptop".to_string(),
        variation: "Standard Display".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Good value laptop for students".to_string(),
    },
    Product {
        name: "The Day Of The Triffids".to_string(),
        variation: "1st Edition".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        name: "The Day Of The Triffids".to_string(),
        variation: "2nd Edition".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        name: "Morphy Richards Food Mixer".to_string(),
        variation: "Deluxe".to_string(),
        category: "KITCHENWARE".to_string(),
        description: "Luxury mixer turning good cakes into great".to_string(),
    },
];
products.insert_many(product_docs).await?;

let order_docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(52).build().unwrap(),
        product_name: "Asus Laptop".to_string(),
        product_variation: "Standard Display".to_string(),
        value: 431.43,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        order_date: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        product_name: "The Day Of The Triffids".to_string(),
        product_variation: "2nd Edition".to_string(),
        value: 5.01,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        product_name: "Morphy Richards Food Mixer".to_string(),
        product_variation: "Deluxe".to_string(),
        value: 63.13,
    },
    Order {
        customer_id: "jjones@tepidmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        product_name: "Asus Laptop".to_string(),
        product_variation: "Standard Display".to_string(),
        value: 429.65,
    },
];
orders.insert_many(order_docs).await?;
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```rust
let mut embedded_pipeline = Vec::new();
embedded_pipeline.push(doc! {
    "$match": {
        "$expr": {
            "$and": [
                { "$eq": ["$product_name", "$$prdname"] },
                { "$eq": ["$product_variation", "$$prdvartn"] }
            ]
        }
    }
});
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```rust
embedded_pipeline.push(doc! {
    "$match": {
        "order_date": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap()
        }
    }
});
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```rust
embedded_pipeline.push(doc! {
    "$unset": ["_id", "product_name", "product_variation"]
});
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```rust
pipeline.push(doc! {
    "$lookup": {
        "from": "orders",
        "let": {
            "prdname": "$name",
            "prdvartn": "$variation"
        },
        "pipeline": embedded_pipeline,
        "as": "orders"
    }
});
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```rust
pipeline.push(doc! {
    "$match": {
        "orders": { "$ne": [] }
    }
});
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```rust
pipeline.push(doc! {
    "$unset": ["_id", "description"]
});
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```rust
let mut cursor = products.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
Document({"name": String("Asus Laptop"), "variation": String("Standard Display"), "category": String("ELECTRONICS"),
"orders": Array([Document({"customer_id": String("elise_smith@myemail.com"), "order_date": DateTime(2020-05-30 8:35:52.0 +00:00:00),
"value": Double(431.42999267578125)}), Document({"customer_id": String("jjones@tepidmail.com"), "order_date":
DateTime(2020-12-26 8:55:46.0 +00:00:00), "value": Double(429.6499938964844)})])})

Document({"name": String("Morphy Richards Food Mixer"), "variation": String("Deluxe"), "category": String("KITCHENWARE"),
"orders": Array([Document({"customer_id": String("oranieri@warmmail.com"), "order_date": DateTime(2020-01-01 8:25:37.0 +00:00:00),
"value": Double(63.130001068115234)})])})
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to join collections on multiple fields.

**shell:**

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `orders` and `products` collections, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      customer_id: "elise_smith@myemail.com",
      orderdate: new Date("2020-05-30T08:35:52Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 431.43,
   },
   {
      customer_id: "tj@wheresmyemail.com",
      orderdate: new Date("2019-05-28T19:13:32Z"),
      product_name: "The Day Of The Triffids",
      product_variation: "2nd Edition",
      value: 5.01,
   },
   {
      customer_id: "oranieri@warmmail.com",
      orderdate: new Date("2020-01-01T08:25:37Z"),
      product_name: "Morphy Richards Food Mixer",
      product_variation: "Deluxe",
      value: 63.13,
   },
   {
      customer_id: "jjones@tepidmail.com",
      orderdate: new Date("2020-12-26T08:55:46Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 429.65,
   }
] )
```

```javascript
db.products.deleteMany({})

db.products.insertMany( [
   {
      name: "Asus Laptop",
      variation: "Ultra HD",
      category: "ELECTRONICS",
      description: "Great for watching movies"
   },
   {
      name: "Asus Laptop",
      variation: "Standard Display",
      category: "ELECTRONICS",
      description: "Good value laptop for students"
   },
   {
      name: "The Day Of The Triffids",
      variation: "1st Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel"
   },
   {
      name: "The Day Of The Triffids",
      variation: "2nd Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel"
   },
   {
      name: "Morphy Richards Food Mixer",
      variation: "Deluxe",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great"
   }
] )
```

**Step 1: Create an embedded pipeline to use in the lookup stage.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The `$lookup` stage contains an embedded
pipeline to configure the join.

```javascript
embedded_pl = [
   // Stage 1: Match the values of two fields on each side of the join
   // The $eq filter uses aliases for the name and variation fields set
   { $match: {
      $expr: {
         $and: [
            { $eq: ["$product_name", "$$prdname"] },
            { $eq: ["$product_variation", "$$prdvartn"] }
         ]
      }
   } },

   // Stage 2: Match orders placed in 2020
   { $match: {
      orderdate: {
         $gte: new Date("2020-01-01T00:00:00Z"),
         $lt: new Date("2021-01-01T00:00:00Z")
      }
   } },

   // Stage 3: Remove unneeded fields from the orders collection side of the join
   { $unset: ["_id", "product_name", "product_variation"] }
]
```

**Step 2: Run the aggregation pipeline.**

```javascript
db.products.aggregate( [
   // Use the embedded pipeline in a lookup stage
   { $lookup: {
         from: "orders",
         let: {
            prdname: "$name",
            prdvartn: "$variation"
         },
         pipeline: embedded_pl,
         as: "orders"
   } },

   // Match products ordered in 2020
   { $match: { orders: { $ne: [] } } },

   // Remove unneeded fields
   { $unset: ["_id", "description"] }
] )
```

**Step 3: Interpret the aggregation results.**

The aggregated results contain two documents. The documents
represent products ordered 2020. Each document contains an
`orders` array field that lists details about each order for
that product.

```javascript
{
   name: 'Asus Laptop',
   variation: 'Standard Display',
   category: 'ELECTRONICS',
   orders: [
      {
         customer_id: 'elise_smith@myemail.com',
         orderdate: ISODate('2020-05-30T08:35:52.000Z'),
         value: 431.43
      },
      {
         customer_id: 'jjones@tepidmail.com',
         orderdate: ISODate('2020-12-26T08:55:46.000Z'),
         value: 429.65
      }
   ]
}
{
   name: 'Morphy Richards Food Mixer',
   variation: 'Deluxe',
   category: 'KITCHENWARE',
   orders: [
      {
         customer_id: 'oranieri@warmmail.com',
         orderdate: ISODate('2020-01-01T08:25:37.000Z'),
         value: 63.13
      }
   ]
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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```python
products_coll = agg_db["products"]
orders_coll = agg_db["orders"]

products_coll.delete_many({})

products_data = [
    {
        "name": "Asus Laptop",
        "variation": "Ultra HD",
        "category": "ELECTRONICS",
        "description": "Great for watching movies",
    },
    {
        "name": "Asus Laptop",
        "variation": "Standard Display",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students",
    },
    {
        "name": "The Day Of The Triffids",
        "variation": "1st Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel",
    },
    {
        "name": "The Day Of The Triffids",
        "variation": "2nd Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel",
    },
    {
        "name": "Morphy Richards Food Mixer",
        "variation": "Deluxe",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great",
    },
]

products_coll.insert_many(products_data)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```python
embedded_pl = [
    {
        "$match": {
            "$expr": {
                "$and": [
                    {"$eq": ["$product_name", "$$prdname"]},
                    {"$eq": ["$product_variation", "$$prdvartn"]},
                ]
            }
        }
    }
]
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```python
embedded_pl.append(
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```python
embedded_pl.append({"$unset": ["_id", "product_name", "product_variation"]})
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```python
pipeline.append(
    {
        "$lookup": {
            "from": "orders",
            "let": {"prdname": "$name", "prdvartn": "$variation"},
            "pipeline": embedded_pl,
            "as": "orders",
        }
    }
)
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```python
pipeline.append({"$match": {"orders": {"$ne": []}}})
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```python
pipeline.append({"$unset": ["_id", "description"]})
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```python
aggregation_result = products_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{'name': 'Asus Laptop', 'variation': 'Standard Display', 'category': 'ELECTRONICS', 'orders': [{'customer_id': 'elise_smith@myemail.com', 'orderdate': datetime.datetime(2020, 5, 30, 8, 35, 52), 'value': 431.43}, {'customer_id': 'jjones@tepidmail.com', 'orderdate': datetime.datetime(2020, 12, 26, 8, 55, 46), 'value': 429.65}]}
{'name': 'Morphy Richards Food Mixer', 'variation': 'Deluxe', 'category': 'KITCHENWARE', 'orders': [{'customer_id': 'oranieri@warmmail.com', 'orderdate': datetime.datetime(2020, 1, 1, 8, 25, 37), 'value': 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```java
MongoCollection<Document> products = aggDB.getCollection("products");
MongoCollection<Document> orders = aggDB.getCollection("orders");

products.deleteMany(Filters.empty());
orders.deleteMany(Filters.empty());

products.insertMany(
        Arrays.asList(
                new Document("name", "Asus Laptop")
                        .append("variation", "Ultra HD")
                        .append("category", "ELECTRONICS")
                        .append("description", "Great for watching movies"),

                new Document("name", "Asus Laptop")
                        .append("variation", "Standard Display")
                        .append("category", "ELECTRONICS")
                        .append("description", "Good value laptop for students"),

                new Document("name", "The Day Of The Triffids")
                        .append("variation", "1st Edition")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),

                new Document("name", "The Day Of The Triffids")
                        .append("variation", "2nd Edition")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),

                new Document("name", "Morphy Richards Food Mixer")
                        .append("variation", "Deluxe")
                        .append("category", "KITCHENWARE")
                        .append("description", "Luxury mixer turning good cakes into great")
        )
);

orders.insertMany(
        Arrays.asList(
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-05-30T08:35:52"))
                        .append("product_name", "Asus Laptop")
                        .append("product_variation", "Standard Display")
                        .append("value", 431.43),

                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2019-05-28T19:13:32"))
                        .append("product_name", "The Day Of The Triffids")
                        .append("product_variation", "2nd Edition")
                        .append("value", 5.01),

                new Document("customer_id", "oranieri@warmmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-01-01T08:25:37"))
                        .append("product_name", "Morphy Richards Food Mixer")
                        .append("product_variation", "Deluxe")
                        .append("value", 63.13),

                new Document("customer_id", "jjones@tepidmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-12-26T08:55:46"))
                        .append("product_name", "Asus Laptop")
                        .append("product_variation", "Standard Display")
                        .append("value", 429.65)
        )
);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```java
List<Bson> embeddedPipeline = new ArrayList<>();

embeddedPipeline.add(Aggregates.match(
        Filters.expr(
                Filters.and(
                        new Document("$eq", Arrays.asList("$product_name", "$$prdname")),
                        new Document("$eq", Arrays.asList("$product_variation", "$$prdvartn"))
                )
        )
));
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```java
embeddedPipeline.add(Aggregates.match(Filters.and(
        Filters.gte("orderdate", LocalDateTime.parse("2020-01-01T00:00:00")),
        Filters.lt("orderdate", LocalDateTime.parse("2021-01-01T00:00:00"))
)));
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```java
embeddedPipeline.add(Aggregates.unset("_id", "product_name", "product_variation"));
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```java
pipeline.add(Aggregates.lookup(
        "orders",
        Arrays.asList(
                new Variable<>("prdname", "$name"),
                new Variable<>("prdvartn", "$variation")
        ),
        embeddedPipeline,
        "orders"
));
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```java
pipeline.add(Aggregates.match(
        Filters.ne("orders", new ArrayList<>())
));
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```java
pipeline.add(Aggregates.unset("_id", "description"));
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```java
AggregateIterable<Document> aggregationResult = products.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name": "Asus Laptop", "variation": "Standard Display", "category": "ELECTRONICS", "orders": [{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T08:35:52Z"}, "value": 431.43}, {"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T08:55:46Z"}, "value": 429.65}]}
{"name": "Morphy Richards Food Mixer", "variation": "Deluxe", "category": "KITCHENWARE", "orders": [{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T08:25:37Z"}, "value": 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**kotlin-coroutine:**

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

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

First, create Kotlin data classes to model the data in the `products`
and `orders` collections:

```kotlin
@Serializable
data class Product(
    val name: String,
    val variation: String,
    val category: String,
    val description: String
)

@Serializable
data class Order(
    val customerID: String,
    @Contextual val orderDate: LocalDateTime,
    val productName: String,
    val productVariation: String,
    val value: Double
)
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```kotlin
val products = aggDB.getCollection<Product>("products")
val orders = aggDB.getCollection<Order>("orders")

products.deleteMany(Filters.empty());
orders.deleteMany(Filters.empty());

products.insertMany(
    listOf(
        Product("Asus Laptop", "Ultra HD", "ELECTRONICS", "Great for watching movies"),
        Product("Asus Laptop", "Standard Display", "ELECTRONICS", "Good value laptop for students"),
        Product("The Day Of The Triffids", "1st Edition", "BOOKS", "Classic post-apocalyptic novel"),
        Product("The Day Of The Triffids", "2nd Edition", "BOOKS", "Classic post-apocalyptic novel"),
        Product(
            "Morphy Richards Food Mixer",
            "Deluxe",
            "KITCHENWARE",
            "Luxury mixer turning good cakes into great"
        )
    )
)

orders.insertMany(
    listOf(
        Order(
            "elise_smith@myemail.com",
            LocalDateTime.parse("2020-05-30T08:35:52"),
            "Asus Laptop",
            "Standard Display",
            431.43
        ),
        Order(
            "tj@wheresmyemail.com",
            LocalDateTime.parse("2019-05-28T19:13:32"),
            "The Day Of The Triffids",
            "2nd Edition",
            5.01
        ),
        Order(
            "oranieri@warmmail.com",
            LocalDateTime.parse("2020-01-01T08:25:37"),
            "Morphy Richards Food Mixer",
            "Deluxe",
            63.13
        ),
        Order(
            "jjones@tepidmail.com",
            LocalDateTime.parse("2020-12-26T08:55:46"),
            "Asus Laptop",
            "Standard Display",
            429.65
        )
    )
)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```kotlin
val embeddedPipeline = mutableListOf<Bson>()

embeddedPipeline.add(
    Aggregates.match(
        Filters.expr(
            Document(
                "\$and", listOf(
                    Document("\$eq", listOf("\$${Order::productName.name}", "$\$prdname")),
                    Document("\$eq", listOf("\$${Order::productVariation.name}", "$\$prdvartn"))
                )
            )
        )
    )
)
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```kotlin
embeddedPipeline.add(
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```kotlin
embeddedPipeline.add(Aggregates.unset("_id", Order::productName.name, Order::productVariation.name))
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```kotlin
pipeline.add(
    Aggregates.lookup(
        "orders",
        listOf(
            Variable("prdname", "\$${Product::name.name}"),
            Variable("prdvartn", "\$${Product::variation.name}")
        ),
        embeddedPipeline,
        "orders"
    )
)
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.ne("orders", mutableListOf<Document>())
    )
)
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```kotlin
pipeline.add(Aggregates.unset("_id", "description"))
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```kotlin
val aggregationResult = products.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
Document{{name=Asus Laptop, variation=Standard Display, category=ELECTRONICS, orders=[Document{{customerID=elise_smith@myemail.com, orderDate=Sat May 30 04:35:52 EDT 2020, value=431.43}}, Document{{customerID=jjones@tepidmail.com, orderDate=Sat Dec 26 03:55:46 EST 2020, value=429.65}}]}}
Document{{name=Morphy Richards Food Mixer, variation=Deluxe, category=KITCHENWARE, orders=[Document{{customerID=oranieri@warmmail.com, orderDate=Wed Jan 01 03:25:37 EST 2020, value=63.13}}]}}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```scala
val products = aggDB.getCollection("products")
val orders = aggDB.getCollection("orders")

products.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

products.insertMany(
  Seq(
    Document(
      "name" -> "Asus Laptop",
      "variation" -> "Ultra HD",
      "category" -> "ELECTRONICS",
      "description" -> "Great for watching movies"
    ),
    Document(
      "name" -> "Asus Laptop",
      "variation" -> "Standard Display",
      "category" -> "ELECTRONICS",
      "description" -> "Good value laptop for students"
    ),
    Document(
      "name" -> "The Day Of The Triffids",
      "variation" -> "1st Edition",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "name" -> "The Day Of The Triffids",
      "variation" -> "2nd Edition",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "name" -> "Morphy Richards Food Mixer",
      "variation" -> "Deluxe",
      "category" -> "KITCHENWARE",
      "description" -> "Luxury mixer turning good cakes into great"
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

orders.insertMany(
  Seq(
    Document(
      "customer_id" -> "elise_smith@myemail.com",
      "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
      "product_name" -> "Asus Laptop",
      "product_variation" -> "Standard Display",
      "value" -> 431.43
    ),
    Document(
      "customer_id" -> "tj@wheresmyemail.com",
      "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
      "product_name" -> "The Day Of The Triffids",
      "product_variation" -> "2nd Edition",
      "value" -> 5.01
    ),
    Document(
      "customer_id" -> "oranieri@warmmail.com",
      "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
      "product_name" -> "Morphy Richards Food Mixer",
      "product_variation" -> "Deluxe",
      "value" -> 63.13
    ),
    Document(
      "customer_id" -> "jjones@tepidmail.com",
      "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
      "product_name" -> "Asus Laptop",
      "product_variation" -> "Standard Display",
      "value" -> 429.65
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```scala
Aggregates.filter(
  Filters.expr(
    Filters.and(
      Document("$eq" -> Seq("$product_name", "$$prdname")),
      Document("$eq" -> Seq("$product_variation", "$$prdvartn"))
    )
  )
),
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```scala
Aggregates.filter(
  Filters.and(
    Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
    Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
  )
),
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```scala
Aggregates.unset("_id", "product_name", "product_variation"),
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```scala
Aggregates.lookup(
  "orders",
  Seq(
    Variable("prdname", "$name"),
    Variable("prdvartn", "$variation"),
  ),
  embeddedPipeline,
  "orders"
),
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```scala
Aggregates.filter(Filters.ne("orders", Seq())),
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```scala
Aggregates.unset("_id", "description")
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```scala
products.aggregate(pipeline)
  .subscribe(
    (doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"),
  )
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name": "Asus Laptop", "variation": "Standard Display", "category": "ELECTRONICS", "orders": [{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 431.43}, {"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 429.65}]}
{"name": "Morphy Richards Food Mixer", "variation": "Deluxe", "category": "KITCHENWARE", "orders": [{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `Name` and
`Variation` fields in documents in the `products` collection, corresponding
to the `ProductName` and `ProductVariation` fields in documents in the
`orders` collection.

First, create C# classes to model the data in the `products` and `orders`
collections:

```csharp
public class Product
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string Name { get; set; }
  public string Variation { get; set; }
  public string Category { get; set; }
  public string Description { get; set; }
}

public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public string ProductName { get; set; }
  public string ProductVariation { get; set; }
  public double Value { get; set; }
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```csharp
var products = aggDB.GetCollection<Product>("products");
var orders = aggDB.GetCollection<Order>("orders");
products.DeleteMany(Builders<Product>.Filter.Empty);
orders.DeleteMany(Builders<Order>.Filter.Empty);

products.InsertMany(new List<Product>
{
    new Product
    {
        Name = "Asus Laptop",
        Variation = "Ultra HD",
        Category = "ELECTRONICS",
        Description = "Great for watching movies"
    },
    new Product
    {
        Name = "Asus Laptop",
        Variation = "Standard Display",
        Category = "ELECTRONICS",
        Description = "Good value laptop for students"
    },
    new Product
    {
        Name = "The Day Of The Triffids",
        Variation = "1st Edition",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Name = "The Day Of The Triffids",
        Variation = "2nd Edition",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Name = "Morphy Richards Food Mixer",
        Variation = "Deluxe",
        Category = "KITCHENWARE",
        Description = "Luxury mixer turning good cakes into great"
    }
});

orders.InsertMany(new List<Order>
{
    new Order
    {
        CustomerId = "elise_smith@myemail.com",
        OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
        ProductName = "Asus Laptop",
        ProductVariation = "Standard Display",
        Value = 431.43
    },
    new Order
    {
        CustomerId = "tj@wheresmyemail.com",
        OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
        ProductName = "The Day Of The Triffids",
        ProductVariation = "2nd Edition",
        Value = 5.01
    },
    new Order
    {
        CustomerId = "oranieri@warmmail.com",
        OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
        ProductName = "Morphy Richards Food Mixer",
        ProductVariation = "Deluxe",
        Value = 63.13
    },
    new Order
    {
        CustomerId = "jjones@tepidmail.com",
        OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
        ProductName = "Asus Laptop",
        ProductVariation = "Standard Display",
        Value = 429.65
    }
});
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to
join the `orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Instantiate the embedded pipeline, then chain a `$match`
stage to match the values of two fields on each side of the join.
Note that the following code uses aliases for the `Name` and
`Variation` fields set when creating the $lookup stage:

```csharp
var embeddedPipeline = new EmptyPipelineDefinition<Order>()
    .Match(new BsonDocument("$expr",
        new BsonDocument("$and", new BsonArray
        {
                new BsonDocument("$eq", new BsonArray { "$ProductName", "$$prdname" }),
                new BsonDocument("$eq", new BsonArray { "$ProductVariation", "$$prdvartn" })
        })))
```

Within the embedded pipeline, add another `$match`
stage to match orders placed in 2020:

```csharp
.Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
            o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

Within the embedded pipeline, add a `$project` stage to
remove unneeded fields from the `orders` collection side of the join:

```csharp
.Project(Builders<Order>.Projection
        .Exclude(o => o.Id)
        .Exclude(o => o.ProductName)
        .Exclude(o => o.ProductVariation));
```

After the embedded pipeline is completed, start the main
aggregation on the `products` collection and chain the
`$lookup` stage. Configure this stage to store the processed
lookup fields in an array field called `Orders`:

```csharp
var results = products.Aggregate()
    .Lookup<Order, BsonDocument, IEnumerable<BsonDocument>, BsonDocument>(
        foreignCollection: orders,
        let: new BsonDocument { { "prdname", "$Name" }, { "prdvartn", "$Variation" } },
        lookupPipeline: embeddedPipeline,
        "Orders"
    )
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `Orders` array created in the previous step:

```csharp
.Match(Builders<BsonDocument>.Filter.Ne("Orders", new BsonArray()))
```

**Step 3: Add a projection stage to remove unneeded fields.**

Finally, add a `$project` stage. The
`$project` stage removes the `_id` and `Description`
fields from the result documents:

```csharp
.Project(Builders<BsonDocument>.Projection
    .Exclude("_id")
    .Exclude("Description")
);
```

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `Orders` array field that lists details
about each order for that product:

```none
{ "Name" : "Asus Laptop", "Variation" : "Standard Display", "Category" : "ELECTRONICS", "Orders" : [{ "CustomerId" : "elise_smith@myemail.com", "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 431.43000000000001 }, { "CustomerId" : "jjones@tepidmail.com", "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 429.64999999999998 }] }
{ "Name" : "Morphy Richards Food Mixer", "Variation" : "Deluxe", "Category" : "KITCHENWARE", "Orders" : [{ "CustomerId" : "oranieri@warmmail.com", "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63.130000000000003 }] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```c
mongoc_collection_t *products = mongoc_client_get_collection(client, "agg_tutorials_db", "products");
mongoc_collection_t *orders = mongoc_client_get_collection(client, "agg_tutorials_db", "orders");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(products, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    if (!mongoc_collection_delete_many(orders, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 5;
    bson_t *product_docs[num_docs];

    product_docs[0] = BCON_NEW(
        "name", BCON_UTF8("Asus Laptop"),
        "variation", BCON_UTF8("Ultra HD"),
        "category", BCON_UTF8("ELECTRONICS"),
        "description", BCON_UTF8("Great for watching movies"));

    product_docs[1] = BCON_NEW(
        "name", BCON_UTF8("Asus Laptop"),
        "variation", BCON_UTF8("Standard Display"),
        "category", BCON_UTF8("ELECTRONICS"),
        "description", BCON_UTF8("Good value laptop for students"));

    product_docs[2] = BCON_NEW(
        "name", BCON_UTF8("The Day Of The Triffids"),
        "variation", BCON_UTF8("1st Edition"),
        "category", BCON_UTF8("BOOKS"),
        "description", BCON_UTF8("Classic post-apocalyptic novel"));

    product_docs[3] = BCON_NEW(
        "name", BCON_UTF8("The Day Of The Triffids"),
        "variation", BCON_UTF8("2nd Edition"),
        "category", BCON_UTF8("BOOKS"),
        "description", BCON_UTF8("Classic post-apocalyptic novel"));

    product_docs[4] = BCON_NEW(
        "name", BCON_UTF8("Morphy Richards Food Mixer"),
        "variation", BCON_UTF8("Deluxe"),
        "category", BCON_UTF8("KITCHENWARE"),
        "description", BCON_UTF8("Luxury mixer turning good cakes into great"));

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

{
    size_t num_docs = 4;
    bson_t *order_docs[num_docs];

    order_docs[0] = BCON_NEW(
        "customer_id", BCON_UTF8("elise_smith@myemail.com"),
        "orderdate", BCON_DATE_TIME(1590822952000UL), // 2020-05-30T08:35:52Z
        "product_name", BCON_UTF8("Asus Laptop"),
        "product_variation", BCON_UTF8("Standard Display"),
        "value", BCON_DOUBLE(431.43));

    order_docs[1] = BCON_NEW(
        "customer_id", BCON_UTF8("tj@wheresmyemail.com"),
        "orderdate", BCON_DATE_TIME(1559063612000UL), // 2019-05-28T19:13:32Z
        "product_name", BCON_UTF8("The Day Of The Triffids"),
        "product_variation", BCON_UTF8("2nd Edition"),
        "value", BCON_DOUBLE(5.01));

    order_docs[2] = BCON_NEW(
        "customer_id", BCON_UTF8("oranieri@warmmail.com"),
        "orderdate", BCON_DATE_TIME(1577869537000UL), // 2020-01-01T08:25:37Z
        "product_name", BCON_UTF8("Morphy Richards Food Mixer"),
        "product_variation", BCON_UTF8("Deluxe"),
        "value", BCON_DOUBLE(63.13));

    order_docs[3] = BCON_NEW(
        "customer_id", BCON_UTF8("jjones@tepidmail.com"),
        "orderdate", BCON_DATE_TIME(1608976546000UL), // 2020-12-26T08:55:46Z
        "product_name", BCON_UTF8("Asus Laptop"),
        "product_variation", BCON_UTF8("Standard Display"),
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
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to
join the `orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Create the embedded pipeline, then add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```c
bson_t embedded_pipeline;
bson_array_builder_t *bab = bson_array_builder_new();

bson_array_builder_append_document(bab, BCON_NEW(
                                            "$match", "{",
                                            "$expr", "{", "$and",
                                            "[",
                                            "{", "$eq", "[", BCON_UTF8("$product_name"), BCON_UTF8("$$prdname"), "]", "}",
                                            "{", "$eq", "[", BCON_UTF8("$product_variation"), BCON_UTF8("$$prdvartn"), "]", "}",
                                            "]",
                                            "}",
                                            "}"));
```

Within the embedded pipeline, add another `$match` stage
to match orders placed in 2020:

```c
bson_array_builder_append_document(bab, BCON_NEW(
                                            "$match", "{", "orderdate",
                                            "{",
                                            "$gte", BCON_DATE_TIME(1577836800000UL),
                                            "$lt", BCON_DATE_TIME(1609459200000UL),
                                            "}",
                                            "}"));
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```c
bson_array_builder_append_document(bab, BCON_NEW(
                                            "$unset",
                                            "[", BCON_UTF8("_id"), BCON_UTF8("product_name"), BCON_UTF8("product_variation"),
                                            "]"));

// Builds the embedded pipeline array and cleans up resources
bson_array_builder_build(bab, &embedded_pipeline);
bson_array_builder_destroy(bab);
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```c
"{", "$lookup", "{",
"from", BCON_UTF8("orders"),
"let", "{",
"prdname", BCON_UTF8("$name"),
"prdvartn", BCON_UTF8("$variation"),
"}",
"pipeline", BCON_ARRAY(&embedded_pipeline),
"as", BCON_UTF8("orders"),
"}", "}",
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```c
"{",
"$match", "{",
"orders", "{", "$ne", "[", "]", "}",
"}", "}",
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("description"), "]", "}",
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(products, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(&embedded_pipeline);
bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(products);
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

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{ "name" : "Asus Laptop", "variation" : "Standard Display", "category" : "ELECTRONICS", "orders" : [ { "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : { "$numberLong" : "1590822952000" } }, "value" : { "$numberDouble" : "431.43000000000000682" } }, { "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" : { "$numberLong" : "1608976546000" } }, "value" : { "$numberDouble" : "429.64999999999997726" } } ] }
{ "name" : "Morphy Richards Food Mixer", "variation" : "Deluxe", "category" : "KITCHENWARE", "orders" : [ { "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : { "$numberLong" : "1577869537000" } }, "value" : { "$numberDouble" : "63.130000000000002558" } } ] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```cpp
auto products = db["products"];
auto orders = db["orders"];

std::vector<bsoncxx::document::value> product_docs = {
    bsoncxx::from_json(R"({
        "name": "Asus Laptop",
        "variation": "Ultra HD",
        "category": "ELECTRONICS",
        "description": "Great for watching movies"
    })"),
    bsoncxx::from_json(R"({
        "name": "Asus Laptop",
        "variation": "Standard Display",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students"
    })"),
    bsoncxx::from_json(R"({
        "name": "The Day Of The Triffids",
        "variation": "1st Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "name": "The Day Of The Triffids",
        "variation": "2nd Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "name": "Morphy Richards Food Mixer",
        "variation": "Deluxe",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great"
    })")
};

products.insert_many(product_docs); // Might throw an exception

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "product_name": "Asus Laptop",
        "product_variation": "Standard Display",
        "value": 431.43
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559062412000},
        "product_name": "The Day Of The Triffids",
        "product_variation": "2nd Edition",
        "value": 5.01
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137000},
        "product_name": "Morphy Richards Food Mixer",
        "product_variation": "Deluxe",
        "value": 63.13
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "jjones@tepidmail.com",
        "orderdate": {"$date": 1608972946000},
        "product_name": "Asus Laptop",
        "product_variation": "Standard Display",
        "value": 429.65
    })")
};

orders.insert_many(order_docs); // Might throw an exception
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```cpp
auto embed_match_stage1 = bsoncxx::from_json(R"({
    "$match": {
        "$expr": {
            "$and": [
                { "$eq": ["$product_name", "$$prdname"] },
                { "$eq": ["$product_variation", "$$prdvartn"] }
            ]
        }
    }
})");
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```cpp
auto embed_match_stage2 = bsoncxx::from_json(R"({
    "$match": {
        "orderdate": {
            "$gte": { "$date": 1577836800000 },
            "$lt": { "$date": 1609459200000 }
        }
    }
})");
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```cpp
auto embed_unset_stage = bsoncxx::from_json(R"({
    "$unset": ["_id", "product_name", "product_variation"]
})");
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```cpp
pipeline.lookup(make_document(
    kvp("from", "orders"),
    kvp("let", make_document(
        kvp("prdname", "$name"),
        kvp("prdvartn", "$variation")
    )),
    kvp("pipeline", make_array(embed_match_stage1, embed_match_stage2, embed_unset_stage)),
    kvp("as", "orders")
));
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orders": { "$ne": [] }
})"));
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "description"]
})"));
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```cpp
auto cursor = products.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{ "name" : "Asus Laptop", "variation" : "Standard Display", "category" : "ELECTRONICS",
"orders" : [ { "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : "2020-05-30T06:55:52Z" },
"value" : 431.43000000000000682 }, { "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" :
"2020-12-26T08:55:46Z" }, "value" : 429.64999999999997726 } ] }
{ "name" : "Morphy Richards Food Mixer", "variation" : "Deluxe", "category" : "KITCHENWARE",
"orders" : [ { "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : "2020-01-01T06:45:37Z" },
"value" : 63.130000000000002558 } ] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```javascript
const products = aggDB.collection("products");
const orders = aggDB.collection("orders");

await products.deleteMany({});
await orders.deleteMany({});

await products.insertMany([
  {
    name: "Asus Laptop",
    variation: "Ultra HD",
    category: "ELECTRONICS",
    description: "Great for watching movies",
  },
  {
    name: "Asus Laptop",
    variation: "Standard Display",
    category: "ELECTRONICS",
    description: "Good value laptop for students",
  },
  {
    name: "The Day Of The Triffids",
    variation: "1st Edition",
    category: "BOOKS",
    description: "Classic post-apocalyptic novel",
  },
  {
    name: "The Day Of The Triffids",
    variation: "2nd Edition",
    category: "BOOKS",
    description: "Classic post-apocalyptic novel",
  },
  {
    name: "Morphy Richards Food Mixer",
    variation: "Deluxe",
    category: "KITCHENWARE",
    description: "Luxury mixer turning good cakes into great",
  },
]);

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    product_name: "Asus Laptop",
    product_variation: "Standard Display",
    value: 431.43,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    product_name: "The Day Of The Triffids",
    product_variation: "2nd Edition",
    value: 5.01,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    product_name: "Morphy Richards Food Mixer",
    product_variation: "Deluxe",
    value: 63.13,
  },
  {
    customer_id: "jjones@tepidmail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    product_name: "Asus Laptop",
    product_variation: "Standard Display",
    value: 429.65,
  },
]);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```javascript
const embedded_pl = [];

embedded_pl.push({
  $match: {
    $expr: {
      $and: [
        { $eq: ["$product_name", "$$prdname"] },
        { $eq: ["$product_variation", "$$prdvartn"] },
      ],
    },
  },
});
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```javascript
embedded_pl.push({
  $match: {
    orderdate: {
      $gte: new Date("2020-01-01T00:00:00Z"),
      $lt: new Date("2021-01-01T00:00:00Z"),
    },
  },
});
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```javascript
embedded_pl.push({
  $unset: ["_id", "product_name", "product_variation"],
});
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```javascript
pipeline.push({
  $lookup: {
    from: "orders",
    let: {
      prdname: "$name",
      prdvartn: "$variation",
    },
    pipeline: embedded_pl,
    as: "orders",
  },
});
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```javascript
pipeline.push({
  $match: {
    orders: { $ne: [] },
  },
});
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```javascript
pipeline.push({
  $unset: ["_id", "description"],
});
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```javascript
const aggregationResult = await products.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```javascript
{
  name: 'Asus Laptop',
  variation: 'Standard Display',
  category: 'ELECTRONICS',
  orders: [
    {
      customer_id: 'elise_smith@myemail.com',
      orderdate: 2020-05-30T08:35:52.000Z,
      value: 431.43
    },
    {
      customer_id: 'jjones@tepidmail.com',
      orderdate: 2020-12-26T08:55:46.000Z,
      value: 429.65
    }
  ]
}
{
  name: 'Morphy Richards Food Mixer',
  variation: 'Deluxe',
  category: 'KITCHENWARE',
  orders: [
    {
      customer_id: 'oranieri@warmmail.com',
      orderdate: 2020-01-01T08:25:37.000Z,
      value: 63.13
    }
  ]
}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**php:**

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

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```php
$products = $client->agg_tutorials_db->products;
$orders = $client->agg_tutorials_db->orders;

$products->deleteMany([]);
$orders->deleteMany([]);

$products->insertMany(
    [
        [
            'name' => "Asus Laptop",
            'variation' => "Ultra HD",
            'category' => "ELECTRONICS",
            'description' => "Great for watching movies"
        ],
        [
            'name' => "Asus Laptop",
            'variation' => "Standard Display",
            'category' => "ELECTRONICS",
            'description' => "Good value laptop for students"
        ],
        [
            'name' => "The Day Of The Triffids",
            'variation' => "1st Edition",
            'category' => "BOOKS",
            'description' => "Classic post-apocalyptic novel"
        ],
        [
            'name' => "The Day Of The Triffids",
            'variation' => "2nd Edition",
            'category' => "BOOKS",
            'description' => "Classic post-apocalyptic novel"
        ],
        [
            'name' => "Morphy Richards Food Mixer",
            'variation' => "Deluxe",
            'category' => "KITCHENWARE",
            'description' => "Luxury mixer turning good cakes into great"
        ]
    ]
);

$orders->insertMany(
    [
        [
            'customer_id' => "elise_smith@myemail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-05-30T08:35:52"))),
            'product_name' => "Asus Laptop",
            'product_variation' => "Standard Display",
            'value' => 431.43
        ],
        [
            'customer_id' => "tj@wheresmyemail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2019-05-28T19:13:32"))),
            'product_name' => "The Day Of The Triffids",
            'product_variation' => "2nd Edition",
            'value' => 5.01
        ],
        [
            'customer_id' => "oranieri@warmmail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-01-01T08:25:37"))),
            'product_name' => "Morphy Richards Food Mixer",
            'product_variation' => "Deluxe",
            'value' => 63.13
        ],
        [
            'customer_id' => "jjones@tepidmail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-12-26T08:55:46"))),
            'product_name' => "Asus Laptop",
            'product_variation' => "Standard Display",
            'value' => 429.65
        ]
    ]
);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join. First, create the
embedded pipeline:

```php
$embeddedPipeline = new Pipeline(
    // Add stages within embedded pipeline.
};
```

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```php
Stage::match(
    Query::expr(
        Expression::and(
            Expression::eq(
                Expression::stringFieldPath('product_name'),
                Expression::variable('prdname')
            ),
            Expression::eq(
                Expression::stringFieldPath('product_variation'),
                Expression::variable('prdvartn')
            ),
        )
    )
),
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```php
Stage::unset('_id', 'product_name', 'product_variation')
```

Next, outside of your `Pipeline` instances, create the
`$lookup` stage in a factory function. Configure this stage to
store the processed lookup fields in an array field called `orders`:

```php
function lookupOrdersStage(Pipeline $embeddedPipeline)
{
    return Stage::lookup(
        from: 'orders',
        let: object(
            prdname: Expression::stringFieldPath('name'),
            prdvartn: Expression::stringFieldPath('variation'),
        ),
        pipeline: $embeddedPipeline,
        as: 'orders',
    );
}
```

Then, in your main `Pipeline` instance, call the
`lookupOrdersStage()` function:

```php
lookupOrdersStage($embeddedPipeline),
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```php
Stage::match(
    orders: Query::ne([])
),
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```php
Stage::unset('_id', 'description')
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```php
$cursor = $products->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{
    "name": "Asus Laptop",
    "variation": "Standard Display",
    "category": "ELECTRONICS",
    "orders": [
        {
            "customer_id": "elise_smith@myemail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1590827752000"
                }
            },
            "value": 431.43
        },
        {
            "customer_id": "jjones@tepidmail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1608972946000"
                }
            },
            "value": 429.65
        }
    ]
}
{
    "name": "Morphy Richards Food Mixer",
    "variation": "Deluxe",
    "category": "KITCHENWARE",
    "orders": [
        {
            "customer_id": "oranieri@warmmail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1577867137000"
                }
            },
            "value": 63.13
        }
    ]
}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```ruby
products = agg_db[:products]
orders = agg_db[:orders]

products.delete_many({})
orders.delete_many({})

products.insert_many(
  [
    {
      name: "Asus Laptop",
      variation: "Ultra HD",
      category: "ELECTRONICS",
      description: "Great for watching movies",
    },
    {
      name: "Asus Laptop",
      variation: "Standard Display",
      category: "ELECTRONICS",
      description: "Good value laptop for students",
    },
    {
      name: "The Day Of The Triffids",
      variation: "1st Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      name: "The Day Of The Triffids",
      variation: "2nd Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      name: "Morphy Richards Food Mixer",
      variation: "Deluxe",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great",
    },
  ]
)

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 431.43,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      product_name: "The Day Of The Triffids",
      product_variation: "2nd Edition",
      value: 5.01,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      product_name: "Morphy Richards Food Mixer",
      product_variation: "Deluxe",
      value: 63.13,
    },
    {
      customer_id: "jjones@tepidmail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 429.65,
    },
  ]
)
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```ruby
{
  "$match": {
    "$expr": {
      "$and": [
        { "$eq": ["$product_name", "$$prdname"] },
        { "$eq": ["$product_variation", "$$prdvartn"] },
      ],
    },
  },
},
```

Within the embedded pipeline, add another `$match` stage to match
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```ruby
{
  "$unset": ["_id", "product_name", "product_variation"],
},
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```ruby
{
  "$lookup": {
    from: "orders",
    let: {
      prdname: "$name",
      prdvartn: "$variation",
    },
    pipeline: embedded_pipeline,
    as: "orders",
  },
},
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```ruby
{
  "$match": {
    orders: { "$ne": [] },
  },
},
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```ruby
{
  "$unset": ["_id", "description"],
},
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```ruby
aggregation_result = products.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
ruby agg_tutorial.rb
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name"=>"Asus Laptop", "variation"=>"Standard Display", "category"=>"ELECTRONICS", "orders"=>[{"customer_id"=>"elise_smith@myemail.com", "orderdate"=>2020-05-30 08:35:52 UTC, "value"=>431.43}, {"customer_id"=>"jjones@tepidmail.com", "orderdate"=>2020-12-26 08:55:46 UTC, "value"=>429.65}]}
{"name"=>"Morphy Richards Food Mixer", "variation"=>"Deluxe", "category"=>"KITCHENWARE", "orders"=>[{"customer_id"=>"oranieri@warmmail.com", "orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

First, create Go structs to model the data in the `products` and `orders`
collections:

```go
type Product struct {
	Name        string
	Variation   string
	Category    string
	Description string
}

type Order struct {
	CustomerID       string        `bson:"customer_id"`
	OrderDate        bson.DateTime `bson:"orderdate"`
	ProductName      string        `bson:"product_name"`
	ProductVariation string        `bson:"product_variation"`
	Value            float32       `bson:"value"`
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```go
products := aggDB.Collection("products")
orders := aggDB.Collection("orders")
products.DeleteMany(context.TODO(), bson.D{})
orders.DeleteMany(context.TODO(), bson.D{})

_, err = products.InsertMany(context.TODO(), []interface{}{
	Product{
		Name:        "Asus Laptop",
		Variation:   "Ultra HD",
		Category:    "ELECTRONICS",
		Description: "Great for watching movies",
	},
	Product{
		Name:        "Asus Laptop",
		Variation:   "Standard Display",
		Category:    "ELECTRONICS",
		Description: "Good value laptop for students",
	},
	Product{
		Name:        "The Day Of The Triffids",
		Variation:   "1st Edition",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		Name:        "The Day Of The Triffids",
		Variation:   "2nd Edition",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		Name:        "Morphy Richards Food Mixer",
		Variation:   "Deluxe",
		Category:    "KITCHENWARE",
		Description: "Luxury mixer turning good cakes into great",
	},
})
if err != nil {
	log.Fatal(err)
}

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID:       "elise_smith@myemail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 52, 0, time.UTC)),
		ProductName:      "Asus Laptop",
		ProductVariation: "Standard Display",
		Value:            431.43,
	},
	Order{
		CustomerID:       "tj@wheresmyemail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		ProductName:      "The Day Of The Triffids",
		ProductVariation: "2nd Edition",
		Value:            5.01,
	},
	Order{
		CustomerID:       "oranieri@warmmail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 1, 1, 8, 25, 37, 0, time.UTC)),
		ProductName:      "Morphy Richards Food Mixer",
		ProductVariation: "Deluxe",
		Value:            63.13,
	},
	Order{
		CustomerID:       "jjones@tepidmail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		ProductName:      "Asus Laptop",
		ProductVariation: "Standard Display",
		Value:            429.65,
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```go
embeddedMatchStage1 := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "$expr", Value: bson.D{
			{Key: "$and", Value: bson.A{
				bson.D{{Key: "$eq", Value: bson.A{"$product_name", "$$prdname"}}},
				bson.D{{Key: "$eq", Value: bson.A{"$product_variation", "$$prdvartn"}}},
			}},
		}},
	}},
}
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```go
embeddedMatchStage2 := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "orderdate", Value: bson.D{
			{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
			{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
		}},
	}},
}
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```go
embeddedUnsetStage := bson.D{
	{Key: "$unset", Value: bson.A{"_id", "product_name", "product_variation"}},
}
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```go
embeddedPipeline := mongo.Pipeline{embeddedMatchStage1, embeddedMatchStage2, embeddedUnsetStage}

lookupStage := bson.D{
	{Key: "$lookup", Value: bson.D{
		{Key: "from", Value: "orders"},
		{Key: "let", Value: bson.D{
			{Key: "prdname", Value: "$name"},
			{Key: "prdvartn", Value: "$variation"},
		}},
		{Key: "pipeline", Value: embeddedPipeline},
		{Key: "as", Value: "orders"},
	}},
}
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```go
matchStage := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "orders", Value: bson.D{{Key: "$ne", Value: bson.A{}}}},
	}},
}
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```go
unsetStage := bson.D{
	{Key: "$unset", Value: bson.A{"_id", "description"}},
}
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```go
pipeline := mongo.Pipeline{lookupStage, matchStage, unsetStage}
cursor, err := products.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name":"Asus Laptop","variation":"Standard Display","category":"ELECTRONICS","orders":[{"customer_id":"elise_smith@myemail.com","orderdate":{"$date":"2020-05-30T08:35:52Z"},"value":431.42999267578125},{"customer_id":"jjones@tepidmail.com","orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":429.6499938964844}]}
{"name":"Morphy Richards Food Mixer","variation":"Deluxe","category":"KITCHENWARE","orders":[{"customer_id":"oranieri@warmmail.com","orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63.130001068115234}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop

An order can only contain one product. The aggregation uses a
multi-field join to match a product document to documents representing
orders of that product. The aggregation joins collections by the `name` and
`variation` fields in documents in the `products` collection, corresponding
to the `product_name` and `product_variation` fields in documents in the
`orders` collection.

First, create Rust structs to model the data in the `products` and `orders`
collections:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Product {
    name: String,
    variation: String,
    category: String,
    description: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    order_date: DateTime,
    product_name: String,
    product_variation: String,
    value: f32,
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```rust
let products: Collection<Product> = agg_db.collection("products");
let orders: Collection<Order> = agg_db.collection("orders");

products.delete_many(doc! {}).await?;
orders.delete_many(doc! {}).await?;

let product_docs = vec![
    Product {
        name: "Asus Laptop".to_string(),
        variation: "Ultra HD".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Great for watching movies".to_string(),
    },
    Product {
        name: "Asus Laptop".to_string(),
        variation: "Standard Display".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Good value laptop for students".to_string(),
    },
    Product {
        name: "The Day Of The Triffids".to_string(),
        variation: "1st Edition".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        name: "The Day Of The Triffids".to_string(),
        variation: "2nd Edition".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        name: "Morphy Richards Food Mixer".to_string(),
        variation: "Deluxe".to_string(),
        category: "KITCHENWARE".to_string(),
        description: "Luxury mixer turning good cakes into great".to_string(),
    },
];
products.insert_many(product_docs).await?;

let order_docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(52).build().unwrap(),
        product_name: "Asus Laptop".to_string(),
        product_variation: "Standard Display".to_string(),
        value: 431.43,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        order_date: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        product_name: "The Day Of The Triffids".to_string(),
        product_variation: "2nd Edition".to_string(),
        value: 5.01,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        product_name: "Morphy Richards Food Mixer".to_string(),
        product_variation: "Deluxe".to_string(),
        value: 63.13,
    },
    Order {
        customer_id: "jjones@tepidmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        product_name: "Asus Laptop".to_string(),
        product_variation: "Standard Display".to_string(),
        value: 429.65,
    },
];
orders.insert_many(order_docs).await?;
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join.

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```rust
let mut embedded_pipeline = Vec::new();
embedded_pipeline.push(doc! {
    "$match": {
        "$expr": {
            "$and": [
                { "$eq": ["$product_name", "$$prdname"] },
                { "$eq": ["$product_variation", "$$prdvartn"] }
            ]
        }
    }
});
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```rust
embedded_pipeline.push(doc! {
    "$match": {
        "order_date": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap()
        }
    }
});
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```rust
embedded_pipeline.push(doc! {
    "$unset": ["_id", "product_name", "product_variation"]
});
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```rust
pipeline.push(doc! {
    "$lookup": {
        "from": "orders",
        "let": {
            "prdname": "$name",
            "prdvartn": "$variation"
        },
        "pipeline": embedded_pipeline,
        "as": "orders"
    }
});
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```rust
pipeline.push(doc! {
    "$match": {
        "orders": { "$ne": [] }
    }
});
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```rust
pipeline.push(doc! {
    "$unset": ["_id", "description"]
});
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```rust
let mut cursor = products.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
Document({"name": String("Asus Laptop"), "variation": String("Standard Display"), "category": String("ELECTRONICS"),
"orders": Array([Document({"customer_id": String("elise_smith@myemail.com"), "order_date": DateTime(2020-05-30 8:35:52.0 +00:00:00),
"value": Double(431.42999267578125)}), Document({"customer_id": String("jjones@tepidmail.com"), "order_date":
DateTime(2020-12-26 8:55:46.0 +00:00:00), "value": Double(429.6499938964844)})])})

Document({"name": String("Morphy Richards Food Mixer"), "variation": String("Deluxe"), "category": String("KITCHENWARE"),
"orders": Array([Document({"customer_id": String("oranieri@warmmail.com"), "order_date": DateTime(2020-01-01 8:25:37.0 +00:00:00),
"value": Double(63.130001068115234)})])})
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.
