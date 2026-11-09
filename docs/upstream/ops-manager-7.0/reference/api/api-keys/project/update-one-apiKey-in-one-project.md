<!-- Converted from reference/api/api-keys/project/update-one-apiKey-in-one-project.txt (reStructuredText). Includes are inlined. -->

# Modify Roles of One Organization API Key to One Project

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /groups/{PROJECT-ID}/apiKeys/{API-KEY-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `PROJECT-ID` | string | Unique identifier for the Project whose API (Application Programming Interface) keys you want to update. Use the /groups endpoint to retrieve all organizations to which the authenticated user has access. |
| `API-KEY-ID` | string | Unique identifier for the API (Application Programming Interface) key you want to update. Request the /groups/{PROJECT-ID}/apiKeys endpoint to retrieve all API (Application Programming Interface) keys to which the authenticated user has access for the specified organization. |

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

The body parameter is required.

* - Name
  - Type
  - Necessity
  - Description

* - `roles`
  - string array
  - Required
  - List of roles that the API (Application Programming Interface) Key should be granted. A minimum
    of one role must be provided. Any roles provided must be
    valid for the assigned Project:

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

    Include all roles that you want this API Key to have. Any
    roles not in this array are removed.

## Response

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
  --header "Content-Type: application/json" \
  --include \
  --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/apiKeys/5d1d143c87d9d63e6d694746?pretty=true" \
  --data '{
      "roles": [ "GROUP_READ_ONLY", "GROUP_DATA_ACCESS_READ_WRITE" ]
    }'
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
  "desc" : "New API key for test purposes",
  "id" : "5d1d143c87d9d63e6d694746",
  "links" : [ {
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfe20b6d97029d82fa63/apiKeys/5d1d143c87d9d63e6d694746",
    "rel" : "self"
  } ],
  "privateKey" : "********-****-****-eac4256753ba",
  "publicKey" : "{PUBLIC-KEY}",
  "roles" : [ {
    "orgId" : "5980cfe20b6d97029d82fa63",
    "roleName" : "ORG_BILLING_ADMIN"
  }, {
    "groupId" : "{PROJECT-ID}",
    "roleName" : "GROUP_DATA_ACCESS_READ_WRITE"
  }, {
    "orgId" : "5980cfe20b6d97029d82fa63",
    "roleName" : "ORG_MEMBER"
  }, {
    "groupId" : "{PROJECT-ID}",
    "roleName" : "GROUP_READ_ONLY"
  } ]
}
```
