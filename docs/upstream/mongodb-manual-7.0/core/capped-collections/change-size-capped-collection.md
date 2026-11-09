<!-- Converted from core/capped-collections/change-size-capped-collection.txt (reStructuredText). Includes are inlined. -->

# Change the Size of a Capped Collection

**New in version:** 6.0

To change the size of a capped collection, use the `collMod` command's
`cappedSize` option. `cappedSize` is specified in bytes, and must be
greater than `0` and less than or equal to `1024^5` (1 PB (petabyte)).

If `cappedSize` is less than the current size of the collection,
MongoDB removes the excess documents on the next insert operation.

## About this Task

Generally, TTL (Time To Live) indexes offer
better performance and more flexibility than capped collections. TTL
indexes expire and remove data from normal collections based on the
value of a date-typed field and a TTL value for the index.

Capped collections serialize write operations and therefore have worse 
concurrent insert, update, and delete performance than non-capped 
collections. Before you create a capped collection, consider if you 
can use a TTL index instead.

## Before you Begin

Create a capped collection called `log` that has a maximum size of
2,621,440 bytes:

```javascript
db.createCollection( "log", { capped: true, size: 2621440 } )
```

## Steps

Run the following command to set the maximum size of the `log`
collection to 5,242,880 bytes:

```javascript
db.runCommand( { collMod: "log", cappedSize: 5242880 } )
```

## Learn More

- capped-collections-change-max-docs

- capped-collections-check

- capped-collections-query
