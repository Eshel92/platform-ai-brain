<!-- Part 3 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```scala
val orders = aggDB.getCollection("orders")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

orders.insertMany(Seq(
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
    "value" -> 231),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-01-13T09:32:07"),
    "value" -> 99),
  Document("customer_id" -> "oranieri@warmmail.com",
    "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
    "value" -> 63),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
    "value" -> 2),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2020-11-23T22:56:53"),
    "value" -> 187),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2020-08-18T23:04:48"),
    "value" -> 4),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
    "value" -> 4),
  Document("customer_id" -> "tj@wheresmyemail.com",
    "orderdate" -> dateFormat.parse("2021-02-28T07:49:32"),
    "value" -> 1024),
  Document("customer_id" -> "elise_smith@myemail.com",
    "orderdate" -> dateFormat.parse("2020-10-03T13:49:44"),
    "value" -> 102)
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```scala
Aggregates.filter(Filters.and(
  Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
  Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
)),
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```scala
Aggregates.sort(Sorts.ascending("orderdate")),
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

```scala
Aggregates.group(
  "$customer_id",
  Accumulators.first("first_purchase_date", "$orderdate"),
  Accumulators.sum("total_value", "$value"),
  Accumulators.sum("total_orders", 1),
  Accumulators.push("orders", Document("orderdate" -> "$orderdate", "value" -> "$value"))
),
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```scala
Aggregates.sort(Sorts.ascending("first_purchase_date")),
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```scala
Aggregates.set(Field("customer_id", "$_id")),
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```scala
Aggregates.unset("_id")
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date": {"$date": "2020-01-01T13:25:37Z"}, "total_value": 63, "total_orders": 1, "orders": [{"orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63}], "customer_id": "oranieri@warmmail.com"}
{"first_purchase_date": {"$date": "2020-01-13T14:32:07Z"}, "total_value": 436, "total_orders": 4, "orders": [{"orderdate": {"$date": "2020-01-13T14:32:07Z"}, "value": 99}, {"orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 231}, {"orderdate": {"$date": "2020-10-03T17:49:44Z"}, "value": 102}, {"orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 4}], "customer_id": "elise_smith@myemail.com"}
{"first_purchase_date": {"$date": "2020-08-19T03:04:48Z"}, "total_value": 191, "total_orders": 2, "orders": [{"orderdate": {"$date": "2020-08-19T03:04:48Z"}, "value": 4}, {"orderdate": {"$date": "2020-11-24T03:56:53Z"}, "value": 187}], "customer_id": "tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

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

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `CustomerId`
field, which contains customer email addresses.

First, create a C# class to model the data in the `orders`
collection:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public int Value { get; set; }
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
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
            Value = 231
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-01-13T09:32:07Z"),
            Value = 99
        },
        new Order
        {
            CustomerId = "oranieri@warmmail.com",
            OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
            Value = 63
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
            Value = 2
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2020-11-23T22:56:53Z"),
            Value = 187
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2020-08-18T23:04:48Z"),
            Value = 4
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
            Value = 4
        },
        new Order
        {
            CustomerId = "tj@wheresmyemail.com",
            OrderDate = DateTime.Parse("2021-02-28T07:49:32Z"),
            Value = 1024
        },
        new Order
        {
            CustomerId = "elise_smith@myemail.com",
            OrderDate = DateTime.Parse("2020-10-03T13:49:44Z"),
            Value = 102
        }
    });
```

**Step 1: Add a match stage for orders in 2020.**

First, start the aggregation on the `orders` collection and
chain a `$match` stage that matches orders placed in
2020:

```csharp
var results = orders.Aggregate()
    .Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
                o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `OrderDate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```csharp
.SortBy(o => o.OrderDate)
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to collect
order documents by the value of the `CustomerId` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `CustomerId`: the customer's email address (the grouping key)
- `FirstPurchaseDate`: the date of the customer's first purchase
- `TotalValue`: the total value of all the customer's purchases
- `TotalOrders`: the total number of the customer's purchases
- `Orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```csharp
.Group(
    o => o.CustomerId,
    g => new
    {
      CustomerId = g.Key,
      FirstPurchaseDate = g.First().OrderDate,
      TotalValue = g.Sum(i => i.Value),
      TotalOrders = g.Count(),
      Orders = g.Select(i => new { i.OrderDate, i.Value }).ToList()
    }
)
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `FirstPurchaseDate` field:

```csharp
.SortBy(c => c.FirstPurchaseDate)
.As<BsonDocument>();
```

The preceding code also converts the output documents to
`BsonDocument` instances for printing.

**Step 5: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "CustomerId" : "oranieri@warmmail.com", "FirstPurchaseDate" : { "$date" : "2020-01-01T08:25:37Z" }, "TotalValue" : 63, "TotalOrders" : 1, "Orders" : [{ "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63 }] }
{ "CustomerId" : "elise_smith@myemail.com", "FirstPurchaseDate" : { "$date" : "2020-01-13T09:32:07Z" }, "TotalValue" : 436, "TotalOrders" : 4, "Orders" : [{ "OrderDate" : { "$date" : "2020-01-13T09:32:07Z" }, "Value" : 99 }, { "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 231 }, { "OrderDate" : { "$date" : "2020-10-03T13:49:44Z" }, "Value" : 102 }, { "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 4 }] }
{ "CustomerId" : "tj@wheresmyemail.com", "FirstPurchaseDate" : { "$date" : "2020-08-18T23:04:48Z" }, "TotalValue" : 191, "TotalOrders" : 2, "Orders" : [{ "OrderDate" : { "$date" : "2020-08-18T23:04:48Z" }, "Value" : 4 }, { "OrderDate" : { "$date" : "2020-11-23T22:56:53Z" }, "Value" : 187 }] }
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

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
