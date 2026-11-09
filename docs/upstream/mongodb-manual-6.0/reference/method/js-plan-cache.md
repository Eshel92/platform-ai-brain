<!-- Converted from reference/method/js-plan-cache.txt (reStructuredText). Includes are inlined. -->

# Query Plan Cache Methods

The PlanCache methods are only accessible from a collection's plan
cache object. To retrieve the plan cache object, use the
`db.collection.getPlanCache()` method.

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

| Name | Description |
|---|---|
| `db.collection.getPlanCache()` | Returns an interface to access the query plan cache object and associated PlanCache methods for a collection. |
| `PlanCache.clear()` | Clears all the cached query plans for a collection. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().clear()`. |
| `PlanCache.clearPlansByQuery()` | Clears the cached query plans for the specified query shape. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().clearPlansByQuery()` |
| `PlanCache.help()` | Displays the methods available for a collection's query plan cache. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().help()`. |
| `PlanCache.list()` | Returns the plan cache information for a collection. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().list()`. |
