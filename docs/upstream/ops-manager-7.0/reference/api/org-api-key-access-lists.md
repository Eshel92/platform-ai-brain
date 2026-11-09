<!-- Converted from reference/api/org-api-key-access-lists.txt (reStructuredText). Includes are inlined. -->

# Organization Programmatic API Key Access Lists

**Note:**

The `whitelist` resource is deprecated for Ops Manager 5.0 and later. 
Use the `accessList` resource instead to control access to 
API operations.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Use the `/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList` resource to
view, create, or delete access list entries for a user or
Programmatic API Key within the specified
Ops Manager organization.

The Organization API (Application Programming Interface) Key, or users with the
`Organization Owner` role in the
organization in which the
API Key belongs, can access these
endpoints.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList | Get all access list entries that belong to `{API-KEY-ID}`. |
| `GET` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{IP-ADDRESS} | Get the access list entry for `{API-KEY-ID}` specified by `{IP-ADDRESS}`. |
| `POST` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList | Create one or more access list entries for `{API-KEY-ID}`. |
| `DELETE` | /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{IP-ADDRESS} | Delete the access list entry for `{API-KEY-ID}` specified by `{IP-ADDRESS}`. |
