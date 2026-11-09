<!-- Converted from reference/method/sh.enableMigrations.txt (reStructuredText). Includes are inlined. -->

# sh.enableMigrations() (mongosh method)

## Definition

**`sh.enableMigrations(namespace)`**

Enables migrations for the specified namespace of the sharded collection, 
but does not start chunk migrations. The balancer includes the collection you pass to 
`sh.enableMigrations()` in migration operations the next time it runs.
For more information on chunk migrations, see sharded-cluster-balancer.

**Important:**

You can only run `sh.enableMigrations()` on a
`mongos` instance. If you run `sh.enableMigrations()` 
on a `mongod` instance, the method returns an error. 

The `sh.enableMigrations()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the collection. |

## Compatibility

This method is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

You can verify migration status using `sh.status()`, which displays 
the `allowMigrations` field for each collection.
