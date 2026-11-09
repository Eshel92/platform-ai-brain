<!-- Converted from tutorial/deploy-sharded-cluster-with-keyfile-access-control.txt (reStructuredText). Includes are inlined. -->

# Deploy Self-Managed Sharded Cluster with Keyfile Authentication

## Overview

Enforcing access control on a sharded cluster requires configuring:

- Security between components of the cluster using
  Internal Authentication.

- Security between connecting clients and the cluster using
  User Access Controls.

For this tutorial, each member of the sharded cluster *must* use the same
internal authentication mechanism and settings. This means enforcing internal
authentication on each `mongos` and `mongod` in the cluster.

The following tutorial uses a keyfile to
enable internal authentication.

Enforcing internal authentication also enforces user access control. To
connect to the replica set, clients like `mongosh` need to
use a user account. See
security-shardClust-deploy-access-control.

### CloudManager and OpsManager

If you are using Cloud Manager or Ops Manager to manage your deployment,
see the respective `Cloud Manager manual`
or the `Ops Manager manual` to enforce authentication.

## Considerations

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

### IP Binding

MongoDB binaries, `mongod` and
`mongos`, bind to `localhost` by default.

### Keyfile Security

Keyfiles are bare-minimum forms of security and are best suited for testing or
development environments. For production environments we recommend using
X.509 certificates.

### Access Control

This tutorial covers creating the minimum number of administrative
users on the `admin` database *only*. For the user authentication,
the tutorial uses the default authentication-scram
authentication mechanism. Challenge-response security mechanisms are
best suited for testing or development environments. For production
environments, we recommend using X.509
certificates or security-ldap
(available for MongoDB Enterprise only) or security-kerberos
(available for MongoDB Enterprise only).

For details on creating users for specific authentication mechanism,
refer to the specific authentication mechanism pages.

See security-checklist-role-based-access-control for best
practices for user creation and management.

### Users

In general, to create users for a sharded clusters, connect to the
`mongos` and add the sharded cluster users.

However, some maintenance operations require direct connections to
specific shards in a sharded cluster. To perform these operations, you
must connect directly to the shard and authenticate as a shard-local
administrative user.

Shard-local users exist only in the specific shard and should only be
used for shard-specific maintenance and configuration. You cannot
connect to the `mongos` with shard-local users.

This tutorial requires creating sharded cluster users, but includes
optional steps for adding shard-local users.

See the /core/security-users security documentation for more
information.

### Operating System

This tutorial uses the `mongod` and `mongos`
programs. Windows users should use the `mongod.exe` and
`mongos.exe` programs instead.

## Deploy Sharded Cluster with Keyfile Access Control

The following procedures involve creating a new sharded cluster that consists
of a `mongos`, the config servers, and two shards.

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

### Create the Keyfile

With keyfile authentication, each
`mongod` or `mongos` instances in the sharded cluster uses the contents of the keyfile as the
shared password for authenticating other members in the deployment. Only
`mongod` or `mongos` instances with the correct keyfile can join the sharded cluster.

**Note:**

Keyfiles for internal membership authentication use YAML format to allow for multiple keys in a 
keyfile. The YAML format accepts either:

- A single key string (same as in earlier versions)

- A sequence of key strings

The YAML format is compatible with the existing single-key
keyfiles that use the text file format.

A key's length must be between 6 and 1024 characters and may only
contain characters in the base64 set. All members of the
sharded cluster must share at least one common key.

**Note:**

On UNIX systems, the keyfile must not have group or world
permissions. On Windows systems, keyfile permissions are not checked.

You can generate a keyfile using any method you choose. For example,
the following operation uses `openssl` to generate a complex
pseudo-random 1024 character string to use as a shared password. It then
uses `chmod` to change file permissions to provide read
permissions for the file owner only:

```bash
openssl rand -base64 756 > <path-to-keyfile>
chmod 400 <path-to-keyfile>
```

See internal-auth-keyfile for additional details  and requirements
for using keyfiles.

### Distribute the Keyfile

Copy the keyfile to each server hosting the sharded cluster members.
Ensure that the user running the `mongod` or `mongos` instances is the owner of the
file and can access the keyfile.

Avoid storing the keyfile on storage mediums that can be easily
disconnected from the hardware hosting the `mongod` or `mongos` instances, such as a
USB drive or a network attached storage device.

### Create the Config Server Replica Set

The following steps deploys a config server replica set.

For a production deployment, deploys a config server replica set with at
least three members. For testing purposes, you can create a
single-member replica set.

**Step 1: **

Start *each* `mongod` in the config server replica set.
Include the `keyFile` setting. The `keyFile` setting
enforces both /core/security-internal-authentication and
/core/authorization.

You can specify the `mongod` settings either via a
configuration file or the command line.

**Configuration File**

If using a configuration file, set `security.keyFile` to the
keyfile's path, `sharding.clusterRole` to `configsvr`, 
and `replication.replSetName` to the desired name of the 
config server replica set.

```yaml
security:
  keyFile: <path-to-keyfile>
sharding:
  clusterRole: configsvr
replication:
  replSetName: <setname>
```

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

Start the `mongod` specifying the `--config` option and the 
path to the configuration file.

```shell
mongod --config <path-to-config-file>
```

**Command Line**

If using the command line parameters, start the `mongod` with 
the `--keyFile`, `--configsvr`, and `--replSet` parameters.

```sh
mongod --keyFile <path-to-keyfile> --configsvr --replSet <setname> --dbpath <path>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Step 2: Connect to a member of the replica set over the localhost interface.**

Connect `mongosh` to one of the 
`mongod` instances over the localhost
interface. You must run `mongosh`
on the same physical machine as the `mongod` instance.

The localhost interface is only available
since no users have been created for the deployment. The
localhost interface closes after the
creation of the first user.

**Step 3: **

The `rs.initiate()` method initiates the replica set and can
take an optional replica set configuration document. In the replica set
configuration document, include:

- The `_id`. The `_id` *must* match the `--replSet`
  parameter passed to the `mongod`.

- The `members` field. The `members` field is an
  array and requires a document per each member of the replica set.

- The `configsvr` field. The `configsvr` field must
  be set to `true` for the config server replica set.

See /reference/replica-configuration for more information on 
replica set configuration documents.

Initiate the replica set using the `rs.initiate()` method
and a configuration document:

```javascript
rs.initiate(
  {
    _id: "myReplSet",
    configsvr: true,
    members: [
      { _id : 0, host : "cfg1.example.net:27019" },
      { _id : 1, host : "cfg2.example.net:27019" },
      { _id : 2, host : "cfg3.example.net:27019" }
    ]
  }
)
```

**Note:**

To use the config server replica set (CSRS) in this procedure, you must first wait
until it completes its initialization.  If the CSRS has not initialized, it causes
`NotYetInitialized` errors.

Once the config server replica set (CSRS) is initiated and up, proceed
to creating the shard replica sets.

### Create the Shard Replica Sets

For a production deployment, use a replica set with at least three
members. For testing purposes, you can create a single-member replica
set.

These steps include optional procedures for adding shard-local users.
Executing them now ensures that there are users available for each
shard to perform shard-level maintenance.

**Step 1: Start each member of the replica set with access control enabled.**

Running a `mongod` with the `keyFile` parameter enforces both 
/core/security-internal-authentication and 
/core/authorization.

Start *each* `mongod` in the replica set using either 
a configuration file or the command line.

**Configuration File**

If using a configuration file, set the `security.keyFile` option
to the keyfile's path, the `replication.replSetName` to the 
desired name of the replica set, and the `sharding.clusterRole` 
option to `shardsvr`.

```yaml
security:
  keyFile: <path-to-keyfile>
sharding:
  clusterRole: shardsvr
replication:
  replSetName: <replSetName>
storage:
   dbPath: <path>
```

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

Start the `mongod` specifying the `--config` option
and the path to the configuration file.

```sh
mongod --config <path-to-config-file>
```

**Command Line**

If using the command line option, when starting the component, specify 
the `--keyFile`, `replSet`, and `--shardsvr` parameters, as in the
following example:

```sh
mongod --keyFile <path-to-keyfile> --shardsvr --replSet <replSetName>  --dbpath <path>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Step 2: Connect to a member of the replica set over the localhost interface.**

Connect `mongosh` to one of the 
`mongod` instances over the localhost
interface. You must run `mongosh`
on the same physical machine as the `mongod` instance.

The localhost interface is only available
since no users have been created for the deployment. The
localhost interface closes after the
creation of the first user.

**Step 3: Initiate the replica set.**

From `mongosh`, run the `rs.initiate()` method.

`rs.initiate()` can take an optional replica set
configuration document. In the
replica set configuration document, include:

- The `_id` field set to the replica set name specified in
  either the `replication.replSetName` or the `--replSet`
  option.

- The `members` array with a document per each member of the
  replica set.

The following example initates a three member replica set.

```javascript
rs.initiate(
  {
    _id : "myReplSet",
    members: [
      { _id : 0, host : "s1-mongo1.example.net:27018" },
      { _id : 1, host : "s1-mongo2.example.net:27018" },
      { _id : 2, host : "s1-mongo3.example.net:27018" }
    ]
  }
)
```

`rs.initiate()` triggers an election and
elects one of the members to be the primary.

Connect to the primary before continuing. Use `rs.status()` to
locate the primary member.

**Step 4: Create the shard-local user administrator (optional).**

**Important:**

After you create the first user, the localhost exception is no longer available.

The first user must have privileges to create other users, such
as a user with the `userAdminAnyDatabase`. This ensures
that you can create additional users after the localhost-exception
closes.

If at least one user does *not* have privileges to create users,
once the localhost exception closes you may be unable to create
or modify users with new privileges, and therefore unable to
access necessary operations.

Add a user using the `db.createUser()` method. The user should
have at minimum the `userAdminAnyDatabase` role on the
`admin` database.

You must be connected to the primary to create users.

The following example creates the user `fred` with the
`userAdminAnyDatabase` role on the `admin` database.

**Important:**

Passwords should be random, long, and complex to ensure system security
and to prevent or delay malicious access.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
admin = db.getSiblingDB("admin")
admin.createUser(
  {
    user: "fred",
    pwd: passwordPrompt(), // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```

Enter the password when prompted.
See database-user-roles for a full list of built-in roles 
related to database administration operations.

**Step 5: Authenticate as the shard-local user administrator (optional).**

Authenticate to the `admin` database.

In `mongosh`, use `db.auth()` to
authenticate. For example, the following authenticate as the user
administrator `fred`:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.getSiblingDB("admin").auth("fred", passwordPrompt()) // or cleartext password
```

Alternatively, connect a new `mongosh` instance to
the primary replica set member using the `-u <username>`,
`-p <password>`, and the `--authenticationDatabase`
parameters.

```sh
mongosh -u "fred" -p  --authenticationDatabase "admin"
```

If you do not specify the password to the `-p`
command-line option, `mongosh` prompts for the
password.

**Step 6: Create the shard-local cluster administrator (optional).**

The shard-local cluster administrator user has the
`clusterAdmin` role, which provides privileges that allow
access to replication operations.

For a full list of roles related to replica set operations see
cluster-admin-roles.

Create a cluster administrator user and assign the
`clusterAdmin` role in the `admin` database:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```sh
db.getSiblingDB("admin").createUser(
  {
    "user" : "ravi",
    "pwd" : passwordPrompt(),     // or cleartext password
    roles: [ { "role" : "clusterAdmin", "db" : "admin" } ]
  }
)
```

Enter the password when prompted.

See cluster-admin-roles for a full list of built-in roles related to
replica set and sharded cluster operations.

### Connect a `mongos` to the Sharded Cluster

**Step 1: Connect a `mongos` to the cluster**

Start a `mongos` specifying
the keyfile using either a configuration file or a command line parameter.

**Configuration File**

If using a configuration file, set the
`security.keyFile` to the keyfile's path and the
`sharding.configDB` to the replica set name and at least
one member of the replica set in `<replSetName>/<host:port>`
format.

```yaml
security:
  keyFile: <path-to-keyfile>
sharding:
  configDB: <configReplSetName>/cfg1.example.net:27019,cfg2.example.net:27019,...
```

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

Start the `mongos` specifying the `--config` option and the
path to the configuration file.

```shell
mongos --config <path-to-config>
```

**Command Line**

If using command line parameters start the `mongos` and specify
the `--keyFile` and `--configdb` parameters.

```sh
mongos --keyFile <path-to-keyfile> --configdb <configReplSetName>/cfg1.example.net:27019,cfg2.example.net:27019,...
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Step 2: Connect to a `mongos` over the localhost interface.**

Connect `mongosh` to one of the 
`mongos` instances over the localhost
interface. You must run `mongosh`
on the same physical machine as the `mongos` instance.

The localhost interface is only available
since no users have been created for the deployment. The
localhost interface closes after the
creation of the first user.

**Step 3: Create the user administrator.**

**Important:**

After you create the first user, the localhost exception is no longer available.

The first user must have privileges to create other users, such
as a user with the `userAdminAnyDatabase`. This ensures
that you can create additional users after the localhost-exception
closes.

If at least one user does *not* have privileges to create users,
once the localhost exception closes you cannot create
or modify users, and therefore may be unable to
perform necessary operations.

Add a user using the `db.createUser()` method. The user should
have at minimum the `userAdminAnyDatabase` role on the
`admin` database.

**Important:**

Passwords should be random, long, and complex to ensure system security
and to prevent or delay malicious access.

The following example creates the user `fred` on the
`admin` database:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
admin = db.getSiblingDB("admin")
admin.createUser(
  {
    user: "fred",
    pwd:  passwordPrompt(),     // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```

See database-user-roles for a full list of built-in roles and
related to database administration operations.

**Step 4: Authenticate as the user administrator.**

Use `db.auth()` to authenticate as the user administrator
to create additional users:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.getSiblingDB("admin").auth("fred", passwordPrompt()) // or cleartext password
```

Enter the password when prompted.

Alternatively, connect a new `mongosh` session to the
target replica set member using the `-u <username>`,
`-p <password>`, and the `--authenticationDatabase "admin"`
parameters. You must use the localhost-exception to connect
to the `mongos`.

```sh
mongosh -u "fred" -p  --authenticationDatabase "admin"
```

If you do not specify the password to the `-p`
command-line option, `mongosh` prompts for the
password.

**Step 5: Create Administrative User for Cluster Management**

The cluster administrator user has the `clusterAdmin` role,
which grants access to replication and sharding operations.

Create a `clusterAdmin` user in the `admin` database.

The following example creates the user `ravi` on the `admin`
database.

**Important:**

Passwords should be random, long, and complex to ensure system
security and to prevent or delay malicious access.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```sh
db.getSiblingDB("admin").createUser(
  {
    "user" : "ravi",
    "pwd" : passwordPrompt(),     // or cleartext password
    roles: [ { "role" : "clusterAdmin", "db" : "admin" } ]
  }
)
```

See cluster-admin-roles for a full list of built-in roles related to
replica set and sharded cluster operations.

**Step 7: Create additional users (Optional).**

Create users to allow clients to connect and access the
sharded cluster. See database-user-roles for available built-in
roles, such as `read` and `readWrite`.
You may also want additional administrative users.
For more information on users, see /core/security-users.

To create additional users, you must authenticate as a user with
`userAdminAnyDatabase` or `userAdmin` roles.

### Add Shards to the Cluster

To proceed, you must be connected to the `mongos` and
authenticated as the cluster administrator user for the sharded cluster.

**Note:**

This is the cluster administrator for the sharded cluster and *not*
the shard-local cluster administrator.

To add each shard to the cluster, use the `sh.addShard()`
method. If the shard is a replica set, specify the name of the replica
set and specify a member of the set. In production deployments, *all*
shards should be replica sets.

The following operation adds a single shard replica set to the cluster:

```javascript
sh.addShard( "<replSetName>/s1-mongo1.example.net:27017")
```

The following operation is an example of adding a standalone `mongod`
shard to the cluster:

```javascript
sh.addShard( "s1-mongo1.example.net:27017")
```

Repeat these steps until the cluster includes all shards. At this
point, the sharded cluster enforces access control for the cluster as
well as for internal communications between each sharded cluster
component.

### Shard a Collection

To proceed, you must be connected to the `mongos` and
authenticated as the cluster administrator user for the sharded cluster.

**Note:**

This is the cluster administrator for the sharded cluster and *not*
the shard-local cluster administrator.

To shard a collection, use the `sh.shardCollection()` method.
You must specify the full namespace of the collection and a document containing
the shard key.

Your selection of shard key affects the efficiency of sharding, as well as
your ability to take advantage of certain sharding features such as
zones. See the selection considerations listed
in the sharding-shard-key-selection.

If the collection already contains data, you must create an index on the
shard key using the `db.collection.createIndex()` method before
using `shardCollection()`.

If the collection is empty, MongoDB creates the index as part of
`sh.shardCollection()`.

The following is an example of the `sh.shardCollection()` method:

```javascript
sh.shardCollection("<database>.<collection>", { <key> : <direction> } )
```

## Next Steps

Create users to allow clients to connect to and interact with
the sharded cluster.

See database-user-roles for basic built-in roles to use in creating
read-only and read-write users.

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see
/tutorial/configure-x509-member-authentication.

To upgrade from keyfile internal authentication to X.509 internal
authentication, see
/tutorial/upgrade-keyfile-to-x509.

**See also:**

- /core/sharded-cluster-components
- /core/sharded-cluster-requirements
