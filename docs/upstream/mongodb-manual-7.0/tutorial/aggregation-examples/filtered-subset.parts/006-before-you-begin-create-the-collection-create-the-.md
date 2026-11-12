<!-- Part 6 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

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


## Steps

The following steps demonstrate how to create and run an aggregation
pipeline to filter for a specific subset of documents.

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The aggregation selects documents based on whether their field values
match specified criteria.

**Step 1: Run the aggregation pipeline.**

```javascript
db.movies.aggregate( [
   // Stage 1: Match documents with the Drama genre
   { $match: { genres: "Drama" } },

   // Stage 2: Sort documents from oldest to newest
   { $sort: { year: 1 } },

   // Stage 3: Limit the results to 3 documents
   { $limit: 3 },

   // Stage 4: Project only the fields needed for the result
   { $project: { _id: 0, title: 1, year: 1, directors: 1, runtime: 1 } }
] )
```

**Step 2: Interpret the aggregation results.**

The aggregated results contain three documents. The documents
represent the three oldest movies in the `Drama` genre,
ordered from oldest to newest. The results include only the
`title`, `year`, `directors`, and `runtime` fields.

```javascript
[
  {
    runtime: 14,
    title: 'A Corner in Wheat',
    directors: [
      'D.W. Griffith'
    ],
    year: 1909
  },
  {
    runtime: 88,
    title: 'Traffic in Souls',
    directors: [
      'George Loane Tucker'
    ],
    year: 1913
  },
  {
    runtime: 65,
    title: 'In the Land of the Head Hunters',
    directors: [
      'Edward S. Curtis'
    ],
    year: 1914
  }
]
```


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

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```python
person_coll = agg_db["persons"]
person_coll.delete_many({})

person_data = [
    {
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": datetime(1972, 1, 13, 9, 32, 7),
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj",
        },
    },
    {
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": datetime(1985, 5, 12, 23, 14, 30),
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo",
        },
    },
    {
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": datetime(1991, 11, 23, 16, 53, 56),
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington",
        },
    },
    {
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": datetime(1941, 4, 7, 22, 11, 52),
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville",
        },
    },
    {
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": datetime(1959, 7, 6, 17, 35, 45),
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge",
        },
    },
    {
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": datetime(1998, 12, 26, 13, 13, 55),
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford",
        },
    },
]

person_coll.insert_many(person_data)
```

**Step 1: Add a match stage for people who are engineers.**

In your `Pipeline` instance, create a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```python
pipeline.append({"$match": {"vocation": "ENGINEER"}})
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```python
pipeline.append({"$sort": {"dateofbirth": -1}})
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```python
pipeline.append({"$limit": 3})
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```python
pipeline.append({"$unset": ["_id", "address"]})
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```python
aggregation_result = person_coll.aggregate(pipeline)
```

Finally, run the following command in your shell to start your
application:

```bash
python3 agg_tutorial.py
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{'person_id': '7363626383', 'firstname': 'Carl', 'lastname': 'Simmons', 'dateofbirth': datetime.datetime(1998, 12, 26, 13, 13, 55), 'vocation': 'ENGINEER'}
{'person_id': '1723338115', 'firstname': 'Olive', 'lastname': 'Ranieri', 'dateofbirth': datetime.datetime(1985, 5, 12, 23, 14, 30), 'gender': 'FEMALE', 'vocation': 'ENGINEER'}
{'person_id': '6392529400', 'firstname': 'Elise', 'lastname': 'Smith', 'dateofbirth': datetime.datetime(1972, 1, 13, 9, 32, 7), 'vocation': 'ENGINEER'}
```


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
