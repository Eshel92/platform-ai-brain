<!-- Converted from reference/command/planCacheListFilters.txt (reStructuredText). Includes are inlined. -->

# planCacheListFilters (database command)

## Definition

**`planCacheListFilters`**

Lists the index filters associated with
query shapes for a collection.

:returns:

   Document listing the index filters. See
   planCacheListFilters-output.

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
     planCacheListFilters: <collection> 
   } 
)
```

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `planCacheListFilters` | string | The name of the collection. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Required Access

A user must have access that includes the
`planCacheIndexFilter` action.

## Output

The `planCacheListFilters` command returns the document with
the following form:

```none
{
   "filters" : [
      {
         "query" : <query>
         "sort" : <sort>,
         "projection" : <projection>,
         "collation" : <collation>,
         "indexes" : [
            <index1>,
            ...
         ]
      },
      ...
   ],
   "ok" : 1
}
```

**`planCacheListFilters.filters`**

The array of documents that contain the index filter information.

Each document contains the following fields:

**`planCacheListFilters.filters.query`**

The query predicate associated with this filter. Although the
`query` shows the specific
values used to create the index filter, the values in the
predicate are insignificant; i.e. query predicates cover similar
queries that differ only in the values.

For instance, a `query`
predicate of `{ "type": "electronics", "status" : "A" }` covers
the following query predicates:

```javascript
{ type: "food", status: "A" }
{ type: "utensil", status: "D" }
```

**`planCacheListFilters.filters.sort`**

The sort associated with this filter. Can be an empty document.

**`planCacheListFilters.filters.projection`**

The projection associated with this filter. Can be an empty
document.

**`planCacheListFilters.filters.collation`**

The collation associated with this filter. Can
be an empty document.

**`planCacheListFilters.filters.indexes`**

The array of indexes for the query shape.

The query shape is the combination of these fields:

- `query`
- `sort`
- `projection`
- `collation`

To choose the best query plan, the query optimizer evaluates the
`indexes` *and* the collection
scan.

**`planCacheListFilters.ok`**

The status of the command.

**See also:**

- `planCacheClearFilters`
- `planCacheSetFilter`
