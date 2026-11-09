<!-- Converted from reference/api/project-api-keys.txt (reStructuredText). Includes are inlined. -->

# Organization API Keys on Projects

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Use the following resources to view, create and assign, or unassign
Organization programmatic API Keys within
the specified Ops Manager project.

## Permissions

To use these endpoints, grant the following roles to an Project API (Application Programming Interface)
Key or user in your Organization:

| Role | Possible Action |
|---|---|
| Any role in the Project | Retrieve Project API (Application Programming Interface) Keys |
| `Project Owner` or `Project User Admin` | Create, update, or delete a Project API (Application Programming Interface) Key |
| `Project Owner` or `Project User Admin` | Assign or unassign an Organization API (Application Programming Interface) Key to a Project |

**Note:**

To configure an access list for a project API (Application Programming Interface) key, use the
Organization Programmatic API Key Access Lists endpoints.

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/apiKeys | Get All Organization API (Application Programming Interface) Keys Assigned to One Project with ID `{GROUP_ID}`. |
| `PATCH` | /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID} | Modify Roles of One Organization API (Application Programming Interface) Key with ID `{API-KEY-ID}` assigned to One Project with ID `{PROJECT-ID}`. |
| `POST` | /groups/{PROJECT-ID}/apiKeys | Create and Assign One Organization API (Application Programming Interface) Key with ID `{API-KEY-ID}` to One Project with ID `{PROJECT-ID}`. |
| `PATCH` | /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID} | Assign One Existing Organization API (Application Programming Interface) Key with ID `{API-KEY-ID}` to One Project with ID `{PROJECT-ID}`. |
| `DELETE` | /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID} | Unassign One Organization API (Application Programming Interface) Key with ID `{API-KEY-ID}` from One Project. |
