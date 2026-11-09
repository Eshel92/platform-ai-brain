<!-- Converted from tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster-no-downtime.txt (reStructuredText). Includes are inlined. -->

# Update Self-Managed Sharded Cluster to Keyfile Authentication (No Downtime)

## Overview

**Important:**

The following procedure applies to sharded clusters using MongoDB
3.4 or later.

Earlier versions of MongoDB do not support no-downtime upgrade. For
sharded clusters using earlier versions of MongoDB, see
/tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster.

A MongoDB sharded cluster can enforce user authentication as well as internal authentication of its components to secure against unauthorized
access.

The following tutorial describes a procedure using
`security.transitionToAuth` to transition an existing sharded
cluster to enforce authentication without incurring downtime.

Before you attempt this tutorial, please familiarize yourself with the
contents of this document.

## Considerations

### Cloud Manager and Ops Manager

If you are using Cloud Manager or Ops Manager to manage your deployment,
refer to *Configure Access Control for MongoDB Deployments*
in the `Cloud Manager manual`
or `Ops Manager manual` to enforce authentication.

### IP Binding

MongoDB binaries, `mongod` and
`mongos`, bind to `localhost` by default.

### Internal and Client Authentication Mechanisms

This tutorial configures authentication using
authentication-scram for client authentication and a
keyfile for internal authentication.

Refer to the authentication documentation for a complete list of
available client and internal authentication mechanisms.

### Architecture

This tutorial assumes that each shard replica set, as well as the config
server replica set, can elect a new primary after stepping down its
existing primary.

A replica set can elect a primary only if both of the following conditions are
true:

- A majority of voting replica set members are available after stepping down
  the primary.

- There is at least one available secondary member that is not
  delayed, hidden, or Priority 0.

### Minimum number of `mongos` instances

Ensure your sharded cluster has at least two mongos instances
available. This tutorial requires restarting each `mongos` in
the cluster. If your sharded cluster has only one `mongos`
instance, this results in downtime during the period that the
`mongos` is offline.

## Enforce Keyfile Access Control on an Existing Sharded Cluster

### Create and Distribute the Keyfile

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
openssl rand -base64 755 > <path-to-keyfile>
chmod 400 <path-to-keyfile>
```

Copy the keyfile to each server hosting the sharded cluster members.
Ensure that the user running the `mongod` or `mongos` instances is the owner of the
file and can access the keyfile.

Avoid storing the keyfile on storage mediums that can be easily
disconnected from the hardware hosting the `mongod` or `mongos` instances, such as a
USB drive or a network attached storage device.

For more information on using keyfiles for internal authentication, refer to
internal-auth-keyfile.

### Configure Sharded Cluster Admin User and Client Users

You must connect to a `mongos` to complete the steps in this
section. The users created in these steps are cluster-level users and
cannot be used for accessing individual shard replica sets.

**Step 1: Create the adminstrator user.**

Use the `db.createUser()` method to create an administrator
user and assign it the following roles:

- `clusterAdmin` on the `admin` database
- `userAdmin` roles on the `admin` database

Clients performing maintenance operations or user administrative
operations on the sharded cluster must authenticate as this user
at the completion of this tutorial. Create this user now to ensure
that you have access to the cluster after enforcing authentication.

```javascript
admin = db.getSiblingDB("admin");
admin.createUser(
  {
    user: "admin",
    pwd: "<password>",
    roles: [
      { role: "clusterAdmin", db: "admin" },
      { role: "userAdmin", db: "admin" }
    ]
  }
);
```

**Important:**

Passwords should be random, long, and complex to prevent or hinder
malicious access.

**Step 2: Create additional users for client applications.**

In addition to the administrator user, you can create additional
users before enforcing authentication.. This ensures access to the
sharded cluster once you fully enforce authentication.

**Example:**

The following operation creates the user `joe` on the
`marketing` database, assigning to this user the
`readWrite` role on the `marketing` database`.

```javascript
db.getSiblingDB("marketing").createUser(
  {
    "user": "joe",
    "pwd": "<password>",
    "roles": [ { "role" : "readWrite", "db" : "marketing" } ]
  }
)
```

Clients authenticating as `"joe"` can perform read and write
operations on the `marketing` database.

See database-user-roles for roles provided by MongoDB.

See the Add Users tutorial for more information on
adding users. Consider security best practices when adding new users.

**Step 3: Update client applications to specify authentication credentials.**

While the sharded cluster does not currently enforce authentication, you can
still update client applications to specify authentication credentials when
connecting to the sharded cluster. This may prevent loss of connectivity at
the completion of this tutorial.

**Example:**

The following operation connects to the sharded cluster using
`mongosh`, authenticating as the user `joe` on the
`marketing` database.

```javascript
mongosh  --username "joe" --password "<password>" \
  --authenticationDatabase "marketing" --host mongos1.example.net:27017
```

If your application uses a MongoDB driver, see the associated
`driver` documentation for instructions on creating
an authenticated connection.

### Transition Each `mongos` Instance to Enforce Authentication

**Step 1: Create a new `mongos` configuration file.**

For each `mongos`:

#. Copy the existing `mongos` configuration file, giving it a
   distinct name such as `<filename>-secure.conf` (or `.cfg` if
   using Windows). You will use this new configuration file to
   transition the `mongos` to enforce authentication in the
   sharded cluster. Retain the original configuration file for backup
   purposes.

#. To the new configuration file, add the following settings:

   - `security.transitionToAuth` set to `true`

   - `security.keyFile` set to the keyfile path.

     If using a different internal authentication mechanism, specify
     settings appropriate for the mechanism.

   ```yaml
   security:
      transitionToAuth: true
      keyFile: <path-to-keyfile>
   ```

   The new configuration file should contain all of the configuration
   settings previously used by the `mongos` as well as the new
   security settings.

**Step 2: One at a time, restart the `mongos` with the new configuration file.**

**Note:**

If your cluster has only one `mongos`, this step results
in downtime while the `mongos` is offline.

Follow the procedure to restart the `mongos` instance, one
`mongos` at a time:

#. Connect to the `mongos` to shutdown.

#. Use the `db.shutdownServer()`
   method against the `admin` database to safely shut down the
   `mongos`.

   ```javascript
   db.getSiblingDB("admin").shutdownServer()
   ```

#. Restart `mongos` with the new configuration file, 
   specifying the path to the config file using
   `--config`. For example, if the new configuration file
   were named `mongos-secure.conf`:

   ```bash
   mongos --config <path>/mongos-secure.conf
   ```

   where `<path>` represents the system path to the folder
   containing the new configuration file.

Repeat the restart process for the next `mongos` instance
until all `mongos` instances in the sharded cluster have
been restarted.

At the end of this section, all `mongos` instances in the
sharded cluster are running with `security.transitionToAuth`
and `security.keyFile` internal authentication.

### Transition Config Server Replica Set Members to Enforce Authentication

**Step 1: Create a new `mongod` configuration file.**

For each `mongod` in the config server replica set,

#. Copy the existing `mongod` configuration file, giving it a
   distinct name such as `<filename>-secure.conf` (or `.cfg` if
   using Windows). You will use this new configuration file to
   transition the `mongod` to enforce authentication in the
   sharded cluster. Retain the original configuration file for
   backup purposes.

#. To the new configuration file, add the following settings:

   - `security.transitionToAuth` set to `true`

   - `security.keyFile` set to the keyfile path.

     If using a different internal authentication mechanism, specify
     settings appropriate for the mechanism.

   ```yaml
   security:
      transitionToAuth: true
      keyFile: <path-to-keyfile>
   ```

**Step 2: One at a time, restart the `mongod` with the new configuration file.**

Restart the replica set, one member at a time, starting with the
secondary members.

#. To restart the secondary members one at a time,

   a. Connect to the `mongod` and use the
      `db.shutdownServer()` method against the `admin`
      database to safely shut down the `mongod`.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the new 
      configuration file, specifying the path to the config file
      using `--config`. For example, if the new
      configuration file were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the new configuration file.

   Once this member is up, repeat for the next secondary member.

#. Once **all** the secondary members have restarted and are up,
   restart the primary:

   a. Connect to the `mongod`.

   #. Use the `rs.stepDown()` method to step down the primary and trigger an election.

      ```javascript
      rs.stepDown()
      ```

      You can use the `rs.status()` method to ensure the
      replica set has elected a new primary.

   #. Once you step down the primary and a new primary has been 
      elected, shut down the old primary using the
      `db.shutdownServer()` method against the `admin`
      database.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the new 
      configuration file, specifying the path to the config file using
      `--config`. For example, if the new configuration file
      were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the new configuration file.

At the end of this section, all `mongod` instances in the config
server replica set is running with `security.transitionToAuth` and
`security.keyFile` internal authentication.

### Transition Each Shard Replica Set Members to Enforce Authentication

#### Create the shard-local administrator

In a sharded cluster that enforces authentication, each shard replica
set should have its own shard-local administrator. You cannot use a shard-local administrator for
one shard to access another shard or the sharded cluster.

Connect to the primary member of each shard replica set and create a
user with the `db.createUser()` method, assigning it the following
roles:

- `clusterAdmin` on the `admin` database
- `userAdmin` roles on the `admin` database

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
    user: "admin",
    pwd: passwordPrompt(),  // or cleartext password
    roles: [
      { role: "clusterAdmin", db: "admin" },
      { role: "userAdmin", db: "admin" }
    ]
  }
)
```

At the completion of this tutorial, if you want to connect to the shard
to perform maintenance operation that require direct connection to a
shard, you must authenticate as the shard-local administrator.

**Note:**

Direct connections to a shard should only be for shard-specific
maintenance and configuration. In general, clients should connect to
the sharded cluster through the `mongos`.

#### Procedure

Transitioning one shard replica set at a time, repeat these steps for
each shard replica set in the sharded cluster.

**Step 1: Create a new `mongod` configuration file.**

For each `mongod` in the shard replica set,

#. Copy the existing `mongod` configuration file, giving it a
   distinct name such as `<filename>-secure.conf` (or `.cfg` if
   using Windows). You will use this new configuration file to
   transition the `mongod` to enforce authentication in the
   sharded cluster. Retain the original configuration file for
   backup purposes.

#. To the new configuration file, add the following settings:

   - `security.transitionToAuth` set to `true`

   - `security.keyFile` set to the keyfile path.

     If using a different internal authentication mechanism, specify
     settings appropriate for the mechanism.

   ```yaml
   security:
      transitionToAuth: true
      keyFile: <path-to-keyfile>
   ```

**Step 2: One at a time, restart the `mongod` with the new configuration file.**

Restart the replica set, one member at a time, starting with the
secondary members.

#. To restart the secondary members one at a time,

   a. Connect to the `mongod` and use the
      `db.shutdownServer()` method against the `admin`
      database to safely shut down the `mongod`.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the new 
      configuration file, specifying the path to the config file
      using `--config`. For example, if the new
      configuration file were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the new configuration file.

   Once this member is up, repeat for the next secondary member of the replica set until all secondaries have been updated.

#. Once **all** the secondary members have restarted and are up,
   restart the primary:

   a. Connect to the `mongod`.

   #. Use the `rs.stepDown()` method to step down the primary and trigger an election.

      ```javascript
      rs.stepDown()
      ```

      You can use the `rs.status()` method to ensure the
      replica set has elected a new primary.

   #. Once you step down the primary and a new primary has been 
      elected, shut down the old primary using the
      `db.shutdownServer()` method against the `admin`
      database.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the new 
      configuration file, specifying the path to the config file using
      `--config`. For example, if the new configuration file
      were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the new configuration file.

At this point in the tutorial, every component of the sharded cluster is
running with `--transitionToAuth` and `security.keyFile`
internal authentication. The sharded cluster has at least one administrative
user, and each shard replica set has a shard-local administrative user.

The remaining sections involve taking the sharded cluster out of the
transition state to fully enforce authentication.

### Restart Each `mongos` Instance without `transitionToAuth`

**Important:**

At the end of this section, clients must specify authentication
credentials to connect to the sharded cluster. Update clients to specify
authentication credentials *before* completing this section to avoid loss of
connectivity.

To complete the transition to fully enforcing authentication in the
sharded cluster, you must restart each `mongos` instance without
the `security.transitionToAuth` setting.

**Step 1: Remove `transitionToAuth` from the `mongos` configuration files.**

Remove the `security.transitionToAuth` key and its value
from the `mongos` configuration files created during this
tutorial. Leave the `security.keyFile` setting added in the
tutorial.

```yaml
security:
   keyFile: <path-to-keyfile>
```

**Step 2: Restart the `mongos` with the updated configuration file.**

**Note:**

If your cluster has only one `mongos`, this step results
in downtime while the `mongos` is offline.

Follow the procedure to restart `mongos` instance, one
`mongos` at a time:

#. Connect to the `mongos` to shutdown.

#. Use the `db.shutdownServer()`
   method against the `admin` database to safely shut down the
   `mongos`.

   ```javascript
   db.getSiblingDB("admin").shutdownServer()
   ```

#. Restart `mongos` with the updated configuration file, 
   specifying the path to the config file using
   `--config`. For example, if the updated configuration file
   were named `mongos-secure.conf`:

   ```bash
   mongos --config <path>/mongos-secure.conf
   ```

At the end of this section, all `mongos` instances enforce client
authentication and `security.keyFile` internal authentication.

### Restart Each Config Server Replica Set Member without `transitionToAuth`

**Important:**

At the end of this step, clients must specify authentication credentials to
connect to the config server replica set. Update clients to specify
authentication credentials *before* completing this section to avoid loss of
connectivity.

To complete the transition to fully enforcing authentication in the
sharded cluster, you must restart each `mongod` instance without
the `security.transitionToAuth` setting.

**Step 1: Remove `transitionToAuth` from the `mongod` configuration files.**

Remove the `security.transitionToAuth` key and its value
from the config server configuration files created during this
tutorial. Leave the `security.keyFile` setting added in the
tutorial.

```yaml
security:
   keyFile: <path-to-keyfile>
```

**Step 2: One at a time, restart the `mongod` with the updated configuration file.**

Restart the replica set, one member at a time, starting with the
secondary members.

#. To restart the secondary members one at a time,

   a. Connect to the `mongod` and use the
      `db.shutdownServer()` method against the `admin`
      database to safely shut down the `mongod`.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the updated 
      configuration file, specifying the path to the config file
      using `--config`. For example, if the new
      configuration file were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the updated configuration file.

   Once this member is up, repeat for the next secondary member.

#. Once **all** the secondary members have restarted and are up,
   restart the primary:

   a. Connect to the `mongod`.

   #. Use the `rs.stepDown()` method to step down the primary and trigger an election.

      ```javascript
      rs.stepDown()
      ```

      You can use the `rs.status()` method to ensure the
      replica set has elected a new primary.

   #. Once you step down the primary and a new primary has been 
      elected, shut down the old primary using the
      `db.shutdownServer()` method against the `admin`
      database.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the updated 
      configuration file, specifying the path to the config file using
      `--config`. For example, if the new configuration file
      were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the updated configuration file.

At the end of this section, all `mongod` instances in the config
server replica set enforce client authentication and
`security.keyFile` internal authentication.

### Restart Each Member in Each Shard Replica Set without `transitionToAuth`

**Important:**

At the end of this step, clients must specify authentication credentials to
connect to the shard replica set. Update clients to specify authentication
credentials *before* completing this section to avoid loss of connectivity.

To complete the transition to fully enforcing authentication in the sharded
cluster, you must restart every member of every shard replica set in the
sharded cluster without the `security.transitionToAuth` setting.

Transitioning one shard replica set at a time, repeat these steps for
each shard replica set in the sharded cluster.

**Step 1: Remove `transitionToAuth` from the `mongod` configuration files.**

Remove the `security.transitionToAuth` key and its value
from the config server configuration files created during this
tutorial. Leave the `security.keyFile` setting added in the
tutorial.

```yaml
security:
   keyFile: <path-to-keyfile>
```

**Step 2: One at a time, restart the `mongod` with the updated configuration file.**

Restart the replica set, one member at a time, starting with the
secondary members.

#. To restart the secondary members one at a time,

   a. Connect to the `mongod` and use the
      `db.shutdownServer()` method against the `admin`
      database to safely shut down the `mongod`.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the updated 
      configuration file, specifying the path to the config file
      using `--config`. For example, if the new
      configuration file were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the updated configuration file.

   Once this member is up, repeat for the next secondary member.

#. Once **all** the secondary members have restarted and are up,
   restart the primary:

   a. Connect to the `mongod`.

   #. Use the `rs.stepDown()` method to step down the primary and trigger an election.

      ```javascript
      rs.stepDown()
      ```

      You can use the `rs.status()` method to ensure the
      replica set has elected a new primary.

   #. Once you step down the primary and a new primary has been 
      elected, shut down the old primary using the
      `db.shutdownServer()` method against the `admin`
      database.

      ```javascript
      db.getSiblingDB("admin").shutdownServer()
      ```

   #. Restart the `mongod` with the updated 
      configuration file, specifying the path to the config file using
      `--config`. For example, if the new configuration file
      were named `mongod-secure.conf`:

      ```bash
      mongod --config <path>/mongod-secure.conf
      ```

      where `<path>` represents the system path to the folder
      containing the updated configuration file.

At the end of this section, all `mongos` and `mongod`
instances in the sharded cluster enforce client authentication and
`security.keyFile` internal authentication. Clients can only connect
to the sharded cluster by using the configured client authentication mechanism.
Additional components can only join the cluster by specifying the correct
keyfile.

## X.509 Certificate Internal Authentication

MongoDB supports X.509 certificate authentication for use with a secure TLS/SSL
connection. Sharded cluster members and replica set members can use X.509
certificates to verify their membership to the cluster or the replica set
instead of using internal-auth-keyfile.

For details on using X.509 certificates for internal authentication, see
/tutorial/configure-x509-member-authentication.

/tutorial/upgrade-keyfile-to-x509 describes how to upgrade a
deployment's internal auth mechanism from keyfile-based authentication to X.509
certificate-based auth.
