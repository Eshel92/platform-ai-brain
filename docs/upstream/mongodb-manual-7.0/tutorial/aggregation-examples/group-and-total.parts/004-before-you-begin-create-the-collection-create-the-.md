<!-- Part 4 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

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
