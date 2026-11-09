<!-- Converted from core/index-intersection.txt (reStructuredText). Includes are inlined. -->

# Index Intersection

**Important:**

This page documents cases where the query optimizer  **may** be able to use index intersection. 

In practice, the query optimizer rarely 
selects plans that use index intersection.

Hash-based index intersection is disabled by default and sort-based 
index intersection is disfavored in plan selection. The optimizer 
behaves in this fashion in order to prevent bad plan selection. 

Schema designs should not rely on index intersection. Instead,
compound indexes should be used.

Future improvements to the query optimizer may allow the system to 
better identify cases where an index intersection plan would be 
beneficial.

MongoDB can use the intersection of multiple indexes to fulfill
queries. In general, each index intersection involves two indexes; 
however, MongoDB can employ multiple/nested index intersections to 
resolve a query.

To illustrate index intersection, consider a collection `orders` that
has the following indexes:

```javascript
{ qty: 1 }
{ item: 1 }
```

MongoDB can use the intersection of the two indexes to support
the following query:

```javascript
db.orders.find( { item: "abc123", qty: { $gt: 15 } } )
```

To determine if MongoDB used index intersection, run
`explain()`; the results of explain() will include either an
`AND_SORTED` stage or an `AND_HASH` stage.

## Index Prefix Intersection

With index intersection, MongoDB can use an intersection of either the
entire index or the index prefix. An index prefix is a subset of a
compound index, consisting of one or more keys starting from the
beginning of the index.

Consider a collection `orders` with the following indexes:

```javascript
{ qty: 1 }
{ status: 1, ord_date: -1 }
```

To fulfill the following query which specifies a condition on both the
`qty` field and the `status` field, MongoDB can use the
intersection of the two indexes:

```javascript
db.orders.find( { qty: { $gt: 10 } , status: "A" } )
```

## Index Intersection and Compound Indexes

Index intersection does not eliminate the need for creating
compound indexes. However, because both
the list order (i.e. the order in which the keys are listed in the
index) and the sort order (i.e. ascending or descending), matter in
compound indexes, a compound index may
not support a query condition that does not include the index
prefix keys or that specifies a different sort
order. 

**Note:**

For deployments hosted on MongoDB Atlas, consider using 
Atlas Search indexes
to avoid limitations due to field order.

For example, if a collection `orders` has the following compound
index, with the `status` field listed before the `ord_date` field:

```javascript
{ status: 1, ord_date: -1 }
```

The compound index can support the following queries:

```javascript
db.orders.find( { status: { $in: ["A", "P" ] } } )
db.orders.find(
   {
     ord_date: { $gt: new Date("2014-02-01") },
     status: {$in:[ "P", "A" ] }
   }
)
```

But not the following two queries:

```javascript
db.orders.find( { ord_date: { $gt: new Date("2014-02-01") } } )
db.orders.find( { } ).sort( { ord_date: 1 } )
```

However, if the collection has two separate indexes:

```javascript
{ status: 1 }
{ ord_date: -1 }
```

The two indexes can, either individually or through index intersection,
support all four aforementioned queries.

The choice between creating compound indexes that support your queries
or relying on index intersection depends on the specifics of your
system.

**See also:**

- compound indexes
- compound-key-indexes

## Index Intersection and Sort

Index intersection does not apply when the `sort()`
operation requires an index completely separate from the query
predicate.

For example, the `orders` collection has the following indexes:

```javascript
{ qty: 1 }
{ status: 1, ord_date: -1 }
{ status: 1 }
{ ord_date: -1 }
```

MongoDB cannot use index intersection for the following query with sort:

```javascript
db.orders.find( { qty: { $gt: 10 } } ).sort( { status: 1 } )
```

That is, MongoDB does not use the `{ qty: 1 }` index for the query,
and the separate `{ status: 1 }` or the ``{ status: 1, ord_date: -1
}`` index for the sort.

However, MongoDB can use index intersection for the following query
with sort since the index `{ status: 1, ord_date: -1 }` can fulfill
part of the query predicate.

```javascript
db.orders.find( { qty: { $gt: 10 } , status: "A" } ).sort( { ord_date: -1 } )
```

## Index Intersection and Atlas Search Indexes

If you use MongoDB Atlas, you can create an Atlas Search index to
fulfill queries when the query optimizer selects a plan that involves 
index intersection. Unlike compound indexes, fields in Atlas Search indexes 
can be defined in any order. As a result, the Atlas Seach index can 
support queries that:

- Specify a different sort order than the index sort order.
- Contain fields that are not part of the index prefix.

For a tutorial on using Atlas Search indexes when index 
intersection is required, see [Flexible Querying with Atlas Search](https://www.mongodb.com/developer/products/atlas/flexible-querying-with-atlas-search/).

**Note:**

Atlas Search Indexes are only available for MongoDB Atlas clusters,
and is not available for self-managed deployments. To 
learn more, see:

- Atlas Search Overview
- Atlas Search Index Definitions
