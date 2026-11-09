<!-- Converted from reference/method/Mongo.getDBNames.txt (reStructuredText). Includes are inlined. -->

# Mongo.getDBNames() (mongosh method)

## Description

**`Mongo.getDBNames()`**

Returns a list of available databases. `Mongo.getDBNames()`
calls the `listDatabases` command.

The `Mongo.getDBNames()` method doesn't take any parameters.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Examples

### List Databases

List the available databases for the current MongoDB instance:

```javascript
db.getMongo().getDBNames()
```

The `db.getMongo()` method creates a connection to the
instance. `Mongo.getDBNames()` returns:

```javascript
[ 'admin', 'config', 'local', 'test' ]
```

### Map Database List to Another Method

Use `Mongo.getDBNames()` to get a list of collections:

```javascript
db.getMongo().getDBNames().map( 
   name => db.getSiblingDB( name ).getCollectionNames()
)
```

Example output:

```javascript
[
   [ 'system.users', 'system.keys', 'system.version' ],
   [
     'settings',
     'tenantMigrationRecipients',
     'system.sessions',
     'transactions',
     'external_validation_keys',
     'image_collection',
     'tenantMigrationDonors',
     'system.indexBuilds'
   ],
   [
     'replset.minvalid',
     'system.views',
     'oplog.rs',
     'replset.initialSyncId',
     'startup_log',
     'system.replset',
     'system.rollback.id',
     'replset.oplogTruncateAfterPoint',
     'replset.election',
     'system.tenantMigration.oplogView'
   ],
   [
     'feedback',
     'inventory',
     'engineers',
     'clothes'
   ]
]
```

- `Mongo.getDBNames()` returns a list of databases.
- `map` defines a function that iterates over the list of databases.
  Each iteration of `map`:

  - assigns a database to the `name` variable,
  - connects to the database currently stored in `name` using
    `db.getSiblingDB()`,
  - returns the collections in the current database using
    `db.getCollectionNames()`.
