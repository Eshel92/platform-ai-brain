<!-- Part 3 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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
