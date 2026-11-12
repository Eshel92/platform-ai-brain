<!-- Part 5 of 6 of reference/program/mongod.md (split because the page is big). -->

### TLS Options

**See also:**

/tutorial/configure-ssl for full
documentation of MongoDB's support.

**`--tlsMode <mode>`**

Enables TLS used for all network connections. The
argument to the `--tlsMode` option can be one of the following:

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
configure-client-tls-tutorial .

**`--tlsCertificateKeyFile <filename>`**

Specifies the `.pem` file that contains both the TLS certificate and 
key.

On macOS or Windows, you can use the
`--tlsCertificateSelector` option to specify a 
certificate from the operating system's secure certificate store
instead of a PEM key file. `--tlsCertificateKeyFile` and
`--tlsCertificateSelector` options are mutually exclusive.
You can only specify one.

- On Linux/BSD, you must specify `--tlsCertificateKeyFile`
  when TLS/SSL is enabled.

- On Windows or macOS, you must specify either
  `--tlsCertificateKeyFile` or
  `--tlsCertificateSelector` when TLS/SSL is enabled.

  **Important:**

  For Windows **only**, MongoDB does not support
  encrypted PEM files. The `mongod` fails to start if
  it encounters an encrypted PEM file. To securely store and
  access a certificate for use with TLS on Windows,
  use `--tlsCertificateSelector`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsCertificateKeyFilePassword <value>`**

Specifies the password to decrypt the certificate-key file (i.e.
`--tlsCertificateKeyFile`). Use the
`--tlsCertificateKeyFilePassword` option only if the
certificate-key file is encrypted. In all cases, the
`mongod` redacts the password from all logging and
reporting output.

- On Linux/BSD, if the private key in the PEM file is encrypted and
  you do not specify the `--tlsCertificateKeyFilePassword` option, MongoDB prompts for a
  passphrase. See ssl-certificate-password.

- On macOS, if the private key in the PEM file is
  encrypted, you must explicitly specify the
  `--tlsCertificateKeyFilePassword` option. Alternatively,
  you can use a certificate from the secure system store (see
  `--tlsCertificateSelector`) instead of a PEM file or use an
  unencrypted PEM file.

- On Windows, MongoDB does not support encrypted certificates.
  The `mongod` fails if it encounters an encrypted
  PEM file. Use `--tlsCertificateSelector` instead. 

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--clusterAuthMode <option>`**

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

**`--tlsClusterFile <filename>`**

Specifies the `.pem` file that contains the X.509
certificate-key file for membership authentication for the cluster or replica set.

On macOS or Windows, you can use the
`--tlsClusterCertificateSelector` option to specify a
certificate from the operating system's secure certificate store
instead of a PEM key file. `--tlsClusterFile` and
`--tlsClusterCertificateSelector` options are mutually
exclusive. You can only specify one.

If `--tlsClusterFile` does not specify the `.pem` file for
internal cluster authentication or the alternative
`--tlsClusterCertificateSelector`, the cluster uses the
`.pem` file specified in the `--tlsCertificateKeyFile`
option or the certificate returned by the
`--tlsCertificateSelector`.

If using X.509 authentication, `--tlsCAFile` or `tls.CAFile`
must be specified unless using `--tlsCertificateSelector`.

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**Important:**

For Windows **only**, MongoDB does not support
encrypted PEM files. The `mongod` fails to start if
it encounters an encrypted PEM file. To securely store and
access a certificate for use with membership authentication on
Windows, use `--tlsClusterCertificateSelector`.

**`--tlsCertificateSelector <parameter>=<value>`**

**Note:**

Available on Windows and macOS as an alternative to
`--tlsCertificateKeyFile`.

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store to use for
TLS.

The `--tlsCertificateKeyFile` and
`--tlsCertificateSelector` options are mutually exclusive.
You can only specify one.

`--tlsCertificateSelector` accepts an argument of the format
`<property>=<value>` where the property can be one of the
following:

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
certificate chain to the TLS certificate. Do **not** use
`--tlsCAFile` or `--tlsClusterCAFile` to specify the
root and intermediate CA certificate

For example, if the TLS/SSL certificate was signed with a single root
CA certificate, the secure certificate store must contain that root
CA certificate. If the TLS/SSL certificate was signed with an
intermediate CA certificate, the secure certificate store must
contain the intermedia CA certificate *and* the root CA certificate.

**Note:**

You cannot use the `rotateCertificates` command or the
`db.rotateCertificates()` shell method when using
`net.tls.certificateSelector` or
`--tlsCertificateSelector`
set to `thumbprint`

**`--tlsClusterCertificateSelector <parameter>=<value>`**

**Note:**

Available on Windows and macOS as an alternative to 
`--tlsClusterFile`.      

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store
for internal X.509 membership authentication.

`--tlsClusterFile` and
`--tlsClusterCertificateSelector` options are mutually
exclusive. You can only specify one.

`--tlsClusterCertificateSelector` accepts an argument of the
format `<property>=<value>` where the property can be one of the
following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

The `mongod` searches the operating system's secure
certificate store for the CA certificates required to validate the
full certificate chain of the specified cluster certificate.
Specifically, the secure certificate store must contain the root CA
and any intermediate CA certificates required to build the full
certificate chain to the cluster certificate. Do **not** use
`--tlsCAFile` or `--tlsClusterCAFile` to specify the
root and intermediate CA certificate.

For example, if the cluster certificate was signed with a single root
CA certificate, the secure certificate store must contain that root
CA certificate. If the cluster certificate was signed with an
intermediate CA certificate, the secure certificate store must
contain the intermedia CA certificate *and* the root CA certificate.

`mongod` / `mongos` logs a warning on
connection if the presented X.509 certificate expires within `30`
days of the `mongod/mongos` host system time.

**`--tlsClusterPassword <value>`**

Specifies the password to decrypt the X.509 certificate-key file
specified with `--tlsClusterFile`. Use the
`--tlsClusterPassword` option only if the certificate-key
file is encrypted. In all cases, the `mongod` redacts
the password from all logging and reporting output.

- On Linux/BSD, if the private key in the X.509 file is encrypted and
  you do not specify the `--tlsClusterPassword` option,
  MongoDB prompts for a passphrase. See
  ssl-certificate-password.

- On macOS, if the private key in the X.509 file is
  encrypted, you must explicitly specify the
  `--tlsClusterPassword` option. Alternatively, you can
  either use a certificate from the secure system store (see
  `--tlsClusterCertificateSelector`) instead of a cluster PEM
  file or use an unencrypted PEM file.

- On Windows, MongoDB does not support encrypted certificates.
  The `mongod` fails if it encounters an encrypted
  PEM file. Use `--tlsClusterCertificateSelector` instead.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsCAFile <filename>`**

Specifies the `.pem` file that contains the root certificate
chain from the Certificate Authority. Specify the file name of the
`.pem` file using relative or absolute paths.

**Important:**

When starting a `mongod` instance with 
TLS/SSL enabled, you must 
specify a value for the `--tlsCAFile` flag, the 
`net.tls.CAFile` configuration option, or the `tlsUseSystemCA` 
parameter. 

`--tlsCAFile`, `tls.CAFile`, and `tlsUseSystemCA` are all mutually 
exclusive.

Windows/macOS Only
  If using `--tlsCertificateSelector` and/or
  `--tlsClusterCertificateSelector`, do **not** use
  `--tlsCAFile` to specify the root and intermediate CA
  certificates. Store all CA certificates required to validate the
  full trust chain of the `--tlsCertificateSelector` and/or
  `--tlsClusterCertificateSelector` certificates in the
  secure certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsClusterCAFile <filename>`**

Specifies the `.pem` file that contains the root certificate
chain from the Certificate Authority used to validate the certificate
presented by a client establishing a connection. Specify the file
name of the `.pem` file using relative or absolute paths. 
`--tlsClusterCAFile` requires that 
`--tlsCAFile` is set.

If `--tlsClusterCAFile` does not specify the `.pem`
file for validating the certificate from a client establishing a
connection, the cluster uses the `.pem` file specified in the
`--tlsCAFile` option.

`--tlsClusterCAFile` lets you use separate Certificate
Authorities to verify the client to server and server to client
portions of the TLS handshake.

Windows/macOS Only
  If using `--tlsCertificateSelector` and/or
  `--tlsClusterCertificateSelector`, do **not** use
  `--tlsClusterCAFile` to specify the root and
  intermediate CA certificates. Store all CA certificates required to
  validate the full trust chain of the
  `--tlsCertificateSelector` and/or
  `--tlsClusterCertificateSelector` certificates in the
  secure certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsCRLFile <filename>`**

Specifies the `.pem` file that contains the Certificate Revocation
List. Specify the file name of the `.pem` file using relative or
absolute paths.

**Note:**

- You cannot specify a CRL file on
  macOS. Instead, you can use the system SSL certificate store,
  which uses OCSP (Online Certificate Status Protocol) to
  validate the revocation status of certificates. See
  `--tlsCertificateSelector` to use the
  system SSL certificate store.

- To check for certificate revocation,
  MongoDB `enables` the use of OCSP
  (Online Certificate Status Protocol) by default as an
  alternative to specifying a CRL file or using the system SSL
  certificate store.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsAllowInvalidCertificates`**

Bypasses the validation checks for TLS certificates on other
servers in the cluster and allows the use of invalid certificates to
connect.

**Note:**

If you specify
`--tlsAllowInvalidCertificates` or ``tls.allowInvalidCertificates:
true`` when using X.509 authentication, an invalid certificate is
only sufficient to establish a TLS connection but is
*insufficient* for authentication.

When using
the `--tlsAllowInvalidCertificates` setting, MongoDB
logs a warning regarding the use of the invalid certificate.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsAllowInvalidHostnames`**

Disables the validation of the hostnames in TLS certificates,
when connecting to other members of the replica set or sharded cluster
for inter-process authentication. This allows `mongod` to connect
to other members if the hostnames in their certificates do not match
their configured hostname.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsAllowConnectionsWithoutCertificates`**

By default, the server bypasses client certificate validation unless 
the server is configured to use a CA file. If a CA file is provided, the 
following rules apply: 

- .. include:: /includes/TLS-SSL-certificates.rst

- For clients that present a certificate, `mongod` performs
  certificate validation using the root certificate chain specified by
  `--tlsCAFile`  and reject clients with invalid 
  certificates.

Use the `--tlsAllowConnectionsWithoutCertificates` option if you have 
a mixed deployment that includes clients that do not or cannot present 
certificates to the `mongod`.

For more information about TLS and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**`--tlsDisabledProtocols <protocol(s)>`**

Prevents a MongoDB server running with TLS from accepting
incoming connections that use a specific protocol or protocols. To
specify multiple protocols, use a comma separated list of protocols.

`--tlsDisabledProtocols` recognizes the following protocols: `TLS1_0`, `TLS1_1`,
`TLS1_2`, and `TLS1_3`.

- On macOS, you cannot disable `TLS1_1` and leave both `TLS1_0` and
  `TLS1_2` enabled. You must disable at least one of the other
  two, for example, `TLS1_0,TLS1_1`.

- To list multiple protocols, specify as a comma separated list of
  protocols. For example `TLS1_0,TLS1_1`.

- Specifying an unrecognized protocol prevents the server from
  starting.

- The specified disabled protocols overrides any default disabled
  protocols.

MongoDB disables the use of TLS 1.0 if TLS
1.1+ is available on the system. To enable the disabled TLS 1.0,
specify `none` to `--tlsDisabledProtocols`. 

Members of replica sets and sharded clusters must speak at least one
protocol in common.

**See also:**

ssl-disallow-protocols

**`--tlsFIPSMode`**

Directs the `mongod` to use the FIPS mode of the  TLS
library. Your system must have a FIPS
compliant library to use the `--tlsFIPSMode` option.

**Note:** FIPS-compatible TLS/SSL is

available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced). See
configure-mdb-for-fips for more information.


### Profiler Options

**`--profile <level>`**

*Default*: 0

Configures the database profiler level.
The following profiler levels are available:

`0`
   The profiler is off and does not collect any data.
   This is the default profiler level.

`1`
   The profiler collects data for operations that take longer
   than the value of `slowms` or that match a filter. 

   When a filter is set:

   - The `slowms` and `sampleRate` options are not used for
     profiling.
   - The profiler only captures operations that match the
     filter.

`2`
   The profiler collects data for all operations.
   When set to level `2`, the profiler ignores user 
   provided values for `slowms` and `filter`.

**Warning:**

Profiling can degrade performance and expose unencrypted query data in the
system log. Carefully consider any performance and security implications
before configuring and enabling the profiler on a production deployment.

See database-profiling-overhead for more information on
potential performance degradation.

   

**`--slowms <integer>`**

*Default*: 100

The *slow* operation time threshold, in milliseconds. Operations
that run for longer than this threshold are considered *slow*.

When `logLevel` is set to `0`, MongoDB records *slow*
operations to the diagnostic log at a rate determined by
`slowOpSampleRate`.

At higher `logLevel` settings, all operations appear in
the diagnostic log regardless of their latency with the following
exception: the logging of slow oplog entry messages by the
secondaries. The secondaries log only the slow oplog
entries; increasing the `logLevel` does not log all
oplog entries.

For `mongod` instances, `--slowms` affects the diagnostic log
and, if enabled, the profiler.

**See also:**

/tutorial/manage-the-database-profiler

**`--slowOpSampleRate <double>`**

*Default*: 1.0

The fraction of *slow* operations that should be profiled or logged.
`--slowOpSampleRate` accepts values between 0 and 1, inclusive.

`--slowOpSampleRate` does not affect the slow oplog entry logging 
by the secondary members of a replica set. Secondary
members log all oplog entries that take longer than the slow
operation threshold regardless of the `--slowOpSampleRate`.

For `mongod` instances, `--slowOpSampleRate` affects the
diagnostic log and, if enabled, the profiler.
