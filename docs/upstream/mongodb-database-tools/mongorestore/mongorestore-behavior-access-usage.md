<!-- Converted from mongorestore/mongorestore-behavior-access-usage.txt (reStructuredText). Includes are inlined. -->

# mongorestore Behavior, Access, and Usage

**Warning:** Data Dump and Restore Conflicts with $ Prefix in Fields

Starting in MongoDB 5.0, document field names can be prefixed with a
dollar character (`$`). However, `mongodump` and
`mongorestore` won't work with field names that are
prefixed with a dollar character in a collection's options.

MongoDB Extended JSON
(v2) cannot differentiate between
type wrappers and fields that have the same name as type
wrappers. Don't use extended JSON formats if the
corresponding BSON representation might include `$` prefixed keys.
The DBRefs mechanism is an exception to
this general rule.

## Behavior

### Restore to Matching Server Version

When using `mongorestore` to load data files created by
`mongodump`, the MongoDB versions of your source and 
destination deployments must be either:

- The same major version.
- The same feature compatibility version. 

For example, if your dump was created from a MongoDB deployment running
version `4.4`, the MongoDB deployment you restore to must also run 
version `4.4` or have its FCV set to `4.4`.

To change your feature compatibility version, see 
`setFeatureCompatibilityVersion`.

**Note:**

You can restore the BSON files generated from `mongodump` into
MongoDB deployments running the same or newer version as the source
deployment. However, restoring files into a newer version deployment
is not the recommended way to upgrade your deployment. To learn how to
upgrade your deployment, see the upgrade documentation.

This guarantee does not apply to metadata, archive, or oplog replay 
files. If you try to restore these files using different 
source and destination deployment versions, the `mongorestore` 
process could result in failure, silent failure, or corrupted 
metadata.

In addition, ensure that you are using the same version of
`mongorestore` to load the data files as the version of `mongodump`
that you used to create them. In practice, using a different version of
`mongorestore` often works, but if the dump format changes between
versions, the restore can fail or restore data incorrectly. For example,
if you use `mongodump` version `{+version+}` to create the dump, use
`mongorestore` version `{+version+}` to restore it.

**Note:**

As an exception to this rule, you can restore data dumped from
a MongoDB 9.0 deployment into an Atlas Infinite Database
cluster. You can also restore data dumped from an
Atlas Infinite Database cluster into a MongoDB 9.0
deployment.

### Insert Only

`mongorestore` can create a new database or add data to an
existing database. However, `mongorestore` performs inserts
only and does not perform updates. If you restore documents to
an existing database and collection and existing documents have the
same value `_id` field as the documents to restore,
`mongorestore` will *not* overwrite those documents.

### Document Order

By default, `mongorestore` may insert documents in a random order. To
preserve document order during the restore process, use
`--maintainInsertionOrder`.

### Rebuild Indexes

`mongorestore` recreates indexes recorded by 
`mongodump` after restoring data.

**Note:**

For MongoDB installations with `featureCompatibilityVersion` (FCV)
set to `"4.0"` or earlier, creating indexes will
error if an index key in an existing document exceeds the
limit. 

To avoid this issue, consider using hashed indexes or indexing a
computed value instead. To resolve the index issue after
restoring the data, you can disable the default index key length
validation on the target database by setting the `mongod`
instance's `failIndexKeyTooLong` parameter to false.

### Exclude `system.profile` Collection

`mongorestore` does not restore the `system.profile
<` collection data.

### FIPS

`mongorestore` automatically creates FIPS-compliant
connections to a `mongod`/`mongos` that is
configured to use FIPS mode.

### Write Concern

If you specify write concern in both the
`--writeConcern` option and the
`--uri` connection string option, the
`--writeConcern` value overrides
the write concern specified in the URI string.

### Time Series Collections

Starting in MongoDB 5.0, you can use `mongorestore` to restore
timeseries collections.
For details, see mongorestore-example-time-series.

#### Oplog Replay Across a Time Series Format Conversion

MongoDB 8.x and MongoDB 9.0 store time series collections in different
formats:

- In MongoDB 8.x, a time series collection consists of a view and a
  separate `system.buckets.<collection>` collection.

- Starting in MongoDB 9.0, a time series collection is a single
  collection.

When you use `setFeatureCompatibilityVersion` to change the
feature compatibility version (FCV) across this boundary, the server
converts each time series collection to the format that matches the new FCV.
The server records every conversion in the oplog.

Each conversion also changes the namespace that bucket writes target,
from `system.buckets.<collection>` to `<collection>`. Oplog entries
recorded before a conversion don't match the collection format that
follows it.

As a result, `mongorestore` can't replay an oplog range that spans a
conversion. Restore the entries on each side of the conversion as
separate ranges, and change the FCV on the target deployment between
the two restores:

**Step 1: Replay the oplog entries that precede the conversion.**

Use `--oplogLimit` to stop
the replay before the conversion.

**Step 2: Change the FCV on the target deployment.**

Run `setFeatureCompatibilityVersion` on the target to
make the same FCV change, in the same direction, that produced
the conversion.

**Step 3: Replay the remaining oplog entries.**

The FCV change on the target is required. `mongorestore` never
changes the FCV and doesn't rewrite namespaces across the
conversion. If the target stays at one FCV for both restores, the
entries in the second range name a namespace that doesn't match the
collection format on the target. The restore then fails.

Starting in Database Tools 100.18.0, `mongorestore` fails with a
message that names the conversion when it encounters one during
`--oplogReplay`. Earlier versions
of Database Tools report an unknown oplog command instead.

To avoid producing a dump that you can't restore, don't change the FCV
while `mongodump --oplog` runs. If you capture the oplog
yourself with `mongodump --db=local --collection=oplog.rs` and replay
it with `--oplogFile`, `mongodump`
can't detect the FCV change, so check that the range you restore
doesn't span a conversion.

### Using `mongorestore` on Atlas Free and Flex  Clusters

On free (`M0`) and Flex clusters, the
following limitations apply:

- You can't run `mongorestore` on the `admin` database. By default,
  `mongorestore` skips this database. If you use the `--db` option to set the destination database to
  `admin`, the program returns an error.

- You can't use the following options with the `mongorestore` program:

  - `--restoreDbUsersAndRoles`
  - `--oplogReplay`
  - `--preserveUUID`

### Using mongorestore on Atlas Infinite Database Clusters

When you restore into an Atlas Infinite Database cluster, you
can't use the following options with the `mongorestore` program:

- `--oplogReplay`
- `--preserveUUID`

This restriction applies whether the dump comes from a MongoDB 9.0
(non-Atlas Infinite Database) or an Atlas Infinite Database
cluster.

**Important:**

`mongorestore` can't detect whether the target cluster is an
Atlas Infinite Database cluster before the restore starts.
If you use `--oplogReplay`
or `--preserveUUID` against
an Atlas Infinite Database cluster, `mongorestore` returns
an error when it tries to apply the oplog. Because
`mongorestore` restores the non-oplog data before it applies
the oplog, the failed oplog replay can leave the restore only
partially complete.

### Crash Behavior

If `mongorestore` crashes, it can leave the system in an 
inconsistent state where only *some* of the data was restored, 
but not all of it. After a crash, delete any restored data and 
rerun the process from the beginning.

**Note:** Target cluster rollbacks

If the cluster undergoes a rollback during the restore process,
delete all restored or imported data and redo the process from 
the beginning. See the rollback documentation 
for more details.

## Required Access

To restore data to a MongoDB deployment that has access control enabled, the `restore` role provides
the necessary privileges to restore data from backups *if* the data does
not include `system.profile <`
collection data and you run `mongorestore` without the
`--oplogReplay` option.

**Note:**

If the target cluster is a MongoDB Atlas cluster, the
`Atlas admin` role is required instead. MongoDB Atlas does not
offer an individual `restore` role, privilege, or privilege
action. To learn more, see mongodb-users.

If the backup data includes `system.profile
<` collection data or you run
`mongorestore` with the
`--oplogReplay` option, you need
additional privileges:

|  |  |
|---|---|
| `system.profile` | If the backup data includes `system.profile <` collection data and the target database does not contain the `system.profile <` collection, `mongorestore` attempts to create the collection even though the program does not actually restore `system.profile` documents. As such, the user requires additional privileges to perform `createCollection` and `convertToCapped` actions on the `system.profile <` collection for a database. Both the built-in roles `dbAdmin` and `dbAdminAnyDatabase` provide the additional privileges. |
| `--oplogReplay` | To run with `--oplogReplay`, create a user-defined role that has `anyAction` on resource-anyresource. Grant only to users who must run `mongorestore` with `--oplogReplay`. |

## Usage in Backup Strategy

### Standalones/Replica Sets

For an overview of `mongorestore` usage as part of a
backup and recovery strategy, see
Back Up and Restore with MongoDB Tools.

### Sharded Clusters

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which guarantee atomicity across shards while
still accepting writes:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)

## Learn More

- mongorestore
- mongorestore-compatibility-and-installation
- mongorestore-examples
