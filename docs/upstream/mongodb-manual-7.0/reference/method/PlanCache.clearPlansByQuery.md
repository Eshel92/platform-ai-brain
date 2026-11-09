<!-- Converted from reference/method/PlanCache.clearPlansByQuery.txt (reStructuredText). Includes are inlined. -->

# PlanCache.clearPlansByQuery() (mongosh method)

## Definition

**`PlanCache.clearPlansByQuery( <query>, <projection>, <sort> )`**

Clears the cached query plans for the specified query shape.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `planCacheClear` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The method is only available from the `plan cache object` of a specific collection; i.e.

```javascript
db.collection.getPlanCache().clearPlansByQuery( <query>, <projection>, <sort>, <collation> )
```

The `PlanCache.clearPlansByQuery()` method accepts the
following parameters:

| Parameter | Type | Description |
|---|---|---|
| `query` | document | The query predicate of the query shape. Only the structure of the predicate, including the field names, are significant to the shape; the values in the query predicate are insignificant. |
| `projection` | document | Optional. The projection associated with the query shape. Required if specifying the `sort` parameter. |
| `sort` | document | Optional. The sort associated with the query shape. |
| `collation` | document | .. include:: /includes/extracts/collation-option.rst |

To see the query shapes for which cached query plans exist, see
planCacheStats-examples.

## Required Access

On systems running with `authorization`, a user must have access that
includes the `planCacheWrite` action.

## Example

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

The following operation removes the query plan cached for the shape:

```javascript
db.orders.getPlanCache().clearPlansByQuery(
   { "qty" : { "$gt" : 10 } },
   { },
   { "ord_date" : 1 },
   { locale: "fr" }
)
```

**See also:**

- `db.collection.getPlanCache()`
- `PlanCache.listQueryShapes()`
- `PlanCache.clear()`
