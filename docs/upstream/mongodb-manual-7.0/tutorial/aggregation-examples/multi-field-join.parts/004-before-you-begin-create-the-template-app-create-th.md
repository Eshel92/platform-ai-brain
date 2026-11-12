<!-- Part 4 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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
