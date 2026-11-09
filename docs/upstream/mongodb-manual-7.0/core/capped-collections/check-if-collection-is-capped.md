<!-- Converted from core/capped-collections/check-if-collection-is-capped.txt (reStructuredText). Includes are inlined. -->

# Check if a Collection is Capped

To check if a collection is capped, use the
`isCapped()` method.

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

Create a non-capped collection and a capped collection:

```javascript
db.createCollection("nonCappedCollection1")

db.createCollection("cappedCollection1", { capped: true, size: 100000 } )
```

   

## Steps

To check if the collections are capped, use the
`isCapped()` method:

```javascript
db.nonCappedCollection1.isCapped()

db.cappedCollection1.isCapped()
```

Output:

```javascript
false
true
```

## Learn More

- capped-collections-create

- capped-collections-convert

- `$collStats`
