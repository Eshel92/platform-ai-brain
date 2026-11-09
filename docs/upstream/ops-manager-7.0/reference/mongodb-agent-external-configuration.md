<!-- Converted from reference/mongodb-agent-external-configuration.txt (reStructuredText). Includes are inlined. -->

# Configure How the MongoDB Agent Manages Config Files and Passwords

**New in version:** 4.2

To meet advanced auditing or compliance needs, you may need to do one
or both of the following actions:

- Store the `mongod` or `mongos` (collectively, the MongoDB process)
  configuration in memory to avoid writing passwords to disk.
- Remove MongoDB Agent passwords from the MongoDB Agent configuration
  file and read the passwords passed in the shell command.

## Store MongoDB Process Configuration Files in Memory

MongoDB configuration files 
may contain credentials such as:

- `net.tls.certificateKeyFilePassword`
- `net.tls.clusterPassword`
- `security.kmip.clientCertificatePassword`
- `security.ldap.bind.queryPassword`

By default, the MongoDB Agent writes MongoDB process configuration files
to disk. However, you can store the configuration files in memory 
by setting `enableLocalConfigurationServer` to `true` 
in your 
MongoDB Agent configuration file. 
Changing this setting results in the following actions:

- The MongoDB Agent caches your MongoDB process configuration in memory.
- The MongoDB configuration file on disk contains only a
  `directive` that points to the full
  configuration file.

When the MongoDB Agent uses an in-memory MongoDB configuration, the MongoDB 
process requests the full configuration file from its local 
MongoDB Agent. The Agent requests the configuration file using the URL (Uniform Resource Locator) 
in the `__rest` expansion directive.

**Warning:**

If you use Ops Manager version 4.2 or versions 4.4.0 - 4.4.6, you may encounter
errors when setting `enableLocalConfigurationServer` to `true`. 
To avoid this, see store-conf-in-memory.

### Considerations

#### Impacts Availability of MongoDB Deployments

When this feature is enabled, the MongoDB Agent doesn't store the MongoDB
process configuration on disk. If the Ops Manager app server
is unavailable and the MongoDB Agent attempts to restart, then the
MongoDB Agent stops running because it doesn't have the necessary
configuration information. If a MongoDB process crashes while the
MongoDB Agent isn't running, then the MongoDB Agent can't restart the
process. 

#### Limits Importing Existing MongoDB Deployments

You can't import
MongoDB processes that store configuration files in memory. When the
MongoDB Agent stores its configuration in memory, MongoDB
redacts any credentials after it starts. Therefore, MongoDB
can't retrieve the credentials needed to import the process.

#### Private Key Format

If the encrypted private key for the `.pem` certificate file 
is in PKCS #8 format, 
it must use PBES2 encryption operations. 
The MongoDB Agent does not support PKCS #8 with other encryption 
operations.

## Remove Passwords from the MongoDB Agent Configuration File

You can set the MongoDB Agent to read its passwords as shell command
flags rather than read from its configuration file. To use this
feature, add the following settings to the MongoDB Agent\'s
configuration file:

- `mmsApiKeyExec`
- `tlsMMSServerClientCertificatePasswordExec`
