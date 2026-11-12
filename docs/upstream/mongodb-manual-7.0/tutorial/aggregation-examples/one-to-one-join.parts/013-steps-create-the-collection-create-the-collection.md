<!-- Part 13 of 13 of tutorial/aggregation-examples/one-to-one-join.md (split because the page is big). -->

### Create the Collection

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Go structs to model the data in the `orders` and `products`
collections:

```go
type Order struct {
	CustomerID string        `bson:"customer_id"`
	OrderDate  bson.DateTime `bson:"orderdate"`
	ProductID  string        `bson:"product_id"`
	Value      float32       `bson:"value"`
}

type Product struct {
	ID          string `bson:"id"`
	Name        string `bson:"name"`
	Category    string `bson:"category"`
	Description string `bson:"description"`
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```go
orders := aggDB.Collection("orders")
products := aggDB.Collection("products")
orders.DeleteMany(context.TODO(), bson.D{})
products.DeleteMany(context.TODO(), bson.D{})

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID: "elise_smith@myemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 52, 0, time.UTC)),
		ProductID:  "a1b2c3d4",
		Value:      431.43,
	},
	Order{
		CustomerID: "tj@wheresmyemail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		ProductID:  "z9y8x7w6",
		Value:      5.01,
	},
	Order{
		CustomerID: "oranieri@warmmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 01, 01, 8, 25, 37, 0, time.UTC)),
		ProductID:  "ff11gg22hh33",
		Value:      63.13,
	},
	Order{
		CustomerID: "jjones@tepidmail.com",
		OrderDate:  bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		ProductID:  "a1b2c3d4",
		Value:      429.65,
	},
})
if err != nil {
	log.Fatal(err)
}

_, err = products.InsertMany(context.TODO(), []interface{}{
	Product{
		ID:          "a1b2c3d4",
		Name:        "Asus Laptop",
		Category:    "ELECTRONICS",
		Description: "Good value laptop for students",
	},
	Product{
		ID:          "z9y8x7w6",
		Name:        "The Day Of The Triffids",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		ID:          "ff11gg22hh33",
		Name:        "Morphy Richardds Food Mixer",
		Category:    "KITCHENWARE",
		Description: "Luxury mixer turning good cakes into great",
	},
	Product{
		ID:          "pqr678st",
		Name:        "Karcher Hose Set",
		Category:    "GARDEN",
		Description: "Hose + nosels + winder for tidy storage",
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{
	{Key: "orderdate", Value: bson.D{
		{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
		{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
	}},
}}}
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```go
lookupStage := bson.D{{Key: "$lookup", Value: bson.D{
	{Key: "from", Value: "products"},
	{Key: "localField", Value: "product_id"},
	{Key: "foreignField", Value: "id"},
	{Key: "as", Value: "product_mapping"},
}}}
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

```go
setStage1 := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_mapping", Value: bson.D{{Key: "$first", Value: "$product_mapping"}}},
}}}

setStage2 := bson.D{{Key: "$set", Value: bson.D{
	{Key: "product_name", Value: "$product_mapping.name"},
	{Key: "product_category", Value: "$product_mapping.category"},
}}}
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id", "product_id", "product_mapping"}}}
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```go
pipeline := mongo.Pipeline{matchStage, lookupStage, setStage1, setStage2, unsetStage}
cursor, err := orders.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
{"customer_id":"elise_smith@myemail.com","orderdate":{"$date":"2020-05-30T08:35:52Z"},"value":431.42999267578125,"product_name":"Asus Laptop","product_category":"ELECTRONICS"}
{"customer_id":"oranieri@warmmail.com","orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63.130001068115234,"product_name":"Morphy Richardds Food Mixer","product_category":"KITCHENWARE"}
{"customer_id":"jjones@tepidmail.com","orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":429.6499938964844,"product_name":"Asus Laptop","product_category":"ELECTRONICS"}
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.


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


### Create the Collection

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells

An order can only contain one product. The aggregation uses a
one-to-one join to match an order document to the corresponding product
document. The aggregation joins the collections by the `product_id` field
that exists in documents in both collections.

First, create Rust structs to model the data in the `orders` and `products`
collections:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    order_date: DateTime,
    product_id: String,
    value: f32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Product {
    id: String,
    name: String,
    category: String,
    description: String,
}
```

To create the `orders` and `products` collections and insert the
sample data, add the following code to your application:

```rust
let orders: Collection<Order> = agg_db.collection("orders");
let products: Collection<Product> = agg_db.collection("products");

orders.delete_many(doc! {}).await?;
products.delete_many(doc! {}).await?;

let order_docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(52).build().unwrap(),
        product_id: "a1b2c3d4".to_string(),
        value: 431.43,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        order_date: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        product_id: "z9y8x7w6".to_string(),
        value: 5.01,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        product_id: "ff11gg22hh33".to_string(),
        value: 63.13,
    },
    Order {
        customer_id: "jjones@tepidmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        product_id: "a1b2c3d4".to_string(),
        value: 429.65,
    },
];
orders.insert_many(order_docs).await?;

let product_docs = vec![
    Product {
        id: "a1b2c3d4".to_string(),
        name: "Asus Laptop".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Good value laptop for students".to_string(),
    },
    Product {
        id: "z9y8x7w6".to_string(),
        name: "The Day Of The Triffids".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        id: "ff11gg22hh33".to_string(),
        name: "Morphy Richardds Food Mixer".to_string(),
        category: "KITCHENWARE".to_string(),
        description: "Luxury mixer turning good cakes into great".to_string(),
    },
    Product {
        id: "pqr678st".to_string(),
        name: "Karcher Hose Set".to_string(),
        category: "GARDEN".to_string(),
        description: "Hose + nosels + winder for tidy storage".to_string(),
    },
];
products.insert_many(product_docs).await?;
```

**Step 1: Add a match stage for orders in 2020.**

Add a `$match` stage that matches
orders placed in 2020:

```rust
pipeline.push(doc! {
    "$match": {
        "order_date": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap()
        }
    }
});
```

**Step 2: Add a lookup stage to link the collections.**

Next, add a `$lookup` stage. The
`$lookup` stage joins the `product_id` field in the `orders`
collection to the `id` field in the `products` collection:

```rust
pipeline.push(doc! {
    "$lookup": {
        "from": "products",
        "localField": "product_id",
        "foreignField": "id",
        "as": "product_mapping"
    }
});
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

```rust
pipeline.push(doc! {
    "$set": {
        "product_mapping": { "$first": "$product_mapping" }
    }
});

pipeline.push(doc! {
    "$set": {
        "product_name": "$product_mapping.name",
        "product_category": "$product_mapping.category"
    }
});
```

**Tip:**

Because this is a one-to-one join, the `$lookup` stage
adds only one array element to the input document. The pipeline
uses the `$first`
operator to retrieve the data from this element.

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the document:

```rust
pipeline.push(doc! {
    "$unset": ["_id", "product_id", "product_mapping"]
});
```

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `orders` collection:

```rust
let mut cursor = orders.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent customer orders that occurred in 2020, with the
`product_name` and `product_category` of the ordered product:

```none
Document({"customer_id": String("elise_smith@myemail.com"), "order_date": DateTime(2020-05-30 8:35:52.0 +00:00:00),
"value": Double(431.42999267578125), "product_name": String("Asus Laptop"), "product_category": String("ELECTRONICS")})

Document({"customer_id": String("oranieri@warmmail.com"), "order_date": DateTime(2020-01-01 8:25:37.0 +00:00:00),
"value": Double(63.130001068115234), "product_name": String("Morphy Richardds Food Mixer"), "product_category": String("KITCHENWARE")})

Document({"customer_id": String("jjones@tepidmail.com"), "order_date": DateTime(2020-12-26 8:55:46.0 +00:00:00),
"value": Double(429.6499938964844), "product_name": String("Asus Laptop"), "product_category": String("ELECTRONICS")})
```

The result consists of documents that contain fields from
documents in the `orders` collection and the `products`
collection, joined by matching the `product_id` field present in
each original document.
