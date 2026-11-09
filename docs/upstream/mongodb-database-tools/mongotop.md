<!-- Converted from mongotop.txt (reStructuredText). Includes are inlined. -->

# `mongotop`

**`mongotop`**

**`mongotop`**

This documentation is for version `{+version+}` of `mongotop`.

## Synopsis

`mongotop` is a command-line tool that provides a method to track the amount
of time a MongoDB instance `mongod` spends reading and writing
data. `mongotop` provides statistics on a per-collection level.
By default, `mongotop` returns values every second.

## Syntax

`mongotop` syntax:

```sh
mongotop <options> <connection-string> <polling interval in seconds>
```

Running `mongotop` without any command-line options will
connect to the `mongod` instance running on localhost over
port `27017`, and will return values every second by default.

```sh
mongotop
```

To have `mongotop` report every 30 seconds, specify the
polling interval:

```sh
mongotop 30
```

When connected to a `mongod` instance, the program reports
first on the connection and then reports on the statistics at the
configured frequency.

```sh
2019-04-29T15:35:27.785-0400	connected to: 127.0.0.1

             ns    total      read      write    <timestamp>
<db.collection>    81802ms     0ms    81802ms   
...
```

### Command Line Options

```sh
mongotop [options] [frequency]
```

You can run `mongotop` with various command-line
options.
  
For example, to connect `mongotop` to a
`mongod` instance running on a remote host
`mongodb0.example.com` and report every 30 seconds:

- You can include the desired frequency of reporting (in this
  example, 30 seconds) and the `--uri`
  option to specify the host and port:

  ```sh
  mongotop 30 --uri='mongodb://mongodb0.example.com:27017' [additional options]
  ```

  If the `mongod` instance requires authentication, you
  can specify the user, password, and authentication database as part
  of the URI connection string:

  ```sh
  mongotop 30 --uri='mongodb://user:password@mongodb0.example.com:27017/?authSource=admin' [additional options]
  ```

  The user running `mongotop` must have the
  `serverStatus` and `top` privileges.

  For more information on the URI connection string, see
  `--uri`.

- Alternatively, you can use the `--host`
  and `--port` options to specify the host
  and port:

  ```sh
  mongotop 30 --host=mongodb0.example.com --port=27017 [additional options]
  ```

  If the `mongod` instance requires authentication, you
  can specify the user `-u`, and the
  authentication database `--authenticationDatabase`. Omit the `--password` option to have `mongoexport` prompt for the
  password.

  ```sh
  mongotop 30 --host=mongodb0.example.com --port=27017 -u=user --authenticationDatabase=admin [additional options]
  ```

  The user running `mongotop` must have the
  `serverStatus` and `top` privileges.

For more information on the options available, see
mongotop-options.

When connected to a `mongod` instance, the program reports
first on the connection and then reports on the statistics at the
configured frequency.

```sh
2019-04-29T15:35:27.785-0400	connected to: 127.0.0.1

             ns    total      read      write    <timestamp>
<db.collection>    81802ms     0ms    81802ms   
...
```

   

## Options

**`--help`**

Returns information on the options and use of `mongotop`.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, (e.g. `-vvvvv`.)
   

**`--quiet`**

Runs `mongotop` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- output from database commands

- replication activity

- connection accepted events

- connection closed events

**`--version`**

Returns the `mongotop` release number.

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongotop` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongotop`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongotop` 
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
  `mongotop` command line options, the command line option overrides
  the corresponding configuration file option.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri="mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

Starting with version `100.0` of `mongotop`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongotop mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongotop --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
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

If using `mongotop` on Ubuntu 18.04, you may experience a
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
default, `mongotop` attempts to connect to a MongoDB
instance running on the localhost on port number `27017`.

To connect to a replica set, specify the
`replSetName` and a seed list of set members, as in
the following:

```none
--host=<replSetName>/<hostname1><:port>,<hostname2><:port>,<...>
```

When specifying the replica set list format, `mongotop` always connects to
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

If connected to a replica set where the primary is not
reachable, `mongotop` returns an error message.

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
certificate-key file is encrypted. In all cases, the `mongotop` will
redact the password from all logging and reporting output.

If the private key in the PEM file is encrypted and you do not specify
the `--sslPEMKeyPassword` option, the `mongotop` will prompt for a passphrase. See
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
`mongotop` to connect to MongoDB instances even if the hostname in their
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

See mongotop-example-connect-using-aws-iam for an example of each.

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

See mongotop-example-connect-using-aws-iam for an example of each.

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

See mongotop-example-connect-using-aws-iam for an example of each.

Only valid when using the `MONGODB-AWS`
`authentication mechanism`.

**`--authenticationDatabase=<dbname>`**

Specifies the authentication database where the specified
`--username` has been created.
`--authenticationDatabase` is required for
`mongod` and `mongos` instances that use
authentication. See user-authentication-database.

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

Specifies the authentication mechanism the `mongotop` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongotop` adds support for
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
    cluster. See mongotop-example-connect-using-aws-iam.

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
   

**`--locks`**

Toggles the mode of `mongotop` to report on use of per-database
locks. This data is only available when connected to a
MongoDB 2.6 or older instance.

`--locks` returns an error when called against a `mongod` 3.0 or
newer instance that does not report per-database lock usage.

**`--rowcount=<int>, -n=<int>`**

Number of lines of data that `mongotop` should print. "0 for indefinite"

**`--json`**

Returns output for `mongotop` in JSON format. In
addition to timing data, the `--json` option also returns a count
of the number of operations which took place during the polling
interval. 

**`<sleeptime>`**

The final argument is the length of time, in seconds, that
`mongotop` waits in between calls. By default `mongotop` returns
data every second.

## Fields

When connected to a `mongod` instance, the program reports
first on the connection and then reports on the statistics at the
configured frequency. `mongotop` returns time values
specified in milliseconds (ms.)

```sh
2019-04-29T15:35:27.785-0400	connected to: 127.0.0.1

             ns    total      read      write    <timestamp>
<db.collection>    81802ms     0ms    81802ms   
...

             ns    total      read      write    <timestamp>
<db.collection>    0ms         0ms        0ms
...
```

`mongotop` only reports active namespaces or databases,
depending on the `--locks` option. If you don't see a database
or collection, it has received no recent activity. You can issue a
simple operation in the `mongo` shell to generate activity to
affect the output of `mongotop`.

**`mongotop.ns`**

Contains the database namespace, which combines the database name
and collection.

If you use the `mongotop --locks`, the `ns`
field does not appear in the `mongotop` output.

**`mongotop.db`**

Contains the name of the database. The database named `.` refers
to the global lock, rather than a specific database.

This field does not appear unless you have invoked
`mongotop` with the `--locks` option.

**`mongotop.total`**

Provides the total amount of time that this `mongod` spent
operating on this namespace.

**`mongotop.read`**

Provides the amount of time that this `mongod` spent
performing read operations on this namespace.

**`mongotop.write`**

Provides the amount of time that this `mongod` spent
performing write operations on this namespace.

**`mongotop.<timestamp>`**

Provides a time stamp for the returned data.

## Additional Information

For more information about monitoring MongoDB, see
Monitoring for MongoDB.

For additional background on various other MongoDB status outputs see:

- serverStatus
- replSetGetStatus
- dbStats
- collStats

For an additional utility that provides MongoDB metrics
see /mongostat.

## Learn More

- mongotop-compatibility-and-installation
- mongotop Behavior
- mongotop-examples
