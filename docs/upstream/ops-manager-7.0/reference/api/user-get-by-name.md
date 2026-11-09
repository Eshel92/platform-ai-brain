<!-- Converted from reference/api/user-get-by-name.txt (reStructuredText). Includes are inlined. -->

# Get a User by Name

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

You can always retrieve your own user account.
Otherwise, you must be a global user or you
must have the `Project User Admin` role in at least
one project that is common between you and the user you are
retrieving.

You cannot use this endpoint to return information on an
API Key. Request the
Get One API Key
endpoint to get this information.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /users/byName/{USER-NAME}
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| USER-NAME | string | *(Required.)* Username of the MongoDB user that you want to retrieve. |

### Request Query Parameters

The following query parameters are optional:

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

This endpoint doesn't use HTTP request body parameters.

## Response

The HTTP document contains each of the following elements:

* - Name
  - Type
  - Description

* - emailAddress
  - string
  - Email address of the Ops Manager user.

* - firstName
  - string
  - First name of the Ops Manager user.

* - id
  - string
  - Unique identifier of the Ops Manager user.

* - lastName
  - string
  - Last name of the Ops Manager user.

* - links
  - object array
  - Links to related sub-resources. All `links` arrays in
    responses include at least one link called self. The
    relationship between URLs are explained in the 
    Web Linking Specification.

* - mobileNumber
  - string
  - Mobile number of the Ops Manager user.

* - roles
  - object array
  - Role assignments.

* - roles.groupId
  - string
  - Unique identifier for the project in which the user has the specified role.

    For the "global" roles (those whose name starts
    with `GLOBAL_`) there is no **groupId** since these
    roles are not tied to a project.

* - roles.orgId
  - string
  - Unique identifier for the organization in which the user has
    the specified role.

* - roles.roleName
  - string
  - Name of the role. Values are:

    | Value | Description |
    |---|---|
    | `ORG_MEMBER` | `Organization Member` |
    | `ORG_READ_ONLY` | `Organization Read Only` |
    | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
    | `ORG_OWNER` | `Organization Owner` |
    | `GROUP_AUTOMATION_ADMIN` | `Project Automation Admin` |
    | `GROUP_BACKUP_ADMIN` | `Project Backup Admin` |
    | `GROUP_MONITORING_ADMIN` | `Project Monitoring Admin` |
    | `GROUP_OWNER` | `Project Owner` |
    | `GROUP_READ_ONLY` | `Project Read Only` |
    | `GROUP_USER_ADMIN` | `Project User Admin` |
    | `GROUP_DATA_ACCESS_ADMIN` | `Project Data Access Admin` |
    | `GROUP_DATA_ACCESS_READ_ONLY` | `Project Data Access Read Only` |
    | `GROUP_DATA_ACCESS_READ_WRITE` | `Project Data Access Read/Write` |
    | `GLOBAL_AUTOMATION_ADMIN` | `Global Automation Admin` |
    | `GLOBAL_BACKUP_ADMIN` | `Global Backup Admin` |
    | `GLOBAL_MONITORING_ADMIN` | `Global Monitoring Admin` |
    | `GLOBAL_OWNER` | `Global Owner` |
    | `GLOBAL_READ_ONLY` | `Global Read Only` |
    | `GLOBAL_USER_ADMIN` | `Global User Admin` |

* - username
  - string
  - Username of the Ops Manager user.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://<ops-manager-host>/api/public/v1.0/users/byName/jane"
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
  "emailAddress" : "jane@qa.example.com",
  "firstName" : "Jane",
  "id" : "533dc19ce4b00835ff81e2eb",
  "lastName" : "D'oh",
  "roles" : [ {
    "groupId" : "{PROJECT-ID}",
    "roleName" : "GROUP_USER_ADMIN"
  },{
    "orgId" : "55555bbe3bd5253aea2d9b16",
    "roleName" : "ORG_MEMBER"
  } ],
  "links" : [],
  "username": "jane"
}
```
