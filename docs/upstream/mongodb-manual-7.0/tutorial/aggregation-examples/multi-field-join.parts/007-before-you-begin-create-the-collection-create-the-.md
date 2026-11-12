<!-- Part 7 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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

First, create Go structs to model the data in the `products` and `orders`
collections:

```go
type Product struct {
	Name        string
	Variation   string
	Category    string
	Description string
}

type Order struct {
	CustomerID       string        `bson:"customer_id"`
	OrderDate        bson.DateTime `bson:"orderdate"`
	ProductName      string        `bson:"product_name"`
	ProductVariation string        `bson:"product_variation"`
	Value            float32       `bson:"value"`
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```go
products := aggDB.Collection("products")
orders := aggDB.Collection("orders")
products.DeleteMany(context.TODO(), bson.D{})
orders.DeleteMany(context.TODO(), bson.D{})

_, err = products.InsertMany(context.TODO(), []interface{}{
	Product{
		Name:        "Asus Laptop",
		Variation:   "Ultra HD",
		Category:    "ELECTRONICS",
		Description: "Great for watching movies",
	},
	Product{
		Name:        "Asus Laptop",
		Variation:   "Standard Display",
		Category:    "ELECTRONICS",
		Description: "Good value laptop for students",
	},
	Product{
		Name:        "The Day Of The Triffids",
		Variation:   "1st Edition",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		Name:        "The Day Of The Triffids",
		Variation:   "2nd Edition",
		Category:    "BOOKS",
		Description: "Classic post-apocalyptic novel",
	},
	Product{
		Name:        "Morphy Richards Food Mixer",
		Variation:   "Deluxe",
		Category:    "KITCHENWARE",
		Description: "Luxury mixer turning good cakes into great",
	},
})
if err != nil {
	log.Fatal(err)
}

_, err = orders.InsertMany(context.TODO(), []interface{}{
	Order{
		CustomerID:       "elise_smith@myemail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 5, 30, 8, 35, 52, 0, time.UTC)),
		ProductName:      "Asus Laptop",
		ProductVariation: "Standard Display",
		Value:            431.43,
	},
	Order{
		CustomerID:       "tj@wheresmyemail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2019, 5, 28, 19, 13, 32, 0, time.UTC)),
		ProductName:      "The Day Of The Triffids",
		ProductVariation: "2nd Edition",
		Value:            5.01,
	},
	Order{
		CustomerID:       "oranieri@warmmail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 1, 1, 8, 25, 37, 0, time.UTC)),
		ProductName:      "Morphy Richards Food Mixer",
		ProductVariation: "Deluxe",
		Value:            63.13,
	},
	Order{
		CustomerID:       "jjones@tepidmail.com",
		OrderDate:        bson.NewDateTimeFromTime(time.Date(2020, 12, 26, 8, 55, 46, 0, time.UTC)),
		ProductName:      "Asus Laptop",
		ProductVariation: "Standard Display",
		Value:            429.65,
	},
})
if err != nil {
	log.Fatal(err)
}
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

```go
embeddedMatchStage1 := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "$expr", Value: bson.D{
			{Key: "$and", Value: bson.A{
				bson.D{{Key: "$eq", Value: bson.A{"$product_name", "$$prdname"}}},
				bson.D{{Key: "$eq", Value: bson.A{"$product_variation", "$$prdvartn"}}},
			}},
		}},
	}},
}
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```go
embeddedMatchStage2 := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "orderdate", Value: bson.D{
			{Key: "$gte", Value: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)},
			{Key: "$lt", Value: time.Date(2021, 1, 1, 0, 0, 0, 0, time.UTC)},
		}},
	}},
}
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```go
embeddedUnsetStage := bson.D{
	{Key: "$unset", Value: bson.A{"_id", "product_name", "product_variation"}},
}
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```go
embeddedPipeline := mongo.Pipeline{embeddedMatchStage1, embeddedMatchStage2, embeddedUnsetStage}

lookupStage := bson.D{
	{Key: "$lookup", Value: bson.D{
		{Key: "from", Value: "orders"},
		{Key: "let", Value: bson.D{
			{Key: "prdname", Value: "$name"},
			{Key: "prdvartn", Value: "$variation"},
		}},
		{Key: "pipeline", Value: embeddedPipeline},
		{Key: "as", Value: "orders"},
	}},
}
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```go
matchStage := bson.D{
	{Key: "$match", Value: bson.D{
		{Key: "orders", Value: bson.D{{Key: "$ne", Value: bson.A{}}}},
	}},
}
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```go
unsetStage := bson.D{
	{Key: "$unset", Value: bson.A{"_id", "description"}},
}
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```go
pipeline := mongo.Pipeline{lookupStage, matchStage, unsetStage}
cursor, err := products.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name":"Asus Laptop","variation":"Standard Display","category":"ELECTRONICS","orders":[{"customer_id":"elise_smith@myemail.com","orderdate":{"$date":"2020-05-30T08:35:52Z"},"value":431.42999267578125},{"customer_id":"jjones@tepidmail.com","orderdate":{"$date":"2020-12-26T08:55:46Z"},"value":429.6499938964844}]}
{"name":"Morphy Richards Food Mixer","variation":"Deluxe","category":"KITCHENWARE","orders":[{"customer_id":"oranieri@warmmail.com","orderdate":{"$date":"2020-01-01T08:25:37Z"},"value":63.130001068115234}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

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

First, create Rust structs to model the data in the `products` and `orders`
collections:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Product {
    name: String,
    variation: String,
    category: String,
    description: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Order {
    customer_id: String,
    order_date: DateTime,
    product_name: String,
    product_variation: String,
    value: f32,
}
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```rust
let products: Collection<Product> = agg_db.collection("products");
let orders: Collection<Order> = agg_db.collection("orders");

products.delete_many(doc! {}).await?;
orders.delete_many(doc! {}).await?;

let product_docs = vec![
    Product {
        name: "Asus Laptop".to_string(),
        variation: "Ultra HD".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Great for watching movies".to_string(),
    },
    Product {
        name: "Asus Laptop".to_string(),
        variation: "Standard Display".to_string(),
        category: "ELECTRONICS".to_string(),
        description: "Good value laptop for students".to_string(),
    },
    Product {
        name: "The Day Of The Triffids".to_string(),
        variation: "1st Edition".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        name: "The Day Of The Triffids".to_string(),
        variation: "2nd Edition".to_string(),
        category: "BOOKS".to_string(),
        description: "Classic post-apocalyptic novel".to_string(),
    },
    Product {
        name: "Morphy Richards Food Mixer".to_string(),
        variation: "Deluxe".to_string(),
        category: "KITCHENWARE".to_string(),
        description: "Luxury mixer turning good cakes into great".to_string(),
    },
];
products.insert_many(product_docs).await?;

let order_docs = vec![
    Order {
        customer_id: "elise_smith@myemail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(5).day(30).hour(8).minute(35).second(52).build().unwrap(),
        product_name: "Asus Laptop".to_string(),
        product_variation: "Standard Display".to_string(),
        value: 431.43,
    },
    Order {
        customer_id: "tj@wheresmyemail.com".to_string(),
        order_date: DateTime::builder().year(2019).month(5).day(28).hour(19).minute(13).second(32).build().unwrap(),
        product_name: "The Day Of The Triffids".to_string(),
        product_variation: "2nd Edition".to_string(),
        value: 5.01,
    },
    Order {
        customer_id: "oranieri@warmmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(1).day(1).hour(8).minute(25).second(37).build().unwrap(),
        product_name: "Morphy Richards Food Mixer".to_string(),
        product_variation: "Deluxe".to_string(),
        value: 63.13,
    },
    Order {
        customer_id: "jjones@tepidmail.com".to_string(),
        order_date: DateTime::builder().year(2020).month(12).day(26).hour(8).minute(55).second(46).build().unwrap(),
        product_name: "Asus Laptop".to_string(),
        product_variation: "Standard Display".to_string(),
        value: 429.65,
    },
];
orders.insert_many(order_docs).await?;
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

```rust
let mut embedded_pipeline = Vec::new();
embedded_pipeline.push(doc! {
    "$match": {
        "$expr": {
            "$and": [
                { "$eq": ["$product_name", "$$prdname"] },
                { "$eq": ["$product_variation", "$$prdvartn"] }
            ]
        }
    }
});
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```rust
embedded_pipeline.push(doc! {
    "$match": {
        "order_date": {
            "$gte": DateTime::builder().year(2020).month(1).day(1).build().unwrap(),
            "$lt": DateTime::builder().year(2021).month(1).day(1).build().unwrap()
        }
    }
});
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```rust
embedded_pipeline.push(doc! {
    "$unset": ["_id", "product_name", "product_variation"]
});
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```rust
pipeline.push(doc! {
    "$lookup": {
        "from": "orders",
        "let": {
            "prdname": "$name",
            "prdvartn": "$variation"
        },
        "pipeline": embedded_pipeline,
        "as": "orders"
    }
});
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```rust
pipeline.push(doc! {
    "$match": {
        "orders": { "$ne": [] }
    }
});
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```rust
pipeline.push(doc! {
    "$unset": ["_id", "description"]
});
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```rust
let mut cursor = products.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
Document({"name": String("Asus Laptop"), "variation": String("Standard Display"), "category": String("ELECTRONICS"),
"orders": Array([Document({"customer_id": String("elise_smith@myemail.com"), "order_date": DateTime(2020-05-30 8:35:52.0 +00:00:00),
"value": Double(431.42999267578125)}), Document({"customer_id": String("jjones@tepidmail.com"), "order_date":
DateTime(2020-12-26 8:55:46.0 +00:00:00), "value": Double(429.6499938964844)})])})

Document({"name": String("Morphy Richards Food Mixer"), "variation": String("Deluxe"), "category": String("KITCHENWARE"),
"orders": Array([Document({"customer_id": String("oranieri@warmmail.com"), "order_date": DateTime(2020-01-01 8:25:37.0 +00:00:00),
"value": Double(63.130001068115234)})])})
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.
