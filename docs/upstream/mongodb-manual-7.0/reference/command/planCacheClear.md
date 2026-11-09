<!-- Converted from reference/command/planCacheClear.txt (reStructuredText). Includes are inlined. -->

# planCacheClear (database command)

## Definition

**`planCacheClear`**

Removes cached query plans for a collection. Specify a query
shape to remove cached query plans for that shape. Omit the query
shape to clear all cached query plans.

   `PlanCache.clearPlansByQuery` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `PlanCache.clear` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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
      planCacheClear: <collection>,
      query: <query>,
      sort: <sort>,
      collation: <collation>,
      projection: <projection>,
      comment: <any>
   }
)
```

## Command Fields

The command takes the following optional fields:

| Field | Type | Description |
|---|---|---|
| `query` | document | Optional. The query predicate of the query shape. Only the structure of the predicate, including the field names, are significant to the shape; the values in the query predicate are insignificant. |
| `projection` | document | Optional. The projection associated with the query shape. |
| `sort` | document | Optional. The sort associated with the query shape. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |
| `collation` | document | .. include:: /includes/extracts/collation-option.rst |

To see the query shapes for which cached query plans exist, see
planCacheStats-examples.

## Required Access

On systems running with `authorization`, a user must have access that
includes the `planCacheWrite` action.

## Examples

### Clear Cached Plans for a Query Shape

If a collection `orders` has the following query shape:

```javascript
{
  "query" : { "qty" : { "$gt" : 10 } },
  "sort" : { "ord_date" : 1 },
  "collation" : { locale : "fr" },
  "projection" : { },
  "queryHash" : "9AAD95BE" 
}
```

The following operation clears the query plan cached for the shape:

```javascript
db.runCommand(
   {
      planCacheClear: "orders",
      query: { "qty" : { "$gt" : 10 } },
      sort: { "ord_date" : 1 },
      collation: { locale : "fr" }
   }
)
```

### Clear All Cached Plans for a Collection

The following example clears all the cached query plans for the
`orders` collection:

```javascript
db.runCommand(
   {
      planCacheClear: "orders"
   }
)
```

**See also:**

- `PlanCache.clearPlansByQuery()`
- `PlanCache.clear()`
