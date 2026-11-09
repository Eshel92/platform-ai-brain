<!-- Converted from tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Update Self-Managed Sharded Cluster to Keyfile Authentication

## Overview

Enforcing access control on a sharded cluster requires configuring:

- Security between components of the cluster using
  Internal Authentication.

- Security between connecting clients and the cluster using
  /core/authorization.

For this tutorial, each member of the sharded cluster *must* use the same
internal authentication mechanism and settings. This means enforcing internal
authentication on each `mongos` and `mongod` in the cluster.

The following tutorial uses a keyfile to
enable internal authentication.

Enforcing internal authentication also enforces user access control. To
connect to the replica set, clients like `mongosh` need to
use a user account. See
security-shardClust-enforce-access-control.

### CloudManager and OpsManager

If Cloud Manager or Ops Manager is managing your deployment, internal
authentication is automatically enforced.

To configure Access Control on a
managed deployment, see: `Configure Access Control for MongoDB Deployments`
in the `Cloud Manager manual`
or in the `Ops Manager manual`.

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

### Operating System

This tutorial primarily refers to the `mongod` process.
Windows users should use the `mongod.exe` program instead.

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

See the /core/security-users security documentation for more
information.

### Downtime

Upgrading a sharded cluster to enforce access control requires downtime.

## Procedures

### Enforce Keyfile Internal Authentication on Existing Sharded Cluster Deployment

**Step 1: Create a keyfile.**

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

```sh
openssl rand -base64 756 > <path-to-keyfile>
chmod 400 <path-to-keyfile>
```

See internal-auth-keyfile for additional details  and requirements
for using keyfiles.

**Step 2: Copy the keyfile to each component in the sharded cluster.**

Every server hosting a `mongod` or `mongos` component
of the sharded cluster must contain a copy of the keyfile.

Copy the keyfile to each server hosting the sharded cluster members.
Ensure that the user running the `mongod` or `mongos` instances is the owner of the
file and can access the keyfile.

Avoid storing the keyfile on storage mediums that can be easily
disconnected from the hardware hosting the `mongod` or `mongos` instances, such as a
USB drive or a network attached storage device.

**Step 3: Disable the Balancer.**

Connect `mongosh` to a `mongos`.

```sh
sh.stopBalancer()
```

The balancer may not stop immediately if a migration is in progress.
The `sh.stopBalancer()` method blocks the shell until the
balancer stops.

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0.3, `sh.stopBalancer()`
also disables auto-splitting for the sharded cluster.

Use `sh.getBalancerState()` to verify that the balancer has
stopped.

```sh
sh.getBalancerState()
```

**Important:** Do not proceed until the balancer has stopped running.

See /tutorial/manage-sharded-cluster-balancer for tutorials on
configuring sharded cluster balancer behavior.

**Step 4: Shut down all `mongos` instances for the sharded cluster.**

Connect `mongosh` to each `mongos` and shut
them down.

Use the `db.shutdownServer()` method on the `admin` database
to safely shut down the `mongos`:

```sh
db.getSiblingDB("admin").shutdownServer()
```

Repeat until all `mongos` instances in the cluster
are offline.

Once this step is complete, all `mongos` instances in the cluster
should be offline.

**Step 5: Shut down config server `mongod` instances.**

Connect `mongosh` to each `mongod` in the
config server deployment and shut them down.

For replica set config server deployments, shut down the primary
member last.

Use the `db.shutdownServer()` method on the `admin` database
to safely shut down the `mongod`:

```sh
db.getSiblingDB("admin").shutdownServer()
```

Repeat until all config servers are offline.

**Step 6: Shut down shard replica set `mongod` instances.**

For each shard replica set, connect `mongosh` to each
`mongod` member in the replica set and shut them down. Shut down
the primary member last.

Use the `db.shutdownServer()` method on the `admin` database
to safely shut down the `mongod`:

```sh
db.getSiblingDB("admin").shutdownServer()
```

Repeat this step for each shard replica set until all `mongod`
instances in all shard replica sets are offline.

Once this step is complete, the entire sharded cluster should be offline.

**Step 7: Enforce Access Control on the Config Servers.**

Start *each* `mongod` in the config server replica set.
Include the `keyFile` setting. The `keyFile` setting enforces
both /core/security-internal-authentication and
/core/authorization.

You can specify the `mongod` settings either via a
configuration file or the command line.

**Configuration File**

If using a configuration file, for a config server replica
set, set `security.keyFile` to the keyfile's path,
`sharding.clusterRole` to `configsvr`, and
`replication.replSetName` to the name of the config
server replica set.

```yaml
security:
  keyFile: <path-to-keyfile>
sharding:
  clusterRole: configsvr
replication:
  replSetName: <setname>
storage:
   dbpath: <path>
```

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

Start the `mongod` specifying the `--config` option and the
path to the configuration file.

```shell
mongod --config <path-to-config>
```

**Command Line**

If using the command line parameters, for a config server replica
set, start the `mongod` with the `-keyFile`,
`--configsvr`, and `--replSet` parameters.

```bash
mongod --keyFile <path-to-keyfile> --configsvr --replSet <setname> --dbpath <path>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

For more information on command line options, see the
`mongod` reference page.

Make sure to use the original replica set name when restarting each
member. You cannot change the name of a replica set.

**Step 8: Enforce Access Control for each Shard in the Sharded Cluster.**

Running a `mongod` with the `keyFile` parameter enforces both
/core/security-internal-authentication and
/core/authorization.

Start *each* `mongod` in the replica set using either
a configuration file or the command line.

**Configuration File**

If using a configuration file, set the
`security.keyFile` option to the keyfile's path and the
`replication.replSetName` option to the *original* name
of the replica set.

```yaml
security:
  keyFile: <path-to-keyfile>
replication:
  replSetName: <setname>
storage:
   dbPath: <path>
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

If using the command line parameters, start the `mongod` and
specify the `--keyFile` and `--replSet` parameters.

```sh
mongod --keyfile <path-to-keyfile> --replSet <setname> --dbpath <path>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

For more information on startup parameters,
see the `mongod` reference page.

Make sure to use the original replica set name when restarting each
member. You cannot change the name of a replica set.

Repeat this step until all shards in the cluster are online.

**Step 9: Create a Shard-Local User Administrator (Optional).**

**Important:**

The localhost-exception allows clients connected over the
localhost interface to create users on a `mongod`
enforcing access control. After creating the first user,
the localhost-exception closes.

The first user must have privileges to create other users, such
as a user with the `userAdminAnyDatabase`. This ensures
that you can create additional users after the localhost-exception
closes.

If at least one user does *not* have privileges to create users,
once the localhost exception closes you may be unable to create
or modify users with new privileges, and therefore unable to
access certain functions or operations.

For each shard replica set in the cluster, connect
`mongosh` to the primary member over the
localhost interface. You must run
`mongosh` on the same machine as the target
`mongod` to use the localhost interface.

Create a user with the `userAdminAnyDatabase`
role on the `admin` database. This user can create
additional users for the shard replica set as necessary.
Creating this user also closes the localhost-exception.

The following example creates the shard-local user `fred` on the
`admin` database.

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
    pwd: passwordPrompt(),  // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```

**Step 10: Enforce Access Control for the `mongos` servers.**

Running a `mongod` with the `keyFile` parameter enforces both
/core/security-internal-authentication and
/core/authorization.

Start *each* `mongos` in the replica set using either
a configuration file or the command line.

**Configuration File**

If using a configuration file, set the
`security.keyFile` to the keyfile`s path and the
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
mongos --config <path-to-config-file>
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

At this point, the entire sharded cluster is back online and can
communicate internally using the keyfile specified. However, external
programs like `mongosh` need to use a correctly
provisioned user in order to read or write to the cluster.

**Step 11: Connect to the `mongos` instance over the localhost interface.**

Connect `mongosh` to one of the 
`mongos` instances over the localhost
interface. You must run `mongosh`
on the same physical machine as the `mongos` instance.

The localhost interface is only available
since no users have been created for the deployment. The
localhost interface closes after the
creation of the first user.

**Step 12: Create the user administrator.**

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

**Step 13: Authenticate as the user administrator.**

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

**Step 14: Create Administrative User for Cluster Management**

The cluster administrator user has the `clusterAdmin` role
for the sharded cluster and *not* the shard-local cluster
administrator.

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

**Step 15: Authenticate as cluster admin.**

To perform sharding operations, authenticate as a
`clusterAdmin` user with either the
`db.auth()` method or a new `mongosh` session
with the `username`, `password`, and `authenticationDatabase`
parameters.

**Note:**

This is the cluster administrator for the sharded cluster and *not*
the shard-local cluster administrator.

**Step 16: Start the balancer.**

Start the balancer.

```javascript
sh.startBalancer()
```

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0.3, `sh.startBalancer()`
also enables auto-splitting for the sharded cluster.

Use the `sh.getBalancerState()` to verify the balancer has started.

See /tutorial/manage-sharded-cluster-balancer for tutorials on
the sharded cluster balancer.

**Step 17: Create additional users (Optional).**

Create users to allow clients to connect and access the
sharded cluster. See database-user-roles for available built-in
roles, such as `read` and `readWrite`.
You may also want additional administrative users.
For more information on users, see /core/security-users.

To create additional users, you must authenticate as a user with
`userAdminAnyDatabase` or `userAdmin` roles.

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see
/tutorial/configure-x509-member-authentication.

To upgrade from keyfile internal authentication to X.509 internal
authentication, see
/tutorial/upgrade-keyfile-to-x509.

**See also:**

- /core/sharded-cluster-components
- /core/sharded-cluster-requirements
