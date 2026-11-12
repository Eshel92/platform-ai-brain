<!-- Part 3 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

First, create C# classes to model the data in the `persons`
collection:

```csharp
public class Person
{
  [BsonId]
  public ObjectId Id { get; set; }
  public string PersonId { get; set; }
  public string FirstName { get; set; }
  public string LastName { get; set; }
  public DateTime DateOfBirth { get; set; }
  [BsonIgnoreIfNull]
  public string? Gender { get; set; }
  public string Vocation { get; set; }
  public Address Address { get; set; }
}

public class Address
{
  public int Number { get; set; }
  public string Street { get; set; }
  public string City { get; set; }
}
```

To create the `persons` collection and insert the sample data, add the
following code to your application:

```csharp
var persons = aggDB.GetCollection<Person>("persons");
persons.DeleteMany(Builders<Person>.Filter.Empty);

persons.InsertMany(new List<Person>
    {
        new Person
        {
            PersonId = "6392529400",
            FirstName = "Elise",
            LastName = "Smith",
            DateOfBirth = DateTime.Parse("1972-01-13T09:32:07Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 5625,
                Street = "Tipa Circle",
                City = "Wojzinmoj"
            }
        },
        new Person
        {
            PersonId = "1723338115",
            FirstName = "Olive",
            LastName = "Ranieri",
            DateOfBirth = DateTime.Parse("1985-05-12T23:14:30Z"),
            Gender = "FEMALE",
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 9303,
                Street = "Mele Circle",
                City = "Tobihbo"
            }
        },
        new Person
        {
            PersonId = "8732762874",
            FirstName = "Toni",
            LastName = "Jones",
            DateOfBirth = DateTime.Parse("1991-11-23T16:53:56Z"),
            Vocation = "POLITICIAN",
            Address = new Address
            {
                Number = 1,
                Street = "High Street",
                City = "Upper Abbeywoodington"
            }
        },
        new Person
        {
            PersonId = "7363629563",
            FirstName = "Bert",
            LastName = "Gooding",
            DateOfBirth = DateTime.Parse("1941-04-07T22:11:52Z"),
            Vocation = "FLORIST",
            Address = new Address
            {
                Number = 13,
                Street = "Upper Bold Road",
                City = "Redringtonville"
            }
        },
        new Person
        {
            PersonId = "1029648329",
            FirstName = "Sophie",
            LastName = "Celements",
            DateOfBirth = DateTime.Parse("1959-07-06T17:35:45Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 5,
                Street = "Innings Close",
                City = "Basilbridge"
            }
        },
        new Person
        {
            PersonId = "7363626383",
            FirstName = "Carl",
            LastName = "Simmons",
            DateOfBirth = DateTime.Parse("1998-12-26T13:13:55Z"),
            Vocation = "ENGINEER",
            Address = new Address
            {
                Number = 187,
                Street = "Hillside Road",
                City = "Kenningford"
            }
        }
    });
```

**Step 1: Add a match stage for people who are engineers.**

First, start the aggregation on the `persons` collection and
chain a `$match` stage that finds documents in which the
value of the `Vocation` field is `"ENGINEER"`:

```csharp
var results = persons.Aggregate()
    .Match(p => p.Vocation == "ENGINEER")
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `DateOfBirth` field to
list the youngest people first:

```csharp
.Sort(Builders<Person>.Sort.Descending(p => p.DateOfBirth))
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit` stage to the pipeline to output
only the first three documents in the results.

```csharp
.Limit(3)
```

**Step 4: Add a projection stage to remove unneeded fields.**

Finally, add a `$project` stage. The
`$project` stage excludes unnecessary fields from the result
documents:

```csharp
.Project(Builders<Person>.Projection
    .Exclude(p => p.Address)
    .Exclude(p => p.Id)
);
```

**Step 5: Run the aggregation and interpret the results.**

Finally, run the application in your IDE and inspect the results.

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `Address`
fields.

```none
{ "PersonId" : "7363626383", "FirstName" : "Carl", "LastName" : "Simmons", "DateOfBirth" : { "$date" : "1998-12-26T13:13:55Z" }, "Vocation" : "ENGINEER" }
{ "PersonId" : "1723338115", "FirstName" : "Olive", "LastName" : "Ranieri", "DateOfBirth" : { "$date" : "1985-05-12T23:14:30Z" }, "Gender" : "FEMALE", "Vocation" : "ENGINEER" }
{ "PersonId" : "6392529400", "FirstName" : "Elise", "LastName" : "Smith", "DateOfBirth" : { "$date" : "1972-01-13T09:32:07Z" }, "Vocation" : "ENGINEER" }
```


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new C app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the [Get Started with the C Driver guide](https://www.mongodb.com/docs/languages/c/c-driver/current/get-started/).

To learn more about performing aggregations in the C Driver, see the
[Aggregation guide](https://www.mongodb.com/docs/languages/c/c-driver/current/aggregation/).

After you install the driver, create a file called
`agg-tutorial.c`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```c
#include <stdio.h>
#include <bson/bson.h>
#include <mongoc/mongoc.h>

int main(void)
{
    mongoc_init();

    // Replace the placeholder with your connection string.
    char *uri = "<connection string>";
    mongoc_client_t* client = mongoc_client_new(uri);

    // Get a reference to relevant collections.
    // ... mongoc_collection_t *some_coll = mongoc_client_get_collection(client, "agg_tutorials_db", "some_coll");
    // ... mongoc_collection_t *another_coll = mongoc_client_get_collection(client, "agg_tutorials_db", "another_coll");

    // Delete any existing documents in collections if needed.
    // ... {
    // ...     bson_t *filter = bson_new();
    // ...     bson_error_t error;
    // ...     if (!mongoc_collection_delete_many(some_coll, filter, NULL, NULL, &error))
    // ...     {
    // ...         fprintf(stderr, "Delete error: %s\n", error.message);
    // ...     }
    // ...     bson_destroy(filter);
    // ... }

    // Insert sample data into the collection or collections.
    // ... {
    // ...     size_t num_docs = ...;
    // ...     bson_t *docs[num_docs];
    // ... 
    // ...     docs[0] = ...;
    // ... 
    // ...     bson_error_t error;
    // ...     if (!mongoc_collection_insert_many(some_coll, (const bson_t **)docs, num_docs, NULL, NULL, &error))
    // ...     {
    // ...         fprintf(stderr, "Insert error: %s\n", error.message);
    // ...     }
    // ... 
    // ...     for (int i = 0; i < num_docs; i++)
    // ...     {
    // ...         bson_destroy(docs[i]);
    // ...     }
    // ... }

    {
        const bson_t *doc;

        // Add code to create pipeline stages.
        bson_t *pipeline = BCON_NEW("pipeline", "[",
        // ... Add pipeline stages here.
        "]");

        // Run the aggregation.
        // ... mongoc_cursor_t *results = mongoc_collection_aggregate(some_coll, MONGOC_QUERY_NONE, pipeline, NULL, NULL);

        bson_destroy(pipeline);

        // Print the aggregation results.
        while (mongoc_cursor_next(results, &doc))
        {
            char *str = bson_as_canonical_extended_json(doc, NULL);
            printf("%s\n", str);
            bson_free(str);
        }
        bson_error_t error;
        if (mongoc_cursor_error(results, &error))
        {
            fprintf(stderr, "Aggregation error: %s\n", error.message);
        }

        mongoc_cursor_destroy(results);
    }

    // Clean up resources.
    // ... mongoc_collection_destroy(some_coll);
    mongoc_client_destroy(client);
    mongoc_cleanup();

    return EXIT_SUCCESS;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/languages/c/c-driver/current/get-started/#create-a-connection-string)
step of the C Get Started guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```c
char *uri = "mongodb+srv://mongodb-example:27017";
```


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
