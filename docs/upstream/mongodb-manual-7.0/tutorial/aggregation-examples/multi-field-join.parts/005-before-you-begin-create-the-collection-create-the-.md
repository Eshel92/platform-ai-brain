<!-- Part 5 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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

```cpp
auto products = db["products"];
auto orders = db["orders"];

std::vector<bsoncxx::document::value> product_docs = {
    bsoncxx::from_json(R"({
        "name": "Asus Laptop",
        "variation": "Ultra HD",
        "category": "ELECTRONICS",
        "description": "Great for watching movies"
    })"),
    bsoncxx::from_json(R"({
        "name": "Asus Laptop",
        "variation": "Standard Display",
        "category": "ELECTRONICS",
        "description": "Good value laptop for students"
    })"),
    bsoncxx::from_json(R"({
        "name": "The Day Of The Triffids",
        "variation": "1st Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "name": "The Day Of The Triffids",
        "variation": "2nd Edition",
        "category": "BOOKS",
        "description": "Classic post-apocalyptic novel"
    })"),
    bsoncxx::from_json(R"({
        "name": "Morphy Richards Food Mixer",
        "variation": "Deluxe",
        "category": "KITCHENWARE",
        "description": "Luxury mixer turning good cakes into great"
    })")
};

products.insert_many(product_docs); // Might throw an exception

std::vector<bsoncxx::document::value> order_docs = {
    bsoncxx::from_json(R"({
        "customer_id": "elise_smith@myemail.com",
        "orderdate": {"$date": 1590821752000},
        "product_name": "Asus Laptop",
        "product_variation": "Standard Display",
        "value": 431.43
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "tj@wheresmyemail.com",
        "orderdate": {"$date": 1559062412000},
        "product_name": "The Day Of The Triffids",
        "product_variation": "2nd Edition",
        "value": 5.01
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "oranieri@warmmail.com",
        "orderdate": {"$date": 1577861137000},
        "product_name": "Morphy Richards Food Mixer",
        "product_variation": "Deluxe",
        "value": 63.13
    })"),
    bsoncxx::from_json(R"({
        "customer_id": "jjones@tepidmail.com",
        "orderdate": {"$date": 1608972946000},
        "product_name": "Asus Laptop",
        "product_variation": "Standard Display",
        "value": 429.65
    })")
};

orders.insert_many(order_docs); // Might throw an exception
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

```cpp
auto embed_match_stage1 = bsoncxx::from_json(R"({
    "$match": {
        "$expr": {
            "$and": [
                { "$eq": ["$product_name", "$$prdname"] },
                { "$eq": ["$product_variation", "$$prdvartn"] }
            ]
        }
    }
})");
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```cpp
auto embed_match_stage2 = bsoncxx::from_json(R"({
    "$match": {
        "orderdate": {
            "$gte": { "$date": 1577836800000 },
            "$lt": { "$date": 1609459200000 }
        }
    }
})");
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```cpp
auto embed_unset_stage = bsoncxx::from_json(R"({
    "$unset": ["_id", "product_name", "product_variation"]
})");
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```cpp
pipeline.lookup(make_document(
    kvp("from", "orders"),
    kvp("let", make_document(
        kvp("prdname", "$name"),
        kvp("prdvartn", "$variation")
    )),
    kvp("pipeline", make_array(embed_match_stage1, embed_match_stage2, embed_unset_stage)),
    kvp("as", "orders")
));
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "orders": { "$ne": [] }
})"));
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "description"]
})"));
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```cpp
auto cursor = products.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{ "name" : "Asus Laptop", "variation" : "Standard Display", "category" : "ELECTRONICS",
"orders" : [ { "customer_id" : "elise_smith@myemail.com", "orderdate" : { "$date" : "2020-05-30T06:55:52Z" },
"value" : 431.43000000000000682 }, { "customer_id" : "jjones@tepidmail.com", "orderdate" : { "$date" :
"2020-12-26T08:55:46Z" }, "value" : 429.64999999999997726 } ] }
{ "name" : "Morphy Richards Food Mixer", "variation" : "Deluxe", "category" : "KITCHENWARE",
"orders" : [ { "customer_id" : "oranieri@warmmail.com", "orderdate" : { "$date" : "2020-01-01T06:45:37Z" },
"value" : 63.130000000000002558 } ] }
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**nodejs:**


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

```javascript
const products = aggDB.collection("products");
const orders = aggDB.collection("orders");

await products.deleteMany({});
await orders.deleteMany({});

await products.insertMany([
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
]);

await orders.insertMany([
  {
    customer_id: "elise_smith@myemail.com",
    orderdate: new Date("2020-05-30T08:35:52Z"),
    product_name: "Asus Laptop",
    product_variation: "Standard Display",
    value: 431.43,
  },
  {
    customer_id: "tj@wheresmyemail.com",
    orderdate: new Date("2019-05-28T19:13:32Z"),
    product_name: "The Day Of The Triffids",
    product_variation: "2nd Edition",
    value: 5.01,
  },
  {
    customer_id: "oranieri@warmmail.com",
    orderdate: new Date("2020-01-01T08:25:37Z"),
    product_name: "Morphy Richards Food Mixer",
    product_variation: "Deluxe",
    value: 63.13,
  },
  {
    customer_id: "jjones@tepidmail.com",
    orderdate: new Date("2020-12-26T08:55:46Z"),
    product_name: "Asus Laptop",
    product_variation: "Standard Display",
    value: 429.65,
  },
]);
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

```javascript
const embedded_pl = [];

embedded_pl.push({
  $match: {
    $expr: {
      $and: [
        { $eq: ["$product_name", "$$prdname"] },
        { $eq: ["$product_variation", "$$prdvartn"] },
      ],
    },
  },
});
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```javascript
embedded_pl.push({
  $match: {
    orderdate: {
      $gte: new Date("2020-01-01T00:00:00Z"),
      $lt: new Date("2021-01-01T00:00:00Z"),
    },
  },
});
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```javascript
embedded_pl.push({
  $unset: ["_id", "product_name", "product_variation"],
});
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```javascript
pipeline.push({
  $lookup: {
    from: "orders",
    let: {
      prdname: "$name",
      prdvartn: "$variation",
    },
    pipeline: embedded_pl,
    as: "orders",
  },
});
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```javascript
pipeline.push({
  $match: {
    orders: { $ne: [] },
  },
});
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```javascript
pipeline.push({
  $unset: ["_id", "description"],
});
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```javascript
const aggregationResult = await products.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```javascript
{
  name: 'Asus Laptop',
  variation: 'Standard Display',
  category: 'ELECTRONICS',
  orders: [
    {
      customer_id: 'elise_smith@myemail.com',
      orderdate: 2020-05-30T08:35:52.000Z,
      value: 431.43
    },
    {
      customer_id: 'jjones@tepidmail.com',
      orderdate: 2020-12-26T08:55:46.000Z,
      value: 429.65
    }
  ]
}
{
  name: 'Morphy Richards Food Mixer',
  variation: 'Deluxe',
  category: 'KITCHENWARE',
  orders: [
    {
      customer_id: 'oranieri@warmmail.com',
      orderdate: 2020-01-01T08:25:37.000Z,
      value: 63.13
    }
  ]
}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**php:**


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
