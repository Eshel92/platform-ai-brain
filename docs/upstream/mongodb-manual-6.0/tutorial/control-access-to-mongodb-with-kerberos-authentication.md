<!-- Converted from tutorial/control-access-to-mongodb-with-kerberos-authentication.txt (reStructuredText). Includes are inlined. -->

# Configure Self-Managed MongoDB with Kerberos Authentication on Linux

## Overview

MongoDB Enterprise supports authentication using a Kerberos
service. Kerberos is an industry standard
authentication protocol for large client/server systems. MongoDB
Enterprise only supports the
[MIT implementation](https://kerberos.org/) of Kerberos.

## Prerequisites

To verify that you are using MongoDB Enterprise, pass the `--version`
command line option to the `mongod` or `mongos`:

```bash
mongod --version
```

In the output from this command, look for the string ``modules:
subscription` or `modules: enterprise`` to confirm you are using the
MongoDB Enterprise binaries.

For replica sets and sharded clusters, ensure that your configuration
uses fully qualified domain names (FQDN) rather than IP addresses or
unqualified hostnames. You must use the FQDN for GSSAPI to correctly
resolve the Kerberos realms and allow you to connect.

Setting up and configuring a Kerberos deployment is beyond the scope of
this document. Please refer to the [MIT Kerberos documentation](https://web.mit.edu/kerberos/krb5-latest/doc/) or your operating
system documentation for information on how to configure a Kerberos
deployment.

In order to use MongoDB with Kerberos, a
Kerberos service principal for each
`mongod` and `mongos` instance in your MongoDB
deployment must be [added to the Kerberos database](https://web.mit.edu/kerberos/krb5-latest/doc/admin/database.html#add-principal).
You can add the service principal by running a command similar to the
following on your KDC:

```bash
kadmin.local addprinc mongodb/m1.example.com@EXAMPLE.COM
```

On each system running `mongod` or `mongos`,
a keytab file must be [created](https://web.mit.edu/kerberos/krb5-latest/doc/admin/appl_servers.html#keytabs)
for the respective service principal. You can create the keytab file by
running a command similar to the following on the system running
`mongod` or `mongos`:

```bash
kadmin.local ktadd mongodb/m1.example.com@EXAMPLE.COM
```

## Procedure

The following procedure outlines the steps to add a Kerberos user
principal to MongoDB, configure a standalone `mongod` instance
for Kerberos support, and connect using `mongosh` and
authenticate the user principal.

**Step 1: Start `mongod` without Kerberos.**

For the initial addition of Kerberos users, start `mongod`
without Kerberos support.

If a Kerberos user is already in MongoDB and has the
privileges required to create a user, you can start
`mongod` with Kerberos support.

Include additional settings as appropriate to your deployment.

**Note:**

`mongod` and `mongos`
bind to localhost by default. If the members of your deployment are
run on different hosts or if you wish remote clients to connect to
your deployment, you must specify `--bind_ip` or
`net.bindIp`. 

**Step 2: Connect to `mongod`.**

Connect `mongosh` to the `mongod`
instance. If `mongod` has `--auth` enabled, ensure
you connect with the privileges required to create a user.

**Step 3: Add Kerberos Principal(s) to MongoDB.**

Add a Kerberos principal, `<username>@<KERBEROS REALM>` or
`<username>/<instance>@<KERBEROS REALM>`, to MongoDB in the
`$external` database. Specify the Kerberos realm in all uppercase.
The `$external` database allows `mongod` to consult an
external source (e.g. Kerberos) to authenticate. To specify the
user's privileges, assign roles to the
user.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

The following example adds the Kerberos principal
`application/reporting@EXAMPLE.NET` with read-only access to the
`records` database:

```javascript
use $external
db.createUser(
   {
     user: "application/reporting@EXAMPLE.NET",
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

**Step 4: Start `mongod` with Kerberos support.**

To start `mongod` with Kerberos support, set the
environmental variable `KRB5_KTNAME` to the path of the keytab
file and the `mongod` parameter
`authenticationMechanisms` to `GSSAPI` in the
following form:

```sh
env KRB5_KTNAME=<path to keytab file> \
mongod \
--setParameter authenticationMechanisms=GSSAPI \
<additional mongod options>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

For example, the following starts a standalone `mongod`
instance with Kerberos support:

```sh
env KRB5_KTNAME=/opt/mongodb/mongod.keytab \
/opt/mongodb/bin/mongod --auth \
--setParameter authenticationMechanisms=GSSAPI \
--dbpath /opt/mongodb/data --bind_ip localhost,<hostname(s)|ip address(es)>
```

The path to your `mongod` as well as your keytab file may differ. The keytab file
must be only accessible to the owner of the `mongod`
process.

With the official `.deb` or `.rpm` packages, you can set the
`KRB5_KTNAME` in a environment settings file. See
setting-krb5_ktname for details.

**Step 5: Connect `mongosh` to `mongod` and authenticate.**

Connect `mongosh` client as the Kerberos principal
`application/reporting@EXAMPLE.NET`. Before connecting, you
must have used Kerberos's `kinit` program to get credentials for
`application/reporting@EXAMPLE.NET`.

You can connect and authenticate from the command line.

```sh
mongosh --host hostname.example.net --authenticationMechanism=GSSAPI --authenticationDatabase='$external' --username application/reporting@EXAMPLE.NET
```

If you are connecting to a system whose hostname matches the
Kerberos name, ensure that you specify the fully qualified
domain name (FQDN) for the `--host`
option, rather than an IP address or unqualified hostname.

If you are connecting to a system whose hostname does not
match the Kerberos name, first connect `mongosh` 
to the `mongod`, and then from 
`mongosh`, use the `db.auth()` method to 
authenticate in the `$external` database.

```javascript
use $external
db.auth( { mechanism: "GSSAPI", user: "application/reporting@EXAMPLE.NET" } )
```

## Additional Considerations

### KRB5_KTNAME

If you installed MongoDB Enterprise using one of the official `.deb`
or `.rpm` packages, and you use the included init/upstart scripts to
control the `mongod` instance, you can set the `KRB5_KTNAME`
variable in the default environment settings file instead of setting
the variable each time.

Recent versions of Red Hat and Debian-based systems use `systemd`.
Older versions use `init` for system initialization. Follow the
appropriate instructions to configure the `KRB5_KTNAME` variable for
your system.

#### `systemd` Configuration Files

`systemd` stores configuration in unit files. Update the unit file to
set the `KRB5_KTNAME` variable.

**Step 1: Find the unit file**

```shell
sudo systemctl cat mongod
```

The `systemctl` command returns the file location and displays its
contents.

**Step 2: Set `KRB5_KTNAME`**

To set the `KRB5_KTNAME` variable, edit the following line to reflect
the location of your `keytab` file:

```shell
Environment="KRB5_KTNAME=<path-to-your-mongod.keytab-file>" 
```

**Step 3: Edit the unit file**

Add the edited line to the unit file. The edited unit file will
resemble:

```shell
[Unit]
Description=High-performance, schema-free document-oriented database
After=network.target
Documentation=https://docs.mongodb.org/manual

[Service]
User=mongodb
Group=mongodb
ExecStart=/usr/bin/mongod --config /etc/mongod.conf
Environment="KRB5_KTNAME=/etc/mongod.keytab"
PIDFile=/var/run/mongodb/mongod.pid
# file size
LimitFSIZE=infinity
# cpu time
LimitCPU=infinity
# virtual memory size
LimitAS=infinity
# open files
LimitNOFILE=64000
# processes/threads
LimitNPROC=64000
# locked memory
LimitMEMLOCK=infinity
# total threads (user+kernel)
TasksMax=infinity
TasksAccounting=false

# Recommended limits for for mongod as specified in
# http://docs.mongodb.org/manual/reference/ulimit/#recommended-settings

[Install]
WantedBy=multi-user.target
```

**Step 4: Reload the updated unit file:**

```shell
sudo systemctl daemon-reload
```

**Step 5: Restart the `mongod` service**

```shell
sudo systemctl restart mongod
```

 

#### `init` Configuration Files

For `.rpm` installations, the default environment settings file is
`/etc/sysconfig/mongod`.

For `.deb` installations, the file is `/etc/default/mongodb`.

Set the `KRB5_KTNAME` value by adding a line that resembles the
following:

```javascript
KRB5_KTNAME="<path to keytab>"
```

### Configure `mongos` for Kerberos

To start `mongos` with Kerberos support, set the environmental
variable `KRB5_KTNAME` to the path of its keytab file and the `mongos` parameter
`authenticationMechanisms` to `GSSAPI` in the following form:

```bash
env KRB5_KTNAME=<path to keytab file> \
mongos \
--setParameter authenticationMechanisms=GSSAPI \
<additional mongos options>
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

For example, the following starts a `mongos` instance with
Kerberos support:

```bash
env KRB5_KTNAME=/opt/mongodb/mongos.keytab \
mongos \
--setParameter authenticationMechanisms=GSSAPI \
--configdb shard0.example.net, shard1.example.net,shard2.example.net \
--keyFile /opt/mongodb/mongos.keyfile \
--bind_ip localhost,<hostname(s)|ip address(es)>
```

The path to your `mongos` as well as your keytab file may differ. The keytab file must
be only accessible to the owner of the `mongos` process.

Modify or include any additional `mongos` options as required
for your configuration. For example, instead of using
`--keyFile` for internal authentication of sharded cluster
members, you can use X.509 member authentication instead.

### Use a Config File

To configure `mongod` or `mongos` for Kerberos
support using a configuration file, specify the
`authenticationMechanisms` setting in the configuration file.

If using the YAML configuration file format:

```yaml
setParameter:
   authenticationMechanisms: GSSAPI
```

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

For example, if `/opt/mongodb/mongod.conf` contains the following
configuration settings for a standalone `mongod`:

```yaml
security:
   authorization: enabled
setParameter:
   authenticationMechanisms: GSSAPI
storage:
   dbPath: /opt/mongodb/data
net:
   bindIp: localhost,<hostname(s)|ip address(es)>
```

To start `mongod` with Kerberos support, use the following
form:

```bash
env KRB5_KTNAME=/opt/mongodb/mongod.keytab \
/opt/mongodb/bin/mongod --config /opt/mongodb/mongod.conf
```

The path to your `mongod`, keytab file,
and configuration file may differ. The
keytab file must be only accessible to the owner
of the `mongod` process.

### Troubleshoot Kerberos Setup for MongoDB

If you encounter problems when starting `mongod` or
`mongos` with Kerberos authentication, see
/tutorial/troubleshoot-kerberos.

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
