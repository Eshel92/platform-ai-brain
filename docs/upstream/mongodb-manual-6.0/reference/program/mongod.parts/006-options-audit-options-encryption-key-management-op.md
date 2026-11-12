<!-- Part 6 of 6 of reference/program/mongod.md (split because the page is big). -->

### Audit Options

**`--auditCompressionMode`**

**New in version:** 5.3

Specifies the compression mode for audit log encryption. You must also enable audit log
encryption using either `--auditEncryptionKeyUID` or
`--auditLocalKeyFile`.

`--auditCompressionMode` can be set to one of these values:

| Value | Description |
|---|---|
| `zstd` | Use the zstd algorithm to compress the audit log. |
| `none` *(default)* | Do not compress the audit log. |

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`--auditDestination`**

Enables auditing and specifies where
`mongod` sends all audit events.

`--auditDestination` can have one of the following values:

| Value | Description |
|---|---|
| `syslog` | Output the audit events to syslog in JSON format. Not available on Windows. Audit messages have a syslog severity level of `info` and a facility level of `user`. The syslog message limit can result in the truncation of audit messages. The auditing system neither detects the truncation nor errors upon its occurrence. |
| `console` | Output the audit events to `stdout` in JSON format. |
| `file` | Output the audit events to the file specified in `--auditPath` in the format specified in `--auditFormat`. |

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`--auditEncryptionKeyUID`**

**New in version:** 6.0

Specifies the unique identifier of the Key Management
Interoperability Protocol (KMIP) key for audit log encryption.

You cannot use `--auditEncryptionKeyUID` and
`--auditLocalKeyFile` together.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

   

**`--auditFormat`**

Specifies the format of the output file for auditing if `--auditDestination` is `file`. The
`--auditFormat` option can have one of the following values:

| Value | Description |
|---|---|
| `JSON` | Output the audit events in JSON format to the file specified in `--auditPath`. |
| `BSON` | Output the audit events in BSON binary format to the file specified in `--auditPath`. |

Printing audit events to a file in JSON format degrades server
performance more than printing to a file in BSON format.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`--auditLocalKeyFile`**

**New in version:** 5.3

Specifies the path and file name for a local audit key file for
audit log encryption.

**Note:**

Only use `--auditLocalKeyFile` for testing because the key is
not secured. To secure the key, use
`--auditEncryptionKeyUID` and an external Key
Management Interoperability Protocol (KMIP) server.

You cannot use `--auditLocalKeyFile` and
`--auditEncryptionKeyUID` together.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`--auditPath`**

Specifies the output file for auditing if
`--auditDestination` has value of `file`. The `--auditPath`
option can take either a full path name or a relative path name.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`--auditFilter`**

Specifies the filter to limit the types of operations the audit system records. The option takes a string representation
of a query document of the form:

```javascript
{ <field1>: <expression1>, ... }
```

The `<field>` can be any field in the audit message, including fields returned in the
param document. The
`<expression>` is a query condition expression.

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).


### SNMP Options

**Note:**

MongoDB Enterprise on macOS does *not* include support for SNMP due
to SERVER-29352.

**`--snmp-disabled`**

Disables SNMP access to `mongod`. The option is incompatible
with `--snmp-subagent` and `--snmp-master`.

**`--snmp-subagent`**

Runs SNMP as a subagent. The option is incompatible with `--snmp-disabled`.

**`--snmp-master`**

Runs SNMP as a master. The option is incompatible with `--snmp-disabled`.

**See also:**

- /tutorial/monitor-with-snmp
- /tutorial/monitor-with-snmp-on-windows
- /tutorial/troubleshoot-snmp


### inMemory Options

**`--inMemorySizeGB <float>`**

*Default*: 50% of physical RAM minus 1 GB.

Maximum amount of memory to allocate for the in-memory storage
engine data, including indexes, the oplog (if the
`mongod` is part of a replica set), sharded
cluster metadata, etc.

Values can range from 256MB to 10TB and can be a float.

By default, the in-memory storage engine uses 50% of physical RAM minus
1 GB.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   


### Encryption Key Management Options

**`--enableEncryption`**

*Default*: false

Enables encryption for the WiredTiger storage engine. This option
must be enabled in order to pass in encryption keys and
configurations.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`--encryptionCipherMode <string>`**

*Default*: AES256-CBC

The cipher mode to use for encryption at rest:

| Mode | Description |
|---|---|
| `AES256-CBC` | 256-bit Advanced Encryption Standard in Cipher Block Chaining Mode |
| `AES256-GCM` | 256-bit Advanced Encryption Standard in Galois/Counter Mode Available only on Linux. MongoDB Enterprise on Windows no longer supports `AES256-GCM` as a block cipher for encryption at rest. This usage is only supported on Linux. |

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`--encryptionKeyFile <string>`**

The path to the local keyfile when managing keys via process *other
than* KMIP. Only set when managing keys via process other than KMIP.
If data is already encrypted using KMIP, MongoDB throws an error.

The keyfile can contain only a single key. The key is either a 16 or
32 character string.

Requires `--enableEncryption`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`--kmipKeyIdentifier <string>`**

Unique KMIP identifier for an existing key within the KMIP server.
Include to use the key associated with the identifier as the system
key. You can only use the setting the first time you enable
encryption for the `mongod` instance. Requires
`--enableEncryption`.

If unspecified, MongoDB requests that the KMIP server create a
new key to utilize as the system key.

If the KMIP server cannot locate a key with the specified identifier
or the data is already encrypted with a key, MongoDB throws an
error

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`--kmipRotateMasterKey <boolean>`**

*Default*: false

If true, rotate the master key and re-encrypt the internal
keystore.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**See also:**

kmip-master-key-rotation

   

**`--kmipServerName <string>`**

Hostname or IP address of the KMIP server to connect to. Requires
`--enableEncryption`.

You can specify multiple KMIP servers as a comma-separated list, for example:
`server1.example.com,server2.example.com`. On startup, the
`mongod` attempts to establish a connection to each
server in the order listed, and selects the first server to
which it can successfully establish a connection. KMIP server
selection occurs only at startup.

When connecting to a KMIP server, the `mongod`
verifies that the specified `--kmipServerName` matches the
Subject Alternative Name `SAN` (or, if `SAN` is not present, the
Common Name `CN`) in the certificate presented by the KMIP server.
If `SAN` is present, `mongod` does not match against
the `CN`. If the hostname does not match the `SAN` (or `CN`),
the `mongod` fails to connect.

Starting in MongoDB 4.2, when performing comparison of SAN, MongoDB
supports comparison of DNS names or IP addresses. In previous versions,
MongoDB only supports comparisons of DNS names.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`--kmipPort <number>`**

*Default*: 5696

Port number to use to communicate with the KMIP server.
Requires `--kmipServerName`. Requires
`--enableEncryption`.

If specifying multiple KMIP servers with `--kmipServerName`,
the `mongod` uses the port specified with
`--kmipPort` for all provided KMIP servers.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`--kmipConnectRetries <number>`**

*Default*: 0

How many times to retry the initial connection to the KMIP server.
Use together with `--kmipConnectTimeoutMS` to
control how long the `mongod` waits for a response
between each retry.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`--kmipConnectTimeoutMS <number>`**

*Default*: 5000

Timeout in milliseconds to wait for a response from the KMIP server.
If the `--kmipConnectRetries` setting is specified,
the `mongod` waits for the specified interval between retries.

Value must be `1000` or greater.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`--kmipClientCertificateSelector <string>`**

**New in version:** 5.0

Available on Windows and macOS as an alternative to
`--kmipClientCertificateFile`. 

`--kmipClientCertificateFile` and `--kmipClientCertificateSelector` options are mutually exclusive. You can only
specify one.

Specifies a certificate property in order to select a matching
certificate from the operating system's certificate store to
authenticate MongoDB to the KMIP server.

`--kmipClientCertificateSelector` accepts an argument of the format `<property>=<value>`
where the property can be one of the following:

| Property | Value type | Description |
|---|---|---|
| `subject` | ASCII string | Subject name or common name on certificate |
| `thumbprint` | hex string | A sequence of bytes, expressed as hexadecimal, used to identify a public key by its SHA-1 digest. The `thumbprint` is sometimes referred to as a `fingerprint`. |

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`--kmipClientCertificateFile <string>`**

Path to the `.pem` file used to authenticate MongoDB to the KMIP
server. The specified `.pem` file must contain both the TLS/SSL
certificate and key. 

To use this option, you must also specify the
`--kmipServerName` option.

**Note:**

On macOS or Windows, you can use a certificate
from the operating system's secure store instead of a PEM key
file. See `--kmipClientCertificateSelector`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

**`--kmipClientCertificatePassword <string>`**

The password to decrypt the Private Key of the Client Certificate that
connects to the KMIP server. This option authenticates
MongoDB to the KMIP server and requires that you provide a
`--kmipClientCertificateFile`.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.

   

**`--kmipServerCAFile <string>`**

Path to CA File. Used for validating secure client connection to
KMIP server.

**Note:**

On macOS or Windows, you can use a certificate
from the operating system's secure store instead of a PEM key
file. See `--kmipClientCertificateSelector`. When using the secure 
store, you do not need to, but can, also specify the `--kmipServerCAFile`.

**`--kmipActivateKeys <boolean>`**

*Default*: true

**New in version:** 5.3

Activates all newly created KMIP keys upon creation and then periodically 
checks those keys are in an active state. 

When `--kmipActivateKeys` is `true` and you have existing keys on a 
KMIP server, the key must be activated first or the `mongod`
node fails to start. 

If the key being used by the mongod transitions into a non-active state, 
the `mongod` node shuts down unless `kmipActivateKeys` is 
false. To ensure you have an active key, rotate the KMIP master key by 
using `--kmipRotateMasterKey`.

**`--kmipKeyStatePollingSeconds <integer>`**

*Default*: 900 seconds 

**New in version:** 5.3

Frequency in seconds at which `mongod` polls the KMIP server for
active keys. 

To disable disable polling, set the value to `-1`.

**`--kmipUseLegacyProtocol <boolean>`**

*Default*: false 

**New in version:** 6.0.6

When `true`, `mongod` uses KMIP protocol version 1.0 or 1.1 instead
of the default version. The default KMIP protocol is version 1.2.

To use audit log encryption
with KMIP version 1.0 or 1.1, you must specify
`auditEncryptKeyWithKMIPGet` at startup.

**`--eseDatabaseKeyRollover`**

Roll over the encrypted storage engine database keys configured with
`AES256-GCM` cipher.

When `mongod` instance is started with this option, the
instance rotates the keys and exits.

**Note:** Enterprise Feature

Available in MongoDB Enterprise only.
