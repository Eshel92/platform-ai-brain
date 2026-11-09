<!-- Converted from reference/api/global-api-key-access-lists.txt (reStructuredText). Includes are inlined. -->

# Global Programmatic API Key Access List

**Note:**

The `whitelist` resource is deprecated for Ops Manager 5.0 and later. 
Use the `accessList` resource instead to control access to 
API operations.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Use the `/admin/accessList` resource to view, create, or delete
Global Access List Entries, used in conjunction with Global Programmatic API Keys.

**See also:**

To learn more about Global Access List Entries, see
access-list-page-admin-ui.

## Permissions

To use these endpoints, grant the following roles to an Project API (Application Programming Interface)
Key or user in your Organization:

| Role | Possible Action |
|---|---|
| Any Global role | Retrieve Global Access List Entries |
| `Global Owner` or `Global User Admin` | Create, update, or delete a Global Access List Entry |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /admin/accessList | Get all global access list entries. |
| `GET` | /admin/accessList/{ACCESS-LIST-ID} | Get one global access list entry. |
| `POST` | /admin/accessList | Create one global access list entry. |
| `PATCH` | /admin/accessList/{ACCESS-LIST-ID} | Update the global access list entry specified by `{ACCESS-LIST-ID}`. |
| `DELETE` | /admin/accessList/{ACCESS-LIST-ID} | Delete the global access list entry specified by `{ACCESS-LIST-ID}`. |
