<!-- Converted from reference/api/groups/project-get-teams.txt (reStructuredText). Includes are inlined. -->

# Get All Teams in One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
GET /groups/{PROJECT-ID}/teams
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `PROJECT-ID` | Required. | The unique identifier for the project. |

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

Each element in the `result` array is one team assigned to the
project.

| Name | Type | Description |
|---|---|---|
| `links` | object array | This array includes one or more links to sub-resources and/or related resources. The relations between URLs are explained in the [Web Linking Specification](http://tools.ietf.org/html/rfc5988). |
| `roleNames` | string array | Array of project roles assigned to the team. |
| `teamId` | string | The unique identifier for the team. |

## Example Request

```sh
curl -u "username:apiKey" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request GET "{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams?pretty=true"
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
         "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams",
         "rel": "self"
     }
 ],
 "results": [
     {
         "links" : [
           {
             "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID}",
             "rel": "self"
           }
         ],
         "roleNames": [
           "GROUP_READ_ONLY"
         ],
         "teamId": "{TEAM-ID}"
     }
 ],
 "totalCount": 1
}
```
