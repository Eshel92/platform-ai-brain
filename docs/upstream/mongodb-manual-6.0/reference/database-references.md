<!-- Converted from reference/database-references.txt (reStructuredText). Includes are inlined. -->

# Database References

For many use cases in MongoDB, the denormalized data model where
related data is stored within a single document is optimal. 
However, in some cases, it makes sense to store related
information in separate documents, typically in different collections
or databases.

**Important:**

You can use the `$lookup` pipeline stage to perform
a left outer join to an unsharded collection in the same database.

You can also use the `$graphLookup` pipeline stage to join an 
unsharded collection to perform recursive search.

This page outlines alternative procedures that predate the
`$lookup` and `$graphLookup` pipeline stages.

You can create a database reference for deployments hosted in the
following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

MongoDB applications use one of two methods to relate documents:

- Manual references save the
  `_id` field of one document in another document as a reference.
  Your application runs a second query to return the related
  data. These references are simple and sufficient for most use
  cases.

- DBRefs are references from one document to another
  using the value of the first document's `_id` field, collection name,
  and, optionally, its database name, as well as any other fields. DBRefs allow
  you to more easily reference documents stored in multiple collections or 
  databases.

To resolve DBRefs, your application must perform additional queries to return
the referenced documents. Some `MongoDB drivers` provide helper 
methods to enable DBRefs to be resolved into documents, but it doesn't happen 
automatically.

DBRefs provide a common format and type to represent relationships among
documents. The DBRef format also provides common semantics for representing
links between documents if your database must interact with
multiple frameworks and tools.

Unless you have a compelling reason to use DBRefs, use manual
references instead.

## Manual References

### Background

A manual reference is the practice of including one
document's `_id` field in another document. The
application can then issue a second query to resolve the referenced
fields as needed.

### Create a Manual Reference in the MongoDB Atlas UI

To create a manual reference in the MongoDB Atlas UI, follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

**Warning:** Navigation Improvements In Progress

We're currently rolling out a new and improved navigation 
experience. If the following steps don't match your view in the 
Atlas UI, see `the preview Atlas documentation`.

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. If it's not already displayed, click Clusters in the 
   sidebar.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection.**

a. For the cluster where you want to add a database
   reference, click Browse Collections.
#. In the left navigation pane, select the database.
#. In the left navigation pane, select the collection. This
   example references a `places` collection.

**Step 3: Add a document.**

a. Click Insert Document.
#. Click the JSON view icon ({{}}).
#. Paste the following data into the document:

   ```
   {
     "_id": {
       "$oid": "651aea5870299b120736f442"
     },
     "name": "Broadway Center",
     "url": "bc.example.net"
   }
   ```

#. Click Insert.

**Step 4: Add a document in the `people` collection that references the entry in `places`.**

a. In the left navigation pane, select a different
   collection. This example references a `people` collection.
#. Click Insert Document.
#. Click the JSON view icon ({{}}).
#. Paste the following data into the document:

   ```
   {
     "_id": {
       "$oid": "651aebeb70299b120736f443"
     },
     "name": "Erin",
     "places_id": "651aea5870299b120736f442"
     "url": "bc.example.net/Erin"
   }
   ```

#. Click Insert.

   When a query returns the document from the `people`
   collection you can, if needed, filter the query results from
   the `places` collection for the document referenced by the
   `places_id` field.

   To learn more about running queries in MongoDB Atlas,
   see View, Filter, and Sort Documents in
   the MongoDB Atlas documentation.

### Create a Manual Reference in the Terminal

Consider the following operation to insert two documents, using the
`_id` field of the first document as a reference in the second
document:

```javascript
original_id = ObjectId()

db.places.insertOne({
    "_id": original_id,
    "name": "Broadway Center",
    "url": "bc.example.net"
})

db.people.insertOne({
    "name": "Erin",
    "places_id": original_id,
    "url":  "bc.example.net/Erin"
})
```

Then, when a query returns the document from the `people` collection
you can, if needed, make a second query for the document referenced by
the `places_id` field in the `places` collection.

### Use

For nearly every case where you want to store a relationship between
two documents, use manual references. The
references are simple to create and your application can resolve
references as needed.

The only limitation of manual linking is that these references do not
convey the database and collection names. If you have documents in a
single collection that relate to documents in more than one
collection, you may need to consider using DBRefs.

## DBRefs

### Background

DBRefs are a convention for representing a document, rather
than a specific reference type. They include the name of the
collection, and in some cases the database name, in addition to the
value from the `_id` field. 

Optionally, DBRefs can include any number of other fields. Extra field names 
must follow any rules for field names 
imposed by the server version.

### Format

DBRefs have the following fields:

**`$ref`**

The `$ref` field holds the name of the collection where the
referenced document resides.

**`$id`**

The `$id` field contains the value of the `_id` field in the
referenced document.

**`$db`**

*Optional.*

Contains the name of the database where the referenced document
resides.

**Example:**

DBRef documents resemble the following document:

```javascript
{ "$ref" : <value>, "$id" : <value>, "$db" : <value> }
```

Consider a document from a collection that stored a DBRef in a
`creator` field:

```javascript
{
  "_id" : ObjectId("5126bbf64aed4daf9e2ab771"),
  // .. application fields
  "creator" : {
                  "$ref" : "creators",
                  "$id" : ObjectId("5126bc054aed4daf9e2ab772"),
                  "$db" : "users",
                  "extraField" : "anything"
               }
}
```

The DBRef in this example points to a document in the `creators`
collection of the `users` database that has
`ObjectId("5126bc054aed4daf9e2ab772")` in its `_id` field. It also contains
an optional field.

**Note:**

The order of fields in the DBRef matters, and you must use the above
sequence when using a DBRef.

### Driver Support for DBRefs

| Driver | DBRef Support | Notes |
|---|---|---|
| C | Not Supported | You can traverse references manually. |
| C++ | Not Supported | You can traverse references manually. |
| C# | Supported | Please see the `C# driver page` for more information. |
| Go | Not Supported | You can traverse references manually. |
| Haskell | Not Supported | You can traverse references manually. |
| Java | Supported | Please see the `Java driver page` for more information. |
| Node.js | Supported | Please see the `Node.js driver page` for more information. |
| Perl | Supported | Please see the `Perl driver page` for more information. |
| PHP | Not Supported | You can traverse references manually. |
| Python | Supported | Please see the `PyMongo driver page` for more information. |
| Ruby | Supported | Please see the `Ruby driver page` for more information. |
| Scala | Not Supported | You can traverse references manually. |

### Use

In most cases you should use the manual reference method for connecting two or more related
documents. However, if you need to reference documents from multiple
collections, consider using DBRefs.
