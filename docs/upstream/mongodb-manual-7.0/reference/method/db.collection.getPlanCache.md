<!-- Converted from reference/method/db.collection.getPlanCache.txt (reStructuredText). Includes are inlined. -->

# db.collection.getPlanCache() (mongosh method)

## Definition

**`db.collection.getPlanCache()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Returns an interface to access the query plan cache for a
collection. The interface provides methods to view and clear the
query plan cache.

:returns: Interface to access the query plan cache.

The query optimizer only caches the plans for those query shapes that
can have more than one viable plan.

## Methods

The following methods are available through the interface:

| Name | Description |
|---|---|
| `PlanCache.help()` | Displays the methods available for a collection's query plan cache. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().help()`. |
| `PlanCache.clearPlansByQuery()` | Clears the cached query plans for the specified query shape. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().clearPlansByQuery()` |
| `PlanCache.clear()` | Clears all the cached query plans for a collection. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().clear()`. |
| `PlanCache.list()` | Returns the plan cache information for a collection. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().list()`. |
