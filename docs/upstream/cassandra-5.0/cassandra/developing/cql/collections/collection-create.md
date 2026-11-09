<!-- Converted from modules/cassandra/pages/developing/cql/collections/collection-create.adoc (AsciiDoc). Includes are inlined. -->

# Creating collections

CQL defines the following collection data types:

* set: store unordered items
* list: store ordered items
* map: store key-value pairs

Collections are intended for insertion and retrieval as a collection. 
Thus, {product} reads collections in their entirety, and can affect retrieval performance.
A good rule of thumb is that sets are more performant than lists, so use a set if you can.
Collections should be smaller than the following maximum size to prevent querying delays.

Guard rails for non-frozen collections:

* No more than 2 billion items in a collection.
* Maximum size of an item in a `set` is 65,535 bytes.
* Maximum size of an item in a `list` or `map` is 2 GB.
* Maximum number of keys in a `map` is 65,535.
* Lists can incur a read-before-write operation for some insertions.

**Important:**
Collections are not paged internally.

Collections cannot be _sliced_;

**Note:**
The limits specified for collections are for non-frozen collections.

'''
