<!-- Part 11 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

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


### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Go structs to model the data in the `persons`
collection:

```go
type Person struct {
	PersonID    string        `bson:"person_id"`
	Firstname   string        `bson:"firstname"`
	Lastname    string        `bson:"lastname"`
	Gender      string        `bson:"gender,omitempty"`
	DateOfBirth bson.DateTime `bson:"dateofbirth"`
	Vocation    string        `bson:"vocation"`
	Address     Address       `bson:"address"`
}

type Address struct {
	Number int
	Street string
	City   string
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```go
persons := aggDB.Collection("persons")
persons.DeleteMany(context.TODO(), bson.D{})

_, err = persons.InsertMany(context.TODO(), []interface{}{
	Person{
		PersonID:    "6392529400",
		Firstname:   "Elise",
		Lastname:    "Smith",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1972, 1, 13, 9, 32, 7, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 5625, Street: "Tipa Circle", City: "Wojzinmoj"},
	},
	Person{
		PersonID:    "1723338115",
		Firstname:   "Olive",
		Lastname:    "Ranieri",
		Gender:      "FEMALE",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1985, 5, 12, 23, 14, 30, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 9303, Street: "Mele Circle", City: "Tobihbo"},
	},
	Person{
		PersonID:    "8732762874",
		Firstname:   "Toni",
		Lastname:    "Jones",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1991, 11, 23, 16, 53, 56, 0, time.UTC)),
		Vocation:    "POLITICIAN",
		Address:     Address{Number: 1, Street: "High Street", City: "Upper Abbeywoodington"},
	},
	Person{
		PersonID:    "7363629563",
		Firstname:   "Bert",
		Lastname:    "Gooding",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1941, 4, 7, 22, 11, 52, 0, time.UTC)),
		Vocation:    "FLORIST",
		Address:     Address{Number: 13, Street: "Upper Bold Road", City: "Redringtonville"},
	},
	Person{
		PersonID:    "1029648329",
		Firstname:   "Sophie",
		Lastname:    "Celements",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1959, 7, 6, 17, 35, 45, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 5, Street: "Innings Close", City: "Basilbridge"},
	},
	Person{
		PersonID:    "7363626383",
		Firstname:   "Carl",
		Lastname:    "Simmons",
		DateOfBirth: bson.NewDateTimeFromTime(time.Date(1998, 12, 26, 13, 13, 55, 0, time.UTC)),
		Vocation:    "ENGINEER",
		Address:     Address{Number: 187, Street: "Hillside Road", City: "Kenningford"},
	},
})
if err != nil {
	log.Fatal(err)
}
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```go
matchStage := bson.D{{Key: "$match", Value: bson.D{{Key: "vocation", Value: "ENGINEER"}}}}
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```go
sortStage := bson.D{{Key: "$sort", Value: bson.D{{Key: "dateofbirth", Value: -1}}}}
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```go
limitStage := bson.D{{Key: "$limit", Value: 3}}
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```go
unsetStage := bson.D{{Key: "$unset", Value: bson.A{"_id", "address"}}}
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```go
pipeline := mongo.Pipeline{matchStage, sortStage, limitStage, unsetStage}
cursor, err := persons.Aggregate(context.TODO(), pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
go run agg_tutorial.go
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id":"7363626383","firstname":"Carl","lastname":"Simmons","dateofbirth":{"$date":"1998-12-26T13:13:55Z"},"vocation":"ENGINEER"}
{"person_id":"1723338115","firstname":"Olive","lastname":"Ranieri","gender":"FEMALE","dateofbirth":{"$date":"1985-05-12T23:14:30Z"},"vocation":"ENGINEER"}
{"person_id":"6392529400","firstname":"Elise","lastname":"Smith","dateofbirth":{"$date":"1972-01-13T09:32:07Z"},"vocation":"ENGINEER"}
```


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

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create Rust structs to model the data in the `persons`
collection:

```rust
#[derive(Debug, Serialize, Deserialize)]
struct Address {
    number: i32,
    street: String,
    city: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Person {
    person_id: String,
    firstname: String,
    lastname: String,
    dateofbirth: DateTime,
    vocation: String,
    address: Address,
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```rust
let persons: Collection<Person> = agg_db.collection("persons");
persons.delete_many(doc! {}).await?;

let data = vec![
    Person {
        person_id: "6392529400".to_string(),
        firstname: "Elise".to_string(),
        lastname: "Smith".to_string(),
        dateofbirth: DateTime::builder().year(1972).month(1).day(13).hour(9).minute(32).second(7).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 5625,
            street: "Tipa Circle".to_string(),
            city: "Wojzinmoj".to_string(),
        },
    },
    Person {
        person_id: "1723338115".to_string(),
        firstname: "Olive".to_string(),
        lastname: "Ranieri".to_string(),
        gender: "FEMALE".to_string(),
        dateofbirth: DateTime::builder().year(1985).month(5).day(12).hour(23).minute(14).second(30).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 9303,
            street: "Mele Circle".to_string(),
            city: "Tobihbo".to_string(),
        },
    },
    Person {
        person_id: "8732762874".to_string(),
        firstname: "Toni".to_string(),
        lastname: "Jones".to_string(),
        dateofbirth: DateTime::builder().year(1991).month(11).day(23).hour(16).minute(53).second(56).build().unwrap(),
        vocation: "POLITICIAN".to_string(),
        address: Address {
            number: 1,
            street: "High Street".to_string(),
            city: "Upper Abbeywoodington".to_string(),
        },
    },
    Person {
        person_id: "7363629563".to_string(),
        firstname: "Bert".to_string(),
        lastname: "Gooding".to_string(),
        dateofbirth: DateTime::builder().year(1941).month(4).day(7).hour(22).minute(11).second(52).build().unwrap(),
        vocation: "FLORIST".to_string(),
        address: Address {
            number: 13,
            street: "Upper Bold Road".to_string(),
            city: "Redringtonville".to_string(),
        },
    },
    Person {
        person_id: "1029648329".to_string(),
        firstname: "Sophie".to_string(),
        lastname: "Celements".to_string(),
        dateofbirth: DateTime::builder().year(1959).month(7).day(6).hour(17).minute(35).second(45).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 5,
            street: "Innings Close".to_string(),
            city: "Basilbridge".to_string(),
        },
    },
    Person {
        person_id: "7363626383".to_string(),
        firstname: "Carl".to_string(),
        lastname: "Simmons".to_string(),
        dateofbirth: DateTime::builder().year(1998).month(12).day(26).hour(13).minute(13).second(55).build().unwrap(),
        vocation: "ENGINEER".to_string(),
        address: Address {
            number: 187,
            street: "Hillside Road".to_string(),
            city: "Kenningford".to_string(),
        },
    },
];

persons.insert_many(data).await?;
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```rust
pipeline.push(doc! { "$match": { "vocation": "ENGINEER" } });
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```rust
pipeline.push(doc! { "$sort": { "dateofbirth": -1 } });
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```rust
pipeline.push(doc! { "$limit": 3 });
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```rust
pipeline.push(doc! { "$unset": ["_id", "address"] });
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```rust
let mut cursor = persons.aggregate(pipeline).await?;
```

Finally, run the following command in your shell to start your
application:

```bash
cargo run
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
Document({"person_id": String("7363626383"), "firstname": String("Carl"), "lastname": String("Simmons"), "dateofbirth": DateTime(1998-12-26 13:13:55.0 +00:00:00), "vocation": String("ENGINEER")})

Document({"person_id": String("1723338115"), "firstname": String("Olive"), "lastname": String("Ranieri"), "gender": String("FEMALE"), "dateofbirth": DateTime(1985-05-12 23:14:30.0 +00:00:00), "vocation": String("ENGINEER")})

Document({"person_id": String("6392529400"), "firstname": String("Elise"), "lastname": String("Smith"), "dateofbirth": DateTime(1972-01-13 9:32:07.0 +00:00:00), "vocation": String("ENGINEER")})
```
