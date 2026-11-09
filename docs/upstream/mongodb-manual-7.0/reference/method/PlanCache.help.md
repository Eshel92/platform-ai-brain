<!-- Converted from reference/method/PlanCache.help.txt (reStructuredText). Includes are inlined. -->

# PlanCache.help() (mongosh method)

## Definition

**`PlanCache.help()`**

Displays the methods available to view and modify a collection's
query plan cache.

The method is only available from the `plan cache object` of a specific collection; i.e.

```javascript
db.collection.getPlanCache().help()
```

**See also:**

`db.collection.getPlanCache()`
