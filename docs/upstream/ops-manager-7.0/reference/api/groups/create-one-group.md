<!-- Converted from reference/api/groups/create-one-group.txt (reStructuredText). Includes are inlined. -->

# Create One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Required Roles

To create a project within an existing organization, you must have
one of the following roles in the specified organization:

- `Organization Project Creator`
- `Organization Owner`

**Note:**

If you create a project using an API (Application Programming Interface) key from an organization 
without an `Organization Owner`, Ops Manager creates the project 
without a `Project Owner`.

## Resource

```http
POST /groups
```

## Request Parameters

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

* - Name
  - Type
  - Necessity
  - Description
  - Default

* - pretty
  - boolean
  - Optional
  - Flag indicating whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Optional
  - Flag that indicates whether or not to wrap the response in an
    envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set **envelope=true** in the
    query.

    For endpoints that return one result, the response body
    includes:

    | Name | Description |
    |---|---|
    | status | HTTP (Hypertext Transfer Protocol) response code |
    | envelope | Expected response body |

  - `false`

### Request Body Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| name | string | Required | Human-readable label that identifies the project. |
| orgId | string | Required | Unique 24-hexadecimal digit string that identifies the organization within which to create the project. Ops Manager set the oldest `Organization Owner` of the specified organization as a `Project Owner` for the new project. |

## Response

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
 --header "Content-Type: application/json" \
 --include \
 --request POST "https://{opsManagerHost}:{port}/api/public/v1.0/groups?pretty=true" \
 --data '
   {
     "name": "Create Project API Example",
     "orgId": "deffb2031b938da53f16d714"
   }'
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
HTTP/1.1 201 Created
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
  "activeAgentCount" : 0,
  "agentApiKey": "{GROUP-API-KEY}",
  "hostCounts" : {
    "arbiter" : 0,
    "config" : 0,
    "primary" : 0,
    "secondary" : 0,
    "mongos" : 0
  },
  "id" : "{PROJECT-ID}",
  "ldapGroupMappings" : [ {
    "roleName": "GROUP_OWNER",
    "ldapGroups": [  project-owner" ]
  }, ... ],
  "links" : [],
  "name" : "Create Project API Test",
  "orgId" : "deffb2031b938da53f16d714",
  "publicApiEnabled": true,
  "replicaSetCount" : 0,
  "shardCount" : 0,
  "tags": [ "DEV", "PRODUCT" ]
}
```
