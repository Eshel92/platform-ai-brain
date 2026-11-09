<!-- Converted from reference/method/sh.disableMigrations.txt (reStructuredText). Includes are inlined. -->

# sh.disableMigrations() (mongosh method)

## Definition

**`sh.disableMigrations(namespace)`**

Disables migrations for the specified namespace of the sharded collection. 
The balancer does not migrate chunks for the collection you pass to `sh.disableMigrations()`
until migrations are re-enabled using `sh.enableMigrations()`.
For more information on chunk migrations, see sharded-cluster-balancer.

**Important:**

You can only run `sh.disableMigrations()` on a
`mongos` instance. If you run `sh.enableMigrations()` 
on a `mongod` instance, the method returns an error. 

The `sh.disableMigrations()` method has the following parameter:

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
