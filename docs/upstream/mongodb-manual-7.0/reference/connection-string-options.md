<!-- Converted from reference/connection-string-options.txt (reStructuredText). Includes are inlined. -->

# Connection String Options

This page lists all connection options to connect to your database using
SRV connection strings and standard connection strings.

Connection options are pairs in the following form: `name=value`.

- The option `name` is case insensitive when using a driver.

- The option `name` is case insensitive when using
  `mongosh`.

- The `value` is always case sensitive.

Separate options with the ampersand (`&`) character
`name1=value1&name2=value2`. In the following example, a
connection includes the `replicaSet` and
`connectTimeoutMS` options:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net:27017,db2.example.net:2500/?replicaSet=test&connectTimeoutMS=300000
```

**Note:** Semi-colon separator for connection string arguments

To provide backwards compatibility, drivers accept
semi-colons (`;`) as option separators.

## Replica Set Option

The following connection string connects to a replica set named
`myRepl` with members running on the specified hosts. It
authenticates as user `myDatabaseUser` with the password
`D1fficultP%40ssw0rd`:

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com:27017,db1.example.com:27017,db2.example.com:27017/?replicaSet=myRepl
```

* - Connection Option
  - Description

* - .. urioption:: replicaSet

  - Specifies the name of the replica set, if the
    `mongod` is a member of a replica set. Set the `replicaSet`
    connection option to ensure consistent behavior across drivers. 

    When connecting to a replica set, provide a seed list
    of the replica set members in the `host[:port]` component.
    See your `driver` documentation for details.

* - .. urioption:: directConnection

  - Specifies whether the client connects directly to the
    `host[:port]` in the connection URI:

    - `true`: The client sends operations only to the specified host and
      does not attempt to discover other replica set members.

    - `false`: The client attempts to discover all servers in the replica set,
      and sends operations to the primary member. This is the default value.

## Connection Options

### TLS Options

The following connection string to a replica set includes 
`tls=true` option. It authenticates as user `myDatabaseUser` 
with the password `D1fficultP%40ssw0rd`.

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&tls=true
```

You can also use the equivalent `ssl=true` option:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&ssl=true
```

* - Connection Option
  - Description

* - .. urioption:: tls

  - Enables or disables TLS/SSL for the connection:

    - `true`: Initiates the connection with TLS/SSL. Default for
      connections-dns-seedlist.

    - `false`: Initiates the connection without TLS/SSL. Default
      for connections-standard-connection-string-format.

    The `tls` option is equivalent to
    `ssl`.

    If the `mongosh` shell specifies additional
    tls/ssl options from the
    command-line, use the `--tls` command-line option instead.

* - .. urioption:: ssl

  - Enables or disables TLS/SSL for the connection:

    - `true`: Initiates the connection with TLS/SSL. Default for
      connections-dns-seedlist.

    - `false`: Initiates the connection without TLS/SSL. Default
      for connections-standard-connection-string-format.

    The `ssl` option is equivalent to the
    `tls` option.

    If the `mongosh` shell specifies additional
    tls/ssl options from the
    command-line, use the `--ssl`
    command-line option instead.

* - .. urioption:: tlsCertificateKeyFile

  - Specifies the location of a local `.pem` file that
    contains either the client's TLS/SSL X.509 certificate or the
    client's TLS/SSL certificate and key.

    The client presents this file to the
    `mongod` / `mongos` instance.

    `mongod` / `mongos` logs a warning on
    connection if the presented X.509 certificate expires within `30`
    days of the `mongod/mongos` host system time.

    This option is not supported by all drivers. Refer to the
    `Drivers` documentation.

    This connection string option is not available for the `mongo` shell. 
    Use the command-line option instead.

* - .. urioption:: tlsCertificateKeyFilePassword

  - Specifies the password to decrypt the `tlsCertificateKeyFile`.

    This option is not supported by all drivers. Refer to the
    `Drivers` documentation.

    This connection string option is not available for the `mongo` shell. 
    Use the command-line option instead.

* - .. urioption:: tlsCAFile

  - Specifies the path to a local `.pem` file that contains 
    the root certificate chain from the Certificate Authority. The 
    client uses this file to validate the certificate presented by
    the `mongod` / `mongos` instance.

    This option is not supported by all drivers. Refer to the
    `Drivers` documentation.

    This connection string option is not available for the `mongo` shell. 
    Use the command-line option instead.

* - .. urioption:: tlsAllowInvalidCertificates

  - Bypasses validation of the certificates presented by the
    `mongod` / `mongos` instance

    Set to `true` to connect to MongoDB instances even if the
    server's present invalid certificates.

    This option is not supported by all drivers. Refer to the
    `Drivers` documentation.

    This connection string option is not available for the `mongo` shell. 
    Use the command-line option instead.

    WARNING: Disabling certificate validation creates a vulnerability.

* - .. urioption:: tlsAllowInvalidHostnames

  - Disables hostname validation of the certificate presented by
    the `mongod` / `mongos` instance.

    Set to `true` to connect to MongoDB instances even if the
    hostname in the server certificates do not match the server's
    host.

    This option is not supported by all drivers. Refer to the
    `Drivers` documentation.

    This connection string option is not available for the `mongo` shell. 
    Use the command-line option instead.

    WARNING: Disabling certificate validation creates a vulnerability.

* - .. urioption:: tlsInsecure

  - Disables various certificate validations. 

    Set to `true` to disable certificate validations. The exact
    validatations disabled vary by drivers. Refer to the
    `Drivers` documentation.

    This connection string option is not available for the `mongo` shell. 
    Use the command-line option instead.

    WARNING: Disabling certificate validation creates a vulnerability.

### Timeout Options

| Connection Option | Description |
|---|---|
| .. urioption:: timeoutMS | The time in milliseconds to attempt an operation before timing out. The timeout applies to all steps in an operation, including server selection, connection checkout, and server-side execution. `timeoutMS` has no default value. If you do not specify a value, the driver applies individual timeout options, such as `socketTimeoutMS`. If you set `timeoutMS` in the connection string, the driver ignores other timeout options, and the timeout applies to every operation in the client. You can override `timeoutMS` at a more specific level, but you cannot unset the value. To learn more about timeout inheritence, see node-csot. IMPORTANT: `timeoutMS` is not yet supported by all official drivers. For availability, see the `driver` documentation. |
| .. urioption:: connectTimeoutMS | The time in milliseconds to attempt a connection before timing out. The default is 10,000 milliseconds, but specific drivers might have a different default. For details, see the `driver` documentation. |
| .. urioption:: socketTimeoutMS | The time in milliseconds to attempt a send or receive on a socket before the attempt times out. The default is no timeout, though different drivers might vary. See the `driver` documentation. |

### Compression Options

* - Connection Option
  - Description

* - .. urioption:: compressors

  - Comma-delimited string of compressors to enable
    network compression for communication between this
    client and a `mongod` / `mongos`
    instance.

    You can specify the following compressors:	

    - snappy
    - zlib
    - zstd

    If you specify multiple compressors, then the order in which you list
    the compressors matter as well as the communication initiator. For
    example, if the client specifies the following network
    compressors `"zlib,snappy"` and the `mongod` specifies
    `"snappy,zlib"`, messages between the client and the
    `mongod` uses `zlib`.

    Messages are compressed only when both parties enable network
    compression and share a common compressor. Otherwise, messages
    between the parties are uncompressed.

    `mongosh` supports the uri connection string
    option `compressors`.

* - .. urioption:: zlibCompressionLevel

  - An integer that specifies the compression level if using
    zlib for `network compression`.

    You can specify an integer value ranging from `-1` to `9`:

    - `-1`: Default compression level, usually level `6`
      compression.

    - `0`: No compression

    - `1` - `9`: Increasing level of compression but at the cost
      of speed, with:

      - `1` providing the best speed but least compression, and

      - `9` providing the best compression but at the slowest speed.

    Supported by `mongosh`.

## Connection Pool Options

Most drivers implement some kind of connection pool handling.
Some drivers do not support connection
pools. See your `driver` documentation
for more information on the connection pooling implementation. These
options allow applications to configure the connection pool when
connecting to the MongoDB deployment.

| Connection Option | Description |
|---|---|
| .. urioption:: maxPoolSize | The maximum number of connections in the connection pool. The default value is `100`. |
| .. urioption:: minPoolSize | The minimum number of connections in the connection pool. The default value is `0`. The `minPoolSize` option is not supported by all drivers. For information on your driver, see the `Drivers` documentation. |
| .. urioption:: maxConnecting | Maximum number of connections a pool can establish concurrently. The default value is `2`. `maxConnecting` is supported for all drivers **except** the `Rust Driver`. Raising the value of `maxConnecting` allows the client to establish connection to the server faster, but increases the chance of connection storms. If the value of `maxConnecting` is too low, your connection pool may experience heavy throttling and increased tail latency for clients checking out connections. |
| .. urioption:: maxIdleTimeMS | The maximum number of milliseconds that a connection can remain idle in the pool before being removed and closed. This option is not supported by all drivers. |
| .. urioption:: waitQueueMultiple | A number that the driver multiplies the `maxPoolSize` value by, to provide the maximum number of threads allowed to wait for a connection to become available from the pool. For default values, see the `driver` documentation. This option is not supported by all drivers. |
| .. urioption:: waitQueueTimeoutMS | The maximum time in milliseconds that a thread can wait for a connection to become available. For default values, see the `driver` documentation. This option is not supported by all drivers. |

## Write Concern Options

Write concern describes the level of
acknowledgment requested from MongoDB. These options are supported by:

- MongoDB drivers
- `mongosh`
- `mongofiles`
- `mongoimport`
- `mongorestore`

You can specify write concern both in the connection string and as a
parameter to methods like `insert` or `update`. If specified in
both places, the method parameter overrides the connection string.

MongoDB Atlas deployment connection strings use `"majority"`
by default. If you don't specify write concern for an MongoDB Atlas
deployment, MongoDB Atlas enforces `"majority"`.

The following connection string to a replica set specifies
`"majority"` write concern and a 5 second
timeout using the `wtimeoutMS` write concern parameter:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&w=majority&wtimeoutMS=5000
```

| Connection Option | Description |
|---|---|
| .. urioption:: w | Corresponds to the write concern wc-w. The `w` option requests acknowledgment that the write operation has propagated to a specified number of `mongod` instances or to `mongod` instances with specified tags. You can specify a `number <`, the string `majority`, or a `tag set <`. For details, see wc-w. |
| .. urioption:: wtimeoutMS | IMPORTANT: The `wtimeoutMS` option is deprecated. Set `timeoutMS` instead. `timeoutMS` overrides `wtimeoutMS`. Corresponds to the write concern wc-wtimeout. `wtimeoutMS` specifies a time limit, in milliseconds, for the write concern. When `wtimeoutMS` is `0`, write operations never time out. For more information, see wc-wtimeout. |
| .. urioption:: journal | Corresponds to the write concern wc-j option. The `journal` option requests acknowledgment from MongoDB that the write operation has been written to the journal. For details, see wc-j. If you set `journal` to `true`, and specify a `w` value less than 1, `journal` prevails. |

For more information, see write-concern.

## readConcern Options

For the WiredTiger storage engine, MongoDB introduces the
`readConcern` option for replica sets and replica set shards.

/reference/read-concern allows clients to choose a level of
isolation for their reads from replica sets.

The following connection string to a replica set specifies
`readConcernLevel=majority`:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&readConcernLevel=majority
```

* - Connection Option
  - Description

* - .. urioption:: readConcernLevel

  - The level of isolation. Accepts one of the following values:

    - `local`
    - `majority`
    - `linearizable`
    - `available`

    This connection string option is not available for
    `mongosh`. Specify the read concern as an
    option to the specific operation.

For more information, see /reference/read-concern.

## Read Preference Options

Read preferences describe the
behavior of read operations with regards to replica sets. These parameters allow you to specify read preferences
on a per-connection basis in the connection string.

For example:

- The following connection string to a replica set specifies
  `secondary` read preference mode and a
  `maxStalenessSeconds` value of 120 seconds:

  ```none
  mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&readPreference=secondary&maxStalenessSeconds=120
  ```

- The following connection string to a sharded cluster specifies
  `secondary` read preference mode and a
  `maxStalenessSeconds` value of 120 seconds:

  ```none
  mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos1.example.com,mongos2.example.com/?readPreference=secondary&maxStalenessSeconds=120
  ```

- The following connection string to a sharded cluster specifies
  `secondary` read preference mode and three
  `readPreferenceTags`:

  ```none
  mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos1.example.com,mongos2.example.com/?readPreference=secondary&readPreferenceTags=dc:ny,rack:r1&readPreferenceTags=dc:ny&readPreferenceTags=
  ```

Order matters when using multiple `readPreferenceTags`. The
`readPreferenceTags` are tried in order until a match is found. Once
found, that specification is used to find all eligible matching
members and any remaining `readPreferenceTags`  are ignored.
For details, see read-preference-tag-order-matching.

* - Connection Option
  - Description

* - .. urioption:: readPreference

  - Specifies the read preferences
    for this connection. Possible values are:

    - `primary` (*Default*)
    - `primaryPreferred`
    - `secondary`
    - `secondaryPreferred`
    - `nearest`

    Transactions that contain
    read operations must use read preference `primary`. All
    operations in a given transaction must route to the same member.

    This connection string option is not available for the
    `mongo` shell. See `cursor.readPref()` and
    `Mongo.setReadPref()` instead.

* - .. urioption:: maxStalenessSeconds

  - Specifies, in seconds, how stale a secondary can be before the client
    stops using it for read operations. For details, see
    replica-set-read-preference-max-staleness.

    By default, there is no maximum staleness and clients do not consider a
    secondary's lag when choosing where to direct a read operation.

    The minimum `maxStalenessSeconds` value is 90
    seconds. Specifying a value between 0 and 90 seconds produces
    an error. MongoDB drivers treat a `maxStalenessSeconds` value
    of `-1` as "no max staleness", the same as if
    `maxStalenessSeconds` is omitted. 

* - .. urioption:: readPreferenceTags

  - Specifies the tags document as a comma-separated
    list of colon-separated key-value pairs. For example,

    - To specify the tags document `{ "dc": "ny", "rack": "r1" }`,
      use `readPreferenceTags=dc:ny,rack:r1` in the connection
      string.

    - To specify an empty tags document `{ }`, use
      `readPreferenceTags=` without setting the value.

    To specify a *list* of tag documents, use multiple
    `readPreferenceTags`. For example,
    `readPreferenceTags=dc:ny,rack:r1&readPreferenceTags=`.

    Order matters when using multiple `readPreferenceTags`. The
    `readPreferenceTags` are tried in order until a match is
    found. For details, see
    read-preference-tag-order-matching.

    This connection string option is not available for the
    `mongo` shell. See `cursor.readPref()` and
    `Mongo.setReadPref()` instead.

For more information, see Read preferences.

## Authentication Options

The following connection string to a replica set specifies the
`authSource` to the `admin` database. That is, the user
credentials are authenticated against the `admin` database.

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?replicaSet=myRepl&authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

* - Connection Option
  - Description

* - .. urioption:: authSource

  - Database name associated with the user's credentials. Defaults
    to `defaultauthdb` if specified, otherwise defaults to
    `admin`.

    The `PLAIN`, `GSSAPI`, and `MONGODB-AWS` mechanisms
    require `authSource` to be set to `$external`,
    as they delegate credential storage to external services.

    MongoDB ignores `authSource` if no username is
    provided in the connection string or via `--username`.

* - .. urioption:: authMechanism

    Default: SCRAM-SHA-256

  - Authentication mechanism for the connection. Without an
    explicit `authMechanism`, MongoDB tries SCRAM-SHA-256 and
    falls back to SCRAM-SHA-1 if that fails.

    - SCRAM-SHA-1

    - SCRAM-SHA-256

    - MONGODB-X509

    - `MONGODB-AWS`

    - GSSAPI (Kerberos)

    - PLAIN (LDAP SASL) 

    Only MongoDB Enterprise `mongod` and
    `mongos` instances provide `GSSAPI` (Kerberos) and
    `PLAIN` (LDAP) mechanisms.

    To use `MONGODB-X509`, you must have TLS/SSL Enabled.

    To use `MONGODB-AWS`, you must connect to a
    [MongoDB Atlas](https://www.mongodb.com/atlas/database) cluster
    configured to support authentication via
    [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
    (an AWS access key ID and a secret access key, and
    optionally an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)).
    The `MONGODB-AWS` authentication mechanism requires that the
    `authSource` be set to `$external`.

    When using `MONGODB-AWS`, provide your AWS access key ID as the
    username and the secret access key as the password. If using an
    [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)
    as well, provide it with the `AWS_SESSION_TOKEN`
    `authMechanismProperties` value.

    If the AWS access key ID, the secret access key, or the session token
    include the following characters, those characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1). 

    ```none
    $ : / ? # [ ] @
    ```

    Alternatively, if the AWS access key ID, secret access key, or
    session token are defined on your platform using their respective
    [AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list),
    `mongosh` uses these environment variable values to 
    authenticate automatically. You do not need to specify them in the connection string.
    There are other methods to provide AWS credentials depending on your deployment 
    environment and security requirements.

    For example usage of the `MONGODB-AWS` authentication
    mechanism, see find-connection-string.

    See /core/authentication for more information about the
    authentication system in MongoDB. Also consider
    /tutorial/configure-x509-client-authentication for more
    information on x509 authentication.

* - .. urioption:: authMechanismProperties

  - Specify properties for the specified `authMechanism`
    as a comma-separated list of colon-separated key-value pairs.

    Possible key-value pairs are:

    `SERVICE_NAME:<string>`
      Set the Kerberos service name when connecting to Kerberized
      MongoDB instances. This value must match the service name set
      on MongoDB instances to which you are connecting. Only valid
      when using the GSSAPI
      authentication mechanism.

      `SERVICE_NAME` defaults to `mongodb` for all clients and
      MongoDB instances. If you change the
      `saslServiceName` setting on a MongoDB instance, you
      must set `SERVICE_NAME` to match that setting. Only valid
      when using the GSSAPI
      authentication mechanism.

    `CANONICALIZE_HOST_NAME:true|false`
      Canonicalize the hostname of the client host machine when
      connecting to the Kerberos server. This may be required when
      hosts report different hostnames than what is in the Kerberos
      database. Defaults to `false`. Only valid when using the
      GSSAPI authentication
      mechanism.

    `SERVICE_REALM:<string>`
      Set the Kerberos realm for the MongoDB service. This may be
      necessary to support cross-realm authentication where the user
      exists in one realm and the service in another. Only valid when
      using the GSSAPI authentication
      mechanism.

    `AWS_SESSION_TOKEN:<security_token>`
      Set the AWS session token for authentication with temporary
      credentials when using an [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
      request, or when working with AWS resources that specify this
      value such as Lambda. Only valid when using the `MONGODB-AWS`
      authentication mechanism. You must have an AWS access key ID
      and a secret access key as well. For example usage, see
      find-connection-string.

* - .. urioption:: gssapiServiceName

  - Set the Kerberos service name when connecting to Kerberized
    MongoDB instances. This value must match the service name set on
    MongoDB instances to which you are connecting.

    `gssapiServiceName` defaults to `mongodb` for all
    clients and MongoDB instances. If you change
    `saslServiceName` setting on a MongoDB instance, you
    must set `gssapiServiceName` to match that setting.

    `gssapiServiceName` is a deprecated aliases for
    `authMechanismProperties=SERVICE_NAME:mongodb`. For more information on which
    options your driver supports and their relative priority to each
    other, reference the documentation for your preferred driver
    version.

## Server Selection and Discovery Options

MongoDB provides the following options to configure how MongoDB drivers
and `mongos` instances select a server to which to direct read
or write operations.

* - Connection Option
  - Description

* - .. urioption:: localThresholdMS

  - The size (in milliseconds) of the latency window for selecting
    among multiple suitable MongoDB instances. *Default*: 15
    milliseconds.

    All drivers use `localThresholdMS`. Use the
    `localThreshold` alias when specifying the latency window size
    to `mongos`.

* - .. urioption:: serverSelectionTimeoutMS

  - Specifies how long (in milliseconds) to block for server
    selection before throwing an exception. *Default*: 30,000
    milliseconds.

* - .. urioption:: serverSelectionTryOnce

  - **Single-threaded drivers only**. When `true`, the
    driver scans the MongoDB deployment exactly once after server
    selection fails and then either selects a server or raises an
    error. When `false`, the driver blocks and searches for a
    server up to the `serverSelectionTimeoutMS` value.
    *Default*: `true`.

    Multi-threaded drivers and `mongos` do not support
    `serverSelectionTryOnce`.

* - .. urioption:: heartbeatFrequencyMS

  - `heartbeatFrequencyMS` controls when the driver
    checks the state of the MongoDB deployment. Specify the interval
    (in milliseconds) between checks, counted from the end of the
    previous check until the beginning of the next one.

    *Default*:

    - Single-threaded drivers: 60 seconds.
    - Multi-threaded drivers: 10 seconds.

    `mongos` does not support changing the frequency of
    the heartbeat checks.

* - .. urioption:: socketCheckIntervalMS

  - **Single-threaded clients only**. Controls how often the client checks the
    state of the TCP connection to the MongoDB deployment. If you specify a lower
    value, the client detects network issues faster but uses more CPU.
    *Default*: 5 seconds.

    This option is not supported by all drivers. Refer to the
    `Drivers` documentation.

## Miscellaneous Configuration

* - Connection Option
  - Description

* - .. urioption:: appName

  - Specify a custom app name. The app name appears in:

    - `mongod` and `mongos` logs
    - the `currentOp.appName` field in the
      `currentOp` command and `db.currentOp()`
      method output
    - the `system.profile.appName` field in the
      database profiler output

    The `appName` connection option is available for:

    - `MongoDB Drivers` 
    - `mongosh` starting in `mongosh` 1.1.9
    - `MongoDB Compass` starting in Compass 1.28.4

* - .. urioption:: retryReads

  - Enables retryable reads.

    Possible values are:

    - `true`. Enables retryable reads for the connection. 

      Official MongoDB drivers default to `true`.

    - `false`. Disables retryable reads for the connection.

    `mongosh` does not support retryable reads.

* - .. urioption:: retryWrites

  - Enable retryable writes.

    Possible values are:

    - `true`. Enables retryable writes for the connection. 

      Official MongoDB drivers default to `true`.

    - `false`. Disables retryable writes for the connection. 

    MongoDB drivers retry 
    transaction commit and abort operations
    regardless of the value of `retryWrites`. For more 
    information on transaction retryability, see
    transactions-retry. 

* - .. urioption:: uuidRepresentation

  - Possible values are:

    `standard`
      The standard binary representation.

    `csharpLegacy`
      The default representation for the .NET/C# driver.

    `javaLegacy`
      The default representation for the Java driver.

    `pythonLegacy`
      The default representation for the Python driver.

    For the default, see the `Drivers`
    documentation for your driver.

    Not all drivers support the `uuidRepresentation`
    option. For information on your driver, see the `drivers` documentation.

* - .. urioption:: loadBalanced 

  - Specifies whether the client is connecting to a load balancer. This option is
    `false` by default.

    You can set this option to `true` only if you meet the following
    requirements:

    - You specify only one host name.
    - You aren't connecting to a replica set.
    - The `srvMaxHosts` option is unset or has a value of `0`.
    - The `directConnection` option is unset or has a value of `false`.

* - .. urioption:: srvMaxHosts

  - Specifies the number of `mongos` connections that can be created for
    sharded topologies. Set this option to a non-negative integer.
    `0` is the default value and means there is no limit on the number of
    `mongos` connections.
