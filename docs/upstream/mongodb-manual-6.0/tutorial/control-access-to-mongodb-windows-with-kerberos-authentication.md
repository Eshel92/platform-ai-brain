<!-- Converted from tutorial/control-access-to-mongodb-windows-with-kerberos-authentication.txt (reStructuredText). Includes are inlined. -->

# Configure Self-Managed MongoDB with Kerberos Authentication on Windows

## Overview

MongoDB Enterprise supports authentication using a Kerberos
service. Kerberos is an industry standard
authentication protocol for large client/server systems. Kerberos allows
MongoDB and applications to take advantage of existing authentication
infrastructure and processes. MongoDB Enterprise only supports the
[MIT implementation](https://kerberos.org/)
of Kerberos.

## Prerequisites

Setting up and configuring a Kerberos deployment is beyond the scope of
this document. This tutorial assumes have configured a Kerberos
service principal for each
`mongod.exe` and `mongos.exe` instance.

For replica sets and sharded clusters, ensure that your configuration
uses fully qualified domain names (FQDN) rather than IP addresses or
unqualified hostnames. You must use the FQDN for GSSAPI to correctly
resolve the Kerberos realms and allow you to connect.

## Procedures

**Step 1: Start `mongod.exe` without Kerberos.**

For the initial addition of Kerberos users, start
`mongod.exe` without Kerberos support.

If a Kerberos user is already in MongoDB and has the
privileges required to create a user, you can start 
`mongod.exe` with Kerberos support.

Include additional settings as appropriate to your deployment.

**Note:**

`mongod` and `mongos`
bind to localhost by default. If the members of your deployment are
run on different hosts or if you wish remote clients to connect to
your deployment, you must specify `--bind_ip` or
`net.bindIp`. 

**Step 2: Connect to `mongod`.**

Connect `mongosh` to the `mongod.exe`
instance. If `mongod.exe` has `--auth` enabled, ensure
you connect with the privileges required to create a user.

**Step 3: Add Kerberos Principal(s) to MongoDB.**

Add a Kerberos principal, `<username>@<KERBEROS REALM>`, to
MongoDB in the `$external` database. Specify the Kerberos realm in
**ALL UPPERCASE**. The `$external` database allows
`mongod.exe` to consult an external source (e.g. Kerberos)
to authenticate. To specify the user's privileges, assign
roles to the user.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

The following example adds the Kerberos principal
`reportingapp@EXAMPLE.NET` with read-only access to the
`records` database:

```javascript
use $external
db.createUser(
   {
     user: "reportingapp@EXAMPLE.NET",
     roles: [ { role: "read", db: "records" } ]
   }
)
```

Add additional principals as needed. For every user you want to
authenticate using Kerberos, you must create a corresponding user in
MongoDB.
For more
information about creating and managing users, see
/reference/command/nav-user-management.

**Step 4: Start `mongod.exe` with Kerberos support.**

You must start `mongod.exe` as the service principal
account.

To start `mongod.exe` with Kerberos support, set
the `mongod.exe` parameter
`authenticationMechanisms` to `GSSAPI`:

```sh
mongod.exe --setParameter authenticationMechanisms=GSSAPI <additional mongod.exe options>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

For example, the following starts a standalone `mongod.exe`
instance with Kerberos support:

```sh
mongod.exe --auth --setParameter authenticationMechanisms=GSSAPI --bind_ip localhost,<hostname(s)|ip address(es)>
```

**Step 5: Connect `mongosh.exe` shell to `mongod.exe` and authenticate.**

Connect the `mongosh` shell client as the Kerberos
principal `application@EXAMPLE.NET`.

You can connect and authenticate from the command line.

Using `cmd.exe`:

```sh
mongosh.exe --host hostname.example.net --authenticationMechanism=GSSAPI --authenticationDatabase=$external --username reportingapp@EXAMPLE.NET
```

Using `Windows PowerShell`:

```sh
mongosh.exe --host hostname.example.net --authenticationMechanism=GSSAPI --authenticationDatabase='$external' --username reportingapp@EXAMPLE.NET
```

If you are connecting to a system whose hostname matches the
Kerberos name, ensure that you specify the fully qualified
domain name (FQDN) for the `--host`
option, rather than an IP address or unqualified hostname.

If you are connecting to a system whose hostname does not match
the Kerberos name, first connect the `mongosh` shell
to `mongod.exe`, and then from the
`mongosh` shell, use the `db.auth()` method
to authenticate in the `$external` database.

```javascript
use $external
db.auth( { mechanism: "GSSAPI", user: "reportingapp@EXAMPLE.NET" } )
```

## Additional Considerations

### Configure `mongos.exe` for Kerberos

To start `mongos.exe` with Kerberos support, set the
`mongos.exe` parameter `authenticationMechanisms`
to `GSSAPI`. You must start `mongos.exe` as the
service principal account:

```bash
mongos.exe --setParameter authenticationMechanisms=GSSAPI <additional mongos options>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

For example, the following starts a `mongos` instance with
Kerberos support:

```bash
mongos.exe --setParameter authenticationMechanisms=GSSAPI --configdb shard0.example.net, shard1.example.net,shard2.example.net --keyFile C:\<path>\mongos.keyfile --bind_ip localhost,<hostname(s)|ip address(es)>
```

Modify or include any additional `mongos.exe` options as required
for your configuration. For example, instead of using
`--keyFile` for internal authentication of sharded cluster
members, you can use X.509 member authentication instead.

### Assign Service Principal Name to MongoDB Windows Service

Use `setspn.exe` to assign the service principal name (SPN) to the
account running the `mongod.exe` and the
`mongos.exe` service:

```bash
setspn.exe -S <service>/<fully qualified domain name> <service account name>
```

**Example:**

If `mongod.exe` runs as a service named
`mongodb` on `testserver.mongodb.com` with the service account
name `mongodtest`, assign the SPN as follows:

```bash
setspn.exe -S mongodb/testserver.mongodb.com mongodtest
```

### Incorporate Additional Authentication Mechanisms

Kerberos authentication (GSSAPI (Kerberos))
can work alongside:

- MongoDB's SCRAM authentication mechanism:

  - SCRAM-SHA-1 

  - SCRAM-SHA-256 
  
- MongoDB's authentication mechanism for LDAP:

  - PLAIN (LDAP SASL)
 
- MongoDB's authentication mechanism for X.509:

  - MONGODB-X509)

Specify the mechanisms as follows:

```bash
--setParameter authenticationMechanisms=GSSAPI,SCRAM-SHA-256
```

Only add the other mechanisms if in use. This parameter setting does
not affect MongoDB's internal authentication of cluster members.

## Testing and Verification

After completing the configuration steps, you can validate your
configuration with the `mongokerberos` tool.

`mongokerberos` provides a convenient method to verify your 
platform's Kerberos configuration for use with MongoDB, and to test that 
Kerberos authentication from a MongoDB client works as expected. See the 
`mongokerberos` documentation for more information.

`mongokerberos` is available in MongoDB Enterprise only.
