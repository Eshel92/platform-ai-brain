<!-- Converted from tutorial/configure-ldap-sasl-activedirectory.txt (reStructuredText). Includes are inlined. -->

# Authenticate Using SASL and LDAP with Active Directory

                    

MongoDB Enterprise provides support for proxy authentication of users.
This allows administrators to configure a MongoDB cluster to
authenticate users by proxying authentication requests to a specified
Lightweight Directory Access Protocol (LDAP) service.

**Note:**

For MongoDB 4.2 Enterprise binaries linked against
`libldap` (such as when running on RHEL), access to the
`libldap` is synchronized, incurring some performance/latency
costs.

For MongoDB 4.2 Enterprise binaries linked against
`libldap_r`, there is no change in behavior from earlier MongoDB
versions.

## Considerations

**Warning:**

MongoDB Enterprise for Windows does not support binding via
`saslauthd`.

- Linux MongoDB servers support binding to an LDAP server via the
  `saslauthd` daemon.

- Use secure encrypted or trusted connections between clients and the
  server, as well as between `saslauthd` and the LDAP server. The
  LDAP server uses the `SASL PLAIN` mechanism, sending and receiving
  data in **plain text**. You should use only a trusted channel such as
  a VPN, a connection encrypted with TLS/SSL, or a trusted wired
  network.

## Configure `saslauthd`

LDAP support for user authentication requires proper configuration of
the `saslauthd` daemon process as well as the MongoDB server.

**Step 1: Specify the mechanism.**

On systems that configure `saslauthd` with the
`/etc/sysconfig/saslauthd` file, such as Red Hat Enterprise Linux,
Fedora, CentOS, and Amazon Linux AMI, set the mechanism `MECH` to
`ldap`:

```javascript
MECH=ldap
```

On systems that configure `saslauthd` with the
`/etc/default/saslauthd` file, such as Ubuntu, set the `MECHANISMS`
option to `ldap`:

```javascript
MECHANISMS="ldap"
```

**Step 2: Adjust caching behavior.**

On certain Linux distributions, `saslauthd` starts with the caching
of authentication credentials *enabled*. Until restarted or until the
cache expires, `saslauthd` will not contact the LDAP server to
re-authenticate users in its authentication cache. This allows
`saslauthd` to successfully authenticate users in its cache, even in
the LDAP server is down or if the cached users' credentials are revoked.

To set the expiration time (in seconds) for the authentication cache, see
the [-t option](https://linux.die.net/man/8/saslauthd) of
`saslauthd`.

**Step 3: Configure LDAP Options with ActiveDirectory.**

If the `saslauthd.conf` file does not exist, create it.
The `saslauthd.conf` file usually resides in the `/etc`
folder. If specifying a different file path, see the
[-O option](https://linux.die.net/man/8/saslauthd) of
`saslauthd`.

To use with ActiveDirectory, start `saslauthd` with the following
configuration options set in the `saslauthd.conf` file:

```none
ldap_servers: <ldap uri>
ldap_use_sasl: yes
ldap_mech: DIGEST-MD5
ldap_auth_method: fastbind
```

For the `<ldap uri>`, specify the uri of the ldap server. For
example, `ldap_servers: ldaps://ad.example.net`.

For more information on `saslauthd` configuration, see
<http://www.openldap.org/doc/admin24/guide.html#Configuring saslauthd>.

**Step 4: Test the `saslauthd` configuration.**

Use `testsaslauthd` utility to test the `saslauthd`
configuration. For example:

```sh
testsaslauthd -u testuser -p testpassword -f /var/run/saslauthd/mux
```

- `0: OK "Success"` indicates successful authentication.
- `0: NO "authentication failed"` indicates a username, password, or
  configuration error.

Modify the file path with respect to the location of the 
`saslauthd` directory on the host operating system.

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

## Configure MongoDB

**Step 1: Add user to MongoDB for authentication.**

Add the user to the `$external` database in MongoDB. To specify the
user's privileges, assign roles to the
user.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

For example, the following adds a user with read-only access to
the `records` database.

```sh
db.getSiblingDB("$external").createUser(
    {
      user : <username>,
      roles: [ { role: "read", db: "records" } ]
    }
)
```

Add additional principals as needed. For more
information about creating and managing users, see
user-management-commands.

**Step 2: Configure MongoDB server.**

To configure the MongoDB server to use the `saslauthd` instance for
proxy authentication, include the following options when starting `mongod`:

- `--auth` command line option or `security.authorization` setting,

- `authenticationMechanisms` parameter set to `PLAIN`, and

- `saslauthdPath` parameter set to the path to the Unix-domain Socket of the `saslauthd` instance.

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

If you use the `authorization` option to enforce
authentication, you will need privileges to create a user.

For socket path of `/<some>/<path>/saslauthd`, set the
`saslauthdPath` to `/<some>/<path>/saslauthd/mux`,
as in the following command line example:

```none
mongod --auth --setParameter saslauthdPath=/<some>/<path>/saslauthd/mux --setParameter authenticationMechanisms=PLAIN
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

Or if using a YAML format configuration file, specify the following settings in
the file:

```yaml
security:
   authorization: enabled

setParameter:
   saslauthdPath: /<some>/<path>/saslauthd/mux
   authenticationMechanisms: PLAIN
```

Or, if using the :v2.4:`older configuration file format
</reference/configuration-options>`:

```ini
auth=true
setParameter=saslauthdPath=/<some>/<path>/saslauthd/mux
setParameter=authenticationMechanisms=PLAIN
```

To use the default Unix-domain socket path, set the
`saslauthdPath` to the empty string `""`, as in the
following command line example:

```none
mongod --auth --setParameter saslauthdPath="" --setParameter authenticationMechanisms=PLAIN
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

Or if using a YAML format configuration file, specify the following settings in
the file:

```yaml
security:
   authorization: enabled

setParameter:
   saslauthdPath: ""
   authenticationMechanisms: PLAIN
```

Or, if using the :v2.4:`older configuration file format
</reference/configuration-options>`:

```ini
auth=true
setParameter=saslauthdPath=""
setParameter=authenticationMechanisms=PLAIN
```

Include additional  options as required
for your configuration. For instance, if you wish remote clients to
connect to your deployment or your deployment members are run on
different hosts, specify the `net.bindIp` setting. 

**Step 3: Authenticate the user in `mongosh`.**

You can authenticate from the command line during connection, or
connect first and then authenticate using `db.auth()` method.

tabs:
   - id: cmdline
     name: Authenticate during Connection
     content: |

        To authenticate when connecting with
        `mongosh`, run `mongosh` with the following
        command-line options, substituting `<host>` and
        `<user>`, and enter your password when prompted:

        ```bash
        mongosh --host <host> --authenticationMechanism PLAIN --authenticationDatabase '$external' -u <user> -p
        ```

   - id: authafter
     name: Authenticate after Connection
     content: |

        Alternatively, connect without supplying credentials and then call
        the `db.auth()` method on the `$external` database. Specify
        the value `"PLAIN"` in the `mechanism` field, the user and
        password in the `user` and `pwd` fields respectively. Use the default
        `digestPassword` value (`false`) since the server must receive an
        undigested password to forward on to `saslauthd`, as in the
        following example:

        **Tip:**

        You can use the `passwordPrompt()` method in conjunction with
        various user authentication management methods and commands to prompt
        for the password instead of specifying the password directly in the
        method or command call. However, you can still specify the password
        directly as you would with earlier versions of the
        `mongo` shell.

        ```javascript
        db.getSiblingDB("$external").auth(
           {
             mechanism: "PLAIN",
             user: <username>,
             pwd:  passwordPrompt() // or cleartext password
           }
        )
        ```

        Enter the password when prompted.

The server forwards the password in plain text. In general, use only
on a trusted channel (VPN, TLS/SSL, trusted wired network). See
Considerations.
