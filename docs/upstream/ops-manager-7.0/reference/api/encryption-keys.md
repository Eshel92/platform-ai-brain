<!-- Converted from reference/api/encryption-keys.txt (reStructuredText). Includes are inlined. -->

# Backup Encryption Keys

**Important:**

This endpoint works with backups of MongoDB databases running FCV
4.0 or earlier. Backups of MongoDB databases running FCV
4.2 or later use the
deployment's encryption setting.

MongoDB Enterprise enables administrators to encrypt
backups. Administrators must integrate with a KMIP (Key Management Interoperability) server. This
server generates and manages a master key that Ops Manager uses to encrypt
the head databases during a backup operation. MongoDB recommends
periodically rotating the KMIP (Key Management Interoperability) master key for increased security.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available for `encryptionKeys`.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/encryptionKey | Retrieve the KMIP (Key Management Interoperability) Master Key ID. |
| `PUT` | /groups/{PROJECT-ID}/backupConfigs/CLUSTER-ID/encryptionKey | Rotate the KMIP (Key Management Interoperability) Master Key. |
