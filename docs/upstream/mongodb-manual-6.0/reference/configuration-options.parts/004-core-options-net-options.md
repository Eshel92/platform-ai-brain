<!-- Part 4 of 7 of reference/configuration-options.md (split because the page is big). -->

### `net` Options

**Changed in version:** 5.0

MongoDB removes the `net.serviceExecutor` configuration option and the
corresponding `--serviceExecutor` command-line option.

```yaml
net:
   port: <int>
   bindIp: <string>
   bindIpAll: <boolean>
   maxIncomingConnections: <int>
   wireObjectCheck: <boolean>
   ipv6: <boolean>
   unixDomainSocket:
      enabled: <boolean>
      pathPrefix: <string>
      filePermissions: <int>
   tls:
      certificateSelector: <string>
      clusterCertificateSelector: <string>
      mode: <string>
      certificateKeyFile: <string>
      certificateKeyFilePassword: <string>
      clusterFile: <string>
      clusterPassword: <string>
      CAFile: <string>
      clusterCAFile: <string>
      CRLFile: <string>
      allowConnectionsWithoutCertificates: <boolean>
      allowInvalidCertificates: <boolean>
      allowInvalidHostnames: <boolean>
      disabledProtocols: <string>
      FIPSMode: <boolean>
      logVersions: <string>
   compression:
      compressors: <string>
```

**`net.port`**

*Type*: integer

*Default*:

- 27017 for `mongod` (if not a shard member or a config server
  member) or `mongos` instance

- 27018 if `mongod` is a `shard member`

- 27019 if `mongod` is a `config server member`

The TCP port on which the MongoDB instance listens for
client connections.

**Changed in version:** 6.0.12

The `net.port` option accepts a range of values between `0` and `65535`.
Setting the port to `0` configures `mongos` or `mongod` to use an arbitrary
port assigned by the operating system.

**`net.bindIp`**

*Type*: string

*Default*: localhost

The hostnames and/or IP addresses and/or full Unix domain socket
paths on which `mongos` or `mongod` should
listen for client connections. You may attach `mongos`
or `mongod` to any interface. To bind to multiple
addresses, enter a list of comma-separated values.

**Example:**

`localhost,/tmp/mongod.sock`

You can specify both IPv4 and IPv6 addresses, or hostnames that
resolve to an IPv4 or IPv6 address.

**Example:**

`localhost, 2001:0DB8:e132:ba26:0d5c:2774:e7f9:d513`

**Note:**

If specifying an IPv6 address *or* a hostname that resolves to an
IPv6 address to `net.bindIp`, you must start
`mongos` or `mongod` with
`net.ipv6 : true` to enable IPv6 support.
Specifying an IPv6 address to `net.bindIp` does not
enable IPv6 support.

If specifying a 
[link-local IPv6 address](https://en.wikipedia.org/wiki/Link-local_address#IPv6)
(`fe80::/10`), you must append the 
[zone index](https://en.wikipedia.org/wiki/IPv6_address#Scoped_literal_IPv6_addresses_(with_zone_index))
to that address (i.e. `fe80::<address>%<adapter-name>`). 

**Example:**

`localhost,fe80::a00:27ff:fee0:1fcf%enp0s3`

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information about IP Binding, refer to the
/core/security-mongodb-configuration documentation.

To bind to all IPv4 addresses, enter `0.0.0.0`.

To bind to all IPv4 and IPv6 addresses, enter `::,0.0.0.0` or
an asterisk `"*"` (enclose the asterisk in quotes to distinguish from 
[YAML alias nodes](https://yaml.org/spec/1.2/spec.html#alias/)). 
Alternatively, use the `net.bindIpAll` setting.

**Note:**

- `net.bindIp` and `net.bindIpAll` are mutually
  exclusive. That is, you can specify one or the other, but not
  both.

- The command-line option `--bind_ip` overrides the configuration
  file setting `net.bindIp`.

To configure cluster nodes for [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS), use host names
instead of IP addresses. 

Starting in MongoDB v5.0, `replSetInitiate` and 
`replSetReconfig` reject configurations that use IP
addresses instead of hostnames.

Use `disableSplitHorizonIPCheck` to modify nodes that
cannot be updated to use host names. The parameter only applies to the
configuration commands. 

`mongod` and `mongos` do not rely on
`disableSplitHorizonIPCheck` for validation at startup.
Legacy `mongod` and `mongos` instances that use IP
addresses instead of host names can start after an upgrade. 

Instances that are configured with IP addresses log a warning to use
host names instead of IP addresses. 

**`net.bindIpAll`**

*Type*: boolean

*Default*: false

If true, the `mongos` or `mongod` instance binds to all IPv4
addresses (i.e. `0.0.0.0`). If `mongos` or `mongod` starts with
`net.ipv6 : true`, `net.bindIpAll` also binds to all IPv6 addresses
(i.e. `::`). 

`mongos` or `mongod` only supports IPv6 if started with `net.ipv6 : true`. Specifying
`net.bindIpAll` alone does not enable IPv6 support.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information about IP Binding, refer to the
/core/security-mongodb-configuration documentation.

Alternatively, set `net.bindIp` to `::,0.0.0.0` or to an asterisk 
`"*"` (enclose the asterisk in quotes to distinguish from [YAML alias nodes](https://yaml.org/spec/1.2/spec.html#alias/)) to bind to all IP
addresses.

**Note:**

`net.bindIp` and `net.bindIpAll` are mutually
exclusive. Specifying both options causes `mongos` or `mongod` to throw
an error and terminate.

**`net.maxIncomingConnections`**

*Type*: integer

| *Default (Windows):* 1,000,000
| *Default (Linux):* ([RLIMIT_NOFILE](https://man7.org/linux/man-pages/man2/getrlimit.2.html)) * 0.8

The maximum number of simultaneous connections that `mongos` or `mongod`
accepts. This setting has no effect if it is higher than your operating
system's configured maximum connection tracking threshold.

Do not assign too low of a value to this option, or you may 
encounter errors during normal application operation.

This is particularly useful for a `mongos` if you have a client
that creates multiple connections and allows them to timeout rather
than closing them.

In this case, set `maxIncomingConnections` to a value slightly
higher than the maximum number of connections that the client creates, or the
maximum size of the connection pool.

This setting prevents the `mongos` from causing connection spikes on
the individual shards. Spikes like these may disrupt the
operation and memory allocation of the sharded cluster.

**`net.wireObjectCheck`**

*Type*: boolean

*Default*: true

When `true`, the `mongod` or `mongos` instance  validates
all requests from clients upon receipt to prevent clients from inserting
malformed or invalid BSON into a MongoDB database.

For objects with a high degree of sub-document nesting, `net.wireObjectCheck` can
have a small impact on performance.

**`net.ipv6`**

*Type*: boolean

*Default*: false

Set `net.ipv6` to `true` to enable IPv6 support. `mongos`/`mongod` disables IPv6 support by default.

Setting `net.ipv6` does *not* direct the `mongos`/`mongod` to listen on any
local IPv6 addresses or interfaces. To configure the `mongos`/`mongod` to
listen on an IPv6 interface, you must either:

- Configure `net.bindIp` with one or more IPv6 addresses or
  hostnames that resolve to IPv6 addresses, **or**
- Set `net.bindIpAll` to `true`.

#### `net.unixDomainSocket` Options

```yaml
net:
   unixDomainSocket:
      enabled: <boolean>
      pathPrefix: <string>
      filePermissions: <int>
```

**`net.unixDomainSocket.enabled`**

*Type*: boolean

*Default*: true

Enable or disable listening on the UNIX domain socket. `net.unixDomainSocket.enabled` applies only
to Unix-based systems.

When `net.unixDomainSocket.enabled` is `true`, `mongos` or `mongod` listens on the UNIX socket.

The `mongos` or `mongod` process always listens on the UNIX socket unless
one of the following is true:

- `net.unixDomainSocket.enabled` is `false`

- `--nounixsocket` is set. The command
  line option takes precedence over the configuration file setting.

- `net.bindIp` is not set

- `net.bindIp` does not specify `localhost` or its associated IP address

`mongos` or `mongod` installed from official install-mdb-community-debian 
and install-mdb-community-redhat-centos packages
have the `bind_ip` configuration set to `127.0.0.1` by
default.

**`net.unixDomainSocket.pathPrefix`**

*Type*: string

*Default*: /tmp

The path for the UNIX socket. `net.unixDomainSocket.pathPrefix` applies only
to Unix-based systems.

If this option has no value, the
`mongos` or `mongod` process creates a socket with `/tmp` as a prefix. MongoDB
creates and listens on a UNIX socket unless one of the following is true:

- `net.unixDomainSocket.enabled` is `false`

- `--nounixsocket` is set

- `net.bindIp` is not set

- `net.bindIp` does not specify `localhost` or its associated IP address

**`net.unixDomainSocket.filePermissions`**

*Type*: int

*Default*: `0700`

Sets the permission for the UNIX domain socket file.

`net.unixDomainSocket.filePermissions` applies only to Unix-based systems.

#### `net.tls` Options

**Note:**

The `tls` options provide identical functionality as the
previous `ssl` options.

```yaml
net:
   tls:
      mode: <string>
      certificateKeyFile: <string>
      certificateKeyFilePassword: <string>
      certificateSelector: <string>
      clusterCertificateSelector: <string>
      clusterFile: <string>
      clusterPassword: <string>
      CAFile: <string>
      clusterCAFile: <string>
      CRLFile: <string>
      allowConnectionsWithoutCertificates: <boolean>
      allowInvalidCertificates: <boolean>
      allowInvalidHostnames: <boolean>
      disabledProtocols: <string>
      FIPSMode: <boolean>
      logVersions: <string>
```

**`net.tls.mode`**

*Type*: string

Enables TLS used for all network connections. The
argument to the `net.tls.mode` setting can be one of the following:

| Value | Description |
|---|---|
| `disabled` | The server does not use TLS. |
| `allowTLS` | Connections between servers do not use TLS. For incoming connections, the server accepts both TLS and non-TLS. |
| `preferTLS` | Connections between servers use TLS. For incoming connections, the server accepts both TLS and non-TLS. |
| `requireTLS` | The server uses and accepts only TLS encrypted connections. |

If `--tlsCAFile` or `tls.CAFile` is not
specified and you are not using X.509 authentication, you must set the 
`tlsUseSystemCA` parameter to `true`. This makes MongoDB use 
the system-wide CA certificate store when connecting to a TLS-enabled server.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.certificateKeyFile`**

*Type*: string

The `.pem` file that contains both the TLS certificate
and key.

On macOS or Windows, you can use the `net.tls.certificateSelector` 
setting to specify a certificate from the operating system's secure 
certificate store instead of a PEM key file. 
`certificateKeyFile` and
`net.tls.certificateSelector` are mutually exclusive.
You can only specify one.

- On Linux/BSD, you must specify
  `net.tls.certificateKeyFile` when TLS is enabled.

- On Windows or macOS, you must specify either
  `net.tls.certificateKeyFile` or
  `net.tls.certificateSelector` when TLS is enabled.

  **Important:**

  For Windows **only**, MongoDB does not support
  encrypted PEM files. The `mongod` fails to start if
  it encounters an encrypted PEM file. To securely store and
  access a certificate for use with TLS on Windows,
  use `net.tls.certificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.certificateKeyFilePassword`**

*Type*: string

The password to de-crypt the certificate-key file (i.e.
`certificateKeyFile`). Use the
`net.tls.certificateKeyFilePassword` option only if the
certificate-key file is encrypted. In all cases, the
`mongos` or `mongod` redacts the
password from all logging and reporting output.

On Linux/BSD, if the private key in the PEM file is encrypted and
you do not specify the `net.tls.certificateKeyFilePassword` 
option, MongoDB prompts for a passphrase. 

For more information, see ssl-certificate-password.

On macOS, if the private key in the PEM file is encrypted, you must
explicitly specify the `net.tls.certificateKeyFilePassword` option.
Alternatively, you can use a certificate from the secure system
store (see `net.tls.certificateSelector`) instead of a PEM
key file or use an unencrypted PEM file.

On Windows, MongoDB does not support encrypted certificates. 
The `mongod` fails if it encounters an encrypted
PEM file. Use `net.tls.certificateSelector` instead.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.certificateSelector`**

*Type*: string

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store to use
for TLS/SSL. Available on Windows and macOS as an alternative to
`net.tls.certificateKeyFile`.

`net.tls.certificateKeyFile` and
`net.tls.certificateSelector` options are mutually
exclusive. You can only specify one.

`net.tls.certificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

When using the system SSL certificate store, OCSP (Online
Certificate Status Protocol) is used to validate the revocation
status of certificates.

The `mongod` searches the operating system's secure
certificate store for the CA certificates required to validate the
full certificate chain of the specified TLS certificate.
Specifically, the secure certificate store must contain the root CA
and any intermediate CA certificates required to build the full
certificate chain to the TLS certificate. 

**Warning:**

If you use `net.tls.certificateSelector` and/or 
`net.tls.clusterCertificateSelector`, we **do not** recommend 
using `net.tls.CAFile` or `net.tls.clusterFile` to
specify the root and intermediate CA certificate

For example, if the TLS certificate was signed with a single root
CA certificate, the secure certificate store must contain that root
CA certificate. If the TLS certificate was signed with an
intermediate CA certificate, the secure certificate store must
contain the intermedia CA certificate *and* the root CA certificate.

**Note:**

You cannot use the `rotateCertificates` command or the
`db.rotateCertificates()` shell method when using
`net.tls.certificateSelector` or
`--tlsCertificateSelector`
set to `thumbprint`

**`net.tls.clusterCertificateSelector`**

*Type*: string

Specifies a certificate property to select a matching certificate
from the operating system's secure certificate store to use for
internal X.509 membership authentication. 

Available on Windows and macOS as an alternative to
`net.tls.clusterFile`.

`net.tls.clusterFile` and
`net.tls.clusterCertificateSelector` options are mutually
exclusive. You can only specify one.

`net.tls.clusterCertificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

The `mongod` searches the operating system's secure
certificate store for the CA certificates required to validate the
full certificate chain of the specified cluster certificate.
Specifically, the secure certificate store must contain the root CA
and any intermediate CA certificates required to build the full
certificate chain to the cluster certificate. 

**Warning:**

If you use `net.tls.certificateSelector` and/or 
`net.tls.clusterCertificateSelector`, we **do not** recommend using 
`net.tls.CAFile` or `net.tls.clusterCAFile` to specify 
the root and intermediate CA certificate.

For example, if the cluster certificate was signed with a single root
CA certificate, the secure certificate store must contain that root
CA certificate. If the cluster certificate was signed with an
intermediate CA certificate, the secure certificate store must
contain the intermediate CA certificate *and* the root CA
certificate.

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

**`net.tls.clusterFile`**

*Type*: string

The `.pem` file that contains the X.509 certificate-key file
for membership authentication for the 
cluster or replica set.

On macOS or Windows, you can use the
`net.tls.clusterCertificateSelector` option to specify a
certificate from the operating system's secure certificate store
instead of a PEM key file. `net.tls.clusterFile` and
`net.tls.clusterCertificateSelector` options are mutually
exclusive. You can only specify one.   

If `net.tls.clusterFile` does not specify the `.pem` file
for internal cluster authentication or the alternative
`net.tls.clusterCertificateSelector`, the cluster uses the
`.pem` file specified in the `certificateKeyFile`
setting or the certificate returned by the
`net.tls.certificateSelector`.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**Important:**

For Windows **only**, MongoDB does not support encrypted PEM files. 
The `mongod` fails to start if it encounters an encrypted 
PEM file. To securely store and access a certificate for use with 
membership authentication on Windows, use 
`net.tls.clusterCertificateSelector`.

**`net.tls.clusterPassword`**

*Type*: string

The password to de-crypt the X.509 certificate-key file specified
with `--sslClusterFile`. Use the `net.tls.clusterPassword` option 
only if the certificate-key file is encrypted. In all cases,
`mongos` or `mongod` redacts the
password from all logging and reporting output.

On Linux/BSD, if the private key in the X.509 file is encrypted and
you do not specify the `net.tls.clusterPassword` option,
MongoDB prompts for a passphrase. 

For more information, see ssl-certificate-password.

On macOS, if the private key in the X.509 file is encrypted, you
must explicitly specify the `net.tls.clusterPassword`
option. Alternatively, you can either use a certificate from the
secure system store (see `net.tls.clusterCertificateSelector`) 
instead of a cluster PEM file or use an unencrypted PEM file.

On Windows, MongoDB does not support encrypted certificates. The 
`mongod` fails if it encounters an encrypted PEM file.
Use `net.tls.clusterCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.CAFile`**

*Type*: string

The `.pem` file that contains the root certificate chain
from the Certificate Authority. Specify the file name of the
`.pem` file using relative or absolute paths.

Windows/macOS Only
  If using `net.tls.certificateSelector` and/or
  `net.tls.clusterCertificateSelector`, do **not** use
  `net.tls.CAFile` to specify the root and intermediate CA
  certificates. Store all CA certificates required to validate the
  full trust chain of the `net.tls.certificateSelector`
  and/or `net.tls.clusterCertificateSelector` certificates
  in the secure certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.clusterCAFile`**

*Type*: string

The `.pem` file that contains the root certificate chain
from the Certificate Authority used to validate the certificate
presented by a client establishing a connection. Specify the file
name of the `.pem` file using relative or absolute paths.
`net.tls.clusterCAFile` requires that
`net.tls.CAFile` is set.

If `net.tls.clusterCAFile` does not specify the `.pem`
file for validating the certificate from a client establishing a
connection, the cluster uses the `.pem` file specified in the
`net.tls.CAFile` option.

`net.tls.clusterCAFile` lets you use separate Certificate
Authorities to verify the client to server and server to client
portions of the TLS handshake.

Starting in 4.0, on macOS or Windows, you can use a certificate from
the operating system's secure store instead of a PEM key file. See
`net.tls.clusterCertificateSelector`. When using the secure
store, you do not need to, but can, also specify the
`net.tls.clusterCAFile`.

Windows/macOS Only
  If using `net.tls.certificateSelector` and/or
  `net.tls.clusterCertificateSelector`, do **not** use
  `net.tls.clusterCAFile` to specify the root and
  intermediate CA certificates. Store all CA certificates required to
  validate the full trust chain of the
  `net.tls.certificateSelector` and/or
  `net.tls.clusterCertificateSelector` certificates in the
  secure certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.CRLFile`**

*Type*: string

The `.pem` file that contains the Certificate Revocation
List. Specify the file name of the `.pem` file using relative or
absolute paths.

**Note:**

- You cannot specify `net.tls.CRLFile` on macOS. Instead, you can 
  use the system SSL certificate store, which uses OCSP (Online
  Certificate Status Protocol) to validate the revocation status
  of certificates. See `net.tls.certificateSelector` to use the 
  system SSL certificate store.

- To check for certificate revocation, MongoDB 
  `enables` the use of OCSP
  (Online Certificate Status Protocol) by default as an alternative
  to specifying a CRL file or using the system SSL certificate
  store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.allowConnectionsWithoutCertificates`**

*Type*: boolean

*Default*: false

If `false`, all clients must provide client TLS certificates. If `true`, 
clients don't need to provide client certificates, but `mongod` 
or `mongos` encrypts the TLS/SSL connection.

If a client provides a client certificate, regardless of what value you set 
for `net.tls.allowConnectionsWithoutCertificates`, `mongos` or 
`mongod` performs certificate validation using the root 
certificate chain specified by `CAFile`, or the system 
CA store if `tlsUseSystemCA` is `true`,  and rejects 
clients with invalid certificates.

Use the `net.tls.allowConnectionsWithoutCertificates` option if you 
have a mixed deployment that includes clients that do not or cannot present 
certificates to the `mongos` or `mongod`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`net.tls.allowInvalidCertificates`**

*Type*: boolean

*Default*: false

Enable or disable the validation checks for TLS certificates on other
servers in the cluster and allows the use of invalid certificates to
connect.

**Note:**

If you specify
`--tlsAllowInvalidCertificates` or ``tls.allowInvalidCertificates:
true`` when using X.509 authentication, an invalid certificate is
only sufficient to establish a TLS connection but is
*insufficient* for authentication.

When using the `net.tls.allowInvalidCertificates` setting, MongoDB
logs a warning regarding the use of the invalid certificate.

For more information about TLS and MongoDB, see 
configure-mongod-mongos-for-tls-ssl and inter-process-auth.

**`net.tls.allowInvalidHostnames`**

*Type*: boolean

*Default*: false

When `net.tls.allowInvalidHostnames` is `true`, MongoDB disables 
the validation of the hostnames in TLS certificates. This allows 
`mongod` or `mongos` to connect to other MongoDB 
instances in the cluster, even if the hostname of their certificates does not 
match the specified hostname.

For more information about TLS and MongoDB, see 
configure-mongod-mongos-for-tls-ssl.

**`net.tls.disabledProtocols`**

*Type*: string

Prevents a MongoDB server running with TLS from accepting
incoming connections that use a specific protocol or protocols. To
specify multiple protocols, use a comma separated list of protocols,
but do not use spaces after the commas. If you include a space before
a protocol name, the server interprets it as an unrecognized protocol
and doesn't start.

`net.tls.disabledProtocols` recognizes the following protocols: `TLS1_0`, `TLS1_1`,
`TLS1_2`, and `TLS1_3`.

- On macOS, you cannot disable `TLS1_1` and leave both `TLS1_0` and
  `TLS1_2` enabled. You must disable at least one of the other
  two, for example, `TLS1_0,TLS1_1`.

- To list multiple protocols, specify as a comma separated list of
  protocols without spaces after the commas. For example `TLS1_0,TLS1_1`.

- Specifying an unrecognized protocol or including a space after a
  comma prevents the server from starting.

- The specified disabled protocols overrides any default disabled
  protocols.

MongoDB disables the use of TLS 1.0 if TLS 1.1+ is available on the
system. To enable TLS 1.0, specify `none` to `net.tls.disabledProtocols`. 

Members of replica sets and sharded clusters must speak at least one
protocol in common.

**See also:**

ssl-disallow-protocols

**`net.tls.FIPSMode`**

*Type*: boolean

*Default*: false

Enable or disable the use of the FIPS mode of the  TLS
library for the `mongos` or `mongod`. Your system must have a FIPS
compliant library to use the `net.tls.FIPSMode` option.

**Note:** FIPS-compatible TLS/SSL is

available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server). See
configure-mdb-for-fips for more information.

**`net.tls.logVersions`**

*Type*: string

Instructs `mongos` or `mongod` to log a
message when a client connects using a specified TLS version.

Specify either a single TLS version or a comma-separated list of
multiple TLS versions.

**Example:**

To instruct `mongos` or `mongod` to
log a message when a client connects using either TLS 1.2 or
TLS 1.3, set `net.tls.logVersions` to
`"TLS1_2,TLS1_3"`.

#### `net.compression` Option

```yaml
net:
   compression:
      compressors: <string>
```

**`net.compression.compressors`**

*Default*: snappy,zstd,zlib

Specifies the default compressor(s) to use for
communication between this `mongod` or `mongos` instance and:

- other members of the deployment if the instance is part of a replica set or a sharded cluster

- `mongosh`

- drivers that support the `OP_COMPRESSED` message format.

MongoDB supports the following compressors:

- snappy

- zlib 

- zstd 

To disable network compression, set the value to `disabled`.

**Important:**

Messages are compressed when both parties enable network
compression. Otherwise, messages between the parties are
uncompressed.

If you specify multiple compressors, then the order in which you list
the compressors matter as well as the communication initiator. For
example, if `mongosh` specifies the following network
compressors `zlib,snappy` and the `mongod` specifies
`snappy,zlib`, messages between `mongosh` and
`mongod` uses `zlib`.

If the parties do not share at least one common compressor, messages
between the parties are uncompressed. For example, if
`mongosh` specifies the network compressor
`zlib` and `mongod` specifies `snappy`, messages
between `mongosh` and `mongod` are not
compressed.
