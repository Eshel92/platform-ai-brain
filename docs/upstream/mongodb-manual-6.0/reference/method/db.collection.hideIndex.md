<!-- Converted from reference/method/db.collection.hideIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.hideIndex()

## Definition

**`db.collection.hideIndex()`**

   using the `collMod` command

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `index.hidden` collection option set.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Hides an existing index from the query planner. An index
hidden from the query planner is not evaluated
as part of query plan selection.

By hiding an index from the planner, you can evaluate the
potential impact of dropping an index without actually dropping the
index. If the impact is negative, you can unhide the index
instead of having to recreate a dropped index. And because indexes
are fully maintained while hidden, the indexes are immediately
available for use once unhidden.

For details, see /core/index-hidden.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```javascript
db.collection.hideIndex(<index>)
```

### Parameters

The `db.collection.hideIndex()` method takes the following
parameter:

* - Parameter

  - Type

  - Description

* - `index`

  - string or document

  - Specifies the index to hide from the query planner. You can
    specify the index either by the index name or by the index
    specification document.

    **Tip:**

    You can use the `db.collection.getIndexes()` method
    to find the index name or the index specification document.

    To hide a text index, specify the
    index name.

The `db.collection.hideIndex()` is a `mongosh` shell
wrapper for the `collMod` command.

## Behavior

### Feature Compatibility Version

To hide an index, you must have featureCompatibilityVersion set to `5.0` or greater. 

### Restrictions

You cannot hide the `_id` index.

### Index Modifications Reset Statistics

Hiding an unhidden index resets its `$indexStats`.

### No-op

Hiding an already hidden index has no effect on the index. However, the
operation will still generate an empty oplog entry.

## Access Control

If the deployment enforces authentication/authorization, you must have
the `collMod` privilege in the collection's database.

The built-in role `dbAdmin` provides the required privileges.

## Example

The following example hides an existing index.

First, use `db.collection.createIndex()` to create an index
without hiding:

```javascript
db.restaurants.createIndex( { borough: 1, ratings: 1 } );
```

To hide the index, you can specify either the index key specification
document or the index name to the `db.collection.hideIndex()`
method. The following specifies the index name:

```javascript
db.restaurants.hideIndex( "borough_1_ratings_1" ); 
```

To verify, run `db.collection.getIndexes()` on the
`restaurants` collection:

```javascript
db.restaurants.getIndexes();
```

The operation returns the following information:

```javascript
[
   {
      "v" : 2,
      "key" : {
         "_id" : 1
      },
      "name" : "_id_"
   },
   {
      "v" : 2,
      "key" : {
         "borough" : 1,
         "ratings" : 1
      },
      "name" : "borough_1_ratings_1",
      "hidden" : true
   }
]
```

The `hidden` index option is only returned if the value is `true`.

**See also:**

- `db.collection.unhideIndex()`
- db.collection.createIndex()
