<!-- Part 5 of 13 of tutorial/aggregation-examples/group-and-total.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing individual product orders. Because each order corresponds to
only one customer, the aggregation groups order documents by the `customer_id`
field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```javascript
const orders = aggDB.collection("orders");
await orders.deleteMany({});

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    value: 231,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-01-13T09:32:07Z"),
    value: 99,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    value: 63,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    value: 2,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2020-11-23T22:56:53Z"),
    value: 187,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2020-08-18T23:04:48Z"),
    value: 4,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    value: 4,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2021-02-29T07:49:32Z"),
    value: 1024,
  },
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-10-03T13:49:44Z"),
    value: 102,
  },
]);
```

**Step 1: Add a match stage for orders in 2020.**

First, add a `$match` stage that matches
orders placed in 2020:

```javascript
pipeline.push({
  $match: {
    orderdate: {
      $gte: new Date("2020-01-01T00:00:00Z"),
      $lt: new Date("2021-01-01T00:00:00Z"),
    },
  },
});
```

**Step 2: Add a sort stage to sort by order date.**

Next, add a `$sort` stage to set an
ascending sort on the `orderdate` field to retrieve the earliest
2020 purchase for each customer in the next stage:

```javascript
pipeline.push({
  $sort: {
    orderdate: 1,
  },
});
```

**Step 3: Add a group stage to group by email address.**

Add a `$group` stage to group
orders by the value of the `customer_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `first_purchase_date`: the date of the customer's first purchase
- `total_value`: the total value of all the customer's purchases
- `total_orders`: the total number of the customer's purchases
- `orders`: the list of all the customer's purchases,
  including the date and value of each purchase

```javascript
pipeline.push({
  $group: {
    _id: "$customer_id",
    first_purchase_date: { $first: "$orderdate" },
    total_value: { $sum: "$value" },
    total_orders: { $sum: 1 },
    orders: {
      $push: {
        orderdate: "$orderdate",
        value: "$value",
      },
    },
  },
});
```

**Step 4: Add a sort stage to sort by first order date.**

Next, add another `$sort` stage to set an
ascending sort on the `first_purchase_date` field:

```javascript
pipeline.push({
  $sort: {
    first_purchase_date: 1,
  },
});
```

**Step 5: Add a set stage to display the email address.**

Add a `$set` stage to recreate the
`customer_id` field from the values in the `_id` field
that were set during the `$group` stage:

```javascript
pipeline.push({
  $set: {
    customer_id: "$_id",
  },
});
```

**Step 6: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```javascript
pipeline.push({ $unset: ["_id"] });
```

**Step 7: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```javascript
const aggregationResult = await orders.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 8: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  first_purchase_date: 2020-01-01T08:25:37.000Z,
  total_value: 63,
  total_orders: 1,
  orders: [ { orderdate: 2020-01-01T08:25:37.000Z, value: 63 } ],
  customer_id: 'oranieri@warmmail.com'
}
{
  first_purchase_date: 2020-01-13T09:32:07.000Z,
  total_value: 436,
  total_orders: 4,
  orders: [
    { orderdate: 2020-01-13T09:32:07.000Z, value: 99 },
    { orderdate: 2020-05-30T08:35:52.000Z, value: 231 },
    { orderdate: 2020-10-03T13:49:44.000Z, value: 102 },
    { orderdate: 2020-12-26T08:55:46.000Z, value: 4 }
  ],
  customer_id: 'elise_smith@myemail.com'
}
{
  first_purchase_date: 2020-08-18T23:04:48.000Z,
  total_value: 191,
  total_orders: 2,
  orders: [
    { orderdate: 2020-08-18T23:04:48.000Z, value: 4 },
    { orderdate: 2020-11-23T22:56:53.000Z, value: 187 }
  ],
  customer_id: 'tj@wheresmyemail.com'
}
```

The result documents contain details from all the orders from
a given customer, grouped by the customer's email address.

**php:**


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new PHP app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the PHP library and connect to MongoDB,
see the [Get Started with the PHP Library](https://www.mongodb.com/docs/php-library/current/get-started/)
tutorial.

To learn more about performing aggregations in the PHP library, see the
[Aggregation guide](https://www.mongodb.com/docs/php-library/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.php`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```php
<?php

require 'vendor/autoload.php';

// Modify imports for each tutorial as needed.
use MongoDB\Client;
use MongoDB\BSON\UTCDateTime;
use MongoDB\Builder\Pipeline;
use MongoDB\Builder\Stage;
use MongoDB\Builder\Type\Sort;
use MongoDB\Builder\Query;
use MongoDB\Builder\Expression;
use MongoDB\Builder\Accumulator;

use function MongoDB\object;

// Replace the placeholder with your connection string.
$uri = '<connection string>';
$client = new Client($uri);

// Get a reference to relevant collections.
// ... $someColl = $client->agg_tutorials_db->someColl;
// ... $anotherColl = $client->agg_tutorials_db->anotherColl;

// Delete any existing documents in collections if needed.
// ... $someColl->deleteMany([]);

// Insert sample data into the collection or collections.
// ... $someColl->insertMany(...);

// Add code to create pipeline stages within the Pipeline instance.
// ... $pipeline = new Pipeline(...);

// Run the aggregation.
// ... $cursor = $someColl->aggregate($pipeline);

// Print the aggregation results.
foreach ($cursor as $doc) {
    echo json_encode($doc, JSON_PRETTY_PRINT), PHP_EOL;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```php
$uri = 'mongodb+srv://mongodb-example:27017';
```


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
