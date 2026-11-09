<!-- Converted from tutorial/manage-indexes.txt (reStructuredText). Includes are inlined. -->

# Manage Indexes

This page shows how to manage existing indexes. For instructions on
creating indexes, refer to the specific index type pages.

## View Existing Indexes

tabs:
  - id: shell
    content: |

      The following sections provide methods for viewing existing indexes
      on a collection or an entire database.

      List All Indexes on a Collection
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      To return a list of all indexes on a collection, use the
      `db.collection.getIndexes()` method or a similar `method
      for your driver`.

      For example, to view all indexes on the `people` collection, run the
      following command:

      ```javascript
      db.people.getIndexes()
      ```

      List All Indexes for a Database
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      To list all the collection indexes in a database, run the following
      command in `mongosh`:

      ```javascript
      db.getCollectionNames().forEach(function(collection) {
          indexes = db[collection].getIndexes();
          print("Indexes for " + collection + ":");
          printjson(indexes);
      });
      ```

      List Specific Type of Indexes
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      To list all indexes of a certain type (such as hashed or text) for all
      collections in all database, run the following command in
      `mongosh`:

      ```javascript
      // The following finds all hashed indexes

      db.adminCommand("listDatabases").databases.forEach(function(d){
          let mdb = db.getSiblingDB(d.name);
          mdb.getCollectionInfos({ type: "collection" }).forEach(function(c){
            let currentCollection = mdb.getCollection(c.name);
            currentCollection.getIndexes().forEach(function(idx){
              let idxValues = Object.values(Object.assign({}, idx.key));

              if (idxValues.includes("hashed")) {
                print("Hashed index: " + idx.name + " on " + d.name + "." + c.name);
                printjson(idx);
              };
            }); 
          });
      });
      ```

  - id: compass
    content: |
      To view a list of all indexes on a collection in MongoDB Compass,
      click on the target collection in the left-hand pane and
      select the Indexes tab.

      (Figure: /images/compass-index-tab-2.png)

      For details on the information displayed in this tab, refer to
      the `Compass documentation`.

## Remove Indexes

**Tip:** Hide an Index Before Dropping It

If you drop an index that is actively used in production, your
application may incur a performance degradation. Before you drop an
index, you can evaluate the potential impact of the drop by
hiding the index.

Hidden indexes are not used to support queries. If you hide an index
and observe substantial negative performance impact, consider keeping
and unhiding the index so queries can resume using it.

tabs:
  - id: shell
    content: |

      When removing indexes in the MongoDB Shell, you can either:

      - Remove a specific index.

      - Remove all indexes from the collection.

      Remove Specific Index
      ~~~~~~~~~~~~~~~~~~~~~

      To remove an index, use the `db.collection.dropIndex()` method.

      For example, the following operation removes an ascending index on the
      `tax-id` field in the `accounts` collection:

      ```javascript
      db.accounts.dropIndex( { "tax-id": 1 } )
      ```

      The operation returns a document with the status of the operation:

      ```javascript
      { "nIndexesWas" : 3, "ok" : 1 }
      ```

      Where the value of `nIndexesWas` reflects the number of indexes
      *before* removing this index.

      For text indexes, pass the index name to the
      `db.collection.dropIndex()` method. See drop-text-index
      for details.

      **Note:**

      `db.collection.dropIndexes()` can accept an array
      of index names.

      `db.collection.dropIndexes()` can stop
      in-progress index builds. See dropIndexes-method-index-builds 
      for more information.

      Remove All Indexes
      ~~~~~~~~~~~~~~~~~~

      You can also use the `db.collection.dropIndexes()` to remove
      *all* indexes except for the _id index from a
      collection.

      For example, the following command removes all indexes from
      the `accounts` collection:

      ```javascript
      db.accounts.dropIndexes()
      ```

      These shell helpers provide wrappers around the
      `dropIndexes` database command. Your `client
      library` may have a different or additional
      interface for these operations.

  - id: compass
    content: |

      To remove an index from a collection in MongoDB Compass:

      1. Navigate to the collection containing the target index.

      2. Click the Indexes tab.

      3. In the Drop column for the target index, click
         the trash icon.

      (Figure: /images/compass-delete-index.png)

## Modify an Index

tabs:
  - id: shell
    content: |
      To modify an existing index in the MongoDB Shell, you need to
      drop and recreate the index. The exception to this rule is
      TTL indexes, which can be modified
      via the `collMod` command in conjunction with the
      `index` collection flag.

  - id: compass
    content: |
      To modify an existing index in MongoDB Compass, you need to drop and
      recreate the index.

### Minimize Performance Impact With a Temporary Index

If you drop an index that is actively used in production, your
application may incur a performance degradation. To ensure queries can
still use an index during modification, you can create a temporary,
redundant index that contains the same fields as the modified index.

#### Example

This example creates a new index and modifies that index to make it
unique.

**Step 1: Create a `siteAnalytics` collection with an index on the `url` field**

Run this command:

```javascript
db.siteAnalytics.createIndex( { "url": 1 } )
```

The command returns the name of the index:

```javascript
url_1
```

**Step 2: Create a temporary index that contains the `url` field**

Run this command:

```javascript
db.siteAnalytics.createIndex( { "url": 1, "dummyField": 1 } )
```

The command returns the name of the index:

```javascript
url_1_dummyField_1
```

This temporary index lets you safely drop the original ``{ "url":
1 }`` index without impacting performance.

**Step 3: Drop the original index**

Run this command:

```javascript
db.siteAnalytics.dropIndex( { "url": 1 } )
```

The command returns:

```javascript
{ nIndexesWas: 3, ok: 1 } 
```

**Step 4: Recreate the `{ "url": 1 }` index with the `unique` property**

Run this command:

```javascript
db.siteAnalytics.createIndex( { "url": 1 }, { "unique": true } )
```

The command returns the name of the index:

```javascript
url_1
```

The `url_1` index is recreated and you can drop the temporary
index without impacting performance. Queries on the `url` field
can use the new unique index.

**Step 5: Drop the temporary index**

Run this command:

```javascript
db.siteAnalytics.dropIndex( { "url": 1, "dummyField": 1 } )
```

The command returns:

```javascript
{ nIndexesWas: 3, ok: 1 } 
```

**Step 6: Confirm that the index was updated**

To view the indexes on the `siteAnalytics` collection, run this
command:

```javascript
db.siteAnalytics.getIndexes()
```

The command returns these indexes, indicating that the `url_1`
index is now unique:

```javascript
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { url: 1 }, name: 'url_1', unique: true }
]       
```

## Find Inconsistent Indexes Across Shards

A sharded collection has an inconsistent index if the collection does
not have the exact same indexes (including the index options) on each
shard that contains chunks for the collection. Although inconsistent
indexes should not occur during normal operations, inconsistent indexes
can occur , such as:

- When a user is creating an index with a `unique` key constraint and
  one shard contains a chunk with duplicate documents. In such cases,
  the create index operation may succeed on the shards without
  duplicates but not on the shard with duplicates.
  
- When a user is creating an index across the shards in a rolling
  manner (i.e. manually building the index one by one across the
  shards) but either
  fails to build the index for an associated shard or incorrectly
  builds an index with different specification.

The config server primary, by default, checks 
for index inconsistencies across the shards for sharded collections, and
the command `serverStatus`, when run on the config server
primary, returns the field `shardedIndexConsistency`
field to report on the number of sharded collections with index
inconsistencies.

If `shardedIndexConsistency` reports any index
inconsistencies, you can run the following pipeline for your
sharded collections until you find the inconsistencies.

#. Define the following aggregation pipeline:

   ```javascript
   const pipeline = [
       // Get indexes and the shards that they belong to.
       {$indexStats: {}},
       // Attach a list of all shards which reported indexes to each document from $indexStats.
       {$group: {_id: null, indexDoc: {$push: "$$ROOT"}, allShards: {$addToSet: "$shard"}}},
       // Unwind the generated array back into an array of index documents.
       {$unwind: "$indexDoc"},
       // Group by index name.
       {
           $group: {
               "_id": "$indexDoc.name",
               "shards": {$push: "$indexDoc.shard"},
               // Convert each index specification into an array of its properties 
               // that can be compared using set operators.
               "specs": {$push: {$objectToArray: {$ifNull: ["$indexDoc.spec", {}]}}},
               "allShards": {$first: "$allShards"}
           }
       },
       // Compute which indexes are not present on all targeted shards and 
       // which index specification properties aren't the same across all shards.
       {
           $project: {
               missingFromShards: {$setDifference: ["$allShards", "$shards"]},
               inconsistentProperties: {
                    $setDifference: [
                        {$reduce: {
                            input: "$specs",
                            initialValue: {$arrayElemAt: ["$specs", 0]},
                            in: {$setUnion: ["$$value", "$$this"]}}},
                        {$reduce: {
                            input: "$specs",
                            initialValue: {$arrayElemAt: ["$specs", 0]},
                            in: {$setIntersection: ["$$value", "$$this"]}}}
                    ]
                }
           }
       },
       // Only return output that indicates an index was inconsistent, i.e. either a shard was missing
       // an index or a property on at least one shard was not the same on all others.
       {
           $match: {
               $expr:
                   {$or: [
                       {$gt: [{$size: "$missingFromShards"}, 0]},
                       {$gt: [{$size: "$inconsistentProperties"}, 0]},
                   ]
               }
           }
       },
       // Output relevant fields.
       {$project: {_id: 0, indexName: "$$ROOT._id", inconsistentProperties: 1, missingFromShards: 1}}
   ];
   ```

#. Run the aggregation pipeline for the sharded collection to test. For
   example, to test if the sharded collection `test.reviews` has
   inconsistent indexes across its associated shards:

   ```javascript
   db.getSiblingDB("test").reviews.aggregate(pipeline)
   ```

   If the collection has inconsistent indexes, the aggregation for that
   collection returns details regarding the inconsistent indexes:

   ```javascript
   { "missingFromShards" : [ "shardB" ], "inconsistentProperties" : [ ], "indexName" : "page_1_score_1" }
   { "missingFromShards" : [ ], "inconsistentProperties" : [ { "k" : "expireAfterSeconds", "v" : 60 }, { "k" : "expireAfterSeconds", "v" : 600 } ], "indexName" : "reviewDt_1" }
   ```

   The returned documents indicate two inconsistencies for the sharded
   collection `test.reviews`:

   #. An index named `page_1_score_1` is missing from the collection
      on `shardB`.

   #. An index named `reviewDt_1` has inconsistent properties across
      the collection's shards, specifically, the `expireAfterSeconds`
      properties differ.

To resolve the inconsistency where an index is missing  from the collection on a particular shard(s),
   You can either:

   - Issue an index build `db.collection.createIndex()` from a
     `mongos` instance. The operation only builds the
     collection's index on the shard(s) missing the index.

     \-OR-

   - Perform a rolling index build for the collection
     on the affected shard(s).

     **Note:**

     Rolling indexes may negatively impact your deployment. For
     information on when to use this index build, see
     rolling-index-build.

To resolve where the index properties differ across the shards, 
   Drop the incorrect index from the collection on the affected
   shard(s) and rebuild the index. To rebuild the index, you can either:

   - Issue an index build `db.collection.createIndex()` from a
     `mongos` instance. The operation only builds the
     collection's index on the shard(s) missing the index.

     \-OR-

   - Perform a rolling index build for the collection
     on the affected shard.

     **Note:**

     Rolling indexes may negatively impact your deployment. For
     information on when to use this index build, see
     rolling-index-build.

   Alternatively, if the inconsistency is the `expireAfterSeconds` property,
   you can run the `collMod` command to update the number of
   seconds instead of dropping and rebuilding the index.
