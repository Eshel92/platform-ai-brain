<!-- Part 6 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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

```php
$products = $client->agg_tutorials_db->products;
$orders = $client->agg_tutorials_db->orders;

$products->deleteMany([]);
$orders->deleteMany([]);

$products->insertMany(
    [
        [
            'name' => "Asus Laptop",
            'variation' => "Ultra HD",
            'category' => "ELECTRONICS",
            'description' => "Great for watching movies"
        ],
        [
            'name' => "Asus Laptop",
            'variation' => "Standard Display",
            'category' => "ELECTRONICS",
            'description' => "Good value laptop for students"
        ],
        [
            'name' => "The Day Of The Triffids",
            'variation' => "1st Edition",
            'category' => "BOOKS",
            'description' => "Classic post-apocalyptic novel"
        ],
        [
            'name' => "The Day Of The Triffids",
            'variation' => "2nd Edition",
            'category' => "BOOKS",
            'description' => "Classic post-apocalyptic novel"
        ],
        [
            'name' => "Morphy Richards Food Mixer",
            'variation' => "Deluxe",
            'category' => "KITCHENWARE",
            'description' => "Luxury mixer turning good cakes into great"
        ]
    ]
);

$orders->insertMany(
    [
        [
            'customer_id' => "elise_smith@myemail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-05-30T08:35:52"))),
            'product_name' => "Asus Laptop",
            'product_variation' => "Standard Display",
            'value' => 431.43
        ],
        [
            'customer_id' => "tj@wheresmyemail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2019-05-28T19:13:32"))),
            'product_name' => "The Day Of The Triffids",
            'product_variation' => "2nd Edition",
            'value' => 5.01
        ],
        [
            'customer_id' => "oranieri@warmmail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-01-01T08:25:37"))),
            'product_name' => "Morphy Richards Food Mixer",
            'product_variation' => "Deluxe",
            'value' => 63.13
        ],
        [
            'customer_id' => "jjones@tepidmail.com",
            'orderdate' => new UTCDateTime((new DateTimeImmutable("2020-12-26T08:55:46"))),
            'product_name' => "Asus Laptop",
            'product_variation' => "Standard Display",
            'value' => 429.65
        ]
    ]
);
```

**Step 1: Add a lookup stage to link the collections and import fields.**

The first stage of the pipeline is a `$lookup` stage to join the
`orders` collection to the `products` collection by two
fields in each collection. The lookup stage contains an
embedded pipeline to configure the join. First, create the
embedded pipeline:

```php
$embeddedPipeline = new Pipeline(
    // Add stages within embedded pipeline.
};
```

Within the embedded pipeline, add a `$match` stage to match the
values of two fields on each side of the join. Note that the following
code uses aliases for the `name` and `variation` fields
set when creating the $lookup stage:

```php
Stage::match(
    Query::expr(
        Expression::and(
            Expression::eq(
                Expression::stringFieldPath('product_name'),
                Expression::variable('prdname')
            ),
            Expression::eq(
                Expression::stringFieldPath('product_variation'),
                Expression::variable('prdvartn')
            ),
        )
    )
),
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```php
Stage::unset('_id', 'product_name', 'product_variation')
```

Next, outside of your `Pipeline` instances, create the
`$lookup` stage in a factory function. Configure this stage to
store the processed lookup fields in an array field called `orders`:

```php
function lookupOrdersStage(Pipeline $embeddedPipeline)
{
    return Stage::lookup(
        from: 'orders',
        let: object(
            prdname: Expression::stringFieldPath('name'),
            prdvartn: Expression::stringFieldPath('variation'),
        ),
        pipeline: $embeddedPipeline,
        as: 'orders',
    );
}
```

Then, in your main `Pipeline` instance, call the
`lookupOrdersStage()` function:

```php
lookupOrdersStage($embeddedPipeline),
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```php
Stage::match(
    orders: Query::ne([])
),
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```php
Stage::unset('_id', 'description')
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```php
$cursor = $products->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{
    "name": "Asus Laptop",
    "variation": "Standard Display",
    "category": "ELECTRONICS",
    "orders": [
        {
            "customer_id": "elise_smith@myemail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1590827752000"
                }
            },
            "value": 431.43
        },
        {
            "customer_id": "jjones@tepidmail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1608972946000"
                }
            },
            "value": 429.65
        }
    ]
}
{
    "name": "Morphy Richards Food Mixer",
    "variation": "Deluxe",
    "category": "KITCHENWARE",
    "orders": [
        {
            "customer_id": "oranieri@warmmail.com",
            "orderdate": {
                "$date": {
                    "$numberLong": "1577867137000"
                }
            },
            "value": 63.13
        }
    ]
}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**ruby:**


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

```ruby
products = agg_db[:products]
orders = agg_db[:orders]

products.delete_many({})
orders.delete_many({})

products.insert_many(
  [
    {
      name: "Asus Laptop",
      variation: "Ultra HD",
      category: "ELECTRONICS",
      description: "Great for watching movies",
    },
    {
      name: "Asus Laptop",
      variation: "Standard Display",
      category: "ELECTRONICS",
      description: "Good value laptop for students",
    },
    {
      name: "The Day Of The Triffids",
      variation: "1st Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      name: "The Day Of The Triffids",
      variation: "2nd Edition",
      category: "BOOKS",
      description: "Classic post-apocalyptic novel",
    },
    {
      name: "Morphy Richards Food Mixer",
      variation: "Deluxe",
      category: "KITCHENWARE",
      description: "Luxury mixer turning good cakes into great",
    },
  ]
)

orders.insert_many(
  [
    {
      customer_id: "elise_smith@myemail.com",
      orderdate: DateTime.parse("2020-05-30T08:35:52Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 431.43,
    },
    {
      customer_id: "tj@wheresmyemail.com",
      orderdate: DateTime.parse("2019-05-28T19:13:32Z"),
      product_name: "The Day Of The Triffids",
      product_variation: "2nd Edition",
      value: 5.01,
    },
    {
      customer_id: "oranieri@warmmail.com",
      orderdate: DateTime.parse("2020-01-01T08:25:37Z"),
      product_name: "Morphy Richards Food Mixer",
      product_variation: "Deluxe",
      value: 63.13,
    },
    {
      customer_id: "jjones@tepidmail.com",
      orderdate: DateTime.parse("2020-12-26T08:55:46Z"),
      product_name: "Asus Laptop",
      product_variation: "Standard Display",
      value: 429.65,
    },
  ]
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

```ruby
{
  "$match": {
    "$expr": {
      "$and": [
        { "$eq": ["$product_name", "$$prdname"] },
        { "$eq": ["$product_variation", "$$prdvartn"] },
      ],
    },
  },
},
```

Within the embedded pipeline, add another `$match` stage to match
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

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```ruby
{
  "$unset": ["_id", "product_name", "product_variation"],
},
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```ruby
{
  "$lookup": {
    from: "orders",
    let: {
      prdname: "$name",
      prdvartn: "$variation",
    },
    pipeline: embedded_pipeline,
    as: "orders",
  },
},
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```ruby
{
  "$match": {
    orders: { "$ne": [] },
  },
},
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```ruby
{
  "$unset": ["_id", "description"],
},
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```ruby
aggregation_result = products.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
ruby agg_tutorial.rb
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name"=>"Asus Laptop", "variation"=>"Standard Display", "category"=>"ELECTRONICS", "orders"=>[{"customer_id"=>"elise_smith@myemail.com", "orderdate"=>2020-05-30 08:35:52 UTC, "value"=>431.43}, {"customer_id"=>"jjones@tepidmail.com", "orderdate"=>2020-12-26 08:55:46 UTC, "value"=>429.65}]}
{"name"=>"Morphy Richards Food Mixer", "variation"=>"Deluxe", "category"=>"KITCHENWARE", "orders"=>[{"customer_id"=>"oranieri@warmmail.com", "orderdate"=>2020-01-01 08:25:37 UTC, "value"=>63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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
