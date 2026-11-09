<!-- Converted from reference/connection-string-examples.txt (reStructuredText). Includes are inlined. -->

# Connection String Examples

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples.

----------

You can use connection strings to define connections between
MongoDB instances and the following destinations:

- Your applications when you connect using `drivers`.
- Tools such as `MongoDB Compass` and 
  `the MongoDB Shell (mongosh)`.

This page provides example URI strings for common connection targets.

## MongoDB Atlas Deployment Connection String Examples

The following example connection strings connect to an MongoDB Atlas
deployment.

### MongoDB Atlas Cluster that Authenticates with a Username and Password

**shell:**

```bash
mongosh "mongodb+srv://cluster0.example.mongodb.net myFirstDatabase" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

### MongoDB Atlas Cluster that Authenticates with AWS IAM credentials

The following connects to a [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server) cluster which
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html):

**shell:**

```bash
mongosh 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'
```

**python:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**java-sync:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**java-async:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**nodejs:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**php:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**perl:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**ruby:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**scala:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**compass:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**csharp:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**go:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**motor:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**rust:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

**shell:**

```bash
mongosh 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>'
```

**python:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**java-sync:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**java-async:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**nodejs:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**php:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**perl:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**ruby:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**scala:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**compass:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**csharp:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**go:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**motor:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**rust:**

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

**Note:**

If the AWS access key ID, the secret access key, or the session token
include the following characters:

```none
$ : / ? # [ ] @
```

those characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1). 

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongosh` checks for the following environment
variables when you use the `MONGODB-AWS`
`authentication mechanism`:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`

If set, these credentials do not need to be specified in the connection
string.

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

**shell:**

```bash
mongosh 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'
```

**python:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**java-sync:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**java-async:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**nodejs:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**php:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**perl:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**ruby:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**scala:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**compass:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**csharp:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**go:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**motor:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

**rust:**

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

## Self-Hosted Deployment Connection String Examples

The following example connection strings connect to a self-hosted
deployment.

### Self-Hosted Cluster that Authenticates with a Username and Password

**srv:**

**repl:**

The following replica set connection string includes these
elements:

- The `replicaSet` option
- The hostname(s) of the `mongod` instance(s) as
  listed in the replica set configuration
- It authenticates as user `myDatabaseUser` with the password
  `D1fficultP%40ssw0rd` to enforce access control

**shell:**

```bash
mongosh "mongodb+srv://mongodb0.example.com/?authSource=admin&replicaSet=myRepl" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**sharded:**

The following sharded cluster connection string includes the
these elements:

- The `mongos` hosts in the connection string
- It authenticates as user `myDatabaseUser` with the password
  `D1fficultP%40ssw0rd` to enforce access control

**shell:**

```bash
mongosh "mongodb+srv://mongos0.example.com/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**standalone:**

The following standalone connection string authenticates as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd` to enforce access control:

**shell:**

```bash
mongosh "mongodb+srv://mongodb0.example.com/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**standard:**

**repl:**

The following replica set connection string includes these
elements:

- The `replicaSet` option
- The hostname(s) of the `mongod` instance(s) as
  listed in the replica set configuration
- A username and password to enforce access control:

**shell:**

```bash
mongosh "mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**sharded:**

The following sharded cluster connection string includes the
these elements:

- The `mongos` hosts in the connection string
- A username and password to enforce access control

**shell:**

```bash
mongosh "mongodb://mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**standalone:**

The following standalone connection string enforces access
control:

**shell:**

```bash
mongosh "mongodb://@mongodb0.example.com:27017/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

### Self-Hosted Database Server Running Locally

The following connects to a database server running locally on the
default port:

**shell:**

```bash
mongosh "mongodb://localhost" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://localhost
```

**java-sync:**

```bash
mongodb://localhost
```

**java-async:**

```bash
mongodb://localhost
```

**nodejs:**

```bash
mongodb://localhost
```

**php:**

```bash
mongodb://localhost
```

**perl:**

```bash
mongodb://localhost
```

**ruby:**

```bash
mongodb://localhost
```

**scala:**

```bash
mongodb://localhost
```

**compass:**

```bash
mongodb://localhost
```

**csharp:**

```bash
mongodb://localhost
```

**go:**

```bash
mongodb://localhost
```

**motor:**

```bash
mongodb://localhost
```

**rust:**

```bash
mongodb://localhost
```

### Self-Hosted `admin` Database Running Locally

The following connects and logs in to the `admin` database as user
`myDatabaseUser` with the password `D1fficultP%40ssw0rd`:

**shell:**

```bash
mongosh "mongodb://localhost" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost
```

### Self-Hosted `records` Database Running Locally

The following connects and logs in to the `records` database as user
`myDatabaseUser` with the password `D1fficultP%40ssw0rd`:

**shell:**

```bash
mongosh "mongodb://localhost/records" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost/records
```

### Self-Hosted UNIX Domain Socket

Use a URL encoded connection string when connecting to a UNIX domain
socket.

The following connects to a UNIX domain socket with file path
`/tmp/mongodb-27017.sock` as user `myDatabaseUser` with the
password `D1fficultP%40ssw0rd`:

**shell:**

```bash
mongosh "mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@%2Ftmp%2Fmongodb-27017.sock
```

**Note:** Not all drivers support UNIX domain sockets. For information

on your driver, see the `Drivers`
documentation.

### Self-Hosted Replica Set with Members on Different Machines

The following connects to a replica set with two members, one on
`db1.example.net` and the other on `db2.example.net`, 
as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd`:

**Note:**

For a replica set, specify the hostname(s) of the `mongod`
instance(s) as listed in the replica set configuration.

**shell:**

```bash
mongosh "mongodb://db1.example.net,db2.example.com/?replicaSet=test" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net,db2.example.com/?replicaSet=test
```

### Self-Hosted Replica Set with Members on `localhost`

The following connects to a replica set with three members running on `localhost` on
ports `27017`, `27018`, and `27019`
as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd`:

**Note:**

For a replica set, specify the hostname(s) of the `mongod`
instance(s) as listed in the replica set configuration.

**shell:**

```bash
mongosh "mongodb://localhost,localhost:27018,localhost:27019/?replicaSet=test" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@localhost,localhost:27018,localhost:27019/?replicaSet=test
```

### Self-Hosted Replica Set with Read Distribution

The following connects to a replica set with three members and
distributes reads to the secondaries
as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd`:

**Note:**

For a replica set, specify the hostname(s) of the `mongod`
instance(s) as listed in the replica set configuration.

**shell:**

```bash
mongosh "mongodb://example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&readPreference=secondary
```

### Self-Hosted Replica Set with a High Level of Write Concern

The following connects to a replica set with write concern configured
to wait for replication to succeed across a majority of the
data-bearing voting members, with a two-second timeout. It authenticates
as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd`.

**Note:**

For a replica set, specify the hostname(s) of the `mongod`
instance(s) as listed in the replica set configuration.

**shell:**

```bash
mongosh "mongodb://example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@example1.com,example2.com,example3.com/?replicaSet=test&w=majority&wtimeoutMS=2000
```

### Self-Hosted Sharded Cluster

The following connects to a sharded cluster with three `mongos` instances as user `myDatabaseUser` with the password
`D1fficultP%40ssw0rd`:

**shell:**

```bash
mongosh "mongodb://router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@router1.example.com:27017,router2.example2.com:27017,router3.example3.com:27017/
```
