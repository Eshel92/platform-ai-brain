<!-- Part 3 of 11 of tutorial/aggregation-examples/unpack-arrays.md (split because the page is big). -->

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
