<!-- Converted from mongodump/mongodump-examples.txt (reStructuredText). Includes are inlined. -->

# mongodump Examples

This page shows examples for `mongodump`.

Run `mongodump` from the system command line, not the
`mongo` shell.

**Important:**

Considerations for mongodump backups

If write operations occur during `mongodump`, the backup might not
represent a single point in time. For a consistent backup, do one of
the following:

- Block writes at the application level. *Recommended for individual
  collection backups.*
- Use Fsync Lock to
  lock the deployment and pause all writes.
- For full replica set dumps, use
  mongodump-example-consistent-backup to capture writes during
  the dump.

For sharded clusters, see backup-sharded-dumps.

## Use `mongodump` with a Collection

The following operation creates a dump file that contains only the
collection named `records` in the database named `test`. In
the example, the database is running on the local interface on port
`27017`.

```sh
mongodump  --db=test --collection=records
```

## Use `mongodump` with a Database and Exclude Specified Collections

The following operation dumps all collections in the `test` database
except for `users` and `salaries`:

```sh
mongodump  --db=test --excludeCollection=users --excludeCollection=salaries
```

## Use `mongodump` with Access Control

In the next example, `mongodump` creates a database dump
located at `/opt/backup/mongodump-2011-10-24`, from a database
running on port `37017` on the host `mongodb1.example.net` and
authenticating using the username `user` as follows:

```sh
mongodump --host=mongodb1.example.net --port=37017 --username=user --authenticationDatabase=admin --out=/opt/backup/mongodump-2011-10-24
```

If you do not include the `--password`,
`mongodump` prompts the user for the password.

## Output to an Archive File

To output the dump to an archive file, run `mongodump` with the
`--archive` option and the archive filename. For example, the following
operation creates a file `test.20150715.archive` that contains the dump
of the `test` database.

```sh
mongodump --archive=test.20150715.archive --db=test
```

## Compress the Output

To compress the files in the output dump directory, run
`mongodump` with the new `--gzip` option. For example,
the following operation outputs compressed files into the default
`dump` directory.

```sh
mongodump --gzip --db=test
```

To compress the archive file output by `mongodump`, use the
`--gzip` option in conjunction with the `--archive`
option, specifying the name of the compressed file.

```sh
mongodump --archive=test.20150715.gz --gzip --db=test
```

## Copy and Clone Databases

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

## Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster which
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongodump` similar to the following:

```none
mongodump 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongodump 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
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
using the `--username`, 
`--password`, and
`--awsSessionToken` options instead, like so:

```none
mongodump 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, the previous three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongodump` checks for the following environment variables when you
use the `MONGODB-AWS`
`authentication mechanism`:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`

If set, these credentials do not need to be specified in the connection
string or via their explicit options.

**Note:**

If you chose to use the AWS environment variables to specify these
values, you cannot mix and match with the corresponding explicit or 
connection string options for these credentials. Either use the
environment variables for access key ID *and* secret access key
(*and* session token if used), **or** specify each of these using the
explicit or connection string options instead.

The following example sets environment variables in the `bash` shell:

```none
export AWS_ACCESS_KEY_ID='<aws access key id>'
export AWS_SECRET_ACCESS_KEY='<aws secret access key>'
export AWS_SESSION_TOKEN='<aws session token>'
```

The syntax for setting environment variables in other shells is
different. For more information, see the documentation for your shell.

To verify the environment variables are set, use this command:

```none
env | grep AWS
```

After you set the environment variables, run the following example to
connect to a MongoDB Atlas cluster:

```none
mongodump 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```

## Authenticating with a Specific Database

To authenticate with a different database than the one being dumped, you
must specify `authSource` in the MongoDB URI.

In this example:

- The username `myuser` and password `mypassword` is used. This user
  has read access to `testdb`.
- The `admin` database is used to authenticate the user.
- The `testdb` database is being dumped.

```none
mongodump 'mongodb+srv://myuser:mypassword@cluster0.example.com/?authSource=admin' --db testdb
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

- mongodump
- mongodump-compatibility-and-installation
- mongodump-behavior

- [mongosync utility](https://www.mongodb.com/docs/cluster-to-cluster-sync/current/reference/mongosync)
  for cluster to cluster migrations
- Migrate or import data in Atlas
- Back up, restore, and archive data
  in Atlas
