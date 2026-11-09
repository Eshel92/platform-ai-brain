<!-- Converted from mongodump.txt (reStructuredText). Includes are inlined. -->

# `mongodump`

**`mongodump`**

**`mongodump`**

 

## Definition

`mongodump` is a utility that creates a binary export of
a database's contents. `mongorestore` allows you to import data
that was exported from `mongodump`.

`mongodump` can export data from:

- Standalone deployments
- Replica sets
- Sharded clusters
- Flex clusters

You can use the MongoDB Database Tools to migrate from a self-hosted deployment
to [MongoDB Atlas](https://www.mongodb.com/docs/atlas). MongoDB
Atlas is the fully managed service for MongoDB deployments in the
cloud. To learn more, see [Seed with mongorestore](https://www.mongodb.com/docs/atlas/import/mongorestore/).

To learn all the ways you can migrate to MongoDB Atlas, see
[Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/).

`mongodump` can connect to `mongod` and
`mongos` instances.

You can restore the BSON files generated from `mongodump` into MongoDB
deployments running the same major version or feature compatibility version as 
the source deployment.

Run `mongodump` from the system command line, not the
`mongo` shell.

**Note:**

If you are archiving stale data to save on storage costs, consider
Online Archive in
[MongoDB Atlas](https://www.mongodb.com/cloud). Online
Archive features data tiering, which automatically archives infrequently
accessed data to fully-managed S3 buckets for availability.

Online Archive isn't supported on Atlas Infinite Database
clusters. See
Public Preview Availability.

`mongodump` dumps:

- Collection documents, metadata, and options.
- Index definitions.
- Writes that occur during the export, if run with the `mongodump`
  `--oplog` option.

`mongodump` dumps data to a directory or a binary archive file.

**Important:**

You can't use `mongodump` with a collection that uses Queryable Encryption or
client-side field level encryption (CSFLE).

### Dump Data to a Directory

Example `mongodump` directory dump structure and files:

```none
dump
├── easternSalesDatabase
│    ├── sales.bson
│    ├── sales.metadata.json
│    └── salesByMonthView.metadata.json 
├── westernSalesDatabase
│    ├── sales.bson
│    ├── sales.metadata.json
│    └── salesByMonthView.metadata.json
└── oplog.bson
```

For a directory dump, `mongodump` creates:

- A root directory with the default name `dump`. You can set the name
  with the `mongodump` `--out` option.
- A subdirectory in the root directory for each database. For example,
  if a database name is `easternSalesDatabase`, the subdirectory name
  is also `easternSalesDatabase`.
- A BSON file with documents for each collection. For example, if a
  collection name is `sales`, the BSON file is `sales.bson`.
- A metadata JSON file for each collection in each database directory.
  For example, a metadata `sales.metadata.json` file. The file
  contains a document with the exported collection metadata, options,
  and indexes.
- A metadata JSON file for each view. For example, a metadata
  `salesByMonthView.metadata.json` file. A view doesn't have a BSON
  file.
- An optional oplog `oplog.bson` file, located in the root
  directory, which contains write operations that occurred during the
  `mongodump` run. To output an `oplog.bson` file, use the
  `mongodump` `--oplog` option.

If you use the `mongodump` `--gzip` option,
the BSON files and JSON metadata files are compressed. The compressed
exported files have `bson.gz` and `metadata.json.gz` at the end of
the names.

### Dump Data to a Binary Archive File

To dump data to a binary archive file, use the `mongodump`
`--archive` option. `mongodump` creates
a binary file that contains the archived data.

If you run `mongodump` with the `--oplog`
option, the archive includes the oplog entries.

## Syntax

`mongodump` syntax:

```sh
mongodump <options> <connection-string>
```

**connect-to-an-instance:**

To connect to a local MongoDB instance running on port 27017 and
use the default settings to export the content, run `mongodump`
without any command-line options:

```sh
mongodump
```

To specify a host and/or port of the MongoDB instance, you can:

- Specify the hostname and port in the `--uri connection string` option:

  ```sh
  mongodump --uri="mongodb://mongodb0.example.com:27017" [additional options]
  ```

- Specify the hostname and port in the `--host` option:

  ```sh
  mongodump --host="mongodb0.example.com:27017"  [additional options]
  ```

- Specify the hostname and port in the `--host` and `--port` options:

  ```sh
  mongodump --host="mongodb0.example.com" --port=27017 [additional options]
  ```

**connect-to-a-replica-set:**

To connect to a replica set to export its data, you can:

- Specify the replica set name and members in the
  `--uri connection string` option:

  ```sh
  mongodump --uri="mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?replicaSet=myReplicaSetName" [additional options]
  ```

- Specify the replica set name and members in the
  `--host` option:

  ```sh
  mongodump --host="myReplicaSetName/mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com" [additional options]
  ```

By default, `mongodump` reads from the primary of the
replica set. To override the default, you can specify the read
preference:

- You can specify the read preference in the
  `--uri connection string` option:

  ```sh
  mongodump --uri="mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?replicaSet=myReplicaSetName&readPreference=secondary" [additional options]
  ```

  If specifying the read preference tags, include the
  `readPreferenceTags` option:

  ```sh
  mongodump --uri="mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?replicaSet=myReplicaSetName&readPreference=secondary&readPreferenceTags=region:east" [additional options]
  ```

- You can specify the read preference using the
  `--readPreference` command-line
  option. The command-line option takes a string if specifying only the read preference mode:

  ```sh
  mongodump --host="myReplicaSetName/mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017" --readPreference=secondary [additional options]
  ```

  Or, the command-line option can take a quote-enclosed document 
  `'{ mode: <mode>, tagSets: [ <tag1>, ... ], maxStalenessSeconds:<num>}'` 
  to specify the mode, the optional read preference tag
  sets, and the optional
  maxStalenessSeconds:

  ```sh
  mongodump --host="myReplicaSetName/mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017" --readPreference='{mode: "secondary", tagSets: [ { "region": "east" } ]}' [additional options]
  ```

**connect-to-a-sharded-cluster:**

**Note:**

To avoid data inconsistencies, pause the following actions on your
sharded cluster when you run `mongodump`:

- Cross-shard transactions
- Data definition language operations (operations that create and modify
  collections)
- Chunk balancing 

To stop the balancer, use the `sh.stopBalancer()` method. 

To connect to a sharded cluster to export its data, you can:

- Specify the hostname of the `mongos` instance in the
  `--uri connection string` option:

  ```sh
  mongodump --uri="mongodb://mongos0.example.com:27017" [additional options]
  ```

- Specify the hostname and port of the `mongos`
  instance in the `--host` option:

  ```sh
  mongodump --host="mongos0.example.com:27017" [additional options]
  ```

By default, `mongodump` reads from the primary of the
shard replica set. To override the default, you can specify the read
preference:

- You can specify the read preference in the
  `--uri connection string` option:

  ```sh
  mongodump --uri="mongodb://mongos0.example.com:27017/?readPreference=secondary" [additional options]
  ```

  If specifying the read preference tags, include the
  `readPreferenceTags` option:

  ```sh
  mongodump --uri="mongodb://mongos0.example.com:27017/?readPreference=secondary&readPreferenceTags=region:east" [additional options]
  ```

- You can specify the read preference using the
  `--readPreference` command-line
  option. The command-line option takes a string if specifying only the read preference mode:

  ```sh
  mongodump --host="mongos0.example.com:27017" --readPreference=secondary [additional options]
  ```

  Or, the command-line option can take a quote-enclosed document 
  `'{ mode: <mode>, tagSets: [ <tag1>, ... ], maxStalenessSeconds: <num>}'` 
  to specify the mode, the optional read preference tag
  sets, and the optional
  maxStalenessSeconds:

  ```sh
  mongodump --host="mongos0.example.com:27017" --readPreference='{mode: "secondary", tagSets: [ { "region": "east" } ]}' [additional options]
  ```

## Options

**`--help`**

Returns information on the options and use of `mongodump`.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times. For example: `-vvvvv`.

**`--quiet`**

Runs `mongodump` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- Output from database commands

- Replication activity

- Connection accepted and closed events

- All logs, including error messages, except for those that occur when
  parsing options

**`--version`**

Returns the `mongodump` release number.

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongodump` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongodump`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongodump` 
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
  `mongodump` command line options, the command line option overrides
  the corresponding configuration file option.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri="mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

Starting with version `100.0` of `mongodump`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongodump mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongodump --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
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

If using `mongodump` on Ubuntu 18.04, you may experience a
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

**`--host=<hostname><:port>, -h=<hostname><:port>`**

*Default*: localhost:27017

Specifies the resolvable hostname of the MongoDB deployment. By
default, `mongodump` attempts to connect to a MongoDB
instance running on the localhost on port number `27017`.

To connect to a replica set, specify the
`replSetName` and a seed list of set members, as in
the following:

```none
--host=<replSetName>/<hostname1><:port>,<hostname2><:port>,<...>
```

When specifying the replica set list format, `mongodump` always connects to
the primary. 

You can also connect to any single member of the replica set by specifying
the host and port of only that member:

```none
--host=<hostname1><:port>
```

If you use IPv6 and use the `<address>:<port>` format, you must
enclose the portion of an address and port combination in
brackets. For example: `[<address>]`.

Alternatively, you can also specify the hostname directly in the
`URI connection string`. Providing a connection
string while also using `--host` and specifying conflicting
information will result in an error.

**`--port=<port>`**

*Default*: 27017

Specifies the TCP port on which the MongoDB instance listens for
client connections.

Alternatively, you can also specify the port directly in the
`URI connection string`. Providing a connection
string while also using `--port` and specifying conflicting
information will result in an error.

**`--ssl`**

Enables a connection to a `mongod` or `mongos` that has
TLS/SSL support enabled.

Alternatively, you can also configure TLS/SSL support directly in the
`URI connection string`. Providing a connection
string while also using `--ssl` and specifying conflicting
information will result in an error.

**`--sslCAFile=<filename>`**

Specifies the `.pem` file that contains the root certificate chain
from the Certificate Authority. Specify the file name of the
`.pem` file using relative or absolute paths.

Alternatively, you can also specify the `.pem` file directly in the
`URI connection string`. Providing a connection
string while also using `--sslCAFile` and specifying conflicting
information will result in an error.

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

**`--sslPEMKeyPassword=<value>`**

Specifies the password to de-crypt the certificate-key file (i.e.
`--sslPEMKeyFile`). Use the ``--sslPEMKeyPassword` option only if the
certificate-key file is encrypted. In all cases, `mongodump` will
redact the password from all logging and reporting output.

If the private key in the PEM file is encrypted and you do not
specify the `--sslPEMKeyPassword` option, `mongodump` will
prompt for a passphrase. See ssl-certificate-password.

Alternatively, you can also specify the password directly in the
`URI connection string`. Providing a connection
string while also using `--sslPEMKeyPassword` and specifying conflicting
information will result in an error.

**Warning:**

On some systems, a password provided directly using the
`--sslPEMKeyPassword` option may be visible to system status
programs such as `ps` that may be invoked by other users. Consider
using the `--config` option to specify a configuration file
containing the password instead.

**`--sslCRLFile=<filename>`**

Specifies the `.pem` file that contains the Certificate
Revocation List. Specify the file name of the `.pem` file using
relative or absolute paths.

**`--sslAllowInvalidCertificates`**

Bypasses the validation checks for server certificates and allows the
use of invalid certificates. When using the
`allowInvalidCertificates` setting, MongoDB logs as
a warning the use of the invalid certificate.

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

   

**`--sslAllowInvalidHostnames`**

Disables the validation of the hostnames in TLS/SSL certificates.
Allows `mongodump` to connect to MongoDB instances even if the
hostname in their certificates do not match the specified hostname.

Alternatively, you can also disable hostname validation directly in the
`URI connection string`. Providing a connection
string while also using `--sslAllowInvalidHostnames` and specifying conflicting
information will result in an error.

**`--username=<username>, -u=<username>`**

Specifies a username with which to authenticate to a MongoDB database
that uses authentication. Use in conjunction with the ``--password
<mongodump --password>` and `--authenticationDatabase <mongodump
--authenticationDatabase>`` options.

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

See mongodump-example-connect-using-aws-iam for an example of each.

**`--password=<password>, -p=<password>`**

Specifies a password with which to authenticate to a MongoDB database
that uses authentication. Use in conjunction with the ``--username
<mongodump --username>` and `--authenticationDatabase <mongodump
--authenticationDatabase>`` options.

To prompt the user for the password, pass the ``--username <mongodump
--username>` option without `--password <mongodump --password>`` or
specify an empty string as the `--password <mongodump --password>`
value, as in `--password ""` .

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

See mongodump-example-connect-using-aws-iam for an example of each.

**Warning:**

On some systems, a password provided directly using the
`--password` option may be visible to system status programs
such as `ps` that may be invoked by other users. Consider instead:

- omitting the `--password` option to receive an interactive
  password prompt, or
- using the `--config` option to specify a configuration file
  containing the password.

**`--awsSessionToken=<AWS Session Token>`**

If connecting to a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) cluster
using the `MONGODB-AWS` `authentication mechanism`, and using session tokens in addition to
your AWS access key ID and secret access key, you can specify your AWS
session token in:

- this field,
- the `AWS_SESSION_TOKEN` `authMechanismProperties`
  parameter to the `connection string`, or
- the `AWS_SESSION_TOKEN` environment variable.

See mongodump-example-connect-using-aws-iam for an example of each.

Only valid when using the `MONGODB-AWS`
`authentication mechanism`.

**`--authenticationDatabase=<dbname>`**

Specifies the authentication database where the specified
`--username <mongodump --username>` has been created. See
user-authentication-database.

If you do not specify an authentication database, `mongodump`
assumes that the database specified to export holds the user's credentials.

If you do not specify an authentication database or a database to
export, `mongodump` assumes the `admin` database holds the user's
credentials.

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

Specifies the authentication mechanism the `mongodump` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongodump` adds support for
the `MONGODB-AWS` authentication mechanism when connecting
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
    cluster. See mongodump-example-connect-using-aws-iam.

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

**`--gssapiServiceName`**

Specify the name of the service using GSSAPI/Kerberos. Only required if the service does not use the
default name of `mongodb`.

This option is available only in MongoDB Enterprise.

Alternatively, you can also specify the service name directly in the
`URI connection string`. Providing a connection
string while also using `--gssapiServiceName` and specifying conflicting
information will result in an error.

**`--gssapiHostName`**

Specify the hostname of a service using ``GSSAPI/Kerberos
</core/kerberos>``. *Only* required if the hostname of a machine does
not match the hostname resolved by DNS.

This option is available only in MongoDB Enterprise.
   

**`--db=<database>, -d=<database>`**

Specifies a database to backup. If you do not specify a database,
`mongodump` copies all databases in this instance into the dump
files.

Alternatively, you can also specify the database directly in the
`URI connection string`. Providing a connection
string while also using `--db` and specifying conflicting
information will result in an error.

**`--collection=<collection>, -c=<collection>`**

Specifies a collection to backup. If you do not specify a collection,
this option copies all collections in the specified database or instance
to the dump files.

**`--query=<json>, -q=<json>`**

Provides a JSON document as a query that optionally limits
the documents included in the output of `mongodump`. To
use the `--query` option, you must also specify the
`--collection <mongodump --collection>` option.

You must enclose the query document in single quotes (`'{ ... }'`) to ensure 
that it does not interact with your shell environment.

The query must be in Extended JSON v2 format
(either relaxed or canonical/strict mode), including enclosing the field
names and operators in quotes. For example:

```sh
mongodump -d=test -c=records -q='{ "a": { "$gte": 3 }, "date": { "$lt": { "$date": "2016-01-01T00:00:00.000Z" } } }'
```

To use `$regex` with `mongodump`, use the following syntax: 

```sh
mongodump -d=sample_mflix -c=movies -q='{ "year": { "$regex": "20" } }'
```

Starting in MongoDB 9.0, the server matches dotted field paths to
`null` differently when an intermediate component of the path is an
array of scalar values. This change affects the `$eq`,
`$ne`, `$in`, and `$nin` operators.

For example, consider a collection that has the document
`{ "a": [ 1 ] }`. The path `a.b` doesn't exist in that document.

- In MongoDB 8.x and earlier, the predicate
  `{ "a.b": { "$ne": null } }` matches the document.

- Starting in MongoDB 9.0, the same predicate doesn't match the
  document, and the predicate `{ "a.b": { "$eq": null } }` matches it
  instead.

If your query uses such a predicate, the same `--query` value selects
a different set of documents on MongoDB 9.0 than on earlier versions.
An operation that filters on `{ "$ne": null }` returns fewer
documents. Review any query that compares a dotted path to `null`
before you dump or export data from a MongoDB 9.0 deployment. Confirm
that the query still selects the documents you expect.

**Note:**

When you use the `--query` option on a time series
collection, you can only query the
field specified as the `metaField`.

**`--queryFile=<path>`**

Specifies the path to a file containing a JSON document as a query
filter that limits the documents included in the output of
`mongodump`. `--queryFile` enables you to create
query filters that are too large to fit in your terminal's buffer.

**Note:**

When you use the `--queryFile` option on a time series
collection, you can only query the
field specified as the `metaField`.

**`--readPreference=<string|document>`**

*Default*: `primary`

Specifies the read preference for
`mongodump`. The `--readPreference` option can take:

- A string if specifying only the read preference mode:

  ```sh
  --readPreference=secondary
  ```

- A quote-enclosed document to specify the mode, the optional
  read preference tag sets, and the
  optional maxStalenessSeconds:

  ```sh
  --readPreference='{mode: "secondary", tagSets: [ { "region": "east" } ], maxStalenessSeconds: 120}'
  ```

  If specifying the maxStalenessSeconds, the value must be greater than or equal to 90.

`mongodump` defaults to `primary`
read preference.

If the read preference is also included in the
`--uri connection string <--uri>`, the command-line
`--readPreference` overrides the read preference specified in
the URI string.

**`--gzip`**

Compresses the output. If `mongodump` outputs to the dump
directory, the new feature compresses the individual files. The files
have the suffix `.gz`.

If `mongodump` outputs to an archive file or the standard
out stream, the new feature compresses the archive file or the data
output to the stream.
   

**`--out=<path>, -o=<path>`**

Specifies the directory where `mongodump` will write
BSON files for the dumped databases. By default,
`mongodump` saves output files in a directory named
`dump` in the current working directory.

To send the database dump to standard output, specify "`-`" instead of
a path. Write to standard output if you want process the output before
saving it, such as to use `gzip` to compress the dump. When writing
standard output, `mongodump` does not write the metadata that
writes in a `<dbname>.metadata.json` file when writing to files
directly.

You cannot use the `--archive` option with the
`--out` option.
   

**`--archive=<file>`**

Writes the output to a specified archive file or, if the archive
file is unspecified, writes to the standard output (`stdout`). An
archive file is a single-file alternative to multiple BSON files. 

- To output the dump to an archive file, run
  `mongodump` with the ``--archive <mongodump
  --archive>`` option and the archive filename.

  ```javascript
  mongodump --archive=<file>
  ```

- To output the dump to the standard output stream in order to pipe
  to another process, run `mongodump` with the
  `--archive <mongodump --archive>` option but *omit* the
  filename.

  ```javascript
  mongodump --archive
  ```

You cannot use the `--archive <mongodump --archive>` option
with the `--out <mongodump --out>` option.

**Note:**

If `mongodump` writes to an archive file,
`mongodump` performance can improve. For more information on
`mongodump` performance impacts, see Output Format
Considerations. 

**`--oplog`**

Captures any oplog entries that occur during the `mongodump`
operation so the dump reflects a single moment in time.

Where `mongodump` puts the oplog data depends on the output target:

- For a directory dump, `mongodump` writes the oplog entries to an
  `oplog.bson` file at the top level of the output directory.
- For an archive dump, the archive includes the oplog entries.

When you restore, replay the oplog entries with `mongorestore
--oplogReplay`. You can use `mongodump --oplog` together with
`mongorestore --oplogReplay` to ensure the data is current and
includes all the writes that occurred during the dump.

Without `--oplog`, if there are write operations during the dump
operation, the dump will not reflect a single moment in time. Changes
made to the database during the update process can affect the output of
the backup.

To back up individual replica sets while still accepting writes, use
`--oplog`.

**Important:**

A `mongodump` running with `--oplog` fails if
a client issues any of the listed operations during the dump
process.

- `renameCollection`
- `db.collection.renameCollection()`
- `db.collection.aggregate()` with `$out`
- `mapReduce` (this operation implicitly renames a
  collection)
- Operations that create or modify users, roles, or privileges                                                                                                                                           
- `setDefaultRWConcern` and other commands that 
  modify cluster-wide settings 

`--oplog` has no effect when running `mongodump` on a `mongos`
instance to dump the entire contents of a sharded cluster.

`--oplog` only works against nodes that maintain an
oplog. This includes all members of a replica set.

`--oplog` does not dump the oplog collection.

You can't run `mongodump` with `--oplog` on a sharded cluster. To back up 
sharded clusters with `mongodump`, see backup-sharded-dumps.

**Note:**

To use `mongodump` with `--oplog`, you must create a full dump of
a replica set member. `mongodump` with  `--oplog` fails
if you use any of the following options to limit the data to be dumped:

- `--db`
- `--collection`
- `--dumpDbUsersAndRoles`
- `--query`

**Warning:**

Don't change the feature compatibility version (FCV) between
MongoDB 8.x and MongoDB 9.0 while `mongodump --oplog` runs on a
deployment that has time series collections. The resulting dump
spans a time series format conversion, which
`mongorestore --oplogReplay` can't replay.

Starting in Database Tools 100.18.0, `mongodump` fails
instead of producing a dump that you can't restore. To learn
more, see mongorestore-time-series-format-conversion.

For an end-to-end example of using `mongodump --oplog` together
with `mongorestore --oplogReplay` to create a consistent
backup while accepting writes, see
mongodump-example-consistent-backup.

**`--dumpDbUsersAndRoles`**

Includes user and role definitions in the database's dump directory
when performing `mongodump` on a specific database. This
option applies only when you specify a database in the
`--db` option. MongoDB always includes user and role
definitions when `mongodump` applies to an entire instance
and not just a specific database.
   

**`--excludeCollection=<string>`**

Excludes the specified collection from the `mongodump` output.
To exclude multiple collections, specify the `--excludeCollection` multiple times.

To use the `--excludeCollection` option, you must specify a database. You can specify
a database with the `--db` option or in the
`--uri` connection string.

**`--excludeCollectionsWithPrefix=<string>`**

Excludes all collections with a specified prefix from the `mongodump`
outputs. To specify multiple prefixes, specify the `--excludeCollectionsWithPrefix` multiple
times.

To use the `--excludeCollectionsWithPrefix` option, you must specify a database. You can specify
a database with the `--db` option or in the 
`--uri` connection string.

**`--numParallelCollections=<int>, -j=<int>`**

*Default*: 4

Number of collections `mongodump` should export
in parallel.

**`--viewsAsCollections`**

When specified, `mongodump` exports views as collections.

**Note:**

Only views are exported. By default, `mongodump` only
exports a view's metadata. To export the documents in a view, use
the `--viewsAsCollections` option.

For each view, `mongodump` creates a BSON file containing
the documents in the view. If you use `mongorestore`
with a BSON file created by `mongodump`, the view is
restored as a collection.

If you do *not* include `--viewsAsCollections`,
`mongodump` captures each view's metadata. If you include a
view's metadata file in a `mongorestore` operation, the view
is recreated.

**`--compressors=<string>`**

Specifies the compression algorithm that `mongodump` uses for network
communication between the `mongodump` client and the MongoDB server.
You can use one or more of these values for the `--compressors`
option:

- `snappy`
- `zlib`
- `zstd`

If you specify multiple compression algorithms, `mongodump` uses the
first one in the list supported by your MongoDB deployment.

For more information on compressors, see the [Go driver network compression documentation](https://www.mongodb.com/docs/drivers/go/current/fundamentals/connections/network-compression/).

## Learn More

For more information about `mongodump`, see:

- mongodump-compatibility-and-installation
- mongodump-behavior
- mongodump-examples

For a tutorial, see backup-sharded-dumps.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.
