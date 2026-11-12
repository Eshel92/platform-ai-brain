<!-- Part 9 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```c
mongoc_collection_t *persons = mongoc_client_get_collection(client, "agg_tutorials_db", "persons");

{
    bson_t *filter = bson_new();
    bson_error_t error;
    if (!mongoc_collection_delete_many(persons, filter, NULL, NULL, &error))
    {
        fprintf(stderr, "Delete error: %s\n", error.message);
    }
    bson_destroy(filter);
}

{
    size_t num_docs = 6;
    bson_t *docs[num_docs];

    docs[0] = BCON_NEW(
        "person_id", "6392529400",
        "firstname", "Elise",
        "lastname", "Smith",
        "dateofbirth", BCON_DATE_TIME(653616727000UL), // 1972-01-13T09:32:07Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(5625),
        "street", "Tipa Circle",
        "city", "Wojzinmoj",
        "}");

    docs[1] = BCON_NEW(
        "person_id", "1723338115",
        "firstname", "Olive",
        "lastname", "Ranieri",
        "dateofbirth", BCON_DATE_TIME(485113500000UL), // 1985-05-12T23:14:30Z
        "gender", "FEMALE",
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(9303),
        "street", "Mele Circle",
        "city", "Tobihbo",
        "}");

    docs[2] = BCON_NEW(
        "person_id", "8732762874",
        "firstname", "Toni",
        "lastname", "Jones",
        "dateofbirth", BCON_DATE_TIME(690559710000UL), // 1991-11-23T16:53:56Z
        "vocation", "POLITICIAN",
        "address", "{",
        "number", BCON_INT32(1),
        "street", "High Street",
        "city", "Upper Abbeywoodington",
        "}");

    docs[3] = BCON_NEW(
        "person_id", "7363629563",
        "firstname", "Bert",
        "lastname", "Gooding",
        "dateofbirth", BCON_DATE_TIME(449595112000UL), // 1941-04-07T22:11:52Z
        "vocation", "FLORIST",
        "address", "{",
        "number", BCON_INT32(13),
        "street", "Upper Bold Road",
        "city", "Redringtonville",
        "}");

    docs[4] = BCON_NEW(
        "person_id", "1029648329",
        "firstname", "Sophie",
        "lastname", "Celements",
        "dateofbirth", BCON_DATE_TIME(316265745000UL), // 1959-07-06T17:35:45Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(5),
        "street", "Innings Close",
        "city", "Basilbridge",
        "}");

    docs[5] = BCON_NEW(
        "person_id", "7363626383",
        "firstname", "Carl",
        "lastname", "Simmons",
        "dateofbirth", BCON_DATE_TIME(915250045000UL), // 1998-12-26T13:13:55Z
        "vocation", "ENGINEER",
        "address", "{",
        "number", BCON_INT32(187),
        "street", "Hillside Road",
        "city", "Kenningford",
        "}");

    bson_error_t error;
    if (!mongoc_collection_insert_many(persons, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    {
        fprintf(stderr, "Insert error: %s\n", error.message);
    }

    for (int i = 0; i < num_docs; i++)
    {
        bson_destroy(docs[i]);
    }
}
```

**Step 1: Add a match stage for people who are engineers.**

In your pipeline, create a `$match` stage
that finds documents in which the value of the `vocation` field
is `"ENGINEER"`:

```c
"{", "$match", "{", "vocation", BCON_UTF8("ENGINEER"), "}", "}",
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```c
"{", "$sort", "{", "dateofbirth", BCON_INT32(-1), "}", "}",
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```c
"{", "$limit", BCON_INT32(3), "}",
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```c
"{", "$unset", "[", BCON_UTF8("_id"), BCON_UTF8("address"), "]", "}",
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```c
mongoc_cursor_t *results =
    mongoc_collection_aggregate(persons, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

bson_destroy(pipeline);
```

Ensure that you clean up the collection resources by adding the
following line to your cleanup statements:

```c
mongoc_collection_destroy(persons);
```

Finally, run the following commands in your shell to generate and
run the executable:

```bash
gcc -o aggc agg-tutorial.c $(pkg-config --libs --cflags libmongoc-1.0)
./aggc
```

**Tip:**

If you encounter connection errors by running the preceding
commands in one call, you can run them separately.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : { "$numberLong" : "915250045000" } }, "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : { "$numberLong" : "653616727000" } }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : { "$numberLong" : "485113500000" } }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
```


### Create the Template App

Before you begin following an aggregation tutorial, you must set up a
new C++ app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with C++](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/get-started/)
tutorial.

To learn more about using the C++ driver, see the [API documentation](https://mongocxx.org/api/current/).

To learn more about performing aggregations in the C++ Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/aggregation/).

After you install the driver, create a file called
`agg-tutorial.cpp`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```cpp
#include <iostream>
#include <bsoncxx/builder/basic/document.hpp>
#include <bsoncxx/builder/basic/kvp.hpp>
#include <bsoncxx/json.hpp>
#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/pipeline.hpp>
#include <mongocxx/uri.hpp>
#include <chrono>

using bsoncxx::builder::basic::kvp;
using bsoncxx::builder::basic::make_document;
using bsoncxx::builder::basic::make_array;

int main() {
   mongocxx::instance instance;

   // Replace the placeholder with your connection string.
   mongocxx::uri uri("<connection string>");
   mongocxx::client client(uri);

   auto db = client["agg_tutorials_db"];
   // Delete existing data in the database, if necessary.
   db.drop();

   // Get a reference to relevant collections.
   // ... auto some_coll = db["..."];
   // ... auto another_coll = db["..."];

   // Insert sample data into the collection or collections.
   // ... some_coll.insert_many(docs);

   // Create an empty pipelne.
   mongocxx::pipeline pipeline;

   // Add code to create pipeline stages.
   // pipeline.match(make_document(...));

   // Run the aggregation and print the results.
   auto cursor = orders.aggregate(pipeline);
   for (auto&& doc : cursor) {
      std::cout << bsoncxx::to_json(doc, bsoncxx::ExtendedJsonMode::k_relaxed) << std::endl;
   }
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/get-started/#create-a-connection-string)
step of the C++ Get Started tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```cpp
mongocxx::uri uri{"mongodb+srv://mongodb-example:27017"};
```


### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```cpp
auto persons = db["persons"];

std::vector<bsoncxx::document::value> docs = {
    bsoncxx::from_json(R"({
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": {"$date": 620947927},
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": {"$date": 485529270000},
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": {"$date": 690978836000},
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": {"$date": -88368048000},
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": {"$date": -31561935000},
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": {"$date": 915148835000},
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford"
        }
    })")
};

auto result = persons.insert_many(docs); // Might throw an exception
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "vocation": "ENGINEER"
})"));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "dateofbirth": -1
})"));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```cpp
pipeline.limit(3);
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "address"]
})"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```cpp
auto cursor = persons.aggregate(pipeline);
```

Finally, run the following commands in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : "1999-01-01T00:00:35Z" }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : "1985-05-21T13:14:30Z" }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : "1970-01-08T04:29:07.927Z" }, "vocation" : "ENGINEER" }
```


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
