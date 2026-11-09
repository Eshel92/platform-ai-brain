<!-- Converted from mongoexport.txt (reStructuredText). Includes are inlined. -->

# `mongoexport`

**`mongoexport`**

**`mongoexport`**

This documentation is for version `{+version+}` of `mongoexport`.

## Synopsis

`mongoexport` is a database tool that produces a JSON
or CSV export of data stored in a MongoDB instance.
`mongoimport` provides the corresponding structured
data import capability.

Run `mongoexport` from the system command line, not the
`mongo` shell.

`mongoexport` is not a tool for backing up deployments. If you want to
create a backup solution, see manual-tutorial-backup-and-restore.

**Note:**

If you are archiving stale data to save on storage costs, consider
Online Archive in
[MongoDB Atlas](https://www.mongodb.com/cloud). Online
Archive features data tiering, which automatically archives infrequently
accessed data to fully-managed S3 buckets for availability.

Online Archive isn't supported on Atlas Infinite Database
clusters. See
Public Preview Availability.

You can use the MongoDB Database Tools to migrate from a self-hosted deployment
to [MongoDB Atlas](https://www.mongodb.com/docs/atlas). MongoDB
Atlas is the fully managed service for MongoDB deployments in the
cloud. To learn more, see [Seed with mongorestore](https://www.mongodb.com/docs/atlas/import/mongorestore/).

To learn all the ways you can migrate to MongoDB Atlas, see
[Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/).

## Syntax

`mongoexport` syntax:

```sh
mongoexport --collection=<coll> <options> <connection-string>
```

You must specify the `collection` to
export. If you do not specify an `output file`, `mongoexport` writes to the standard output (e.g.
stdout).

### Connect to a MongoDB Instance

To connect to a local MongoDB instance running on port 27017, you do
not have to specify the host or port.

For example, to export the specified `collection` to the specified `output file` from a local MongoDB instance running on port 27017:

```sh
mongoexport --collection=events --db=reporting --out=events.json
```

To specify a host and/or port of the MongoDB instance, you can either:

- Specify the hostname and port in the `--uri connection string`:

  ```sh
  mongoexport --uri="mongodb://mongodb0.example.com:27017/reporting"  --collection=events  --out=events.json [additional options]
  ```

  When using the `--uri connection string`,
  the database can be specified as part of the string.
  
- Specify the hostname and port in the `--host`:

  ```sh
  mongoexport --host="mongodb0.example.com:27017" --collection=events --db=reporting --out=events.json [additional options]
  ```

  
- Specify the hostname and port in the `--host` and `--port`:

  ```sh
  mongoexport --host="mongodb0.example.com" --port=27017 --collection=events --db=reporting --out=events.json [additional options]
  ```

For more information on the options available, see mongoexport-options.

### Connect to a Replica Set

**Note:**

`mongoexport` is not a tool for backing up data. To back up your
replica set, see manual-tutorial-backup-and-restore. 

To connect to a replica set to export its data, you can either:

- Specify the replica set name and members in the `--uri connection string`:

  ```sh
  mongoexport --uri="mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/reporting?replicaSet=myReplicaSetName" --collection=events --out=events.json [additional options]
  ```

  When using the `--uri connection string`,
  the database can be specified as part of the string.

- Specify the replica set name and members in the `--host`:

  ```sh
  mongoexport --host="myReplicaSetName/mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com" --collection=events --db=reporting --out=events.json [additional options]
  ```

By default, `mongoexport` reads from the primary of the
replica set. To override the default, you can specify the read
preference:

- You can specify the read preference in the
  `--uri connection string`

  ```sh
  mongoexport --uri="mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/reporting?replicaSet=myReplicaSetName&readPreference=secondary" --collection=events --out=events.json [additional options]
  ```

  If specifying the read preference tags, include the
  `readPreferenceTags` option:

  ```sh
  mongoexport --uri="mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/reporting?replicaSet=myReplicaSetName&readPreference=secondary&readPreferenceTags=region:east" --collection=events --out=events.json [additional options]
  ```

  When using the `--uri connection string`,
  the database can be specified as part of the string.

- You can specify the read preference using the
  `--readPreference` command-line
  option. The command-line option takes a string if specifying only the read preference mode:

  ```sh
  mongoexport --host="myReplicaSetName/mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017" --readPreference=secondary --collection=events --db=reporting --out=events.json [additional options]
  ```

  Or, the command-line option can takes a quote-enclosed document 
  `'{ mode: <mode>, tagSets: [ <tag1>, ... ], maxStalenessSeconds:<num>}'` 
  to specify the mode, the optional read preference tag
  sets, and the optional
  maxStalenessSeconds:
  

  ```sh
  mongoexport --host="myReplicaSetName/mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017" --readPreference='{mode: "secondary", tagSets: [ { "region": "east" } ]}' --collection=events --db=reporting --out=events.json [additional options]
  ```

For more information on the options available, see mongoexport-options.

### Connect to a Sharded Cluster

**Note:**

`mongoexport` is not a tool for backing up data. To back up your
sharded cluster, see backup-restore-sharded-clusters. 

To connect to a sharded cluster to export its data, you can either:

- Specify the hostname of the `mongos` instance in the
  `--uri connection string`

  ```sh
  mongoexport --uri="mongodb://mongos0.example.com:27017/reporting" --collection=events --out=events.json [additional options]
  ```

  
  When using the `--uri connection string`,
  the database can be specified as part of the string.

- Specify the hostname and port of the `mongos` instance in the `--host` 

  ```sh
  mongoexport --host="mongos0.example.com:27017" --collection=events --db=reporting --out=events.json[additional options]
  ```

By default, `mongoexport` reads from the primary of the
shard replica set. To override the default, you can specify the read
preference:

- You can specify the read preference in the
  `--uri connection string`

  ```sh
  mongoexport --uri="mongodb://mongos0.example.com:27017/reporting?readPreference=secondary" --collection=events --out=events.json [additional options]
  ```

  If specifying the read preference tags, include the
  `readPreferenceTags` option:

  ```sh
  mongoexport --uri="mongodb://mongos0.example.com:27017/reporting?readPreference=secondary&readPreferenceTags=region:east" --collection=events --out=events.json [additional options]
  ```

  When using the `--uri connection string`,
  the database can be specified as part of the string.

- You can specify the read preference using the
  `--readPreference` command-line
  option.  The command-line option takes a string if specifying only the read preference mode:

  ```sh
  mongoexport --host="mongos0.example.com:27017" --readPreference=secondary --collection=events --db=reporting --out=events.json [additional options]
  ```

  Or, the command-line option can takes a quote-enclosed document 
  `'{ mode: <mode>, tagSets: [ <tag1>, ... ], maxStalenessSeconds:<num>}'` 
  to specify the mode, the optional read preference tag
  sets, and the optional
  maxStalenessSeconds:
  

  ```sh
  mongoexport --host="mongos0.example.com:27017" --readPreference='{mode: "secondary", tagSets: [ { "region": "east" } ]}' --collection=events --db=reporting --out=events.json [additional options]
  ```

## Options

**`--help`**

Returns information on the options and use of `mongoexport`.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, (e.g. `-vvvvv`.)
   

**`--quiet`**

Runs `mongoexport` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- Output from database commands

- Replication activity

- Connection accepted and closed events

- All logs, including error messages, except for those that occur when
  parsing options

**`--version`**

Returns the `mongoexport` release number.

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongoexport` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongoexport`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongoexport` 
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
  `mongoexport` command line options, the command line option overrides
  the corresponding configuration file option.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri="mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

Starting with version `100.0` of `mongoexport`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongoexport mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongoexport --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
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

If using `mongoexport` on Ubuntu 18.04, you may experience a
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
default, `mongoexport` attempts to connect to a MongoDB
instance running on the localhost on port number `27017`.

To connect to a replica set, specify the
`replSetName` and a seed list of set members, as in
the following:

```none
--host=<replSetName>/<hostname1><:port>,<hostname2><:port>,<...>
```

When specifying the replica set list format, `mongoexport` always connects to
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

**`--port=<port>`**

*Default*: 27017

Specifies the TCP port on which the MongoDB instance listens for
client connections.

Alternatively, you can also specify the port directly in the
`URI connection string`. Providing a connection
string while also using `--port` and specifying conflicting
information will result in an error.

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
certificate-key file is encrypted. In all cases, the `mongoexport` will
redact the password from all logging and reporting output.

If the private key in the PEM file is encrypted and you do not specify
the `--sslPEMKeyPassword` option, the `mongoexport` will prompt for a passphrase. See
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

**`--sslCRLFile=<filename>`**

Specifies the `.pem` file that contains the Certificate Revocation
List. Specify the file name of the `.pem` file using relative or
absolute paths.

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
`mongoexport` to connect to MongoDB instances even if the hostname in their
certificates do not match the specified hostname.

Alternatively, you can also disable hostname validation directly in the
`URI connection string`. Providing a connection
string while also using `--sslAllowInvalidHostnames` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

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

See mongoexport-example-connect-using-aws-iam for an example of each.

**`--password=<password>, -p=<password>`**

Specifies a password with which to authenticate to a MongoDB database
that uses authentication. Use in conjunction with the `--username` and
`--authenticationDatabase` options.

To prompt the user for the password, pass the `--username`
option without `--password` or specify an empty string as the
`--password` value, as in `--password ""` .

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

See mongoexport-example-connect-using-aws-iam for an example of each.

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

See mongoexport-example-connect-using-aws-iam for an example of each.

Only valid when using the `MONGODB-AWS`
`authentication mechanism`.

**`--authenticationDatabase=<dbname>`**

Specifies the authentication database where the specified `--username` has been created.
See user-authentication-database.

If you do not specify an authentication database, `mongoexport`
assumes that the database specified to export holds the user's credentials.

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

Specifies the authentication mechanism the `mongoexport` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongoexport` adds support
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
    cluster. See mongoexport-example-connect-using-aws-iam.

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

**`--gssapiServiceName=<serviceName>`**

Specify the name of the service using GSSAPI/Kerberos. Only required if the service does not use the
default name of `mongodb`.

This option is available only in MongoDB Enterprise.
   

**`--gssapiHostName=<hostname>`**

Specify the hostname of a service using GSSAPI/Kerberos. *Only* required if the hostname of a machine does
not match the hostname resolved by DNS.

This option is available only in MongoDB Enterprise.
   

**`--db=<database>, -d=<database>`**

Specifies the name of the database on which to run the `mongoexport`.

Alternatively, you can also specify the database directly in the
`URI connection string`. Providing a connection
string while also using `--db` and specifying conflicting
information will result in an error.

**`--collection=<collection>, -c=<collection>`**

Specifies the collection to export.
   

**`--fields=<field1[,field2]>, -f=<field1[,field2]>`**

Specifies a field or fields to *include* in the export. Use a comma
separated list of fields to specify multiple fields.

If any of your field names include white space, use
quotation marks to enclose the field list. For example, if you wished
to export two fields, `phone` and `user number`, you would
specify `--fields "phone,user number"`.

For `csv` output formats,
`mongoexport` includes only the specified field(s), and the
specified field(s) can be a field within a sub-document.

For JSON output formats, `mongoexport` includes
only the specified field(s) **and** the `_id` field, and if the
specified field(s) is a field within a sub-document, the
`mongoexport` includes the sub-document with all
its fields, not just the specified field within the document.

See: mongoexport-fields-example for sample usage.
   

**`--fieldFile=<filename>`**

An alternative to `--fields`. The
`--fieldFile` option allows you to
specify in a file the field or fields to *include* in the export and is
**only valid** with the `--type` option
with value `csv`. The
file must have only one field per line, and the line(s) must end with
the LF character (`0x0A`).

`mongoexport` includes only the specified field(s). The
specified field(s) can be a field within a sub-document.

See mongoexport-fieldFile-example for sample usage.

**`--query=<JSON>, -q=<JSON>`**

Provides a query as a JSON document (enclosed in quotes) to 
return matching documents in the export. 

You must enclose the query document in single quotes (`'{ ... }'`) to ensure 
that it does not interact with your shell environment.

The query must be in Extended JSON v2 format
(either relaxed or canonical/strict mode), including enclosing the
field names and operators in quotes:

For example, given a collection named `records` in the database
`test` with the following documents:

```json
{ "_id" : ObjectId("51f0188846a64a1ed98fde7c"), "a" : 1, "date" : ISODate("1960-05-01T00:00:00Z") }
{ "_id" : ObjectId("520e61b0c6646578e3661b59"), "a" : 1, "b" : 2, "date" : ISODate("1970-05-01T00:00:00Z") }
{ "_id" : ObjectId("520e642bb7fa4ea22d6b1871"), "a" : 2, "b" : 3, "c" : 5, "date" : ISODate("2010-05-01T00:00:00Z") }
{ "_id" : ObjectId("520e6431b7fa4ea22d6b1872"), "a" : 3, "b" : 3, "c" : 6, "date" : ISODate("2015-05-02T00:00:00Z") }
{ "_id" : ObjectId("520e6445b7fa4ea22d6b1873"), "a" : 5, "b" : 6, "c" : 8, "date" : ISODate("2018-03-01T00:00:00Z") }
{ "_id" : ObjectId("5cd0de910dbce4346295ae28"), "a" : 15, "b" : 5, "date" : ISODate("2015-03-01T00:00:00Z") }
```

The following `mongoexport` uses the `-q` option
to export only the documents with the field `a` greater than or
equal to (`$gte`) `3` and the field `date` less than
(`$lt`) `ISODate("2016-01-01T00:00:00Z")`, which is
specified using the extended JSON v2 format (relaxed mode) for
dates ( ``{ "$date":
"YYYY-MM-DDTHH:mm:ss.mmm\<offset\>"}`` ): 

```bash
mongoexport -d=test -c=records -q='{ "a": { "$gte": 3 }, "date": { "$lt": { "$date": "2016-01-01T00:00:00.000Z" } } }' --out=exportdir/myRecords.json
```

The resulting file contains the following documents:

```json
{"_id":{"$oid":"520e6431b7fa4ea22d6b1872"},"a":3.0,"b":3.0,"c":6.0,"date":{"$date":"2015-05-02T00:00:00Z"}}
{"_id":{"$oid":"5cd0de910dbce4346295ae28"},"a":15.0,"b":5.0,"date":{"$date":"2015-03-01T00:00:00Z"}}
```

You can sort the results with the `--sort` option to
`mongoexport`.

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

**`--queryFile=<filename>`**

An alternative to `--query`. The
`--queryFile` option allows you to
specify in a file the query in Extended JSON v2 format. 

**`--type=<string>`**

*Default*: json

Specifies the file type to export. Specify `csv` for CSV
format or `json` for JSON format.

If you specify `csv`, then you must also use either
the `--fields` or the `--fieldFile` option to
declare the fields to export from the collection.
   

**`--out=<file>, -o=<file>`**

Specifies a file to write the export to. If you do not specify a file
name, the `mongoexport` writes data to standard output
(e.g. `stdout`).
   

**`--jsonFormat=<canonical|relaxed>`**

*Default*: relaxed

Modifies the output to use either canonical or relaxed mode of the
MongoDB Extended JSON (v2) format.

For differences between canonical and relaxed modes, see
MongoDB Extended JSON (v2).

**`--jsonArray`**

Modifies the output of `mongoexport` to write the
entire contents of the export as a single JSON array. By
default `mongoexport` writes data using one JSON document
for every MongoDB document.
   

**`--pretty`**

Outputs documents in a pretty-printed format JSON.
   

**`--noHeaderLine`**

By default, `mongoexport` includes the exported field names as the first
line in a CSV output. `--noHeaderLine` directs `mongoexport` to export the
data without the list of field names.
`--noHeaderLine` is **only valid** with the
`--type` option with value `csv`.

See mongoexport-noHeaderLine-example for sample usage.

**`--readPreference=<string|document>`**

*Default*: `primary`

Specifies the read preference for
`mongoexport`. The `--readPreference` option can take:

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

`mongoexport` defaults to `primary`
read preference.

If the read preference is also included in the
`--uri connection string`, the command-line
`--readPreference` overrides the read preference specified in
the URI string.

**`--skip=<number>`**

Use `--skip` to control where `mongoexport` begins
exporting documents. See `skip()` for information about
the underlying operation.

**`--limit=<number>`**

Specifies a maximum number of documents to include in the
export. See `limit()` for information about
the underlying operation.
   

**`--sort=<JSON>`**

Specifies an ordering for exported results. If an index does
**not** exist that can support the sort operation, the results must
be *less than* 32 megabytes.

Use `--sort` conjunction with `--skip` and
`--limit` to limit number of exported documents.

```sh
mongoexport -d=test -c=records --sort='{a: 1}' --limit=100 --out=export.0.json
mongoexport -d=test -c=records --sort='{a: 1}' --limit=100 --skip=100 --out=export.1.json
mongoexport -d=test -c=records --sort='{a: 1}' --limit=100 --skip=200 --out=export.2.json
```

See `sort()` for information about the underlying
operation.

## Learn More

- mongoexport-compatibility-and-installation
- mongoexport Behavior
- mongoexport-examples
