<!-- Converted from tutorial/configure-ssl-clients.txt (reStructuredText). Includes are inlined. -->

# TLS/SSL Configuration for Clients

Clients must have support for TLS/SSL to connect to a
`mongod` or a `mongos` instance that require
TLS/SSL connections.

**Note:**

- The *Linux 64-bit legacy x64* binaries of MongoDB do **not** include
  support for TLS/SSL.

- .. include:: /includes/fact-tls-1.0.rst

**Important:**

A full description of TLS/SSL, PKI (Public Key Infrastructure) certificates, and Certificate Authority is beyond the scope of this document.
This page assumes prior knowledge of TLS/SSL as well as access to valid certificates.

## MongoDB Shell

`mongosh` provides various TLS/SSL settings,
including:

| TLS Option | Notes |
|---|---|
| `--tls` | Enables TLS/SSL connection. |
| `--tlsCertificateKeyFile` | Specifies the `.pem` file that contains `mongosh`'s certificate and key to present to the `mongod` or `mongos` instance. This option is mutually exclusive with `--tlsCertificateSelector` `mongod` / `mongos` logs a warning on connection if the presented X.509 certificate expires within `30` days of the `mongod/mongos` host system time. |
| `--tlsCertificateKeyFilePassword` | If `mongosh`'s certificate key file is encrypted. |
| `--tlsCAFile` | Specifies the Certificate Authority (CA) `.pem` file for verification of the certificate presented by the `mongod` or the `mongos` instance. |
| `--tlsCertificateSelector` | If running on Windows or macOS, use a certificate from the system certificate store. This option is mutually exclusive with `--tlsCertificateKeyFile`. `mongod` / `mongos` logs a warning on connection if the presented X.509 certificate expires within `30` days of the `mongod/mongos` host system time. |

For a complete list of `mongosh`'s `tls`
options, see `TLS options`.

For TLS/SSL connections, `mongosh` validates the
certificate presented by the `mongod` or
`mongos` instance:

- `mongosh` verifies that the certificate is from
  the specified Certificate Authority (`--tlsCAFile`. If the certificate is not from the specified CA,
  `mongosh` will fail to connect.

- .. include:: /includes/extracts/ssl-facts-mongo-ssl-hostname-verification.rst

  To connect `mongosh` to a `mongod` or
  `mongos` that requires TLS/SSL, specify the
  `--host` option or use a connection
  string to specify the hostname. All
  other `TLS/SSL` options must be specified using the command-line
  options.

### Connect to MongoDB Instances Using Encryption

To connect to a `mongod` or `mongos` instance
that requires encrypted communication,
start `mongosh` with:

- `--tls`

- `--host` and `--tlsCAFile` to validate the server certificate.

For example, consider a `mongod` instance running on
`hostname.example.com` with the following options:

```bash
mongod --tlsMode requireTLS --tlsCertificateKeyFile <pem> 
```

To connect to the instance, start `mongosh` with
the following options:

```bash
mongosh --tls --host hostname.example.com --tlsCAFile /etc/ssl/caToValidateServerCertificates.pem
```

`mongosh` verifies the certificate presented by
the `mongod` instance against the specified hostname and
the CA file.

### Connect to MongoDB Instances that Require Client Certificates

To connect to a `mongod` or `mongos` that
requires CA-signed client certificates, start `mongosh` with:

- `--tls`

- `--host` and the `--tlsCAFile` to validate the server certificate,

- `--tlsCertificateKeyFile` option to specify
  the client certificate to present to the server.

For example, consider a `mongod` instance running on
`hostname.example.com` with the following options:

```bash
mongod --tlsMode requireTLS --tlsCertificateKeyFile /etc/ssl/mongodb.pem --tlsCAFile /etc/ssl/caToValidateClientCertificates.pem
```

To connect to the instance, start `mongosh` with the
following options:

```bash
mongosh --tls --host hostname.example.com --tlsCertificateKeyFile /etc/ssl/client.pem --tlsCAFile /etc/ssl/caToValidateServerCertificates.pem
```

#### Windows and macOS

To specify a client certificate from the system certificate store, use 
the `--tlsCertificateSelector` option instead of
`--tlsCertificateKeyFile`.

If the CA file is also in the system certificate store, you can omit the
`--tlsCAFile` option.

For example, if a certificate with the `CN` (Common Name) of
`myclient.example.net` and the accompanying CA file are both in the
macOS system certificate store, you can connect like this:

```bash
mongosh --tls  --host hostname.example.com --tlsCertificateSelector subject="myclient.example.net"
```

There are available in `mongosh`, but you should use the `tls`
alternatives instead.

### Avoid Use of `--tlsAllowInvalidCertificates` Option

**Warning:**

Although available, avoid using the
`--tlsAllowInvalidCertificates` option if possible. If the use of
`--tlsAllowInvalidCertificates` is necessary, only use the option on
systems where intrusion is not possible.

If `mongosh` runs with the
`--tlsAllowInvalidCertificates` option, `mongosh`
will not attempt to validate the server certificates. This
creates a vulnerability to expired `mongod` and
`mongos` certificates as well as to foreign processes
posing as valid `mongod` or `mongos`
instances. If you only need to disable the validation of the
hostname in the TLS/SSL certificates, see
`--tlsAllowInvalidHostnames`.

## MongoDB Atlas, MongoDB Cloud Manager and MongoDB Ops Manager

MongoDB Atlas uses TLS/SSL to encrypt the connections to your databases.

The MongoDB Cloud Manager and Ops Manager Monitoring agents use encrypted communication
to gather its statistics. Because the agents already encrypt
communications to the MongoDB Cloud Manager/Ops Manager servers, this is just a matter
of enabling TLS/SSL support in MongoDB Cloud Manager/Ops Manager on a per host basis.

For more information, see:

- [MongoDB Atlas documentation](https://docs.atlas.mongodb.com/setup-cluster-security/)

- `MongoDB Cloud Manager documentation` 

- `MongoDB Ops Manager documentation`.

## MongoDB Drivers

The MongoDB Drivers support encrypted communication. For details, see:

- [C Driver](https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/guides/configuring_tls/)
- [C++ Driver](https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/configuration/#configuring-tls-ssl)
- [C# Driver](https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/connection/tls/)
- [Java Driver](https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/connection/tls/)
- [Node.js Driver](https://www.mongodb.com/docs/drivers/node/current/fundamentals/connection/tls/)
- [PHP Driver](https://php.net/manual/en/mongodb-driver-manager.construct.php)
- [Python Driver](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/tls/)
- [Ruby Driver](https://www.mongodb.com/docs/ruby-driver/current/reference/authentication/#client-certificate--x.509-)
- [Scala Driver](https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/connect/tls/)

## MongoDB Tools

Various MongoDB utility programs support encrypted communication. These
tools include:

- `mongodump`
- `mongoexport`
- `mongofiles`
- `mongoimport`
- `mongorestore`
- `mongostat`
- `mongotop`

To use encrypted communication with these tools, use the same `tls` options as
`mongosh`. See mongo-shell-tls-connect.

**See also:**

configure-mongod-mongos-for-tls-ssl
