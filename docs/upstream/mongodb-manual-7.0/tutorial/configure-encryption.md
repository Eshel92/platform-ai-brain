<!-- Converted from tutorial/configure-encryption.txt (reStructuredText). Includes are inlined. -->

# Configure Encryption

## Overview

This page discusses server configuration to support encryption at rest.
If you use [MongoDB Atlas](https://www.mongodb.com/atlas/database),
your data is already encrypted. MongoDB manages Atlas encryption at the
cloud provider level, but you can also use your own key management
solution. See the Atlas [key management documentation](https://docs.atlas.mongodb.com/security-kms-encryption/) for details.

MongoDB Enterprise 3.2 introduces a native encryption option for the
WiredTiger storage engine. Outside Atlas, encryption is only available
for enterprise installations that use the WiredTiger Storage Engine.

Secure management of the encryption keys is a critical requirement for
storage encryption. MongoDB uses a master key that is not stored with
the MongoDB installation. Only the master key is externally managed,
other keys can be stored with your MongoDB instance.

MongoDB's encrypted storage engine supports two key management options
for the master key:

- Integration with a third party key management appliance via the Key
  Management Interoperability Protocol (KMIP). **Recommended**
- Use of local key management via a keyfile.

**Important:**

MongoDB cannot encrypt existing data. When you enable encryption
with a new key, the MongoDB instance cannot have any pre-existing
data. If your MongoDB installation already has existing data, see
encrypt-existing-data for additional steps.

## Key Manager

MongoDB Enterprise supports secure transfer of keys with compatible key
management appliances. Using a key manager allows for the keys to be
stored in the key manager.

MongoDB Enterprise supports secure transfer of keys with Key Management
Interoperability Protocol (KMIP) compliant key management appliances.

For a list of MongoDB's certified partners,
refer to the [Partners List](https://www.mongodb.com/partners/list).

**Tip:** Recommended

Using a key manager meets regulatory key management guidelines, such
as HIPAA, PCI-DSS, and FERPA, and is recommended over the local key
management.

### Prerequisites

- Your key manager must support the KMIP communication protocol.

  The default KMIP protocol version is 1.2. You can configure MongoDB to
  use KMIP version 1.0 or 1.1 in the MongoDB server configuration
  file.

- .. include:: /includes/fact-required-kmip-ops.rst

- To authenticate MongoDB to a KMIP server, you must have a valid
  certificate issued by the key management appliance.

**Note:**

MongoDB Enterprise on Windows no longer supports `AES256-GCM` as a
block cipher for encryption at rest. This usage is only supported on Linux.

### Encrypt Using a New Key

To create a new key when you connect to the key manager, add an entry similar to
the following to your configuration file. Replace the strings and port number
with your values.

```yaml
security:
   enableEncryption: true
   kmip:
      serverName: "mdbhost.somecompany.com"
      port: 5696
      serverCAFile: "security/libs/trusted-ca.pem"
      clientCertificateFile: "security/libs/trusted-client.pem"
```

For more information on these options, see encryption-key-management-conf-options.

To connect to a version 1.0 or 1.1 KMIP server, set the
`security.kmip.useLegacyProtocol` configuration
option.

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

`mongod` verifies the connection to the KMIP server on startup.

The server name specified in `security.kmip.serverName` 
must match either the Subject Alternative Name `SAN` or the 
Common Name `CN` on the certificate presented by
the KMIP server. `SAN` can be a system name or an IP address. 

If `SAN` is present, `mongod` does not try to match against `CN`.

If the hostname or IP address of the KMIP server does does not match
either `SAN` or `CN`, `mongod` does not start.

To verify that the key creation and usage was successful, check the log
file. If successful, the process will log the following messages:

```bash
[initandlisten] Created KMIP key with id: <UID>
[initandlisten] Encryption key manager initialized using master key with id: <UID>
```

**See also:**

encryption-key-management-options

### Encrypt Using an Existing Key

You can use an existing master key that your KMIP server already
manages. To use an existing key, add an entry similar to
the following to your configuration file before you start `mongod`.
Replace the strings and port number with your values.

```yaml
security:
   enableEncryption: true
   kmip:
      keyIdentifier: "a29fba3-fd8327a2-74ba-43aa-bd3b-78a549a5295f"
      serverName: "mdbhost.somecompany.com"
      port: 5696
      serverCAFile: "security/libs/trusted-ca.pem"
      clientCertificateFile: "security/libs/trusted-client.pem"
```

For more information on these options, see encryption-key-management-conf-options.

To connect to a version 1.0 or 1.1 KMIP server, set the
`security.kmip.useLegacyProtocol` configuration
option.

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

`mongod` verifies the connection to the KMIP server on startup.

The server name specified in `security.kmip.serverName` 
must match either the Subject Alternative Name `SAN` or the 
Common Name `CN` on the certificate presented by
the KMIP server. `SAN` can be a system name or an IP address. 

If `SAN` is present, `mongod` does not try to match against `CN`.

If the hostname or IP address of the KMIP server does does not match
either `SAN` or `CN`, `mongod` does not start.

**See also:**

encryption-key-management-options

## Local Key Management

**Important:**

Using the keyfile method does not meet most regulatory key
management guidelines and requires users to securely manage their
own keys.

The safe management of the keyfile is critical.

To encrypt using a keyfile, you must have a base64 encoded keyfile that
contains a single 16 or 32 character string. The keyfile must only be
accessible by the owner of the `mongod` process.

#. Create the base64 encoded keyfile with the 16 or 32 character
   string. You can generate the encoded keyfile using any method you
   prefer. For example,

   ```bash
   openssl rand -base64 32 > mongodb-keyfile
   ```

#. Update the file permissions.

   ```bash
   chmod 600 mongodb-keyfile
   ```

#. To use the key file, start `mongod` with the following
   options:

   - `--enableEncryption`,

   - `--encryptionKeyFile <path to keyfile>`,

   ```bash
   mongod --enableEncryption --encryptionKeyFile  mongodb-keyfile
   ```

   Include additional options as required for your configuration. For
   instance, if you wish remote clients to connect to your deployment
   or your deployment members are run on different hosts, specify the
   `--bind_ip`. 

#. Verify if the encryption key manager successfully initialized with
   the keyfile. If the operation was successful, the process will log the
   following message:

   ```bash
   [initandlisten] Encryption key manager initialized with key file: <path to keyfile>
   ```

**See also:**

encryption-key-management-options

## Encrypt Existing Data at Rest

MongoDB cannot encrypt existing data. When you enable encryption with a
new key, the MongoDB instance cannot have any pre-existing data.

If you are using a replica set that does have existing data, use a
rolling initial sync to encrypt the
data. 

For example, consider a replica set with three members. The replica set
is in use and holds data that you want to encrypt. These are the steps
you would take to encrypt the data at rest:

**Step 1: Prepare a server.**

Follow these steps to prepare the server: 

- Pick one of the secondary servers. 
- Stop `mongod` on the secondary server.
- Optional: Backup the data in `dbPath`. If a full
  backup is not required, consider backing up just the
  `diagnostic.data` directory to preserve potentially-useful
  troubleshooting data in the event of an issue. See Full Time
  Diagnostic Data Capture for more information.
- Remove the files and directories in the
  `dbPath`.

**Step 2: Enable encryption.**

Start the secondary server with encryption enabled. The `mongod` instance creates
a new keystore.

**Step 3: Synchronize the data.**

Import the data from the primary. Start the mongod process, specifying
cli-mongod-replica-set as appropriate.

`mongod` performs an initial sync and encrypts the data
during the sync up process.

**Step 4: Repeat the process on the secondaries.**

When the first secondary has finished importing and encrypting the
data, repeat the process on the other secondary
`mongod` instances.

**Step 5: Encrypt the primary.**

When the all the secondaries have been encrypted, `step down` the primary. Eligible secondaries will elect a new 
primary.

The old primary is now a secondary. Repeat the steps to remove the
unencrypted data and then run an initial sync.
