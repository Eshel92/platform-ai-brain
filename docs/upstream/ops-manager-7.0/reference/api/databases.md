<!-- Converted from reference/api/databases.txt (reStructuredText). Includes are inlined. -->

# Databases

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available for `databases`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases | Retrieve all MongodDB processes running on the specified host. |
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME} | Retrieve a single MongoDB process from the specified host by name. |
