<!-- Converted from mongotop/mongotop-examples.txt (reStructuredText). Includes are inlined. -->

# mongotop Examples

This page shows examples for `mongotop`.

Run `mongotop` from the system command line, not the 
`mongo` shell.

## Examples

By default `mongotop` connects to the MongoDB instance
running on the localhost port `27017`. However, `mongotop` can optionally
connect to remote `mongod`
instances. See the mongotop options for more
information.

To force `mongotop` to return less frequently specify a number, in
seconds at the end of the command. In this example, `mongotop` will
return every 15 seconds.

```sh
mongotop 15
```

This command produces the following output:

```sh
2019-04-29T15:35:27.785-0400	connected to: 127.0.0.1

                    ns    total    read    write    2019-04-29T15:35:57-04:00
    admin.system.roles      0ms     0ms      0ms                             
    admin.system.users      0ms     0ms      0ms                             
  admin.system.version      0ms     0ms      0ms                             
config.system.sessions      0ms     0ms      0ms                             
     local.startup_log      0ms     0ms      0ms                             
  local.system.replset      0ms     0ms      0ms
```

To return a `mongotop` report every 5 minutes, use the
following command:

```sh
mongotop 300
```

### Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster which
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongotop` similar to the following:

```none
mongotop 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongotop 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
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
mongotop 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, these three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongotop` checks for the following environment variables when you
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
mongotop 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```

## Learn More

- mongotop
- mongotop-compatibility-and-installation
- mongotop Behavior
