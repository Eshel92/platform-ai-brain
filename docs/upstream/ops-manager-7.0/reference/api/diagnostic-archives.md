<!-- Converted from reference/api/diagnostic-archives.txt (reStructuredText). Includes are inlined. -->

# Diagnostic Archives

MongoDB engineers may request that Ops Manager administrators provide
diagnostic archives for one project for debugging and troubleshooting.
Project diagnostic archives also contain global system information
about Ops Manager.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Required Roles

The API Key requires the `Global Monitoring Admin` or
`Global Owner` role to download a diagnostic archive.

## Endpoints

The following lists the endpoints available for the diagnostic archive
resource.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /{PROJECT-ID}/diagnostics | Retrieves the project's diagnostics archive file. |
