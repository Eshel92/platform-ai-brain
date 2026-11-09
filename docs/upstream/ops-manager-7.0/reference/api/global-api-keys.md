<!-- Converted from reference/api/global-api-keys.txt (reStructuredText). Includes are inlined. -->

# Global Programmatic API Keys

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Use the `/admin/apiKeys` resource to view, create, or delete
Global API Keys.

**See also:**

To learn more about Global Programmatic API Keys, see
API Keys.

## Permissions

To use these endpoints, grant the following roles to an Project API (Application Programming Interface)
Key or user in your Organization:

| Role | Possible Action |
|---|---|
| Any Global role | Retrieve Global API (Application Programming Interface) Keys |
| `Global Owner` or `Global User Admin` | Create, update, or delete a Global API (Application Programming Interface) Key |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /admin/apiKeys | Get all Global API (Application Programming Interface) Keys. |
| `GET` | /admin/apiKeys/roles | Get all roles for Global API (Application Programming Interface) Keys. |
| `GET` | /admin/apiKeys/{API-KEY-ID} | Get one API (Application Programming Interface) Key with ID `{API-KEY-ID}`. |
| `POST` | /admin/apiKeys | Create an API (Application Programming Interface) Key. |
| `PATCH` | /admin/apiKeys/{API-KEY-ID} | Update one API (Application Programming Interface) Key with ID `{API-KEY-ID}`. |
| `DELETE` | /admin/apiKeys/{API-KEY-ID} | Delete the API (Application Programming Interface) Key with ID `{API-KEY-ID}`. |
