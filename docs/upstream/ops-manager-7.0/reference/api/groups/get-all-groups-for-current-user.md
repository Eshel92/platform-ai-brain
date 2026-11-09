<!-- Converted from reference/api/groups/get-all-groups-for-current-user.txt (reStructuredText). Includes are inlined. -->

# Get All Projects for the Current User

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups
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

Each **result** is one project.

* - Name
  - Type
  - Description

* - activeAgentCount
  - integer
  - Number of active agents sending regular pings to Ops Manager.

    The value is refreshed about every 24 hours and cached. If
    you start a new agent or stop an existing one, the change
    can take up to 30 minutes to show up in the
    `activeAgentCount` field.

* - hostCounts
  - object
  - Total number of hosts by type. The embedded fields
    should be self-explanatory.

* - id
  - string
  - Unique identifier for the project.

* - lastActiveAgent
  - string
  - Time Ops Manager last updated the `activeAgentCount` total for
    the project. Ops Manager refreshes this value every 24 hours and
    caches it to record the number of active MongoDB Agents.

* - ldapGroupMappings
  - object array
  - For LDAP-backed Ops Manager, the mappings of
    LDAP groups
    to Ops Manager project roles. Only present for LDAP-backed
    Ops Manager.

* - | ldapGroupMappings
    | .roleName
  - string
  - Ops Manager user role. The mapping of
    Project Role to `roleName`
    follows:

    | User Role | `roleName` Value |
    |---|---|
    | `Project Owner` (required) | `GROUP_OWNER` |
    | `Project Automation Admin` | `GROUP_AUTOMATION_ADMIN` |
    | `Project Backup Admin` | `GROUP_BACKUP_ADMIN` |
    | `Project Monitoring Admin` | `GROUP_MONITORING_ADMIN` |
    | `Project Data Access Admin` | `GROUP_DATA_ACCESS_ADMIN` |
    | `Project Data Access Read/Write` | `GROUP_DATA_ACCESS_READ_WRITE` |
    | `Project Data Access Read Only` | `GROUP_DATA_ACCESS_READ_ONLY` |
    | `Project Read Only` | `GROUP_READ_ONLY` |

* - | ldapGroupMappings
    | .ldapGroups
  - string array
  - LDAP project(s) that map to the Ops Manager role.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - name
  - string
  - Display name for the project.

* - orgId
  - string
  - Unique identifier for the organization to which the project
    belongs.

* - publicApiEnabled
  - boolean
  - Flag indicating that the API (Application Programming Interface) is enabled for this project.
    This is a read-only field that is always `true`.

* - replicaSetCount
  - integer
  - Total number of replica sets for this project.

* - shardCount
  - integer
  - Total number of shards for this project.

* - tags
  - string array
  - Tags assigned to the project for use in programmatically
    identifying the project.

    - To *view* tags you must have the
      `Project Read Only`
      role.

    - To *create* or *edit* tags you must have the
      `Project Automation Admin` role.

    A project can have up to 10 tags. Tags follow these rules:

    - Are case-sensitive

    - Can contain these characters:

      - `A` through `Z`
      - `0` through `9`
      - `.` (period)
      - `_` (underscore)
      - `-` (dash)

    - Are limited to 32 characters

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups?pretty=true"
```

### Example Response

#### Response Header

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

#### Response Body

```json
{
  "links": [{
    "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups?pretty=true&pageNum=1&itemsPerPage=100",
    "rel": "self"
  }, {
    "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups?pretty=true&itemsPerPage=100&pageNum=2",
    "rel": "next"
  }],
  "results": [{
    "activeAgentCount": 0,
    "hostCounts": {
      "arbiter": 0,
      "config": 0,
      "mongos": 0,
      "primary": 0,
      "secondary": 0
    },
    "id": "56a10a80e4b0fd3b9a9bb0c2",
    "lastActiveAgent": "2016-03-09T18:19:37Z",
    "links": [{
      "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}",
      "rel": "self"
    }],
    "name": "012i3091203jioawjioej",
    "orgId": "5980cfdf0b6d97029d82f86e",
    "publicApiEnabled": true,
    "replicaSetCount": 0,
    "shardCount": 0,
    "tags": []
  }, {
    "activeAgentCount": 0,
    "hostCounts": {
      "arbiter": 0,
      "config": 0,
      "mongos": 0,
      "primary": 0,
      "secondary": 0
    },
    "id": "56aa691ce4b0a0e8c4be51f7",
    "lastActiveAgent": "2016-01-29T19:02:56Z",
    "links": [{
      "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}",
      "rel": "self"
    }],
    "name": "1454008603036",
    "orgId": "5980d0040b6d97029d831798",
    "publicApiEnabled": true,
    "replicaSetCount": 0,
    "shardCount": 0,
    "tags": []
  }, {
    "activeAgentCount": 0,
    "hostCounts": {
      "arbiter": 0,
      "config": 0,
      "mongos": 0,
      "primary": 0,
      "secondary": 0
    },
    "id": "56aa6dfde4b0fe328eee82ad",
    "lastActiveAgent": "2016-01-29T20:34:28Z",
    "links": [{
      "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}",
      "rel": "self"
    }],
    "name": "1454009852809",
    "orgId": "5980d0040b6d97029d831799",
    "publicApiEnabled": true,
    "replicaSetCount": 0,
    "shardCount": 0,
    "tags": []
  }, {
    "activeAgentCount": 0,
    "hostCounts": {
      "arbiter": 0,
      "config": 0,
      "mongos": 0,
      "primary": 0,
      "secondary": 0
    },
    "id": "56aa8421e4b0d04c1c54df99",
    "lastActiveAgent": "2016-01-29T21:36:10Z",
    "links": [{
      "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}",
      "rel": "self"
    }],
    "name": "1454015520776",
    "orgId": "5980d0040b6d97029d83179a",
    "publicApiEnabled": true,
    "replicaSetCount": 0,
    "shardCount": 0,
    "tags": []
  }, {
    "activeAgentCount": 0,
    "hostCounts": {
      "arbiter": 0,
      "config": 0,
      "mongos": 0,
      "primary": 0,
      "secondary": 0
    },
    "id": "56aa85f9e4b0d04c1c54e347",
    "lastActiveAgent": "2016-01-29T21:36:10Z",
    "links": [{
      "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}",
      "rel": "self"
    }],
    "name": "1454015992252",
    "orgId": "5980d0040b6d97029d83179b",
    "publicApiEnabled": true,
    "replicaSetCount": 0,
    "shardCount": 0,
    "tags": []
  }],
  "totalCount": 5
}
```
