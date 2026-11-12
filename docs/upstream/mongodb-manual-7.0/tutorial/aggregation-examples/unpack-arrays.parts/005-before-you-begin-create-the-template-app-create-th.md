<!-- Part 5 of 11 of tutorial/aggregation-examples/unpack-arrays.md (split because the page is big). -->

### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Ruby app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the Ruby Driver and connect to MongoDB,
see the [Get Started with the Ruby Driver guide](https://www.mongodb.com/docs/ruby-driver/upcoming/get-started/).

To learn more about performing aggregations in the Ruby Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/ruby-driver/upcoming/aggregation/).

After you install the driver, create a file called
`agg_tutorial.rb`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```ruby
# typed: strict
require 'mongo'
require 'bson'

# Replace the placeholder with your connection string.
uri = "<connection string>"

Mongo::Client.new(uri) do |client|

  agg_db = client.use('agg_tutorials_db')

  # Get a reference to relevant collections.
  # ... some_coll = agg_db[:some_coll]

  # Delete any existing documents in collections if needed.
  # ... some_coll.delete_many({})

  # Insert sample data into the collection or collections.
  # ... some_coll.insert_many( ... )

  # Add code to create pipeline stages within the array.
  # ... pipeline = [ ... ]

  # Run the aggregation.
  # ... aggregation_result = some_coll.aggregate(pipeline)

  # Print the aggregation results.
  aggregation_result.each do |doc|
    puts doc
  end

end
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/ruby-driver/upcoming/get-started/create-a-connection-string/)
step of the Ruby Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```ruby
uri = "mongodb+srv://mongodb-example:27017"
```


### Create the Collection

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```ruby
orders = agg_db[:orders]
orders.delete_many({})

orders.insert_many(
  [
    {
      order_id: 6363763262239,
      products: [
        {
          prod_id: "abc12345",
          name: "Asus Laptop",
          price: 431,
        },
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 22,
        },
      ],
    },
    {
      order_id: 1197372932325,
      products: [
        {
          prod_id: "abc12345",
          name: "Asus Laptop",
          price: 429,
        },
      ],
    },
    {
      order_id: 9812343774839,
      products: [
        {
          prod_id: "pqr88223",
          name: "Morphy Richards Food Mixer",
          price: 431,
        },
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 21,
        },
      ],
    },
    {
      order_id: 4433997244387,
      products: [
        {
          prod_id: "def45678",
          name: "Karcher Hose Set",
          price: 23,
        },
        {
          prod_id: "jkl77336",
          name: "Picky Pencil Sharpener",
          price: 1,
        },
        {
          prod_id: "xyz11228",
          name: "Russell Hobbs Chrome Kettle",
          price: 16,
        },
      ],
    },
  ]
)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```ruby
{
  "$unwind": {
    path: "$products",
  },
},
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```ruby
{
  "$match": {
    "products.price": {
      "$gt": 15,
    },
  },
},
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```ruby
{
  "$group": {
    _id: "$products.prod_id",
    product: { "$first": "$products.name" },
    total_value: { "$sum": "$products.price" },
    quantity: { "$sum": 1 },
  },
},
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```ruby
{
  "$set": {
    product_id: "$_id",
  },
},
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```ruby
{ "$unset": ["_id"] },
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```ruby
aggregation_result = orders.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
ruby agg_tutorial.rb
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product"=>"Asus Laptop", "total_value"=>860, "quantity"=>2, "product_id"=>"abc12345"}
{"product"=>"Russell Hobbs Chrome Kettle", "total_value"=>16, "quantity"=>1, "product_id"=>"xyz11228"}
{"product"=>"Karcher Hose Set", "total_value"=>66, "quantity"=>3, "product_id"=>"def45678"}
{"product"=>"Morphy Richards Food Mixer", "total_value"=>431, "quantity"=>1, "product_id"=>"pqr88223"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Go app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Go Driver Quick Start guide`.

To learn more about performing aggregations in the Go Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.go`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "go.mongodb.org/mongo-driver/v2/bson"
    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

// Define structs.
// type MyStruct struct { ... }

func main() {
    // Replace the placeholder with your connection string.
    const uri = "<connection string>"

    client, err := mongo.Connect(options.Client().ApplyURI(uri))
    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err = client.Disconnect(context.TODO()); err != nil {
            log.Fatal(err)
        }
    }()

    aggDB := client.Database("agg_tutorials_db")

    // Get a reference to relevant collections.
    // ... someColl := aggDB.Collection("...")
    // ... anotherColl := aggDB.Collection("...")

    // Delete any existing documents in collections if needed.
    // ... someColl.DeleteMany(context.TODO(), bson.D{})

    // Insert sample data into the collection or collections.   
    // ... _, err = someColl.InsertMany(...)

    // Add code to create pipeline stages.
    // ... myStage := bson.D{{...}}

    // Create a pipeline that includes the stages.
    // ... pipeline := mongo.Pipeline{...}

    // Run the aggregation.
    // ... cursor, err := someColl.Aggregate(context.TODO(), pipeline)

    if err != nil {
        log.Fatal(err)
    }

    defer func() {
        if err := cursor.Close(context.TODO()); err != nil {
            log.Fatalf("failed to close cursor: %v", err)
        }
    }()

    // Decode the aggregation results.
    var results []bson.D
    if err = cursor.All(context.TODO(), &results); err != nil {
        log.Fatalf("failed to decode results: %v", err)
    }

    // Print the aggregation results.
    for _, result := range results {
        res, _ := bson.MarshalExtJSON(result, false, false)
        fmt.Println(string(res))
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a MongoDB Cluster`
step of the Go Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```go
const uri = "mongodb+srv://mongodb-example:27017";
```


### Create the Collection

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Go structs to model the data in the `orders`
collection:

```go
type Order struct {
	OrderID  int       `bson:"order_id"`
	Products []Product `bson:"products"`
}

type Product struct {
	ProductID string `bson:"prod_id"`
	Name      string `bson:"name"`
	Price     int    `bson:"price"`
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```go
orders := aggDB.Collection("orders")
orders.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		OrderID: 6363763262239,
		Products: []Product{
			{ProductID: "abc12345", Name: "Asus Laptop", Price: 431},
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 22},
		},
	},
	Order{
		OrderID: 1197372932325,
		Products: []Product{
			{ProductID: "abc12345", Name: "Asus Laptop", Price: 429},
		},
	},
	Order{
		OrderID: 9812343774839,
		Products: []Product{
			{ProductID: "pqr88223", Name: "Morphy Richards Food Mixer", Price: 431},
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 21},
		},
	},
	Order{
		OrderID: 4433997244387,
		Products: []Product{
			{ProductID: "def45678", Name: "Karcher Hose Set", Price: 23},
			{ProductID: "jkl77336", Name: "Picky Pencil Sharpene", Price: 1},
			{ProductID: "xyz11228", Name: "Russell Hobbs Chrome Kettle", Price: 16},
		},
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```go
unwindStage := bson.D{{Key: "$unwind", Value: bson.D{
	{Key: "path", Value: "$products"},
}}}
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "products.price", Value: bson.D{{Key: "$gt", Value: 15}}},
}}}
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```go
groupStage := bson.D{{Key: "$group", Value: bson.D{
	{Key: "_id", Value: "$products.prod_id"},
	{Key: "product", Value: bson.D{{Key: "$first", Value: "$products.name"}}},
	{Key: "total_value", Value: bson.D{{Key: "$sum", Value: "$products.price"}}},
	{Key: "quantity", Value: bson.D{{Key: "$sum", Value: 1}}},
}}}
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```go
setStage := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_id", Value: "$_id"},
}}}
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id"}}}
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{unwindStage, matchStage, groupStage, setStage, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"product":"Morphy Richards Food Mixer","total_value":431,"quantity":1,"product_id":"pqr88223"}
{"product":"Russell Hobbs Chrome Kettle","total_value":16,"quantity":1,"product_id":"xyz11228"}
{"product":"Karcher Hose Set","total_value":66,"quantity":3,"product_id":"def45678"}
{"product":"Asus Laptop","total_value":860,"quantity":2,"product_id":"abc12345"}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Rust app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Rust Driver Quick Start guide`.

To learn more about performing aggregations in the Rust Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg-tutorial.rs`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```rust
use mongodb::{
    bson::{doc, Document},
    options::ClientOptions,
    Client,
};
use futures::stream::TryStreamExt;
use std::error::Error;

// Define structs.
// #[derive(Debug, Serialize, Deserialize)]
// struct MyStruct { ... }

#[tokio::main]
async fn main() mongodb::error::Result<()> {
    // Replace the placeholder with your connection string.
    let uri = "<connection string>";
    let client = Client::with_uri_str(uri).await?;

    let agg_db = client.database("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... let some_coll: Collection<T> = agg_db.collection("...");
    // ... let another_coll: Collection<T> = agg_db.collection("...");

    // Delete any existing documents in collections if needed.
    // ... some_coll.delete_many(doc! {}).await?;

    // Insert sample data into the collection or collections.
    // ... some_coll.insert_many(vec![...]).await?;

    // Create an empty pipeline.
    let mut pipeline = Vec::new();

    // Add code to create pipeline stages.
    // pipeline.push(doc! { ... });

    // Run the aggregation and print the results.
    let mut results = some_coll.aggregate(pipeline).await?;
    while let Some(result) = results.try_next().await? {
       println!("{:?}\n", result);
    }
    Ok(())
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Rust Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```rust
let uri = "mongodb+srv://mongodb-example:27017";
```
