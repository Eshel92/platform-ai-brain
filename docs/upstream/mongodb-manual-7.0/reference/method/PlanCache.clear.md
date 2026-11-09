<!-- Converted from reference/method/PlanCache.clear.txt (reStructuredText). Includes are inlined. -->

# PlanCache.clear() (mongosh method)

## Definition

**`PlanCache.clear()`**

Removes all cached query plans for a collection.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `planCacheClear` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The method is only available from the `plan cache object` of a specific collection; i.e.

```javascript
db.collection.getPlanCache().clear()
```

For example, to clear the cache for the `orders` collection:

```javascript
db.orders.getPlanCache().clear()
```

## Required Access

On systems running with `authorization`, a user must have access that
includes the `planCacheWrite` action.

**See also:**

- `db.collection.getPlanCache()`
- `PlanCache.clearPlansByQuery()`
