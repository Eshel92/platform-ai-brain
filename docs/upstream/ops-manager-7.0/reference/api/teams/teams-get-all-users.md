<!-- Converted from reference/api/teams/teams-get-all-users.txt (reStructuredText). Includes are inlined. -->

# Get All Users Assigned to a Team

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
GET /orgs/{ORG-ID}/teams/{TEAM-ID}/users
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `ORG-ID` | Required | The unique identifier for the organization associated with the team. |
| `TEAM-ID` | Required | The unique identifier of the team whose user membership you want to retrieve. |

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

This endpoint doesn't use HTTP request body parameters.

## Response

### Response Document

The response JSON (Javascript Object Notation) document includes an array of result
objects, an array of link objects and a count of the total
number of result objects retrieved.

| Name | Type | Description |
|---|---|---|
| `results` | array | Array includes one object for each item detailed in the results-embedded-document-get-all section. |
| `links` | array | Array includes one or more links to sub-resources and/or related resources. The relations between URL (Uniform Resource Locator)\s are explained in the Web Linking Specification. |
| `totalCount` | number | Integer count of the total number of items in the result set. It may be greater than the number of objects in the results array if the entire result set is paginated. |

### `results` Embedded Document

Each element in the `result` array is one user assigned to the team.

| Name | Type | Description |
|---|---|---|
| `emailAddress` | string | The email address associated to the user. |
| `firstName` | string | The first name of the user. |
| `id` | string | The unique identifier for the team. |
| `lastName` | string | The last name of the user. |
| `links` | object array | .. include:: /includes/links-explanation.rst |
| `roles` | array | Each object in the `roles` array represents the MongoDB Atlas organization role the user has for the associated `orgId` or `groupId`. |
| `roles.orgId` | string | ID of the organization where the user has the assigned `roles.roleName` organization role. |
| `roles.groupId` | string | ID of the project where the user has the assigned `roles.roleName` project role. |
| `roles.roleName` | string | The organization role assigned to the user for the specified `roles.orgId` or `roles.groupId`. |
| `teamsIds` | array | Array of string IDs for each team the user is a member of. |
| `username` | string | Username associated to the user. |

## Example Request

```shell
curl --user "{username:apiKey}" --digest -i \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users?pretty=true"
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
  "links": [
      {
          "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users?pageNum=1&itemsPerPage=100",
          "rel": "self"
      }
  ],
  "results": [
      {
          "emailAddress": "CloudUser@example.com",
          "firstName": "Cloud",
          "id": "{USER-ID}",
          "lastName": "User",
          "links": [
              {
                  "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/users/{USER-ID}",
                  "rel": "self"
              }
          ],
          "roles": [
              {
                  "groupId": "{PROJECT-ID}",
                  "roleName": "GROUP_OWNER"
              },
              {
                  "orgId": "{ORG-ID}",
                  "roleName": "ORG_OWNER"
              }
          ],
          "teamIds": [
              "{TEAM-ID}"
          ],
          "username": "CloudUser@example.com"
      }
  ],
  "totalCount": 1
}
```
