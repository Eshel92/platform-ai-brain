<!-- Converted from tutorial/enforce-keyfile-access-control-in-existing-replica-set.txt (reStructuredText). Includes are inlined. -->

# Update Self-Managed Replica Set to Keyfile Authentication

## Overview

Enforcing access control on an existing replica set requires
configuring:

- Security between members of the replica set using
  Internal Authentication, and

- Security between connecting clients and the replica set using
  User Access Controls.

For this tutorial, each member of the replica set uses the same internal
authentication mechanism and settings.

Enforcing internal authentication also enforces user access control. To
connect to the replica set, clients like `mongosh` need to
use a user account. See
security-replSet-auth-access-control.

### Cloud Manager and Ops Manager

If Cloud Manager or Ops Manager is managing your deployment, see the
`Cloud Manager manual` or the `Ops
Manager manual` for
enforcing access control.

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

This tutorial uses the `mongod` programs. Windows users should
use the `mongod.exe` program instead.

### Keyfile Security

Keyfiles are bare-minimum forms of security and are best suited for testing or
development environments. For production environments we recommend using
X.509 certificates.

### Users

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

### Downtime

The following procedure for enforcing access control requires downtime.
For a procedure that does not require downtime, see
/tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime
instead.

## Enforce Keyfile Access Control on Existing Replica Set

**Step 1: Create a keyfile.**

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

**Step 2: Copy the keyfile to each replica set member.**

Copy the keyfile to each server hosting the replica set members.
Ensure that the user running the `mongod` instances is the owner of the
file and can access the keyfile.

Avoid storing the keyfile on storage mediums that can be easily
disconnected from the hardware hosting the `mongod` instances, such as a
USB drive or a network attached storage device.

**Step 3: Shut down all members of the replica set.**

Shut down each `mongod` in the replica set, starting with the 
secondaries. Continue until *all* members of the 
replica set are offline, including any arbiters. 
The primary must be the *last* member shut down to avoid 
potential rollbacks.

To shut down a `mongod`, connect each `mongod` using
`mongosh` and issue the `db.shutdownServer()` on the 
`admin` database:

```sh
use admin
db.shutdownServer()
```

At the end of this step, *all* members of the replica set should be offline.

**Step 4: Restart each member of the replica set with access control enforced.**

Restart *each* `mongod` in the replica set with either the
`security.keyFile` configuration file setting or the
`--keyFile` command-line option. Running `mongod` with
the `--keyFile` command-line option or the
`security.keyFile` configuration file setting enforces both
/core/security-internal-authentication and
/core/authorization.

If using a configuration file, set

- `security.keyFile` to the keyfile's path, and

- `replication.replSetName` to the replica set name.

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

```yaml
security:
  keyFile: <path-to-keyfile>
replication:
  replSetName: <replicaSetName>
net:
   bindIp: localhost,<hostname(s)|ip address(es)>
```

Start the `mongod` using the configuration file:

```shell
mongod --config <path-to-config-file>
```

For more information on the configuration file, see
configuration options.

If using the command line options, start the `mongod` with the following options:

- `--keyFile` set to  the keyfile's path, and

- `--replSet` set to the replica set name.

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

```sh
mongod --keyFile <path-to-keyfile> --replSet <replicaSetName> --bind_ip localhost,<hostname(s)|ip address(es)>
```

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

For more information on command-line options, see the
`mongod` reference page.

**Step 5: Connect to the primary using the localhost interface.**

Connect `mongosh` to one of the 
`mongod` instances over the localhost
interface. You must run `mongosh`
on the same physical machine as the `mongod` instance.

Use `rs.status()` to identify the primary replica set
member. If you are connected to the primary, continue to the next
step. If not, connect `mongosh` to the primary
over the localhost
interface.

**Important:** You must connect to the primary before proceeding.

**Step 6: Create the user administrator.**

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
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
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

**Step 7: Authenticate as the User Administrator.**

Authenticate to the `admin` database.

In `mongosh`, use `db.auth()` to
authenticate. For example, the following authenticate as the user
administrator `fred`:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
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

**Step 8: Create the cluster administrator (Optional).**

The cluster administrator user has the `clusterAdmin` role, 
which grants access to replication operations.

Create a cluster administrator user and assign the
`clusterAdmin` role in the `admin` database:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
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
replica set operations.

**Step 9: Create additional users (Optional).**

Create users to allow clients to connect and interact with the replica set.
See database-user-roles for basic built-in roles to use in creating
read-only and read-write users.

You may also want additional administrative users.
For more information on users, see /core/security-users.

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see
/tutorial/configure-x509-member-authentication.

To upgrade from keyfile internal authentication to X.509 internal
authentication, see
/tutorial/upgrade-keyfile-to-x509.
