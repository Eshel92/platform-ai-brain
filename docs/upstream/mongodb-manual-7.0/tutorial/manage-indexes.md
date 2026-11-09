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
      `db.collection.getIndexes()` method or a similar 
      `method for your driver`.

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

      To list all indexes of a certain type (such as hashed or text) for 
      all collections in all database, run the following command in
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
      the Compass documentation.

## Remove Indexes

**Tip:** Hide an Index Before Dropping It

If you drop an index that is actively used in production, your
application may incur a performance degradation. Before you drop an
index, you can evaluate the potential impact of the drop by
hiding the index.

Hidden indexes are not used to support queries. If you hide an index
and observe substantial negative performance impact, consider keeping
and unhiding the index so queries can resume using it.

To learn how to remove an existing index, see drop-an-index.

To learn how to remove an index in MongoDB Compass, see `Manage Indexes in Compass`.

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

To convert a non-unique index to a unique index with the
`collMod` command, see index-convert-to-unique.

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
db.siteAnalytics.dropIndex( { "url_1" } )
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
db.siteAnalytics.dropIndex( { "url_1_dummyField_1" } )
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
can occur, such as:

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
inconsistencies, you can run the `checkMetadataConsistency`
command with `checkIndexes: true` for your sharded collections to 
find the inconsistencies.

#. Run the `checkMetadataConsistency` command:

   ```javascript
   db.runCommand( {
      checkMetadataConsistency: 1,
      checkIndexes: true
   } )
   ```

#. If the collection has inconsistent indexes, the `checkMetadataConsistency` 
   command returns details regarding the inconsistent indexes similar to the
   following:

   ```javascript
   {
     cursor: {
       id: Long('0'),
       ns: 'test.$cmd.aggregate',
       firstBatch: [
         {
           type: 'InconsistentIndex',
           description: 'Found an index of a sharded collection that is inconsistent between different shards',
           details: {
             namespace: 'test.reviews',
             info: { 
               missingFromShards: [],
               inconsistentProperties: [
                 { k: 'expireAfterSeconds', v: Long('600') },
                 { k: 'expireAfterSeconds', v: 3600 }
               ],
               indexName: 'reviewDt_1'
             }
           }
         },
         {
           type: 'InconsistentIndex',
           description: 'Found an index of a sharded collection that is inconsistent between different shards',
           details: {
             namespace: 'test.reviews',
             info: {
               missingFromShards: [ 'shard02' ],
               inconsistentProperties: [],
               indexName: 'page_1_score_1'
             }
           }
         }
       ]
     },
     ok: 1,
     '$clusterTime': {
       clusterTime: Timestamp({ t: 1752574769, i: 1 }),
       signature: {
         hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
         keyId: Long('0')
       }
     },
     operationTime: Timestamp({ t: 1752574760, i: 1 })
   }
   ```

   The output indicates two inconsistencies for the sharded
   collection `test.reviews`:

   #. An index named `reviewDt_1` has inconsistent properties across
      the collection's shards, specifically, the `expireAfterSeconds`
      properties differ.

   #. An index named `page_1_score_1` is missing from the collection
      on `shard02`.

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

**Warning:**

Avoid performing rolling index and replicated index build processes
concurrently as it might lead to unexpected issues, such as broken 
builds and crash loops.

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
