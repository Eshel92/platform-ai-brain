<!-- Converted from mongorestore/mongorestore-examples.txt (reStructuredText). Includes are inlined. -->

# mongorestore Examples

This page shows examples for `mongorestore`.

Run `mongorestore` from the system command line, not the 
`mongo` shell.

## Restore with Access Control

In the following example, `mongorestore` restores from
`/opt/backup/mongodump-2011-10-24` to a `mongod`
instance running on port `27017` on the host
`mongodb1.example.net`. The `--uri`
string omits the user's password to have `mongorestore`
prompt for the password.

```sh
mongorestore --uri="mongodb://user@mongodb1.example.net:27017/?authSource=admin" /opt/backup/mongodump-2011-10-24
```

Alternatively, you can specify the host, port, username, and
authentication database using `--host`,
`--port`, `--username`, and `--authenticationDatabase`.  Omit `--password` to have `mongorestore` prompt for the password:

```sh
mongorestore --host=mongodb1.example.net --port=27017 --username=user --authenticationDatabase=admin /opt/backup/mongodump-2011-10-24
```

## Restore a Collection

To restore a specific collection, use `--nsInclude`, passing in the full namespace
(`<database>.<collection>`) of the collection.

The following example restores the collection named
`purchaseorders` in the database `test` from the corresponding
files located in the `dump/` directory.

```sh
mongorestore --nsInclude=test.purchaseorders dump/
```

The `mongorestore` outputs the results, including the
number of documents restored:

```sh
2019-06-28T19:23:42.858-0400   preparing collections to restore from
2019-06-28T19:23:42.858-0400   reading metadata for test.purchaseorders from dump/test/purchaseorders.metadata.json
2019-06-28T19:23:42.893-0400   restoring test.purchaseorders from dump/test/purchaseorders.bson
2019-06-28T19:23:42.896-0400   restoring indexes for collection test.purchaseorders from metadata
2019-06-28T19:23:42.991-0400   finished restoring test.purchaseorders (6 documents, 0 failures)
2019-06-28T19:23:42.991-0400   6 document(s) restored successfully. 0 document(s) failed to restore.
```

If the `dump/` directory does not contain the corresponding data
files for the specified namespace, no data will be restored:

```sh
2019-07-08T14:39:57.121-0400. preparing collections to restore from
2019-07-08T14:39:57.121-0400  0 document(s) restored successfully. 0 document(s) failed to restore.
```

Alternatively, you can restore a specific collection using the
`--db`, `--collection`, and a `.bson` file:

```sh
mongorestore --db=test --collection=purchaseorders dump/test/purchaseorders.bson
```

```sh
2019-06-30T12:21:44.777-0400   checking for collection data in dump/test/purchaseorders.bson
2019-06-30T12:21:44.779-0400   reading metadata for test.purchaseorders from dump/test/purchaseorders.metadata.json
2019-06-30T12:21:44.813-0400   restoring test.purchaseorders from dump/test/purchaseorders.bson
2019-06-30T12:21:44.881-0400   restoring indexes for collection test.purchaseorders from metadata
2019-06-30T12:21:44.987-0400   finished restoring test.purchaseorders (6 documents, 0 failures)
2019-06-30T12:21:44.987-0400   6 document(s) restored successfully. 0 document(s) failed to restore.
```

## Restore Collections Using Wild Cards

`--nsInclude` and
`--nsExclude` support specifying the
namespaces you wish to include or exclude from a
restore operation using asterisks as *wild cards*.

The following example restores the documents in the `dump/`
sub-directory of the current directory that match the specified
namespace pattern. The `--nsInclude`
statement specifies to only restore documents in the `transactions`
database while `--nsExclude`
instructs `mongorestore` to exclude collections whose
names end with `_dev`. `mongorestore` restores data to
the `mongod` instance running on the localhost interface
on port `27017`.

```sh
mongorestore --nsInclude='transactions.*' --nsExclude='transactions.*_dev' dump/
```

## Change Collection Namespaces during Restore

To change the namespace of the collection that you are restoring, use the 
`--nsFrom` and `--nsTo` 
options.

The `--nsFrom` and `--nsTo` options support using asterisks as wild cards *and*
support using dollar signs to delimit "wild card" variables to use in
the replacement.

Consider a database `data` that you have exported to a `dump/`
directory using `mongodump`. The `data` database
contains the following collections:

- `sales_customer1`
- `sales_customer2`
- `sales_customer3`
- `users_customer1`
- `users_customer2`
- `users_customer3`

Using `--nsFrom` and `--nsTo`, you can restore the data into different
namespaces. The following operation

- restores the `sales_<customerName>` collections in the `data`
  database to `sales` collections in the `<customerName>` database,
  and

- restores the `users_<customerName>` collections to `users`
  collections in the `<customerName>` database.

```sh
mongorestore --nsInclude="data.*" --nsFrom="data.$prefix$_$customer$" --nsTo="$customer$.$prefix$"
```

## Copy/Clone a Database

Starting in version 4.2, MongoDB removes the deprecated `copydb`
command and `clone` command.

As an alternative, users can use `mongodump` and
`mongorestore` (with the `mongorestore` options
`--nsFrom` and `--nsTo`).

For example, to copy the `test` database from a local instance
running on the default port 27017 to the `examples` database on the
same instance, you can:

#. Use `mongodump` to  dump the `test` database to
   an archive `mongodump-test-db`:

   ```sh
   mongodump --archive="mongodump-test-db" --db=test
   ```

#. Use `mongorestore` with `--nsFrom` and `--nsTo` to restore (with database name change) from the
   archive:

   ```sh
   mongorestore --archive="mongodump-test-db" --nsFrom="test.*" --nsTo="examples.*"
   ```

**Tip:**

Include additional options as necessary, such as to specify
the uri or host, username, password and authentication
database.

## Restore from an Archive File

To restore from an archive file, run `mongorestore` with the new
`--archive` option and the archive filename.

```sh
mongorestore --archive=test.20150715.archive 
```

### Restore a Database from an Archive File

To restore from an archive file, run `mongorestore` with the new
`--archive` option and the archive filename. For example, the
following operation restores the `test` database from the file
`test.20150715.archive`.

```sh
mongorestore --archive=test.20150715.archive  --nsInclude="test.*"
```

## Restore from Compressed Data

`mongorestore` can restore from compressed files or
compressed archive files created by `mongodump`.

To restore from a dump directory that contains compressed files, run
`mongorestore` with the `--gzip` option. For example, the following operation restores the `test`
database from the compressed files located in the default `dump`
directory:

```sh
mongorestore --gzip  --nsInclude="test.*" dump/
```

To restore from a compressed archive file, run
`mongorestore` with the `--gzip` option and the `--archive`
option. For example, the following operation restores the `test`
database from the archive file `test.20150715.gz`.

```sh
mongorestore --gzip --archive=test.20150715.gz --nsInclude="test.*"
```

To change the namespace of the collection that you are restoring, use the 
`--nsFrom` and `--nsTo` 
options with the `--gzip` option.

```sh
mongorestore --gzip --nsFrom="data.$prefix$_$customer$" --nsTo="$customer$.$prefix$"
```

## Restore a Time Series Collection

Use `mongosh` to create a time series collection. This example 
uses the default `test` database:

```javascript
db.createCollection(
   "weather",
   {
      timeseries: {
         timeField: "timestamp",
         metaField: "metadata",
         granularity: "hours"
      }
   }
)
```

Insert time series documents into the collection:

```javascript
db.weather.insertMany( [
   {
      "metadata": { "sensorId": 5578, "type": "temperature" },
      "timestamp": ISODate("2021-05-18T00:00:00.000Z"),
      "temp": 12
   },
   {
      "metadata": { "sensorId": 5578, "type": "temperature" },
      "timestamp": ISODate("2021-05-18T04:00:00.000Z"),
      "temp": 11
   },
   {
      "metadata": { "sensorId": 5578, "type": "temperature" },
      "timestamp": ISODate("2021-05-18T08:00:00.000Z"),
      "temp": 11
   }
] )
```

From your terminal, use `mongodump` to export the time series
collection to the `dump/test` directory:

```sh
mongodump --db=test
```

Use `mongorestore` to restore the data to the `mongorestore.weather`
namespace:

```sh
mongorestore --host localhost --port 27017 --nsFrom="test.*" --nsTo="mongorestore.*" dump/
```

## Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster that
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongorestore` similar to the following:

```none
mongorestore 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongorestore 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
```

**Note:**

If the AWS access key ID, secret access key, or session token
include the following characters:

```none
: / ? # [ ] @
```

those characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1).

Alternatively, the AWS access key ID, secret access key, and optionally
session token can each be provided outside of the connection string
using the `--username`, `--password`, and
`--awsSessionToken` options instead, like so:

```none
mongorestore 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, these three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongorestore` checks for the following environment variables when you
use the `MONGODB-AWS`
`authentication mechanism`:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`

If set, these credentials do not need to be specified in the connection
string or through their explicit options.

**Note:**

If you chose to use the AWS environment variables to specify these
values, you cannot mix and match with the corresponding explicit or 
connection string options for these credentials. Either use the
environment variables for access key ID *and* secret access key
(*and* session token if used), **or** specify each of these using the
explicit or connection string options instead.

The following example sets these environment variables in the `bash`
shell:

```none
export AWS_ACCESS_KEY_ID='<aws access key id>'
export AWS_SECRET_ACCESS_KEY='<aws secret access key>'
export AWS_SESSION_TOKEN='<aws session token>'
```

Syntax for setting environment variables in other shells will be
different. Consult the documentation for your platform for more
information.

You can verify that these environment variables have been set with the
following command:

```none
env | grep AWS
```

Once set, the following example connects to a MongoDB Atlas cluster
using these environment variables:

```none
mongorestore 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```

## Create and Restore Consistent Backup Files

To create a consistent `mongodump` backup file using oplog
entries, use the `mongodump --oplog` option. To restore data
from the backup file, use the `mongorestore --oplogReplay`
option.

**Note:**

To back up sharded clusters with `mongodump`, see backup-sharded-dumps.

The oplog contains the history of database write operations.

`mongodump` outputs:

- Collection documents, metadata, and options.
- Index definitions.
- Writes that occur during the `mongodump` run, if `--oplog` is
  specified.

### Use mongodump with oplog Option

`mongodump --oplog` creates a file named `oplog.bson` in the top
level of the `mongodump` output directory. The file contains write
operations that occur during the `mongodump` run. Writes that occur
after `mongodump` completes aren't recorded in the file.

### Use mongorestore with oplogReplay Option

To restore oplog entries from the `oplog.bson` file, use
`mongorestore --oplogReplay`. Use `mongodump --oplog` together with
`mongorestore --oplogReplay` to ensure the database is current and has
all writes that occurred during the `mongodump` run.

## Learn More

- mongorestore
- mongorestore-compatibility-and-installation
- Behavior
- manual-tutorial-backup-and-restore
- backup-sharded-dumps

- [mongosync utility](https://www.mongodb.com/docs/cluster-to-cluster-sync/current/reference/mongosync)
  for cluster to cluster migrations
- Migrate or import data in Atlas
- Back up, restore, and archive data
  in Atlas
