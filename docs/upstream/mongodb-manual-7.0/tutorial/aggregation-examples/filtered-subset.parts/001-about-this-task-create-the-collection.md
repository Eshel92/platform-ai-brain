<!-- Part 1 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

## About This Task

The aggregation pipeline in this tutorial performs the following
operations:

- Matches a subset of documents by a field value
- Formats result documents


## Before You Begin

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


### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```java
MongoCollection<Document> persons = aggDB.getCollection("persons");
persons.deleteMany(Filters.empty());

persons.insertMany(
        Arrays.asList(
                new Document("person_id", "6392529400")
                        .append("firstname", "Elise")
                        .append("lastname", "Smith")
                        .append("dateofbirth", LocalDateTime.parse("1972-01-13T09:32:07"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 5625)
                                .append("street", "Tipa Circle")
                                .append("city", "Wojzinmoj")),
                new Document("person_id", "1723338115")
                        .append("firstname", "Olive")
                        .append("lastname", "Ranieri")
                        .append("dateofbirth", LocalDateTime.parse("1985-05-12T23:14:30"))
                        .append("gender", "FEMALE")
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 9303)
                                .append("street", "Mele Circle")
                                .append("city", "Tobihbo")),
                new Document("person_id", "8732762874")
                        .append("firstname", "Toni")
                        .append("lastname", "Jones")
                        .append("dateofbirth", LocalDateTime.parse("1991-11-23T16:53:56"))
                        .append("vocation", "POLITICIAN")
                        .append("address", new Document("number", 1)
                                .append("street", "High Street")
                                .append("city", "Upper Abbeywoodington")),
                new Document("person_id", "7363629563")
                        .append("firstname", "Bert")
                        .append("lastname", "Gooding")
                        .append("dateofbirth", LocalDateTime.parse("1941-04-07T22:11:52"))
                        .append("vocation", "FLORIST")
                        .append("address", new Document("number", 13)
                                .append("street", "Upper Bold Road")
                                .append("city", "Redringtonville")),
                new Document("person_id", "1029648329")
                        .append("firstname", "Sophie")
                        .append("lastname", "Celements")
                        .append("dateofbirth", LocalDateTime.parse("1959-07-06T17:35:45"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 5)
                                .append("street", "Innings Close")
                                .append("city", "Basilbridge")),
                new Document("person_id", "7363626383")
                        .append("firstname", "Carl")
                        .append("lastname", "Simmons")
                        .append("dateofbirth", LocalDateTime.parse("1998-12-26T13:13:55"))
                        .append("vocation", "ENGINEER")
                        .append("address", new Document("number", 187)
                                .append("street", "Hillside Road")
                                .append("city", "Kenningford"))
        )
);
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```java
pipeline.add(Aggregates.match(Filters.eq("vocation", "ENGINEER")));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```java
pipeline.add(Aggregates.sort(Sorts.descending("dateofbirth")));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```java
pipeline.add(Aggregates.limit(3));
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```java
pipeline.add(Aggregates.unset("_id", "address"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```java
AggregateIterable<Document> aggregationResult = persons.aggregate(pipeline);
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id": "7363626383", "firstname": "Carl", "lastname": "Simmons", "dateofbirth": {"$date": "1998-12-26T13:13:55Z"}, "vocation": "ENGINEER"}
{"person_id": "1723338115", "firstname": "Olive", "lastname": "Ranieri", "dateofbirth": {"$date": "1985-05-12T23:14:30Z"}, "gender": "FEMALE", "vocation": "ENGINEER"}
{"person_id": "6392529400", "firstname": "Elise", "lastname": "Smith", "dateofbirth": {"$date": "1972-01-13T09:32:07Z"}, "vocation": "ENGINEER"}
```
