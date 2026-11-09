<!-- Converted from reference/api/api-keys/project/get-all-apiKeys-in-one-project.txt (reStructuredText). Includes are inlined. -->

# Get All Organization API Keys Assigned to One Project

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/apiKeys
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `PROJECT-ID` | string | Unique identifier for the Project from which you want to retrieve its assigned Organization API (Application Programming Interface) keys. Use the /groups endpoint to retrieve all Projects to which the authenticated user has access. |

### Request Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Description
  - Default

* - pageNum
  - integer
  - Page number (1-index based).
  - `1`

* - itemsPerPage
  - integer
  - Number of items to return per page, up to a maximum of 500.
  - `100`

* - pretty
  - boolean
  - Indicates whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Indicates whether or not to wrap the response in an envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set `"envelope" : true` in the
    query.

    For endpoints that return one result, response body
    includes:

    | status | HTTP (Hypertext Transfer Protocol) response code |
    |---|---|
    | envelope | Expected response body |

    For endpoints that return a list of results, the `results`
    object is an envelope. Ops Manager adds the `status` field to the
    response body.
  - None

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

Each **result** is one Project API (Application Programming Interface) key.

* - Name
  - Type
  - Description

* - `desc`
  - string
  - Description of this Organization API (Application Programming Interface) key assigned to this
    Project.

* - `id`
  - string
  - Unique identifier for this Organization API (Application Programming Interface) key assigned to
    this Project.

* - `privateKey`
  - string
  - Redacted Private key for this Organization API (Application Programming Interface) key assigned to
    this Project.

    **This key displays unredacted when first created.**

* - `publicKey`
  - string
  - Public key for this Organization API (Application Programming Interface) key assigned to this Project.

* - `roles`
  - object array
  - Roles that this Organization API (Application Programming Interface) key assigned to this Project
    has. This array returns all the Organization and Project roles
    the user has in Ops Manager.

* - `roles.groupId`
  - string
  - Unique identifier of the Project to which this role belongs.

* - `roles.orgId`
  - string
  - Unique identifier of the Organization to which this role
    belongs.

* - `roles.roleName`
  - string
  - Name of the role. This resource returns all the roles the user
    has in Ops Manager. Possible values are:

    **Organization Roles**

    If this is an `roles.orgId` (Organization), values include:

    | Role Value in API | Role |
    |---|---|
    | `ORG_OWNER` | `Organization Owner` |
    | `ORG_MEMBER` | `Organization Member` |
    | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
    | `ORG_READ_ONLY` | `Organization Read Only` |

    **Project Roles**

    If this is an `roles.groupId` (Project), values include:

    | Role Value in API | Role |
    |---|---|
    | `GROUP_AUTOMATION_ADMIN` | `Project Automation Admin` |
    | `GROUP_BACKUP_ADMIN` | `Project Backup Admin` |
    | `GROUP_DATA_ACCESS_ADMIN` | `Project Data Access Admin` |
    | `GROUP_DATA_ACCESS_READ_ONLY` | `Project Data Access Read Only` |
    | `GROUP_DATA_ACCESS_READ_WRITE` | `Project Data Access Read/Write` |
    | `GROUP_MONITORING_ADMIN` | `Project Monitoring Admin` |
    | `GROUP_OWNER` | `Project Owner` |
    | `GROUP_READ_ONLY` | `Project Read Only` |
    | `GROUP_USER_ADMIN` | `Project User Admin` |

## Example Request

**Note:**

The user who makes the request can be formatted either as
`{USERNAME}:{APIKEY}` or `{PUBLIC-KEY}:{PRIVATE-KEY}`.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --include \
  --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/apiKeys?pretty=true"
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
  "links" : [ {
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/apiKeys?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "desc" : "Updated API Key description for DOCSP-6042",
    "id" : "5d1cf1f980eef570c9fc87e5",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfe20b6d97029d82fa63/apiKeys/5d1cf1f980eef570c9fc87e5",
      "rel" : "self"
    } ],
    "privateKey" : "********-****-****-9d4ae38e4ddd",
    "publicKey" : "{PUBLIC-KEY}",
    "roles" : [ {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_AUTOMATION_ADMIN"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_MONITORING_ADMIN"
    }, {
      "orgId" : "5980cfe20b6d97029d82fa63",
      "roleName" : "ORG_MEMBER"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_DATA_ACCESS_ADMIN"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_USER_ADMIN"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_READ_ONLY"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_OWNER"
    }, {
      "orgId" : "5980cfe20b6d97029d82fa63",
      "roleName" : "ORG_OWNER"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_DATA_ACCESS_READ_WRITE"
    }, {
      "orgId" : "5980cfe20b6d97029d82fa63",
      "roleName" : "ORG_GROUP_CREATOR"
    }, {
      "orgId" : "5980cfe20b6d97029d82fa63",
      "roleName" : "ORG_READ_ONLY"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_DATA_ACCESS_READ_ONLY"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_BACKUP_ADMIN"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_CLUSTER_MANAGER"
    } ]
  }, {
    "desc" : "New API key for test purposes",
    "id" : "5d1d12c087d9d63e6d682438",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfe20b6d97029d82fa63/apiKeys/5d1d12c087d9d63e6d682438",
      "rel" : "self"
    } ],
    "privateKey" : "********-****-****-cb34f12aafdb",
    "publicKey" : "oxhzytwb",
    "roles" : [ {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_READ_ONLY"
    }, {
      "orgId" : "5980cfe20b6d97029d82fa63",
      "roleName" : "ORG_MEMBER"
    } ]
  } ],
  "totalCount" : 2
}
```
