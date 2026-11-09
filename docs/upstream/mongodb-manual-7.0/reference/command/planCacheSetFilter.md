<!-- Converted from reference/command/planCacheSetFilter.txt (reStructuredText). Includes are inlined. -->

# planCacheSetFilter (database command)

## Definition

**`planCacheSetFilter`**

Set an index filter for a collection. If
an index filter already exists for the query shape, the
command overrides the previous index filter.

## Compatibility

This command is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
      planCacheSetFilter: <collection>,
      query: <query>,
      sort: <sort>,
      projection: <projection>,
      collation: { <collation> },
      indexes: [ <index1>, <index2>, ...],
      comment: <any>
   }
)
```

The query shape for the index filter is the combination of:

- `query`
- `sort`
- `projection`
- `collation`

## Command Fields

The command has the following fields:

* - Field
  - Type
  - Description

* - `planCacheSetFilter`
  - string
  - The name of the collection for the index filter.

* - `query`
  - document
  - The query predicate for the index filter.

    Only the predicate structure, including the field names,
    is used in the index filter. The field values in the query
    predicate are not used. Therefore, the query predicate in an
    index filter is used by similar queries that differ only in the
    field values.

* - `sort`
  - document
  - Optional. The sort for the index filter.

* - `projection`
  - document
  - Optional. The projection for the index filter.

* - `collation` 
  - document
  - .. include:: /includes/extracts/collation-option.rst

    Starting in MongoDB 6.0, an index filter uses the collation previously set using the `planCacheSetFilter`
    command.

* - `indexes`   
  - array
  - An array of index filters for the specified query shape.

    Specify the index filters as one of these arrays:

    - Index specification documents. For example, ``[ { x : 1 }, ...
      ]``.
    - Index names. For example, `[ "x_1", ... ]`.

    The query optimizer uses either a
    collection scan or the index arrays for the query plan. If the
    specified indexes do not exist or are hidden, the optimizer uses a collection scan.

    For multiple indexes with the same key pattern, you must 
    specify the index as an array of names.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

Index filters only exist for the duration of the server process and do
not persist after shutdown. To clear the index filters, use the
`planCacheClearFilters` command.

## Required Access

A user must have access that includes the
`planCacheIndexFilter` action.

## Examples

### Set Filter on Query Shape Consisting of Predicate Only

The following example creates an index filter on the `orders`
collection such that for queries that consist only of an equality
match on the `status` field without any projection and sort, the
query optimizer evaluates only the two specified indexes and the
collection scan for the winning plan:

```javascript
db.runCommand(
   {
      planCacheSetFilter: "orders",
      query: { status: "A" },
      indexes: [
         { cust_id: 1, status: 1 },
         { status: 1, order_date: -1 }
      ]
   }
)
```

In the query predicate, only the structure of the predicate, including
the field names, are significant; the values are insignificant. As
such, the created filter applies to the following operations:

```javascript
db.orders.find( { status: "D" } )
db.orders.find( { status: "P" } )
```

To see whether MongoDB will apply an index filter for a query shape,
check the `indexFilterSet` field of either
the `db.collection.explain()` or the `cursor.explain()`
method.

### Set Filter on Query Shape Consisting of Predicate, Projection, and Sort

The following example creates an index filter for the `orders`
collection. The filter applies to queries whose predicate is an
equality match on the `item` field, where only the `quantity` field
is projected and an ascending sort by `order_date` is specified.

```javascript
db.runCommand(
   {
      planCacheSetFilter: "orders",
      query: { item: "ABC" },
      projection: { quantity: 1, _id: 0 },
      sort: { order_date: 1 },
      indexes: [
         { item: 1, order_date: 1 , quantity: 1 }
      ]
   }
)
```

For the query shape, the query optimizer will only consider indexed
plans which use the index `{ item: 1, order_date: 1, quantity: 1 }`.

### Set Filter on Query Shape Consisting of Predicate and Collation

The following example creates an index filter for the `orders`
collection. The filter applies to queries whose predicate is an equality
match on the `item` field and the collation `en_US` (English United
States).

```javascript
db.runCommand(
   {
      planCacheSetFilter: "orders",
      query: { item: "Movie" },
      collation: { locale: "en_US" },
      indexes: [
         { item: 1, order_date: 1 , quantity: 1 }
      ]
   }
)
```

For the query shape, the query optimizer only uses indexed plans that
use the index `{ item: 1, order_date: 1, quantity: 1 }`.

Starting in MongoDB 6.0, an index filter uses the collation previously set using the `planCacheSetFilter`
command.

**See also:**

- `planCacheClearFilters`
- `planCacheListFilters`
- `$planCacheStats`
