<!-- Part 9 of 13 of tutorial/aggregation-examples/one-to-one-join.md (split because the page is big). -->

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

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```scala
val orders = aggDB.getCollection("orders")
val products = aggDB.getCollection("products")

orders.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

products.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

orders.insertMany(
  Seq(
    Document(
      "customer_id" -> "elise_smith@myemail.com",
      "orderdate" -> dateFormat.parse("2020-05-30T08:35:52"),
      "product_id" -> "a1b2c3d4",
      "value" -> 431.43
    ),
    Document(
      "customer_id" -> "tj@wheresmyemail.com",
      "orderdate" -> dateFormat.parse("2019-05-28T19:13:32"),
      "product_id" -> "z9y8x7w6",
      "value" -> 5.01
    ),
    Document(
      "customer_id" -> "oranieri@warmmail.com",
      "orderdate" -> dateFormat.parse("2020-01-01T08:25:37"),
      "product_id" -> "ff11gg22hh33",
      "value" -> 63.13
    ),
    Document(
      "customer_id" -> "jjones@tepidmail.com",
      "orderdate" -> dateFormat.parse("2020-12-26T08:55:46"),
      "product_id" -> "a1b2c3d4",
      "value" -> 429.65
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

products.insertMany(
  Seq(
    Document(
      "id" -> "a1b2c3d4",
      "name" -> "Asus Laptop",
      "category" -> "ELECTRONICS",
      "description" -> "Good value laptop for students"
    ),
    Document(
      "id" -> "z9y8x7w6",
      "name" -> "The Day Of The Triffids",
      "category" -> "BOOKS",
      "description" -> "Classic post-apocalyptic novel"
    ),
    Document(
      "id" -> "ff11gg22hh33",
      "name" -> "Morphy Richardds Food Mixer",
      "category" -> "KITCHENWARE",
      "description" -> "Luxury mixer turning good cakes into great"
    ),
    Document(
      "id" -> "pqr678st",
      "name" -> "Karcher Hose Set",
      "category" -> "GARDEN",
      "description" -> "Hose + nosels + winder for tidy storage"
    )
  )
).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```scala
Aggregates.filter(Filters.and(
  Filters.gte("orderdate", dateFormat.parse("2020-01-01T00:00:00")),
  Filters.lt("orderdate", dateFormat.parse("2021-01-01T00:00:00"))
)),
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```scala
Aggregates.lookup(
  "products",
  "product_id",
  "id",
  "product_mapping"
),
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

```scala
Aggregates.set(Field("product_mapping", Document("$first" -> "$product_mapping"))),
Aggregates.set(
  Field("product_name", "$product_mapping.name"),
  Field("product_category", "$product_mapping.category")
),
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```scala
Aggregates.unset("_id", "product_id", "product_mapping")
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```scala
orders.aggregate(pipeline)
  .subscribe(
    (doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"),
  )
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T12:35:52Z"}, "value": 431.43, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T13:25:37Z"}, "value": 63.13, "product_name": "Morphy Richardds Food Mixer", "product_category": "KITCHENWARE"}
{"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T13:55:46Z"}, "value": 429.65, "product_name": "Asus Laptop", "product_category": "ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.


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

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `ProductId` field
that exists in documents in both collections.

First, create C# classes to model the data in the `orders` and `products`
collections:

```csharp
public class Order
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string CustomerId { get; set; }
  public DateTime OrderDate { get; set; }
  public string ProductId { get; set; }
  public double Value { get; set; }
}

public class Product
{
  [BsonId]
  public string Id { get; set; }
  public string Name { get; set; }
  public string Category { get; set; }
  public string Description { get; set; }
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```csharp
var orders = aggDB.GetCollection<Order>("orders");
var products = aggDB.GetCollection<Product>("products");
orders.DeleteMany(Builders<Order>.Filter.Empty);
products.DeleteMany(Builders<Product>.Filter.Empty);

orders.InsertMany(new List<Order>
{
    new Order
    {
        CustomerId = "elise_smith@myemail.com",
        OrderDate = DateTime.Parse("2020-05-30T08:35:52Z"),
        ProductId = "a1b2c3d4",
        Value = 431.43
    },
    new Order
    {
        CustomerId = "tj@wheresmyemail.com",
        OrderDate = DateTime.Parse("2019-05-28T19:13:32Z"),
        ProductId = "z9y8x7w6",
        Value = 5.01
    },
    new Order
    {
        CustomerId = "oranieri@warmmail.com",
        OrderDate = DateTime.Parse("2020-01-01T08:25:37Z"),
        ProductId = "ff11gg22hh33",
        Value = 63.13
    },
    new Order
    {
        CustomerId = "jjones@tepidmail.com",
        OrderDate = DateTime.Parse("2020-12-26T08:55:46Z"),
        ProductId = "a1b2c3d4",
        Value = 429.65
    }
});

products.InsertMany(new List<Product>
{
    new Product
    {
        Id = "a1b2c3d4",
        Name = "Asus Laptop",
        Category = "ELECTRONICS",
        Description = "Good value laptop for students"
    },
    new Product
    {
        Id = "z9y8x7w6",
        Name = "The Day Of The Triffids",
        Category = "BOOKS",
        Description = "Classic post-apocalyptic novel"
    },
    new Product
    {
        Id = "ff11gg22hh33",
        Name = "Morphy Richardds Food Mixer",
        Category = "KITCHENWARE",
        Description = "Luxury mixer turning good cakes into great"
    },
    new Product
    {
        Id = "pqr678st",
        Name = "Karcher Hose Set",
        Category = "GARDEN",
        Description = "Hose + nosels + winder for tidy storage"
    }
});
```

**Step 1: Add a match stage for orders in 2020.**

First, start the aggregation on the `orders` collection and
chain a `$match` stage that matches orders placed in 2020:

```csharp
var results = orders.Aggregate()
    .Match(o => o.OrderDate >= DateTime.Parse("2020-01-01T00:00:00Z") &&
                o.OrderDate < DateTime.Parse("2021-01-01T00:00:00Z"))
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `ProductId` field in the `orders`
collection to the `Id` field in the `products` collection:

```csharp
.Lookup<Product, Order>(
    foreignCollectionName: "products",
    localField: "ProductId",
    foreignField: "Id",
    @as: "ProductMapping"
)
```

**Step 3: Add a projection stage to create new document fields and omit unneeded fields.**

Next, add a `$project` stage to the pipeline.

The `$project` stage creates two new fields, `ProductName`
and `ProductCategory`, from the first entries of the respective
values in the `ProductMapping` object field. The stage also
specifies which fields to include and exclude from the output documents:

```csharp
.Project(new BsonDocument
    {
        { "ProductName", new BsonDocument("$first", "$ProductMapping.Name") },
        { "ProductCategory", new BsonDocument("$first", "$ProductMapping.Category") },
        { "OrderDate", 1 },
        { "CustomerId", 1 },
        { "Value", 1 },
        { "_id", 0 },
    });
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first` operator to retrieve the data from
this element.

**Step 4: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`ProductName` and `ProductCategory` of the ordered product:

```none
{ "CustomerId" : "elise_smith@myemail.com", "OrderDate" : { "$date" : "2020-05-30T08:35:52Z" }, "Value" : 431.43000000000001, "ProductName" : "Asus Laptop", "ProductCategory" : "ELECTRONICS" }
{ "CustomerId" : "oranieri@warmmail.com", "OrderDate" : { "$date" : "2020-01-01T08:25:37Z" }, "Value" : 63.130000000000003, "ProductName" : "Morphy Richardds Food Mixer", "ProductCategory" : "KITCHENWARE" }
{ "CustomerId" : "jjones@tepidmail.com", "OrderDate" : { "$date" : "2020-12-26T08:55:46Z" }, "Value" : 429.64999999999998, "ProductName" : "Asus Laptop", "ProductCategory" : "ELECTRONICS" }
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `ProductId` field present in
each original document.
