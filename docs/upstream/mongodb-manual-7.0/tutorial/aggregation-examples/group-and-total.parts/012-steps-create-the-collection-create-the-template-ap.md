<!-- Part 12 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$orders->deleteMany([]);

$orders->insertMany(
    [
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-05-30T08:35:52')),
            'value' => 231
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-13T09:32:07')),
            'value' => 99
        ],
        [
            'customer_id' => 'oranieri@warmmail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-01-01T08:25:37')),
            'value' => 63
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2019-05-28T19:13:32')),
            'value' => 2
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-11-23T22:56:53')),
            'value' => 187
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-08-18T23:04:48')),
            'value' => 4
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-12-26T08:55:46')),
            'value' => 4
        ],
        [
            'customer_id' => 'tj@wheresmyemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2021-02-28T07:49:32')),
            'value' => 1024
        ],
        [
            'customer_id' => 'elise_smith@myemail.com',
            'orderdate' => new UTCDateTime(new DateTimeImmutable('2020-10-03T13:49:44')),
            'value' => 102
        ]
    ]
);
```

**Step 1: Add a match stage for orders in 2020.**

In your `Pipeline` instance, add a `$match` stage that matches
orders placed in 2020:

```php
Stage::match(
    orderdate: [
        Query::gte(new UTCDateTime(new DateTimeImmutable('2020-01-01T00:00:00'))),
        Query::lt(new UTCDateTime(new DateTimeImmutable('2021-01-01T00:00:00'))),
    ]
),
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```php
Stage::sort(orderdate: Sort::Asc),
```

**Step 3: Add a group stage to group by email address.**

Outside of your `Pipeline` instance, create a `$group` stage in a factory
function to collect order documents by the value of the
`customer_id` field. In this stage, add aggregation operations
that create the following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```php
function groupByCustomerStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('customer_id'),
        first_purchase_date: Accumulator::first(
            Expression::arrayFieldPath('orderdate')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('value'),
        ),
        total_orders: Accumulator::sum(1),
        orders: Accumulator::push(
            object(
                orderdate: Expression::dateFieldPath('orderdate'),
                value: Expression::numberFieldPath('value'),
            ),
        ),
    );
}
```

Then, in your `Pipeline` instance, call the
`groupByCustomerStage()` function:

```php
function groupByCustomerStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('customer_id'),
        first_purchase_date: Accumulator::first(
            Expression::arrayFieldPath('orderdate')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('value'),
        ),
        total_orders: Accumulator::sum(1),
        orders: Accumulator::push(
            object(
                orderdate: Expression::dateFieldPath('orderdate'),
                value: Expression::numberFieldPath('value'),
            ),
        ),
    );
}
```

**Step 4: Add a sort stage to sort by first order date.**

Next, create another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```php
Stage::sort(first_purchase_date: Sort::Asc),
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```php
Stage::set(customer_id: Expression::stringFieldPath('_id')),
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```php
Stage::unset('_id')
```

**Step 7: Run the aggregation pipeline.**

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

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1577867137000"
        }
    },
    "total_value": 63,
    "total_orders": 1,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1577867137000"
                }
            },
            "value": 63
        }
    ],
    "customer_id": "oranieri@warmmail.com"
}
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1578907927000"
        }
    },
    "total_value": 436,
    "total_orders": 4,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1578907927000"
                }
            },
            "value": 99
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1590827752000"
                }
            },
            "value": 231
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1601732984000"
                }
            },
            "value": 102
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1608972946000"
                }
            },
            "value": 4
        }
    ],
    "customer_id": "elise_smith@myemail.com"
}
{
    "first_purchase_date": {
        "$date": {
            "$numberLong": "1597791888000"
        }
    },
    "total_value": 191,
    "total_orders": 2,
    "orders": [
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1597791888000"
                }
            },
            "value": 4
        },
        {
            "orderdate": {
                "$date": {
                    "$numberLong": "1606172213000"
                }
            },
            "value": 187
        }
    ],
    "customer_id": "tj@wheresmyemail.com"
}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

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
