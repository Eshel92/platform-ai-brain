<!-- Converted from core/index-hashed.txt (reStructuredText). Includes are inlined. -->

# Hashed Indexes

Hashed indexes maintain entries with hashes of the values of the
indexed field.

Hashed indexes support sharding
using hashed shard keys. Hashed based sharding uses a hashed index of a field as the shard
key to partition data across your sharded cluster.

Using a hashed shard key to shard a collection results in a more even
distribution of data. See sharding-hashed-sharding for more
details.

## Hashing Function

Hashed indexes use a hashing function to compute the hash of the value
of the index field. [#hashvalue]_ The hashing function collapses
embedded documents and computes the hash for the entire value but does
not support multi-key (i.e. arrays) indexes. Specifically, creating a
hashed index on a field that contains an array *or* attempting to insert
an array into a hashed indexed field returns an error.

**Tip:**

MongoDB automatically computes the hashes when resolving queries using
hashed indexes.  Applications do **not** need to compute hashes.

## Create a Hashed Index

To create a hashed index, specify
`hashed` as the value of the index key, as in the following
example:

```javascript
db.collection.createIndex( { _id: "hashed" } )
```

## Create a Compound Hashed Index

**New in version:** 4.4

Starting with MongoDB 4.4, MongoDB supports creating compound indexes
that include a single hashed field. To create a compound hashed index,
specify `hashed` as the value of any single index key when creating
the index:

```javascript
db.collection.createIndex( { "fieldA" : 1, "fieldB" : "hashed", "fieldC" : -1 } )
```

Compound hashed indexes require featureCompatibilityVersion set to `4.4`. 

**See also:**

sharding-hashed-sharding

## Considerations

### Embedded Documents

The hashing function collapses embedded documents and computes the hash
for the entire value, but does not support multi-key (i.e. arrays)
indexes. Specifically, creating a hashed index on a field that contains
an array *or* attempting to insert an array to a hashed indexed field
returns an error.

### Unique Constraint

MongoDB does not support specifying a unique constraint on a `hashed`
index. You can instead create an additional non-hashed index with the
unique constraint on that field. MongoDB can use that non-hashed index
for enforcing uniqueness on the field.

### 2`53` Limit

**Warning:**

MongoDB `hashed` indexes truncate floating point numbers to 64-bit integers
before hashing. For example, a `hashed` index would store the same
value for a field that held a value of `2.3`, `2.2`, and `2.9`.
To prevent collisions, do not use a `hashed` index for floating
point numbers that cannot be reliably converted to 64-bit
integers (and then back to floating point). MongoDB `hashed` indexes do
not support floating point values larger than 2`53`.

To see what the hashed value would be for a key, see
`convertShardKeyToHashed()`.

### PowerPC and 2`63`

For hashed indexes, MongoDB 4.2 ensures
that the hashed value for the floating point value 2`63` on
PowerPC is consistent with other platforms. 

Although hashed indexes on a field that may
contain floating point values greater than 2`53` is an
unsupported configuration, clients may still insert documents where the
indexed field has the value 2`63`.

To list all `hashed` indexes for all
collections in your deployment, you can use the following
operation in `mongosh`:

```javascript
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

To check if the indexed field contains the value 2`63`, run the
following operation for the collection and the indexed field:

- If the indexed field type is a scalar and never a document:

  ```javascript
  // substitute the actual collection name for <collection>
  // substitute the actual indexed field name for <indexfield>

  db.<collection>.find( { <indexfield>: Math.pow(2,63) } );
  ```

- If the indexed field type is a document (or a scalar), you can run:

  ```javascript
  // substitute the actual collection name for <collection>
  // substitute the actual indexed field name for <indexfield>

  db.<collection>.find({
      $where: function() {
          function findVal(obj, val) {
              if (obj === val)
                  return true;

              for (const child in obj) {
                  if (findVal(obj[child], val)) {
                      return true;
                  }
              }
              return false;
          }
          return findVal(this.<indexfield>, Math.pow(2, 63));
      }
  })
  ```
