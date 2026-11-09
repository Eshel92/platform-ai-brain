<!-- Converted from core/security-ldap.txt (reStructuredText). Includes are inlined. -->

# Self-Managed LDAP Proxy Authentication

[MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server) supports
proxying authentication requests to a Lightweight Directory Access Protocol
(LDAP) service.

MongoDB supports simple and SASL binding to LDAP servers:

| Via | Description |
|---|---|
| Operating system libraries | MongoDB supports binding to an LDAP server via operating system libraries. This allows MongoDB servers on Linux and Windows to use an LDAP server for authentication. In earlier versions, MongoDB on Microsoft Windows cannot connect to LDAP servers. |
| `saslauthd` | MongoDB servers on Linux supports binding to an LDAP server via the `saslauthd` daemon. Not available for MongoDB on Windows. |

## Considerations

A full description of LDAP is beyond the scope of this documentation. This
page assumes prior knowledge of LDAP.

This documentation only describes MongoDB LDAP authentication, and does not
replace other resources on LDAP. We encourage you to thoroughly familiarize
yourself with LDAP and its related subject matter before configuring LDAP
authentication.

MongoDB can provide [professional services](https://www.mongodb.com/products/consulting?tck=docs_server) for optimal
configuration of LDAP authentication for your MongoDB deployment.

### Connection Pool

When connecting to the LDAP server for authentication/authorization, MongoDB, 
by default:

- Uses connection pooling if run:

  - on Windows or

  - on Linux where MongoDB Enterprise binaries are linked against
    libldap_r.

- Does not use connection pooling if run:

  - on Linux where MongoDB Enterprise binaries are linked against
    libldap.

To change the connection pooling behavior, update the
`ldapUseConnectionPool` parameter.

### `saslauthd` and Directory Permissions

**Important:**

The parent directory of the `saslauthd` Unix domain socket file
specified to `security.sasl.saslauthdSocketPath` or
`--setParameter saslauthdPath` must grant 
read and execute  (`r-x`) permissions for either: 

- The user starting the `mongod` or 
  `mongos`, *or* 
- A group to which that user belongs.

The `mongod` or `mongos` cannot successfully authenticate via
`saslauthd` without the specified permission on the `saslauthd` 
directory and its contents.

### `libldap` and `libldap_r`

For MongoDB 4.2 Enterprise binaries linked against
`libldap` (such as when running on RHEL), access to the
`libldap` is synchronized, incurring some performance/latency
costs.

For MongoDB 4.2 Enterprise binaries linked against
`libldap_r`, there is no change in behavior from earlier MongoDB
versions.

### Managing LDAP Users on the MongoDB server

When using LDAP authentication **without** LDAP authorization, user management requires managing users both on
the LDAP server and the MongoDB server. For each user authenticating via
LDAP, MongoDB requires a user on the `$external` database whose name
exactly matches the authentication username. Changes to a user on the
LDAP server may require changes to the corresponding MongoDB
`$external` user.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

**Example:**

A user authenticates as `sam@dba.example.com`. The MongoDB server
binds to the LDAP server and authenticates the user, respecting any
`username transformations`.
On successful authentication, the MongoDB server then checks the
`$external` database for a user `sam@dba.example.com` and
grants the authenticated user the roles and privileges associated to
that user.

To manage users on the MongoDB server, you must authenticate as an LDAP user
whose corresponding MongoDB `$external` user has user administrative
privileges on the `$external` database, such as those provided by
`userAdmin`.

**Important:**

If no `$external` users have user administrative privileges on
`$external` database, you cannot perform user management for LDAP
authentication. This scenario may occur if you configure users prior to
enabling LDAP authentication, but do not create the appropriate user
administrators.

### Managing existing non-LDAP users

If there are existing users not on the `$external` database, you must meet
the following requirements for each user to ensure continued access:

- User has a corresponding user object on the LDAP server

- User exists on the `$external` database with equivalent roles and
  privileges

If you want to continue allowing access by users *not* on the
`$external` database, you must configure `setParameter`
`authenticationMechanisms` to include `SCRAM-SHA-1` and/or
`SCRAM-SHA-256` as appropriate. Users must then specify
`--authenticationMechanism SCRAM-SHA-1` or
`SCRAM-SHA-256` when authenticating.

### Deploying LDAP authentication on a replica set

For replica sets, configure LDAP authentication on
secondary and arbiter members first before configuring the
primary. This also applies to shard replica sets, or config server replica sets.
Configure one replica set member at a time to maintain a majority of members
for write availability.

### Deploying LDAP authentication on a sharded cluster

In sharded clusters, you must configure LDAP
authentication on the config servers and each
`mongos` for cluster-level users. You can optionally configure LDAP
authorization on each shard for shard-local users.

## LDAP Authentication via the Operating System LDAP libraries

The LDAP authentication via OS libraries process is summarized below:

#. A client authenticates to MongoDB, providing a user's credentials.

#. If the username requires mapping to an LDAP DN prior to binding against the
   LDAP server, MongoDB can apply transformations based on the configured
   `security.ldap.userToDNMapping` setting.

#. MongoDB binds to an LDAP server specified in
   `security.ldap.servers` using the provided username or, if a
   transformation was applied, the transformed username.

   MongoDB uses simple binding by default, but can also use `sasl` binding
   if configured in `security.ldap.bind.method` and
   `security.ldap.bind.saslMechanisms`.

   If a transformation requires querying the LDAP server, or if the LDAP
   server disallows anonymous binds, MongoDB uses the username and password
   specified to `security.ldap.bind.queryUser` and
   `security.ldap.bind.queryPassword` to bind to the LDAP server
   before attempting to authenticate the provided user credentials.

#. The LDAP server returns the result of the bind attempt to MongoDB. On
   success, MongoDB attempts to authorize the user.

#. The MongoDB server attempts to map the username to a user on the
   `$external` database, assigning the user any roles or privileges
   associated to a matching user. If MongoDB cannot find a matching user,
   authentication fails.

#. The client can perform those actions for which MongoDB granted the
   authenticated user roles or privileges.

To use LDAP for authentication via operating system libraries, specify the
following settings as a part of your `mongod` or `mongos`
configuration file:

| Option | Description | Required |
|---|---|---|
| `security.ldap.servers` | Quote-enclosed comma-separated list of LDAP servers in `host[:port]` format. You can prefix LDAP servers with `srv:` and `srv_raw:`. If your connection string specifies `"srv:<DNS_NAME>"`, `mongod` verifies that `"_ldap._tcp.gc._msdcs.<DNS_NAME>"` exists for SRV to support Active Directory. If not found, `mongod` verifies that `"_ldap._tcp.<DNS_NAME>"` exists for SRV. If an SRV record cannot be found, `mongod` warns you to use `"srv_raw:<DNS_NAME>"` instead. If your connection string specifies `"srv_raw:<DNS_NAME>"`, `mongod` performs an SRV record lookup for `"<DNS NAME>"`. | **YES** |
| `security.ldap.bind.method` | Used to specify the method the `mongod` or `mongos` uses to authenticate, or bind, to the LDAP server. Specify `sasl` to use one of the SASL protocols defined in `security.ldap.bind.saslMechanisms`. Defaults to `simple`. | **NO**, unless using `sasl` for binding to the LDAP server. |
| `security.ldap.bind.saslMechanisms` | Used to specify the SASL mechanisms `mongod` or `mongos` can use when authenticating or binding to the LDAP server. MongoDB and the LDAP server must agree on at least one SASL mechanism. Defaults to `DIGEST-MD5`. | **NO**, unless setting `method` to `sasl` *and* you need different or additional SASL mechanisms. |
| `security.ldap.bind.queryUser` | The LDAP entity, identified by its distinguished name (DN) or SASL name, with which the MongoDB server authenticates, or binds, when connecting to an LDAP server. Use with `queryPassword`. The user specified must have the appropriate privileges to execute queries on the LDAP server. | **NO**, unless specifying a query as part of a `userToDNMapping` transformation, or if the LDAP server's security settings disallow anonymous binds. |
| `security.ldap.bind.queryPassword` | The password used to authenticate to an LDAP server when using `queryUser`. | **NO**, unless specifying `queryUser`. |
| `security.ldap.bind.useOSDefaults` | Windows MongoDB deployments can use the operating system credentials in place of `queryUser` and `queryPassword` for authenticating or binding as when connecting to the LDAP server. | **NO**, unless replacing `queryUser` and `queryPassword`. |
| `security.ldap.userToDNMapping` | Clients may authenticate using a username whose format is incompatible with the format expected by the configured `bind method`. For example, `simple` binding may require a full LDAP DN while the username used to authenticate to MongoDB might be an e-mail address. `userToDNMapping` allows MongoDB to transform incoming usernames into a format compatible with your LDAP schema. MongoDB supports transformations using either a substitution template or an LDAP query template. If you specify a `userToDNMapping` transformation that uses LDAP queries as part of the transformation, you must also specify a `queryUser` with the appropriate level of permissions for the LDAP server | **NO**, unless client authenticate using usernames that require transformation. |

## LDAP Authentication via `saslauthd`

**Warning:**

MongoDB Enterprise for Windows does not support binding via
`saslauthd`.

### Considerations

- Linux MongoDB servers support binding to an LDAP server via the
  `saslauthd` daemon.

- Use secure encrypted or trusted connections between clients and the
  server, as well as between `saslauthd` and the LDAP server. The
  LDAP server uses the `SASL PLAIN` mechanism, sending and receiving
  data in **plain text**. You should use only a trusted channel such as
  a VPN, a connection encrypted with TLS/SSL, or a trusted wired
  network.

### Configuration

To configure the MongoDB server to bind to the LDAP server using via
`saslauthd`, start the `mongod` using either
the following command line options *or* the following configuration
file settings:

**commandline:**

- `--auth` to enable access control,

- `--setParameter` with the
  `authenticationMechanisms` set to `PLAIN`, and

- `--setParameter` with the
  `saslauthdPath` parameter set to the path to the
  Unix-domain Socket of the `saslauthd` instance. Specify an
  empty string `""` to use the default Unix-domain socket path.

Include any other command line options required for your
deployment. For complete documentation on `mongod`
command line options, see /reference/program/mongod.

**configuration:**

- `security.authorization` set to `enabled`,

- `setParameter` with the 
  `authenticationMechanisms` parameter set to
  `PLAIN`, and

- `setParameter` with the `saslauthdPath` set
  to the path to the Unix-domain Socket of the saslauthd instance.
  Specify an empty string `""` to use the default Unix-domain
  socket path.

Include any other configuration file settings required for your
deployment. For complete documentation on configuration files, see
YAML configuration file.

You need to create or update the `saslauthd.conf` file with the parameters
appropriate for your LDAP server. Documenting `saslauthd.conf` is out
of scope for this documentation. 

**Important:**

The parent directory of the `saslauthd` Unix domain socket file
specified to `security.sasl.saslauthdSocketPath` or
`--setParameter saslauthdPath` must grant 
read and execute  (`r-x`) permissions for either: 

- The user starting the `mongod` or 
  `mongos`, *or* 
- A group to which that user belongs.

The `mongod` or `mongos` cannot successfully authenticate via
`saslauthd` without the specified permission on the `saslauthd` 
directory and its contents.

The following tutorials provide basic
information on configuring `saslauthd.conf` to work with two popular
LDAP services:

- /tutorial/configure-ldap-sasl-openldap

- /tutorial/configure-ldap-sasl-activedirectory

Please see the documentation for `saslauthd` as well as your specific
LDAP service for guidance.

## Connect to a MongoDB server via LDAP authentication

To authenticate to a MongoDB server via LDAP authentication, use
`db.auth()` on the `$external` database with the following
parameters:

| Option | Description |
|---|---|
| `username` | The username to authenticate as. |
| `password` | The password to authenticate with. |
| `mechanism` | Set to `PLAIN`. |
