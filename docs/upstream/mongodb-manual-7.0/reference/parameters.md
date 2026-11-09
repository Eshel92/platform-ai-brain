<!-- Converted from reference/parameters.txt (reStructuredText). Includes are inlined. -->

# MongoDB Server Parameters for a Self-Managed Deployment

## Synopsis

MongoDB provides several configuration options that you can set
using:

- the `setParameter` command:

  ```javascript
  db.adminCommand( { setParameter: 1, <parameter>: <value>  } )
  ```

- the `setParameter` configuration setting:

  ```yaml
  setParameter:
     <parameter1>: <value1>
     ...
  ```

- the `--setParameter` command-line option for `mongod`
  and `mongos`:

  ```bash
  mongod --setParameter <parameter>=<value>
  mongos --setParameter <parameter>=<value>
  ```

For additional configuration options, see
configuration-options, `mongod` and
`mongos`.

## Parameters

### Authentication Parameters

**`allowRolesFromX509Certificates`**

Available for both `mongod` and `mongos`.

*Default*: true

Allows or disallows the retrieval of authorization roles from
client X.509 certificates.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

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
| GSSAPI (Kerberos) | External authentication using Kerberos. This mechanism is available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced). |
| PLAIN (LDAP SASL) | External authentication using LDAP. You can also use `PLAIN` for authenticating in-database users. `PLAIN` transmits passwords in plain text. This mechanism is available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced). |
| MONGODB-OIDC | OpenID Connect is an authentication layer built on top of OAuth2. This mechanism is available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced). |

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to specify both `PLAIN` and `SCRAM-SHA-256` as the
authentication mechanisms, use the following command:

```bash
mongod --setParameter authenticationMechanisms=PLAIN,SCRAM-SHA-256 --auth
```

**`awsSTSRetryCount`**

**Changed in version:** 7.0 (Also starting in 6.0.7 and 5.0.18)

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
configure-client-tls-tutorial .

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

**`JWKSMinimumQuiescePeriodSecs`**

**New in version:** 7.0.31

Available for both `mongod` and `mongos`.

*Default*: 60 seconds (1 minute)

Specifies the minimum time period that must pass between subsequent fetches of
a given IdP's `JWKSetURI` endpoint. If an RSA public key is changed multiple 
times within the quiesce period, that key may not work as expected 
for up to a minute unless the quiesce period is manually reduced. If this parameter
is set to zero, there is no quiesce period and the key can be refreshed repeatedly.

This parameter is available at both startup and runtime. To set the
parameter, use the `setParameter` setting. 

**`KeysRotationIntervalSec`**

*Default*: 7776000 seconds (90 days)

Specifies the number of seconds for which an [HMAC signing key](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
is valid before rotating to the next one. This parameter is intended
primarily to facilitate authentication testing.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`ldapForceMultiThreadMode`**

Available for both `mongod` and `mongos`.

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

If you have any concerns regarding your MongoDB version, OS version,
or libldap version, contact MongoDB Support.

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

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

To set the retry count at startup, use the
`security.ldap.retryCount` configuration file option.

For example, the following sets `ldapRetryCount` to
`3`:

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
security-ldap-external.

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
start-up, and cannot change this setting during run time with the
`setParameter` database command.

**`ldapConnectionPoolMinimumConnectionsPerHost`**

*Default*: 1

The minimum number of connections to keep open to each LDAP server.

You can only set
`ldapConnectionPoolMinimumConnectionsPerHost` during
start-up, and cannot change this setting during run time with the
`setParameter` database command.

**`ldapConnectionPoolMaximumConnectionsPerHost`**

*Changed starting in MongoDB versions 5.0.9 and 6.0.0*
Changed default value to `2147483647`. In previous versions, the
default is unset.

*Default*: 2147483647

The maximum number of connections to keep open to each LDAP server.

You can only set
`ldapConnectionPoolMaximumConnectionsPerHost` during
start-up, and cannot change this setting during run time with the
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
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`oidcIdentityProviders`**

**New in version:** 7.0

Use this parameter to specify identity provider (IDP) configurations when 
using OpenID Connect Authentication.

`oidcIdentityProviders` accepts an array of zero or more identity provider 
(IDP) configurations. An empty array (default) indicates no OpenID Connect 
support is enabled. 

When more than one IDP is defined, `oidcIdentityProviders` uses the 
`matchPattern` field to select an IDP. Array order determines the priority 
and the first IDP is always selected.

Starting in MongoDB 7.0, when multiple identity providers (IDP) are 
defined, the `oidcIdentityProviders` parameter accepts duplicate 
`issuer` values as long as the `audience` value is unique for each 
issuer. 

**Important:**

- If you are using FCV (feature compatibility version) 
  lower than `7.0`, the `authorizationClaim` and `clientId` 
  fields are required.

- The `useAuthorizationClaim` and `supportsHumanFlows` fields are 
  only available in deployments with FCV (feature 
  compatibility version) `7.0`.

To find the FCV used by your deployment, see 
get-feature-compat-version.

#### oidcIdentityProviders Fields

* - Field

  - Necessity

  - Type

  - Description

* - `issuer`

  - Required

  - string

  - The issuer URI of the IdP that the server should accept tokens from. This 
    must match the `iss` field in any JWT used for authentication.

    Starting in MongoDB 7.0, when multiple identity providers (IDP) are 
    defined, the `oidcIdentityProviders` parameter accepts duplicate 
    `issuer` values as long as the `audience` value is unique for each 
    issuer. 

    If you specify an unreachable issuer URI, MongoDB:

    1. Logs a warning.
    #. Continues server startup, which allows you to update the issuer
       URI.
    #. Reattempts issuer contact. If MongoDB reaches the issuer URI
       and validates the access token, authentication succeeds. If
       the issuer URI remains unreachable, authentication fails.

* - `authNamePrefix`

  - Required

  - string

  - Unique prefix applied to each generated `UserName` and `RoleName` used 
    in authorization. `authNamePrefix` can only contain the
    following characters:

    - alphanumeric characters (combination of `a` to `z` and `0` to `9`)
    - hyphens (`-`)
    - underscores (`_`) 

* - `matchPattern`

  - Conditional

  - string

  - Regex pattern used to determine which IdP should be used. `matchPattern` 
    matches against usernames. Array order determines the priority and the 
    first IdP is always selected. 

    `matchPattern` is required in some configurations, depending on 
    how the user sets `supportsHumanFlows`:

    - When only one IdP has `supportsHumanFlows` set to `true`
      (the default), `matchPatterns` is optional.

    - When multiple IdP's have `supportsHumanFlows` set to `true`
      (the default), each of these requires `matchPatterns`.

    - `matchPatterns` is optional for any IdP where `supportsHumanFlows`
      is set to `false`.

    This is not a security mechanism. `matchPattern` serves only as an advisory 
    to clients. MongoDB accepts tokens issued by the IdP whose principal 
    names do not match this pattern.

* - `clientId`

  - Conditional

  - string 

  - ID provided by the IdP to identify the client that receives the access tokens.

    Required when `supportsHumanFlows` is set to `true` (the default).

    IMPORTANT: When using FCV below `7.0`, `clientId` is **required**.

* - `audience`

  - Required

  - string 

  - Specifies the application or service that the access token is intended for.

    When more than one IdP is defined, this must be a unique value for 
    each configuration that shares an `issuer`. 

* - `requestScopes`

  - Optional

  - array[ string ] 

  - Permissions and access levels that MongoDB requests from the IdP.

    IMPORTANT: By default, clients such as `Compass` and 
    `mongosh` request the `oidc` and `offline_access` scopes 
    from the IdP. If the IdP supports neither `oidc` nor `offline_access`, 
    the client doesn't request them. If the IdP supports `oidc` but not 
    `offline_access`, you must re-authenticate frequently.

* - `principalName`

  - Optional 

  - string 

  - The claim to be extracted from the access token containing MongoDB user 
    identifiers. 

    The default value is `sub` (stands for `subject`). 

* - `useAuthorizationClaim` 

  - Optional

  - boolean

  - Determines if the `authorizationClaim` field is required. The default 
    value is `true`.

    If the `useAuthorizationClaim` field is set to `true`, the server requires 
    an `authorizationClaim` for the identity provider's config. This is the 
    default behavior.

    If the `useAuthorizationClaim` field is set to `false`, the 
    `authorizationClaim` field is optional (and ignored if provided). 
    Instead, the server does the following:

    - Searches the token for a claim whose name is listed in the 
      `principalNameClaim` field. This is typically named `sub`. For 
      example:

      `sub: "spencer.jackson@example.com"`

    - Constructs the internal username by concatenating the `authNamePrefix`, 
      a forward slash (`/`), and the contents of the claim identified by 
      `principalNameClaim` within the access token. For example, with a 
      `authNamePrefix` field value of "mdbinc", the internal username is:

      `mdbinc/spencer.jackson@example.com`

    - Looks for the user with this username and authorize the client with the 
      roles:

      ```javascript
      { user: "mdbinc/spencer.jackson@example.com", 
        db: "$external" }
      ```

    **New in version:** 7.0.5

    IMPORTANT: `useAuthorizationClaim` is only available in 
    deployments with FCV `7.0`.

* - `authorizationClaim` 

  - Conditional

  - string

  - Required, unless `useAuthorizationClaim` is set to `false`.

    Claim extracted from access token that contains MongoDB role names.

    IMPORTANT: When using FCV below `7.0`, `authorizationClaim` 
    is **required**.

* - `logClaims`

  - Optional

  - array[ string ]

  - List of access token claims to include in log and audit messages upon 
    authentication completion.

* - `JWKSPollSecs`

  - Optional

  - integer

  - Frequency, in seconds, to request an updated JSON Web Key Set (JWKS) from the IdP. 
    A setting of 0 disables polling.

    When more than one IdP is defined, this must be the same value for 
    each configuration that shares an `issuer`.  

* - `supportsHumanFlows`

  - Optional

  - boolean

  - Whether the OIDC provider supports human or machine workflows.  This
    affects the `clientId` and `matchPattern` fields.

    You may find it useful to set this field to `false` with machine workload
    IdP's to allow them to omit the `clientId` when it's unneeded.

    Default: `true`.

    **New in version:** 7.2 (*Also available in 7.0.5*)

    IMPORTANT: `supportsHumanFlows` is only available in 
    deployments with FCV `7.0`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

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

- `ocspStaplingRefreshPeriodSecs`
- `tlsOCSPStaplingTimeoutSecs`
- `tlsOCSPVerifyTimeoutSecs`

**`ocspStaplingRefreshPeriodSecs`**

Available for both `mongod` and `mongos`.

Available on Linux.

The number of seconds to wait before refreshing the stapled OCSP
status response. Specify a number greater than or equal to 1.

You can only set `ocspStaplingRefreshPeriodSecs` during
startup in the `configuration file` or with
the `--setParameter` option on the command line. For example, the
following sets the parameter to 3600 seconds:

```bash
mongod --setParameter ocspStaplingRefreshPeriodSecs=3600 ...
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

**`pessimisticConnectivityCheckForAcceptedConnections`**

*Available on Linux only*

*Type:* boolean

*Default:* false

When set to `true`, instructs the server to check the connectivity of accepted connections 
before processing them and to immediately discard connections that the client terminates.

Consider enabling this parameter on smaller instance types. You can use it when 
you want to trade a small amount of latency on new connection establishment for 
reduced server work when processing new connections that have already been closed on the client side.

**`saslauthdPath`**

Available for both `mongod` and `mongos`.

**Note:** Available only in MongoDB Enterprise (except MongoDB Enterprise for Windows).

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

Available for both `mongod` and `mongos`.

*Default*: `10000`

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
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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

Available for both `mongod` and `mongos`.

*Default*: `15000`

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
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

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
configure-client-tls-tutorial .

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

Use the `tlsMode` parameter during rolling
upgrade to TLS/SSL to minimize
downtime.

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

```bash
db.adminCommand( { setParameter: 1, tlsMode: "preferTLS" } )
```

For more information about TLS/SSL and MongoDB, see
/tutorial/configure-ssl and
configure-client-tls-tutorial .

**See also:**

`sslMode`

**`tlsClusterAuthX509Override`**

**New in version:** 7.0

Overrides the `clusterAuthX509` configuration options.

```yaml
setParameter:
   tlsClusterAuthX509Override: "{ attributes: 'O=MongoDB, OU=MongoDB Server' }"
```

The parameter supports `attributes` and `extensionValue` overrides.

When the server authenticates connections from members, it analyzes the
X.509 certificate to determine whether it belongs to a cluster member.
If the server uses the `attributes` 
setting or the `attributes` field on the 
`tlsClusterAuthX509Override` parameter, it checks 
the Distinguished Name (DN) values of the certificate.
If the `extensionValue` setting or the
`extensionValue` field of 
the `tlsClusterAuthX509Override` parameter is set, it checks 
the extension values of the certificate.  If it finds a match,
it authorizes the connection as a peer.

Use this parameter to rotate certificates when the new certificates have
different attributes or extension values.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

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
- `ocspStaplingRefreshPeriodSecs`
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
- `ocspStaplingRefreshPeriodSecs`
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
configure-client-tls-tutorial .

**`tlsWithholdClientCertificate`**

Available for both `mongod` and `mongos`.

*Default*: false

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
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

You can use this parameter for a rolling update of certificates to
new certificates that contain a new `DN` value. See
/tutorial/rotate-x509-membership-certificates.

For more information about membership certificate requirements, see
x509-member-certificate-requirements for details.

**`tlsX509ExpirationWarningThresholdDays`**

Available for both `mongod` and `mongos`.

*Default* : 30

`mongod` / `mongos` logs a warning on connection if the 
presented X.509 certificate expires within `30` days of the 
`mongod/mongos` system clock. Use the 
`tlsX509ExpirationWarningThresholdDays` parameter
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

Available for `mongos` only.

*Default*: 30

On a `mongos` instance, specifies the interval (in seconds)
at which the `mongos` instance checks to determine whether
the in-memory cache of user objects has stale data, and if so,
clears the cache. If there are no changes to user objects,
`mongos` will not clear the cache.

This parameter has a minimum value of `1` second and a maximum
value of `86400` seconds (24 hours).

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`authFailedDelayMs`**

Available for both `mongod` and `mongos`.

*Default*: 0

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

Available for both `mongod` and `mongos`.

*Default*: true

A boolean flag that allows or disallows the retrieval of
authorization roles from client X.509 certificates.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

### General Parameters

**`allowDiskUseByDefault`**

Available for `mongod` only.

*Default*: True

Starting in MongoDB 6.0, pipeline stages that require more than 100 
megabytes of memory to execute write temporary files to disk by 
default. These temporary files last for the duration of the pipeline 
execution and can influence storage space on your instance. In earlier 
versions of MongoDB, you must pass  `{ allowDiskUse: true }` to 
individual `find` and `aggregate` commands to enable this 
behavior.

Individual `find` and `aggregate` commands can override the 
`allowDiskUseByDefault` parameter by either:

- Using `{ allowDiskUse: true }` to allow writing temporary files out 
  to disk when `allowDiskUseByDefault` is set to `false`

- Using `{ allowDiskUse: false }` to prohibit writing temporary files
  out to disk when `allowDiskUseByDefault` is set to `true`

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongod --setParameter allowDiskUseByDefault=false
```

`allowDiskUseByDefault` only works on `mongod` 
not `mongos`. `mongos` never writes temporary
files to disk. Use the `setParameter` command in 
a `mongosh` session that is connected to a running 
`mongod` to change the value of the parameter while the
server is running:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      allowDiskUseByDefault: false 
  }
)
```

**`capMemoryConsumptionForPreAuthBuffers`**

**New in version:** 7.0.29

Available for both `mongod` and `mongos`.

*Type*: Int

*Default*: 20

Specifies the maximum percentage of total memory to allocate to pre-auth 
buffers for connections. Setting the parameter to `100` disables this 
limitation.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following operation sets `capMemoryConsumptionForPreAuthBuffers`
to `30`:

```bash
mongod --setParameter capMemoryConsumptionForPreAuthBuffers=30
```

**`httpVerboseLogging`**

Available for both `mongod` and `mongos`.

Adds more verbose tracing for curl on Linux and macOS. Has no affect on Windows.

By default, the parameter is unset.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongos --setParameter httpVerboseLogging=true
```

**`slowConnectionThresholdMillis`**

**New in version:** 6.3

Available for both `mongod` and `mongos`.

*Default*: 100

Sets the time limit in milliseconds to log the establishment of slow
server connections.

If a connection takes longer to establish than the
`slowConnectionThresholdMillis` parameter, an event is
added to the log with the message `msg`
field set to `"Slow connection establishment"`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `slowConnectionThresholdMillis`
to `250` milliseconds.

```bash
mongod --setParameter slowConnectionThresholdMillis=250
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, slowConnectionThresholdMillis: 250 } )
```

**`connPoolMaxConnsPerHost`**

Available for both `mongod` and `mongos`.

*Default*: 200

Sets the maximum size of the legacy connection pools for outgoing connections
to other `mongod` instances in the global connection pool. The size
of a pool does not prevent the creation of additional connections,
but *does* prevent a connection pool from retaining connections in
excess of the value of `connPoolMaxConnsPerHost`.

**Note:**

The parameter is separate from the connections in TaskExecutor
pools. See `ShardingTaskExecutorPoolMaxSize`.

**Only** adjust this setting if your driver does *not* pool
connections and you're using authentication in the
context of a sharded cluster.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter connPoolMaxConnsPerHost=250
```

**`connPoolMaxInUseConnsPerHost`**

Available for both `mongod` and `mongos`.

Sets the maximum number of in-use connections at any given time for
for outgoing connections to other `mongod` instances in
the legacy global connection pool.

By default, the parameter is unset.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter connPoolMaxInUseConnsPerHost=100
```

**See also:**

`connPoolMaxConnsPerHost`

**`globalConnPoolIdleTimeoutMinutes`**

Available for both `mongod` and `mongos`.

Sets the time limit that connection in the legacy global connection
pool can remain idle before being closed.

By default, the parameter is unset.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongos --setParameter globalConnPoolIdleTimeoutMinutes=10
```

**`cursorTimeoutMillis`**

Available for both `mongod` and `mongos`.

*Default*: 600000 (10 minutes)

Sets the expiration threshold in milliseconds for idle cursors before
MongoDB removes them; specifically, MongoDB removes cursors that have
been idle for the specified `cursorTimeoutMillis`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the `cursorTimeoutMillis`
to `300000` milliseconds (5 minutes).

```bash
mongod --setParameter cursorTimeoutMillis=300000
```

Or, if using the `setParameter` command within
`mongosh`:

```javascript
db.adminCommand( { setParameter: 1, cursorTimeoutMillis: 300000 } )
```

Setting `cursorTimeoutMillis` to less than or equal
to `0` results in all cursors being immediately eligible for timeout.
Generally, the timeout value should be greater than the average amount of
time for a query to return results. Use tools like the `cursor.explain()`
cursor modifier to analyze the average query time and select an appropriate
timeout period.

**Warning:**

MongoDB cleans up orphaned cursors after the
`cursorTimeoutMillis` threshold only if they are not tied to sessions.

MongoDB cleans up cursors linked to sessions with the
`localLogicalSessionTimeoutMinutes` lifecycle, regardless of
the `cursorTimeoutMillis` value. To handle long idle periods,
use `Mongo.startSession()` and refresh the session using the
`refreshSessions` command. For details, see
refresh-session-cursor-example.

**`maxNumActiveUserIndexBuilds`**

Available for `mongod` only.

*Type*: integer

*Default*: 3

Sets the maximum number of index build requests that MongoDB can
perform concurrently. `maxNumActiveUserIndexBuilds` is a global
limit that applies for all collections.

The following table shows the default values for 
`maxNumActiveUserIndexBuilds` based on Atlas tiers:

| **Atlas Tiers** | **maxNumActiveUserIndexBuilds Default** |
|---|---|
| Small M tiers (`M10`, `M20`, `M30`, `M40`) | `1` |
| Medium M tiers (`M50`, `M60`) | `2` |
| Large M tiers (`M80` and higher, including NMVe variants) | `3` |

**Note:**

These defaults also apply to the corresponding low-CPU `R` tiers.

The `createIndexes` command builds indexes. Even if the
`createIndexes` command builds multiple indexes at once, the
command execution only adds `1` to `maxNumActiveUserIndexBuilds`.

Increasing the value of `maxNumActiveUserIndexBuilds` allows
additional concurrent index builds at the cost of increased pressure
on the WiredTiger cache.

System indexes are not limited to `maxNumActiveUserIndexBuilds`,
however a system index build counts against the limit for user index
builds.

After the server reaches `maxNumActiveUserIndexBuilds`, it blocks
additional user index builds until the number of concurrent index
builds drops below the `maxNumActiveUserIndexBuilds` limit. If an
index build is blocked, the server logs this message:

```sh
Too many index builds running simultaneously, waiting until the
number of active index builds is below the threshold.
```

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following command sets a limit of 4 concurrent index builds:

```javascript
db.adminCommand( { setParameter: 1, maxNumActiveUserIndexBuilds: 4 } )
```

See also:

- `maxIndexBuildMemoryUsageMegabytes`
- index-creation-background

**`messageSizeErrorRateSec`**

**New in version:** 7.0.29

Available for both `mongod` and `mongos`.

*Type*: Int

*Default*: 5

Specifies the rate, in seconds, at which the server logs message size errors
at the Info level. 

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following operation sets `messageSizeErrorRateSec`
to `6`:

```bash
mongod --setParameter messageSizeErrorRateSec=6
```

**`notablescan`**

Available for `mongod` only.

Prevents running some collection scans when an index could be used, whether 
present or not. If `true`, MongoDB will not execute queries that require
a collection scan and will return an error. Exclusions include queries 
without filters and queries against capped collections, such as the oplog.

Consider the following example which sets `notablescan` to `true`
or true:

```javascript
db.adminCommand( { setParameter: 1, notablescan: true } )
```

Set `notablescan` to `true` to test application queries
and identify queries that scan an entire collection and cannot use
an index.

To detect unindexed queries without `notablescan`, consider reading
the /tutorial/evaluate-operation-performance section and using
the `logLevel` parameter, `mongostat` and
profiling.

Don't run production `mongod` instances with
`notablescan` because preventing collection scans can potentially
affect queries in all databases, including administrative queries.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**Note:**

`notablescan` does not allow unbounded queries that use a
clustered index because the queries require a full collection
scan. For more information, see Collection Scans.

**`preAuthMaximumMessageSizeBytes`**

**New in version:** 7.0.29

Available for both `mongod` and `mongos`.

*Type*: Int

*Default*: 16384 (16 KiB)

The maximum size of a message in bytes that you can send before the session
authenticates.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the maximum size of the message to 
1700 bytes:

```bash
mongod --setParameter preAuthMaximumMessageSizeBytes=1700
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, preAuthMaximumMessageSizeBytes: 1700 } )
```

**`ttlMonitorEnabled`**

Available for `mongod` only.

*Default*: `true`

To support TTL Indexes, `mongod`
instances have a background thread that is responsible for deleting
documents from collections with TTL indexes.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To disable this worker thread for a `mongod`, set
`ttlMonitorEnabled` to `false`, as in the following
operations:

```javascript
db.adminCommand( { setParameter: 1, ttlMonitorEnabled: false } )
```

Alternately, you may disable the thread at startup time by starting the
`mongod` instance with the following option:

```bash
mongod --setParameter ttlMonitorEnabled=false
```

**Important:**

Do not run production `mongod` instances with
`ttlMonitorEnabled` disabled, except under guidance from MongoDB
support. Preventing TTL document removal can negatively impact
MongoDB internal system operations that depend on TTL Indexes.

**`tcpFastOpenServer`**

Available for both `mongod` and `mongos`.

*Default*: `true`

Enables support for accepting inbound TCP Fast Open (TFO) connections
to the `mongod/mongos` from a client. TFO requires both the
client and `mongod/mongos` host machine support and enable
TFO:

Windows
  The following Windows operating systems support TFO:

  - Microsoft Windows Server 2016 and later.
  - Microsoft Windows 10 Update 1607 and later.

macOS
  macOS 10.11 (El Capitan) and later support TFO.

Linux
  Linux operating systems running Linux Kernel 3.7 or later
  can support inbound TFO.

  Set the value of `/proc/sys/net/ipv4/tcp_fastopen` to
  enable inbound TFO connections:

  - Set to `2` to enable only inbound TFO connections.
  - Set to `3` to enable inbound and outbound TFO connections.

This parameter has no effect if the host operating system does not
support *or* is not configured to support TFO connections.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

[RFC7413](https://tools.ietf.org/html/rfc7413).

**`tcpFastOpenClient`**

Available for both `mongod` and `mongos`.

*Default*: `true`

*Linux Operating System Only*

Enables support for outbound TCP Fast Open (TFO) connections from the
`mongod/mongos` to a client. TFO requires both the client
and the `mongod/mongos` host machine support and enable TFO.

Linux operating systems running Linux Kernel 4.11 or later can
support outbound TFO.

Set the value of `/proc/sys/net/ipv4/tcp_fastopen` to enable
outbound TFO connections:

- `1` to enable only outbound TFO connections.
- `3` to enable inbound and outbound TFO connections.

This parameter has no effect if the host operating system does not
support *or* is not configured to support TFO connections.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

[RFC7413](https://tools.ietf.org/html/rfc7413).

**`tcpFastOpenQueueSize`**

Available for both `mongod` and `mongos`.

*Default*: `1024`

As part of establishing a TCP Fast Open (TFO) connection, the client
submits a valid TFO cookie to the `mongod/mongos` *before*
completion of the standard TCP 3-way handshake. The
`mongod/mongos` keeps a queue of all such pending TFO connections.

The `tcpFastOpenQueueSize` parameter sets the size of the queue of
pending TFO connections. While the queue is full, the
`mongod/mongos` falls back to the normal three-way handshake for
incoming client requests and ignores the presence of TFO cookies.
Once the queue size falls back below the limit, the `mongod/mongos`
begins accepting new TFO cookies.

- Increasing the default queue size may improve the effect of
  TFO on network performance. However, large queue sizes also
  increase the risk of server resource exhaustion due to excessive
  incoming TFO requests.

- Decreasing the default queue size may reduce the risk of resource
  server resource exhaustion due to excessive incoming TFO requests.
  However, small queue sizes may also reduce the effect of TFO on
  network performance.

  The minimum queue size is `0`. A queue of `0` effectively
  disables TFO.

This parameter has no effect on host operating systems that do
not support or are not configured for TFO connections. 

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

- [RFC7413 TCP Fast Open Section 5: Security Considerations](https://tools.ietf.org/html/rfc7413#section-5)

- [RFC7413 TCP Fast Open Section 6: TFO Applicability](https://tools.ietf.org/html/rfc7413#section-6)

**`disableJavaScriptJIT`**

Available for `mongod` only.

The MongoDB JavaScript engine uses SpiderMonkey, which implements
Just-in-Time (JIT) compilation for improved performance when running scripts.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To enable the JIT, set `disableJavaScriptJIT` to `false`, as in
the following example:

```javascript
db.adminCommand( { setParameter: 1, disableJavaScriptJIT: false } )
```

**Note:**

`$where` will reuse existing JavaScript interpreter
contexts, so changes to `disableJavaScriptJIT` may not
take effect immediately for these operations.

Alternately, you may enable the JIT at startup time by starting the
`mongod` instance with the following option:

```bash
mongod --setParameter disableJavaScriptJIT=false
```

**`indexMaxNumGeneratedKeysPerDocument`**

**New in version:** 5.3

*Default*: 100000

Limits the maximum number of keys generated for a document to
prevent out of memory errors. It is possible to raise the limit, but
if an operation requires more keys than the
`indexMaxNumGeneratedKeysPerDocument` parameter specifies,
the operation will fail.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`maxIndexBuildMemoryUsageMegabytes`**

*Default*: 200 

Limits the amount of memory that simultaneous index
builds on one collection may consume for the duration of the
builds. The specified amount of memory is shared between all
indexes built using a single
`createIndexes` command or its shell helper
`db.collection.createIndexes()`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The memory consumed by an index build is separate from the
WiredTiger cache memory (see
`cacheSizeGB`).

`maxIndexBuildMemoryUsageMegabytes` sets a limit on how much 
memory the index build uses at once. This can impact performance 
when the index build process generates 
and sorts keys for the index. Increasing the memory limit 
improves sorting performance during an index build.

The `maxIndexBuildMemoryUsageMegabytes` limit applies to all
index builds initiated by user commands like `createIndexes` or
administrative processes like initial sync.

An initial sync populates only one collection 
at a time and has no risk of exceeding the memory limit. However, it is 
possible for a user to start index builds on multiple collections in 
multiple databases simultaneously.

Changing `maxIndexBuildMemoryUsageMegabytes` does not affect an 
in progress index build if it has already started a collection scan. 
However, a forced replica set reconfiguration restarts the collection 
scan and uses the most current 
`maxIndexBuildMemoryUsageMegabytes` provided.

- For feature compatibility version (fcv) `"4.2"`
  and later, the index build memory limit applies to all index builds.

**`reportOpWriteConcernCountersInServerStatus`**

*Default*: false

A boolean flag that determines whether the
`db.serverStatus()` method and `serverStatus`
command return `opWriteConcernCounters` information. [#perf]_

```bash
mongod --setParameter reportOpWriteConcernCountersInServerStatus=true
```

**`watchdogPeriodSeconds`**

Available for `mongod` only.

*Type*: integer

*Default*: -1 (disabled)

Determines how frequent the Storage Node Watchdog checks the status of the monitored
filesystems:

* The `--dbpath` directory
* The `journal` directory inside the `--dbpath` 
  directory
* The directory of `--logpath` file
* The directory of `--auditPath` file

Valid values for `watchdogPeriodSeconds` are:

- `-1` (the default), to disable/pause Storage Node Watchdog, or

- An integer greater than or equal to 60.

**Note:**

- If a filesystem on a monitored directory becomes unresponsive,
  it can take a maximum of nearly *twice* the value of
  `watchdogPeriodSeconds` to terminate the
  `mongod`.

- If any of its monitored directory is a symlink to other
  volumes, the Storage Node Watchdog does not monitor the symlink
  target. For example, if the `mongod` uses
  `storage.directoryPerDB: true` (or `--directoryperdb`) and symlinks a database directory to
  another volume, the Storage Node Watchdog does not follow the
  symlink to monitor the target.

To enable Storage Node Watchdog,
`watchdogPeriodSeconds` must be set during startup.

```bash
mongod --setParameter watchdogPeriodSeconds=60
```

You can only enable the Storage Node Watchdog at startup. However, once enabled, you can
pause the Storage Node Watchdog or
change the `watchdogPeriodSeconds` during run time.

Once enabled,

- To pause the Storage Node Watchdog
  during run time, set `watchdogPeriodSeconds` to -1.

  ```javascript
  db.adminCommand( { setParameter: 1, watchdogPeriodSeconds: -1 } )
  ```

- To resume or change the period during run time, set
  `watchdogPeriodSeconds` to a number greater than or
  equal to 60.

  ```javascript
  db.adminCommand( { setParameter: 1, watchdogPeriodSeconds: 120 } )
  ```

**`tcmallocAggressiveMemoryDecommit`**

*Type*: integer (`0` or `1` only)

Default: 0

If you enable `tcmallocAggressiveMemoryDecommit`, MongoDB:

- releases a chunk of memory to system, and 

- attempts to return all neighboring free chunks. 

A value of `1` enables `tcmallocAggressiveMemoryDecommit`; 
`0` disables this parameter.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

If you enable this parameter, the system will require new memory allocations 
for use. Consider enabling `tcmallocAggressiveMemoryDecommit` 
only on memory-constrained systems and after pursuing other memory and 
performance options.

Despite the potential performance degradation when using 
`tcmallocAggressiveMemoryDecommit`, it is often preferred over using 
`tcmallocReleaseRate`.

**`tcmallocReleaseRate`**

Default: 1.0

Specifies the tcmalloc release rate ([TCMALLOC_RELEASE_RATE](https://gperftools.github.io/gperftools/tcmalloc.html#runtime)).
Per https://gperftools.github.io/gperftools/tcmalloc.html#runtime
TCMALLOC_RELEASE_RATE is described as the "Rate at which we release
unused memory to the system, via
madvise(MADV_DONTNEED), on systems that support it. Zero means we
never release memory back to the system. Increase this flag to
return memory faster; decrease it to return memory slower.
Reasonable rates are in the range [0,10]."

**Note:**

Consider using `tcmallocAggressiveMemoryDecommit` instead of 
`tcmallocReleaseRate`, unless you see a significant performance 
degradation when using `tcmallocAggressiveMemoryDecommit`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To modify the release rate during run time, you can use the
`setParameter` command; for example:

```javascript
db.adminCommand( { setParameter: 1, tcmallocReleaseRate: 5.0 } )
```

You can also set `tcmallocReleaseRate` at startup time;
for example:

```bash
mongod --setParameter "tcmallocReleaseRate=5.0"
```

**`fassertOnLockTimeoutForStepUpDown`**

**New in version:** 5.3

Available for both `mongod` and `mongos`.

Default: 15 seconds

Allows a server that receives a request to step up or step down, to 
terminate if it is unable to comply (for example due
to faulty server disks) within the timeout. This enables a cluster to 
successfully elect a new primary node and thus continue to be available. 

`fassertOnLockTimeoutForStepUpDown` defaults to 15 seconds. To disable
nodes from fasserting, set `fassertOnLockTimeoutForStepUpDown=0`. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example disables nodes from fasserting: 

```bash
mongod --setParameter fassertOnLockTimeoutForStepUpDown=0
```

### Logging Parameters

**`logLevel`**

Available for both `mongod` and `mongos`.

*Default*: 0 (informational)

Specify an integer between `0` and `5` signifying the verbosity
of the logging, where `5` is the
most verbose. [#log-message]_

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the `logLevel` to `2`:

```javascript
db.adminCommand( { setParameter: 1, logLevel: 2 } )
```

**See also:**

- `logComponentVerbosity`
- `systemLog.verbosity`

**`logComponentVerbosity`**

Available for both `mongod` and `mongos`.

*Default*: 0

Sets the verbosity levels of various components for log messages. The verbosity level determines the
amount of Informational and Debug
messages MongoDB outputs. [#log-message2]_

The verbosity level can range from `0` to `5`:

- `0` is the MongoDB's default log verbosity level, to include
  Informational messages.

- `1` to `5` increases the verbosity level to include
  Debug messages.

For a component, you can also specify `-1` to inherit the parent's
verbosity level.

To specify the verbosity level, use a document similar to the
following:

```none
{
  verbosity: <int>,
  <component1>: { verbosity: <int> },
  <component2>: {
     verbosity: <int>,
     <component3>: { verbosity: <int> }
  },
  ...
}
```

For the components, you can specify just the `<component>: <int>`
in the document, unless you are setting both the parent verbosity
level and that of the child component(s) as well:

```none
{
  verbosity: <int>,
  <component1>: <int> ,
  <component2>: {
     verbosity: <int>,
     <component3>: <int>
  }
  ...
}
```

The top-level `verbosity` field corresponds to
`systemLog.verbosity` which sets the default level for all
components. The default value of `systemLog.verbosity` is
`0`.

The components correspond to the following settings:

- `accessControl`

- `assert`

- `command`

- `control`

- `ftdc`

- `geo`

- `index`

- `network`

- `query`

- `queryStats`

- `replication`

- `replication.election`

- `replication.heartbeats`

- `replication.initialSync`

- `replication.rollback`

- `recovery`

- `sharding`

- `storage`

- `storage.journal`

- `transaction`

- `write`

Unless explicitly set, the component has the verbosity level of its
parent. For example, `storage` is the parent of
`storage.journal`. That is, if you specify a `storage` verbosity level, this level
also applies to:

- `storage.journal` components
  *unless* you specify the verbosity level for
  `storage.journal`.

- `storage.recovery` components
  *unless* you specify the verbosity level for
  `storage.recovery`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the `default verbosity
level` to `1`, the `query` to `2`, the
`storage` to `2`,
and the `storage.journal` to `1`.

```javascript
db.adminCommand( {
   setParameter: 1,
   logComponentVerbosity: {
      verbosity: 1,
      query: { verbosity: 2 },
      storage: {
         verbosity: 2,
         journal: {
            verbosity: 1
         }
      }
   }
} )
```

You can also set parameter `logComponentVerbosity` at
startup time, passing the verbosity level document as a string.

```bash
mongod --setParameter "logComponentVerbosity={command: 3}"
```

`mongosh` also provides the `db.setLogLevel()`
to set the log level for a single component. For various ways to set
the log verbosity level, see log-messages-configure-verbosity.

**`maxLogSizeKB`**

Available for both `mongod` and `mongos`.

*Type*: non-negative integer

*Default*: 10

Specifies the maximum size, in kilobytes, for an individual
attribute field in a log entry; attributes exceeding this limit are
truncated.

Truncated attribute fields print field content up to the
`maxLogSizeKB` limit and excise field content past that
limit, retaining valid JSON formatting. Log entries that contain
truncated attributes append a `truncated` object to the end of the
log entry.

See log message truncation for more
information.

A value of `0` disables truncation entirely. Negative values for
this parameter are not valid.

**Warning:**

Using a large value, or disabling truncation with a value of
`0`, may adversely affect system performance and negatively
impact database operations.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the maximum log line size to `20`
kilobytes:

```bash
mongod --setParameter maxLogSizeKB=20
```

**`profileOperationResourceConsumptionMetrics`**

Available for `mongod` only.

*Type*: boolean

*Default*: false

Flag that determines whether operations collect resource 
consumption metrics and report them in the slow query logs. 
If you enable profiling, 
these metrics are also included.

If set to `true`, running the `explain` command
returns operationMetrics when the verbosity 
is `executionStats` or higher.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`quiet`**

Available for both `mongod` and `mongos`.

Sets quiet logging mode. If
`1`, `mongod` will go into a quiet logging
mode which will not log the following events/activities:

- connection events;

- the `drop` command, the
  `dropIndexes` command, the
  `validate` command; and

- replication synchronization activities.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Consider the following example which sets the
`quiet` parameter to `1`:

```javascript
db.adminCommand( { setParameter: 1, quiet: 1 } )
```

**See also:**

`systemLog.quiet`

**`redactClientLogData`**

Available for both `mongod` and `mongos`.

*Type*: boolean

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

Configure the `mongod` or `mongos` to
redact any message accompanying a given log event before logging.
This prevents the program from writing potentially sensitive data
stored on the database to the diagnostic log. Metadata such as error
or operation codes, line numbers, and source file names are still
visible in the logs.

Use `redactClientLogData` in conjunction with
/core/security-encryption-at-rest and
/core/security-transport-encryption to assist compliance with
regulatory requirements.

To enable log redaction at startup, you can either:

- Start `mongod` with the
  `--redactClientLogData` option: 

  ```javascript
  mongod --redactClientLogData
  ```

- Set the `security.redactClientLogData` option in the 
  configuration file:

  ```yaml
  security: 
     redactClientLogData: true
     ...
  ```

You can't use the `--setParameter` 
option to set `redactClientLogData` at startup.

To enable log redaction on a running `mongod` or
`mongos`, use the following command:

```javascript
db.adminCommand( { setParameter: 1, redactClientLogData : true } )
```

**See also:**

`security.redactClientLogData`

**`redactEncryptedFields`**

**New in version:** 6.1.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: `true`

Configures `mongod` and `mongos` to redact field values
of encrypted `Binary` data from all 
log messages.

- If the `redactClientLogData` parameter or the
  `security.redactClientLogData` setting is set to `false` and
  `redactEncryptedFields` is set to `true` (the default), encrypted 
  fields are redacted from all log messages.

- If the `redactClientLogData` parameter or
  `security.redactClientLogData` setting is set to `true`,
  all fields are redacted, regardless of the `redactEncryptedFields`
  setting.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`traceExceptions`**

Available for both `mongod` and `mongos`.

Configures `mongod` to log full source code stack traces
for every database and socket C++ exception, for use with debugging.
If `true`, `mongod` will log full stack traces.

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

Consider the following example which sets the
`traceExceptions` to `true`:

```javascript
db.adminCommand( { setParameter: 1, traceExceptions: true } )
```

**See also:**

`systemLog.traceAllExceptions`

**`suppressNoTLSPeerCertificateWarning`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

By default, a `mongod` or `mongos` with
TLS/SSL enabled and
`net.ssl.allowConnectionsWithoutCertificates` : `true`
lets clients connect without providing a certificate for
validation while logging an warning. Set
`suppressNoTLSPeerCertificateWarning` to `1` or `true` to
suppress those warnings.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following operation sets `suppressNoTLSPeerCertificateWarning`
to `true`:

```bash
db.adminCommand( { setParameter: 1, suppressNoTLSPeerCertificateWarning: true} )
```

**`enableDetailedConnectionHealthMetricLogLines`**

**New in version:** 7.0

Available for both `mongod` and `mongos`. 

*Type*: boolean

*Default*: true 

Determines whether to enable specific log messages related to cluster 
connection health metrics. If 
`enableDetailedConnectionHealthMetricLogLines` is set to 
`false`, the following log messages are turned off, but MongoDB still 
collects data on the cluster connection health metrics:

| Log Message | Description |
|---|---|
| Accepted TLS connection from peer | Indicates that the server successfully parsed the peer certificate during the TLS handshake with an accepted ingress connection. |
| Ingress TLS handshake complete | Indicates that the TLS handshake with an ingress connection is complete. |
| Hello completed | Indicates that the initial connection handshake completed on an incoming client connection. MongoDB displays the log message only with the first `hello` command. |
| Auth metrics report | Specifies the completion of a step in the authentication conversation. |
| Received first command on ingress connection since session start or auth handshake | Indicates that an ingress connection received the first command that is not part of the handshake. |
| Slow network response send time | Indicates that the time spent, in milliseconds, to send the response back to the client over an ingress connection takes more time than the duration defined by the `slowMS` server parameter. |
| Completed client-side verification of OCSP request | If the peer doesn't include an OCSP (Online Certificate Status Protocol) response to the TLS handshake when an egress TLS connection is established, the server must send an OCSP request to the certificate authority. MongoDB writes this log message when the certificate authority receives the OCSP response. |
| Slow connection establishment | Indicates that the time taken to send a response back to the client over an ingress connection takes longer than the threshold specified with the `slowConnectionThresholdMillis` parameter. MongoDB also emits this log message when the connection establishment times out. |
| Operation timed out while waiting to acquire connection | Indicates that an operation timed out while waiting to acquire an egress connection. |
| Acquired connection for remote operation and completed writing to wire | Indicates that the server took one millisecond or longer to write an outgoing request on an egress connection, counting from the instant when the connection establishes. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

### Diagnostic Parameters

To facilitate analysis of the MongoDB server behavior by MongoDB
engineers, MongoDB logs server statistics to diagnostic files at
periodic intervals.

For `mongod`, the diagnostic data files are stored in the
`diagnostic.data` directory under the `mongod` instance's
`--dbpath` or `storage.dbPath`.

For `mongos`, the diagnostic data files, by default, are
stored in a directory under the `mongos` instance's
`--logpath` or `systemLog.path` directory. The diagnostic
data directory is computed by truncating the logpath's file
extension(s) and concatenating `diagnostic.data` to the remaining
name.

For example, if `mongos` has ``--logpath
/var/log/mongodb/mongos.log.201708015``, then the diagnostic data
directory is `/var/log/mongodb/mongos.diagnostic.data/` directory. To
specify a different diagnostic data directory for `mongos`,
set the `diagnosticDataCollectionDirectoryPath` parameter.

The following parameters support diagnostic data capture (FTDC):

**Note:**

The default values for the diagnostic data capture interval and the
maximum sizes are configured to provide data to MongoDB engineers
with minimal impact on performance and storage size. Typically, these
values need modification only when requested by MongoDB engineers
for specific diagnostic purposes.

**`diagnosticDataCollectionEnabled`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: true

Determines whether to enable the collecting and logging of data for
diagnostic purposes. Diagnostic logging is enabled by default.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following disables the diagnostic collection:

```bash
mongod --setParameter diagnosticDataCollectionEnabled=false
```

**`diagnosticDataCollectionDirectoryPath`**

Available for `mongos` only.

*Type*: String

**Warning:**

If Full Time Diagnostic Data Capture (FTDC) is 
disabled with `diagnosticDataCollectionEnabled` or if 
`systemLog.destination` is set to `syslog`, you must restart 
`mongos` after setting 
`diagnosticDataCollectionDirectoryPath`.

Specify the directory for the diagnostic directory for
`mongos`. If the directory does not exist,
`mongos` creates the directory.

If unspecified, the diagnostic data directory is computed by
truncating the `mongos` instance's `--logpath` or
`systemLog.path` file extension(s) and concatenating
`diagnostic.data`.

For example, if `mongos` has ``--logpath
/var/log/mongodb/mongos.log.201708015``, then the diagnostic data
directory is `/var/log/mongodb/mongos.diagnostic.data/`.

If the `mongos` cannot create the specified directory, the 
diagnostic data capture is disabled for that instance. `mongos`
may not be able to create the specified directory if a file with the same 
name already exists in the path or if the process does not have permissions 
to create the directory.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`diagnosticDataCollectionDirectorySizeMB`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 200

Specifies the maximum size, in megabytes, of the `diagnostic.data`
directory. If directory size exceeds this number, the oldest
diagnostic files in the directory are automatically deleted based on
the timestamp in the file name.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the maximum size of the directory to
`250` megabytes:

```bash
mongod --setParameter diagnosticDataCollectionDirectorySizeMB=250
```

The minimum value for
`diagnosticDataCollectionDirectorySizeMB` is `10`
megabytes. `diagnosticDataCollectionDirectorySizeMB` must
be greater than maximum diagnostic file size
`diagnosticDataCollectionFileSizeMB`.

**`diagnosticDataCollectionFileSizeMB`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10

Specifies the maximum size, in megabytes, of each diagnostic
file. If the file exceeds the maximum file size, MongoDB creates a new file.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the maximum size of each diagnostic
file to `20` megabytes:

```bash
mongod --setParameter diagnosticDataCollectionFileSizeMB=20
```

The minimum value for
`diagnosticDataCollectionFileSizeMB` is `1` megabyte.

**`diagnosticDataCollectionPeriodMillis`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 1000

Specifies the interval, in milliseconds, at which to collect
diagnostic data.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, the following sets the interval to
`5000` milliseconds or 5 seconds:

```bash
mongod --setParameter diagnosticDataCollectionPeriodMillis=5000
```

The minimum value for
`diagnosticDataCollectionPeriodMillis` is `100`
milliseconds.

### Replication and Consistency

**`abortStreamingHelloWithSmallTimeout`**

*Type*: boolean

*Default*: false

Controls how the server responds when an unauthenticated client
sends a streaming `hello` command with a
`maxAwaitTimeMS` value below the
`minWaitForStreamingHelloMillis` floor:

- When `false`, the server clamps the effective timeout up to
  `minWaitForStreamingHelloMillis`.

- When `true`, the server rejects the command and returns an
  `InvalidOptions` error.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `abortStreamingHelloWithSmallTimeout`
to `true` at startup:

```bash
mongod --setParameter abortStreamingHelloWithSmallTimeout=true
mongos --setParameter abortStreamingHelloWithSmallTimeout=true
```

The following example sets
`abortStreamingHelloWithSmallTimeout` to `true` using the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, abortStreamingHelloWithSmallTimeout: true } )
```

**`changeSyncSourceThresholdMillis`**

Available for `mongod` only.

*Type*: integer

*Default*: 5

The minimum latency improvement, in milliseconds, that a candidate
sync source
must have over the current sync source before a secondary considers
switching to it. A lower value makes secondaries more sensitive to
small latency differences, which increases the number of sync
source changes. A higher value reduces switching between candidates
with similar latency.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set `changeSyncSourceThresholdMillis` for
a `mongod` instance to `200` using the
`setParameter` command within `mongosh`:

```javascript
db.adminCommand( { setParameter: 1, changeSyncSourceThresholdMillis: 200 } )
```

**`connectTimeoutMs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10000

Sets the connection timeout,
in milliseconds, for the replica set 
monitor.

This parameter is only available at startup. If you set this parameter,
it must be greater than or equal to 500.

The following example sets `connectTimeoutMs` for a `mongod` 
instance to 700 milliseconds:

```bash
mongod --setParameter connectTimeoutMs=700
```

**`disableSplitHorizonIPCheck`**

**New in version:** 5.0.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

To configure cluster nodes for split horizon DNS, use host names
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

To allow configuration changes using IP addresses, set
`disableSplitHorizonIPCheck=true` using the command line:

```javascript
/usr/local/bin/mongod  --setParameter disableSplitHorizonIPCheck=true -f /etc/mongod.conf
```

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```javascript
setParameter:
   disableSplitHorizonIPCheck: true
```

**`enableOverrideClusterChainingSetting`**

**New in version:** 5.0.2

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

If `enableOverrideClusterChainingSetting` is `true`,
replica set secondary members can replicate data from
other secondary members even if `settings.chainingAllowed` is
`false`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the
`enableOverrideClusterChainingSetting` for a
`mongod` instance to `true`:

```bash
mongod --setParameter enableOverrideClusterChainingSetting=true
```

**`heartBeatFrequencyMs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10000

When `replicaSetMonitorProtocol` is set to `'sdam'`, 
`heartBeatFrequencyMs` determines how long, 
in milliseconds, to wait between `hello` requests.

When `replicaSetMonitorProtocol` is set to `'streamable'`, 
`heartBeatFrequencyMs` determines how long, 
in milliseconds, to wait between `hello` round trip time
(RTT) measurements. RTT measurements are used in 
server selection.

This parameter is only available at startup. If you set this
parameter, it must be greater than or equal to 500.

The following example sets `heartBeatFrequencyMs` 
in a `mongod` instance to 700 milliseconds:

```bash
mongod --setParameter heartBeatFrequencyMs=700
```

**`initialSyncIndexBuildMemoryPercentage`**

**New in version:** 7.0.26

Available for `mongod` only.

*Type*: double

*Default*: 10.0

The percentage of system memory that MongoDB allocates for index builds 
during initial sync. The amount of system 
memory used is bound by the values of 
`initialSyncIndexBuildMemoryMinMB` and 
`initialSyncIndexBuildMemoryMaxMB`.

You can specify a value between `0.0` and `80.0`, inclusive.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the `initialSyncIndexBuildMemoryPercentage`
for a `mongod` instance to 40%:

```bash
mongod --setParameter initialSyncIndexBuildMemoryPercentage=40
```

**`initialSyncIndexBuildMemoryMaxMB`**

**New in version:** 7.0.26

Available for `mongod` only.

*Type*: integer

*Default*: 16384

The maximum amount of system memory, in megabytes, that MongoDB can use for 
index builds during initial sync.

You can specify a value between `50` and `10000000`. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the `initialSyncIndexBuildMemoryMaxMB`
for a `mongod` instance to 20000 MB:

```bash
mongod --setParameter initialSyncIndexBuildMemoryMaxMB=20000
```

**`initialSyncIndexBuildMemoryMinMB`**

**New in version:** 7.0.26

Available for `mongod` only.

*Type*: Integer

*Default*: 200

The minimum amount of system memory, in megabytes, that MongoDB can use for
index builds during initial sync.

You can specify a value between `50` and `10000000`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the `initialSyncIndexBuildMemoryMinMB`
for a `mongod` instance to 60 MB:

```bash
mongod --setParameter initialSyncIndexBuildMemoryMinMB=60
```

**`localLogicalSessionTimeoutMinutes`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 30

**Warning:** For testing purposes only

This parameter is intended for testing purposes only and not for
production use.

The time in minutes that a session remains active
after its most recent use. Sessions that have not received a new
read/write operation from the client or been refreshed with
`refreshSessions` within this threshold are cleared from the
cache. State associated with an expired session may be cleaned up by the
server at any time.

This parameter applies only to the instance on which it is set. To
set this parameter on replica sets and sharded clusters, you must
specify the same value on every member; otherwise, sessions will
not function properly.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `localLogicalSessionTimeoutMinutes`
for a test `mongod` instance to 20 minutes:

```bash
mongod --setParameter localLogicalSessionTimeoutMinutes=20
```

**`localThresholdMs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 15

Defines the length of the latency window used in
server selection in
milliseconds.

This parameter is only available at startup. If you set this parameter,
it must be greater than or equal to 0.

The following example sets `localThresholdMs`
for a `mongod` instance to 20 milliseconds:

```bash
mongod --setParameter localThresholdMs=20
```

**`logicalSessionRefreshMillis`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 300000 (5 minutes)

The interval (in milliseconds) at which the cache refreshes its logical
session records against the main session store.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `logicalSessionRefreshMillis`
for a `mongod` instance to 10 minutes:

```bash
mongod --setParameter logicalSessionRefreshMillis=600000
```

**`maxAcceptableLogicalClockDriftSecs`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 31536000 (1 year)

The maximum amount by which the current cluster time can be advanced;
specifically, `maxAcceptableLogicalClockDriftSecs` is the
maximum difference between the new value of the cluster time and the
current cluster time. Cluster time is a logical time used for
ordering of operations.

You cannot advance the cluster time to a new value if the new
cluster time differs from the current cluster time by more than
`maxAcceptableLogicalClockDriftSecs`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `maxAcceptableLogicalClockDriftSecs`
for a `mongod` instance to 15 minutes:

```bash
mongod --setParameter maxAcceptableLogicalClockDriftSecs=900
```

**`maxSessions`**

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 1000000

The maximum number of sessions that can be cached.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `maxSessions`
for a `mongod` instance to 1000:

```bash
mongod --setParameter maxSessions=1000
```

**`maxSyncSourceLagSecs`**

Available for `mongod` only.

*Type*: integer

*Default*: 30

The maximum lag, in seconds, that a candidate
sync source
can have relative to the newest oplog entry on the primary and
still qualify as an eligible sync source. If a candidate's most
recent oplog entry is more than `maxSyncSourceLagSecs`
seconds behind the primary, MongoDB rejects it as a sync source.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set `maxSyncSourceLagSecs` for a
`mongod` instance to `20`:

```bash
mongod --setParameter maxSyncSourceLagSecs=20
```

**`oplogBatchDelayMillis`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 0

The number of milliseconds to delay applying batches of oplog
operations on secondary nodes. By default, `oplogBatchDelayMillis`
is `0`, meaning oplog batches are applied with no delay. When there
is no delay, MongoDB may apply frequent, small oplog batches to
secondaries.

Increasing `oplogBatchDelayMillis` causes MongoDB to apply oplog
batches less frequently on secondaries, with each batch containing
larger amounts of data. This reduces IOPS (Input/Output
Operations Per Second) on secondaries, but adds latency for writes
with write concern `"majority"`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, run the following command to set the
`oplogBatchDelayMillis` for a `mongod` instance to 20
milliseconds:

```bash
mongod --setParameter oplogBatchDelayMillis=20
```

**`periodicNoopIntervalSecs`**

Available for `mongod` only.

*Type*: integer

*Default*: 10

The duration in seconds between noop writes on each individual node.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**Note:**

To modify this value for a MongoDB Atlas cluster, you
must contact Atlas Support.

The following example sets the `periodicNoopIntervalSecs` to 1 second at 
startup:

```javascript
mongod --setParameter periodicNoopIntervalSecs=1
```

**`replicaSetMonitorProtocol`**

Available for both `mongod` and `mongos`.

*Type*: string

*Default*: "streamable"

Determines which replica set monitor protocol to use. You can set this
parameter to `"streamable"`, which is compliant with [Server Discovery and Monitoring (SDAM)](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md) 
specification and allows for constant `hello`
requests. You can also set this parameter to `"sdam"`, which is compliant
with SDAM specification.

This parameter is only available at startup. 

The following example sets
`replicaSetMonitorProtocol` to `"sdam"` on a `mongod`
instance:

```bash
mongod --setParameter replicaSetMonitorProtocol='sdam'
```

**`storeFindAndModifyImagesInSideCollection`**

**New in version:** 5.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: true

Determines whether the temporary documents required for
retryable `findAndModify`
commands are stored in the *side* collection
(`config.image_collection`).

If `storeFindAndModifyImagesInSideCollection` is:

- `true`, the temporary documents are stored in the side
  collection.

- `false`, the temporary documents are stored in the replica
  set oplog.

Keep `storeFindAndModifyImagesInSideCollection` set to
`true` if you:

- Have a large retryable
  `findAndModify` workload.

- Require more temporary document space for retryable `findAndModify` commands than is
  available in the replica set oplog.

**Note:**

Secondaries may experience increased CPU
usage when `storeFindAndModifyImagesInSideCollection`
is `true`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set
`storeFindAndModifyImagesInSideCollection` to `false`
during startup:

```bash
mongod --setParameter storeFindAndModifyImagesInSideCollection=false
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, storeFindAndModifyImagesInSideCollection: false } )
```

**`TransactionRecordMinimumLifetimeMinutes`**

Available for `mongod` only.

*Type*: integer

*Default*: 30

The minimum lifetime a transaction record exists in the
`transactions` collection before the record becomes
eligible for cleanup.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the `TransactionRecordMinimumLifetimeMinutes`
for a `mongod` instance to 20 minutes:

```bash
mongod --setParameter TransactionRecordMinimumLifetimeMinutes=20
```

**See also:**

`localLogicalSessionTimeoutMinutes`

**`enableFlowControl`**

*Type*: boolean

*Default*: true

Enables or disables the mechanism that controls the rate at which the
primary applies its writes with the goal of keeping the secondary members'
`majority committed` lag under a
configurable maximum value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`flowControlTargetLagSeconds`**

*Type*: integer

*Default*: 10

The target maximum `majority committed` lag when running
with flow control. When flow control is enabled, the mechanism
attempts to keep the `majority committed` lag under
the specified seconds. The parameter has no effect if flow control
is disabled.

The specified value must be greater than 0.

In general, the default settings should suffice; however, if
modifying from the default value, decreasing, rather than
increasing, the value may prove to be more useful.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`flowControlWarnThresholdSeconds`**

*Type*: integer

*Default*: 10

The amount of time to wait to log a warning once the flow control
mechanism detects the majority commit point has not moved.

The specified value must be greater than or equal to 0, with 0 to
disable warnings.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`initialSyncTransientErrorRetryPeriodSeconds`**

*Type*: integer

*Default*: 86400

The amount of time in seconds a secondary performing initial sync
attempts to resume the process if interrupted by a transient
network error. The default value is equivalent to 24 hours.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`initialSyncSourceReadPreference`**

Available for `mongod` only.

*Type*: String

The preferred source for performing initial sync. Specify one of the following read
preference modes:

- `primary`
- `primaryPreferred` (Default for voting replica set members)
- `secondary`
- `secondaryPreferred`
- `nearest` (Default for newly added *or* non-voting replica set members)

If the replica set has disabled `chaining`, the default
`initialSyncSourceReadPreference` read preference mode
is `primary`.

You cannot specify a tag set or `maxStalenessSeconds` to
`initialSyncSourceReadPreference`.

If the `mongod` cannot find a sync source based on the
specified read preference, it logs an error and restarts the initial
sync process. The `mongod` exits with an error if it
cannot complete the initial sync process after `10` attempts. For
more information on sync source selection, see
replica-set-initial-sync-source-selection.

`initialSyncSourceReadPreference` takes precedence over
the replica set's `settings.chainingAllowed` setting when
selecting an initial sync source. After a replica set member
successfully completes initial sync, it defers to the value of
`chainingAllowed` when selecting a replication sync
source.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`initialSyncMethod`**

**New in version:** 5.2

Available for `mongod` only.                                                            

*Type*: String                                                           

*Default*: `logical`   

Available only in MongoDB Enterprise.

Method used for initial sync.

Set to `logical` to use logical initial sync. Set to `fileCopyBased` to         
use file copy based initial sync.

This parameter only affects the sync method for the member on which
it is specified. Setting this parameter on a single replica set
member does not affect the sync method of any other replica set
members.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`maxNumSyncSourceChangesPerHour`**

**New in version:** 5.0

*Type*: integer

*Default*: 3

Sync sources
are evaluated each time a sync source is updated and each time a
node fetches a batch of oplog entries. If there are more than
`maxNumSyncSourceChangesPerHour` source changes in an hour, the
node temporarily stops re-evaluating that sync source. If this
parameter is set with a high value, the node may make unnecessary
source changes.

This parameter will not prevent a node from starting to sync from
another node if it doesn't have a sync source. The node will
re-evaluate if a sync source becomes invalid. Similarly, if the
primary changes and chaining is disabled, the node will update to
sync from the new primary.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`oplogFetcherUsesExhaust`**

Available for `mongod` only.

*Type*: boolean

*Default*: true

Enables or disables streaming replication. Set the value to `true` to enable
streaming replication.

Set the value to `false` to disable streaming replication. If
disabled, secondaries fetch batches of oplog
entries by issuing a request to their *sync from* source and waiting for a
response. This requires a network roundtrip for each batch of oplog entries.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`oplogInitialFindMaxSeconds`**

Available for `mongod` only.

*Type*: integer

*Default*: 60

Maximum time in seconds for a member of a replica set to wait
for the `find` command to finish during
data synchronization.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`replWriterThreadCount`**

Available for `mongod` only.

*Type*: integer

*Default*: 16

Maximum number of threads to use to apply replicated operations in
parallel. Values can range from 1 to 256 inclusive. However, the
maximum number of threads used is capped at twice the number of
available cores.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

`replWriterMinThreadCount`

**`replWriterMinThreadCount`**

**New in version:** 5.0

Available for `mongod` only.

*Type*: integer

*Default*: 0

Minimum number of threads to use to apply replicated operations in
parallel. Values can range from 0 to 256 inclusive. You can only set
`replWriterMinThreadCount` at startup and cannot change
this setting with the `setParameter` command.

Parallel application of replication operations uses up to
`replWriterThreadCount` threads. If
`replWriterMinThreadCount` is configured with a value
less than `replWriterThreadCount`, the thread pool will
timeout idle threads until the total count of threads in the thread
pool is equal to `replWriterMinThreadCount`.

`replWriterMinThreadCount` must be configured with a value
that is less than or equal to `replWriterThreadCount`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`rollbackTimeLimitSecs`**

*Type*: 64-bit integer

*Default*: 86400  (1 day)

Maximum age of data that can be rolled back. Negative values for
this parameter are not valid.

If the time between the end
of the to-be-rolledback instance's oplog and the first operation
after the common point (the last point where the source node and the
to-be-rolledback node had the same data) exceeds this value, the
rollback will fail.

To effectively have an unlimited rollback period, set the value to
`2147483647` which is the maximum value allowed and equivalent to
roughly 68 years.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`waitForSecondaryBeforeNoopWriteMS`**

Available for `mongod` only.

*Type*: integer

*Default*: 10

The length of time (in milliseconds) that a secondary must wait if
the `afterClusterTime` is greater than the last applied time from
the oplog. After the `waitForSecondaryBeforeNoopWriteMS` passes,
if the `afterClusterTime` is still greater than the last applied
time, the secondary makes a no-op write to advance the last applied
time.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the
`waitForSecondaryBeforeNoopWriteMS` to 20 milliseconds:

```bash
mongod --setParameter waitForSecondaryBeforeNoopWriteMS=20
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, waitForSecondaryBeforeNoopWriteMS: 20 } )
```

**`createRollbackDataFiles`**

Available for `mongod` only.

*Type*: boolean

*Default*: true

Flag that determines whether MongoDB creates rollback files that contains documents affected during a
rollback.

By default, `createRollbackDataFiles` is `true` and
MongoDB creates the rollback files.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `createRollbackDataFiles`
to false so that the rollback files are not created:

```javascript
mongod --setParameter createRollbackDataFiles=false
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, createRollbackDataFiles: false } )
```

For more information, see rollback-data-files.

**`replBatchLimitBytes`**

*Default*: 104857600 (100MB)

Sets the maximum oplog application batch size in bytes.

Values can range from 16777216 (16MB) to 104857600 (100MB) inclusive.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `replBatchLimitBytes`
to 64 MB to limit the oplog application batch size:

```javascript
mongod --setParameter replBatchLimitBytes=67108864
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, replBatchLimitBytes: 64 * 1024 * 1024 } )
```

**`minWaitForStreamingHelloMillis`**

*Type*: integer

*Default*: 500

Specifies the minimum effective timeout, in milliseconds, that the
server enforces for streaming `hello` commands sent by
unauthenticated clients. If an
unauthenticated client supplies a `maxAwaitTimeMS` value below
this floor, the server either clamps the timeout up to this value
or rejects the command, depending on
`abortStreamingHelloWithSmallTimeout`.

This parameter mitigates excessive CPU use from unauthenticated
clients that send streaming `hello` commands with very small
`maxAwaitTimeMS` values.

The value must be greater than or equal to `0`. A value of `0`
disables enforcement. Authenticated clients are not affected, and
topology changes still wake waiting clients immediately regardless
of this parameter.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `minWaitForStreamingHelloMillis` to
`1000` milliseconds at startup:

```bash
mongod --setParameter minWaitForStreamingHelloMillis=1000
mongos --setParameter minWaitForStreamingHelloMillis=1000
```

The following example sets `minWaitForStreamingHelloMillis` to
`1000` milliseconds using the `setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, minWaitForStreamingHelloMillis: 1000 } )
```

**`mirrorReads`**

Available for `mongod` only.

*Type*: Document

*Default*: `{ samplingRate: 0.01, maxTimeMS: 1000 }`

Specifies the settings for mirrored reads
for the `mongod` instance. The settings only take
effect when the member is a primary.

The parameter `mirrorReads` takes a JSON document with
the following fields:

* - Field
  - Description

* - `samplingRate`

  - The sampling rate used to mirror a subset of operations
    that support mirroring
    to a subset of electable (specifically,  `priority
    greater than 0`) secondaries. That is,
    the primary mirrors reads to each electable secondary at the
    specified sampling rate.

    Valid values are:

    |  |  |
    |---|---|
    | `0.0` | Turns off mirroring. |
    | `1.0` | The primary mirrors all operations that supports mirroring to each electable secondary. |
    | Number between `0.0` and `1.0` (exclusive) | The primary randomly samples each electable secondary at the specified rate to be sent mirrored reads. |

    For example, given a replica set with a primary and two
    electable secondaries and a sampling rate of `0.10`, the
    primary mirrors reads to each electable secondary at the
    sampling rate of 10 percent such that one read may be
    mirrored to one secondary and not to the other or to both or
    to neither. That is, if the primary receives `100`
    operations that can be mirrored, the sampling rate of
    `0.10` may result in `8` reads being mirrored to one
    secondary and `13` reads to the other or `10` to each,
    etc.

    The default value is `0.01`.

* - `maxTimeMS`

  - The maximum time in milliseconds for the mirrored reads. The
    default value is `1000`.

    The `maxTimeMS` for the mirrored reads is separate from the
    `maxTimeMS` of the original read being mirrored.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

If you specify from the configuration file or on the command
line, **enclose the** `mirrorReads` **document in quotes**.

For example, the following sets the mirror reads sampling rate to
`0.10` from the command line:

```bash
mongod --setParameter mirrorReads='{ samplingRate: 0.10 }'
```

Or, to specify in a configuration file:

```yaml
setParameter:
   mirrorReads: '{samplingRate: 0.10}'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongod`, do **not** enclose the document in quotes:

```javascript
db.adminCommand( { setParameter: 1, mirrorReads: { samplingRate: 0.10 } } )
```

**`allowMultipleArbiters`**

**New in version:** 5.3

Available for `mongod` only.

*Type*: boolean

*Default*: false

Specifies whether the replica set allows the use of multiple arbiters.

The use of multiple arbiters is not recommended:

- Multiple arbiters prevent the reliable use of the majority write concern.
  MongoDB counts arbiters in calculating a membership majority, but arbiters
  do not store data. With the inclusion of multiple arbiters, it's possible
  for a majority write operation to return success before the write replicates
  to a majority of data bearing nodes.

- Multiple arbiters allow replica sets to accept writes even when the
  replica set doesn't have sufficient secondaries for data replication.

For more information, see
Concerns with Multiple Arbiters.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter allowMultipleArbiters=true
```

### Sharding Parameters

**`analyzeShardKeyCharacteristicsDefaultSampleSize`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 10000000

If `sampleRate` and `sampleSize` are not set when 
you run `analyzeShardKey`, specifies the number of documents to 
sample when calculating shard key characteristics metrics. Must be 
greater than `0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `analyzeShardKeyCharacteristicsDefaultSampleSize` 
to `10000` at startup:

```bash
mongod --setParameter analyzeShardKeyCharacteristicsDefaultSampleSize=10000
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, analyzeShardKeyCharacteristicsDefaultSampleSize: 10000 } )
```

**`analyzeShardKeyNumMostCommonValues`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 5

Specifies the number of most common shard key values to return. If
the collection contains fewer unique shard keys than this value, 
`analyzeShardKeyNumMostCommonValues` returns that number of 
most common values. Must be greater than `0` and less than or equal 
to `1000`. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `analyzeShardKeyNumMostCommonValues` 
to `3` at startup:

```bash
mongod --setParameter analyzeShardKeyNumMostCommonValues=3
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, analyzeShardKeyNumMostCommonValues: 3 } )
```

**`analyzeShardKeyNumRanges`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 100

Specifies the number of ranges to partition the shard key space into 
when calculating the hotness of shard key 
ranges. Must be greater than `0` and less than or equal to 
`10000`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `analyzeShardKeyNumRanges` to `50` at startup:

```bash
mongod --setParameter analyzeShardKeyNumRanges=50
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, analyzeShardKeyNumRanges: 50 } )
```

**`analyzeShardKeyMonotonicityCorrelationCoefficientThreshold`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: double

*Default*: 0.7

Specifies the `RecordId` correlation coefficient threshold used to 
determine if a shard key is monotonically changing in insertion order. 
Must be greater than `0` and less than or equal to `1`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets 
`analyzeShardKeyMonotonicityCorrelationCoefficientThreshold` to 
`1` at startup:

```bash
mongod --setParameter analyzeShardKeyMonotonicityCorrelationCoefficientThreshold=1
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, analyzeShardKeyMonotonicityCorrelationCoefficientThreshold: 1 } )
```

**`analyzeShardKeyNumSamplesPerRange`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: Non-negative integer

*Default*: 10

The number of documents to sample per shard key range. 
Must be a value greater than zero and less than or equal to `10000`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `analyzeShardKeyNumSamplesPerRange` to `50` at startup:

```bash
mongod --setParameter analyzeShardKeyNumSamplesPerRange=50
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, analyzeShardKeyNumSamplesPerRange: 50 } )
```

**`autoMergerIntervalSecs`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 3600

When AutoMerger is enabled, specifies the amount of time
between automerging rounds, in seconds. The default value 
is 3600 seconds, or one hour. 

`autoMergerIntervalSecs` can only be set on config servers.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `autoMergerIntervalSecs` to 7200 seconds, 
or two hours, at startup:

```bash
mongod --setParameter autoMergerIntervalSecs=7200
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, autoMergerIntervalSecs: 7200 } )
```

**`autoMergerThrottlingMS`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 15000

When AutoMerger is enabled, specifies the minimum amount 
time between merges initiated by the AutoMerger on the same 
collection, in milliseconds. 

`autoMergerThrottlingMS` can only be set on config servers.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `autoMergerThrottlingMS` to 60000 milliseconds, 
or one minute, at startup:

```bash
mongod --setParameter autoMergerThrottlingMS=60000
```

During run time, you can set or modify the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, autoMergerThrottlingMS: 60000 } )
```

**`balancerMigrationsThrottlingMs`**

**New in version:** 7.0 (*Also available starting in 6.3.1, 6.0.6, 5.0.18*)

Available for `mongod` only.

*Type*: integer

*Default*: 1000

Specifies the minimum amount of time between two consecutive 
balancing rounds. This allows you to throttle the balancing
rate. This parameter only takes effect on config server nodes.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `balancerMigrationsThrottlingMs` to 2000 
milliseconds at startup:

```bash
mongod --setParameter balancerMigrationsThrottlingMs=2000
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, balancerMigrationsThrottlingMs: 2000 } )
```

**`catalogCacheCollectionMaxEntries`**

**New in version:** 7.0.22

*Type*: integer

*Default*: 10000

Available for both `mongod` and `mongos`.

Maximum number of entries allowed in the catalog cache for
collections.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`catalogCacheDatabaseMaxEntries`**

**New in version:** 7.0.22

*Type*: integer

*Default*: 10000

Available for both `mongod` and `mongos`.

Maximum number of entries allowed in the catalog cache for
databases.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`catalogCacheIndexMaxEntries`**

**New in version:** 7.0.22

*Type*: integer

*Default*: 10000

Available for both `mongod` and `mongos`.

Maximum number of entries allowed in the catalog cache for
indexes.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`chunkDefragmentationThrottlingMS`**

**New in version:** 5.3

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 1000

Specifies the minimum time period (in milliseconds) between
consecutive split and merge commands run by the balancer when
the chunks in a sharded collection
are defragmented. `chunkDefragmentationThrottlingMS`
limits the rate of split and merge commands.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`chunkDefragmentationThrottlingMS` to `10` milliseconds:

```bash
mongod --setParameter chunkDefragmentationThrottlingMS=10
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, chunkDefragmentationThrottlingMS: 10 } )
```

**`directConnectionChecksWithSingleShard`**

**New in version:** 7.0.12

Available for `mongod` only.

*Type*: boolean

*Default*: false

When set on a sharded cluster with a single shard, enables direct connection
warnings. If a user connects directly to the single-shard cluster, `mongod`
logs a warning every hour and
updates `shardingStatistics.unauthorizedDirectShardOps` with
unauthorized direct shard operations.

To avoid this, users should connect to single-shard clusters through a
router, like `mongos`. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

**`disableResumableRangeDeleter`**

Available for `mongod` only.

*Type*: boolean

*Default*: false

If set on a shard's primary, specifies if range deletion is paused on
the shard. If set to `true`, cleanup of ranges
containing orphaned documents is paused.
The shard can continue to donate chunks to other shards, but the
donated documents will not be removed from this shard until you set
this parameter to `false`. This shard can continue to receive
chunks from other shards as long as it does not have a pending range
deletion task in the `config.rangeDeletions` collection that
overlaps with the incoming chunk's range.

When `disableResumableRangeDeleter` is `true`, chunk
migrations fail if orphaned documents
exist on the recipient shard's primary in the same range as the
incoming chunks.

The parameter has no effect on the `mongod` if it is not
the shard's primary.

**Important:**

If you set `disableResumableRangeDeleter` parameter to
`true`, ensure that you apply it consistently for all members in
the shard's replica set. In the event of a failover, this
setting's value on the new primary dictates the behavior of the
range deleter.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```javascript
mongod --setParameter disableResumableRangeDeleter=false
```

**`enableShardedIndexConsistencyCheck`**

Available for `mongod` only.

*Type*: boolean

*Default*: true

If set on the config server's primary, enables or disables the index
consistency check for sharded collections. The parameter has no
effect on the `mongod` if it is not the config server's
primary.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`enableShardedIndexConsistencyCheck` to `false` for a
config server primary:

```javascript
mongod --setParameter enableShardedIndexConsistencyCheck=false
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, enableShardedIndexConsistencyCheck: false } )
```

**See also:**

- `shardedIndexConsistencyCheckIntervalMS` parameter
- `shardedIndexConsistency` metrics returned by the
  `serverStatus` command.

**`opportunisticSecondaryTargeting`**

**New in version:** 6.1.0

Available for `mongos` only.

*Type*: boolean

*Default*: `false`

Determines whether `mongos` performs opportunistic reads against
replica sets.

When this parameter is set to `true`, `mongos` directs secondary 
reads to secondaries with active connections. It sends the request to the 
first secondary that accepts the connection. When this parameter is set to 
`false`, `mongos` holds secondary reads until it can establish 
a connection to a specific secondary, (except in the case of 
hedged reads).

**Note:**

Under certain workloads, opportunistic reads may trigger the 
opening of unnecessary connections from `mongos` to 
`mongod` and reduce overall performance. 
This parameter should not be enabled unless your application has 
a specific need for the feature.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set `opportunisticSecondaryTargeting` during startup:

```bash
mongos --setParameter opportunisticSecondaryTargeting=true
```

**`shardedIndexConsistencyCheckIntervalMS`**

Available for `mongod` only.

*Type*: integer

*Default*: 600000

If set on the config server's primary, the interval, in
milliseconds, at which the config server's primary checks the index
consistency of sharded collections. The parameter has no effect on
the `mongod` if it is not the config server's primary.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following sets the interval at 300000 milliseconds
(5 minutes) at startup:

```javascript
mongod --setParameter shardedIndexConsistencyCheckIntervalMS=300000
```

**See also:**

- `enableShardedIndexConsistencyCheck` parameter
- `shardedIndexConsistency` metrics returned by the
  `serverStatus` commandq

**`enableFinerGrainedCatalogCacheRefresh`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: true

This parameter allows the catalog cache to be refreshed only if the
shard needs to be refreshed. If disabled, any stale chunk will cause
the entire chunk distribution for a collection to be considered stale
and force all routers who
contact the shard to refresh their shard catalog cache.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter enableFinerGrainedCatalogCacheRefresh=true
mongos --setParameter enableFinerGrainedCatalogCacheRefresh=true
```

**See also:**

- sharding-background
- `shardingStatistics.catalogCache`

**`maxTimeMSForHedgedReads`**

Available for `mongos` only.

*Type*: integer

*Default*: 150

Specifies the maximum time limit (in milliseconds) for the
hedged read. That is, the additional
read sent to hedge the read operation uses the `maxTimeMS` value
of `maxTimeMSForHedgedReads` while the read operation
that is being hedged uses the `maxTimeMS` value specified for the
operation.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the limit to 200 milliseconds, you can issue the
following during startup:

```bash
mongos --setParameter maxTimeMSForHedgedReads=200
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( { setParameter: 1, maxTimeMSForHedgedReads: 200 } )
```

**See also:**

- `readHedgingMode`
- mongos-hedged-reads

**`maxCatchUpPercentageBeforeBlockingWrites`**

**New in version:** 5.0

Available for `mongod` only.

*Type*: integer

*Default*: 10

For `moveChunk` and `moveRange` operations, 
specifies the maximum percentage of untrasferred data allowed by the 
migration protocol (expressed in percentage of the total chunk size) 
to transition from the `catchup` phase to the `commit` phase.

Setting a higher catchup percentage can decrease the amount of time
it takes for the migration to complete at the cost of increased
latency during concurrent `upsert`
and `delete` operations.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

Starting in MongoDB 7.1 (and 7.0.1), you can set the parameter during
runtime.

For example, to set the maximum percentage to 20, you can issue the
following during startup:

```bash
mongod --setParameter maxCatchUpPercentageBeforeBlockingWrites=20
```

Starting in MongoDB 7.1 (and 7.0.1), you can 
set the parameter during runtime with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, maxCatchUpPercentageBeforeBlockingWrites: 20} )
```

**See also:**

[Live Migration Protocol](https://github.com/mongodb/mongo/blob/master/src/mongo/db/s/README.md#the-live-migration-protocol)

**`metadataRefreshInTransactionMaxWaitBehindCritSecMS`**

**New in version:** 5.2 (*Also available starting in 5.1.0, 5.0.4*)

Available for `mongod` only.

*Type*: integer

*Default*: 500

Limits the time a shard waits for a critical section within a
transaction. 

When a query accesses a shard, a chunk migration or DDL operation may already hold the critical
section for the collection. If the query finds the critical
section is taken, the shard waits until the critical section has
been released. When the shard returns control to `mongos`,
`mongos` retries the query. However, if a multi-shard
transaction interacts with an operation that takes the critical
section on multiple shards, the interaction can result in a
distributed deadlock.

`metadataRefreshInTransactionMaxWaitBehindCritSecMS`
limits the maximum time a shard waits within a transaction for the
critical section to be released.

To reduce the maximum wait time for the critical section within a
transaction, lower the value of
`metadataRefreshInTransactionMaxWaitBehindCritSecMS`. 

**Warning:**

If `metadataRefreshInTransactionMaxWaitBehindCritSecMS`
is too low, `mongos` could use all of its retry attempts
and return an error.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set `metadataRefreshInTransactionMaxWaitBehindCritSecMS`
to 400 milliseconds:

```javascript
db.adminCommand( { setParameter: 1, metadataRefreshInTransactionMaxWaitBehindCritSecMS: 400 } )
```

**`queryAnalysisSamplerConfigurationRefreshSecs`**

**New in version:** 7.0

**Changed in version:** 7.0.1

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 10

Interval that a sampler (`mongos` or `mongod`) refreshes its 
query analyzer sample rates. 

The sample rate configured by the `configureQueryAnalyzer` 
command is divided among `mongos` instances in the sharded cluster 
or `mongod` instances in the replica set based on the traffic going 
through them. To make the sample rate assignment for a `mongos` or 
`mongod` more responsive to the traffic going through it, decrease
this value. 

We recommend using the default value. 

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

Starting in MongoDB 7.0.1, you can set
`queryAnalysisSamplerConfigurationRefreshSecs` during run time. 

This example sets `queryAnalysisSamplerConfigurationRefreshSecs` to 
60 seconds at startup on a `mongod` instance:

```bash
mongod --setParameter queryAnalysisSamplerConfigurationRefreshSecs=60
```

This example sets `queryAnalysisSamplerConfigurationRefreshSecs` to 
60 seconds at startup on a `mongos` instance:

```bash
mongos --setParameter queryAnalysisSamplerConfigurationRefreshSecs=60
```

To set the value to 30 seconds, run the following:

```javascript
db.adminCommand( { setParameter: 1, queryAnalysisSamplerConfigurationRefreshSecs: 30 } )
```

**`queryAnalysisWriterIntervalSecs`**

**New in version:** 7.0

**Changed in version:** 7.0.1

Available for `mongod` only.

*Type*: integer

*Default*: 90

Interval that sampled queries are written to disk, in seconds.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

Starting in MongoDB 7.0.1, you can set
`queryAnalysisWriterIntervalSecs` during run time. 

This example sets `queryAnalysisWriterIntervalSecs` to 
60 seconds at startup on a `mongod` instance:

```bash
mongod --setParameter queryAnalysisWriterIntervalSecs=60
```

To set the value to 60 seconds, run the following:

```javascript
db.adminCommand( { setParameter: 1, queryAnalysisWriterIntervalSecs: 60 } )
```

**`queryAnalysisWriterMaxMemoryUsageBytes`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 100 * 1024 * 1024

Maximum amount of memory in bytes that the query sampling writer is 
allowed to use. Once the limit is reached, all new queries and diffs 
are discarded from sampling until the buffer is flushed. Must be 
greater than `0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `queryAnalysisWriterMaxMemoryUsageBytes` to 
`10000000` at startup on a `mongod` instance:

```bash
mongod --setParameter queryAnalysisWriterMaxMemoryUsageBytes=10000000
```

**`queryAnalysisWriterMaxBatchSize`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 100000

Maximum number of sampled queries to write to disk at once. Must be
greater than `0` and less than or equal to `100000`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `queryAnalysisWriterMaxBatchSize` to 
`1000` at startup on a `mongod` instance:

```bash
mongod --setParameter queryAnalysisWriterMaxBatchSize=1000
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, queryAnalysisWriterMaxBatchSize: 1000 } )
```

**`queryAnalysisSampleExpirationSecs`**

**New in version:** 7.0

Available for `mongod` only.

*Type*: integer

*Default*: 7 * 24 * 3600 

Amount of time that a sampled query document exists before 
being removed by the TTL monitor, in seconds. Must be greater
than `0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

This example sets `queryAnalysisSampleExpirationSecs` to 
`691200` (`8 * 24 * 3600`) at startup on a `mongod` instance:

```bash
mongod --setParameter queryAnalysisSampleExpirationSecs=691200
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, queryAnalysisSampleExpirationSecs: 691200 } )
```

**`readHedgingMode`**

Available for `mongos` only.

*Type*: string

*Default*: on

Specifies whether `mongos` supports hedged reads for
those read operations whose read preference have enabled the hedged read option.

Available values are:

| Value | Description |
|---|---|
| `on` | The `mongos` instance supports hedged reads for read operations whose read preference have enabled the hedged read option. |
| `off` | The `mongos` instance does not support hedged reads. That is, hedged reads are unavailable, even for read operations whose read preference have enabled the hedged read option. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to turn off hedged read support for a
`mongos` instance, you can issue the following during
startup:

```bash
mongos --setParameter readHedgingMode=off
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( { setParameter: 1, readHedgingMode: "off" } )
```

**See also:**

- mongos-hedged-reads
- `maxTimeMSForHedgedReads`

**`routingTableCacheChunkBucketSize`**

**New in version:** 7.0.1

Available for both `mongod` and `mongos`.

*Type*: integer

*Default*: 500

Specifies the size of the routing table cache buckets used to 
implement chunk grouping optimization. Must be greater than or equal 
to `0`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, to set the cache chunk bucket size to `250` on a 
`mongod`, issue the following command at startup:

```bash
mongod --setParameter routingTableCacheChunkBucketSize=250
```

**`shutdownTimeoutMillisForSignaledShutdown`**

**New in version:** 5.0

Available for `mongod` only.

*Type*: integer

*Default*: 15000

Specifies the time (in milliseconds) to wait for any ongoing database
operations to complete before initiating a shutdown of
`mongod` in response to a `SIGTERM` signal.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the time to 250 milliseconds, you can issue the
following during startup:

```bash
mongod --setParameter shutdownTimeoutMillisForSignaledShutdown=250
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongod`:

```javascript
db.adminCommand( { setParameter: 1, shutdownTimeoutMillisForSignaledShutdown: 250 } )
```

**`mongosShutdownTimeoutMillisForSignaledShutdown`**

**New in version:** 5.0

Available for `mongos` only.

*Type*: integer

*Default*: 15000

Specifies the time (in milliseconds) to wait for any ongoing database
operations to complete before initiating a shutdown of
`mongos` in response to a `SIGTERM` signal.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the time to 250 milliseconds, you can issue the
following during startup:

```bash
mongos --setParameter mongosShutdownTimeoutMillisForSignaledShutdown=250
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( { setParameter: 1, mongosShutdownTimeoutMillisForSignaledShutdown: 250 } )
```

**`ShardingTaskExecutorPoolHostTimeoutMS`**

Available for both `mongod` and `mongos`.

Type: integer

Default: 300000 (5 minutes)

Maximum time that `mongos` goes without communication to a
host before `mongos` drops all connections to the host.

If set, `ShardingTaskExecutorPoolHostTimeoutMS` should be
greater than the sum of
`ShardingTaskExecutorPoolRefreshRequirementMS` and
`ShardingTaskExecutorPoolRefreshTimeoutMS`. Otherwise,
`mongos` adjusts the value of
`ShardingTaskExecutorPoolHostTimeoutMS` to be greater than the
sum.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`ShardingTaskExecutorPoolHostTimeoutMS` to `120000`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolHostTimeoutMS=120000
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolHostTimeoutMS: 120000 } )
```

**`ShardingTaskExecutorPoolMaxConnecting`**

Available for both `mongod` and `mongos`.

Type: integer

Default: 2

Maximum number of simultaneous initiating connections (including
pending connections in setup/refresh state) each TaskExecutor
connection pool can have to a `mongod` instance. You can
set this parameter to control the rate at which `mongos`
adds connections to a `mongod` instance.

If set, `ShardingTaskExecutorPoolMaxConnecting` should be
less than or equal to `ShardingTaskExecutorPoolMaxSize`.
If it is greater, `mongos` ignores the
`ShardingTaskExecutorPoolMaxConnecting` value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`ShardingTaskExecutorPoolMaxConnecting` to `20`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolMaxConnecting=20
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMaxConnecting: 20 } )
```

**`ShardingTaskExecutorPoolMaxSize`**

Available for both `mongod` and `mongos`.

Type: integer

Default:

- On-prem deployments: `32767` for both `mongos` and
  `mongod`
- MongoDB Atlas:

  - `250` for `mongos` routers
  - `32767` for `mongod` instances

**Note:**

While the maximum configurable value is 2`64` - 1, the
defaults for both on-premises and MongoDB Atlas deployments
are significantly lower to optimize performance and resource
usage.

Maximum number of outbound connections each TaskExecutor connection
pool can open to any given `mongod` instance. The maximum
possible connections to any given host across all TaskExecutor pools
is:

```none
ShardingTaskExecutorPoolMaxSize * taskExecutorPoolSize
```

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`ShardingTaskExecutorPoolMaxSize` to `20`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolMaxSize=20
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMaxSize: 20 } )
```

`mongos` can have up to `n` TaskExecutor connection
pools, where `n` is the number of cores. See
`taskExecutorPoolSize`.

**See also:**

`ShardingTaskExecutorPoolMinSize`

**`ShardingTaskExecutorPoolMaxSizeForConfigServers`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

Type: integer

Default: -1

Optional override for `ShardingTaskExecutorPoolMinSize` to set the minimum number
of outbound connections each TaskExecutor connection pool can open to a
configuration server.

When set to:

- `-1`, `ShardingTaskExecutorPoolMinSize` is used. This is the default.

- an integer value greater than `-1`, overrides the
  minimum number of outbound connections each TaskExecutor
  connection pool can open to a configuration server.

Parameter only applies to sharded deployments.

The following example sets `ShardingTaskExecutorPoolMinSize` to `2` during startup, which
sets the minimum number of outbound connections each
TaskExecutor connection pool can open to a configuration server to
`2`:

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongos --setParameter ShardingTaskExecutorPoolMaxSizeForConfigServers=2
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMaxSizeForConfigServers: 2 } )
```

**`ShardingTaskExecutorPoolMinSize`**

Available for both `mongod` and `mongos`.

Type: integer

Default: 1

Minimum number of outbound connections each TaskExecutor connection
pool can open to any given `mongod` instance.

`ShardingTaskExecutorPoolMinSize` connections are created the
first time a connection to a new host is requested from the pool.
While the pool is idle, the pool maintains this number of
connections until `ShardingTaskExecutorPoolHostTimeoutMS`
milliseconds pass without any application using that pool.

For a `mongos` using the
`warmMinConnectionsInShardingTaskExecutorPoolOnStartup`
parameter, the `ShardingTaskExecutorPoolMinSize` parameter also
controls how many connections to each shard host are established on
startup of the `mongos` instance before it begins
accepting incoming client connections.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`ShardingTaskExecutorPoolMinSize` to `2`
during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolMinSize=2
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMinSize: 2 } )
```

`mongos` can have up to `n` TaskExecutor connection
pools, where `n` is the number of cores. See
`taskExecutorPoolSize`.

**See also:**

- `ShardingTaskExecutorPoolMaxSize`
- `warmMinConnectionsInShardingTaskExecutorPoolOnStartup`

**`ShardingTaskExecutorPoolMinSizeForConfigServers`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

Type: integer

Default: -1

Optional override for `ShardingTaskExecutorPoolMinSize` to set the minimum number
of outbound connections each TaskExecutor connection pool can open to a
configuration server.

When set to:

- `-1`, `ShardingTaskExecutorPoolMinSize` is used. This is the default.

- an integer value greater than `-1`, overrides the
  minimum number of outbound connections each TaskExecutor
  connection pool can open to a configuration server.

Parameter only applies to sharded deployments.

The following example sets `ShardingTaskExecutorPoolMinSize` to `2` during startup, which
sets the minimum number of outbound connections each
TaskExecutor connection pool can open to a configuration server to
`2`:

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongos --setParameter ShardingTaskExecutorPoolMinSizeForConfigServers=2
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolMinSizeForConfigServers: 2 } )
```

**`ShardingTaskExecutorPoolRefreshRequirementMS`**

Available for both `mongod` and `mongos`.

Type: integer

Default: 60000 (1 minute)

Maximum time the `mongos` waits before attempting to
heartbeat an idle connection in the pool. An idle connection may be 
discarded during the refresh if the pool is above its 
minimum size. 

If set, `ShardingTaskExecutorPoolRefreshRequirementMS` should be
greater than `ShardingTaskExecutorPoolRefreshTimeoutMS`.
Otherwise, `mongos` adjusts the value of
`ShardingTaskExecutorPoolRefreshTimeoutMS` to be less than
`ShardingTaskExecutorPoolRefreshRequirementMS`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`ShardingTaskExecutorPoolRefreshRequirementMS` to
`90000` during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolRefreshRequirementMS=90000
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolRefreshRequirementMS: 90000 } )
```

**`ShardingTaskExecutorPoolRefreshTimeoutMS`**

Available for both `mongod` and `mongos`.

Type: integer

Default: 20000 (20 seconds)

Maximum time the `mongos` waits for a heartbeat before
timing out the heartbeat.

If set, `ShardingTaskExecutorPoolRefreshTimeoutMS` should be
less than `ShardingTaskExecutorPoolRefreshRequirementMS`.
Otherwise, `mongos` adjusts the value of
`ShardingTaskExecutorPoolRefreshTimeoutMS` to be less than
`ShardingTaskExecutorPoolRefreshRequirementMS`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`ShardingTaskExecutorPoolRefreshTimeoutMS` to
`30000` during startup:

```bash
mongos --setParameter ShardingTaskExecutorPoolRefreshTimeoutMS=30000
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, ShardingTaskExecutorPoolRefreshTimeoutMS: 30000 } )
```

**`ShardingTaskExecutorPoolReplicaSetMatching`**

**Changed in version:** 5.0

Available for both `mongod` and `mongos`.

Type: string

Default: "automatic"

On a `mongos` instance, this parameter sets the policy
that determines the minimum size limit of its connection pools to
nodes within replica sets.

On a `mongod` instance, this parameter sets the policy
that determines the minimum size limit of its connection pools to
nodes within *other* replica sets.

Note that this parameter only manages connections for operations that
are directly related to user requests and CRUD operations.

Available values are:

| Matching Policy | Description |
|---|---|
| `"automatic"` (Default) | Starting in 5.0, `"automatic"` is the new default value. When set for a `mongos`, the instance follows the behavior specified for the `"matchPrimaryNode"` option. When set for a `mongod`, the instance follows the behavior specified for the `"disabled"` option. WARNING: If the `ShardingTaskExecutorPoolReplicaSetMatching` is set to `"automatic"`, the `replicaSetMatchingStrategy` still describes the actual policy being used, not `"automatic"`. To find the value of the `ShardingTaskExecutorPoolReplicaSetMatching`, use `getParameter` which returns the value of the server parameter. |
| `"matchPrimaryNode"` | When set for a `mongos`, the minimum size limit of the instance's connection pool to each secondary of a replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the size of its connection pool to that replica set's primary. When set for a `mongod`, the minimum size limit of the instance's connection pool to each secondary of another replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the size of its connection pool to that replica set's primary. WARNING: If multiple shard servers in your topology can experience a rapid influx of cross-shard operations, do not set this option on your `mongod` instances. In case of a primary stepdown, `matchPrimaryNode` ensures that any secondary that becomes the primary can handle the current level of primary reads and writes. |
| `"matchBusiestNode"` | When set for a `mongos`, the instance's minimum size limit of the connection pool to each member of a replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the largest among the active connection counts to the primary and each secondary member of that replica set. When set for a `mongod`, the instance's minimum size limit of the connection pool to each member of another replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the largest among the active connection counts to the primary and each secondary member of that replica set. With `"matchBusiestNode"`, `mongos` maintains enough connections to each secondary to handle the current level of primary and secondary reads and writes. The number of connections to maintain in the pool decreases as the number of active connections decreases. |
| `"disabled"` | When set for a `mongos`, the instance's minimum number of connections in the instance's connection pool to each node of a replica set in the sharded clusterv (specifically, shard replica set and config servers) is equal to the `ShardingTaskExecutorPoolMinSize`. When set for a `mongod`, the instance's minimum number of connections in the instance's connection pool to each node of another replica set in the sharded cluster (specifically, shard replica set and config servers) is equal to the `ShardingTaskExecutorPoolMinSize`. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the
`ShardingTaskExecutorPoolReplicaSetMatching` to
`"automatic"` during startup:

```bash
mongod --setParameter ShardingTaskExecutorPoolReplicaSetMatching="automatic"
```

During run time, you can also set the parameter with the
`setParameter` command:

```javascript
db.adminCommand( { setParameter: 1,  ShardingTaskExecutorPoolReplicaSetMatching: "automatic" } )
```

**`taskExecutorPoolSize`**

Available for `mongos` only.

Type: integer

Default: 1

The number of Task Executor connection pools to use for a given
`mongos`.

If the parameter value is `0` or less, the number of Task Executor
connection pools is the number of cores with the following
exceptions:

- If the number of cores is less than 4, the number of Task Executor
  connection pools is 4.

- If the number of cores is greater than 64, the number of Task
  Executor connection pools is 64.

The default value of `taskExecutorPoolSize` is `1`:

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

```bash
mongos --setParameter taskExecutorPoolSize=6
```

**See also:**

- `ShardingTaskExecutorPoolMaxSize`
- `ShardingTaskExecutorPoolMinSize`

**`loadRoutingTableOnStartup`**

Available for `mongos` only.

Type: boolean

*Default*: true

Configures a `mongos` instance to preload the routing
table for a sharded cluster on startup. With this setting
enabled, the `mongos` caches the cluster-wide routing
table for each sharded collection as part of its startup procedure,
before it begins accepting client connections.

Without this setting enabled, the `mongos` only loads
a routing table as needed for incoming client connections, and only
loads the specific routing table for the namespace of a given
request.

A `mongos` instance with the
`loadRoutingTableOnStartup` parameter enabled may
experience longer startup times, but will result in faster servicing
of initial client connections once started.

`loadRoutingTableOnStartup` is enabled by default.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`warmMinConnectionsInShardingTaskExecutorPoolOnStartup`**

Available for `mongos` only.

Type: boolean

*Default*: true

Configures a `mongos` instance to prewarm its connection
pool on startup. With this parameter enabled, the
`mongos` attempts to establish
`ShardingTaskExecutorPoolMinSize` network
connections to each shard server as part of its startup procedure,
before it begins accepting client connections.

A timeout for this behavior can be configured with the
`warmMinConnectionsInShardingTaskExecutorPoolOnStartupWaitMS`
parameter. If this timeout is reached, the `mongos` will
begin accepting client connections regardless of the size of its
connection pool.

A `mongos` instance with this parameter enabled may
experience longer startup times, but will result in faster servicing
of initial client connections once started.

`warmMinConnectionsInShardingTaskExecutorPoolOnStartup` is
enabled by default.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

- `warmMinConnectionsInShardingTaskExecutorPoolOnStartupWaitMS`
- `ShardingTaskExecutorPoolMinSize`

**`warmMinConnectionsInShardingTaskExecutorPoolOnStartupWaitMS`**

Available for `mongos` only.

Type: integer

*Default*: 2000 (2 seconds)

Sets the timeout threshold in milliseconds for a
`mongos` to wait for `ShardingTaskExecutorPoolMinSize`
connections to be established per shard host when using the
`warmMinConnectionsInShardingTaskExecutorPoolOnStartup`
parameter. If this timeout is reached, the `mongos` will
begin accepting client connections regardless of the size of its
connection pool.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**See also:**

- `warmMinConnectionsInShardingTaskExecutorPoolOnStartup`
- `ShardingTaskExecutorPoolMinSize`

**`migrateCloneInsertionBatchDelayMS`**

Available for `mongod` only.

Type: Non-negative integer

Default: 0

Time in milliseconds to wait between batches of insertions during
cloning step of the migration process. This wait is in addition to
the `secondaryThrottle`.

The default value of `0` indicates no additional wait.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the `migrateCloneInsertionBatchDelayMS` to 200
milliseconds:

```bash
mongod --setParameter migrateCloneInsertionBatchDelayMS=200
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, migrateCloneInsertionBatchDelayMS: 200 } )
```

**`migrateCloneInsertionBatchSize`**

Available for `mongod` only.

Type: Non-negative integer

Default: 0

The maximum number of documents to insert in a single batch during
the cloning step of the migration process.

The default value of `0` indicates no maximum number of documents
per batch. However, in practice, this results in batches that
contain up to 16 MB of documents.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the `migrateCloneInsertionBatchSize` to 100
documents:

```bash
mongod --setParameter migrateCloneInsertionBatchSize=100
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, migrateCloneInsertionBatchSize: 100 } )
```

**`orphanCleanupDelaySecs`**

Available for `mongod` only.

Default: 900 (15 minutes)

Minimum delay before a migrated chunk is deleted from the source
shard.

Before deleting a migrated chunk, MongoDB waits for 
in-progress queries involving the chunk to complete on the shard primary 
and then waits an additional `orphanCleanupDelaySecs` seconds.

However, because the shard primary has no knowledge of in-progress queries
running on shard secondaries, a query that runs on a secondary can 
miss documents if it reads from documents in the migrating chunk.

To learn more about range migrations, see chunk-migration-procedure.

**Note:**

The behavior described above only applies to queries that start 
before a chunk migration commits. If a query starts after a chunk 
migration commits, the query does not use the migrating chunk.

If a shard has storage constraints, consider reducing this value
temporarily. If running queries that exceed 15 minutes on shard
secondaries, consider increasing this value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the `orphanCleanupDelaySecs` to 20 minutes:

```bash
mongod --setParameter orphanCleanupDelaySecs=1200
```

This may also be set using the `setParameter` command:

```javascript
db.adminCommand( { setParameter: 1, orphanCleanupDelaySecs: 1200 } )
```

**Tip:**

In all versions, the new value of `orphanCleanupDelaySecs` is
only applied to range deletions created after the value is changed. To
apply the new value to existing range deletions, force a step down.

**`persistedChunkCacheUpdateMaxBatchSize`**

**New in version:** 7.0.4 (and 6.0.13, 5.0.25)

Available for `mongod` only.

Type: Integer

Default: 1000

To route and serve operations, shards must know the routing and
ownership information associated with their collections. This
information propagates from a shard's primary node to its
secondary nodes through the replication of the internal cache
collections `config.cache.collections` and
`config.cache.chunks.<collectionName>`.

In previous versions, updates on the chunk cache collection were
performed individually (meaning that an entry was deleted and a new
entry was inserted). Starting in MongoDB 7.0.4, these updates are
performed as a batch of deletions followed by a batch of insertions.
The updated logic improves performance for collections that contain a
large number of chunks.

The `persistedChunkCacheUpdateMaxBatchSize` parameter specifies the
maximum batch size used for updating the persisted chunk cache.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `persistedChunkCacheUpdateMaxBatchSize`
to 700 at startup:

```bash
mongod --setParameter persistedChunkCacheUpdateMaxBatchSize=700
```

You can also set `persistedChunkCacheUpdateMaxBatchSize` during
runtime:

```javascript
db.adminCommand( { setParameter: 1, persistedChunkCacheUpdateMaxBatchSize: 700 } )
```

**`rangeDeleterBatchDelayMS`**

Available for `mongod` only.

Type: Non-negative integer

Default: 20

The amount of time in milliseconds to wait before the next batch of
deletion during the cleanup stage of range migration (or the `cleanupOrphaned`
command).

The _secondaryThrottle replication delay occurs after each batch deletion.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the `rangeDeleterBatchDelayMS` to 200
milliseconds:

```bash
mongod --setParameter rangeDeleterBatchDelayMS=200
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, rangeDeleterBatchDelayMS: 200 } )
```

**Tip:**

In versions prior to 6.0.3, the new value of `rangeDeleterBatchDelayMS` is
only applied to range deletions created after the value is changed. To
apply the new value to existing range deletions, force a step down.

From 6.0.3 on, the new value of the parameter is applied to all the range deletions processed
after the update, regardless of when the range deletion was created.

**`rangeDeleterBatchSize`**

Available for `mongod` only.

Type: Non-negative integer

Default: 2147483647 starting in MongoDB 5.1.2 and 5.0.6

The maximum number of documents in each batch to delete during the
cleanup stage of range migration
(or the `cleanupOrphaned` command).

A value of `0` indicates that the system chooses the default value.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `rangeDeleterBatchSize` to 32
documents:

```bash
mongod --setParameter rangeDeleterBatchSize=32
```

The parameter may also be set using the `setParameter`
command:

```javascript
db.adminCommand( { setParameter: 1, rangeDeleterBatchSize: 32 } )
```

**Tip:**

In versions prior to 6.0.3, the new value of `rangeDeleterBatchSize` is
only applied to range deletions created after the value is changed. To
apply the new value to existing range deletions, force a step down.

From 6.0.3 on, the new value of the parameter is applied to all the range deletions processed 
after the update, regardless of when the range deletion was created.

**`skipShardingConfigurationChecks`**

Available for `mongod` only.

Type: boolean

Default: false

When `true`, allows for starting a shard member or config server
member as a standalone for maintenance operations. This parameter is
mutually exclusive with the `--configsvr` or `--shardsvr` options.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter skipShardingConfigurationChecks=true
```

**Important:**

Once maintenance has completed, remove the
`skipShardingConfigurationChecks` parameter when
restarting the `mongod`.

**`findChunksOnConfigTimeoutMS`**

**New in version:** 5.0

Available for both `mongod` and `mongos`.

Type: Non-negative integer

Default: 900000

The timeout in milliseconds for find operations on
`chunks`.

If there is a large number of chunks in the cluster and chunk loading
fails with the error `ExceededTimeLimit`, increase the parameter
value:

```bash
mongod --setParameter findChunksOnConfigTimeoutMS=1000000
```

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

### Health Manager Parameters

**`activeFaultDurationSecs`**

Available for `mongos` only.

*Type*: Document

The amount of time to wait from a Health Managers Overview failure until the 
mongos is removed from the cluster, in seconds.

When a failure is detected and a Health Manager is configured as 
`critical`, the server waits for the specified interval 
before removing the `mongos` from the cluster. 

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

For example, to set the duration from failure to crash to five
minutes, issue the following at startup:

```bash
mongos --setParameter activeFaultDurationSecs=300
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      activeFaultDurationSecs: 300 
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `activeFaultDurationSecs`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   activeFaultDurationSecs: 300
```

**`healthMonitoringIntensities`**

Available for `mongos` only.

*Type*: Array of documents

Use this parameter to set intensity levels for Health Managers.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

`healthMonitoringIntensities` accepts an array of documents,
`values`. Each document in `values` takes two fields: 

- `type`, the Health Manager facet 
- `intensity`, the intensity level

#### Health Managers

| Facet | What the Health Observer Checks |
|---|---|
| `configServer` | Cluster health issues related to connectivity to the config server. |
| `dns` | Cluster health issues related to DNS availability and functionality. |
| `ldap` | Cluster health issues related to LDAP availability and functionality. |

#### Intensity Levels

| Intensity Level | Description |
|---|---|
| `critical` | The Health Manager on this facet is enabled and has the ability to move the failing mongos out of the cluster if an error occurs. The Health Manager waits the amount of time specified by `activeFaultDurationSecs` before stopping and moving the mongos out of the cluster automatically. |
| `non-critical` | The Health Manager on this facet is enabled and logs errors, but the mongos remains in the cluster if errors are encountered. |
| `off` | The Health Manager on this facet is disabled. The mongos does not perform any health checks on this facet. This is the default intensity level. |

For example, to set the `dns` Health Manager facet to the 
`critical` intensity level, issue the following at startup:

```bash
mongos --setParameter 'healthMonitoringIntensities={ values:[ { type:"dns", intensity: "critical"} ] }'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      healthMonitoringIntensities: { values: [ { type: "dns", intensity: "critical" } ] } } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `healthMonitoringIntensities`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   healthMonitoringIntensities: "{ values:[ { type:\"dns\", intensity: \"critical\"} ] }"
```

**`healthMonitoringIntervals`**

Available for `mongos` only.

*Type*: Array of documents

How often this Health Manager will run, in milliseconds.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

`healthMonitoringIntervals` accepts an array of documents,
`values`. Each document in `values` takes two fields:

- `type`, the Health Manager facet 
- `interval`, the time interval it runs at, in milliseconds

#### Health Managers

| Facet | What the Health Observer Checks |
|---|---|
| `configServer` | Cluster health issues related to connectivity to the config server. |
| `dns` | Cluster health issues related to DNS availability and functionality. |
| `ldap` | Cluster health issues related to LDAP availability and functionality. |

For example, to set the `ldap` Health Manager facet to the 
run health checks every 30 seconds, issue the following at startup:

```bash
mongos --setParameter 'healthMonitoringIntervals={ values:[ { type:"ldap", interval: "30000"} ] }'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      healthMonitoringIntervals: { values: [ { type: "ldap", interval: "30000" } ] } } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `healthMonitoringIntervals`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   healthMonitoringIntervals: "{ values: [{type: \"ldap\", interval: 200}] }"
```

**`progressMonitor`**

Available for `mongos` only.

*Type*: Document

Progress Monitor runs tests 
to ensure that Health Manager checks do not become stuck or 
unresponsive. Progress Monitor runs these tests in intervals specified 
by `interval`. If a health check begins but does not complete within
the timeout given by `deadline`, Progress Monitor stops the 
mongos and removes it from the cluster.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

#### `progressMonitor` Fields

| Field | Description | Units |
|---|---|---|
| `interval` | How often to ensure Health Managers are not stuck or unresponsive. | Milliseconds |
| `deadline` | Timeout before automatically failing the mongos if a Health Manager check is not making progress. | Seconds |

To set the `interval` to 1000 milliseconds and the `deadline` 
to 300 seconds, issue the following at startup:

```bash
mongos --setParameter 'progressMonitor={"interval": 1000, "deadline": 300}'
```

Or if using the `setParameter` command in a
`mongosh` session that is connected to a running
`mongos`:

```javascript
db.adminCommand( 
  {
      setParameter: 1, 
      progressMonitor: { interval: 1000, deadline: 300 } )
  }
)
```

Parameters set with `setParameter` do not persist across
restarts. See the setParameter page for details.

To make this setting persistent, set `progressMonitor`
in your mongos config file using the
`setParameter` option as in the following example:

```yaml
setParameter:
   progressMonitor: "{ interval: 1000, deadline: 300 }"
```

### Storage Parameters

**`honorSystemUmask`**

Available for both `mongod` and `mongos`.

*Default*: `false`

If `honorSystemUmask` is set to `true`, new files
created by MongoDB have permissions in accordance with the
user's `umask` settings. You cannot set `processUmask`
if `honorSystemUmask` is set to `true`.

If `honorSystemUmask` is set to `false`, new files
created by MongoDB have permissions set to `600`, which gives
read and write permissions only to the owner. New directories have
permissions set to `700`. You can use `processUmask`
to override the default permissions for groups and other users on
all new files created by MongoDB.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

```bash
mongod --setParameter honorSystemUmask=true

mongos --setParameter honorSystemUmask=true
```

**Note:**

`honorSystemUmask` is not available on Windows systems.

**`journalCommitInterval`**

Available for `mongod` only.

Specify an integer between `1` and `500` signifying the number
of milliseconds (ms) between journal commits.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Consider the following example which sets the
`journalCommitInterval` to `200` ms:

```javascript
db.adminCommand( { setParameter: 1, journalCommitInterval: 200 } )
```

**See also:**

`storage.journal.commitIntervalMs`

**`minSnapshotHistoryWindowInSeconds`**

**New in version:** 5.0

Available for `mongod` only.

*Default*: `300`

The minimum time window in seconds for which the storage engine keeps
the snapshot history. If you query data using read concern
`"snapshot"` and specify an
atClusterTime value older than the specified
`minSnapshotHistoryWindowInSeconds`, `mongod` returns
a `SnapshotTooOld` error.

**Warning:**

In sharded clusters, changing the default `minSnapshotHistoryWindowInSeconds` 
value on config server nodes may cause 
internal operations to fail.

Do not set `minSnapshotHistoryWindowInSeconds` to `0` on config server 
nodes. Setting this parameter to `0` causes internal operations conducting 
`snapshot` reads targeting the config server with a specified 
`atClusterTime` to fail.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Specify an integer greater than or equal to (`>=`) 0.

Consider the following example which sets the
`minSnapshotHistoryWindowInSeconds` to `600` seconds:

```javascript
db.adminCommand( { setParameter: 1, minSnapshotHistoryWindowInSeconds: 600 } )
```

**Note:**

Increasing the value of
`minSnapshotHistoryWindowInSeconds` increases disk
usage. For more information, see storage-snapshot-history.

To modify this value for a MongoDB Atlas cluster, you
must contact Atlas Support.

**`processUmask`**

Available for `mongod` only.

Overrides the default permissions used for groups and other users
when `honorSystemUmask` is set to `false`. By default,
when `honorSystemUmask` is set to `false`, new files
created by MongoDB have permissions set to `600`. Use the
`processUmask` parameter to override this default with a custom
`umask` value. The file owner inherits permissions from the system
`umask`.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

You cannot set this parameter if `honorSystemUmask` is set
to `true`. 

Consider the following example, which sets the permissions for groups
and other users to read/write only and retains the system `umask`
settings for the owner:

```bash
mongod --setParameter processUmask=011
```

**Note:**

`processUmask` is not available on Windows systems.

**`storageEngineConcurrentReadTransactions`**

**Changed in version:** 7.0

Available for `mongod` only.

*Type*: integer

Specifies the maximum number of concurrent read transactions (read tickets)
allowed into the storage engine.

**Note:**

Starting in version 7.0, MongoDB dynamically adjusts the number of 
tickets to optimize performance, with a highest possible value of 128.

Modifying this value can cause performance issues or errors. To 
determine if disabling the dynamic concurrent storage engine 
transactions algorithm is optimal for the cluster, contact 
[MongoDB Support](https://www.mongodb.com/docs/manual/support/).

Starting in MongoDB 7.0, this parameter is available for all storage 
engines. In earlier versions, this parameter is available for the 
WiredTiger storage engine only.

**See also:**

`wiredTiger.concurrentTransactions`

**`storageEngineConcurrentWriteTransactions`**

**Changed in version:** 7.0

Available for `mongod` only.

*Type*: integer 

Specifies the maximum number of concurrent write transactions allowed
into the WiredTiger storage engine.

**Note:**

Starting in version 7.0, MongoDB dynamically adjusts the number of 
tickets to optimize performance, with a highest possible value of 128.

Modifying this value can cause performance issues or errors. To 
determine if disabling the dynamic concurrent storage engine 
transactions algorithm is optimal for the cluster, contact 
[MongoDB Support](https://www.mongodb.com/docs/manual/support/).

Starting in MongoDB 7.0, this parameter is available for all storage 
engines. In earlier versions, this parameter is available for the 
WiredTiger storage engine only.

**See also:**

`wiredTiger.concurrentTransactions`

**`syncdelay`**

Available for `mongod` only.

*Default*: 60

Specify the interval in seconds when
`mongod` flushes its working memory to disk. By
default, `mongod` flushes memory to disk every 60
seconds. In almost every situation you should not set this value
and use the default setting.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Consider the following example which sets the `syncdelay` to
`60` seconds:

```javascript
db.adminCommand( { setParameter: 1, syncdelay: 60 } )
```

To provide durable data, WiredTiger
uses checkpoints. For more
details, see journaling-wiredTiger.

**See also:**

- `journalCommitInterval`
- `storage.syncPeriodSecs`

**`temporarilyUnavailableBackoffBaseMs`**

Available for `mongod` only.

*Default*: 1000

Specifies the initial delay before retying a write operation that was
rolled back due to cache pressure.

In rare circumstances, a write can fail due to cache pressure. When
this happens MongoDB issues a `TemporarilyUnavailable` error and
increments the `temporarilyUnavailableErrors` counter in two places:
the slow query log and the Full Time Diagnostic Data Capture
(FTDC).

Individual operations within multi-document transactions never return
`TemporarilyUnavailable` errors.

Adjust the write retry properties by modifying the
`temporarilyUnavailableBackoffBaseMs` and
`temporarilyUnavailableMaxRetries` parameters.

Contact support if you experience any cache pressure 
issues. 

The parameter accepts:

| Value | Description |
|---|---|
| `integer >= 0` | Defaults to 1 second. The initial delay between retries. The value increases with each retry to a maximum of 55 seconds. A larger value increases the chance that the cache pressure will be reduced before the next retry. To configure number of retries, use `temporarilyUnavailableMaxRetries`. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To set a new value, use `db.adminCommand()`:

```javascript
db.adminCommand( { setParameter: 1, temporarilyUnavailableBackoffBaseMs: 3 } )
```

**New in version:** 6.1.0

**`temporarilyUnavailableMaxRetries`**

Available for `mongod` only.

*Default*: 10

Specifies the maximum number of retries when a write operation is
rolled back due to cache pressure.

In rare circumstances, a write can fail due to cache pressure. When
this happens MongoDB issues a `TemporarilyUnavailable` error and
increments the `temporarilyUnavailableErrors` counter in two places:
the slow query log and the Full Time Diagnostic Data Capture
(FTDC).

Individual operations within multi-document transactions never return
`TemporarilyUnavailable` errors.

Adjust the write retry properties by modifying the
`temporarilyUnavailableBackoffBaseMs` and
`temporarilyUnavailableMaxRetries` parameters.

Contact support if you experience any cache pressure 
issues. 

The parameter accepts:

| Value | Description |
|---|---|
| `integer >= 0` | The maximum number of retries. There is an increasing delay between retries. To configure the backoff time, use `temporarilyUnavailableBackoffBaseMs`. |

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To set a new value, use `db.adminCommand()`:

```javascript
db.adminCommand( { setParameter: 1, temporarilyUnavailableMaxRetries: 5 } )
```

**New in version:** 6.1.0

**`upsertMaxRetryAttemptsOnDuplicateKeyError`**

Available for both `mongod` and `mongos`.

**New in version:** 7.0.22

Maximum number of retry attempts when an `upsert` operation
encounters a duplicate key error. 

*Type*: Integer

*Default*: 100

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets the maximum number of times the server 
retries an `upsert` operation when encountering a duplicate key 
error to `50`.

```bash
mongod --setParameter "upsertMaxRetryAttemptsOnDuplicateKeyError=50"
```

During run time, you can also set the parameter with the 
`setParameter` command:

```javascript
db.adminCommand( { 
   setParameter: 1, 
   upsertMaxRetryAttemptsOnDuplicateKeyError: 50 
} )
```

### WiredTiger Parameters

**`wiredTigerConcurrentReadTransactions`**

Available for `mongod` only.

*Type*: integer

Specifies the maximum number of concurrent read transactions (read tickets)
allowed into the storage engine.

**Note:**

Starting in version 7.0, MongoDB dynamically adjusts the number of 
tickets to optimize performance, with a highest possible value of 128.

Modifying this value can cause performance issues or errors. To 
determine if disabling the dynamic concurrent storage engine 
transactions algorithm is optimal for the cluster, contact 
[MongoDB Support](https://www.mongodb.com/docs/manual/support/).

Starting in MongoDB 7.0, this parameter is available for all storage 
engines. In earlier versions, this parameter is available for the 
WiredTiger storage engine only.

**Changed in version:** 6.0

The `wiredTigerConcurrentReadTransactions` parameter was renamed to 
`storageEngineConcurrentReadTransactions`.

**`wiredTigerConcurrentWriteTransactions`**

Available for `mongod` only.

*Type*: integer

Specifies the maximum number of concurrent write transactions allowed
into the WiredTiger storage engine.

**Note:**

Starting in version 7.0, MongoDB dynamically adjusts the number of 
tickets to optimize performance, with a highest possible value of 128.

Modifying this value can cause performance issues or errors. To 
determine if disabling the dynamic concurrent storage engine 
transactions algorithm is optimal for the cluster, contact 
[MongoDB Support](https://www.mongodb.com/docs/manual/support/).

Starting in MongoDB 7.0, this parameter is available for all storage 
engines. In earlier versions, this parameter is available for the 
WiredTiger storage engine only.

**Changed in version:** 6.0

The `wiredTigerConcurrentWriteTransactions` parameter was renamed to 
`storageEngineConcurrentWriteTransactions`.

**`wiredTigerEngineRuntimeConfig`**

Available for `mongod` only.

Specify `wiredTiger` storage engine configuration options for a
running `mongod` instance. 

This parameter is only available at runtime. To set the
parameter, use the `setParameter` command.

**Warning:**

Avoid modifying the `wiredTigerEngineRuntimeConfig`
unless under the direction from MongoDB engineers as this setting has
major implication across both WiredTiger and MongoDB.

Consider the following operation prototype:

```javascript
db.adminCommand({
   "setParameter": 1,
   "wiredTigerEngineRuntimeConfig": "<option>=<setting>,<option>=<setting>"
})
```

**`wiredTigerFileHandleCloseIdleTime`**

Available for `mongod` only.

*Type*: integer 

*Default*: 600

Specifies the amount of time in seconds that a file handle in `wiredTiger` 
can remain idle before being closed.

If you set `wiredTigerFileHandleCloseIdleTime` to `0`, idle handles 
are not closed. 

**Tip:**

This parameter is case sensitive. If you capitalize the `w` in 
`wiredTigerFileHandleCloseIdleTime` and run the parameter, the operation
returns the following error message:

```bash
{ "code":2,"codeName":"BadValue","errmsg":"Unknown --setParameter 'WiredTigerFileHandleCloseIdleTime'" }
```

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example:

```bash
mongod --setParameter wiredTigerFileHandleCloseIdleTime=100000
```

See the WiredTiger documentation for all available
:wtdocs-v5.0:`WiredTiger configuration options </struct_w_t___c_o_n_n_e_c_t_i_o_n.html#>`.

### Auditing Parameters

**`auditAuthorizationSuccess`**

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

Enables the auditing of authorization
successes for the authCheck
action.

When `auditAuthorizationSuccess` is `false`, the
audit system only logs the authorization
failures for `authCheck`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

To enable the audit of authorization successes, issue the following
command:

```javascript
db.adminCommand( { setParameter: 1, auditAuthorizationSuccess: true } )
```

Enabling `auditAuthorizationSuccess` degrades performance
more than logging only the authorization failures.

If runtime audit configuration
is enabled, the `auditAuthorizationSuccess` parameter
should not appear in the `mongod` or `mongos` configuration
file. The server will fail to start if the parameter is present.

**See also:**

`getParameter`

**`auditConfigPollingFrequencySecs`**

**New in version:** 5.0

*Type*: integer

*Default*: 300

A sharded cluster may have servers which maintain audit
configuration settings for the cluster. Set the interval, in
seconds, for non-configured servers to poll a config server for the
current audit generation. If this value returned differs from the
previously known value, the initiating node will request the current
configuration and update its internal state.

**Note:**

Using the default value of 300 seconds, non-config nodes may lag up
to 5 minutes behind a setAuditConfig command.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

**`auditEncryptionHeaderMetadataFile`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

*Type*: string

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

Path and file name for logging metadata audit headers for audit
log encryption. A header is
placed at the top of each audit log file and contains metadata for
decrypting the audit log. The headers are also stored in the
audit log.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

For example, the following sets the path and file for
`auditEncryptionHeaderMetadataFile`:

```bash
mongod --setParameter auditEncryptionHeaderMetadataFile=/auditFiles/auditHeadersMetadataFile.log
```

**`auditEncryptKeyWithKMIPGet`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

*Type*: boolean

*Default*: false

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

Enables audit log encryption for Key Management
Interoperability Protocol (KMIP) servers that only support KMIP
protocol version 1.0 or 1.1.

This parameter is only available at startup. To set the
parameter, use the `setParameter` setting. 

The following example sets
`auditEncryptKeyWithKMIPGet` to `true`:

```bash
mongod --setParameter auditEncryptKeyWithKMIPGet=true
```

### Transaction Parameters

**`AbortExpiredTransactionsSessionCheckoutTimeout`**

**New in version:** 7.0.26

Available for `mongod` only.

*Type*: integer

*Default*: 100 milliseconds

A session is checked out from a session pool to run database operations.

`AbortExpiredTransactionsSessionCheckoutTimeout` sets the
maximum number of milliseconds for a session to be checked out when
attempting to end an expired transaction.

If the expired transaction is successfully ended, MongoDB increments
`metrics.abortExpiredTransactions.successfulKills`. If the
transaction isn't successfully ended because it timed out when
attempting to check out a session, MongoDB increments
`metrics.abortExpiredTransactions.timedOutKills`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`AbortExpiredTransactionsSessionCheckoutTimeout` to `120`
milliseconds:

```javascript
db.adminCommand( { setParameter: 1, AbortExpiredTransactionsSessionCheckoutTimeout: 120 } )
```

You can also set this parameter during startup. For example:

```bash
mongod --setParameter AbortExpiredTransactionsSessionCheckoutTimeout=120
```

**`coordinateCommitReturnImmediatelyAfterPersistingDecision`**

**New in version:** 5.0

*Updated in version 6.1*

Available for `mongod` only.

*Type*: boolean

*Default*: false

- When set to `false`, the shard
  transaction coordinator waits for all participating shards
  to acknowledge the decision to either commit or cancel a
  multi-document transaction
  before returning the result to the client.

- When set to `true`, the shard transaction coordinator
  returns a multi-document transaction commit decision to the client as
  soon as the decision is made durable with the
  requested transaction write concern.

  If the client requested a write concern that is less than
  `"majority"`, the commit may roll back after the
  decision is returned to the client.

  Transactions may not have "read your writes" consistency.
  That is, a read operation may not show the results of write
  operations that preceded it. This can happen if: 

  - A transaction has to write to multiple shards.
  - The read and the earlier write take place in different sessions.

  Causal consistency only guarantees the
  causal relationship of reads and writes that occur within the same
  session.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`coordinateCommitReturnImmediatelyAfterPersistingDecision` to
`true`:

```javascript
mongod --setParameter coordinateCommitReturnImmediatelyAfterPersistingDecision=true
```

During run time, you can also set the parameter with the
`setParameter` command:

```bash
db.adminCommand( { setParameter: 1, coordinateCommitReturnImmediatelyAfterPersistingDecision: true } )
```

**`internalSessionsReapThreshold`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

*Default*: 1000

Session limit for internal session metadata deletion. The metadata:

- Contains session transaction information for user operations.
- Is stored in the `config.transactions` collection.

When the number of internal sessions is greater than
`internalSessionsReapThreshold`, the metadata is deleted.

If you set `internalSessionsReapThreshold` to `0`, the
internal session metadata is only deleted when the user session ends.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets `internalSessionsReapThreshold`
to `500` sessions:

```javascript
db.adminCommand( { setParameter: 1, internalSessionsReapThreshold: 500 } )
```

You can also set `internalSessionsReapThreshold` at
startup. For example:

```bash
mongod --setParameter internalSessionsReapThreshold=500
```

**`maxConcurrentMultiDocumentTransactions`**

**New in version:** 7.0.46

Available for `mongod` only.

*Type*: integer

*Default*: 10000

The maximum number of concurrently open multi-document
transactions that the server allows for
external clients at one time. When this limit is reached, the
server rejects new multi-document transactions from external
clients and returns a `TooManyOpenTransactions` error.

The count of open transactions is server-wide. Process-internal
transactions are exempt from rejection, but still contribute to the
total count when the server enforces the limit for external
clients.

Limiting the number of concurrent multi-document transactions can
help prevent high numbers of idle transactions from degrading
system performance.

Set this parameter to `0` to disable the limit. The minimum value
is `0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following example sets
`maxConcurrentMultiDocumentTransactions` to `5000` at runtime:

```javascript
db.adminCommand( { setParameter: 1, maxConcurrentMultiDocumentTransactions: 5000 } )
```

You can also set this parameter at startup. For example:

```bash
mongod --setParameter maxConcurrentMultiDocumentTransactions=5000
```

**`transactionLifetimeLimitSeconds`**

Available for `mongod` only.

*Default*: 60

Specifies the lifetime of multi-document transactions. Transactions that exceed this limit are
considered expired and will be aborted by a periodic cleanup
process. The cleanup process runs every
`transactionLifetimeLimitSeconds`/2 seconds or at least
once every 60 seconds.

The cleanup process helps relieve storage cache pressure.

The minimum value for transactionLifetimeLimitSeconds is `1`
second.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the
`transactionLifetimeLimitSeconds` to `30`
seconds:

```javascript
db.adminCommand( { setParameter: 1, transactionLifetimeLimitSeconds: 30 } )
```

You can also set parameter `transactionLifetimeLimitSeconds` at
startup time.

```bash
mongod --setParameter "transactionLifetimeLimitSeconds=30"
```

To set the parameter for a sharded cluster, the parameter must be
modified for all shard replica set members.

Starting in MongoDB 5.0, if you change the
`transactionLifetimeLimitSeconds` parameter, you must also
change `transactionLifetimeLimitSeconds` to the same value on
all config server replica set members. Keeping this value consistent:

- Ensures the routing table history is retained for at least as long as
  the transaction lifetime limit on the shard replica set members.

- Reduces the transaction retry frequency and therefore improves
  performance.

**`transactionTooLargeForCacheThreshold`**

**New in version:** 6.2

Available for `mongod` only.

*Type*: decimal

*Default*: 0.75

The threshold value for retrying transactions that fail due to cache
pressure. The value is a percentage of the dirty cache size. The
default value, `0.75`, means 75% of the dirty cache.

The dirty cache is limited to 20% of the total cache size. When
`transactionTooLargeForCacheThreshold` is set to `0.75`, the
server only retries transactions that use less than 15%
(`0.75 * 20%`) of the total storage engine cache.

The limit only applies to retries. Large transactions can use more
than `transactionTooLargeForCacheThreshold` percent of the dirty
cache. However, if a large transaction is rolled back due to cache
pressure, the server issues a
transactionTooLargeForCache-error error and does not retry the
transaction. 

To disable this behavior, set
`transactionTooLargeForCacheThreshold` to `1.0`.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

Contact support if you experience any cache pressure 
issues. 

For more information on WiredTiger storage, see:
wiredTiger-storage-options.

**`maxTransactionLockRequestTimeoutMillis`**

Available for `mongod` only.

*Type*: integer

*Default*: 5

The maximum amount of time in milliseconds that multi-document
transactions should wait to acquire locks
required by the operations in the transaction.

If the transaction cannot acquire the locks after waiting
`maxTransactionLockRequestTimeoutMillis`, the transaction
aborts.

By default, multi-document transactions
wait `5` milliseconds. That is, if the transaction cannot acquire
the locks within `5` milliseconds, the transaction aborts. If an
operation provides a greater timeout in a lock request,
`maxTransactionLockRequestTimeoutMillis` overrides the
operation-specific timeout.

You can set `maxTransactionLockRequestTimeoutMillis` to:

- `0` such that if the transaction cannot acquire the required
  locks immediately, the transaction aborts.

- A number greater than `0` to wait the specified time to acquire
  the required locks. This can help obviate transaction aborts on
  momentary concurrent lock acquisitions, like fast-running metadata
  operations. However, this could possibly delay the abort of
  deadlocked transaction operations.

- `-1` to use the operation specific timeout.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following sets the
`maxTransactionLockRequestTimeoutMillis` to `20`
milliseconds:

```javascript
db.adminCommand( { setParameter: 1, maxTransactionLockRequestTimeoutMillis: 20 } )
```

You can also set this parameter during start-up:

```bash
mongod --setParameter maxTransactionLockRequestTimeoutMillis=20
```

### Slot-Based Execution Parameters

**`planCacheSize`**

**New in version:** 6.3

Available for `mongod` only.

*Type*: string

*Default*: 5%

**Note:**

Although the `planCacheSize` parameter existed in prior versions of 
MongoDB, it had no effect on the plan cache until version 6.3.

Sets the size of the plan cache 
only for the slot-based query execution engine.

You can set the `planCacheSize` value to either:

- A percentage of the system's total physical memory to allocate for
  the plan cache. For example, `"8.5%"`.

- The exact amount of data to allocate for the plan cache in either
  `MB` or `GB`. For example, `"100MB"` or `"1GB"`.

Increasing the plan cache size adds more cached query shapes for the
query planner. This can
improve query performance, but increases memory usage.

This parameter is available both at runtime and at startup:

- To set the parameter at runtime, use the
  `setParameter` command.

- To set the parameter at startup, use the
  `setParameter` setting.

The following startup command sets `planCacheSize` to 80
megabytes:

```bash
mongod --setParameter planCacheSize="80MB"
```

You can also use the `setParameter` command within the
`MongoDB Shell`:

```javascript
db.adminCommand( { setParameter: 1, planCacheSize: "80MB" } )
```
