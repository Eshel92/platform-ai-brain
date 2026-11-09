<!-- Converted from mongodump/mongodump-behavior.txt (reStructuredText). Includes are inlined. -->

# mongodump Behavior, Access, and Usage

**Warning:**

When dumping to a case-insensitive file system such as Windows 
or macOS, collections with names that differ only by capitalization 
will be overwritten. For case-insensitive file systems, always use 
the `--archive` 
option.  

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

### Using `mongodump` Without an `authSource`

When `authSource` is not specified in the MongoDB URI, the
database name specified in `--db` is used both
to authenticate your `mongodump` session and to indicate the database
being dumped. For an example of using a different database for
authentication when using `mongodump`, see mongodump-auth-dump.

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

### Time Series Collections

To dump time series collections
from a MongoDB 9.0 deployment, use Database Tools 100.16.0 or later.
Earlier Database Tools versions read time series bucket namespaces
directly, which MongoDB 9.0 doesn't allow. If you use an earlier
Database Tools version, `mongodump` aborts with a
`CommandNotSupportedOnLegacyTimeseriesBucketsNamespace` error. To
resolve the error, upgrade to the latest Database Tools version.

If a time series format conversion starts while `mongodump` reads a
time series collection, the operation fails with an
`InterruptedDueToTimeseriesUpgradeDowngrade` error. The dump isn't
truncated or corrupted. To resolve the error, wait for the feature
compatibility version (FCV) change to finish, then run `mongodump`
again. To learn more about the conversion, see
mongorestore-time-series-format-conversion.

### Read Preference

By default, `mongodump` uses read preference
`primary`. To override the default, you can specify the
read preference in the
`--readPreference` command-line
option or in the `--uri connection string`.

If read preference is specified in both the URI string and the
`--readPreference`
option, the `--readPreference`
value overrides the read preference specified in the URI string.

### Data Exclusion

If you specify both the `--db` and the
`--collection` options, `mongodump`
dumps the specified collection.

If you only specify the `--db` option,
`mongodump` dumps that database with the following exclusions:

- If the value of `--db` is `admin`:

  - If you aren't connected to an Atlas Proxy, `mongodump` dumps the
    database but excludes the `system.keys` collection. 
  - If you're connected to an Atlas Proxy, `mongodump` attempts to
    dump the database but errors out.

- If the value of `--db` is `config`, `mongodump` dumps all
  collections in that database. 

- If the value of `--db` is `local`, `mongodump` dumps all
  collections in that database.  
  
- For all other databases, `mongodump` excludes all collections that
  start with `system.`, except for `system.js`. 

If you omit the `--db` option, the following exclusions apply: 

- `mongodump` excludes the `local` database.
- `mongodump` only includes the following collections in the output
  for the `config` database:   

  - `chunks`
  - `collections`
  - `databases`
  - `settings`
  - `shards`
  - `tags`
  - `version`
    
- If you're connected to an Atlas Proxy, `mongodump` excludes the
  `admin` database.

`mongodump` output:

- Contains the documents in the database and the index definitions.
- Does not contain the index data.

`mongorestore` or `mongod` must rebuild the
indexes after restoring data.

If you're using views:

- By default, `mongodump` only exports a view's metadata.
  `mongodump` doesn't create a binary export of the
  documents included in the view.
- To export the documents in a view, use
  `--viewsAsCollections`.

### Metadata Output

If `mongodump` outputs to a directory, the output contains
collection metadata which includes the following properties: 

- Collection names
- Collection types
- Collection configuration options
- UUIDs
- Indexes

If `mongodump` outputs to standard output (`stdout`), the
output does not include metadata. For more information, see the
`--out` option. 

### Metadata Format

`mongodump` uses Extended
JSON v2.0 (Canonical) format
for the metadata files. To parse these files for restore, use
`mongorestore`, which supports Extended
JSON v2.0 (Canonical or Relaxed mode) format.

### Overwrite Files

`mongodump` overwrites output files if they exist in the
backup data folder. Before running the `mongodump` command
multiple times, either ensure that you no longer need the files in the
output folder (the default is the `dump/` folder) or rename the
folders or files.

### `mongodump` During Resharding

`mongodump` fails if:

- `mongodump` is initiated when a 
  resharding operation is in progress.

- The `reshardCollection` command is run during a 
  `mongodump` operation.

### Data Compression Handling

When run on a `mongod` instance that uses the
WiredTiger storage engine,
`mongodump` outputs uncompressed data.

### Working Set

`mongodump` can adversely affect performance of the
`mongod`. If your data is larger than system memory,
`mongodump` will push the working set out of memory.

### FIPS

`mongodump` automatically creates FIPS-compliant
connections to a `mongod` or `mongos` that are
configured to use FIPS mode.

### Using `mongodump` on Atlas Free and Shared Tier Clusters

On free (`M0`) and shared (`M2` and `M5`) tier Atlas clusters, the
following limitations apply: 

- You can't run `mongodump` on the `admin` database. By default,
  `mongodump` skips this database. If you use the `--db` option to set the destination database to `admin`,
  the program returns an error.

- You can't use the following options with the `mongodump` program:

  - `--dumpDbUsersAndRoles`
  - `--oplog`

### Using mongodump on Atlas Infinite Database Clusters

`mongodump` supports the `--oplog`
option when you dump data from an Atlas Infinite Database
cluster. Oplog replay is not supported with
Atlas Infinite Database clusters. For details, see
mongorestore-behavior-access-usage.

**Note:** Target cluster rollbacks

If the cluster undergoes a rollback during the restore process,
delete all restored or imported data and redo the process from 
the beginning. See the rollback documentation 
for more details.

## Required Access

To run `mongodump` against a MongoDB deployment that has
access control enabled, you must have
privileges that grant `find` action for each database to
back up. The built-in `backup` role provides the required
privileges to perform backup of any and all databases.

## Usage in Backup Strategy

### Standalone Deployments and Replica Sets

For standalone or a replica set, `mongodump` can be a part
of a backup strategy with
`mongorestore` for partial backups based on a query,
syncing from production to staging or development environments, or
changing the storage engine of a standalone.

For details on using `mongodump` with
`mongorestore` as part of a backup and recovery strategy,
see:

- Back Up and Restore with MongoDB Tools

- MongoDB Backup Methods

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

- mongodump
- mongodump-compatibility-and-installation
- mongodump-examples
