<!-- Converted from reference/api/organizations/organization-create-one.txt (reStructuredText). Includes are inlined. -->

# Create One Organization

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Required Roles

Your API Key must have the `Global Owner` role to
successfully call this resource.

**Note:**

If you use a global programmatic API key 
to create an organization, Ops Manager creates the organization 
without an `Organization Owner`. To add an `Organization Owner`, 
see /tutorial/manage-users.

## Request

```http
POST /orgs
```

## Request Parameters

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

### Request Body Parameters

* - Name
  - Type
  - Necessity
  - Description

* - `ldapGroupMappings`
  - array
  - Optional
  - Requires LDAP (Lightweight Directory Access Protocol) integration for Ops Manager.

    Array of documents that specify the mapping between the
    Ops Manager organization-roles and the LDAP groups.

    If specifying `ldapGroupMappings`, mapping for
    `ORG_OWNER` role is required.

* - | `ldapGroupMappings`
    | `.roleName`
  - string
  - Optional
  - Ops Manager organization role to map. Can specify from the
    following list:

    - `ORG_READ_ONLY`
    - `ORG_MEMBER`
    - `ORG_OWNER`

    You cannot specify a global role, project role,
    or an organization billing admin role.

* - | `ldapGroupMappings`
    | `.ldapGroups`
  - array
  - Optional
  - LDAP (Lightweight Directory Access Protocol) group(s) that map to associate to the `roleName`.

* - `name`
  - string
  - Required
  - Name of the organization you want to create.

## Response Parameters

| Name | Type | Description |
|---|---|---|
| `id` | string | Unique identifier for the organization. |
| `name` | string | Name of the organization. |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --header 'Accept: application/json' \
 --header 'Content-Type: application/json' \
 --include \
 --request POST "https://{opsManagerHost}:{port}/api/public/v1.0/orgs" \
 --data
   '{ "name" : "myNewOrganization" }'
```

## Example Response

### Response Header

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=ISO-8859-1
Date: {dateInUnixFormat}
WWW-Authenticate: Digest realm="MMS Public API", domain="", nonce="{nonce}", algorithm=MD5, op="auth", stale=false
Content-Length: {requestLengthInBytes}
Connection: keep-alive
```

```http
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

```json
{
  "id" : "{ORG-ID}",
  "name" : "myNewOrganization"
}
```
