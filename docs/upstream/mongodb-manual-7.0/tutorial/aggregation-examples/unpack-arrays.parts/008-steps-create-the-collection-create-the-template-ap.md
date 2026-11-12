<!-- Part 8 of 11 of tutorial/aggregation-examples/unpack-arrays.md (split because the page is big). -->

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
