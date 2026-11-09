<!-- Converted from core/capped-collections/convert-collection-to-capped.txt (reStructuredText). Includes are inlined. -->

# Convert a Collection to Capped

To convert a non-capped collection to a capped collection, use the `convertToCapped`
database command.

The `convertToCapped` command holds a database-exclusive lock for the
duration of the operation. Other operations that lock the same database
are blocked until the `convertToCapped` operation completes.

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

Create a non-capped collection called `log2`:

```javascript
db.createCollection("log2")
```

## Steps

**Step 1: Convert the collection to a capped collection**

To convert the `log2` collection to a capped collection, run the
`convertToCapped` command:

```javascript
db.runCommand( {
   convertToCapped: "log2",
   size: 100000
} )
```

The `log2` collection has a maximum size of 100,000 bytes.

**Step 2: Confirm that the collection is capped**

To confirm that the `log2` collection is now capped, use the
`isCapped()` method:

```javascript
db.log2.isCapped()
```

Output:

```javascript
   true
```

## Learn More

- faq-concurrency-database-lock

- capped-collections-change-size

- capped-collections-query
