<!-- Converted from reference/api/teams/teams-update-roles.txt (reStructuredText). Includes are inlined. -->

# Update Team Roles in One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```http
PATCH /groups/{PROJECT-ID}/teams/{TEAM-ID}
```

### Request Path Parameters

| Path Parameter | Type | Necessity | Description |
|---|---|---|---|
| `PROJECT-ID` | string | Required | Unique identifier of the project associated with this team. |
| `TEAM-ID` | string | Required | Unique identifier of the team for which you want to update roles. |

### Request Query Parameters

| Query Parameter | Type | Necessity | Description |
|---|---|---|---|
| `envelope` | boolean | Optional | Flag that specifies whether or not to wrap the response in an envelope. Defaults to `false`. |
| `pretty` | boolean | Optional | Flag that specifies whether or not to return a "pretty-printed" JSON (Javascript Object Notation) document. Defaults to `false`. |

### Request Body Parameters

Specify an array of strings, where each string represents one role
you want to add to the team. You must specify an array even if you are
only associating a single role to the team.

| Body Parameter | Type | Necessity | Description |
|---|---|---|---|
| `roleNames` | array | Required | Project roles you want to assign the given team. |

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

Each element in the `result` array is one set of roles specified for
one team.

| Response Parameter | Type | Description |
|---|---|---|
| `roleNames` | array | Project roles assigned to the team for the specified `teamsId`. |
| `teamsId` | string | Unique identifier of the team assigned the listed roles. |

## Example

### Request

```shell
   curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --request PATCH "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID3}?pretty=true" \
    --data '{
        "roleNames": ["GROUP_OWNER"]
      }'
```

### Response

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

```json
{
  "links": [{
    "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID3}?pretty=true&pageNum=1&itemsPerPage=100",
    "rel": "self"
  }],
  "results": [{
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID1}",
      "rel": "self"
    }],
    "roleNames": ["GROUP_OWNER", "GROUP_BACKUP_ADMIN", "GROUP_DATA_ACCESS_READ_ONLY", "GROUP_AUTOMATION_ADMIN", "GROUP_DATA_ACCESS_ADMIN", "GROUP_USER_ADMIN", "GROUP_DATA_ACCESS_READ_WRITE", "GROUP_READ_ONLY"],
    "teamId": "{TEAM-ID1}"
  }, {
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID2}",
      "rel": "self"
    }],
    "roleNames": ["GROUP_DATA_ACCESS_ADMIN", "GROUP_READ_ONLY"],
    "teamId": "{TEAM-ID2}"
  }, {
    "links": [{
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/teams/{TEAM-ID3}",
      "rel": "self"
    }],
    "roleNames": ["GROUP_OWNER"],
    "teamId": "{TEAM-ID3}"
  }],
  "totalCount": 3
}
```
