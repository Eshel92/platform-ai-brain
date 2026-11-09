<!-- Converted from mongostat.txt (reStructuredText). Includes are inlined. -->

# `mongostat`

**`mongostat`**

**`mongostat`**

This documentation is for version `{+version+}` of `mongostat`.

## Synopsis

`mongostat` is a command-line tool that provides a quick overview of the
status of a currently running `mongod` or
`mongos` instance.  Use `mongostat` to help
identify system bottlenecks.

`mongostat` is functionally
similar to the UNIX/Linux file system utility `vmstat`, but provides
data regarding `mongod` and `mongos`
instances.

Run `mongostat` from the system command line, not the 
`mongo` shell.

## Syntax

`mongostat` syntax:

```sh
mongostat <options> <connection-string> <polling interval in seconds>
```

## Options

**`--help`**

Returns information on the options and use of `mongostat`.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, (e.g. `-vvvvv`.)
   

**`--version`**

Returns the `mongostat` release number.

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongostat` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongostat`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongostat` 
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
  `mongostat` command line options, the command line option overrides
  the corresponding configuration file option.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri="mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

Starting with version `100.0` of `mongostat`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongostat mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongostat --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
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

If using `mongostat` on Ubuntu 18.04, you may experience a
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
default, `mongostat` attempts to connect to a MongoDB
instance running on the localhost on port number `27017`.

To connect to a replica set, you can specify the set member or
members to report on, as in the following (see also the
`--discover` flag):

```none
--host=<hostname1><:port>,<hostname2><:port>,<...>
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
`--sslPEMKeyFile`). Use the
`--sslPEMKeyPassword` option
only if the certificate-key file is encrypted. In all cases, the
`mongostat` will redact the password from all logging and
reporting output.

If the private key in the PEM file is encrypted and you do not
specify the `--sslPEMKeyPassword` option, the `mongostat` will prompt
for a passphrase. See ssl-certificate-password.

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
`mongostat` to connect to MongoDB instances even if the hostname in their
certificates do not match the specified hostname.

Alternatively, you can also disable hostname validation directly in the
`URI connection string`. Providing a connection
string while also using `--sslAllowInvalidHostnames` and specifying conflicting
information will result in an error.

For more information about TLS/SSL and MongoDB, see
Configure mongod and mongos for TLS/SSL and
TLS/SSL Configuration for Clients.

**`--username=<username>, -u=<username>`**

Specifies a username with which to authenticate to a MongoDB
database that uses authentication. Use in conjunction with the
`--password` and
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

See mongostat-example-connect-using-aws-iam for an example of each.

**`--password=<password>, -p=<password>`**

Specifies a password with which to authenticate to a MongoDB
database that uses authentication. Use in conjunction with the
`--username` and
`--authenticationDatabase` options.

To prompt the user for the password, pass the `--username` option without
`--password` or specify an empty
string as the `--password` value, as
in `--password=""` .

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

See mongostat-example-connect-using-aws-iam for an example of each.

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

See mongostat-example-connect-using-aws-iam for an example of each.

Only valid when using the `MONGODB-AWS`
`authentication mechanism`.

**`--authenticationDatabase=<dbname>`**

Specifies the authentication database where the specified
`--username` has been created. See
user-authentication-database.

`--authenticationDatabase` is required for `mongod`
and `mongos` instances that use authentication.

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

Specifies the authentication mechanism the `mongostat` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongostat` adds support for
the `MONGODB-AWS` authentication mechanism when connecting to a
MongoDB Atlas cluster.

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
    cluster. See mongostat-example-connect-using-aws-iam.

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

**`--gssapiServiceName=<string>`**

Specify the name of the service using GSSAPI/Kerberos. Only required if the service does not use the
default name of `mongodb`.

This option is available only in MongoDB Enterprise.
   

**`--gssapiHostName=<string>`**

Specify the hostname of a service using GSSAPI/Kerberos. *Only* required if the hostname of a machine does
not match the hostname resolved by DNS.

This option is available only in MongoDB Enterprise.
   

**`--humanReadable=<boolean>`**

*Default*: true

When `true`, `mongostat` formats dates and quantity values for
easier reading, as in the following sample output:

```sh
insert query update delete getmore command dirty used flushes vsize  res qrw arw net_in net_out conn                time
   991    *0     *0     *0       0     2|0  3.4% 4.5%       0 2.90G 297M 0|0 0|0  12.9m   84.2k    2 Oct  6 09:45:37.478
   989    *0     *0     *0       0     2|0  3.6% 4.7%       0 2.91G 310M 0|0 0|0  12.9m   84.1k    2 Oct  6 09:45:38.476
   988    *0     *0     *0       0     1|0  3.7% 4.8%       0 2.92G 323M 0|0 0|0  12.8m   83.8k    2 Oct  6 09:45:39.481
   976    *0     *0     *0       0     2|0  3.9% 5.0%       0 2.94G 335M 0|0 0|0  12.7m   83.7k    2 Oct  6 09:45:40.476
```

When `false`, `mongostat` returns the raw data, as in the following
sample output:

```sh
insert query update delete getmore command dirty used flushes      vsize       res qrw arw   net_in net_out conn                      time
   992    *0     *0     *0       0     2|0   1.3  2.4       0 2941255680 149946368 0|0 0|0 12913607   84271    2 2016-10-06T09:45:25-04:00
   989    *0     *0     *0       0     1|0   1.5  2.6       0 2974810112 163577856 0|0 0|0 12873225   84087    2 2016-10-06T09:45:26-04:00
   996    *0     *0     *0       0     1|0   1.6  2.8       0 2972712960 177209344 0|0 0|0 12955423   84345    2 2016-10-06T09:45:27-04:00
   987    *0     *0     *0       0     1|0   1.8  2.9       0 2989490176 190840832 0|0 0|0 12861852   84008    2 2016-10-06T09:45:28-04:00
```

**`-o=<field list>`**

When output fields are specified with `-o`, only the
specified fields are included in the `mongostat` output.

Use dot notation to specify
`serverStatus fields`, as in
`metrics.document.inserted`.

A custom field name can include spaces. If you include a space, do
not put additional quotes around the field name. To specify a custom
name for a field, use `<field>=<customName>`, as in:

```sh
mongostat -o='host=H,time=T,version=MongoDB Version'
```

`-o` supports the following methods to modify the information
returned for a given serverStatus field:

**`.rate()`**

Use `.rate()` to view the rate per second at which a
serverStatus field is changing from `mongostat` call to
call.

ex-mongostat-rate illustrates how to use
`mongostat` with `-o` and the
`.rate()` method.

**`.diff()`**

Use `.diff()` to view how much a serverStatus field has
changed since the previous `mongostat` call. The
interval between calls is specified by `<sleeptime>`.

ex-mongostat-diff illustrates how to use
`mongostat` with `-o` and the
`.diff()` method.

`mongostat` supports specifying *either* `-o` or `-O`: you cannot include
both options.

See ex-mongostat-specify-columns for an example of
`-o`.

**`-O=<field list>`**

When specified, `mongostat` includes the specified
`serverStatus` fields after the default
`mongostat` output.

Use dot notation to specify
`serverStatus fields`, as in
`metrics.document.inserted`.

A custom field name can include spaces. If you include a space, do
not put additional quotes around the field name. To specify a custom
name for a field, use `<field>=<customName>`, as in:

```sh
mongostat -O=host=H,time=T
```

`mongostat` supports specifying *either* `-O` or `-o`: you cannot include
both options.

See ex-mongostat-append-columns for an example of
`-O`.

**`--noheaders`**

Disables the output of column or field names.
   

**`--rowcount=<number>, -n=<number>`**

Controls the number of rows to output. Use in conjunction with
the `sleeptime` argument to control the duration of a
`mongostat` operation.

Unless `--rowcount` is specified, `mongostat`
will return an infinite number of rows (e.g. value of `0`.)

**`--discover`**

Discovers and reports on statistics from all members of a replica
set or sharded cluster. When connected to any member of a
replica set, `--discover` all non-hidden members of the replica set. When connected to a `mongos`,
`mongostat` will return data from all shards in
the cluster. If a replica set provides a shard in the sharded cluster,
`mongostat` will report on non-hidden members of that replica
set.

The `mongostat --host` option is not required but
potentially useful in this case.

When running with `--discover`,
`mongostat` respects
`--rowcount`.

**`--all`**

Configures `mongostat` to return all optional fields.
   

**`--json`**

Returns output for `mongostat` in JSON format.

**`--interactive`**

Display `mongostat` output in an interactive non-scrolling interface
rather than the default scrolling output.

`--interactive` is not available with the `--json`
option.

See: example-mongostat-interactive for an example of `--interactive`.

**`<sleeptime>`**

*Default*: 1

The final `mongostat` argument is the length of time, in seconds, that
`mongostat` waits in between calls. By default `mongostat`
returns one call every second.

`mongostat` returns values that reflect the operations
over a 1 second period. For values of `<sleeptime>` greater
than 1, `mongostat` averages data to reflect average
operations per second.

## Fields

`mongostat` returns values that reflect the operations over a
1 second period. When `mongostat` has a value
greater than 1, `mongostat` averages the statistics to reflect
average operations per second.

`mongostat` outputs the following fields:

**`inserts`**

The number of objects inserted into the database per second. If
followed by an asterisk (e.g. `*`), the datum refers to a
replicated operation.

**`query`**

The number of query operations per second.

**`update`**

The number of update operations per second.

**`delete`**

The number of delete operations per second.

**`getmore`**

The number of get more (i.e. cursor batch) operations per second.

**`command`**

The number of commands per second. On 
secondary systems, `mongostat` presents two values
separated by a pipe character (e.g. `|`), in the form of
`local|replicated` commands.

**`flushes`**

For the storage-wiredtiger, `flushes` refers to the number
of WiredTiger checkpoints triggered between each polling interval.

**`dirty`**

Only for storage-wiredtiger. The percentage of the WiredTiger
cache with dirty bytes, calculated by
`wiredTiger.cache.tracked dirty bytes in the cache`
/ `wiredTiger.cache.maximum bytes configured`.

**`used`**

Only for storage-wiredtiger. The percentage of the WiredTiger
cache that is in use, calculated by
`wiredTiger.cache.bytes currently in the cache` /
`wiredTiger.cache.maximum bytes configured`.

**`vsize`**

The amount of virtual memory in megabytes used by the process at
the time of the last `mongostat` call.

**`res`**

The amount of resident memory in megabytes used by the process at
the time of the last `mongostat` call.

**`locked`**

The percent of time in a global write lock. Only appears when
`mongostat` runs against pre-3.0 versions of MongoDB
instances.

**`qr`**

The length of the queue of clients waiting to read data from the
MongoDB instance.

**`qw`**

The length of the queue of clients waiting to write data from the
MongoDB instance.

**`ar`**

The number of active clients performing read operations.

**`aw`**

The number of active clients performing write operations.

**`netIn`**

The amount of network traffic, in *bytes*, received by the MongoDB instance.

This includes traffic from `mongostat` itself.

**`netOut`**

The amount of network traffic, in *bytes*, sent by the MongoDB instance.

This includes traffic from `mongostat` itself.

**`conn`**

The total number of open connections.

**`set`**

The name, if applicable, of the replica set.

**`repl`**

The replication status of the member.

| Value | Replication Type |
|---|---|
| `PRI` | primary |
| `SEC` | secondary |
| `REC` | recovering |
| `UNK` | unknown |
| `RTR` | `mongos` process ("router") |
| `ARB` | arbiter |

## Additional Information

For more information about monitoring MongoDB, see
Monitoring for MongoDB.

For more background on other MongoDB status outputs see:

- serverStatus
- replSetGetStatus
- dbStats
- collStats

For an additional utility that provides MongoDB metrics see
/mongotop.

## Learn More

- mongostat-compatibility-and-installation
- mongostat Behavior
- mongostat-examples
