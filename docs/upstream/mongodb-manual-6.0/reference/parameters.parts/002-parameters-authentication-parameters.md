<!-- Part 2 of 8 of reference/parameters.md (split because the page is big). -->

### Authentication Parameters

**`authenticationMechanisms`**

Available for both `mongod` and `mongos`.

Specifies the list of authentication mechanisms the server accepts. Set
this to one or more of the following values. If you specify multiple
values, use a comma-separated list and no spaces. For descriptions
of the authentication mechanisms, see /core/authentication.

| Value | Description |
|---|---|
| SCRAM-SHA-1 | [RFC 5802](https://tools.ietf.org/html/rfc5802) standard Salted Challenge Response Authentication Mechanism using the SHA-1 hash function. |
| SCRAM-SHA-256 | [RFC 7677](https://tools.ietf.org/html/rfc7677) standard Salted Challenge Response Authentication Mechanism using the SHA-256 hash function. |
| MONGODB-X509 | MongoDB TLS/SSL certificate authentication. |
| GSSAPI (Kerberos) | External authentication using Kerberos. This mechanism is available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server). |
| PLAIN (LDAP SASL) | External authentication using LDAP. You can also use `PLAIN` for authenticating in-database users. `PLAIN` transmits passwords in plain text. This mechanism is available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server). |

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to specify both `PLAIN` and `SCRAM-SHA-256` as the
authentication mechanisms, use the following command:

```bash
mongod --setParameter authenticationMechanisms=PLAIN,SCRAM-SHA-256 --auth
```

**`awsSTSRetryCount`**

**Changed in version:** 6.0.7 (Also starting in 5.0.18)

In previous versions, AWS IAM authentication retried only when the 
server returned an HTTP 500 error.

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 2

For MongoDB deployments using [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) or [AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).

Maximum number of AWS IAM authentication retries after a connection 
failure.

The following example sets `awsSTSRetryCount` to `15` 
retries:

```bash
mongod --setParameter awsSTSRetryCount=15
```

Alternatively, the following examples uses the 
`setParameter` command within `mongosh`:

```javascript
db.adminCommand( { setParameter: 1, awsSTSRetryCount: 15 } )
```

**`clusterAuthMode`**

Available for both `mongod` and `mongos`.

Set the `clusterAuthMode` to either `sendX509` or
`x509`. Useful during rolling upgrade to use x509 for
membership authentication
to minimize downtime.

For more information about TLS/SSL and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

```bash
db.adminCommand( { setParameter: 1, clusterAuthMode: "sendX509" } )
```

**`enableLocalhostAuthBypass`**

Available for both `mongod` and `mongos`.

Specify `0` or `false` to disable localhost authentication
bypass. Enabled by default.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

See localhost-exception for more information.

**`KeysRotationIntervalSec`**

*Default*: 7776000 seconds (90 days)

Specifies the number of seconds for which an [HMAC signing key](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
is valid before rotating to the next one. This parameter is intended
primarily to facilitate authentication testing.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`ldapForceMultiThreadMode`**

*Default*: false

Enables the performance of concurrent LDAP operations. 

**Note:**

Only if you are certain that your instance of `libldap`
is safe to use in this mode, enable this flag. You may experience 
crashes of the MongoDB process if the `libldap` version you are using 
is not thread safe.

You must use `ldapForceMultiThreadMode` to use LDAP connection 
pool. To enable LDAP connection pool, set `ldapForceMultiThreadMode` 
and `ldapUseConnectionPool` to `true`.

**Tip:**

If you have any concerns regarding your MongoDB version, OS version or 
libldap version, please contact MongoDB Support.

**`ldapQueryPassword`**

Available for both `mongod` and `mongos`.

*Type*: string

The password used to bind to an LDAP server. You must use 
`ldapQueryUser` with this parameter.

If not set, mongod or mongos does not attempt to bind to the LDAP server.

**`ldapQueryUser`**

Available for both `mongod` and `mongos`.

*Type*: string

The user that binds to an LDAP server. You must use 
`ldapQueryPassword` with this parameter.

If not set, mongod or mongos does not attempt to bind to the LDAP server.

**`ldapRetryCount`**

**New in version:** 6.1

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 0

For MongoDB deployments using security-ldap-external.

Number of operation retries by the server LDAP manager after a
network error.

For example, the following sets `ldapRetryCount` to `3`
seconds:

```bash
mongod --ldapRetryCount=3
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, ldapRetryCount: 3 } )
```

**`ldapUserCacheInvalidationInterval`**

**Changed in version:** 5.2

Available for `mongod` only.

*Default*: 30 seconds

**Note:**

Starting in MongoDB 5.2, the update interval for cached user information
retrieved from an LDAP server depends on
`ldapShouldRefreshUserCacheEntries`:

- If true, use `ldapUserCacheRefreshInterval`.

- If false, use `ldapUserCacheInvalidationInterval`.

For use with MongoDB deployments using
security-ldap-external. Available for `mongod`
instances only.

The interval (in seconds) that the `mongod` instance
waits between external user cache flushes. After MongoDB flushes the
external user cache, MongoDB
reacquires authorization data from the LDAP server the
next time an LDAP-authorized user issues an operation.

Increasing the value specified increases the amount of time
MongoDB and the LDAP server can be out of sync, but reduces the load on
the LDAP server. Conversely, decreasing the value specified
decreases the time MongoDB and the LDAP server can be out of sync while
increasing the load on the LDAP server.

**`ldapUserCacheRefreshInterval`**

**New in version:** 5.2

Available for `mongod` only.

*Type*: integer

*Default*: 30 seconds

**Note:**

Starting in MongoDB 5.2, the update interval for cached user information
retrieved from an LDAP server depends on
`ldapShouldRefreshUserCacheEntries`:

- If true, use `ldapUserCacheRefreshInterval`.

- If false, use `ldapUserCacheInvalidationInterval`.

For MongoDB deployments using security-ldap-external.

The interval in seconds that `mongod` waits before
refreshing the cached user information from the LDAP server.

The maximum interval is 86,400 seconds (24 hours).

For example, the following sets
`ldapUserCacheRefreshInterval` to `4000` seconds:

```bash
mongod --setParameter ldapUserCacheRefreshInterval=4000
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, ldapUserCacheRefreshInterval: 4000 } )
```

 

**`ldapUserCacheStalenessInterval`**

**New in version:** 5.2

Available for `mongod` only.

*Type*: integer

*Default*: 90 seconds

For MongoDB deployments using security-ldap-external.

The interval in seconds that `mongod` retains the cached
LDAP user information after the last cache refresh.

If more than `ldapUserCacheStalenessInterval` seconds
elapse without a successful refresh of the user information from the
LDAP server, then `mongod`:

- Invalidates the cached LDAP user information.
- Is unable to authenticate new sessions for LDAP users until
  `mongod` connects to the LDAP server and
  authorizes the LDAP user.
- Authorizes any existing sessions that use previously authenticated
  LDAP users if `mongod` is unable to connect to the
  LDAP server. When `mongod` reconnects to the LDAP
  server, `mongod` ensures the LDAP users are correctly
  authorized.

The maximum interval is 86,400 seconds (24 hours).

For example, the following sets
`ldapUserCacheStalenessInterval` to `4000` seconds:

```bash
mongod --setParameter ldapUserCacheStalenessInterval=4000
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, ldapUserCacheStalenessInterval: 4000 } )
```

**`ldapUseConnectionPool`**

Specifies whether MongoDB should use connection pooling when
connecting to the LDAP server for authentication/authorization.

MongoDB uses the following default values:

- true on Windows.

- true on Linux where MongoDB Enterprise binaries are linked against
  `libldap_r`.

- false on Linux where MongoDB Enterprise binaries are linked against
  `libldap`.

You can only set `ldapUseConnectionPool` during
start-up, and cannot change this setting with the
`setParameter` database command.

**`ldapConnectionPoolUseLatencyForHostPriority`**

*Default*: true

A boolean that determines whether the LDAP connection pool (see
`ldapUseConnectionPool`) should use latency of the LDAP
servers to determine the connection order (from lowest latency to
highest).

You can only set
`ldapConnectionPoolUseLatencyForHostPriority` during
start-up, and cannot change this setting during runtime with the
`setParameter` database command.

**`ldapConnectionPoolMinimumConnectionsPerHost`**

*Default*: 1

The minimum number of connections to keep open to each LDAP server.

You can only set
`ldapConnectionPoolMinimumConnectionsPerHost` during
start-up, and cannot change this setting during runtime with the
`setParameter` database command.

**`ldapConnectionPoolMaximumConnectionsPerHost`**

*Changed starting in MongoDB versions 5.0.9 and 6.0.0*
Changed default value to `2147483647`. In previous versions, the
default is unset.

*Default*: 2147483647

The maximum number of connections to keep open to each LDAP server.

You can only set
`ldapConnectionPoolMaximumConnectionsPerHost` during
start-up, and cannot change this setting during runtime with the
`setParameter` database command.

**`ldapConnectionPoolMaximumConnectionsInProgressPerHost`**

*Changed starting in MongoDB versions 5.0.9 and 6.0.0*
Changed default value to `2`. In previous versions, the
default is unset.

*Default*: 2

The maximum number of in-progress connect operations to each LDAP server.

You can only set
`ldapConnectionPoolMaximumConnectionsInProgressPerHost`
during start-up, and cannot change this setting with the
`setParameter` database command.

**`ldapConnectionPoolHostRefreshIntervalMillis`**

*Default*: 60000

The number of milliseconds in-between health checks of the pooled
LDAP connections.

You can only set
`ldapConnectionPoolHostRefreshIntervalMillis` during
start-up, and cannot change this setting with the
`setParameter` database command.

**`ldapConnectionPoolIdleHostTimeoutSecs`**

*Default*: 300

The maximum number of seconds that the pooled connections to an LDAP
server can remain idle before being closed.

You can only set
`ldapConnectionPoolIdleHostTimeoutSecs` during
start-up, and cannot change this setting with the
`setParameter` database command.

**`ldapShouldRefreshUserCacheEntries`**

**New in version:** 5.2

Available for `mongod` only.

*Type*: boolean

*Default*: true

For MongoDB deployments using security-ldap-external.

Starting in MongoDB 5.2, the update interval for cached user information
retrieved from an LDAP server depends on
`ldapShouldRefreshUserCacheEntries`:

- If true, use `ldapUserCacheRefreshInterval`.

- If false, use `ldapUserCacheInvalidationInterval`.

You can only set `ldapShouldRefreshUserCacheEntries`
during startup in the `configuration file` or
with the `--setParameter` option on the command line. For example,
the following disables
`ldapShouldRefreshUserCacheEntries`:

```bash
mongod --setParameter ldapShouldRefreshUserCacheEntries=false
```

**`maxValidateMemoryUsageMB`**

**New in version:** 5.0

*Default*: 200

The maximum memory usage limit in megabytes for the
`validate` command. If the limit is exceeded,
`validate` returns as many results as possible and warns
that not all corruption might be reported because of the limit.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`ocspEnabled`**

Available on Linux and macOS.

*Default*: true

The flag that enables or disables OCSP.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following disables OCSP:

```bash
mongod --setParameter ocspEnabled=false ...
```

Starting in MongoDB 6.0, if `ocspEnabled` is set to `true` during 
initial sync, all nodes must be able to reach the OCSP 
responder.

If a member fails in the `STARTUP2` state, set 
`tlsOCSPVerifyTimeoutSecs` to a value that is less than `5`. 

**See also:**

- `ocspValidationRefreshPeriodSecs`
- `tlsOCSPStaplingTimeoutSecs`
- `tlsOCSPVerifyTimeoutSecs`

**`ocspValidationRefreshPeriodSecs`**

Available on Linux.

The number of seconds to wait before refreshing the stapled OCSP
status response. Specify a number greater than or equal to 1.

You can only set `ocspValidationRefreshPeriodSecs` during
startup in the `configuration file` or with
the `--setParameter` option on the command line. For example, the
following sets the parameter to 3600 seconds:

```bash
mongod --setParameter ocspValidationRefreshPeriodSecs=3600 ...
```

Starting in MongoDB 5.0, the `rotateCertificates` command
and `db.rotateCertificates()` method will also refresh any
stapled OCSP responses.

**See also:**

- `ocspEnabled`
- `tlsOCSPStaplingTimeoutSecs`
- `tlsOCSPVerifyTimeoutSecs`

**`opensslCipherConfig`**

*Available on Linux only*

With the use of native TLS/SSL libraries, the parameter
`opensslCipherConfig` is supported for Linux/BSD and
no longer supported in Windows and macOS. 

Specify the cipher string for OpenSSL when using TLS/SSL encryption.
For a list of cipher strings, see
<https://www.openssl.org/docs/man1.1.1/man1/ciphers.html>.
Multiple cipher strings can be provided as a colon-separated list.

**Note:**

This parameter is only for use with TLS 1.2 or earlier. To specify
cipher suites for use with TLS 1.3, use the
`opensslCipherSuiteConfig` parameter.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The use of `TLS` options is preferred over `SSL` options. The TLS options 
have the same functionality as the `SSL` options. The following example 
configures a `mongod` with a `opensslCipherConfig` 
cipher string of `'HIGH:!EXPORT:!aNULL@STRENGTH'`:

```bash
mongod --setParameter opensslCipherConfig='HIGH:!EXPORT:!aNULL@STRENGTH' --tlsMode requireTLS --tlsCertificateKeyFile Certs/server.pem
```

**`opensslCipherSuiteConfig`**

**New in version:** 5.0

*Available on Linux only*

Specify the list of supported cipher suites OpenSSL should permit
when using TLS 1.3 encryption.

For a list of cipher suites for use with TLS 1.3, see
<https://www.openssl.org/docs/man1.1.1/man3/SSL_CTX_set_cipher_list.html>.
Multiple cipher suites can be provided as a colon-separated list.

**Note:**

This parameter is only for use with TLS 1.3. To specify cipher
strings for use with TLS 1.2 or earlier, use the
`opensslCipherConfig` parameter.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following configures a `mongod`
with a `opensslCipherSuiteConfig` cipher suite of
`'TLS_AES_256_GCM_SHA384'` for use with TLS 1.3:

```bash
mongod --setParameter opensslCipherSuiteConfig='TLS_AES_256_GCM_SHA384' --tlsMode requireTLS --tlsCertificateKeyFile Certs/server.pem
```

**`opensslDiffieHellmanParameters`**

*Available on Linux only*

Specify the path to the PEM file that contains the OpenSSL
Diffie-Hellman parameters when using TLS 1.2 or previous. Specifying
the OpenSSL Diffie-Hellman parameters enables support for dhe
cipher suites during TLS/SSL encryption.

This parameter is not supported for use with TLS 1.3.

Ephemeral Diffie-Hellman (DHE) cipher suites (and Ephemeral Elliptic
Curve Diffie-Hellman (ECDHE) cipher suites) provide
tls-forward-secrecy. tls-forward-secrecy cipher suites
create an ephemeral session key that is protected by the server's
private key but never transmitted. This ensures that even if a
server's private key is compromised, you cannot decrypt past
sessions with the compromised key.

**Note:**

If `opensslDiffieHellmanParameters` is unset but
ECDHE is enabled, MongoDB enables DHE using the
`ffdhe3072` Diffie-Hellman parameter, as defined in
7919#appendix-A.2. The `ffdhe3072` is a strong parameter
(specifically, size is greater than 1024). Strong parameters are
not supported with Java 6 and 7 unless extended support has been
purchased from Oracle.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

If for performance reasons, you need to disable support for DHE
cipher suites, use the `opensslCipherConfig` parameter:

```bash
mongod --setParameter opensslCipherConfig='HIGH:!EXPORT:!aNULL:!DHE:!kDHE@STRENGTH' ...
```

**`saslauthdPath`**

**Note:** Available only in MongoDB Enterprise (except MongoDB Enterprise for Windows).

Available for both `mongod` and `mongos`.

Specify the path to the Unix Domain Socket of the `saslauthd`
instance to use for proxy authentication.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`saslHostName`**

Available for both `mongod` and `mongos`.

`saslHostName` overrides MongoDB's default hostname
detection for the purpose of configuring SASL and Kerberos
authentication.

`saslHostName` does not affect the hostname of the
`mongod` or `mongos` instance for any purpose
beyond the configuration of SASL and Kerberos.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**Note:**

`saslHostName` supports Kerberos authentication and is
only included in MongoDB Enterprise. For more information, see the
following:

- Linux:
  /tutorial/control-access-to-mongodb-with-kerberos-authentication
- Windows:
  /tutorial/control-access-to-mongodb-windows-with-kerberos-authentication

**`saslServiceName`**

Available for both `mongod` and `mongos`.

Allows users to override the default Kerberos
service name component of the Kerberos
principal name, on a per-instance basis. If unspecified, the
default value is `mongodb`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

`saslServiceName` is only available in MongoDB
Enterprise.

**Important:**

Ensure that your driver supports alternate service names.

**`scramIterationCount`**

*Default*: `10000`

Available for both `mongod` and `mongos`.

Changes the number of hashing iterations used for all new
`SCRAM-SHA-1` passwords. More iterations increase the amount of
time required for clients to authenticate to MongoDB, but makes
passwords less susceptible to brute-force attempts. The default
value is ideal for most common use cases and requirements.

If you modify this value, it does not change the iteration count for
existing passwords. The `scramIterationCount` value must
be `5000` or greater.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, the following sets the `scramIterationCount`
to `12000`.

```bash
mongod --setParameter scramIterationCount=12000
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, scramIterationCount: 12000 } )
```

**See also:**

- `db.changeUserPassword()`
- `db.createUser()`
- `db.updateUser()`

**`scramSHA256IterationCount`**

*Default*: `15000`

Available for both `mongod` and `mongos`.

Changes the number of hashing iterations used for all new
`SCRAM-SHA-256` passwords. More iterations increase the amount of
time required for clients to authenticate to MongoDB, but makes
passwords less susceptible to brute-force attempts. The default
value is ideal for most common use cases and requirements.

If you modify this value, it does not change iteration count for
existing passwords. The `scramSHA256IterationCount` value
must be `5000` or greater.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

For example, the following sets the `scramSHA256IterationCount`
to `20000`.

```bash
mongod --setParameter scramSHA256IterationCount=20000
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, scramSHA256IterationCount: 20000 } )
```

**See also:**

- `db.changeUserPassword()`
- `db.createUser()`
- `db.updateUser()`

**`sslMode`**

Available for both `mongod` and `mongos`.

Set the `net.ssl.mode` to either `preferSSL` or
`requireSSL`. Useful during rolling upgrade to TLS/SSL to minimize downtime.

For more information about TLS/SSL and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

```bash
db.adminCommand( { setParameter: 1, sslMode: "preferSSL" } )
```

**See also:**

`tlsMode`

**`tlsMode`**

Available for both `mongod` and `mongos`.

Set to either:

- `preferTLS`

- `requireTLS`

The `tlsMode` parameter is useful during rolling
upgrade to TLS/SSL to minimize
downtime.

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

```bash
db.adminCommand( { setParameter: 1, tlsMode: "preferTLS" } )
```

For more information about TLS/SSL and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**See also:**

`sslMode`

**`tlsOCSPStaplingTimeoutSecs`**

Available for Linux.

The maximum number of seconds the
`mongod` / `mongos` instance should wait to
receive the OCSP status response for its certificates.

Specify an integer greater than or equal to (`>=`) 1. If unset,
`tlsOCSPStaplingTimeoutSecs` uses the
`tlsOCSPVerifyTimeoutSecs` value.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following sets the
`tlsOCSPStaplingTimeoutSecs` to 20 seconds:

```bash
mongod --setParameter tlsOCSPStaplingTimeoutSecs=20 ...
```

**See also:**

- `ocspEnabled`
- `ocspValidationRefreshPeriodSecs`
- `tlsOCSPVerifyTimeoutSecs`

**`tlsOCSPVerifyTimeoutSecs`**

Available for Linux and Windows.

*Default*: 5

The maximum number of seconds that the
`mongod` / `mongos` should wait for the OCSP
response when verifying server certificates.

Specify an integer greater than or equal to (`>=`) 1.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following sets the
`tlsOCSPVerifyTimeoutSecs` to 20 seconds:

```bash
mongod --setParameter tlsOCSPVerifyTimeoutSecs=20 ...
```

**See also:**

- `ocspEnabled`
- `ocspValidationRefreshPeriodSecs`
- `tlsOCSPStaplingTimeoutSecs`

**`tlsUseSystemCA`**

Available for `mongod` only.

*Type*: boolean

*Default*: false

Specifies whether MongoDB loads TLS certificates that are already 
available to the operating system's certificate authority. 

**Important:**

When starting a `mongod` instance with 
TLS/SSL enabled, you must 
specify a value for the `--tlsCAFile` flag, the 
`net.tls.CAFile` configuration option, or the `tlsUseSystemCA` 
parameter. 

`--tlsCAFile`, `tls.CAFile`, and `tlsUseSystemCA` are all mutually 
exclusive.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set `tlsUseSystemCA` to `true`: 

```bash
mongod --setParameter tlsUseSystemCA=true
```

For more information about TLS/SSL and MongoDB, see
/tutorial/configure-ssl and
/tutorial/configure-ssl-clients .

**`tlsWithholdClientCertificate`**

Available for both `mongod` and `mongos`.

A TLS certificate is set for a `mongod` or
`mongos` either by the
`--tlsClusterFile` option or by the
`--tlsCertificateKeyFile` option when
`--tlsClusterFile` is not set. If the TLS
certificate is set, by default, the instance sends the certificate when
initiating intra-cluster communications with other
`mongod` or `mongos` instances in
the deployment. Set `tlsWithholdClientCertificate` to `1` or `true` to
direct the instance to withhold sending its TLS certificate during these
communications. Use this option with
`--tlsAllowConnectionsWithoutCertificates`
(to allow inbound connections without certificates) on all members of the
deployment. `tlsWithholdClientCertificate` is mutually exclusive with
`--clusterAuthMode x509`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`tlsX509ClusterAuthDNOverride`**

Available for both `mongod` and `mongos`.

An alternative Distinguished Name (DN) that the instance can also
use to identify members of the deployment.

For a MongoDB deployment that uses X.509 certificates for
`clusterAuthMode`, deployment members identify
each other using X.509 certificates (
`net.tls.clusterFile`, if specified, and
`net.tls.certificateKeyFile`) during intra-cluster
communications. For members of the same deployment, the `DN` from
their certificates must have the same Organization attributes
(`O`\'s), the Organizational Unit attributes (`OU`\'s), and the
Domain Components (`DC`\'s).

If `tlsX509ClusterAuthDNOverride` is set for a member,
the member can also use the override value when comparing the `DN`
components (`O`\'s, `OU`\'s, and `DC`\'s) of the presented
certificates. That is the member checks the presented certificates
against its
`net.tls.clusterFile`/`net.tls.certificateKeyFile`.
If the DN does not match, the member checks the presented
certificate against the `tlsX509ClusterAuthDNOverride`
value.

**Note:**

If set, you must set this parameter on all members of the
deployment.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

You can use this parameter for a rolling update of certificates to
new certificates that contain a new `DN` value. See
/tutorial/rotate-x509-membership-certificates.

For more information about membership certificate requirements, see
x509-member-certificate-requirements for details.

**`tlsX509ExpirationWarningThresholdDays`**

Available for both `mongod` and `mongos`.

*Default* : 30

Starting in MongoDB 4.4, `mongod` / `mongos`
logs a warning on connection if the presented X.509 certificate
expires within `30` days of the `mongod/mongos` system clock.
Use the `tlsX509ExpirationWarningThresholdDays` parameter
to control the certificate expiration warning threshold:

- Increase the parameter value to trigger warnings farther ahead of
  the certificate expiration date.

- Decrease the parameter value to trigger warnings closer to the
  certificate expiration date.

- Set the parameter to `0` to disable the warning.

This parameter has a minimum value of `0`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For more information on X.509 certificate validity, see [RFC 5280 4.1.2.5](https://tools.ietf.org/html/rfc5280#section-4.1.2.5).

**`userCacheInvalidationIntervalSecs`**

*Default*: 30

Available for `mongos` only.

On a `mongos` instance, specifies the interval (in seconds)
at which the `mongos` instance checks to determine whether
the in-memory cache of user objects has stale data, and if so,
clears the cache. If there are no changes to user objects,
`mongos` will not clear the cache.

This parameter has a minimum value of `1` second and a maximum
value of `86400` seconds (24 hours).

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command

- To set the parameter at startup, use the
  `setParameter` setting

**`authFailedDelayMs`**

*Default*: 0

Available for both `mongod` and `mongos`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

The number of milliseconds to wait before informing clients that their
authentication attempt has failed. This parameter may be in the range
`0` to `5000`, inclusive.

Setting this parameter makes brute-force login attacks on a database
more time-consuming. However, clients waiting for a response from the
MongoDB server still consume server resources, and this may adversely
impact benign login attempts if the server is denying access to many
other clients simultaneously.

**`allowRolesFromX509Certificates`**

*Default*: true

Available for both `mongod` and `mongos`.

A boolean flag that allows or disallows the retrieval of
authorization roles from client X.509 certificates.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting.
