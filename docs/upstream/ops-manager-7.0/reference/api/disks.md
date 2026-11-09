<!-- Converted from reference/api/disks.txt (reStructuredText). Includes are inlined. -->

# Disks

Retrieves the disks and disk partitions on which MongoDB runs.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available for `hosts`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks | Retrieves all disk partitions on the specified host. |
| GET | /groups/{PROJECT-ID}/hosts/HOST-ID/disks/{PARTITION-NAME} | Retrieves a single disk partition. |
