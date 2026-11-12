<!-- Part 4 of 11 of tutorial/aggregation-examples/unpack-arrays.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```cpp
auto orders = db["orders"];

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21
            }
        ]
    })"),
    bsoncxx::from_json(R"({
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16
            }
        ]
    })")
};
orders.insert_many(order_docs); // Might throw an exception
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```cpp
pipeline.unwind("$products");
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "products.price": { "$gt": 15 }
})"));
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```cpp
pipeline.group(bsoncxx::from_json(R"({
    "_id": "$products.prod_id",
    "product": { "$first": "$products.name" },
    "total_value": { "$sum": "$products.price" },
    "quantity": { "$sum": 1 }
})"));
```

**Step 4: Add an addFields stage to display the product ID.**

Add an `$addFields` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```cpp
pipeline.add_fields(bsoncxx::from_json(R"({
    "product_id": "$_id"
})"));
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id"]
})"));
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```cpp
auto cursor = orders.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{ "product" : "Karcher Hose Set", "total_value" : 66, "quantity" : 3, "product_id" : "def45678" }
{ "product" : "Asus Laptop", "total_value" : 860, "quantity" : 2, "product_id" : "abc12345" }
{ "product" : "Morphy Richards Food Mixer", "total_value" : 431, "quantity" : 1, "product_id" : "pqr88223" }
{ "product" : "Russell Hobbs Chrome Kettle", "total_value" : 16, "quantity" : 1, "product_id" : "xyz11228" }
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Node.js app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Node.js Driver Quick Start guide`.

To learn more about performing aggregations in the Node.js Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.js`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```javascript
const { MongoClient } = require("mongodb");

// Replace the placeholder with your connection string.
const uri = "<connection string>";
const client = new MongoClient(uri);

async function run() {
  try {
    const aggDB = client.db("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... const someColl =
    // ... const anotherColl =

    // Delete any existing documents in collections.
    // ... await someColl.deleteMany({});

    // Insert sample data into the collection or collections.
    // ... const someData = [ ... ];
    // ... await someColl.insertMany(someData);

    // Create an empty pipeline array.
    const pipeline = [];

    // Add code to create pipeline stages.
    // ... pipeline.push({ ... })

    // Run the aggregation.
    // ... const aggregationResult = ...

    // Print the aggregation results.
    for await (const document of aggregationResult) {
      console.log(document);
    }
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Node.js Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```javascript
const uri = "mongodb+srv://mongodb-example:27017";
```


### Create the Collection

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```javascript
const orders = aggDB.collection("orders");
await orders.deleteMany({});

await orders.insertMany([
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
]);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```javascript
pipeline.push({
  $unwind: {
    path: "$products",
  },
});
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```javascript
pipeline.push({
  $match: {
    "products.price": {
      $gt: 15,
    },
  },
});
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```javascript
pipeline.push({
  $group: {
    _id: "$products.prod_id",
    product: { $first: "$products.name" },
    total_value: { $sum: "$products.price" },
    quantity: { $sum: 1 },
  },
});
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```javascript
pipeline.push({
  $set: {
    product_id: "$_id",
  },
});
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```javascript
pipeline.push({ $unset: ["_id"] });
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```javascript
{
  product: 'Asus Laptop',
  total_value: 860,
  quantity: 2,
  product_id: 'abc12345'
}
{
  product: 'Morphy Richards Food Mixer',
  total_value: 431,
  quantity: 1,
  product_id: 'pqr88223'
}
{
  product: 'Russell Hobbs Chrome Kettle',
  total_value: 16,
  quantity: 1,
  product_id: 'xyz11228'
}
{
  product: 'Karcher Hose Set',
  total_value: 66,
  quantity: 3,
  product_id: 'def45678'
}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.


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
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```php
$orders = $client->agg_tutorials_db->orders;
$orders->deleteMany([]);

$orders->insertMany(
    [
        [
            'order_id' => 6363763262239,
            'products' => [
                [
                    'prod_id' => 'abc12345',
                    'name' => 'Asus Laptop',
                    'price' => 431,
                ],
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 22,
                ],
            ],
        ],
        [
            'order_id' => 1197372932325,
            'products' => [
                [
                    'prod_id' => 'abc12345',
                    'name' => 'Asus Laptop',
                    'price' => 429,
                ],
            ],
        ],
        [
            'order_id' => 9812343774839,
            'products' => [
                [
                    'prod_id' => 'pqr88223',
                    'name' => 'Morphy Richards Food Mixer',
                    'price' => 431,
                ],
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 21,
                ],
            ],
        ],
        [
            'order_id' => 4433997244387,
            'products' => [
                [
                    'prod_id' => 'def45678',
                    'name' => 'Karcher Hose Set',
                    'price' => 23,
                ],
                [
                    'prod_id' => 'jkl77336',
                    'name' => 'Picky Pencil Sharpener',
                    'price' => 1,
                ],
                [
                    'prod_id' => 'xyz11228',
                    'name' => 'Russell Hobbs Chrome Kettle',
                    'price' => 16,
                ],
            ],
        ]
    ]
);
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```php
Stage::unwind(
    path: Expression::arrayFieldPath('products')
),
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```php
Stage::match(
    ['products.price' => Query::gt(15)]
),
```

**Step 3: Add a group stage to group by product type.**

Outside of your `Pipeline` instance, create a `$group` stage in a factory
function to collect order documents by the value of the
`prod_id` field. In this stage, add aggregation operations that
create the following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```php
function groupByProductStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('products.prod_id'),
        product: Accumulator::first(
            Expression::stringFieldPath('products.name')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('products.price'),
        ),
        quantity: Accumulator::sum(1)
    );
}
```

Then, in your `Pipeline` instance, call the
`groupByProductStage()` function:

```php
function groupByProductStage()
{
    return Stage::group(
        _id: Expression::stringFieldPath('products.prod_id'),
        product: Accumulator::first(
            Expression::stringFieldPath('products.name')
        ),
        total_value: Accumulator::sum(
            Expression::numberFieldPath('products.price'),
        ),
        quantity: Accumulator::sum(1)
    );
}
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```php
Stage::set(product_id: Expression::stringFieldPath('_id')),
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```php
Stage::unset('_id')
```

**Step 6: Run the aggregation pipeline.**

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

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{
    "product": "Russell Hobbs Chrome Kettle",
    "total_value": 16,
    "quantity": 1,
    "product_id": "xyz11228"
}
{
    "product": "Asus Laptop",
    "total_value": 860,
    "quantity": 2,
    "product_id": "abc12345"
}
{
    "product": "Karcher Hose Set",
    "total_value": 66,
    "quantity": 3,
    "product_id": "def45678"
}
{
    "product": "Morphy Richards Food Mixer",
    "total_value": 431,
    "quantity": 1,
    "product_id": "pqr88223"
}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.
