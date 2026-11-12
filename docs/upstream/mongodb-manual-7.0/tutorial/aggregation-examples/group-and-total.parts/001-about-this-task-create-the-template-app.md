<!-- Part 1 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

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
