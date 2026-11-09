<!-- Converted from mongorestore.txt (reStructuredText). Includes are inlined. -->

# `mongorestore`

**`mongorestore`**

**`mongorestore`**

This documentation is for version `{+version+}` of `mongorestore`.

## Definition

The `mongorestore` program loads data from either a binary
database dump created by `mongodump` or the standard input
into a `mongod` or `mongos` instance. `mongorestore`
is installed when you install 
the MongoDB Database Tools.

You can use the MongoDB Database Tools to migrate from a self-hosted deployment
to [MongoDB Atlas](https://www.mongodb.com/docs/atlas). MongoDB
Atlas is the fully managed service for MongoDB deployments in the
cloud. To learn more, see [Seed with mongorestore](https://www.mongodb.com/docs/atlas/import/mongorestore/).

To learn all the ways you can migrate to MongoDB Atlas, see
[Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/).

You can restore the BSON files generated from `mongodump` into MongoDB
deployments running the same major version or feature compatibility version as 
the source deployment.

`mongorestore` has the following behaviors and limitations:

- You must run `mongorestore` from the system command line, not
  the [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/).

- MongoDB doesn't support running multiple `mongorestore` programs
  concurrently for the same collection.

- You can't use `mongorestore` with a collection that uses Queryable Encryption or
  client-side field level encryption (CSFLE).

## Syntax

Use the following command syntax when you run `mongorestore`:

```sh
mongorestore <options> <connection-string> <directory or file to restore>
```

See mongorestore-options for what options you can use when you run
`mongorestore`.

When you run `mongorestore` with no arguments, the default setting is to
restore data from a local `./dump` directory to a local `mongod`
instance running on port `27017`:

```sh
mongorestore
```

You can also specify a `dump` directory at a different path. For example, 
the following command restores data from a directory at `./downloads/dump`
to an Atlas cluster specified by a connection string:

```sh
mongorestore --uri="<my-connection-string>" ./downloads/dump
```

As `mongorestore` restores from the provided directory,
it creates the database and collections as needed and logs its progress:

```sh
2019-07-08T14:37:38.942-0400	preparing collections to restore from
2019-07-08T14:37:38.944-0400	reading metadata for test.bakesales from dump/test/bakesales.metadata.json
2019-07-08T14:37:38.944-0400	reading metadata for test.salaries from dump/test/salaries.metadata.json
2019-07-08T14:37:38.976-0400	restoring test.salaries from dump/test/salaries.bson
2019-07-08T14:37:38.985-0400	no indexes to restore
2019-07-08T14:37:38.985-0400	finished restoring test.salaries (10 documents, 0 failures)
2019-07-08T14:37:39.009-0400	restoring test.bakesales from dump/test/bakesales.bson
2019-07-08T14:37:39.011-0400	restoring indexes for collection test.bakesales from metadata
2019-07-08T14:37:39.118-0400	finished restoring test.bakesales (21 documents, 0 failures)
2019-07-08T14:37:39.118-0400	restoring users from dump/admin/system.users.bson
2019-07-08T14:37:39.163-0400	restoring roles from dump/admin/system.roles.bson
2019-07-08T14:37:39.249-0400	31 document(s) restored successfully. 0 document(s) failed to restore.
```

You can also restore a specific collection or collections from the
`dump` directory. For example, the following operation restores the
`test.purchaseorders` collection from corresponding data files in the `dump`
directory:

```sh
mongorestore --nsInclude=test.purchaseorders ./dump
```

If the `dump` directory does not contain the corresponding data file
for the specified namespace, `mongorestore` does not restore any data.
For example, the following command specifies a collection namespace 
that does not have corresponding data in the `dump` directory:

```sh
mongorestore --nsInclude=foo.bar dump/
```

`mongorestore` outputs the following messages:

```sh
2019-07-08T14:38:15.142-0400	preparing collections to restore from
2019-07-08T14:38:15.142-0400	0 document(s) restored successfully. 0 document(s) failed to restore.
```

If `mongorestore` cannot find database information from the `--nsInclude`
option, metadata file, or dump directory name, it restores to a `test` database.
For example, the following `mongorestore` command restores from a `bands.bson`
file:

```sh
mongorestore ./bands.bson
```

Because there's no namespace information or path like `./dump/music/bands.bson`,
`mongorestore` has the following output:

```sh
2026-01-23T11:26:31.821-0500	restoring test.bands from bands.bson
2026-01-23T11:26:31.867-0500	finished restoring test.bands (1 document, 0 failures)
2026-01-23T11:26:31.867-0500	1 document(s) restored successfully. 0 document(s) failed to restore.
```

`mongorestore` restores the data to a `bands` collection in the `test` database.
It creates the database and collection if they do not exist.

For more `mongorestore` examples, see mongorestore-examples.

## Options

This section includes information about all available options for 
`mongorestore`.

**`--archive=<file>`**

Restores from an archive created by `mongodump --archive`.
`mongorestore` restores from the specified archive file or, if you
do not specify a file, from the standard input (`stdin`).

To restore from an archive file, run `mongorestore` with the
`--archive` option and the archive filename. 

To restore from the standard input, run `mongorestore` with the 
`--archive` option and omit the filename.

The following example shows how to restore from the standard input:

```shell
mongodump --archive | mongorestore --archive
```

This command pipeline first runs `mongodump` with the `--archive` flag,
which prints its output to `stdout`, or standard output. Then, the input
is piped to `mongorestore`'s standard input by using the `|` pipe operator.

**Important:**

- You cannot use the `--archive` option with the `--dir`
  option, which specifies the dump directory.

- The `--db` and `--collection` options are
  deprecated when restoring from an archive file. To restore a specific
  database or collection, use `--nsInclude`.

- If you use the `--archive` option with the ``
  parameter, `mongorestore` ignores `<path>`.

**`--authenticationDatabase=<dbname>`**

Specifies the authentication database where the specified 
`--username` has been created.
Use in conjunction with the `--username` and 
`--password` options.

For more information on authentication databases, see user-authentication-database.

If you use the GSSAPI (Kerberos),
PLAIN (LDAP SASL), or `MONGODB-AWS`
`authentication mechanisms`, you
must set `--authenticationDatabase` to `$external`.

Alternatively, you can also specify the authentication database directly in the
`URI connection string`. Providing a connection
string while also using `--authenticationDatabase` and specifying conflicting
information will result in an error.

**`--authenticationMechanism=<name>`**

*Default*: SCRAM-SHA-1

Specifies the authentication mechanism the `mongorestore` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongorestore` adds support
for the `MONGODB-AWS` authentication mechanism when connecting
to a MongoDB Atlas cluster.

* - Value

  - Description

* - SCRAM-SHA-1

  - [RFC 5802](https://tools.ietf.org/html/rfc5802) standard
    Salted Challenge Response Authentication Mechanism using the SHA-1
    hash function.

* - SCRAM-SHA-256

  - [RFC 7677](https://tools.ietf.org/html/rfc7677) standard
    Salted Challenge Response Authentication Mechanism using the SHA-256
    hash function.

    Requires featureCompatibilityVersion set to `4.0`.

* - MONGODB-X.509

  - MongoDB TLS/SSL certificate authentication.

* - `MONGODB-AWS`

  - External authentication using AWS IAM credentials for use in
    connecting to a
    [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    cluster. See mongorestore-example-connect-using-aws-iam.

    **New in version:** 100.1.0

* - GSSAPI (Kerberos)

  - External authentication using Kerberos. This mechanism is
    available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).

* - PLAIN (LDAP SASL)

  - External authentication using LDAP. You can also use `PLAIN`
    for authenticating in-database users. `PLAIN` transmits
    passwords in plain text. This mechanism is available only in
    [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).

Alternatively, you can also specify the authentication mechanism directly in the
`URI connection string`. Providing a connection
string while also using `--authenticationMechanism` and specifying conflicting
information will result in an error.

**`--awsSessionToken=<AWS Session Token>`**

If connecting to a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) cluster
using the `MONGODB-AWS` `authentication mechanism`, and using session tokens in addition to
your AWS access key ID and secret access key, you can specify your AWS
session token in:

- this field,
- the `AWS_SESSION_TOKEN` `authMechanismProperties`
  parameter to the `connection string`, or
- the `AWS_SESSION_TOKEN` environment variable.

See mongorestore-example-connect-using-aws-iam for an example of each.

Only valid when using the `MONGODB-AWS`
`authentication mechanism`.

**`--bypassDocumentValidation`**

Enables `mongorestore` to bypass document validation
during the operation. This lets you insert documents that do not
meet the validation requirements.

**`--collection=<collection>, -c=<collection>`**

**Important:**

The use of `--db` and `--collection` options is
deprecated when restoring from a directory or an archive file.
To restore a specific database or collection from an archive or a directory, see
`--nsInclude`.

Specifies the name of the destination collection for `mongorestore` to
restore data *into* when restoring from a BSON file. If
you do not specify `--collection`, `mongorestore` takes
the collection name from the input filename. If the input file has an
extension, MongoDB omits the extension of the file from the collection
name.

```sh
mongorestore --db=reporting --collection=employeesalaries dump/test/salaries.bson 
```

**`--compressors=<string>`**

Specifies the compression algorithm that `mongodump` uses for network
communication between the `mongorestore` client and the MongoDB server.
You can use one or more of these values for the `--compressors`
option:

- `snappy`
- `zlib`
- `zstd`

If you specify multiple compression algorithms, `mongorestore` uses the
first one in the list supported by your MongoDB deployment.

For more information on compressors, see the [Go driver network compression documentation](https://www.mongodb.com/docs/drivers/go/current/fundamentals/connections/network-compression/).

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongorestore` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongorestore`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongorestore` 
command line options, such as `--username` and `--host`.

Be sure to secure this file with appropriate filesystem permissions.

**Important:**

When using the `--config` option, keep the following limitations and
behaviors in mind:

- If you provide the `password` field and provide a connection 
  string in the `uri` field with a conflicting password, 
  `mongorestore` throws an error.

- If you specify a configuration file with `--config` and also use
  the `--password`, `--uri`, or `--sslPEMKeyPassword`
  `mongorestore` command line options, the command line option overrides
  the corresponding configuration file option.

**`--convertLegacyIndexes`**

**New in version:** 100.0.0

Removes any invalid index options specified in the corresponding
`mongodump` output, and rewrites any legacy index key
values to use valid values.

- *Invalid index options* are any options specified to an index that
  are not listed as a valid field for
  the `createIndexes` command. For example, `name` and 
  `collation` are valid, but an arbitrary `custom_field` is not.
  With `--convertLegacyIndexes` specified, any invalid index
  options found are dropped.

- *Legacy index key values* are any values for
  index type that are
  no longer supported. For example,
  `1` and `-1` are valid index key values, but `0` or an empty
  string are legacy values. With `--convertLegacyIndexes`
  specified, any legacy index key values found are rewritten as
  `1`. Non-empty string values are not replaced.

Without the `--convertLegacyIndexes` option specified, the presence
of invalid index options or legacy index key values could cause the
index build to fail.

If the `--noIndexRestore`
option is specified to `mongorestore`, the
`--convertLegacyIndexes` option is ignored.

**`--db=<database>, -d=<database>`**

**Important:**

The use of `--db` and `--collection` options is
deprecated when restoring from a directory or an archive file.
To restore a specific database or collection from an archive or a directory, see
`--nsInclude`.

Specifies the destination database for `mongorestore` to restore data
*into* when restoring from a BSON file. If the database does not
exist, `mongorestore` creates the database. For example, the following
example restores the `salaries` collection into the `reporting` database.

```sh
mongorestore --db=reporting dump/test/salaries.bson 
```

If you do not specify `--db`, `mongorestore` reads the database name
from the data files.

Alternatively, you can also specify the database directly in the
`URI connection string`. Providing a connection
string while also using `--db` and specifying conflicting
information will result in an error.

**`--dir=string`**

Specifies the dump directory.

- You cannot specify both the `--dir` option and the `<path>`
  argument, which also specifies the dump directory, to `mongorestore`.

- You cannot use the `--archive` option with the `--dir` option.

**`--drop`**

Before restoring the collections from the dumped backup, drops the
collections from the target database. `--drop` does not drop
collections that are not in the backup.

When the restore includes the `admin` database, `mongorestore` with
`--drop` removes all user credentials and replaces them with the
users defined in the dump file. Therefore, in systems with
`authorization` enabled, `mongorestore` must be able
to authenticate to an existing user *and* to a user defined in the
dump file. If `mongorestore` can't authenticate to a user defined in the
dump file, the restoration process will fail, leaving an empty
database.

If a collection is dropped and recreated as part of the restore, the
newly created collection has a different UUID unless 
`--drop` is used with 
`--preserveUUID`.

**`--dryRun`**

Runs `mongorestore` without actually importing any data, returning the
`mongorestore` summary information. Use with `--verbose` to produce
more detailed summary information.

**`--fixDottedHashIndex`**

Creates all hashed indexes on dotted fields as 
single field ascending indexes on the destination database.

**`--gssapiHostName=<hostname>`**

Specify the hostname of a service using GSSAPI/Kerberos. *Only* required if the hostname of a machine does
not match the hostname resolved by DNS.

This option is available only in MongoDB Enterprise.
   

**`--gssapiServiceName=<serviceName>`**

Specify the name of the service using GSSAPI/Kerberos. Only required if the service does not use the
default name of `mongodb`.

This option is available only in MongoDB Enterprise.

**`--gzip`**

Restores from compressed files or data stream created by
`mongodump --gzip`.

To restore from a dump directory that contains compressed files, run
`mongorestore` with the `--gzip` option.

To restore from a compressed archive file, run `mongorestore` with
both the `--gzip` and the `--archive` options.

**Note:**

You can use the `--nsFrom` and
`--nsTo` options with the `--gzip` option to 
change the namespace of the collection that you are restoring.

**`--help`**

Returns information on the options and use of `mongorestore`.

**`--host=<hostname><:port>, -h=<hostname><:port>`**

*Default*: localhost:27017

Specifies the resolvable hostname of the MongoDB deployment. By
default, `mongorestore` attempts to connect to a MongoDB
instance running on the localhost on port number `27017`.

To connect to a replica set, specify the
`replSetName` and a seed list of set members, as in
the following:

```none
--host=<replSetName>/<hostname1><:port>,<hostname2><:port>,<...>
```

When specifying the replica set list format, `mongorestore` always connects to
the primary. 

You can also connect to any single member of the replica set by specifying
the host and port of only that member:

```none
--host=<hostname1><:port>
```

If you use IPv6 and use the `<address>:<port>` format, you must
enclose the portion of an address and port combination in
brackets (e.g. `[<address>]`).

Alternatively, you can also specify the hostname directly in the
`URI connection string`. Providing a connection
string while also using `--host` and specifying conflicting
information will result in an error.

**`--keepIndexVersion`**

Prevents `mongorestore` from upgrading the index to the latest
version during the restoration process.

**`--maintainInsertionOrder`**

*Default*: false

If specified, `mongorestore` inserts the documents in the
order of their appearance in the input source. That is, both the
bulk write batch order and document order within the batches are
maintained.

Specifying `--maintainInsertionOrder` also enables
`--stopOnError` and sets
`numInsertionWorkersPerCollection` to 1.

If unspecified, `mongorestore` may perform the insertions in
an arbitrary order.

**`--noIndexRestore`**

Prevents `mongorestore` from restoring and building indexes as
specified in the corresponding `mongodump` output.

**`--noOptionsRestore`**

Prevents `mongorestore` from setting the collection options,
such as those specified by the `collMod` database
command, on restored collections.

**`--nsExclude=<namespace pattern>`**

Specifies a namespace pattern (e.g. `"test.myCollection"`,
`"reporting.*"`, `"dept*.bar"`) to *exclude* the matching
namespaces from the restore. In the pattern, you can use asterisks
`*` as *wild cards*. For an example of the wildcard pattern, see
example-basic-wildcard-usage.

You can specify `--nsExclude` multiple times to exclude multiple namespace
patterns.

If you specify both `--nsExclude` and `--nsInclude`, the pattern 
that `--nsExclude` specifies takes precedence. For example, if you
specify both `--nsExclude="prod.*"` and `--nsInclude="prod.trips"`, 
no collections from the `prod` namespace are restored. 

**`--nsFrom=<namespace pattern>`**

Use with `--nsTo` to rename a namespace during the
restore operation. `--nsFrom` specifies the collection in the
dump file, while `--nsTo` specifies the name that should be
used in the restored database.

`--nsFrom` accepts a *namespace pattern* as its argument. The namespace
pattern permits `--nsFrom` to refer to any namespace that matches the
specified pattern. `mongorestore` matches the smallest valid occurence
of the namespace pattern.

For simple replacements, use asterisks (`*`) as wild cards.
Escape all literal asterisks and backslashes with a backslash.
Replacements correspond linearly to matches: each asterisk in
`--nsFrom` must correspond to an asterisk in `--nsTo`, and the
first asterisk in `--nsFrom` matches the first asterisk in `nsTo`.

For more complex replacements, use dollar signs to delimit a "wild
card" variable to use in the replacement.
example-complex-wildcard-usage provides an example of complex
replacements with dollar sign-delimited wild cards.

Unlike replacements with asterisks, replacements with dollar
sign-delimited wild cards do **not** need to be linear.

**`--nsInclude=<namespace pattern>`**

Specifies a namespace pattern (e.g. `"test.myCollection"`,
`"reporting.*"`, `"dept*.bar"`) to restore only the namespaces
that match the pattern. In the pattern, you can use asterisks `*`
as *wild cards*. For an example of the wildcard pattern, see
example-basic-wildcard-usage.

You can specify `--nsInclude` multiple times to include multiple namespace
patterns.

If source directory or file (i.e. the directory/file from which you
are restoring the data) does not contain data files that match the
namespace pattern, no data will be restored.

For collection names that contain non-ascii characters,
`mongodump` outputs the corresponding filenames with
percent-encoded names. However, to restore these collections, do not
use the encoded names. Instead, use the namespace with the non-ascii
characters.

For example, if the dump directory contains
`dump/test/caf%C3%A9s.bson`, specify `--nsInclude "test.cafés"`.

If you specify both `--nsExclude` and `--nsInclude`, the pattern 
that `--nsExclude` specifies takes precedence. For example, if you
specify both `--nsExclude="prod.*"` and `--nsInclude="prod.trips"`, 
no collections from the `prod` namespace are restored. 

**`--nsTo=<namespace pattern>`**

Use with `--nsFrom` to rename a namespace during the
restore operation. `--nsTo` specifies the new collection
name to use in the restored database, while
`--nsFrom` specifies the name in the dump file.

`--nsTo` accepts a *namespace pattern* as its argument. The namespace
pattern permits `--nsTo` to refer to any namespace that matches the
specified pattern. `mongorestore` matches the smallest valid occurence
of the namespace pattern.

For simple replacements, use asterisks (`*`) as wild cards.
Escape all literal asterisks and backslashes with a backslash.
Replacements correspond linearly to matches: each asterisk in
`--nsFrom` must correspond to an asterisk in `--nsTo`, and the
first asterisk in `--nsFrom` matches the first asterisk in `nsTo`.

For more complex replacements, use dollar signs to delimit a "wild
card" variable to use in the replacement.
example-complex-wildcard-usage provides an example of complex
replacements with dollar sign-delimited wild cards.

Unlike replacements with asterisks, replacements with dollar
sign-delimited wild cards do **not** need to be linear.

**`--numInsertionWorkersPerCollection=<int>`**

*Default*: 1

Specifies the number of insertion workers to run concurrently per collection.

For large imports, increasing the number of insertion workers
may increase the speed of the import.

**`--numParallelCollections=<int>, -j=<int>`**

*Default*: 4

Number of collections `mongorestore` should restore
in parallel.

If you specify `-j` when restoring a *single* collection, `-j`
maps to the `--numInsertionWorkersPerCollection` option rather than
`--numParallelCollections`.

**`--objcheck`**

**Deprecated since version:** 9.0

Forces `mongorestore` to validate all requests from clients
upon receipt to ensure that clients never insert invalid documents into
the database. For objects with a high degree of sub-document nesting,
`--objcheck` can have a small impact on performance.

Starting in MongoDB 9.0, this option has no effect on server
behavior. The server always validates BSON documents.

**`--oplogFile=<path>`**

Specifies the path to the oplog file containing oplog data for the
restore. Use with `--oplogReplay`. 

If you specify `--oplogFile` and there is an `oplog.bson`
file at the top level of the dump directory, `mongorestore` returns an 
error.

**Warning:**

Use `oplogFile` with caution: manually specifying the oplog
entries to apply might cause corruption and inconsistencies in the
restored data.

**`--oplogLimit=<timestamp>`**

Prevents `mongorestore` from applying oplog entries
with timestamp newer than or equal to `<timestamp>`. Specify
`<timestamp>` values in the form of `<time_t>:<ordinal>`, where
`<time_t>` is the seconds since the UNIX epoch, and `<ordinal>`
represents a counter of operations in the oplog that occurred in the
specified second.

**Warning:**

Use `oplogLimit` with caution: manually specifying the oplog
entries to apply might cause corruption and inconsistencies in the
restored data.

You must use `--oplogLimit` in conjunction with the
`--oplogReplay` option.

**`--oplogReplay`**

After restoring the database dump, replays the oplog entries
from an `oplog.bson` file.

**Note:**

Sharded clusters do not support the `oplogReplay` option.

To apply oplog entries from the `oplog.bson` file in the restore,
use `mongorestore --oplogReplay`. You can use `mongodump
--oplog` together with `mongorestore --oplogReplay` to ensure the
data is current and has all the writes that occurred during the dump
operation.

`mongorestore` searches for any valid source  for the bson file
in the following locations:

- The top level of the dump directory, as in the case of a dump created
  with `mongodump --oplog`.

- The path specified by `--oplogFile`.

- `<dump-directory>/local/oplog.rs.bson`, as in the case of a dump
  of the `oplog.rs` collection in the `local` database
  on a `mongod` that is a member of a replica set.

If there is an `oplog.bson` file at the top level of the dump
directory **and** a path specified by `--oplogFile`,
`mongorestore` returns an error.

If there is an `oplog.bson` file at the top level of the dump directory,
`mongorestore` restores that file as the oplog. If there are also bson
files in the `dump/local` directory, `mongorestore` restores them like
normal collections.

If you specify an oplog file using `--oplogFile`,
`mongorestore` restores that file as the oplog. If there are also bson
files in the `dump/local` directory, `mongorestore` restores them like
normal collections.

The following message in the oplog replay output shows the number of
inserts before the oplog replay. It does not include inserts
performed during the replay.

```sh
0 document(s) restored successfully. 0 document(s) failed to
restore.
```

For an example of `--oplogReplay`, see backup-restore-oplogreplay.

**Note:**

When using `mongorestore` with `--oplogReplay` to restore
a replica set, you must 
restore a full dump of a replica set member created 
using `mongodump --oplog`. 
`mongorestore` with `--oplogReplay` fails if you use any of 
the following options to limit the data to be restored:

- `--db`
- `--collection`
- `--nsInclude`
- `--nsExclude`
- `--nsFrom`
- `--nsTo`

**Warning:**

`mongorestore` can't replay an oplog range that spans a time
series format conversion. The server performs this conversion
when you change the feature compatibility version (FCV) between
MongoDB 8.x and MongoDB 9.0. To learn how to restore across a
conversion, see
mongorestore-time-series-format-conversion.

**See also:**

- mongorestore Required Access
- `mongodump --oplog`

**`--password=<password>, -p=<password>`**

Specifies a password with which to authenticate to a MongoDB database
that uses authentication. Use in conjunction with the `--username` and
`--authenticationDatabase` options.

To prompt the user for the password, pass the `--username`
option without `--password` or specify an empty string as the
`--password` value, as in `--password=""` .

Alternatively, you can also specify the password directly in the
`URI connection string`. Providing a connection
string while also using `--password` and specifying conflicting
information will result in an error.

If connecting to a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) cluster
using the `MONGODB-AWS` `authentication mechanism`, you can specify your AWS secret access
key in:

- this field,
- the `connection string`, or
- the `AWS_SECRET_ACCESS_KEY` environment variable.

See mongorestore-example-connect-using-aws-iam for an example of each.

**Warning:**

On some systems, a password provided directly using the
`--password` option may be visible to system status programs
such as `ps` that may be invoked by other users. Consider instead:

- omitting the `--password` option to receive an interactive
  password prompt, or
- using the `--config` option to specify a configuration file
  containing the password.

**`<path>`**

The directory path or BSON file name from which to restore data.

You cannot specify both the `<path>` argument and the `--dir`
option, which also specifies the dump directory, to `mongorestore`.

**`--port=<port>`**

*Default*: 27017

Specifies the TCP port on which the MongoDB instance listens for
client connections.

Alternatively, you can also specify the port directly in the
`URI connection string`. Providing a connection
string while also using `--port` and specifying conflicting
information will result in an error.

**`--preserveUUID`**

Restored collections use the UUID from the restore data instead of
creating a new UUID for collections that are dropped and recreated
as part of the restore.

To use `--preserveUUID`, you
must also include the `--drop` option.

**Note:**

Sharded clusters do not support the `preserveUUID` option.

**`--quiet`**

Runs `mongorestore` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- errors

- output from database commands

- replication activity

- connection accepted events

- connection closed events

**`--restoreDbUsersAndRoles`**

Restore user and role definitions for the given database. See
system.roles Collection
and
system.users Collection
for more information.

**Note:**

- You can only use `--restoreDbUsersAndRoles` on a database dump that 
  was created with the `--dumpDbUsersAndRoles` option. 

- Restoring the `admin` database by specifying 
  `--db admin` automatically restores all 
  users and roles. You cannot use `--restoreDbUsersAndRoles` 
  on the `admin` database, and attempting to do so results in an error. 

**`--ssl`**

Enables connection to a `mongod` or `mongos` that has
TLS/SSL support enabled.

Alternatively, you can also configure TLS/SSL support directly in the
`URI connection string`. Providing a connection
string while also using `--ssl` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

   

**`--sslAllowInvalidCertificates`**

Bypasses the validation checks for server certificates and allows
the use of invalid certificates. When using the
`allowInvalidCertificates` setting, MongoDB logs as a
warning the use of the invalid certificate.

**Warning:**

Although available, avoid using the
`--sslAllowInvalidCertificates` option if possible. If the use
of `--sslAllowInvalidCertificates` is necessary, only use the
option on systems where intrusion is not possible.

Connecting to a `mongod` or
`mongos` instance without validating server
certificates is a potential security risk. If you only need to
disable the validation of the hostname in the TLS/SSL
certificates, see `--sslAllowInvalidHostnames`.

Alternatively, you can also disable certificate validation directly in the
`URI connection string`. Providing a connection
string while also using `--sslAllowInvalidCertificates` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

   

**`--sslAllowInvalidHostnames`**

Disables the validation of the hostnames in TLS/SSL certificates. Allows
`mongorestore` to connect to MongoDB instances even if the hostname in their
certificates do not match the specified hostname.

Alternatively, you can also disable hostname validation directly in the
`URI connection string`. Providing a connection
string while also using `--sslAllowInvalidHostnames` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

**`--sslCAFile=<filename>`**

Specifies the `.pem` file that contains the root certificate chain
from the Certificate Authority. Specify the file name of the
`.pem` file using relative or absolute paths.

Alternatively, you can also specify the `.pem` file directly in the
`URI connection string`. Providing a connection
string while also using `--sslCAFile` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

**`--sslCRLFile=<filename>`**

Specifies the `.pem` file that contains the Certificate Revocation
List. Specify the file name of the `.pem` file using relative or
absolute paths.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

   

**`--sslPEMKeyFile=<filename>`**

Specifies the `.pem` file that contains both the TLS/SSL certificate
and key. Specify the file name of the `.pem` file using relative
or absolute paths.

This option is required when using the `--ssl` option to connect
to a `mongod` or `mongos` that has
`CAFile` enabled *without*
`allowConnectionsWithoutCertificates`.

Alternatively, you can also specify the `.pem` file directly in the
`URI connection string`. Providing a connection
string while also using `--sslPEMKeyFile` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

   

**`--sslPEMKeyPassword=<value>`**

Specifies the password to de-crypt the certificate-key file (i.e.
`--sslPEMKeyFile`). Use the `--sslPEMKeyPassword` option only if the
certificate-key file is encrypted. In all cases, the `mongorestore` will
redact the password from all logging and reporting output.

If the private key in the PEM file is encrypted and you do not specify
the `--sslPEMKeyPassword` option, the `mongorestore` will prompt for a passphrase. See
ssl-certificate-password.

Alternatively, you can also specify the password directly in the
`URI connection string`. Providing a connection
string while also using `--sslPEMKeyPassword` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

**Warning:**

On some systems, a password provided directly using the
`--sslPEMKeyPassword` option may be visible to system status
programs such as `ps` that may be invoked by other users. Consider
using the `--config` option to specify a configuration file
containing the password instead.

**`--stopOnError`**

Forces `mongorestore` to halt the restore when it encounters an
error.

By default, `mongorestore` continues when it encounters
duplicate key and document validation errors. To ensure that the
program stops on these errors, specify
`--stopOnError`.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri="mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

Starting with version `100.0` of `mongorestore`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongorestore mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongorestore --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
```

Only one connection string can be provided. Attempting to
include more than one, whether using the `--uri` option or as
a positional argument, will result in an error.

For information on the components of the connection string, see
the Connection String URI Format documentation. 

**Note:**

Some components in the `connection string` may
alternatively be specified using their own explicit command-line
options, such as `--username` and `--password`.
Providing a connection string while also using an explicit option and
specifying conflicting information will result in an error.

**Note:**

If using `mongorestore` on Ubuntu 18.04, you may experience a
`cannot unmarshal DNS` error message when using
SRV connection strings (in the
form `mongodb+srv://`) with the `--uri` option. If so, use
one of the following options instead:

- the `--uri` option with a non-SRV connection string (in the form
  `mongodb://`)
- the `--host` option to specify the host to connect to
  directly

**Warning:**

On some systems, a password provided in a connection string
with the `--uri` option may be visible to system status
programs such as `ps` that may be invoked by other users. Consider
instead:

- omitting the password in the connection string to receive an
  interactive password prompt, or
- using the `--config` option to specify a configuration file
  containing the password.

**`--username=<username>, -u=<username>`**

Specifies a username with which to authenticate to a MongoDB database
that uses authentication. Use in conjunction with the `--password` and
`--authenticationDatabase` options.

Alternatively, you can also specify the username directly in the
`URI connection string`. Providing a connection
string while also using `--username` and specifying conflicting
information will result in an error.

If connecting to a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) cluster
using the `MONGODB-AWS` `authentication mechanism`, you can specify your AWS access key ID
in:

- this field,
- the `connection string`, or
- the `AWS_ACCESS_KEY_ID` environment variable.

See mongorestore-example-connect-using-aws-iam for an example of each.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, (e.g. `-vvvvv`.)

**`--version`**

Returns the `mongorestore` release number.

**`--writeConcern=<document>`**

*Default*: majority

Specifies the write concern for each write operation that `mongorestore`
performs.

Specify the write concern as a document with w options:

```sh
--writeConcern="{w:'majority'}"
```

If the write concern is also included in the `--uri
connection string`, the command-line
`--writeConcern` overrides the write concern specified in
the URI string.

## Learn More

- mongorestore-compatibility-and-installation
- Behavior
- mongorestore-examples
- backup-sharded-dumps
