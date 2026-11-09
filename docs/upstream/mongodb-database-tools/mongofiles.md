<!-- Converted from mongofiles.txt (reStructuredText). Includes are inlined. -->

**`mongofiles`**

**`mongofiles`**

# `mongofiles`

## Synopsis

The `mongofiles` utility makes it possible to manipulate files
stored in your MongoDB instance in GridFS objects from the
command line. It is particularly useful as it provides an interface
between objects stored in your file system and GridFS.

Run `mongofiles` from the system command line, not the `mongo` shell.

### Versioning

`mongofiles` is now released separately
from the MongoDB Server and uses its own versioning, with an initial
version of `100.0.0`. Previously, `mongofiles` was released
alongside the MongoDB Server and used matching versioning.

**Note:** Quick links to older documentation

- :v4.2:`MongoDB 4.2 mongofiles </reference/program/mongofiles>`
- :v4.0:`MongoDB 4.0 mongofiles </reference/program/mongofiles>`

This documentation is for version `{+version+}` of `mongofiles`. 

## Compatibility

### MongoDB Server Compatibility

`mongofiles` version `{+version+}` supports the following versions
of the MongoDB Server:

- MongoDB 9.0
- MongoDB 8.3
- MongoDB 8.2
- MongoDB 8.1
- MongoDB 8.0
- MongoDB 7.0
- MongoDB 6.0
- MongoDB 5.0
- MongoDB 4.4
- MongoDB 4.2

`mongofiles` does not support MongoDB Server versions earlier than
4.2. Attempts to connect to an earlier Server version fail.

### Platform Support

`mongofiles` version `{+version+}` is supported on the following
platforms:

|  | x86_64 | ARM64 | PPC64LE | s390x |
|---|---|---|---|---|
| Amazon Linux 2023 | ✓ | ✓ |  |  |
| Amazon 2 | ✓ | ✓ |  |  |
| Debian 12 | ✓ |  |  |  |
| Debian 11 | ✓ |  |  |  |
| Debian 10 | ✓ |  |  |  |
| Debian 9 | ✓ |  |  |  |
| RHEL (Red Hat Enterprise Linux) / CentOS 9 | ✓ | ✓ | ✓ | ✓ |
| RHEL (Red Hat Enterprise Linux) / CentOS 8 | ✓ |  | ✓ | ✓ |
| RHEL (Red Hat Enterprise Linux) / CentOS 7 | ✓ |  | ✓ | ✓ |
| RHEL (Red Hat Enterprise Linux) / CentOS 6 | ✓ |  |  |  |
| SUSE 15 | ✓ |  |  |  |
| SUSE 12 | ✓ |  |  |  |
| Ubuntu 24.04 | ✓ | ✓ |  |  |
| Ubuntu 22.04 | ✓ | ✓ |  |  |
| Ubuntu 20.04 | ✓ | ✓ |  |  |
| Ubuntu 18.04 | ✓ | ✓ |  |  |
| Ubuntu 16.04 | ✓ | ✓ | ✓ |  |
| Windows 11 and later | ✓ |  |  |  |
| Windows Server 2016 and later | ✓ |  |  |  |
| macOS 11 and later | ✓ | ✓ |  |  |
| macOS 10.12 - 10.15 | ✓ |  |  |  |

## Installation

The `mongofiles` tool is part of the *MongoDB Database Tools* package: 

→ Follow the Database Tools Installation Guide to install `mongofiles`.

## Syntax

The `mongofiles` command has the following form:

```sh
mongofiles <options> <connection-string> <command> <filename or _id>
```

Run `mongofiles` from the system command line, not the `mongo` shell.

The components of the `mongofiles` command are:

1. Options. You may use one or more of
   these options to control the behavior of `mongofiles`.

2. `Connection String`. The connection string
   of the `mongod` / `mongos` to connect to
   with `mongofiles`.

3. Command. Use one of these commands to
   determine the action of `mongofiles`.

4. An identifier which is either: the name of a file on your local file
   system, or a GridFS object.

**Important:**

For replica sets,
`mongofiles` can only read from the set's
primary.

## Required Access

In order to connect to a `mongod` that enforces authorization
with the `--auth` option, you must use the
`--username` and `--password` options. The connecting user must possess, at a
minimum:

- the `read` role for the accessed database when using the
  `list`, `search` or `get` commands,

- the `readWrite` role for the accessed database when using
  the `put` or `delete` commands.

## Behavior

### FIPS

`mongofiles` automatically creates FIPS-compliant
connections to a `mongod`/`mongos` that is
configured to use FIPS mode.

### Read Preference

By default, `mongofiles` uses read preference
`primary`. To override the default, you can specify the
read preference in the
`--readPreference` command line
option or in the `--uri connection string`.

If you specify read preference in the URI
string and the `--readPreference`,
the `--readPreference` value
overrides the read preference specified in the URI string.

### Write Concern

You can specify both the
`--writeConcern` and the
`--uri connection string` option. If write
concern is specified using both options, the
`--writeConcern` value overrides
the write concern specified in the URI string.

## Options

**`--help`**

Returns information on the options and use of `mongofiles`.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, (e.g. `-vvvvv`.)
   

**`--quiet`**

Runs `mongofiles` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- output from database commands

- replication activity

- connection accepted events

- connection closed events

**`--version`**

Returns the `mongofiles` release number.

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongofiles` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongofiles`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongofiles` 
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
  `mongofiles` command line options, the command line option overrides
  the corresponding configuration file option.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri="mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

Starting with version `100.0` of `mongofiles`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongofiles mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongofiles --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
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

If using `mongofiles` on Ubuntu 18.04, you may experience a
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

**`--host=<hostname><:port>`**

Specifies a resolvable hostname for the `mongod` that holds
your GridFS system. By default `mongofiles` attempts to connect
to a MongoDB process running on the localhost port number `27017`.

Optionally, specify a port number to connect a MongoDB instance running
on a port other than 27017.

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
certificate-key file is encrypted. In all cases, the `mongofiles` will
redact the password from all logging and reporting output.

If the private key in the PEM file is encrypted and you do not specify
the `--sslPEMKeyPassword` option, the `mongofiles` will prompt for a passphrase. See
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
`mongofiles` to connect to MongoDB instances even if the hostname in their
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

See mongofiles-example-connect-using-aws-iam for an example of each.

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

See mongofiles-example-connect-using-aws-iam for an example of each.

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

See mongofiles-example-connect-using-aws-iam for an example of each.

Only valid when using the `MONGODB-AWS`
`authentication mechanism`.

**`--authenticationDatabase=<dbname>`**

Specifies the authentication database where the specified `--username` has been created.
See user-authentication-database.

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

Specifies the authentication mechanism the `mongofiles` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongofiles` adds support
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
    cluster. See mongofiles-example-connect-using-aws-iam.

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

Specifies the name of the database on which to run the `mongofiles`.

Alternatively, you can also specify the database directly in the
`URI connection string`. Providing a connection
string while also using `--db` and specifying conflicting
information will result in an error.

**`--local=<filename>, -l=<filename>`**

Specifies the local filesystem name of a file for get and put
operations.

In the `mongofiles put` and `mongofiles get` commands,
the required `<filename>` modifier refers to the name the object will
have in GridFS. `mongofiles` assumes that this reflects the
file's name on the local file system. This setting overrides this
default.
   

**`--type=<MIME>`**

Provides the ability to specify a MIME type to describe the file
inserted into GridFS storage. `mongofiles` omits this option in
the default operation.

Use only with `mongofiles put` operations.
   

**`--replace, -r`**

Alters the behavior of `mongofiles put` to replace existing
GridFS objects with the specified local file, rather than adding an
additional object with the same name.

In the default operation, files will not be overwritten by a
`mongofiles put` option.
   

**`--prefix=<string>`**

*Default*: fs

GridFS prefix to use.
   

**`--writeConcern=<document>`**

*Default*: majority

Specifies the write concern for each write operation that `mongofiles`
performs.

Specify the write concern as a document with w options:

```sh
--writeConcern="{w:'majority'}"
```

If the write concern is also included in the `--uri
connection string`, the command-line
`--writeConcern` overrides the write concern specified in
the URI string.

**`--readPreference=<string|document>`**

*Default*: `primary`

Specifies the read preference for
`mongofiles`. The `--readPreference` option can take:

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

`mongofiles` defaults to `primary`
read preference.

If the read preference is also included in the
`--uri connection string`, the command-line
`--readPreference` overrides the read preference specified in
the URI string.

## Commands

**`list <prefix>`**

Lists the files in the GridFS store. The characters specified after
`list` (e.g. `<prefix>`) optionally limit the list of
returned items to files that begin with that string of characters.

**`search <string>`**

Lists the files in the GridFS store with names that match any
portion of `<string>`.

**`put <filename1[ filename2] ...>`**

Copy the specified file or files from the local file system into
GridFS storage. Multiple files can be specified as a space-separated 
list.

Each specified filename refers to the name the object will have in
GridFS, and `mongofiles` assumes that this reflects the
name the file has on the local file system. If the local filename is
different, use the `mongofiles --local` option.

**`get <filename1[ filename2] ...>`**

Copy the specified file or files from GridFS storage to the local
file system.

Each specified filename refers to the name the object has in
GridFS, and `mongofiles` will use this filename when
writing to the local file system.

If specifying *only one* `filename` to the `get` command, you can
use the `--local` option to specify a
different local filename to write to, if desired. The
`--local` option **cannot** be used if
specifying *more than one* `filename` to the `get` command.

**Note:**

To copy files from GridFS storage that match a regular expression,
use the `get_regex` command instead.

**`get_id "<_id>"`**

Copy the file, specified by its `<_id>`, from GridFS storage to the
local file system. `<_id>` refers to the extended JSON `_id` of
the object in GridFS. `get_id` can accept either ObjectId values or
non-ObjectId values for `<_id>`.

`mongofiles` writes the file to the local
file system using the file's filename in GridFS. To choose a
different location for the file on the local file system, use the
`--local` option.

**`get_regex <regex> --regexOptions <regex-options>`**

Copy the file or files, matched by the specified `<regex>`
expression, from GridFS storage to the local file system. The
`get_regex` command uses Perl compatible regular expressions
("PCRE") version 8.42 with UTF-8 support.

You may optionally specify one or more `<regex-options>` using the
`--regexOptions` flag. These can be any of the
options supported by the $regex operator, which include settings such as
case-insensitivity. Multiple options should be provided together
without separators, e.g. `--regexOptions si`

`mongofiles` writes the file or files to the local
file system using each file's matched filename in GridFS. You
**cannot** use the `--local` option with
the `get_regex` command.

**`delete <filename>`**

Delete the specified file from GridFS storage.

**`delete_id "<_id>"`**

Delete the file, specified by its `<_id>`, from GridFS storage.
`delete_id` can accept either ObjectId values or non-ObjectId
values for `<_id>`. 

## Examples

Run `mongofiles` from the system command line, not the `mongo` shell.

To return a list of all files in a GridFS collection in the
`records` database, use the following invocation at the system shell:

```sh
mongofiles -d=records list
```

This `mongofiles` instance will connect to the
`mongod` instance running on the `27017` localhost
interface to specify the same operation on a different port or
hostname, and issue a command that resembles one of the following:

```sh
mongofiles --port=37017 -d=records list
mongofiles --host=db1.example.net -d=records list
mongofiles --host=db1.example.net --port=37017 -d=records list
```

Modify any of the following commands as needed if you're connecting
the `mongod` instances on different ports or hosts.

To upload a file named `32-corinth.lp` to the GridFS collection in
the `records` database, you can use the following command:

```sh
mongofiles -d=records put 32-corinth.lp
```

To delete the `32-corinth.lp` file from this GridFS collection in
the `records` database, you can use the following command:

```sh
mongofiles -d=records delete 32-corinth.lp
```

To search for files in the GridFS collection in the `records`
database that have the string `corinth` in their names, you can use
following command:

```sh
mongofiles -d=records search corinth
```

To list all files in the GridFS collection in the `records` database
with names that begin with the string `32`, you can use the following
command:

```sh
mongofiles -d=records list 32
```

To fetch the file from the GridFS collection in the `records`
database named `32-corinth.lp`, you can use the following command:

```sh
mongofiles -d=records get 32-corinth.lp
```

To fetch all files from the GridFS collection in the `records`
database with names beginning with the string `32` and ending with the
string `.lp`, you can use the following command:

```sh
mongofiles -d=records get_regex 32*.lp
```

To fetch the file from the GridFS collection in the `records` database
with `_id: ObjectId("56feac751f417d0357e7140f")`, you can use the
following command:

```sh
mongofiles -d=records get_id '{"$oid": "56feac751f417d0357e7140f"}'
```

You must include quotation marks around the `_id`.

### Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster which
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongofiles` similar to the following:

```none
mongofiles 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongofiles 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
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
mongofiles 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, these three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongofiles` checks for the following environment variables when you
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
mongofiles 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```
