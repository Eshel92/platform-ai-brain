<!-- Converted from mongoexport/mongoexport-examples.txt (reStructuredText). Includes are inlined. -->

# mongoexport Examples

This page shows examples for `mongoexport`.

Run `mongoexport` from the system command line, not the 
`mongo` shell.

## Export in CSV Format

### Export Data in CSV Format using `--fields` option

In the following example, `mongoexport` exports data from the
collection `contacts` collection in the `users` database in CSV
format to the file `/opt/backups/contacts.csv`.

The `mongod` instance that `mongoexport` connects to is
running on the localhost port number `27017`.

When you export in CSV format, you must specify the fields in the documents
to export. The operation specifies the `name` and `address` fields
to export.

```sh
mongoexport --db=users --collection=contacts --type=csv --fields=name,address --out=/opt/backups/contacts.csv
```

The output would then resemble:

```none
name, address
Sophie Monroe, 123 Example Road
Charles Yu, 345 Sample Street
```

### Use a File to Specify the Fields to Export in CSV Format

For CSV exports only, you can also specify the fields in a file
containing the line-separated list of fields to export. The file must
have only one field per line.

For example, you can specify the `name` and `address` fields in a
file `fields.txt`:

```none
name
address
```

Then, using the `--fieldFile` option, specify the fields to export with
the file:

```sh
mongoexport --db=users --collection=contacts --type=csv --fieldFile=fields.txt --out=/opt/backups/contacts.csv
```

### Exclude Field Names from CSV Output

The `--noHeaderLine` option can be
used to exclude field names in a CSV export. The following example
exports the `name` and `address` fields in the `contacts`
collection in the `users` database and uses
`--noHeaderLine` to suppress the
output of the field names as the first line:

```sh
mongoexport --db=users --collection=contacts --type=csv --fields=name,address --noHeaderLine --out=/opt/backups/contacts.csv
```

The CSV output would then resemble:

```none
Sophie Monroe, 123 Example Road
Charles Yu, 345 Sample Street
```

## Export in JSON Format

This example creates an export of the `contacts` collection from the
MongoDB instance running on the localhost port number `27017`. This
writes the export to the `contacts.json` file in JSON format.

```sh
mongoexport --db=sales --collection=contacts --out=contacts.json
```

## Export from Remote Host Running with Authentication

The following example exports the `contacts` collection in the
`marketing` database from a remote MongoDB instance that requires
authentication.

Specify the:

- `--host`

- `--port`

- `--username`

- `--authenticationDatabase`

- `--collection`

- `--db`

- `--out`

**Tip:**

Omit the `--password` option to
have `mongoexport` prompt for the password:

```sh
mongoexport --host=mongodb1.example.net --port=27017 --username=someUser --authenticationDatabase=admin --collection=contacts --db=marketing --out=mdb1-examplenet.json
```

Alternatively, you use the `--uri` option to specify the host, port, username, authentication database, and db.

**Tip:**

Omit the password in the URI string to have `mongoexport` prompt
for the password:

```sh
mongoexport --uri='mongodb://someUser@mongodb0.example.com:27017/marketing?authsource=admin' --collection=contacts --out=mdb1-examplenet.json
```

## Export Query Results

You can export only the results of a query by supplying a query filter with
the `--query` option, and limit the results to a single
database using the "`--db`" option.

For instance, this command returns all documents in the `sales`
database's `contacts` collection that contain a field named `dept`
equal to `"ABC"` and the field `date` greater than or equal to
ISODate("2018-01-01") (using the canonical format for dates
{ "$date": "YYYY-MM-DDTHH:mm:ss.mmm<offset>"} )

```sh
mongoexport --db=sales --collection=contacts --query='{"dept": "ABC", date: { $gte: { "$date": "2018-01-01T00:00:00.000Z" } }}'
```

You must enclose the query document in single quotes (`'{ ... }'`) to ensure 
that it does not interact with your shell environment.

## Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster which has been 
configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongoexport` similar to the following:

```none
mongoexport 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongoexport 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
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
mongoexport 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, these three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongoexport` checks for the following environment variables when you
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
mongoexport 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```

## Learn More

- mongoexport
- mongoexport-compatibility-and-installation
- mongoexport Behavior
