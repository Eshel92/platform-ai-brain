<!-- Converted from reference/method/Bulk.insert.txt (reStructuredText). Includes are inlined. -->

# Bulk.insert()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.insert(<document>)`**

Adds an insert operation to a bulk operations list.

`Bulk.insert()` accepts the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `doc` | document | Document to insert. The size of the document must be less than or equal to the `maximum BSON document size`. |

          

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Behavior

### Insert Inaccuracies

Even if you encounter a server error during an insert, some documents 
may have been inserted. 

After a successful insert, the system returns `BulkWriteResult.nInserted`, the number 
of documents inserted into the collection. If the insert 
operation is interrupted by a replica set state change,
the system may continue inserting documents. As a result,
`BulkWriteResult.nInserted` may report fewer documents than actually inserted.

### Performance Consideration for Random Data

If an operation inserts a large amount of random data (for example,
hashed indexes) on an indexed field, insert performance may decrease.
Bulk inserts of random data create random index entries, which increase
the size of the index. If the index reaches the size that requires each
random insert to access a different index entry, the inserts result in a
high rate of WiredTiger cache eviction and replacement. When this
happens, the index is no longer fully in cache and is updated on disk,
which decreases performance.

To improve the performance of bulk inserts of random data on indexed
fields, you can either: 

- Drop the index, then recreate it after you insert the random data.
- Insert the data into an empty unindexed collection.

Creating the index after the bulk insert sorts the data in memory and
performs an ordered insert on all indexes. 

## Example

The following initializes a `Bulk()` operations builder for the
`items` collection and adds a series of insert operations to add
multiple documents:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.insert( { item: "abc123", defaultQty: 100, status: "A", points: 100 } );
bulk.insert( { item: "ijk123", defaultQty: 200, status: "A", points: 200 } );
bulk.insert( { item: "mop123", defaultQty: 0, status: "P", points: 0 } );
bulk.execute();
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.execute()`
