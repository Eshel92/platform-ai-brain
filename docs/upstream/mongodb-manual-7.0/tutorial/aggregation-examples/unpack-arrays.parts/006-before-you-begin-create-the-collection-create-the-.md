<!-- Part 6 of 11 of tutorial/aggregation-examples/unpack-arrays.md (split because the page is big). -->

### Create the Collection

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

First, create Rust structs to model the data in the `orders`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Product {
    prod_id: String,
    name: String,
    price: i32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Order {
    order_id: i64,
    products: Vec<Product>,
}
```

To create the `orders` collection and insert the sample data, add the
following code to your application:

```rust
let orders_coll: Collection<Order> = agg_db.collection("orders");
orders.delete_many(doc! {}).await?;

let orders = vec![
    Order {
        order_id: 6363763262239,
        products: vec![
            Product {
                prod_id: "abc12345".to_string(),
                name: "Asus Laptop".to_string(),
                price: 431,
            },
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 22,
            },
        ],
    },
    Order {
        order_id: 1197372932325,
        products: vec![Product {
            prod_id: "abc12345".to_string(),
            name: "Asus Laptop".to_string(),
            price: 429,
        }],
    },
    Order {
        order_id: 9812343774839,
        products: vec![
            Product {
                prod_id: "pqr88223".to_string(),
                name: "Morphy Richards Food Mixer".to_string(),
                price: 431,
            },
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 21,
            },
        ],
    },
    Order {
        order_id: 4433997244387,
        products: vec![
            Product {
                prod_id: "def45678".to_string(),
                name: "Karcher Hose Set".to_string(),
                price: 23,
            },
            Product {
                prod_id: "jkl77336".to_string(),
                name: "Picky Pencil Sharpene".to_string(),
                price: 1,
            },
            Product {
                prod_id: "xyz11228".to_string(),
                name: "Russell Hobbs Chrome Kettle".to_string(),
                price: 16,
            },
        ],
    },
];

orders_coll.insert_many(orders).await?;
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```rust
pipeline.push(doc! {
    "$unwind": {
        "path": "$products"
    }
});
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```rust
pipeline.push(doc! {
    "$match": {
        "products.price": { "$gt": 15 }
    }
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

```rust
pipeline.push(doc! {
    "$group": {
        "_id": "$products.prod_id",
        "product": { "$first": "$products.name" },
        "total_value": { "$sum": "$products.price" },
        "quantity": { "$sum": 1 }
    }
});
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`prod_id` field from the values in the `_id` field
that were set during the `$group` stage:

```rust
pipeline.push(doc! {
    "$set": {
        "prod_id": "$_id"
    }
});
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```rust
pipeline.push(doc! {
    "$unset": ["_id"]
});
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```rust
let mut cursor = orders_coll.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
Document({"product": String("Russell Hobbs Chrome Kettle"), "total_value": Int32(16), "quantity": Int32(1),
"prod_id": String("xyz11228")})

Document({"product": String("Morphy Richards Food Mixer"), "total_value": Int32(431), "quantity": Int32(1),
"prod_id": String("pqr88223")})

Document({"product": String("Karcher Hose Set"), "total_value": Int32(66), "quantity": Int32(3),
"prod_id": String("def45678")})

Document({"product": String("Asus Laptop"), "total_value": Int32(860), "quantity": Int32(2),
"prod_id": String("abc12345")})
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.


## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to unpack array fields into separate documents and compute new
values based on groups of common values.

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection, use the
`insertMany()` method:

```javascript
db.orders.deleteMany({})

db.orders.insertMany( [
   {
      order_id: 6363763262239,
      products: [
         {
            prod_id: "abc12345",
            name: "Asus Laptop",
            price: 431
         },
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 22
         }
      ]
   },
   {
      order_id: 1197372932325,
      products: [
         {
            prod_id: "abc12345",
            name: "Asus Laptop",
            price: 429
         }
      ]
   },
   {
      order_id: 9812343774839,
      products: [
         {
            prod_id: "pqr88223",
            name: "Morphy Richards Food Mixer",
            price: 431
         },
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 21
         }
      ]
   },
   {
      order_id: 4433997244387,
      products: [
         {
            prod_id: "def45678",
            name: "Karcher Hose Set",
            price: 23
         },
         {
            prod_id: "jkl77336",
            name: "Picky Pencil Sharpener",
            price: 1
         },
         {
            prod_id: "xyz11228",
            name: "Russell Hobbs Chrome Kettle",
            price: 16
         }
      ]
   }
] )
```

**Step 1: Run the aggregation pipeline.**

```javascript
db.orders.aggregate( [ 

   // Stage 1: Unwind the array of product orders
   { $unwind: { path: "$products" } },

   // Stage 2: Match products that cost more than $15
   { $match: { "products.price": { $gt: 15 } } },

   // Stage 3: Group products by product type
   { $group:
      {
         _id: "$products.prod_id",
         product: { $first: "$products.name"  },
         total_value: { $sum: "$products.price" },
         quantity: { $sum: 1 }
      }
   },

   // Stage 4: Display the product ID
   { $set: { product_id: "$_id" } },

   // Stage 5: Remove unneeded fields
   { $unset: [ "_id"] }
] )
```

**Step 2: Interpret the aggregation results.**

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

**Note:**

If you run this example, the order of documents in your results
might differ from the order of documents on this page because the
aggregation pipeline does not contain a sort stage. 


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Python app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install PyMongo and connect to MongoDB,
see the [Get Started with PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
tutorial.

To learn more about performing aggregations in PyMongo, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.py`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```python
# Modify imports for each tutorial as needed.
from pymongo import MongoClient

# Replace the placeholder with your connection string.
uri = "<connection string>"
client = MongoClient(uri)

try:
    agg_db = client["agg_tutorials_db"]

    # Get a reference to relevant collections.
    # ... some_coll = agg_db["some_coll"]
    # ... another_coll = agg_db["another_coll"]

    # Delete any existing documents in collections if needed.
    # ... some_coll.delete_many({})

    # Insert sample data into the collection or collections.
    # ... some_coll.insert_many(...)

    # Create an empty pipeline array.
    pipeline = []

    # Add code to create pipeline stages.
    # ... pipeline.append({...})

    # Run the aggregation.
    # ... aggregation_result = ...

    # Print the aggregation results.
    for document in aggregation_result:
        print(document)

finally:
    client.close()
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
uri = "mongodb+srv://mongodb-example:27017"
```


### Create the Collection

This example uses an `orders` collection, which contains documents
describing product orders. Because each order contains multiple products,
the first step of the aggregation unpacks the products array into
individual product order documents.

To create the `orders` collection and insert the sample data, add the
following code to your application:

```python
orders_coll = agg_db["orders"]
orders_coll.delete_many({})

order_data = [
    {
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22,
            },
        ],
    },
    {
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429,
            }
        ],
    },
    {
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21,
            },
        ],
    },
    {
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23,
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1,
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16,
            },
        ],
    },
]

orders_coll.insert_many(order_data)
```

**Step 1: Add an unwind stage to unpack the array of product orders.**

First, add an `$unwind` stage to separate the
entries in the `products` array into individual documents:

```python
pipeline.append({"$unwind": {"path": "$products"}})
```

**Step 2: Add a match stage for products that cost more than $15.**

Next, add a `$match` stage that matches
products with a `products.price` value greater than `15`:

```python
pipeline.append({"$match": {"products.price": {"$gt": 15}}})
```

**Step 3: Add a group stage to group by product type.**

Add a `$group` stage to collect
order documents by the value of the `prod_id` field. In this
stage, add aggregation operations that create the
following fields in the result documents:

- `product`: the product name
- `total_value`: the total value of all the sales of the product
- `quantity`: the number of orders for the product

```python
pipeline.append(
    {
        "$group": {
            "_id": "$products.prod_id",
            "product": {"$first": "$products.name"},
            "total_value": {"$sum": "$products.price"},
            "quantity": {"$sum": 1},
        }
    }
)
```

**Step 4: Add a set stage to display the product ID.**

Add a `$set` stage to recreate the
`product_id` field from the values in the `_id` field
that were set during the `$group` stage:

```python
pipeline.append({"$set": {"product_id": "$_id"}})
```

**Step 5: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` field from the result
documents:

```python
pipeline.append({"$unset": ["_id"]})
```

**Step 6: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```python
aggregation_result = orders_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 7: Interpret the aggregation results.**

The aggregation returns the following summary of customers' orders
from 2020:

```none
{'product': 'Morphy Richards Food Mixer', 'total_value': 431, 'quantity': 1, 'product_id': 'pqr88223'}
{'product': 'Asus Laptop', 'total_value': 860, 'quantity': 2, 'product_id': 'abc12345'}
{'product': 'Russell Hobbs Chrome Kettle', 'total_value': 16, 'quantity': 1, 'product_id': 'xyz11228'}
{'product': 'Karcher Hose Set', 'total_value': 66, 'quantity': 3, 'product_id': 'def45678'}
```

The result documents contain details about the total value and
quantity of orders for products that cost more than $15.


### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new Java app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Get Started with the Java Driver guide`.

To learn more about performing aggregations in the Java Sync Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`AggTutorial.java`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```java
package org.example;

// Modify imports for each tutorial as needed.
import com.mongodb.client.*;
import com.mongodb.client.model.Aggregates;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Sorts;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AggTutorial {
    public static void main( String[] args ) {

        // Replace the placeholder with your connection string.
        String uri = "<connection string>";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            MongoDatabase aggDB = mongoClient.getDatabase("agg_tutorials_db");

            // Get a reference to relevant collections.
            // ... MongoCollection<Document> someColl = ...
            // ... MongoCollection<Document> anotherColl = ...

            // Delete any existing documents in collections if needed.
            // ... someColl.deleteMany(Filters.empty());

            // Insert sample data into the collection or collections.   
            // ... someColl.insertMany(...);

            // Create an empty pipeline array.
            List<Bson> pipeline = new ArrayList<>();

            // Add code to create pipeline stages.
            // ... pipeline.add(...);

            // Run the aggregation.
            // ... AggregateIterable<Document> aggregationResult = someColl.aggregate(pipeline);

            // Print the aggregation results.
            for (Document document : aggregationResult) {
                System.out.println(document.toJson());
            }
        }
    }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Java Sync Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```java
String uri = "mongodb+srv://mongodb-example:27017";
```
