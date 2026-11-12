<!-- Part 5 of 7 of reference/configuration-options.md (split because the page is big). -->

### `security` Options

```yaml
security:
   keyFile: <string>
   clusterAuthMode: <string>
   authorization: <string>
   transitionToAuth: <boolean>
   javascriptEnabled:  <boolean>
   redactClientLogData: <boolean>
   clusterIpSourceAllowlist:
     - <string>
   sasl:
      hostName: <string>
      serviceName: <string>
      saslauthdSocketPath: <string>
   enableEncryption: <boolean>
   encryptionCipherMode: <string>
   encryptionKeyFile: <string>
   kmip:
      keyIdentifier: <string>
      rotateMasterKey: <boolean>
      serverName: <string>
      port: <string>
      clientCertificateFile: <string>
      clientCertificatePassword: <string>
      clientCertificateSelector: <string>
      serverCAFile: <string>
      connectRetries: <int>
      connectTimeoutMS: <int>
   ldap:
      servers: <string>
      bind:
         method: <string>
         saslMechanisms: <string>
         queryUser: <string>
         queryPassword: <string | array>
         useOSDefaults: <boolean>
      transportSecurity: <string>
      timeoutMS: <int>
      userToDNMapping: <string>
      authz:
         queryTemplate: <string>
      validateLDAPServerConfig: <boolean>
```

**`security.keyFile`**

*Type*: string

The path to a key file that stores the shared secret
that MongoDB instances use to authenticate to each other in a
sharded cluster or replica set. `keyFile` implies
`security.authorization`. See inter-process-auth for more
information.

Keyfiles for internal membership authentication use YAML format to allow for multiple keys in a 
keyfile. The YAML format accepts either:

- A single key string (same as in earlier versions)

- A sequence of key strings

The YAML format is compatible with the existing single-key
keyfiles that use the text file format.

**`security.clusterAuthMode`**

*Type*: string

*Default*: keyFile

The authentication mode used for cluster authentication. If you use
internal X.509 authentication,
specify so here. This option can have one of the following values:

| Value | Description |
|---|---|
| `keyFile` | Use a keyfile for authentication. Accept only keyfiles. |
| `sendKeyFile` | For rolling upgrade purposes. Send a keyfile for authentication but can accept both keyfiles and X.509 certificates. |
| `sendX509` | For rolling upgrade purposes. Send the X.509 certificate for authentication but can accept both keyfiles and X.509 certificates. |
| `x509` | Recommended. Send the X.509 certificate for authentication and accept only X.509 certificates. |

If `--tlsCAFile` or `tls.CAFile` is not
specified and you are not using X.509 authentication, you must set the 
`tlsUseSystemCA` parameter to `true`. This makes MongoDB use 
the system-wide CA certificate store when connecting to a TLS-enabled server.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

   

**`security.authorization`**

*Type*: string

*Default*: disabled

Enable or disable Role-Based Access Control (RBAC) to govern each
user's access to database resources and operations.

Set this option to one of the following:

| Value | Description |
|---|---|
| `enabled` | A user can access only the database resources and actions for which they have been granted privileges. |
| `disabled` | A user can access any database and perform any action. |

See authorization for more information.

**Changed in version:** 7.0.41

`security.authorization` enforces case-sensitive values. You
must set it to `enabled` or `disabled` exactly. `mongod`
rejects any other value at startup. Earlier versions of MongoDB
silently ignore incorrect case such as `Enabled` or
`eNaBlEd` and leave authorization disabled.

The `security.authorization` setting is available only for `mongod`.

**`security.transitionToAuth`**

*Type*: boolean

*Default*: false

Allows the `mongod` or `mongos` to accept and 
create authenticated and non-authenticated connections to and from other 
`mongod` and `mongos` instances in the deployment. 
Used for performing rolling transition of replica sets or sharded clusters
from a no-auth configuration to internal authentication.
Requires specifying a internal authentication mechanism such as
`security.keyFile`.

For example, if using keyfiles for
internal authentication, the `mongod` or `mongos` creates
an authenticated connection with any `mongod` or `mongos`
in the deployment using a matching keyfile. If the security mechanisms do
not match, the `mongod` or `mongos` utilizes a non-authenticated connection instead.

A `mongod` or `mongos` running with `security.transitionToAuth`
does not enforce user access
controls. Users may connect to your deployment without any
access control checks and perform read, write, and administrative operations.

**Note:**

A `mongod` or `mongos` running with internal authentication
and *without* `security.transitionToAuth` requires clients to
connect
using user access controls. Update clients to
connect to the `mongod` or `mongos` using the appropriate user
prior to restarting `mongod` or `mongos` without `security.transitionToAuth`.

**`security.javascriptEnabled`**

*Type*: boolean

*Default*: true

Enables or disables server-side JavaScript execution. When disabled, you cannot use
operations that perform server-side execution of JavaScript code,
such as the `$where` query operator, `mapReduce`
command, `$accumulator`, and `$function`.

If you do not use these operations, disable server-side scripting.

`security.javascriptEnabled` is available for both
`mongod` and `mongos`. In earlier versions, the
setting is only available for `mongod`.

**`security.redactClientLogData`**

*Type*: boolean

*Available in MongoDB Enterprise only.*

A `mongod` or `mongos` running with `security.redactClientLogData` redacts any message accompanying a given
log event before logging. This prevents the `mongod` or `mongos` from writing
potentially sensitive data stored on the database to the diagnostic log.
Metadata such as error or operation codes, line numbers, and source file
names are still visible in the logs.

Use `security.redactClientLogData` in conjunction with
security-encryption-at-rest and
transport-encryption to assist compliance with
regulatory requirements.

For example, a MongoDB deployment might store Personally Identifiable
Information (PII) in one or more collections. The `mongod` or `mongos` logs events
such as those related to CRUD operations, sharding metadata, etc. It is
possible that the `mongod` or `mongos` may expose PII as a part of these logging
operations. A `mongod` or `mongos` running with `security.redactClientLogData` removes any message
accompanying these events before being output to the log, effectively
removing the PII.

Diagnostics on a `mongod` or `mongos` running with `security.redactClientLogData` may be more difficult
due to the lack of data related to a log event. See the
process logging manual page for an
example of the effect of `security.redactClientLogData` on log output.

On a running `mongod` or `mongos`, use `setParameter` with the
`redactClientLogData` parameter to configure this setting.

**`security.clusterIpSourceAllowlist`**

*Type*: list

**New in version:** 5.0

**Changed in version:** 5.2

A list of IP addresses/CIDR ([Classless Inter-Domain Routing](https://tools.ietf.org/html/rfc4632)) ranges against which the
`mongod` validates authentication requests from other 
members of the replica set and, if part of a sharded cluster, the 
`mongos` instances. The `mongod` verifies 
that the originating IP is either explicitly in the list or belongs 
to a CIDR range in the list. If the IP address is not present, the 
server does not authenticate the `mongod` or `mongos`.

`security.clusterIpSourceAllowlist` has no effect on a `mongod`
started without authentication.

Starting in MongoDB 5.2, you can configure
`security.clusterIpSourceAllowlist` on a running `mongod` or
`mongos` using `setParameter`.

This example updates `security.clusterIpSourceAllowlist`
during runtime to include the IP addresses `"1.1.1.1/24"`, 
`"2.2.2.2/16"`, and `"3.3.3.3"`.

```javascript
db.adminCommand( {
   setParameter: 1,
   "clusterIpSourceAllowlist": ["1.1.1.1/24", "2.2.2.2/16", "3.3.3.3"]
} );
```

This example updates `security.clusterIpSourceAllowlist` during
runtime to exclude all IP addresses:

```javascript
 db.adminCommand( {
    setParameter: 1,
    "clusterIpSourceAllowlist": null
} );
```

`security.clusterIpSourceAllowlist` has no effect on a 
`mongod` started without
authentication.

`security.clusterIpSourceAllowlist` requires specifying each 
IPv4/6 address or Classless Inter-Domain Routing 
([CIDR](https://tools.ietf.org/html/rfc4632)) range as a YAML list:

```yaml
security:
  clusterIpSourceAllowlist:
    - 192.0.2.0/24
    - 127.0.0.1
    - ::1
```

**Important:**

Ensure `security.clusterIpSourceAllowlist` includes the 
IP address *or* CIDR ranges that include the IP address of each 
replica set member or `mongos` in the deployment to 
ensure healthy communication between cluster components.

#### Key Management Configuration Options

```yaml
security:
   enableEncryption: <boolean>
   encryptionCipherMode: <string>
   encryptionKeyFile: <string>
   kmip:
      keyIdentifier: <string>
      rotateMasterKey: <boolean>
      serverName: <string>
      port: <int>
      clientCertificateFile: <string>
      clientCertificatePassword: <string>
      clientCertificateSelector: <string>
      serverCAFile: <string>
      connectRetries: <int>
      connectTimeoutMS: <int>
      activateKeys: <boolean>
      keyStatePollingSeconds: <int>
      useLegacyProtocol: <boolean>
```

**`security.enableEncryption`**

*Type*: boolean

*Default*: false

Enables encryption for the WiredTiger storage engine. You must set
to `true` to pass in encryption keys and configurations.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.encryptionCipherMode`**

*Type*: string

*Default*: `AES256-CBC`

The cipher mode to use for encryption at rest:

| Mode | Description |
|---|---|
| `AES256-CBC` | 256-bit Advanced Encryption Standard in Cipher Block Chaining Mode |
| `AES256-GCM` | 256-bit Advanced Encryption Standard in Galois/Counter Mode Available only on Linux. MongoDB Enterprise on Windows no longer supports `AES256-GCM` as a block cipher for encryption at rest. This usage is only supported on Linux. |

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.encryptionKeyFile`**

*Type*: string

The path to the local keyfile when managing keys through a process *other
than* KMIP. Only set when managing keys through a process other than KMIP.
If data is already encrypted using KMIP, MongoDB throws an error.

Requires `security.enableEncryption` to be `true`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.keyIdentifier`**

*Type*: string

Unique KMIP identifier for an existing key within the KMIP server.
Include to use the key associated with the identifier as the system
key. You can only use the setting the first time you enable
encryption for the `mongod` instance. Requires
`security.enableEncryption` to be true.

If unspecified, MongoDB requests that the KMIP server create a
new key to utilize as the system key.

If the KMIP server cannot locate a key with the specified identifier
or the data is already encrypted with a key, MongoDB throws an error.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.rotateMasterKey`**

*Type*: boolean

*Default*: false

If true, rotate the master key and re-encrypt the internal
keystore.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**See also:**

kmip-master-key-rotation

   

**`security.kmip.serverName`**

*Type*: string

Hostname or IP address of the KMIP server to connect to. Requires
`security.enableEncryption` to be true.

You can specify multiple KMIP servers as a comma-separated list, for example
`server1.example.com,server2.example.com`. On startup, the
`mongod` attempts to establish a connection to each
server in the order listed, and selects the first server to
which it can successfully establish a connection. KMIP server
selection occurs only at startup.

`mongod` verifies the connection to the KMIP server on startup.

The server name specified in `security.kmip.serverName` 
must match either the Subject Alternative Name `SAN` or the 
Common Name `CN` on the certificate presented by
the KMIP server. `SAN` can be a system name or an IP address. 

If `SAN` is present, `mongod` does not try to match against `CN`.

If the hostname or IP address of the KMIP server does does not match
either `SAN` or `CN`, `mongod` does not start.

Starting in MongoDB 4.2, when performing comparison of SAN, MongoDB
supports comparison of DNS names or IP addresses. In previous versions,
MongoDB only supports comparisons of DNS names.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.port`**

*Type*: int

*Default*: 5696

Port number to use to communicate with the KMIP server. Requires
`security.kmip.serverName`. Requires
`security.enableEncryption` to be true.

If specifying multiple KMIP servers with
`security.kmip.serverName`, the `mongod`
uses the port specified with `security.kmip.port` for all
provided KMIP servers.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.clientCertificateFile`**

*Type*: string

Path to the `.pem` file used to authenticate MongoDB to the KMIP
server. The specified `.pem` file must contain both the TLS/SSL
certificate and key. 

To use this setting, you must also specify the
`security.kmip.serverName` setting.

**Note:**

Starting in 4.0, on macOS or Windows, you can use a certificate
from the operating system's secure store instead of a PEM key
file. See `security.kmip.clientCertificateSelector`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.clientCertificatePassword`**

*Type*: string

The password to decrypt the Private Key of the Client Certificate that
connects to the KMIP server. This option authenticates
MongoDB to the KMIP server and requires that you provide a
`--kmipClientCertificateFile`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`security.kmip.clientCertificateSelector`**

*Type*: string

**New in version:** 5.0

Available on Windows and macOS as an alternative to
`security.kmip.clientCertificateFile`. 

`security.kmip.clientCertificateFile` and `security.kmip.clientCertificateSelector` options are mutually exclusive. You can only
specify one.

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store to
authenticate MongoDB to the KMIP server.

`security.kmip.clientCertificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.serverCAFile`**

*Type*: string

Path to CA File. Used for validating secure client connection to
KMIP server.

**Note:**

Starting in 4.0, on macOS or Windows, you can use a certificate
from the operating system's secure store instead of a PEM key
file. See `security.kmip.clientCertificateSelector`. When using the secure store, you do not
need to, but can, also specify the `security.kmip.serverCAFile`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.connectRetries`**

*Type*: int

*Default*: 0

How many times to retry the initial connection to the KMIP server.
Use together with `connectTimeoutMS` to
control how long the `mongod` waits for a response
between each retry.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.connectTimeoutMS`**

*Type*: int

*Default*: 5000

Timeout in milliseconds to wait for a response from the KMIP server.
If the `connectRetries` setting is specified,
the `mongod` waits up to the value specified with
`connectTimeoutMS` for each retry.

Value must be `1000` or greater.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`security.kmip.activateKeys`**

*Type*: boolean

*Default*: true

**New in version:** 5.3

Activates all newly created KMIP keys upon creation and then periodically 
checks those keys are in an active state.  

When `security.kmip.activateKeys` is `true` and you have existing keys 
on a KMIP server, the key must be activated first or the `mongod` 
node fails to start.

If the key being used by the mongod transitions into a non-active state, 
the `mongod` node shuts down unless `kmipActivateKeys` is 
false. To ensure you have an active key, rotate the KMIP master key by 
using `security.kmip.rotateMasterKey`.

**`security.kmip.keyStatePollingSeconds`**

*Type*: int

*Default*: 900 seconds

**New in version:** 5.3

Frequency in seconds at which mongod polls the KMIP server for active keys. 

To disable disable polling, set the value to `-1`. 

**`security.kmip.useLegacyProtocol`**

*Type*: boolean

*Default*: false

**New in version:** 7.0 (and 6.0.6)

When `true`, `mongod` uses KMIP protocol version 1.0 or 1.1 instead
of the default version. The default KMIP protocol is version 1.2.

To use audit log encryption
with KMIP version 1.0 or 1.1, you must specify
`auditEncryptKeyWithKMIPGet` at startup.

To use KMIP protocol version 1.0 or 1.1, substitute your local values
and add an entry like this to your `mongod` configuration file:

```bash
security:
  enableEncryption: true
  kmip:
    serverName: "mdbhost.somecompany.com"
    serverCAFile: "security/libs/trusted-ca.pem"
    clientCertificateFile: "security/libs/trusted-client.pem"
    useLegacyProtocol: true
```

#### `security.sasl` Options

```yaml
security:
   sasl:
      hostName: <string>
      serviceName: <string>
      saslauthdSocketPath: <string>
```

**`security.sasl.hostName`**

*Type*: string

A fully qualified server domain name for the purpose of configuring SASL
and Kerberos authentication. The SASL hostname overrides the hostname
only for the configuration of SASL and Kerberos.
   

**`security.sasl.serviceName`**

*Type*: string

Registered name of the service using SASL. This option allows you to
override the default Kerberos
service name component of the Kerberos
principal name, on a per-instance basis. If unspecified, the default
value is `mongodb`.

MongoDB permits setting this option only at startup. The
`setParameter` can not change this setting.

This option is available only in MongoDB Enterprise.

**Important:**

Ensure that your driver supports alternate service names.
For `mongosh` and other MongoDB tools to
connect to the new `serviceName`, see the
`gssapiServiceName` option.

**`security.sasl.saslauthdSocketPath`**

*Type*: string

The path to the UNIX domain socket file for `saslauthd`.
   

#### `security.ldap` Options

```yaml
security:
   ldap:
      servers: <string>
      bind:
         method: <string>
         saslMechanisms: <string>
         queryUser: <string>
         queryPassword: <string | array>
         useOSDefaults: <boolean>
      transportSecurity: <string>
      timeoutMS: <int>
      retryCount: <int>
      userToDNMapping: <string>
      authz:
         queryTemplate: <string>
      validateLDAPServerConfig: <boolean>
```

**`security.ldap.servers`**

*Type*: string

*Available in MongoDB Enterprise only.*

The LDAP server against which the `mongod` or `mongos` authenticates users or
determines what actions a user is authorized to perform on a given
database. If the LDAP server specified has any replicated instances,
you may specify the host and port of each replicated server in a
comma-delimited list.

If your LDAP infrastructure partitions the LDAP directory over multiple LDAP
servers, specify *one* LDAP server or any of its replicated instances to
`security.ldap.servers`. MongoDB supports following LDAP referrals as defined in [RFC 4511 4.1.10](https://www.rfc-editor.org/rfc/rfc4511.txt). Do not use `security.ldap.servers`
for listing every LDAP server in your infrastructure.

You can prefix LDAP servers with `srv:` and `srv_raw:`.

If your connection string specifies `"srv:<DNS_NAME>"`, `mongod`
verifies that `"_ldap._tcp.gc._msdcs.<DNS_NAME>"` exists for SRV to
support Active Directory. If not found, `mongod` verifies that
`"_ldap._tcp.<DNS_NAME>"` exists for SRV. If an SRV record cannot be
found, `mongod` warns you to use `"srv_raw:<DNS_NAME>"` instead.

If your connection string specifies `"srv_raw:<DNS_NAME>"`,
`mongod` performs an SRV record lookup for `"<DNS NAME>"`.

This setting can be configured on a running `mongod` or `mongos` using
`setParameter`.

If unset, `mongod` or `mongos` cannot use LDAP authentication or authorization.

**`security.ldap.bind.queryUser`**

*Type*: string

*Available in MongoDB Enterprise only.*

The identity with which `mongod` or `mongos` binds as, when connecting to or
performing queries on an LDAP server.

Only required if any of the following are true:

- Using LDAP authorization.
- Using an LDAP query for `security.ldap.userToDNMapping`.
- The LDAP server disallows anonymous binds

You must use `queryUser` with
`queryPassword`.

If unset, `mongod` or `mongos` does not
attempt to bind to the LDAP server.

This setting can be configured on a running
`mongod` or `mongos` using
`setParameter`.

**Note:**

Windows MongoDB deployments can use `useOSDefaults`
instead of `queryUser` and `queryPassword`. You cannot specify
both `queryUser` and `useOSDefaults` at the same time.

**`security.ldap.bind.queryPassword`**

*Type*: string or array

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`queryUser`. You must use 
`queryPassword` with
`queryUser`.

If not set, `mongod` or `mongos` does not attempt to
bind to the LDAP server.

You can configure this setting on a running `mongod` or 
`mongos` using `setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `useOSDefaults`
instead of `queryUser` and 
`queryPassword`. You cannot specify both 
`queryPassword` and 
`useOSDefaults` at the same time.

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`--ldapQueryUser`. You must use `--ldapQueryPassword` with
`--ldapQueryUser`.

If not set, `mongod` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongod` using
`setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. 
You cannot specify both `--ldapQueryPassword` and 
`--ldapBindWithOSDefaults` at the same time.

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`--ldapQueryUser`. You must use `--ldapQueryPassword` with
`--ldapQueryUser`.

If not set, `mongoldap` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongoldap` using
`setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. 
You cannot specify both `--ldapQueryPassword` and 
`--ldapBindWithOSDefaults` at the same time.

**`security.ldap.bind.useOSDefaults`**

*Type*: boolean

*Default*: false

Available in MongoDB Enterprise for the Windows platform only.

Allows `mongod` or `mongos` to authenticate, or bind, using your Windows login
credentials when connecting to the LDAP server.

Only required if:

- Using LDAP authorization.
- Using an LDAP query for `username transformation`.
- The LDAP server disallows anonymous binds

Use `useOSDefaults` to replace `queryUser` and
`queryPassword`.

**`security.ldap.bind.method`**

*Type*: string

*Default*: simple

*Available in MongoDB Enterprise only.*

The method `mongod` or `mongos` uses to authenticate to an LDAP server.
Use with `queryUser` and
`queryPassword` to
connect to the LDAP server.

`method` supports the following values:

* `simple` - `mongod` or `mongos` uses simple authentication.

* `sasl` - `mongod` or `mongos` uses SASL protocol for authentication

If you specify `sasl`, you can configure the available SASL mechanisms
using `security.ldap.bind.saslMechanisms`. `mongod` or `mongos` defaults to
using `DIGEST-MD5` mechanism.

**`security.ldap.bind.saslMechanisms`**

*Type*: string

*Default*: DIGEST-MD5

*Available in MongoDB Enterprise only.*

A comma-separated list of SASL mechanisms `mongod` or `mongos` can
use when authenticating to the LDAP server. The `mongod` or `mongos` and the
LDAP server must agree on at least one mechanism. The `mongod` or `mongos`
dynamically loads any SASL mechanism libraries installed on the host
machine at runtime.

Install and configure the appropriate libraries for the selected
SASL mechanism(s) on both the `mongod` or `mongos` host and the remote
LDAP server host. Your operating system may include certain SASL
libraries by default. Defer to the documentation associated with each
SASL mechanism for guidance on installation and configuration.

If using the `GSSAPI` SASL mechanism for use with
security-kerberos, verify the following for the
`mongod` or `mongos` host machine:

`Linux`
  - The `KRB5_CLIENT_KTNAME` environment
    variable resolves to the name of the client keytab-files
    for the host machine. For more on Kerberos environment
    variables, please defer to the
    [Kerberos documentation](https://web.mit.edu/kerberos/krb5-1.13/doc/admin/env_variables.html).
  - The client keytab includes a
    kerberos-user-principal for the `mongod` or `mongos` to use when
    connecting to the LDAP server and execute LDAP queries.

`Windows`
  If connecting to an Active Directory server, the Windows
  Kerberos configuration automatically generates a
  [Ticket-Granting-Ticket](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380510(v=vs.85).aspx)
  when the user logs onto the system. Set `useOSDefaults` to
  `true` to allow `mongod` or `mongos` to use the generated credentials when
  connecting to the Active Directory server and execute queries.

Set `method` to `sasl` to use this option.

**Note:**

For a complete list of SASL mechanisms see the
[IANA listing](http://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml).
Defer to the documentation for your LDAP or Active Directory
service for identifying the SASL mechanisms compatible with the
service.

MongoDB is not a source of SASL mechanism libraries, nor
is the MongoDB documentation a definitive source for
installing or configuring any given SASL mechanism. For
documentation and support, defer to the SASL mechanism
library vendor or owner.

For more information on SASL, defer to the following resources:

- For Linux, please see the [Cyrus SASL documentation](https://www.cyrusimap.org/sasl/).
- For Windows, please see the [Windows SASL documentation](https://msdn.microsoft.com/en-us/library/cc223500.aspx).

**`security.ldap.transportSecurity`**

*Type*: string

*Default*: tls

*Available in MongoDB Enterprise only.*

By default, `mongod` or `mongos` creates a TLS/SSL secured connection to the LDAP
server.

For Linux deployments, you must configure the appropriate TLS Options in
`/etc/openldap/ldap.conf` file. Your operating system's package manager
creates this file as part of the MongoDB Enterprise installation, through the
`libldap` dependency. See the documentation for `TLS Options` in the
[ldap.conf OpenLDAP documentation](http://www.openldap.org/software/man.cgi?query=ldap.conf&manpath=OpenLDAP+2.4-Release)
for more complete instructions.

For Windows deployment, you must add the LDAP server CA certificates to the
Windows certificate management tool. The exact name and functionality of the
tool may vary depending on operating system version. Please see the
documentation for your version of Windows for more information on
certificate management.

Set `transportSecurity` to `none` to disable TLS/SSL between `mongod` or `mongos` and the LDAP
server.

**Warning:**

Setting `transportSecurity` to `none` transmits plaintext information and possibly
credentials between `mongod` or `mongos` and the LDAP server.

**`security.ldap.timeoutMS`**

*Type*: int

*Default*: 10000

*Available in MongoDB Enterprise only.*

The amount of time in milliseconds `mongod` or `mongos` should wait for an LDAP server
to respond to a request.

Increasing the value of `timeoutMS` may prevent connection failure between the
MongoDB server and the LDAP server, if the source of the failure is a
connection timeout. Decreasing the value of `timeoutMS` reduces the time
MongoDB waits for a response from the LDAP server.

This setting can be configured on a running `mongod` or `mongos` using
`setParameter`.

**`security.ldap.retryCount`**

**New in version:** 6.1

*Type*: int

*Default*: 0

*Available in MongoDB Enterprise only.*

Number of operation retries by the server LDAP manager after a
network error.

This setting can be configured on a running `mongod` or
`mongos` using `setParameter`.

**`security.ldap.userToDNMapping`**

*Type*: string

*Available in MongoDB Enterprise only.*

Maps the username provided to `mongod` or `mongos` for authentication to a LDAP
Distinguished Name (DN). You may need to use `userToDNMapping` to transform a
username into an LDAP DN in the following scenarios:

- Performing LDAP authentication with simple LDAP binding, where users
  authenticate to MongoDB with usernames that are not full LDAP DNs.

- Using an `LDAP authorization query template` that requires a DN.

- Transforming the usernames of clients authenticating to Mongo DB using
  different authentication mechanisms (for example, X.509, kerberos) to a full LDAP
  DN for authorization.

`userToDNMapping` expects a quote-enclosed JSON-string representing an ordered array
of documents. Each document contains a regular expression `match` and
either a `substitution` or `ldapQuery` template used for transforming the
incoming username.

Each document in the array has the following form:

```javascript
{
  match: "<regex>"
  substitution: "<LDAP DN>" | ldapQuery: "<LDAP Query>"
}
```

| Field | Description | Example |
|---|---|---|
| `match` | An ECMAScript-formatted regular expression (regex) to match against a provided username. Each parenthesis-enclosed section represents a regex capture group used by `substitution` or `ldapQuery`. | `"(.+)ENGINEERING"` `"(.+)DBA"` |
| `substitution` | An LDAP distinguished name (DN) formatting template that converts the authentication name matched by the `match` regex into a LDAP DN. Each curly bracket-enclosed numeric value is replaced by the corresponding [regex capture group](http://www.regular-expressions.info/refcapture.html) extracted from the authentication username through the `match` regex. The result of the substitution must be an [RFC4514](https://www.ietf.org/rfc/rfc4514.txt) escaped string. | `"cn={0},ou=engineering, dc=example,dc=com"` |
| `ldapQuery` | A LDAP query formatting template that inserts the authentication name matched by the `match` regex into an LDAP query URI encoded respecting RFC4515 and RFC4516. Each curly bracket-enclosed numeric value is replaced by the corresponding [regex capture group](http://www.regular-expressions.info/refcapture.html) extracted from the authentication username through the `match` expression. `mongod` or `mongos` executes the query against the LDAP server to retrieve the LDAP DN for the authenticated user. `mongod` or `mongos` requires exactly one returned result for the transformation to be successful, or `mongod` or `mongos` skips this transformation. | `"ou=engineering,dc=example, dc=com??one?(user={0})"` |

**Note:**

An explanation of  [RFC4514](https://www.ietf.org/rfc/rfc4514.txt),
[RFC4515](https://tools.ietf.org/html/rfc4515),
[RFC4516](https://tools.ietf.org/html/rfc4516), or LDAP queries is out
of scope for the MongoDB Documentation. Please review the RFC directly or
use your preferred LDAP resource.

For each document in the array, you must use either `substitution` or
`ldapQuery`. You *cannot* specify both in the same document.

When performing authentication or authorization, `mongod` or `mongos` steps through
each document in the array in the given order, checking the authentication
username against the `match` filter.  If a match is found,
`mongod` or `mongos` applies the transformation and uses the output for
authenticating the user. `mongod` or `mongos` does not check the remaining documents
in the array.

If the given document does not match the provided authentication
name, `mongod` or `mongos` continues
through the list of documents to find additional matches. If no
matches are found in any document, or the transformation the document
describes fails, `mongod` or `mongos`
returns an error. 

`mongod` or `mongos` also returns an error if one 
of the transformations cannot be evaluated due to networking or
authentication failures to the LDAP server. `mongod` or
`mongos` rejects the connection request and does not
check the remaining documents in the array.

Starting in MongoDB 5.0, `userToDNMapping`
accepts an empty string `""` or empty array `[ ]` in place of a
mapping document. If providing an empty string or empty array to
`userToDNMapping`, MongoDB maps the
authenticated username as the LDAP DN. Previously, providing an
empty mapping document would cause mapping to fail.

**Important:**

You must pass the array to
`userToDNMapping` as a string.

**Example:**

The following shows two transformation documents. The first
document matches against any string ending in `@ENGINEERING`, placing
anything preceding the suffix into a regex capture group. The
second document matches against any string ending in `@DBA`, placing
anything preceding the suffix into a regex capture group.

```text
"[
   {
      match: "(.+)@ENGINEERING.EXAMPLE.COM",
      substitution: "cn={0},ou=engineering,dc=example,dc=com"
   },
   {
      match: "(.+)@DBA.EXAMPLE.COM",
      ldapQuery: "ou=dba,dc=example,dc=com??one?(user={0})"

   }

]"
```

A user with username `alice@ENGINEERING.EXAMPLE.COM` matches the first
document. The regex capture group `{0}` corresponds to the string
`alice`. The resulting output is the DN
`"cn=alice,ou=engineering,dc=example,dc=com"`.

A user with username `bob@DBA.EXAMPLE.COM` matches the second document.
The regex capture group `{0}` corresponds to the string `bob`.  The
resulting output is the LDAP query
`"ou=dba,dc=example,dc=com??one?(user=bob)"`. `mongod` or `mongos` executes this
query against the LDAP server, returning the result
`"cn=bob,ou=dba,dc=example,dc=com"`.

If `userToDNMapping` is unset, `mongod` or `mongos` applies no transformations to the username
when attempting to authenticate or authorize a user against the LDAP server.

This setting can be configured on a running `mongod` or `mongos` using the
`setParameter` database command.

**`security.ldap.authz.queryTemplate`**

*Type*: string

*Available in MongoDB Enterprise only.*

A relative LDAP query URL formatted conforming to [RFC4515](https://tools.ietf.org/html/rfc4515) and [RFC4516](https://tools.ietf.org/html/rfc4516) that `mongod` executes to obtain
the LDAP groups to which the authenticated user belongs to. The query is
relative to the host or hosts specified in `security.ldap.servers`.

**Note:**

For better performance, consider placing the LDAP groups used for
MongoDB authorization into their own Organizational Unit (`OU`).

In the URL, you can use the following substitution tokens:

| Substitution Token | Description |
|---|---|
| `{USER}` | Substitutes the authenticated username, or the `transformed` username if a `userToDNMapping` is specified. |
| `{PROVIDED_USER}` | Substitutes the supplied username, i.e. before either authentication or LDAP transformation. |

When constructing the query URL, ensure that the order of LDAP parameters
respects RFC4516:

```bash
[ dn  [ ? [attributes] [ ? [scope] [ ? [filter] [ ? [Extensions] ] ] ] ] ]
```

If your query includes an attribute, `mongod` assumes that the query
retrieves a list of the DNs which this entity is a member of.

If your query does not include an attribute, `mongod` assumes
the query retrieves all entities which the user is member of.

For each LDAP DN returned by the query, `mongod` assigns the authorized
user a corresponding role on the `admin` database. If a role on the on the
`admin` database exactly matches the DN, `mongod` grants the user the
roles and privileges assigned to that role. See the
`db.createRole()` method for more information on creating roles.

**Example:**

This LDAP query returns any groups listed in the LDAP user object's
`memberOf` attribute.

```bash
"{USER}?memberOf?base"
```

Your LDAP configuration may not include the `memberOf` attribute as part
of the user schema, may possess a different attribute for reporting group
membership, or may not track group membership through attributes.
Configure your query with respect to your own unique LDAP configuration.

If unset, `mongod` cannot authorize users using LDAP.

Although you can modify the value of the `ldapAuthzQueryTemplate` parameter
on a running `mongod` by using the `setParameter` 
database command, you can't enable or disable it during runtime. To enable 
this setting, you must configure `security.ldap.authz.queryTemplate` in 
your configuration file during startup.

**Note:**

An explanation of [RFC4515](https://tools.ietf.org/html/rfc4515),
[RFC4516](https://tools.ietf.org/html/rfc4516) or LDAP queries is out
of scope for the MongoDB Documentation. Please review the RFC directly or
use your preferred LDAP resource.

**`security.ldap.validateLDAPServerConfig`**

*Type*: boolean

*Default*: true

*Available in MongoDB Enterprise*

A flag that determines if the `mongod` or
`mongos` instance checks the availability of the
`LDAP server(s)` as part of its
startup:

- If `true`, the `mongod` or `mongos`
  instance performs the availability check and only continues to
  start up if the LDAP server is available.

- If `false`, the `mongod` or `mongos`
  instance skips the availability check; i.e. the instance starts up
  even if the LDAP server is unavailable.
