<!-- Converted from mongoimport/mongoimport-examples.txt (reStructuredText). Includes are inlined. -->

# mongoimport Examples

This page shows examples for `mongoimport`.

Run `mongoimport` from the system command line, not the 
`mongo` shell.

## Simple Import

`mongoimport` restores a database from a backup taken with
`mongoexport`. Most of the arguments to `mongoexport` also
exist for `mongoimport`.

In the following example, `mongoimport` imports
the JSON data from the `contacts.json` file into the collection
`contacts` in the `users` database.

```sh
mongoimport --db=users --collection=contacts --file=contacts.json
```

## Replace Matching Documents during Import

With `--mode` `upsert`, `mongoimport` replaces
existing documents in the database that match a document in the
import file with the document from the import file.
Documents that do not match an existing document in the database are
inserted as usual. By default `mongoimport` matches documents
based on the `_id` field. Use `--upsertFields` to specify
the fields to match against.

Consider the following document in the `people` collection in the
`example` database:

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "name" : "Crystal Duncan",
   "region" : "United States",
   "email" : "crystal@example.com"
}
```

The following document exists in a `people-20160927.json` JSON file.
The `_id` field of the JSON object matches the `_id` field of the
document in the `people` collection.

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "username" : "crystal",
   "likes" : [ "running", "pandas", "software development" ]
}
```

To import the `people-20160927.json` file and replace documents in
the database that match the documents in the import file, specify `--mode`
`upsert`, as in the following:

```sh
mongoimport -c=people -d=example --mode=upsert --file=people-20160927.json
```

The document in the `people` collection would then contain only
the fields from the imported document, as in the following:

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "username" : "crystal",
   "likes" : [ "running", "pandas", "software development" ]
}
```

## Merge Matching Documents during Import

With `--mode` `merge`, `mongoimport` enables you to
merge fields from a new record with an existing document in the
database. Documents that do not match an existing document in the
database are inserted as usual. By default `mongoimport`
matches documents based on the `_id` field. Use
`--upsertFields` to specify the fields to match against.

The `people` collection in the `example` database contains the
following document:

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "name" : "Crystal Duncan",
   "region" : "United States",
   "email" : "crystal@example.com"
}
```

The following document exists in a `people-20160927.json` JSON file.
The `_id` field of the JSON object matches the `_id` field of the
document in the `people` collection.

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "username" : "crystal",
   "email": "crystal.duncan@example.com",
   "likes" : [ "running", "pandas", "software development" ]
}
```

To import the `people-20160927.json` file and merge documents from
the import file with matching documents in the database, specify
`--mode` `merge`, as in the following:

```sh
mongoimport -c=people -d=example --mode=merge --file=people-20160927.json
```

The import operation combines the fields from the JSON file with the
original document in the database,
matching the documents based on the `_id` field.
During the import process, `mongoimport` adds the new `username` and
`likes` fields to the document and updates the `email` field with
the value from the imported document, as in the following:

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "name" : "Crystal Duncan",
   "region" : "United States",
   "email" : "crystal.duncan@example.com",
   "username" : "crystal",
   "likes" : [
      "running",
      "pandas",
      "software development"
   ]
}
```

## Delete Matching Documents

**New in version:** 100.0.0

With `--mode` `delete`,
`mongoimport` deletes existing documents in the database
that match a document in the import file. Documents that do not match an
existing document in the database are ignored. By default
`mongoimport` matches documents based on the `_id` field.
Use `--upsertFields` to specify
the fields to match against.

**Note:**

With `--mode` `delete`,
`mongoimport` only deletes one existing document per
match. Ensure that documents from the import file match a single
existing document from the database.

The `people` collection in the `example` database contains the
following document:

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "name" : "Crystal Duncan",
   "region" : "United States",
   "email" : "crystal@example.com",
   "employee_id" : "5463789356"
}
```

The following document exists in a `people-20160927.json` JSON file.
The `_id` field of the JSON object matches the `_id` field of the
document in the `people` collection.

```javascript
{
   "_id" : ObjectId("580100f4da893943d393e909"),
   "username" : "crystal",
   "email": "crystal.duncan@example.com",
   "likes" : [ "running", "pandas", "software development" ],
   "employee_id" : "5463789356"
}
```

To delete the documents in the database that match a document in the
`people-20160927.json` file, specify
`--mode` `delete`, as in the following:

```sh
mongoimport -c=people -d=example --mode=delete --file=people-20160927.json
```

Because the `_id` fields match between the database and the input
file, `mongoimport` deletes the matching document from the
`people` collection. The same results could also have been achieved
by using `--upsertFields` to
specify the `employee_id` field, which also matches between the
database and the input file.

## Import `JSON` to Remote Host Running with Authentication

In the following example, `mongoimport` imports data from the
file `/opt/backups/mdb1-examplenet.json` into the `contacts` collection
within the database `marketing` on a remote MongoDB
database with authentication enabled.

`mongoimport` connects to the `mongod` instance running on
the host `mongodb1.example.net` over port `37017`. It authenticates with the
username `user`; the example omits the `--password`
option to have `mongoimport` prompt for the password:

```sh
mongoimport --host=mongodb1.example.net --port=37017 --username=user --collection=contacts --db=marketing --file=/opt/backups/mdb1-examplenet.json
```

## `CSV` Import

### General CSV Import

In the following example, `mongoimport` imports the CSV
formatted data in the `/opt/backups/contacts.csv` file into the
collection `contacts` in the `users` database on the MongoDB
instance running on the localhost port numbered
`27017`.

Specifying `--headerline` instructs
`mongoimport` to determine the name of the fields using the first
line in the CSV file.

```sh
mongoimport --db=users --collection=contacts --type=csv --headerline --file=/opt/backups/contacts.csv
```

`mongoimport` uses the input file name, without the
extension, as the collection name if `-c` or `--collection` is
unspecified. The following example is therefore equivalent:

```none
mongoimport --db=users --type=csv --headerline --file=/opt/backups/contacts.csv
```

### Import CSV with Specified Field Types

When specifying the field name, you can also specify the data type. To
specify field names and type, include
`--columnsHaveTypes` with
either: `--fields`, `--fieldFile`, or `--headerline`.

Specify field names and data types in the form
`<colName>.<type>(<arg>)`. 

For example, `/example/file.csv` contains the following data:

```none
Katherine Gray, 1996-02-03, false, 1235, TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwgc2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBhbGlxdWEuIFV0IGVuaW0gYWQgbWluaW0gdmVuaWFtLCBxdWlzIG5vc3RydWQgZXhlcmNpdGF0aW9uIHVsbGFtY28gbGFib3JpcyBuaXNpIHV0IGFsaXF1aXAgZXggZWEgY29tbW9kbyBjb25zZXF1YXQuIER1aXMgYXV0ZSBpcnVyZSBkb2xvciBpbiByZXByZWhlbmRlcml0IGluIHZvbHVwdGF0ZSB2ZWxpdCBlc3NlIGNpbGx1bSBkb2xvcmUgZXUgZnVnaWF0IG51bGxhIHBhcmlhdHVyLiBFeGNlcHRldXIgc2ludCBvY2NhZWNhdCBjdXBpZGF0YXQgbm9uIHByb2lkZW50LCBzdW50IGluIGN1bHBhIHF1aSBvZmZpY2lhIGRlc2VydW50IG1vbGxpdCBhbmltIGlkIGVzdCBsYWJvcnVtLg==
Albert Gilbert, 1992-04-24, true, 13, Q3VwY2FrZSBpcHN1bSBkb2xvciBzaXQgYW1ldCB0b290c2llIHJvbGwgYm9uYm9uIHRvZmZlZS4gQ2FuZHkgY2FuZXMgcGllIGNyb2lzc2FudCBjaG9jb2xhdGUgYmFyIGxvbGxpcG9wIGJlYXIgY2xhdyBtYWNhcm9vbi4gU3dlZXQgcm9sbCBjdXBjYWtlIGNoZWVzZWNha2Ugc291ZmZsw6kgYnJvd25pZSBpY2UgY3JlYW0uIEp1anViZXMgY2FrZSBjdXBjYWtlIG1hY2Fyb29uIGRhbmlzaCBqZWxseS1vIHNvdWZmbMOpLiBDYWtlIGFwcGxlIHBpZSBnaW5nZXJicmVhZCBjaG9jb2xhdGUgc3VnYXIgcGx1bS4gU3dlZXQgY2hvY29sYXRlIGNha2UgY2hvY29sYXRlIGNha2UganVqdWJlcyB0aXJhbWlzdSBvYXQgY2FrZS4gU3dlZXQgc291ZmZsw6kgY2hvY29sYXRlLiBMaXF1b3JpY2UgY290dG9uIGNhbmR5IGNob2NvbGF0ZSBtYXJzaG1hbGxvdy4gSmVsbHkgY29va2llIGNha2UgamVsbHkgYm==
```

The following operation uses `mongoimport` with the
`--fields` and
`--columnsHaveTypes` option
to specify both the field names and the BSON types of the imported CSV
data.

```sh
mongoimport --db=users --collection=contacts --type=csv \
   --columnsHaveTypes \
   --fields="name.string(),birthdate.date(2006-01-02),contacted.boolean(),followerCount.int32(),thumbnail.binary(base64)" \
   --file=/example/file.csv
```

### Ignore Blank Fields

Use the `--ignoreBlanks` option
to ignore blank fields. For CSV and TSV imports, this
option provides the desired functionality in most cases because it avoids
inserting fields with null values into your collection.

The following example imports the data from `data.csv`, skipping
any blank fields:

```sh
mongoimport --db=users --collection=contacts --type=csv --file=/example/data.csv --ignoreBlanks
```

### Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster which
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongoimport` similar to the following:

```none
mongoimport 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongoimport 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
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
mongoimport 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, these three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongoimport` checks for the following environment variables when you
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

Other shells use different syntax to set environment variables. Consult
the documentation for your platform for more information.

You can verify that these environment variables have been set with the
following command:

```none
env | grep AWS
```

Once set, the following example connects to a MongoDB Atlas cluster
using these environment variables:

```none
mongoimport 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```

## Learn More

- mongoimport
- mongoimport-compatibility-and-installation
- mongoimport Behavior
