<!-- Converted from mongoimport.txt (reStructuredText). Includes are inlined. -->

# `mongoimport`

**`mongoimport`**

**`mongoimport`**

This documentation is for version `{+version+}` of `mongoimport`.

## Synopsis

`mongoimport` imports content from an
Extended JSON, CSV, or TSV export
created by `mongoexport`, or potentially, another third-party export
tool.

Run `mongoimport` from the system command line, not the 
`mongo` shell.

`mongoexport` provides data export capabilities.

You can use the MongoDB Database Tools to migrate from a self-hosted deployment
to [MongoDB Atlas](https://www.mongodb.com/docs/atlas). MongoDB
Atlas is the fully managed service for MongoDB deployments in the
cloud. To learn more, see [Seed with mongorestore](https://www.mongodb.com/docs/atlas/import/mongorestore/).

To learn all the ways you can migrate to MongoDB Atlas, see
[Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/).

**Tip:**

You can also import and export data using the graphical user 
interface tool MongoDB Compass. For details, see 
MongoDB Compass Import and Export.

## Syntax

`mongoimport` syntax:

```sh
mongoimport <options> <connection-string> <file>
```

## Options

**`--help`**

Returns information on the options and use of `mongoimport`.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, (e.g. `-vvvvv`.)
   

**`--quiet`**

Runs `mongoimport` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- output from database commands

- replication activity

- connection accepted events

- connection closed events

**`--version`**

Returns the `mongoimport` release number.

**`--config=<filename>`**

**New in version:** 100.3.0

Specifies the full path to a YAML configuration file that contains
sensitive values for the following `mongoimport` options: 

- `--password`
- `--uri`
- `--sslPEMKeyPassword`

This is the recommended way to specify a password to `mongoimport`,
aside from specifying it through a password prompt. You can use any combination
of the arguments in the file.

The configuration file takes the following form:

```sh
password: <password>
uri: mongodb://mongodb0.example.com:27017
sslPEMKeyPassword: <password>
```

If you specify the `password` option without specifying `uri`, you can
specify the other components of the connection string by using `mongoimport` 
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
  `mongoimport` command line options, the command line option overrides
  the corresponding configuration file option.

**`--uri=<connectionString>`**

Specifies the resolvable URI connection string of the MongoDB deployment, enclosed
in quotes:

```none
--uri "mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]"
```

**Note:**

If you don't specify a database with the `--db` or 
`--uri` option, `mongoimport` uses the 
`test` database by default. If the `test` database doesn't exist, 
`mongoimport` creates the database.

Starting with version `100.0` of `mongoimport`, the connection
string may alternatively be provided as a positional parameter,
without using the `--uri` option:

```none
mongoimport mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```

As a positional parameter, the connection string may be specified
at any point on the command line, as long as it begins with either
`mongodb://` or `mongodb+srv://`. For example:

```none
mongoimport --username joe --password secret1 mongodb://mongodb0.example.com:27017 --ssl
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

If using `mongoimport` on Ubuntu 18.04, you may experience a
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
default, `mongoimport` attempts to connect to a MongoDB
instance running on the localhost on port number `27017`.

To connect to a replica set, specify the
`replSetName` and a seed list of set members, as in
the following:

```none
--host=<replSetName>/<hostname1><:port>,<hostname2><:port>,<...>
```

When specifying the replica set list format, `mongoimport` always connects to
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
certificate-key file is encrypted. In all cases, the `mongoimport` redacts the password from all logging and reporting output.

If the private key in the PEM file is encrypted and you do not specify
the `--sslPEMKeyPassword` option, the `mongoimport` 
prompts for a passphrase. See ssl-certificate-password.

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
`allowInvalidCertificates` setting, MongoDB logs a
warning for invalid certificates.

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
`mongoimport` to connect to MongoDB instances even if the hostname in their
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

See mongoimport-example-connect-using-aws-iam for an example of each.

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

See mongoimport-example-connect-using-aws-iam for an example of each.

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

See mongoimport-example-connect-using-aws-iam for an example of each.

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

Specifies the authentication mechanism the `mongoimport` instance uses to
authenticate to the `mongod` or `mongos`.

**Changed in version:** 100.1.0

Starting in version `100.1.0`, `mongoimport` adds support
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
    cluster. See mongoimport-example-connect-using-aws-iam.

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

Specifies the name of the database on which to run the `mongoimport`.

Alternatively, you can also specify the database directly in the
`URI connection string`. Providing a connection
string while also using `--db` and specifying conflicting
information will result in an error.

**Note:**

If you don't specify a database with the `--db` or 
`--uri` option, `mongoimport` uses the 
`test` database by default. If the `test` database doesn't exist, 
`mongoimport` creates the database.

**`--collection=<collection>, -c=<collection>`**

Specifies the collection to import. If you do not specify
`--collection`, `mongoimport` reads the
collection name from the input filename, omitting the file's
extension if it has one.

**`--fields=<field1[,field2]>, -f=<field1[,field2]>`**

Specify a comma separated list of field names when importing CSV
or TSV files that do not have field names in the first (i.e.
header) line of the file. 

To also specify the field type as well as the field name, use
`--fields` with `--columnsHaveTypes`.

If you attempt to include `--fields` when importing JSON data,
`mongoimport` returns an error. `--fields` is only for CSV
or TSV imports.

**`--fieldFile=<filename>`**

As an alternative to `--fields`, the `--fieldFile`
option allows you to specify a file that holds a list of field names if
your CSV or TSV file does not include field names in the
first line of the file (i.e. header). Place one field per line.

To also specify the field type as well as the field name, use
`--fieldFile` with `--columnsHaveTypes`.

If you attempt to include `--fieldFile` when importing JSON data,
`mongoimport` returns an error. `--fieldFile` is only for CSV
or TSV imports.

**`--ignoreBlanks`**

Ignores empty fields in CSV and TSV exports. If not
specified, `mongoimport` creates fields without values in
imported documents.

If you attempt to include `--ignoreBlanks` when importing JSON data,
`mongoimport` returns an error. `--ignoreBlanks` is only for CSV
or TSV imports.

**`--type=<json|csv|tsv>`**

Specifies the file type to import. The default format is JSON,
but it's possible to import CSV and TSV files.

The `csv` parser accepts that data that complies with 4180. 
As a result, backslashes are *not* a valid escape character. If you use 
double-quotes to enclose fields in the CSV data, you must escape internal 
double-quote marks by prepending another double-quote.
   

**`--file=<filename>`**

Specifies the location and name of a file containing the data to import.
If you do not specify a file, `mongoimport` reads data from
standard input (e.g. "stdin").
   

**`--drop`**

Modifies the import process so that the target instance drops
the collection and any associated indexes before 
importing data from the input.
   

**`--headerline`**

If using `--type csv` or `--type
tsv`, uses the first line as field names.
Otherwise, `mongoimport` imports the first line as a
distinct document.

If you attempt to include `--headerline` when importing JSON data,
`mongoimport` returns an error. `--headerline` is only for CSV
or TSV imports.

**`--useArrayIndexFields`**

**New in version:** 100.0.0

Interpret natural numbers in fields as array indexes when importing
CSV or TSV files.

Field names must be in the form `<colName>.<arrayIndex>` where 
`arrayIndex` is a natural number beginning with `0` and
increasing sequentially by `1` for each member of the array.

For example, with the following CSV file:

```javascript
a.0,a.1,a.2,a.3
red,yellow,green,blue
```

An import with the `--useArrayIndexFields` option would
result in the following document:

```javascript
"a" : [ "red", "yellow", "green", "blue" ]
```

If using the `--columnsHaveTypes` option as well, use the
form `<colName>.<arrayIndex>.<type>(<arg>)` to specify both the
array index and type for each field. See `--columnsHaveTypes`
for more information.

Numerical keys with leading zeros (e.g. `a.000,a.001`) are not
interpreted as array indexes.

If the first part of a key is a natural number (e.g. `0.a,1.a`), it
is interpreted as a document key, and not an array index.

If using the `--ignoreBlanks` option with
`--useArrayIndexFields`, `mongoimport` returns an
error if you attempt to import a document that contains a
blank value (e.g. `""`) for an array index field.

The `--useArrayIndexFields` option has no effect when
importing JSON data, as arrays are already encoded in
JSON format.

**`--mode=<insert|upsert|merge|delete>`**

*Default*: insert

Specifies how the import process should handle existing documents
in the database that match documents in the import file.

By default, `mongoimport` uses the `_id` field to match documents in
the collection with documents in the import file.
To specify the fields against which to match existing
documents for the `upsert`, `merge`, and `delete` modes,
use `--upsertFields`.

* - Value
  - Description

* - `insert`

  - Insert the documents in the import file.
    `mongoimport` returns an error if you attempt to
    import a document that contains a duplicate value for a field
    with a unique index, such as `_id`.

* - `upsert`

  - Replace existing documents in the database with matching
    documents from the
    import file. `mongoimport` inserts all other
    documents. ex-mongoimport-upsert describes how to
    use `--mode` `upsert`.

* - `merge`

  - Merge existing documents that match a document in the import file with
    the new document. `mongoimport` inserts all other documents.
    ex-mongoimport-merge describes how to use `--mode`
    `merge`.

* - `delete`

  - Delete existing documents in the database that match a
    document in the import file. `mongoimport` takes
    *no action* on non-matching documents.
    ex-mongoimport-delete describes how to use
    `--mode` `delete`.

    **New in version:** 100.0.0

**`--upsertFields=<field1[,field2]>`**

Specifies a list of fields for the query portion of the
import process. `--upsertFields` can be used with
`--mode` `upsert`, `merge`, and `delete`.

Use this option if the `_id` fields in the
existing documents don't match the field in the document, but
another field or field combination can uniquely identify
documents as a basis for performing upsert operations.

If you do not specify a field, `--upsertFields` upserts
on the basis of the `_id` field.

To ensure adequate performance, indexes should exist for the
field or fields you specify with `--upsertFields`.

**`--stopOnError`**

Forces `mongoimport` to halt the insert operation at the
first error rather than continuing the operation despite errors.

By default, `mongoimport` continues an operation
when it encounters duplicate key and document validation errors. 
To ensure that the program stops on these errors, specify
`--stopOnError`.

**`--jsonArray`**

Accepts the import of data expressed with multiple MongoDB documents
within a single JSON array. Limited to
imports of 16 MB or smaller.

Use `--jsonArray` in conjunction with `mongoexport --jsonArray`.

**`--legacy`**

Indicates that the import data is in Extended JSON v1 format instead of the default
Extended JSON v2 format.

**Tip:**

In general, the versions of `mongoexport` and
`mongoimport` should match. That is, to import
data created from `mongoexport`, you should use
the corresponding version of `mongoimport`.

For example, if the import data is in v1 format:

```javascript
{"_id":1.0,"myregfield":{"$regex":"foo","$options":"i"}}
```

Import without the `--legacy` option results in
the following document in the collection:

```javascript
{ "_id" : 1, "myregfield" : { "$regex" : "foo", "$options" : "i" } }
```

Import with the `--legacy` results in
the following document in the collection:

```javascript
{ "_id" : 1, "myregfield" : { "$regularExpression" : { "pattern" : "foo", "options" : "i" } } }
```

**`--maintainInsertionOrder`**

*Default*: false

If specified, `mongoimport` inserts the documents in the
order of their appearance in the input source. That is, both the
bulk write batch order and document order within the batches are
maintained. 

Specifying `--maintainInsertionOrder` also enables
`--stopOnError` and sets
`numInsertionWorkers` to
1.

If unspecified, `mongoimport` may perform the insertions in
an arbitrary order.

**`--numInsertionWorkers=<int>`**

*Default*: 1

Specifies the number of insertion workers to run concurrently.

For large imports, increasing the number of insertion workers
may increase the speed of the import.
   

**`--writeConcern=<document>`**

*Default*: majority

Specifies the write concern for each write operation that `mongoimport`
performs.

Specify the write concern as a document with w options:

```sh
--writeConcern "{w:'majority'}"
```

If the write concern is also included in the `--uri
connection string`, the command-line
`--writeConcern` overrides the write concern specified in
the URI string.

**`--bypassDocumentValidation`**

Enables `mongoimport` to bypass document validation
during the operation. This lets you insert documents that do not
meet the validation requirements.

**`--columnsHaveTypes`**

Instructs `mongoimport` that the
field list specified in `--fields`, `--fieldFile`,
or `--headerline` specifies the types of each field.

Field names must be in the form of `<colName>.<type>(<arg>)`. You
must backslash-escape the following characters if you wish to include
them in an argument: `(`, `)`, and `\`.

* - `type`
  - Supported Arguments
  - Example Header Field

* - `auto()`
  - None.
  - `misc.auto()`

* - `binary(<arg>)`
  - - `base32` (RFC4648 encoding schema)
    - `base64` (RFC4648 encoding schema)
    - `hex`
  - `user thumbnail.binary(base64)`

* - `boolean()`
  - None.
  - `verified.boolean()`

* - `date(<arg>)`
  - Alias for `date_go(<arg>)`. Go Language time.Parse format.
  - `created.date(2006-01-02 15:04:05)`

* - `date_go(<arg>)`
  - Go Language time.Parse format
  - `created.date_go(2006-01-02T15:04:05Z)`

* - `date_ms(<arg>)`
  - [Microsoft SQL Server FORMAT format](https://msdn.microsoft.com/en-us/library/hh213505.aspx)
  - `created.date_ms(yyyy-MM-dd H:mm:ss)`

* - `date_oracle(<arg>)`
  - [Oracle Database TO_DATE format](https://docs.oracle.com/cd/B19306_01/server.102/b14200/functions183.htm).
  - `created.date_oracle(YYYY-MM-DD HH24:MI:SS)`

* - `decimal()`
  - None
  - `price.decimal()`

* - `double()`
  - None.
  - `revenue.double()`

* - `int32()`
  - None.
  - `followerCount.int32()`

* - `int64()`
  - None.
  - `bigNumber.int64()`

* - `string()`
  - None.
  - `zipcode.string()`

See example-csv-import-types for sample usage.

If you attempt to include `--columnsHaveTypes` when importing JSON data,
`mongoimport` returns an error. `--columnsHaveTypes` is only for CSV
or TSV imports.

**`--parseGrace=<grace>`**

*Default*: stop

Specifies how `mongoimport` handles type coercion failures when importing
CSV or TSV files with `--columnsHaveTypes`.

`--parseGrace` has no effect when importing JSON documents.

| Value | Description |
|---|---|
| `autoCast` | Assigns a type based on the value of the field. For example, if a field is defined as a `double` and the value for that field was `"foo"`, `mongoimport` would make that field value a string type. |
| `skipField` | For the row being imported, `mongoimport` does not include the field whose type does not match the expected type. |
| `skipRow` | `mongoimport` does not import rows containing a value whose type does not match the expected type. |
| `stop` | `mongoimport` returns an error that ends the import. |

   

## Learn More

- mongoimport-compatibility-and-installation
- mongoimport Behavior
- mongoimport-examples
- MongoDB Compass Import and Export
