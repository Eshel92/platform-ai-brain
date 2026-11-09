<!-- Converted from tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime.txt (reStructuredText). Includes are inlined. -->

# Update Self-Managed Replica Set to Keyfile Authentication (No Downtime)

## Overview

To secure against unauthorized access, enforce authentication for your deployments. Authentication
for replica sets consists of internal authentication
among the replica set members, and user access control
for clients connecting to the replica set.

If your deployment does not currently enforce authentication, you can use the
`--transitionToAuth` option to enforce
authentication without downtime.

This tutorial uses the keyfile internal
authentication mechanism for internal security, and
authentication-scram-based role-based access controls for client connections.

### Cloud Manager and Ops Manager

If you are using Cloud Manager or Ops Manager to manage your deployment,
see the respective `Cloud Manager manual`
or the `Ops Manager manual` to enforce authentication.

### Architecture

This tutorial assumes that your replica set can elect a new
primary after stepping down the existing primary replica set member.
This requires:

- A majority of voting replica set members available after stepping down the
  primary.

- At least one secondary member that is not delayed, hidden,
  or Priority 0.

### Transition State

A `mongod` running with `--transitionToAuth` accepts both
authenticated and non-authenticated connections. Clients connected to the
`mongod` during this transition state can perform read, write, and
administrative operations on any database.

### Client Access

At the end of the following procedure, the replica set rejects any
client attempting to make a non-authenticated connection. The procedure creates
users for client applications to use when connecting to the
replica set.

See security-checklist-role-based-access-control for user creation and
management best practices.

### IP Binding

MongoDB binaries, `mongod` and
`mongos`, bind to `localhost` by default.

### Passwords

**Important:**

Passwords should be random, long, and complex to ensure system
security and to prevent or delay malicious access.

## Enforce Keyfile Access Control on Existing Replica Set

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

**Step 1: Create the user administrator.**

Connect to the primary to create a user with
`userAdminAnyDatabase` role. The
`userAdminAnyDatabase` role grants access to user creation
on any database in the deployment.

The following example creates the user `fred` with the
`userAdminAnyDatabase` role on the `admin` database.

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

```javascript
admin = db.getSiblingDB("admin")
admin.createUser(
  {
    user: "fred",
    pwd: " passwordPrompt(),     // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```

At the completion of this procedure, any client that administers users in
the replica set must authenticate as this user, or a user with
similar permissions.

See database-user-roles for a full list of built-in roles and
related to database administration operations.

**Step 2: Create the cluster administrator.**

Connect to the primary to create a user with
`clusterAdmin` role. The `clusterAdmin` role
grants access to replication operations, such as configuring the
replica set.

The following example creates the user `ravi` with the
`clusterAdmin` role on the `admin` database.

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
db.getSiblingDB("admin").createUser(
  {
    "user" : "ravi",
    "pwd" :  passwordPrompt(),     // or cleartext password
    roles: [ { "role" : "clusterAdmin", "db" : "admin" } ] 
  }
)
```

At the completion of this procedure, any client that administrates or
maintains the replica set must authenticate as this user, or a user with
similar permissions.

See cluster-admin-roles for a full list of built-in roles related to 
replica set operations.

**Step 3: Create users for client applications.**

Create users to allow client application to connect and interact with the
replica set. At the completion of this tutorial, clients must authenticate as 
a configured user to connect to the replica set.

See database-user-roles for basic built-in roles to use
in creating read-only and read-write users.

The following creates a user with read and write permissions
on the `foo` database.

**Important:**

Passwords should be random, long, and complex to ensure system security
and to prevent or delay malicious access.

Create a user with the 
`readWrite` role in the `foo` database.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.getSiblingDB("foo").createUser(
  {
    "user" : "joe",
    "pwd" :  passwordPrompt(),     // or cleartext password
    roles: [ { "role" : "readWrite", "db" : "foo" } ] 
  }
)
```

Clients authenticating as this user can perform read and write operations
against the `foo` database. See authentication-auth-as-user for
more on creating an authenticated connection to the replica set.

See the Add Users tutorial for more information on
adding users. Consider security best practices when adding new users.

**Step 4: Update Client Applications**

At this point in the procedure, the replica set does not enforce
authentication. However, client applications can still specify auth
credentials and connect to the replica set.

Update client applications to authenticate to the replica set using a
configured user. Authenticated connections require a username, password, and
the authentication database. See authentication-auth-as-user.

For example, the following connects to a replica set named `mongoRepl`
and authenticates as the user `joe`.

```shell
mongosh  -u joe -password  -authenticationDatabase foo --host mongoRepl/mongo1.example.net:27017, mongo2.example.net:27017, mongo3.example.net:27017
```

If you do not specify the password to the `-p`
command-line option, `mongosh` prompts for the
password.

If your application uses a MongoDB driver, see the associated
`driver` documentation for instructions on
creating an authenticated connection.

At the completion of this tutorial, the replica set rejects non-authenticated
client connections. Performing this step now ensures clients can connect
to the replica set before and after the transition.

**Step 5: Create a keyfile.**

With keyfile authentication, each
`mongod` instances in the replica set uses the contents of the keyfile as the
shared password for authenticating other members in the deployment. Only
`mongod` instances with the correct keyfile can join the replica set.

**Note:**

Keyfiles for internal membership authentication use YAML format to allow for multiple keys in a 
keyfile. The YAML format accepts either:

- A single key string (same as in earlier versions)

- A sequence of key strings

The YAML format is compatible with the existing single-key
keyfiles that use the text file format.

A key's length must be between 6 and 1024 characters and may only
contain characters in the base64 set. All members of the
replica set must share at least one common key.

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

**Step 6: Copy the keyfile to each replica set member.**

Copy the keyfile to each server hosting the replica set members.
Ensure that the user running the `mongod` instances is the owner of the
file and can access the keyfile.

Avoid storing the keyfile on storage mediums that can be easily
disconnected from the hardware hosting the `mongod` instances, such as a
USB drive or a network attached storage device.

**Step 7: Restart each secondary or arbiter member of the replica set with `transitionToAuth`.**

Restart each secondary or arbiter member in the
replica set, including in the configuration:

- The `security.transitionToAuth` setting. Starting the
  `mongod` with `security.transitionToAuth` set to
  `true` places the instance in a transition state where it can
  accept and create both authenticated and non-authenticated
  connections.

- An internal authentication mechanism such as
  `security.keyFile`.

You must restart each member one at a time to ensure a majority of
members in the replica set remain online.

From a `mongosh` session that is connected to the
secondary or arbiter, issue the `db.shutdownServer()`
against the `admin` database.

```javascript
admin = db.getSiblingDB("admin")
admin.shutdownServer()
```

Specify the following settings in your configuration file.

- `security.keyFile`, with the path to the keyfile.
- `replication.replSetName` to the original replica set name.
- `security.transitionToAuth` to `true`.

`mongod` and `mongos`
bind to localhost by default. If the members of your deployment are
run on different hosts or if you wish remote clients to connect to
your deployment, you must specify the `net.bindIp` setting.

```yaml
security:
  keyFile: <path-to-keyfile>
  transitionToAuth: true
replication:
  replSetName: <replicaSetName>
```

Specify the `--config` option with the path to the configuration
file when starting the `mongod`.

```shell
mongod --config <path-to-config-file>
```

For more information on the configuration file, see 
configuration options.

Alternatively, you can use the equivalent `mongod`
command-line options (e.g. `--transitionToAuth` and
`--keyFile`) when starting your `mongod`. See the
`mongod` reference page for a complete list of options.

Include additional settings as appropriate to your deployment.

At the end of this step, all secondaries and arbiters should be up
and running with `security.transitionToAuth` set to `true`.

**Step 8: Step down the primary member of the replica set and restart it with `--transitionToAuth`.**

Step down the primary member in the replica set and restart
the member, including in its configuration:

- The `security.transitionToAuth` setting. Starting the
  `mongod` with `security.transitionToAuth` set to
  `true` places the instance in a transition state where it can
  accept and create both authenticated and non-authenticated
  connections.

- An internal authentication mechanism such as
  `security.keyFile`.

Connect to the primary using `mongosh` and step down
the primary using the `rs.stepDown()` method.

```javascript
rs.stepDown()
```

Once the primary steps down and the replica set elects a new primary,
shut down the old primary `mongod`.

From a `mongosh` session that is connected to the old
primary, issue the `db.shutdownServer()` on the `admin`
database.

```javascript
admin = db.getSiblingDB("admin")
admin.shutdownServer()
```

Specify the following settings in your configuration file.

- `security.keyFile`, with the path to the keyfile.
- `replication.replSetName` to the original replica set name.
- `security.transitionToAuth` to `true`.

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

```yaml
security:
  keyFile: <path-to-keyfile>
  transitionToAuth: true
replication:
  replSetName: <replicaSetName>
```

Start the `mongod` using the configuration file.

```shell
mongod --config <path-to-config-file>
```

For more information on the configuration file, see 
configuration options.

Alternatively, you can use the equivalent `mongod`
command-line options (e.g. `--transitionToAuth` and
`--keyFile`) when starting your `mongod`. See the
`mongod` reference page for a complete list of options.

Include additional settings as appropriate to your deployment.

At the end of this step, all members of the replica set should be up
and running with `security.transitionToAuth` set to `true`
and `security.keyFile` set to the keyfile path.

**Step 9: Restart secondaries and arbiters *without* `--transitionToAuth`**

Restart each secondary or arbiter member in the replica set,
removing the `security.transitionToAuth` option on restart. You must do
this one at a time to ensure a majority of members in the replica set remain
online.

If the majority of replica set members are offline at the same time, the
replica set may go into read-only mode.

Connect `mongosh` to the secondary or arbiter, and
issue the `db.shutdownServer()` on the `admin` database.

```javascript
admin = db.getSiblingDB("admin")
admin.shutdownServer()
```

Restart the `mongod`, this time *without* the 
`security.transitionToAuth` option but *with* internal authentication
mechanism such as `security.keyFile`.

Specify the following settings in your configuration file.

- `security.keyFile`, with the path to the keyfile.
- `replication.replSetName` to the original replica set name.

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

```yaml
security:
  keyFile: <path-to-keyfile>
replication:
  replSetName: <replicaSetName>
```

Start the `mongod` using the configuration file:

```shell
mongod --config <path-to-config-file>
```

For more information on the configuration file, see 
configuration options.

You can also use the equivalent `mongod` options when starting your
`mongod`. See the `mongod` reference page for a complete list of
options.

Include additional settings as appropriate to your deployment.

At the end of this step, all secondaries and arbiters should be up and
running with internal authentication configured, but *without*
`security.transitionToAuth`. Clients can only connect to these
`mongod` instances by using the configured client authentication
mechanism.

**Step 10: Step down and restart the primary replica set member *without* `--transitionToAuth`.**

Step down the primary member in the replica set, then restart it
without the `security.transitionToAuth` option.

**Important:**

At the end of this step, clients not connecting with auth cannot connect
to the replica set. Update clients to connect with authentication *before*
completing this step to avoid loss of connectivity.

Connect to the primary using `mongosh` and step down
the primary using the `rs.stepDown()` method.

```javascript
rs.stepDown()
```

Once the primary steps down and the replica set elects a new primary,
shut down the old primary `mongod`. 

From a `mongosh` session that is connected to the old
primary, issue the `db.shutdownServer()` on the `admin`
database.

```javascript
admin = db.getSiblingDB("admin")
admin.shutdownServer()
```

Restart the `mongod`, this time *without* the 
`security.transitionToAuth` option but *with* the internal authentication
mechanism such as `security.keyFile`.

Specify the following settings in your configuration file.

- `security.keyFile`, with the path to the keyfile.
- `replication.replSetName` to the original replica set name.

```yaml
security:
  keyFile: <path-to-keyfile>
replication:
  replSetName: <replicaSetName>
```

Start the `mongod` using the configuration file:

```shell
mongod --config <path-to-config-file>
```

For more information on the configuration file, see 
configuration options.

You can also use the equivalent `mongod` options when starting your
mongod. See the `mongod` reference page for a complete list of
options.

Include additional settings as appropriate to your deployment.

At the end of this step, all members of the replica set should be up and
running with authentication enforced. Clients can only connect to these
`mongod` instances by using the configured client authentication
mechanism.

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see
/tutorial/configure-x509-member-authentication.

To upgrade from keyfile internal authentication to X.509 internal
authentication, see
/tutorial/upgrade-keyfile-to-x509.
