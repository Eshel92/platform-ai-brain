<!-- Part 6 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```ruby
orders = agg_db[:orders]
orders.delete_many({})

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      value: 231,

    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-01-13T09:32:07Z"),
      value: 99,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      value: 63,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      value: 2,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2020-11-23T22:56:53Z"),
      value: 187,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2020-08-18T23:04:48Z"),
      value: 4,
    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      value: 4,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2021-02-28T07:49:32Z"),
      value: 1024,
    },
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-10-03T13:49:44Z"),
      value: 102,
    },
  ]
)
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```ruby
{
  "$match": {
    orderdate: {
      "$gte": DateTime.parse("2020-01-01T00:00:00Z"),
      "$lt": DateTime.parse("2021-01-01T00:00:00Z"),
    },
  },
},
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```ruby
{
  "$sort": {
    orderdate: 1,
  },
},
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

```ruby
{
  "$group": {
    _id: "$customer_id",
    first_purchase_date: { "$first": "$orderdate" },
    total_value: { "$sum": "$value" },
    total_orders: { "$sum": 1 },
    orders: { "$push": {
      orderdate: "$orderdate",
      value: "$value",
    } },
  },
},
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```ruby
{
  "$sort": {
    first_purchase_date: 1,
  },
},
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```ruby
{
  "$set": {
    customer_id: "$_id",
  },
},
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```ruby
{ "$unset": ["_id"] },
```

**Step 7: Run the aggregation pipeline.**

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

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date"=>2020-01-01 08:25:37 UTC, "total_value"=>63, "total_orders"=>1, "orders"=>[{"orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63}], "customer_id"=>"oranieri@warmmail.com"}
{"first_purchase_date"=>2020-01-13 09:32:07 UTC, "total_value"=>436, "total_orders"=>4, "orders"=>[{"orderdate"=>2020-01-13 09:32:07 UTC, "value"=>99}, {"orderdate"=>2020-05-30 08:35:52 UTC, "value"=>231}, {"orderdate"=>2020-10-03 13:49:44 UTC, "value"=>102}, {"orderdate"=>2020-12-26 08:55:46 UTC, "value"=>4}], "customer_id"=>"elise_smith@myemail.com"}
{"first_purchase_date"=>2020-08-18 23:04:48 UTC, "total_value"=>191, "total_orders"=>2, "orders"=>[{"orderdate"=>2020-08-18 23:04:48 UTC, "value"=>4}, {"orderdate"=>2020-11-23 22:56:53 UTC, "value"=>187}], "customer_id"=>"tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**go:**


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
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

First, create a Go struct to model the data in the `orders`
collection:

```go
type Order struct {
	CustomerID string        `bson:"customer_id,omitempty"`
	OrderDate  bson.DateTime `bson:"orderdate"`
	Value      int           `bson:"value"`
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```go
orders := aggDB.Collection("orders")
orders.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 53, 0, time.UTC)),
		Value:      231,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 1, 13, 9, 32, 7, 0, time.UTC)),
		Value:      99,
	},
	Order{
		CustomerID: "oranieri@warmmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 1, 01, 8, 25, 37, 0, time.UTC)),
		Value:      63,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		Value:      2,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 11, 23, 22, 56, 53, 0, time.UTC)),
		Value:      187,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 8, 18, 23, 4, 48, 0, time.UTC)),
		Value:      4,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		Value:      4,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2021, 2, 29, 7, 49, 32, 0, time.UTC)),
		Value:      1024,
	},
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 10, 3, 13, 49, 44, 0, time.UTC)),
		Value:      102,
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "orderdate", Value: bson.D{
		{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
		{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
	}},
}}}
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```go
sortStage1 := bson.D{{Key: "$sort", Value: bson.D{
	{Key: "orderdate", Value: 1},
}}}
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

```go
groupStage := bson.D{{Key: "$group", Value: bson.D{
	{Key: "_id", Value: "$customer_id"},
	{Key: "first_purchase_date", Value: bson.D{{Key: "$first", Value: "$orderdate"}}},
	{Key: "total_value", Value: bson.D{{Key: "$sum", Value: "$value"}}},
	{Key: "total_orders", Value: bson.D{{Key: "$sum", Value: 1}}},
	{Key: "orders", Value: bson.D{{Key: "$push", Value: bson.D{
		{Key: "orderdate", Value: "$orderdate"},
		{Key: "value", Value: "$value"},
	}}}},
}}}
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```go
sortStage2 := bson.D{{Key: "$sort", Value: bson.D{
	{Key: "first_purchase_date", Value: 1},
}}}
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```go
setStage := bson.D{{Key: "$set", Value: bson.D{
	{Key: "customer_id", Value: "$_id"},
}}}
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id"}}}
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{matchStage, sortStage1, groupStage, setStage, sortStage2, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{"first_purchase_date":{"$date":"2020-01-01T08:25:37Z"},"total_value":63,"total_orders":1,"orders":[{"orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63}],"customer_id":"oranieri@warmmail.com"}
{"first_purchase_date":{"$date":"2020-01-13T09:32:07Z"},"total_value":436,"total_orders":4,"orders":[{"orderdate":{"$date":"2020-01-13T09:32:07Z"},"value":99},{"orderdate":{"$date":"2020-05-30T08:35:53Z"},"value":231},{"orderdate":{"$date":"2020-10-03T13:49:44Z"},"value":102},{"orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":4}],"customer_id":"elise_smith@myemail.com"}
{"first_purchase_date":{"$date":"2020-08-18T23:04:48Z"},"total_value":191,"total_orders":2,"orders":[{"orderdate":{"$date":"2020-08-18T23:04:48Z"},"value":4},{"orderdate":{"$date":"2020-11-23T22:56:53Z"},"value":187}],"customer_id":"tj@wheresmyemail.com"}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**rust:**


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
