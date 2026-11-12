<!-- Part 8 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```scala
val persons = aggDB.getCollection("persons")

persons.deleteMany(Filters.empty()).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)

val dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss")

persons.insertMany(Seq(
  Document(
    "person_id" -> "6392529400",
    "firstname" -> "Elise",
    "lastname" -> "Smith",
    "dateofbirth" -> dateFormat.parse("1972-01-13T09:32:07"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 5625,
      "street" -> "Tipa Circle",
      "city" -> "Wojzinmoj"
    )
  ),
  Document(
    "person_id" -> "1723338115",
    "firstname" -> "Olive",
    "lastname" -> "Ranieri",
    "dateofbirth" -> dateFormat.parse("1985-05-12T23:14:30"),
    "gender" -> "FEMALE",
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 9303,
      "street" -> "Mele Circle",
      "city" -> "Tobihbo"
    )
  ),
  Document(
    "person_id" -> "8732762874",
    "firstname" -> "Toni",
    "lastname" -> "Jones",
    "dateofbirth" -> dateFormat.parse("1991-11-23T16:53:56"),
    "vocation" -> "POLITICIAN",
    "address" -> Document(
      "number" -> 1,
      "street" -> "High Street",
      "city" -> "Upper Abbeywoodington"
    )
  ),
  Document(
    "person_id" -> "7363629563",
    "firstname" -> "Bert",
    "lastname" -> "Gooding",
    "dateofbirth" -> dateFormat.parse("1941-04-07T22:11:52"),
    "vocation" -> "FLORIST",
    "address" -> Document(
      "number" -> 13,
      "street" -> "Upper Bold Road",
      "city" -> "Redringtonville"
    )
  ),
  Document(
    "person_id" -> "1029648329",
    "firstname" -> "Sophie",
    "lastname" -> "Celements",
    "dateofbirth" -> dateFormat.parse("1959-07-06T17:35:45"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 5,
      "street" -> "Innings Close",
      "city" -> "Basilbridge"
    )
  ),
  Document(
    "person_id" -> "7363626383",
    "firstname" -> "Carl",
    "lastname" -> "Simmons",
    "dateofbirth" -> dateFormat.parse("1998-12-26T13:13:55"),
    "vocation" -> "ENGINEER",
    "address" -> Document(
      "number" -> 187,
      "street" -> "Hillside Road",
      "city" -> "Kenningford"
    )
  )
)).subscribe(
  _ => {},
  e => println("Error: " + e.getMessage),
)
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```scala
Aggregates.filter(Filters.equal("vocation", "ENGINEER")),
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```scala
Aggregates.sort(Sorts.descending("dateofbirth")),
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```scala
Aggregates.limit(3),
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```scala
Aggregates.unset("_id", "address")
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```scala
persons.aggregate(pipeline)
  .subscribe((doc: Document) => println(doc.toJson()),
    (e: Throwable) => println(s"Error: $e"))
```

Finally, run the application in your IDE.

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{"person_id": "7363626383", "firstname": "Carl", "lastname": "Simmons", "dateofbirth": {"$date": "1998-12-26T18:13:55Z"}, "vocation": "ENGINEER"}
{"person_id": "1723338115", "firstname": "Olive", "lastname": "Ranieri", "dateofbirth": {"$date": "1985-05-13T03:14:30Z"}, "gender": "FEMALE", "vocation": "ENGINEER"}
{"person_id": "6392529400", "firstname": "Elise", "lastname": "Smith", "dateofbirth": {"$date": "1972-01-13T14:32:07Z"}, "vocation": "ENGINEER"}
```


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new C#/.NET app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `C#/.NET Driver Quick Start guide`.

To learn more about performing aggregations in the C#/.NET Driver, see the
`Aggregation guide`.

After you install the driver, paste the following code into your
`Program.cs` file to create an app template for the aggregation
tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```csharp
using MongoDB.Driver;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

// Define data model classes.
// ... public class MyClass { ... }

// Replace the placeholder with your connection string.
var uri = "<connection string>";
var client = new MongoClient(uri);
var aggDB = client.GetDatabase("agg_tutorials_db");

// Get a reference to relevant collections.
// ... var someColl = aggDB.GetCollection<MyClass>("someColl");
// ... var anotherColl = aggDB.GetCollection<MyClass>("anotherColl");

// Delete any existing documents in collections if needed.
// ... someColl.DeleteMany(Builders<MyClass>.Filter.Empty);

// Insert sample data into the collection or collections.
// ... someColl.InsertMany(new List<MyClass> { ... });

// Add code to chain pipeline stages to the Aggregate() method.
// ... var results = someColl.Aggregate().Match(...);

// Print the aggregation results.
foreach (var result in results.ToList())
{
  Console.WriteLine(result);
}
```

For every tutorial, you must replace the connection string placeholder
with your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Set Up a Free Cluster in Atlas`
step of the C# Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```csharp
var uri = "mongodb+srv://mongodb-example:27017";
```


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
