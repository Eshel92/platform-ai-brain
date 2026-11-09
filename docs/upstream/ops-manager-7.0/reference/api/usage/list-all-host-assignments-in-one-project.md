<!-- Converted from reference/api/usage/list-all-host-assignments-in-one-project.txt (reStructuredText). Includes are inlined. -->

# List All Host Assignments In One Project

Retrieves all host assignments for one project.

## Required Roles

Your API Key must have the `Global Owner` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /usage/groups/{groupId}/hosts
```

### Request Path Parameters

Ops Manager requires all path parameters:

| Path Parameter | Type | Description |
|---|---|---|
| groupId | string | Unique identifier of the project associated with the desired hosts. |

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

| Query Parameter | Type | Necessity | Description | Default |
|---|---|---|---|---|
| startDate | string | Required | Date in ISO 8601 date format when the list of host assignments starts. |  |
| endDate | string | Required | Date in ISO 8601 date format when the list of host assignments ends. |  |
| pageNum | integer | Required | Starting group of host assignments to return. Group size gets defined in **itemsPerPage**. This value starts with 1. |  |
| itemsPerPage | integer | Required | Number of host assignments to return in one group. | `100` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

* - Response Element
  - Type
  - Description

* - hosts
  - array of strings
  - List of virtual hosts bound to the provided physical host.

* - | hosts
    | .groupId
  - string
  - Unique identifier of the project into which Ops Manager places this
    virtual host.

* - | hosts
    | .hostname
  - string
  - FQDN (fully qualified domain name) of the virtual host bound to the physical host.

* - processes
  - array of objects
  - MongoDB processes running on the virtual host.

* - | processes
    | .[n].cluster
  - object
  - Name of the cluster to which the MongoDB process belongs.

* - | processes
    | .[n].groupName
  - string
  - Name of the project to which the MongoDB process belongs.

* - | processes
    | .[n].orgName
  - string
  - Name of the organization to which the MongoDB process belongs.

* - | processes
    | .[n].groupId
  - string
  - Unique identifier of the project to which the MongoDB process
    belongs.

* - | processes
    | .[n].hasConflictingServerType
  - Boolean
  - Flag that indicates whether the node has a different server type
    than the other nodes.

* - | processes
    | .[n].name
  - string
  - Name of the node hosting the MongoDB process.

* - | processes
    | .[n].processType
  - integer
  - Number representing the type of MongoDB process.

* - serverType
  - object
  - Server Type of the physical host.

    To learn more, see admin-console-general-mongodb-usage.

* - serverType.name
  - string
  - Ops Manager returns one of the following values:

    - `DEV_SERVER`
    - `TEST_SERVER`
    - `PRODUCTION_SERVER`
    - `RAM_POOL`

* - serverType.label
  - string
  - Ops Manager returns one of the following values:

    - `Dev Server`
    - `Test Server`
    - `Production Server`
    - `Ram Pool`

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/usage/groups/{groupId}/hosts?startDate=2020-07-23&endDate=2020-07-28&pageNum=1&itemsPerPage=100&pretty=true"
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
  "links": [{
    "rel": "self",
    "href": "http://usage.example.com/api/public/v1.0/usage/assignments?startDate=2020-07-23&endDate=2020-07-28&pageNum=1&itemsPerPage=100"
  }],
  "totalCount": 3,
  "results": [{
    "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-0",
    "processes": [{
      "cluster": "sdivabux",
      "groupName": "{projectName}",
      "orgName": "{orgName}",
      "groupId": "{groupId}",
      "hasConflictingServerType": true,
      "name": "replicaPrimary-0-proc0-run51839",
      "processType": 7
    },
    {
      "cluster": "sdivabux",
      "groupName": "{projectName}",
      "orgName": "{orgName}",
      "groupId": "{groupId}",
      "hasConflictingServerType": true,
      "name": "replicaPrimary-0-proc1-run51839",
      "processType": 7
    }
  ],
    "serverType": {
      "name": "PRODUCTION_SERVER",
      "label": "Production Server"
    },
    "isChargeable": true,
    "memSizeMB": 178
  },
  {
    "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-1",
    "processes": [{
      "cluster": "sdivabux",
      "groupName": "{projectName}",
      "orgName": "{orgName}",
      "groupId": "{groupId}",
      "hasConflictingServerType": true,
      "name": "replicaSecondary-0-proc0-run51839",
      "processType": 8
    },
    {
      "cluster": "sdivabux",
      "groupName": "{projectName}",
      "orgName": "{orgName}",
      "groupId": "{groupId}",
      "hasConflictingServerType": true,
      "name": "replicaSecondary-0-proc1-run51839",
      "processType": 8
    }
  ],
    "serverType": {
      "name": "PRODUCTION_SERVER",
      "label": "Production Server"
    },
    "isChargeable": true,
    "memSizeMB": 178
  },
  {
    "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-2",
    "processes": [{
      "cluster": "sdivabux",
      "groupName": "{projectName}",
      "orgName": "{orgName}",
      "groupId": "{groupId}",
      "hasConflictingServerType": true,
      "name": "replicaSecondary-0-proc1-run51839",
      "processType": 8
    },
    {
      "cluster": "sdivabux",
      "groupName": "{projectName}",
      "orgName": "{orgName}",
      "groupId": "{groupId}",
      "hasConflictingServerType": true,
      "name": "replicaSecondary-0-proc0-run51839",
      "processType": 8
    }
  ],
    "serverType": {
      "name": "RAM_POOL",
      "label": "RAM Pool"
    },
    "isChargeable": true,
    "memSizeMB": 178
  }
]
}
```
