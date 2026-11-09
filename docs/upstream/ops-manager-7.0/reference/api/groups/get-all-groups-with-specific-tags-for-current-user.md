<!-- Converted from reference/api/groups/get-all-groups-with-specific-tags-for-current-user.txt (reStructuredText). Includes are inlined. -->

# Get All Projects with Specific Tags for the Current User

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

* - Name
  - Type
  - Description

* - tag
  - string
  - The tags assigned to the project for use in programmatically
    identifying the project.

    - To *view* tags you must have the `Project Read Only`
      role.

    - To *create* or *edit* tags you must have the
      `Project Automation Admin`
      role.

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
 --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups?tag=ABC&tag=DEF&pretty=true"
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
  "links": [],
  "results": [{
      "id": "xxx",
      "name": "My Project",
      "orgId": "111111111cccccf38dc78bdf",
      "hostCounts": {
        "arbiter": 2,
        "config": 1,
        "primary": 4,
        "secondary": 8,
        "mongos": 2
          },
      "lastActiveAgent": "2016-08-05T07:23:34Z",
      "activeAgentCount": 1,
      "replicaSetCount": 3,
      "shardCount": 2,
      "publicApiEnabled": true,
      "agentApiKey": "cbd728abd6a6d6c6b6d7826345dbcff0e",
      "tags": ["ABC", "DEF"],
      "ldapGroupMappings": [{
        "roleName": "GROUP_OWNER",
        "ldapGroups": [ "project-owner"]
      }],
      "links": []
    }
  ],
  "totalCount": 1
}
```
