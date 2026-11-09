<!-- Converted from reference/built-in-roles.txt (reStructuredText). Includes are inlined. -->

# Built-In Roles

MongoDB grants access to data and commands through
role-based authorization. MongoDB provides built-in
roles that grant the different levels of access commonly needed in
a database system.

A role grants privileges to perform sets of actions on defined resources. A role applies to the database on which it is
defined and can grant access down to a collection level of
granularity.

Each built-in role defines access at the database level for all
non-system collections in the role's database and at the collection
level for all system collections.

*System collections* include those in:

- `<database>.system.*` namespace
- `local.replset.*` replica set namespace

*Non-system collections* are those not in namespaces in the
previous list.

MongoDB Atlas database users have different built-in roles than
self-hosted deployment users. However, MongoDB builds the built-in
roles for each type of deployment from the same set of
privilege actions.

Use the selector at the top of the page to choose your deployment
type and see the available built-in roles.

## MongoDB Atlas Built-In Roles

This section describes the Atlas built-in roles and the
MongoDB Roles they
represent.

Create database users and assign built-in roles in the MongoDB Atlas
user interface. To learn more, see Add Database Users.

To learn more about common commands that Atlas does not
support with the current Atlas user privileges, see
paid-tier-command-limitations.

### Protected MongoDB Database Namespaces

Avoid writing to the `admin`, `local`, and `config`
databases, or any database prefixed with `__mdb_internal_`.
Atlas manages multiple collections in these databases. To
learn more, see cloud-system-databases and
metadata-system-collections.

`atlasAdmin` has the `update` privilege
on the `config.settings` collection to manage the balancer.

### Built-in Roles and Inherited Privileges

In the following table, cog indicates that the
operation also supports timeseries collections.

| Atlas Built-in Role | MongoDB Role | Inherited Roles or Privilege Actions |
|---|---|---|
| .. atlasrole:: Atlas admin | .. atlasrole:: atlasAdmin | \| `analyzeShardKey` cog \| backup \| `checkMetadataConsistency` \| `cleanupOrphaned` \| `clearJumboFlag` cog \| clusterMonitor \| `compact` \| dbAdminAnyDatabase \| enableSharding cog \| `flushRouterConfig` cog \| `killAnyCursor` \| `moveChunk` cog \| readWriteAnyDatabase \| `refineCollectionShardKey` cog \| `reshardCollection` cog \| `shardedDataDistribution` cog \| `splitChunk` cog \| `viewRole` |
| .. atlasrole:: backup | `backup` | backup |
| .. atlasrole:: clusterMonitor | `clusterMonitor` | clusterMonitor |
| .. atlasrole:: dbAdmin | `dbAdmin` | dbAdmin |
| .. atlasrole:: dbAdminAnyDatabase | `dbAdminAnyDatabase` | dbAdminAnyDatabase |
| .. atlasrole:: enableSharding | `enableSharding` | enableSharding |
| .. atlasrole:: read | `read` | read |
| .. atlasrole:: readWrite | `readWrite` | readWrite |
| .. atlasrole:: readWriteAnyDatabase | `readWriteAnyDatabase` | readWriteAnyDatabase |
| .. atlasrole:: readAnyDatabase | `readAnyDatabase` | readAnyDatabase |

### MongoDB Built-In Role Descriptions

The following are the MongoDB built-in roles used by
Atlas built-in roles.

| MongoDB Role | Description |
|---|---|
| .. _atlas-backup: `backup` | .. include:: /includes/extracts/built-in-roles-backup.rst |
| .. _atlas-clusterMonitor: `clusterMonitor` | .. include:: /includes/extracts/built-in-roles-clusterMonitor.rst |
| .. _atlas-dbAdmin: `dbAdmin` | .. include:: /includes/extracts/built-in-roles-dbAdmin.rst |
| .. _atlas-dbAdminAnyDatabase: `dbAdminAnyDatabase` | .. include:: /includes/extracts/built-in-roles-dbAdminAnyDatabase.rst |
| .. _atlas-enableSharding: `enableSharding` | Provides the ability to enable sharding for a collection and modify existing shard keys. |
| .. _atlas-read: `read` | Provides read access to all *non*-system collections and the `system.js <` collection. |
| .. _atlas-readAnyDatabase: `readAnyDatabase` | .. include:: /includes/extracts/built-in-roles-readAnyDatabase.rst |
| .. _atlas-readWrite: `readWrite` | .. include:: /includes/extracts/built-in-roles-read-write.rst |
| .. _atlas-readWriteAnyDatabase: `readWriteAnyDatabase` | .. include:: /includes/extracts/built-in-roles-readWriteAnyDatabase.rst |

## Learn More

If built-in roles do not meet your requirements, create
user-defined roles. For more information, see
mongodb-roles.

## Self-Managed Deployment Built-In Roles

MongoDB provides the following built-in roles in self-managed
deployments.

To view the privileges for a built-in role, run the
`rolesInfo` command with the `showPrivileges` and
`showBuiltinRoles` fields both set to `true`. The following
command shows the privileges for the `readWrite` role:

```javascript
db.getRole("readWrite", { showPrivileges: true, showBuiltinRoles: true } )
```

Output:

```javascript
{
   db: 'test',
   role: 'readWrite',
   roles: [],
   privileges: [
      {
         resource: { db: 'test', collection: '' },
         actions: [
            'changeStream',
            'cleanupStructuredEncryptionData',
            'collStats',
            'compactStructuredEncryptionData',
            'convertToCapped',
            'createCollection',
            'createIndex',
            'createSearchIndexes',
            'dbHash',
            'dbStats',
            'dropCollection',
            'dropIndex',
            'dropSearchIndex',
            'find',
            'insert',
            'killCursors',
            'listCollections',
            'listIndexes',
            'listSearchIndexes',
            'updateSearchIndex',
            'planCacheRead',
            'performRawDataOperations',
            'remove',
            'renameCollectionSameDB',
            'update'
         ]
      },
      {
         resource: { db: 'test', collection: 'system.js' },
         actions: [
            'changeStream',
            'cleanupStructuredEncryptionData',
            'collStats',
            'compactStructuredEncryptionData',
            'convertToCapped',
            'createCollection',
            'createIndex',
            'createSearchIndexes',
            'dbHash',
            'dbStats',
            'dropCollection',
            'dropIndex',
            'dropSearchIndex',
            'find',
            'insert',
            'killCursors',
            'listCollections',
            'listIndexes',
            'listSearchIndexes',
            'updateSearchIndex',
            'planCacheRead',
            'performRawDataOperations',
            'remove',
            'renameCollectionSameDB',
            'update'
         ]
      }
   ],
   inheritedRoles: [],
   inheritedPrivileges: [
      {
         resource: { db: 'test', collection: '' },
         actions: [
            'changeStream',
            'cleanupStructuredEncryptionData',
            'collStats',
            'compactStructuredEncryptionData',
            'convertToCapped',
            'createCollection',
            'createIndex',
            'createSearchIndexes',
            'dbHash',
            'dbStats',
            'dropCollection',
            'dropIndex',
            'dropSearchIndex',
            'find',
            'insert',
            'killCursors',
            'listCollections',
            'listIndexes',
            'listSearchIndexes',
            'updateSearchIndex',
            'planCacheRead',
            'performRawDataOperations',
            'remove',
            'renameCollectionSameDB',
            'update'
         ]
      },
      {
         resource: { db: 'test', collection: 'system.js' },
         actions: [
            'changeStream',
            'cleanupStructuredEncryptionData',
            'collStats',
            'compactStructuredEncryptionData',
            'convertToCapped',
            'createCollection',
            'createIndex',
            'createSearchIndexes',
            'dbHash',
            'dbStats',
            'dropCollection',
            'dropIndex',
            'dropSearchIndex',
            'find',
            'insert',
            'killCursors',
            'listCollections',
            'listIndexes',
            'listSearchIndexes',
            'updateSearchIndex',
            'planCacheRead',
            'performRawDataOperations',
            'remove',
            'renameCollectionSameDB',
            'update'
         ]
      }
   ],
   isBuiltin: true
}
```

### Database User Roles

Every database includes the following client roles:

**`read`**

Provides read access to all *non*-system collections and the
`system.js <` collection.

**Note:**

This role does not provide privileges to directly access the
`system.namespaces` collection.

The role provides read access by granting the following
actions:

- `changeStream`
- `collStats`
- `dbHash`
- `dbStats`
- `find`
- `killCursors`
- `listCollections`
- `listIndexes`
- `listSearchIndexes`

Users without the `listDatabases` privilege action can
run the `listDatabases` command to return a list of
databases for which they have privileges. This includes databases
where the user has privileges on specific collections. Run the
command with the `authorizedDatabases` option unspecified or set
to `true`.

**`readWrite`**

Provides all privileges of the `read` role plus the
ability to modify data on all *non*-system collections and the
`system.js <` collection.

The role provides the following actions on those collections:

- `changeStream`
- `collStats`
- `convertToCapped`
- `createCollection`
- `createIndex`
- `createSearchIndexes`
- `dbHash`
- `dbStats`
- `dropCollection`
- `dropIndex`
- `dropSearchIndex`
- `find`
- `insert`
- `killCursors`
- `listCollections`
- `listIndexes`
- `listSearchIndexes`
- `remove`
- `renameCollectionSameDB`
- `update`
- `updateSearchIndex`

### Database Administration Roles

Every database includes the following database administration roles:

**`dbAdmin`**

Provides the ability to perform administrative tasks such as
schema-related tasks, indexing, and gathering statistics. This
role does not grant privileges for user and role management.

The role provides the following privileges:

* - Resource

  - Permitted Actions

* - `system.profile <`
  - .. hlist:

  ```
  :columns: 2

  - :authaction:`changeStream`
  - :authaction:`collStats`
  - :authaction:`convertToCapped`
  - :authaction:`createCollection`
  - :authaction:`dbHash`
  - :authaction:`dbStats`
  - :authaction:`dropCollection`
  - :authaction:`find`
  - :authaction:`killCursors`
  - :authaction:`listCollections`
  - :authaction:`listIndexes`
  - :authaction:`listSearchIndexes`
  - :authaction:`planCacheRead`
  ```

* - All *non*-system collections
      (database resource)

  - .. hlist:

  ```
     :columns: 2

     - :authaction:`bypassDocumentValidation`
     - :authaction:`collMod`
     - :authaction:`collStats`
     - :authaction:`compact`
     - :authaction:`convertToCapped`
     - :authaction:`createCollection`
     - :authaction:`createIndex`
     - :authaction:`createSearchIndexes`
     - :authaction:`dbStats`
     - :authaction:`dropCollection`
     - :authaction:`dropDatabase`
     - :authaction:`dropIndex`
     - :authaction:`dropSearchIndex`
     - :authaction:`enableProfiler`
     - :authaction:`listCollections`
     - :authaction:`listIndexes`
     - :authaction:`listSearchIndexes`
     - :authaction:`planCacheIndexFilter`
     - :authaction:`planCacheRead`
     - :authaction:`planCacheWrite`
     - :authaction:`reIndex`
     - :authaction:`renameCollectionSameDB`
     - :authaction:`updateSearchIndex`
     - :authaction:`validate`

  For these collections, :authrole:`dbAdmin` does not
  include full read access such as :authaction:`find`.
  ```

**`dbOwner`**

The database owner can perform any administrative action on the
database. This role combines the privileges granted by the
`readWrite`, `dbAdmin` and
`userAdmin` roles.

**`userAdmin`**

  Provides the ability to create and modify roles and users on the
  current database. The `userAdmin` role allows users to
  grant any privilege to any user, including themselves. This role
  also indirectly provides superuser access to
  either the database or, if scoped to the `admin` database, the
  cluster.

  The `userAdmin` role explicitly provides the following actions:

  - `changeCustomData`
  - `changePassword`
  - `createRole`
  - `createUser`
  - `dropRole`
  - `dropUser`
  - `grantRole`
  - `revokeRole`
  - `setAuthenticationRestriction`
  - `viewRole`
  - `viewUser`

  **Warning:**

  Understand the security implications of granting the
  `userAdmin` role. A user with this role for a
  database can assign themselves any privilege on that
  database. Granting the `userAdmin` role on the
  `admin` database has further security implications as
  this indirectly provides superuser
  access to a cluster. With `admin` scope, a user with the
  `userAdmin` role can grant cluster-wide roles or
  privileges including `userAdminAnyDatabase`.

### Cluster Administration Roles

The `admin` database includes the following roles for
administering the whole system rather than just a single
database. These roles include but are not limited to
replica set and sharded cluster administrative
functions.

**`clusterAdmin`**

Provides the greatest cluster-management access. This role
combines the privileges granted by the `clusterManager`,
`clusterMonitor`, and `hostManager` roles.
Additionally, the role provides the `dropDatabase`
action.

**`clusterManager`**

Provides management and monitoring actions on the cluster. A
user with this role can access the `config` and `local`
databases, which are used in sharding and replication,
respectively.

* - Resource
  - Actions

* - cluster

  - .. hlist:

  ```
  :columns: 2

  - :authaction:`addShard`
  - :authaction:`appendOplogNote`
  - :authaction:`applicationMessage`
  - :authaction:`checkMetadataConsistency` (New in version 7.0)
  - :authaction:`cleanupOrphaned`
  - :authaction:`flushRouterConfig`
  - :dbcommand:`getClusterParameter`
  - :authaction:`getDefaultRWConcern`
  - :authaction:`listSessions`
  - :authaction:`listShards`
  - :authaction:`removeShard`
  - :authaction:`replSetConfigure`
  - :authaction:`replSetGetConfig`
  - :authaction:`replSetGetStatus`
  - :authaction:`replSetStateChange`
  - :authaction:`resync`
  - :dbcommand:`setClusterParameter`
  - :authaction:`setDefaultRWConcern` 
  - :authaction:`setFeatureCompatibilityVersion`
  ```

* - *All* databases

  - .. hlist:

  ```
     :columns: 1

     - :authaction:`analyzeShardKey` (New in version 7.0)
     - :authaction:`clearJumboFlag`
     - :dbcommand:`configureQueryAnalyzer`
     - :authaction:`enableSharding`
     - :authaction:`moveChunk`
     - :authaction:`refineCollectionShardKey`
     - :authaction:`reshardCollection`

  :authrole:`clusterManager` provides additional
  privileges for the ``config`` and ``local`` databases.
  ```

On the `config` database, permits the following actions:

* - Resource
  - Actions

* - All non-system collections in the `config` database

  - .. hlist:

  ```
  :columns: 2

  - :authaction:`collStats`
  - :authaction:`dbHash`
  - :authaction:`dbStats`
  - :authaction:`enableSharding`
  - :authaction:`find`
  - :authaction:`insert`
  - :authaction:`killCursors`
  - :authaction:`listCollections`
  - :authaction:`listIndexes`
  - :authaction:`listSearchIndexes`
  - :authaction:`moveChunk`
  - :authaction:`planCacheRead`
  - :authaction:`remove`
  - :authaction:`update`
  ```

* - `system.js <`

  - .. hlist:

  ```
  :columns: 2

  - :authaction:`collStats`
  - :authaction:`dbHash`
  - :authaction:`dbStats`
  - :authaction:`find`
  - :authaction:`killCursors`
  - :authaction:`listCollections`
  - :authaction:`listIndexes`
  - :authaction:`listSearchIndexes`
  - :authaction:`planCacheRead`
  ```

On the `local` database, permits the following actions:

* - Resource
  - Actions

* - All non-system collections in the `local` database

  - .. hlist:

  ```
  :columns: 2

  - :authaction:`enableSharding`
  - :authaction:`insert`
  - :authaction:`moveChunk`
  - :authaction:`remove`
  - :authaction:`update`
  ```

* - `system.replset` collection
  - .. hlist:

  ```
  :columns: 2

  - :authaction:`collStats`
  - :authaction:`dbHash`
  - :authaction:`dbStats`
  - :authaction:`find`
  - :authaction:`killCursors`
  - :authaction:`listCollections`
  - :authaction:`listIndexes`
  - :authaction:`listSearchIndexes`
  - :authaction:`planCacheRead`
  ```

**`clusterMonitor`**

Provides read-only access to monitoring tools, such as the
[MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) and `Ops Manager` monitoring agent.

Permits the following actions on the cluster as a whole:

- `connPoolStats`
- `getCmdLineOpts`
- `getDefaultRWConcern`
- `getLog`
- `getParameter`
- `getShardMap`
- `hostInfo`
- `inprog`
- `listDatabases`
- `listSessions`
- `listShards`
- `replSetGetConfig`
- `replSetGetStatus`
- `serverStatus`
- `shardingState`
- `top`

Permits the following actions on *all* databases in the cluster:

- `collStats`
- `dbStats`
- `indexStats`
- `useUUID`

Permits the `find` action on all `system.profile
<` collections in the cluster.

On the `config` database, permits the following actions:

| Resource | Actions |
|---|---|
| All non-system collections in the `config` database | \| `collStats` \| `dbHash` \| `dbStats` \| `find` \| `indexStats` \| `killCursors` \| `listCollections` \| `listIndexes` \| `listSearchIndexes` \| `planCacheRead` |
| `system.js <` collection | \| `collStats` \| `dbHash` \| `dbStats` \| `find` \| `killCursors` \| `listCollections` \| `listIndexes` \| `planCacheRead` |

On the `local` database, permits the following actions:

| Resource | Actions |
|---|---|
| All non-system collections in the `local` database | \| `collStats` \| `dbHash` \| `dbStats` \| `find` \| `indexStats` \| `killCursors` \| `listCollections` \| `listIndexes` \| `listSearchIndexes` \| `planCacheRead` |
| \| `system.js <` collection | \| `collStats` \| `dbHash` \| `dbStats` \| `find` \| `killCursors` \| `listCollections` \| `listIndexes` \| `listSearchIndexes` \| `planCacheRead` |
| \| `system.replset`, \| `system.profile <`, | `find` |

**`enableSharding`**

Provides the ability to enable sharding for a collection and
modify existing shard keys.

Provides the following actions on all non-system collections:

- `analyzeShardKey`
- `enableSharding`
- `refineCollectionShardKey` 
- `reshardCollection`

**`hostManager`**

Provides the ability to monitor and manage servers.

On the cluster as a whole, provides the following actions:

- `applicationMessage`
- `closeAllDatabases`
- `compact` (New in version 7.3)
- `connPoolSync`
- `flushRouterConfig`
- `fsync`
- `invalidateUserCache`
- `killAnyCursor`
- `killAnySession`
- `killop`
- `logRotate`
- `oidReset`
- `resync`
- `rotateCertificates` (New in version 5.0)
- `setParameter`
- `shutdown`
- `touch`
- `unlock`

On *all* databases in the cluster, provides the following actions:

- `killCursors`

### Backup and Restoration Roles

The `admin` database includes the following roles for backing
up and restoring data:

**`backup`**

Provides minimal privileges needed for backing up data. This role
provides sufficient privileges to use the [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) backup agent,
`Ops Manager` backup agent, or to use
`mongodump` to back up an entire
`mongod` instance.

Provides the `insert` and `update`
actions on the `settings` collection
in the `config` database.

On anyResource, provides the following actions:

- `listDatabases`
- `listCollections`
- `listIndexes`
- `listSearchIndexes`

On the cluster as a whole, provides
the following actions:

- `appendOplogNote`
- `getParameter`
- `listDatabases`
- `serverStatus`
- `setUserWriteBlockMode` (Starting in MongoDB 6.0)

Provides the `find` action on the following:

- All *non*-system collections in the cluster, including those
  in the `config` and `local` databases

- The following system collections in the cluster:
  `system.js <` and
  `system.profile <`

- The `admin.system.users` and
  `admin.system.roles` collections

- The `config.settings` collection

- Legacy `system.users` collections from versions of MongoDB
  prior to 2.6

Provides the `insert` and `update`
actions on the `config.settings` collection.

The `backup` role provides additional privileges to back
up the `system.profile <`
collection that exists when running with database profiling.

**`restore`**

Provides `convertToCapped` on non-system collections.

Provides the necessary privileges to restore data from backups if
the data does not include `system.profile
<` collection data and you run
`mongorestore` without the `--oplogReplay` option.

You need additional privileges if the backup data includes
`system.profile <` collection data
or you run with `--oplogReplay`:

|  |  |
|---|---|
| `system.profile` | If the backup data includes `system.profile <` collection data and the target database does not contain the `system.profile <` collection, `mongorestore` attempts to create the collection even though the program does not actually restore `system.profile` documents. The user requires additional privileges to perform `createCollection` and `convertToCapped` actions on the `system.profile <` collection for a database. Both the built-in roles `dbAdmin` and `dbAdminAnyDatabase` provide the additional privileges. |
| `--oplogReplay` | To run with `--oplogReplay`, create a user-defined role that has `anyAction` on resource-anyresource. Grant only to users who must run `mongorestore` with `--oplogReplay`. |

Provides the following action on the cluster as a whole:

- `getParameter`

Provides the following actions on all *non*-system collections:

- `bypassDocumentValidation`
- `changeCustomData`
- `changePassword`
- `collMod`
- `convertToCapped`
- `createCollection`
- `createIndex`
- `createRole`
- `createSearchIndexes`
- `createUser`
- `dropCollection`
- `dropRole`
- `dropUser`
- `grantRole`
- `insert`
- `revokeRole`
- `updateSearchIndex`
- `viewRole`
- `viewUser`

Provides the following actions on `system.js
<` collection:

- `bypassDocumentValidation`
- `collMod`
- `createCollection`
- `createIndex`
- `dropCollection`
- `insert`
- `updateSearchIndex`

Provides the following action on anyResource:

- `listCollections`

Provides the following actions on all non-system collections
on the `config` and the `local` databases:

- `bypassDocumentValidation`
- `collMod`
- `createCollection`
- `createIndex`
- `dropCollection`
- `insert`
- `updateSearchIndex`

Provides the following actions on `admin.system.version`

- `bypassDocumentValidation`
- `collMod`
- `createCollection`
- `createIndex`
- `dropCollection`
- `find`
- `insert`
- `updateSearchIndex`

Provides the following action on `admin.system.roles`

- `createIndex`

Provides the following actions on `admin.system.users`
and legacy `system.users` collections:

- `bypassDocumentValidation`
- `collMod`
- `createCollection`
- `createIndex`
- `dropCollection`
- `find`
- `insert`
- `remove`
- `update`
- `updateSearchIndex`

`restore` includes the ability to modify the
documents in the `admin.system.users` collection using
normal modification operations. However, only modify these
data using the user management methods.

Provides the following action on the
`<database>.system.views` collection:

- `dropCollection` (Starting in MongoDB 6.0)

On the cluster as a whole, provides
the following actions:

- `bypassWriteBlockingMode` (Staring in MongoDB 6.0)
- `setUserWriteBlockMode` (Starting in MongoDB 6.0)

### All-Database Roles

The following roles are available on the `admin` database and
provide privileges that apply to all databases except `local`
and `config`:

**`readAnyDatabase`**

Provides the same read-only privileges as `read` on all
databases except `local` and `config`. The role also provides
the `listDatabases` action on the cluster as a whole.

This role grants permissions on database resources, not
cluster administrative resources.

See also the `clusterManager` and
`clusterMonitor` roles for access to the `config` and
`local` databases.

**`readWriteAnyDatabase`**

Provides the same privileges as `readWrite` on all
databases except `local` and `config`. The role also provides:

- the `listDatabases` action on the cluster as a
  whole
- the `compactStructuredEncryptionData` action

This role grants permissions on database resources, not
cluster administrative resources.

See also the `clusterManager` and
`clusterMonitor` roles for access to the `config` and
`local` databases.

**`userAdminAnyDatabase`**

Provides the same access to user administration operations as
`userAdmin` on all databases except `local` and
`config`.

`userAdminAnyDatabase` also provides the following
privilege actions on the cluster:

- `authSchemaUpgrade`
- `invalidateUserCache`
- `listDatabases`

The role provides the following privilege actions on the
`system.users` and
`system.roles` collections on the
`admin` database, and on legacy `system.users` collections
from versions of MongoDB prior to 2.6:

- `collStats`
- `createIndex`
- `createSearchIndexes`
- `dbHash`
- `dbStats`
- `dropIndex`
- `dropSearchIndex`
- `find`
- `killCursors`
- `planCacheRead`

The `userAdminAnyDatabase` role does not restrict
the privileges that a user can grant. As a result,
`userAdminAnyDatabase` users can grant themselves
privileges in excess of their current privileges and even can
grant themselves *all privileges*, even though the role does
not explicitly authorize privileges beyond user
administration. This role is effectively a MongoDB system
superuser.

See also the `clusterManager` and
`clusterMonitor` roles for access to the `config` and
`local` databases.

**`dbAdminAnyDatabase`**

Provides the same privileges as `dbAdmin` on all
databases except `local` and `config`. The role also provides
the `listDatabases` action on the cluster as a whole.

See also the `clusterManager` and
`clusterMonitor` roles for access to the `config` and
`local` databases.

Starting in MongoDB 5.0, `dbAdminAnyDatabase`
includes the applyOps privilege
action.

### Superuser Roles

Several roles provide either indirect or direct system-wide
superuser access.

The following roles provide the ability to assign any user any
privilege on any database. Users with one of these roles can
assign *themselves* any privilege on any database:

- `dbOwner` role, when scoped to the `admin`
  database

- `userAdmin` role, when scoped to the `admin`
  database

- `userAdminAnyDatabase` role

The following role provides full privileges on all resources:

**`root`**

Provides access to the operations and all the resources of the
following combined roles:

- `readWriteAnyDatabase`
- `dbAdminAnyDatabase`
- `userAdminAnyDatabase`
- `clusterAdmin`
- `restore`
- `backup`

Also provides the `validate`
privilege action on `system.` collections.

**Changed in version:** 6.0

The `root` role includes `find` and
`remove` privileges on the `system.preimages`
collection in the `config` database.

### Internal Role

**`__system`**

MongoDB assigns this role to user objects that represent
cluster members, such as replica set members and
`mongos` instances. The role entitles its holder
to take any action against any object in the database.

**Do not** assign this role to user objects representing
applications or human administrators, other than in
exceptional circumstances.

If you need access to all actions on all resources, for
example to run `applyOps` commands, do not assign
this role. Instead, create a user-defined role that grants
`anyAction` on resource-anyresource and
ensure that only the users who need access to these
operations have this access.

## Learn More

If built-in roles do not meet your requirements, create
user-defined roles. For more information, see
user-defined-roles.
