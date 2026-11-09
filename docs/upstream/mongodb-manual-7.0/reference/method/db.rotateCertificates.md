<!-- Converted from reference/method/db.rotateCertificates.txt (reStructuredText). Includes are inlined. -->

# db.rotateCertificates() (mongosh method)

## Definition

**New in version:** 5.0

**`db.rotateCertificates(message)`**

Rotates the currently used TLS certificates for a `mongod` or
`mongos` to use the updated values for these
certificates defined in the configuration file.

```javascript
db.rotateCertificates(message)
```

The `db.rotateCertificates()` method takes the following
optional argument:

| Parameter | Type | Description |
|---|---|---|
| `message` | string | *optional* A message logged by the server to the log file and audit file. |

The `db.rotateCertificates()` method wraps the
`rotateCertificates` command.

## Compatibility

This method is available in deployments hosted in the following environments: 

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

Atlas automatically rotates the certificates. You don't need to run
the `rotateCertificates` command when using Atlas. Use the
`rotateCertificates` command only if you want to rotate the
certificates manually.

              

## Output

The `db.rotateCertificates()` method returns a document with
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

#. Run `db.rotateCertificates()` to rotate the certificates used
   by the `mongod` or `mongos` instance.

When certificate rotation takes place:

- Existing connections to the `mongod` or
  `mongos` instance are not terminated, and will continue
  to use the old certificates.

- Any new connections will use the new certificates.

If you have configured `OCSP` for your
deployment, the `db.rotateCertificates()` method will also fetch
stapled OCSP responses during rotation.

The `db.rotateCertificates()` method may be run on a running
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
to `thumbprint`, `db.rotateCertificates()` will fail and write
a warning message to the log file.

## Logging

On successful rotation, the subject names, thumbprints, and the
validity period of the server and cluster certificate thumbprints are
logged to the configured log destination. If auditing is
enabled, this information is also written to the audit log.

On Linux and Windows platforms, if a `CRL file` is present, its thumbprint and validity period are
also logged to these locations.

## Required Access

You must have the `rotateCertificates` action in order to use the `db.rotateCertificates()` method. The
`rotateCertificates` action is part of the
`hostManager` role.

## Example

The following operation rotates the certificates on a running
`mongod` instance, after having made the appropriate
updates to the configuration file to specify the updated certificate
information:

```javascript
db.rotateCertificates()
```

The following performs the same as above, but also writes a custom log
message at rotation time to the log file and audit file:

```javascript
db.rotateCertificates("message": "Rotating certificates")
```
