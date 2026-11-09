<!-- Converted from core/sharding-find-shard-key.txt (reStructuredText). Includes are inlined. -->

# Find a Shard Key

Every shared collection has a shard key. To
display the shard key, connect to a `mongos` instance and run
the `db.printShardingStatus()` method:

```javascript
db.printShardingStatus()
```

The output resembles:

```javascript
<dbname>.<collection>
   shard key: { <shard key> : <1 or hashed> }
   unique: <boolean>
   balancing: <boolean>
   chunks:
      <shard name1> <number of chunks>
      <shard name2> <number of chunks>
      ...
   { <shard key>: <min range1> } -->> { <shard key> : <max range1> } on : <shard name> <last modified timestamp>
   { <shard key>: <min range2> } -->> { <shard key> : <max range2> } on : <shard name> <last modified timestamp>
   ...
   tag: <tag1>  { <shard key> : <min range1> } -->> { <shard key> : <max range1> }
   ...
```

For more details on the `db.printShardingStatus()` output, see the
sharded collection section
on the `sh.status()` page.
