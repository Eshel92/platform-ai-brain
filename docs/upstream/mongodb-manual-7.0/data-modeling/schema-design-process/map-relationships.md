<!-- Converted from data-modeling/schema-design-process/map-relationships.txt (reStructuredText). Includes are inlined. -->

# Map Schema Relationships

How you map relationships between data entities affects
your application's performance and scalability.

The recommended way to handle related data is to embed it in a sub-document.
Embedding related data lets your application query the data it needs with a
single read operation and avoid slow `$lookup` operations.

For some use cases, you can use a reference to point to related data in a
separate collection. 

## About this Task

To determine if you should embed related data or use references,
consider the relative importance of the following goals for your
application:

Improve queries on related data
  If your application frequently queries one entity to return data about
  another entity, embed the data to avoid the need for frequent
  `$lookup` operations.

Improve data returned from different entities
  If your application returns data from related entities together,
  embed the data in a single collection. 

Improve update performance
  If your application frequently updates related data, consider
  storing the data in its own collection and using a reference to access it.
  When you use a reference, you reduce your application's write workload by only
  needing to update the data in a single place.

To learn more about the benefits of embedded data and references, see
data-modeling-decisions.

## Steps

**Step 1: Identify related data in your schema**

Identify the data that your application queries and how entities
relate to each other.

Consider the operations you identified from your application's
workload in the Identify Application Workload step. Note the
information these operations write and return, and what
information overlaps between multiple operations. 

**Step 2: Create a schema map for your related data**

Your schema map should show related data fields and the type of
relationship between those fields (one-to-one, one-to-many,
many-to-many).

Your schema map can resemble an [entity-relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model).

**Step 3: Choose whether to embed related data or use references**

The decision to embed data or use references depends on your
application's common queries. Review the queries you identified in
the first step of the schema design process and use the guidelines
mentioned earlier on this page to design your schema.

Configure your databases, collections, and application logic to
match the approach you choose.

## Examples

The following examples show how to optimize your schema for different
queries depending on the needs of your application.

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Optimize Queries for Movies

If your application queries movies for fields such as `title`,
embed related information in the `movies` collection. Embedding
data returns everything the application needs in a single operation.

The following document optimizes queries on movies:

```javascript
db.movies.insertOne( {
   title: "The Brutalist",
   year: 2024,
   runtime: 215,
   genres: [ "Drama", "History" ],
   comments: [
      {
         name: "joel_m",
         email: "joel_m@gameofthron.es",
         text: "Visually stunning!"
      }
   ],
   user: {
      name: "Joel M",
      email: "joel_m@gameofthron.es"
   }
} )
```

### Optimize Queries for Movies and Users

If your application returns movie information and user information
separately, consider storing movies and users in separate collections.
This schema design reduces the work required to return user
information, and lets you return only user information without
including unneeded fields.

In the following schema, the `movies` collection contains a
`userId` field, which is a reference to the `users` collection.

#### Movies Collection

```javascript
db.movies.insertOne( {
   title: "A Complete Unknown",
   year: 2024,
   runtime: 141,
   genres: [ "Biography", "Drama", "Music" ],
   userId: 987
} )
```

#### Users Collection

```javascript
db.users.insertOne( {
   _id: 987,
   name: "Joel M",
   email: "joel_m@gameofthron.es"
} )
```

## Next Steps

After you map relationships for your application's data, the next step
in the schema design process is to apply design patterns to optimize
your schema. See data-modeling-apply-patterns.

## Learn More

- databases-and-collections

- data-modeling-duplicate-data

- data-model-example-keyword-search
