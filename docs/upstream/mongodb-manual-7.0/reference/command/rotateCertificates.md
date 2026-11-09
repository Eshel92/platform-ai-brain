<!-- Converted from reference/command/rotateCertificates.txt (reStructuredText). Includes are inlined. -->

# rotateCertificates (database command)

## Definition

**New in version:** 5.0

**`rotateCertificates`**

Rotates the currently used TLS certificates for a `mongod` or
`mongos` to use the updated values for these
certificates defined in the configuration file.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

Atlas automatically rotates the certificates. You don't need to run
the `rotateCertificates` command when using Atlas. Use the
`rotateCertificates` command only if you want to rotate the
certificates manually.

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     rotateCertificates: 1,
     message: "<optional log message>" 
   }
)
```

## Command Fields

The command takes the following optional field:

| Parameter | Type | Description |
|---|---|---|
| `message` | string | *optional* A message logged by the server to the log file and audit file. |

## Output

The `rotateCertificates` command returns a document with
the following field:

| Field | Type | Description |
|---|---|---|
| `ok` | bool | Contains the command's execution status. `true` on success, or `false` if an error occurred. If `false`, an `errmsg` field is additionally provided with a detailed error message. |

## Behavior

Rotation includes the following certificates:

- `TLS Certificates`
- `CRL (Certificate Revocation List) files`
  (on Linux and Windows platforms)
- `CA (Certificate Authority) files`

To rotate one or more of these certificates:

#. Replace the certificate or certificates you wish to rotate on the
   filesystem, noting the following constraints:
   
   - Each new certificate must have the *same filename* and
     *same filepath* as the certificate it is replacing.

   - If rotating an encrypted `TLS Certificate`, its password must be the same as
     the password for the old certificate (as specified to the
     `certificateKeyFilePassword` configuration file
     setting). Certificate rotation does not support the interactive
     password prompt.

#. Connect `mongosh` to the `mongod` or
   `mongos` instance that you wish to perform certificate
   rotation on.

#. Run the `rotateCertificates` command to rotate the
   certificates used by the `mongod` or
   `mongos` instance.

When certificate rotation takes place:

- Existing connections to the `mongod` or
  `mongos` instance are not terminated, and will continue
  to use the old certificates.

- Any new connections will use the new certificates.

If you have configured `OCSP` for your
deployment, the `rotateCertificates` command will also fetch
stapled OCSP responses during rotation.

The `rotateCertificates` command may be run on a running
`mongod` or `mongos` regardless of replication
status.

Only one instance of `db.rotateCertificates()` or
`rotateCertificates` may run on each `mongod` or
`mongos` process at a time. Attempting to initiate a second
instance while one is already running will result in an error.

Incorrect, expired, revoked, or missing certificate files will cause the
certificate rotation to fail, but will not invalidate the existing
TLS configuration or terminate the running `mongod` or
`mongos` process.

If the `mongod` or `mongos` is running with
`--tlsCertificateSelector` set
to `thumbprint`, `rotateCertificates` will fail and write
a warning message to the log file.

## Logging

On successful rotation, the subject names, thumbprints, and the
validity period of the server and cluster certificate thumbprints are
logged to the configured log destination. If auditing is
enabled, this information is also written to the audit log.

On Linux and Windows platforms, if a `CRL file` is present, its thumbprint and validity period are
also logged to these locations.

## Required Access

You must have the `rotateCertificates` action in order to use the `rotateCertificates` command. The
`rotateCertificates` action is part of the
`hostManager` role.

## Example

The following operation rotates the certificates on a running
`mongod` instance, after having made the appropriate
updates to the configuration file to specify the updated certificate
information:

```javascript
db.adminCommand( { rotateCertificates: 1 } )
```

The following performs the same as above, but also writes a custom log
message at rotation time to the log file and audit file:

```javascript
db.adminCommand( { rotateCertificates: 1, message: "Rotating certificates" } )
```
