<!-- Converted from reference/command/planCacheClearFilters.txt (reStructuredText). Includes are inlined. -->

# planCacheClearFilters (database command)

## Definition

**`planCacheClearFilters`**

Removes index filters on a collection.
Although index filters only exist for the duration of the server
process and do not persist after shutdown, you can also clear
existing index filters with the `planCacheClearFilters`
command.

Specify the query shape to remove a specific index filter.
Omit the query shape to clear all index filters on a collection.

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
      planCacheClearFilters: <collection>,
      query: <query pattern>,
      sort: <sort specification>,
      projection: <projection specification>,
      collation: { <collation> },
      comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

* - Field
  - Type
  - Description

* - `planCacheClearFilters`
  - string
  - The name of the collection to remove the index filters from.

* - `query`
  - document
  - Optional. The query predicate for the index filter to
    remove. If omitted, the command clears all index filters from the
    collection.

    The values in the `query` predicate do not:

    - Determine the query shape.
    - Need to match the values returned by
      `planCacheListFilters`.

* - `sort`   
  - document
  - Optional. The sort for the index filter to remove, if any.

* - `projection`   
  - document
  - Optional. The projection for the index filter to remove, if any.

* - `collation` 
  - document
  - .. include:: /includes/extracts/collation-option.rst

    Starting in MongoDB 6.0, an index filter uses the collation previously set using the `planCacheSetFilter`
    command.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst
       

## Required Access

A user must have access that includes the
`planCacheIndexFilter` action.

## Examples

### Clear Specific Index Filter on Collection

The `orders` collection contains the following index filters:

```javascript
{
  "query" : { "status" : "A" },
  "sort" : { "ord_date" : -1 },
  "projection" : { },
  "indexes" : [ { "status" : 1, "cust_id" : 1 } ]
}

{
  "query" : { "status" : "A" },
  "sort" : { },
  "projection" : { },
  "indexes" : [ { "status" : 1, "cust_id" : 1 } ]
}

{
  "query": { "item": "Movie" },
  "collation": { locale: "en_US" },
  "indexes": [ { "item": 1, "order_date": 1 , "quantity": 1 } ]
}
```

**Note:**

Starting in MongoDB 6.0, an index filter uses the collation previously set using the `planCacheSetFilter`
command.

The following command removes the second index filter only:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders",
      query: { "status" : "A" }
   }
)
```

Because the values in the `query` predicate are insignificant in
determining the query shape, the following command would also
remove the second index filter:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders",
      query: { "status" : "P" }
   }
)
```

### Clear all Index Filters on a Collection

The following example clears all index filters on the `orders`
collection:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders"
   }
)
```

### Clear Index Filter Containing a Query and a Collation

The following example clears the index filter containing the query on
`Movie` and the collation `en_US` for the `orders` collection:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders",
      query: { item: "Movie" },
      collation: { locale: "en_US" }
   }
)
```

**See also:**

- `planCacheListFilters`
- `planCacheSetFilter`
