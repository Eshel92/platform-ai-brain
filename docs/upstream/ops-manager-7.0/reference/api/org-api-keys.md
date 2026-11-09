<!-- Converted from reference/api/org-api-keys.txt (reStructuredText). Includes are inlined. -->

# Organization Programmatic API Keys

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Use the `/orgs/{ORG-ID}/apiKeys` resource to view, create, or delete
Programmatic :abbr:API (Application Programming Interface)` Keys <mms-prog-api-key>` within the specified
Ops Manager organization.

## Permissions

To use these endpoints, grant the following roles to an Project API (Application Programming Interface) Key or user in your Organization:

| Role | Possible Action |
|---|---|
| Any role in the Organization | Retrieve Organization API (Application Programming Interface) Keys |
| `Organization Owner` or `Organization User Admin` | Create, update, or delete a Organization API (Application Programming Interface) Key |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /orgs/{ORG-ID}/apiKeys | Get all API (Application Programming Interface) Keys for the organization identified with `{ORG-ID}`. |
| `GET` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID} | Get one API (Application Programming Interface) Key for the organization identified with `{ORG-ID}`. |
| `POST` | /orgs/{ORG-ID}/apiKeys | Create an API (Application Programming Interface) Key for the organization identified with `{ORG-ID}`. |
| `PATCH` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID} | Update one API (Application Programming Interface) Key for the organization identified with `{ORG-ID}`. |
| `DELETE` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID} | Delete the API (Application Programming Interface) Key with ID `{API-KEY-ID}`. |
