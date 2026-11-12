<!-- Part 1 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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
