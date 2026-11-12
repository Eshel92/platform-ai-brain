<!-- Part 9 of 14 of tutorial/aggregation-examples/multi-field-join.md (split because the page is big). -->

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

```java
MongoCollection<Document> products = aggDB.getCollection("products");
MongoCollection<Document> orders = aggDB.getCollection("orders");

products.deleteMany(Filters.empty());
orders.deleteMany(Filters.empty());

products.insertMany(
        Arrays.asList(
                new Document("name", "Asus Laptop")
                        .append("variation", "Ultra HD")
                        .append("category", "ELECTRONICS")
                        .append("description", "Great for watching movies"),

                new Document("name", "Asus Laptop")
                        .append("variation", "Standard Display")
                        .append("category", "ELECTRONICS")
                        .append("description", "Good value laptop for students"),

                new Document("name", "The Day Of The Triffids")
                        .append("variation", "1st Edition")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),

                new Document("name", "The Day Of The Triffids")
                        .append("variation", "2nd Edition")
                        .append("category", "BOOKS")
                        .append("description", "Classic post-apocalyptic novel"),

                new Document("name", "Morphy Richards Food Mixer")
                        .append("variation", "Deluxe")
                        .append("category", "KITCHENWARE")
                        .append("description", "Luxury mixer turning good cakes into great")
        )
);

orders.insertMany(
        Arrays.asList(
                new Document("customer_id", "elise_smith@myemail.com")
                        .append("orderdate", LocalDateTime.parse("2020-05-30T08:35:52"))
                        .append("product_name", "Asus Laptop")
                        .append("product_variation", "Standard Display")
                        .append("value", 431.43),

                new Document("customer_id", "tj@wheresmyemail.com")
                        .append("orderdate", LocalDateTime.parse("2019-05-28T19:13:32"))
                        .append("product_name", "The Day Of The Triffids")
                        .append("product_variation", "2nd Edition")
                        .append("value", 5.01),

                new Document("customer_id", "oranieri@warmmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-01-01T08:25:37"))
                        .append("product_name", "Morphy Richards Food Mixer")
                        .append("product_variation", "Deluxe")
                        .append("value", 63.13),

                new Document("customer_id", "jjones@tepidmail.com")
                        .append("orderdate", LocalDateTime.parse("2020-12-26T08:55:46"))
                        .append("product_name", "Asus Laptop")
                        .append("product_variation", "Standard Display")
                        .append("value", 429.65)
        )
);
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

```java
List<Bson> embeddedPipeline = new ArrayList<>();

embeddedPipeline.add(Aggregates.match(
        Filters.expr(
                Filters.and(
                        new Document("$eq", Arrays.asList("$product_name", "$$prdname")),
                        new Document("$eq", Arrays.asList("$product_variation", "$$prdvartn"))
                )
        )
));
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```java
embeddedPipeline.add(Aggregates.match(Filters.and(
        Filters.gte("orderdate", LocalDateTime.parse("2020-01-01T00:00:00")),
        Filters.lt("orderdate", LocalDateTime.parse("2021-01-01T00:00:00"))
)));
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```java
embeddedPipeline.add(Aggregates.unset("_id", "product_name", "product_variation"));
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```java
pipeline.add(Aggregates.lookup(
        "orders",
        Arrays.asList(
                new Variable<>("prdname", "$name"),
                new Variable<>("prdvartn", "$variation")
        ),
        embeddedPipeline,
        "orders"
));
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```java
pipeline.add(Aggregates.match(
        Filters.ne("orders", new ArrayList<>())
));
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```java
pipeline.add(Aggregates.unset("_id", "description"));
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```java
AggregateIterable<Document> aggregationResult = products.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
{"name": "Asus Laptop", "variation": "Standard Display", "category": "ELECTRONICS", "orders": [{"customer_id": "elise_smith@myemail.com", "orderdate": {"$date": "2020-05-30T08:35:52Z"}, "value": 431.43}, {"customer_id": "jjones@tepidmail.com", "orderdate": {"$date": "2020-12-26T08:55:46Z"}, "value": 429.65}]}
{"name": "Morphy Richards Food Mixer", "variation": "Deluxe", "category": "KITCHENWARE", "orders": [{"customer_id": "oranieri@warmmail.com", "orderdate": {"$date": "2020-01-01T08:25:37Z"}, "value": 63.13}]}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**kotlin-coroutine:**


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

First, create Kotlin data classes to model the data in the `products`
and `orders` collections:

```kotlin
@Serializable
data class Product(
    val name: String,
    val variation: String,
    val category: String,
    val description: String
)

@Serializable
data class Order(
    val customerID: String,
    @Contextual val orderDate: LocalDateTime,
    val productName: String,
    val productVariation: String,
    val value: Double
)
```

To create the `products` and `orders` collections and insert the
sample data, add the following code to your application:

```kotlin
val products = aggDB.getCollection<Product>("products")
val orders = aggDB.getCollection<Order>("orders")

products.deleteMany(Filters.empty());
orders.deleteMany(Filters.empty());

products.insertMany(
    listOf(
        Product("Asus Laptop", "Ultra HD", "ELECTRONICS", "Great for watching movies"),
        Product("Asus Laptop", "Standard Display", "ELECTRONICS", "Good value laptop for students"),
        Product("The Day Of The Triffids", "1st Edition", "BOOKS", "Classic post-apocalyptic novel"),
        Product("The Day Of The Triffids", "2nd Edition", "BOOKS", "Classic post-apocalyptic novel"),
        Product(
            "Morphy Richards Food Mixer",
            "Deluxe",
            "KITCHENWARE",
            "Luxury mixer turning good cakes into great"
        )
    )
)

orders.insertMany(
    listOf(
        Order(
            "elise_smith@myemail.com",
            LocalDateTime.parse("2020-05-30T08:35:52"),
            "Asus Laptop",
            "Standard Display",
            431.43
        ),
        Order(
            "tj@wheresmyemail.com",
            LocalDateTime.parse("2019-05-28T19:13:32"),
            "The Day Of The Triffids",
            "2nd Edition",
            5.01
        ),
        Order(
            "oranieri@warmmail.com",
            LocalDateTime.parse("2020-01-01T08:25:37"),
            "Morphy Richards Food Mixer",
            "Deluxe",
            63.13
        ),
        Order(
            "jjones@tepidmail.com",
            LocalDateTime.parse("2020-12-26T08:55:46"),
            "Asus Laptop",
            "Standard Display",
            429.65
        )
    )
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

```kotlin
val embeddedPipeline = mutableListOf<Bson>()

embeddedPipeline.add(
    Aggregates.match(
        Filters.expr(
            Document(
                "\$and", listOf(
                    Document("\$eq", listOf("\$${Order::productName.name}", "$\$prdname")),
                    Document("\$eq", listOf("\$${Order::productVariation.name}", "$\$prdvartn"))
                )
            )
        )
    )
)
```

Within the embedded pipeline, add another `$match` stage to match
orders placed in 2020:

```kotlin
embeddedPipeline.add(
    Aggregates.match(
        Filters.and(
            Filters.gte(
                Order::orderDate.name,
                LocalDateTime.parse("2020-01-01T00:00:00").toJavaLocalDateTime()
            ),
            Filters.lt(Order::orderDate.name, LocalDateTime.parse("2021-01-01T00:00:00").toJavaLocalDateTime())
        )
    )
)
```

Within the embedded pipeline, add an `$unset` stage to remove
unneeded fields from the `orders` collection side of the join:

```kotlin
embeddedPipeline.add(Aggregates.unset("_id", Order::productName.name, Order::productVariation.name))
```

After the embedded pipeline is completed, add the
`$lookup` stage to the main aggregation pipeline.
Configure this stage to store the processed lookup fields in
an array field called `orders`:

```kotlin
pipeline.add(
    Aggregates.lookup(
        "orders",
        listOf(
            Variable("prdname", "\$${Product::name.name}"),
            Variable("prdvartn", "\$${Product::variation.name}")
        ),
        embeddedPipeline,
        "orders"
    )
)
```

**Step 2: Add a match stage for products ordered in 2020.**

Next, add a `$match` stage to only show
products for which there is at least one order in 2020,
based on the `orders` array calculated in the previous step:

```kotlin
pipeline.add(
    Aggregates.match(
        Filters.ne("orders", mutableListOf<Document>())
    )
)
```

**Step 3: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes the `_id` and `description`
fields from the result documents:

```kotlin
pipeline.add(Aggregates.unset("_id", "description"))
```

**Step 4: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `products` collection:

```kotlin
val aggregationResult = products.aggregate<Document>(pipeline)
```

Finally, run the application in your IDE.

**Step 5: Interpret the aggregation results.**

The aggregated result contains two documents. The documents
represent products for which there were orders placed in 2020.
Each document contains an `orders` array field that lists details
about each order for that product:

```none
Document{{name=Asus Laptop, variation=Standard Display, category=ELECTRONICS, orders=[Document{{customerID=elise_smith@myemail.com, orderDate=Sat May 30 04:35:52 EDT 2020, value=431.43}}, Document{{customerID=jjones@tepidmail.com, orderDate=Sat Dec 26 03:55:46 EST 2020, value=429.65}}]}}
Document{{name=Morphy Richards Food Mixer, variation=Deluxe, category=KITCHENWARE, orders=[Document{{customerID=oranieri@warmmail.com, orderDate=Wed Jan 01 03:25:37 EST 2020, value=63.13}}]}}
```

The result documents contain details from documents in the
`orders` collection and the `products` collection, joined by
the product names and variations.

**scala:**
