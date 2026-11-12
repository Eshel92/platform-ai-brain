<!-- Part 1 of 13 of tutorial/aggregation-examples/one-to-one-join.md (split because the page is big). -->

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
