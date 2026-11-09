<!-- Converted from reference/method/db.collection.unhideIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.unhideIndex()

## Definition

**`db.collection.unhideIndex()`**

   `collMod` command

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `index.hidden` collection option set using the.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Unhides an existing index from the query planner. Once unhidden, the
indexes are immediately available for use.

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
db.collection.unhideIndex(<index>)
```

### Parameters

The `db.collection.unhideIndex()` method takes the following
parameter:

* - Parameter

  - Type

  - Description

* - `index`

  - string or document

  - Specifies the index to unhide from the query planner. You can
    specify the index either by the index name or by the index
    specification document.

    **Tip:**

    You can use the `db.collection.getIndexes()` method
    to find the index name or the index specification document.

    To unhide a text index, specify the
    index name.

The `db.collection.unhideIndex()` is a `mongosh` shell
wrapper for the `collMod` command.

## Behavior

### Index Modifications Reset Statistics

Unhiding a hidden index resets its `$indexStats`.

### No-op

Unhiding an already unhidden index has no effect on the index. However,
the operation will still generate an empty oplog entry.

## Required Access

If the deployment enforces authentication/authorization, you must have
the `collMod` privilege in the collection's database.

The built-in role `dbAdmin` provides the required privileges.

## Example

The following example unhides an existing index.

First, use `db.collection.createIndex()` to create a hidden
index:

```javascript
db.restaurants.createIndex( { borough: 1, ratings: 1 }, { hidden: true } );
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

The index option `hidden` is only returned if the value is `true`.

To unhide the index, you can specify either the index key specification
document or the index name to the `db.collection.unhideIndex()`
method. The following specifies the index name:

```javascript
db.restaurants.unhideIndex( "borough_1_ratings_1" );  
```

To verify, run `db.collection.getIndexes()` on the
`restaurants` collection:

```javascript
db.restaurants.getIndexes()
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
      "name" : "borough_1_ratings_1"
   }
]
```

The index option `hidden` no longer appears as part of the
`borough_1_ratings_1` index since the field is only returned if the
value is `true`.

**See also:**

- `db.collection.hideIndex()`
- db.collection.createIndex()
