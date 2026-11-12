<!-- Part 12 of 13 of tutorial/aggregation-examples/one-to-one-join.md (split because the page is big). -->

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

```php
$orders = $client->agg_tutorials_db->orders;
$products = $client->agg_tutorials_db->products;

$orders->deleteMany([]);
$products->deleteMany([]);

$orders->insertMany(
    [
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-05-30T08:35:52')),
            'product_id' => 'a1b2c3d4',
            'value' => 431.43
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2019-05-28T19:13:32')),
            'product_id' => 'z9y8x7w6',
            'value' => 5.01
        ],
        [
            'customer_id' => 'oranieri@warmmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-01T08:25:37')),
            'product_id' => 'ff11gg22hh33',
            'value' => 63.13,
        ],
        [
            'customer_id' => 'jjones@tepidmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-12-26T08:55:46')),
            'product_id' => 'a1b2c3d4',
            'value' => 429.65
        ],
    ]
);

$products->insertMany(
    [
        [
            'id' => 'a1b2c3d4',
            'name' => 'Asus Laptop',
            'category' => 'ELECTRONICS',
            'description' => 'Good value laptop for students',
        ],
        [
            'id' => 'z9y8x7w6',
            'name' => 'The Day Of The Triffids',
            'category' => 'BOOKS',
            'description' => 'Classic post-apocalyptic novel',
        ],
        [
            'id' => 'ff11gg22hh33',
            'name' => 'Morphy Richardds Food Mixer',
            'category' => 'KITCHENWARE',
            'description' => 'Luxury mixer turning good cakes into great',
        ],
        [
            'id' => 'pqr678st',
            'name' => 'Karcher Hose Set',
            'category' => 'GARDEN',
            'description' => 'Hose + nosels + winder for tidy storage',
        ],
    ]
);
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

**Step 2: Add a lookup stage to link the collections.**

Outside of your `Pipeline` instance, create a `$lookup` stage in a factory
function. The`$lookup` stage joins the `product_id` field in
the `orders` collection to the `id` field in the `products`
collection:

```php
function lookupProductsStage()
{
    return Stage::lookup(
        from: 'products',
        localField: 'product_id',
        foreignField: 'id',
        as: 'product_mapping',
    );
}
```

Then, in your `Pipeline` instance, call the
`lookupProductsStage()` function:

```php
function lookupProductsStage()
{
    return Stage::lookup(
        from: 'products',
        localField: 'product_id',
        foreignField: 'id',
        as: 'product_mapping',
    );
}
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

```php
Stage::set(
    product_mapping: Expression::first(
        Expression::arrayFieldPath('product_mapping')
    )
),
Stage::set(
    product_name: Expression::stringFieldPath('product_mapping.name'),
    product_category: Expression::stringFieldPath('product_mapping.category')
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

```php
Stage::unset('_id', 'product_id', 'product_mapping')
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```php
$cursor = $orders->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{
    "customer_id": "elise_smith@myemail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1590827752000"
        }
    },
    "value": 431.43,
    "product_name": "Asus Laptop",
    "product_category": "ELECTRONICS"
}
{
    "customer_id": "oranieri@warmmail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1577867137000"
        }
    },
    "value": 63.13,
    "product_name": "Morphy Richardds Food Mixer",
    "product_category": "KITCHENWARE"
}
{
    "customer_id": "jjones@tepidmail.com",
    "orderdate": {
        "$date": {
            "$numberLong": "1608972946000"
        }
    },
    "value": 429.65,
    "product_name": "Asus Laptop",
    "product_category": "ELECTRONICS"
}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.


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

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```ruby
orders = agg_db[:orders]
products = agg_db[:products]

orders.delete_many({})
products.delete_many({})

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      product_id: "a1b2c3d4",
      value: 431.43,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      product_id: "z9y8x7w6",
      value: 5.01,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      product_id: "ff11gg22hh33",
      value: 63.13,
    },
    {
      customer_id: "jjones@tepidmail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      product_id: "a1b2c3d4",
      value: 429.65,
    },
  ]
)

products.insert_many(
  [
    {
      id: "a1b2c3d4",
      name: "Asus Laptop",
      category: "ELECTRONICS",
      description: "Good value laptop for students",
    },
    {
      id: "z9y8x7w6",
      name: "The Day Of The Triffids",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      id: "ff11gg22hh33",
      name: "Morphy Richardds Food Mixer",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great",
    },
    {
      id: "pqr678st",
      name: "Karcher Hose Set",
      category: "GARDEN",
      description: "Hose + nosels + winder for tidy storage",
    },
  ]
)
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
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

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```ruby
{
  "$lookup": {
    from: "products",
    localField: "product_id",
    foreignField: "id",
    as: "product_mapping",
  },
},
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

```ruby
{
  "$set": {
    product_mapping: { "$first": "$product_mapping" },
  },
},
{
  "$set": {
    product_name: "$product_mapping.name",
    product_category: "$product_mapping.category",
  },
},
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```ruby
{ "$unset": ["_id", "product_id", "product_mapping"] },
```

**Step 5: Run the aggregation pipeline.**

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

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id"=>"elise_smith@myemail.com", "orderdate"=>2020-05-30 08:35:52 UTC, "value"=>431.43, "product_name"=>"Asus Laptop", "product_category"=>"ELECTRONICS"}
{"customer_id"=>"oranieri@warmmail.com", "orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63.13, "product_name"=>"Morphy Richardds Food Mixer", "product_category"=>"KITCHENWARE"}
{"customer_id"=>"jjones@tepidmail.com", "orderdate"=>2020-12-26 08:55:46 UTC, "value"=>429.65, "product_name"=>"Asus Laptop", "product_category"=>"ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.


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
