<!-- Converted from reference/api/api-keys/global/create-one-global-api-key.txt (reStructuredText). Includes are inlined. -->

# Create One Global API Key

Create one Global API (Application Programming Interface) Key for Ops Manager.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /admin/apiKeys
```

## Required Roles

Requires that the API (Application Programming Interface) Key calling this endpoint have the
`Global Owner` role.

Requires that the API (Application Programming Interface) Key calling this endpoint have the
`Global Read Only` role.

## Request Parameters

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

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

You must provide all request body parameters.

* - Name
  - Type
  - Necessity
  - Description

* - `desc`
  - string
  - Required
  - Description of the Global API (Application Programming Interface) Key. Must be between 1 and 250
    characters in length.

* - `roles`
  - string array
  - Required
  - List of roles that the Global API (Application Programming Interface) Key needs to have. If the
    `roles` array is provided:

    - Provide at least one role
    - Make sure all roles are valid.

    Global roles accepted by default include:

    | Role Value in API | Role |
    |---|---|
    | `GLOBAL_AUTOMATION_ADMIN` | `Global Automation Admin` |
    | `GLOBAL_BACKUP_ADMIN` | `Global Backup Admin` |
    | `GLOBAL_MONITORING_ADMIN` | `Global Monitoring Admin` |
    | `GLOBAL_OWNER` | `Global Owner` |
    | `GLOBAL_READ_ONLY` | `Global Read Only` |
    | `GLOBAL_USER_ADMIN` | `Global User Admin` |

## Response

* - Name
  - Type
  - Description

* - `desc`
  - string
  - Description of this Global API (Application Programming Interface) Key.

* - `id`
  - string
  - Unique identifier for this Global API (Application Programming Interface) Key.

* - `links`
  - string
  - An array of documents, representing a link
    to one or more sub-resources and/or related resources such as
    list pagination. See api-linking for
    more information.

* - `privateKey`
  - string
  - Unredacted Private key for this Global API (Application Programming Interface) Key.

* - `publicKey`
  - string
  - Public key for this Global API (Application Programming Interface) Key.

* - `roles`
  - object array
  - Roles that this Global API (Application Programming Interface) Key has. This array returns
    all the Global roles the user has in Ops Manager.

* - `roles.roleName`
  - string
  - Name of the role. This resource returns all the roles the user
    has in Ops Manager. Possible values are:

    | Role Value in API | Role |
    |---|---|
    | `GLOBAL_AUTOMATION_ADMIN` | `Global Automation Admin` |
    | `GLOBAL_BACKUP_ADMIN` | `Global Backup Admin` |
    | `GLOBAL_MONITORING_ADMIN` | `Global Monitoring Admin` |
    | `GLOBAL_OWNER` | `Global Owner` |
    | `GLOBAL_READ_ONLY` | `Global Read Only` |
    | `GLOBAL_USER_ADMIN` | `Global User Admin` |

## Example Request

**Note:**

The user who makes the request can be formatted either as
`{USERNAME}:{APIKEY}` or `{PUBLIC-KEY}:{PRIVATE-KEY}`.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --include \
  --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/admin/apiKeys?pretty=true" \
  --data '{
    "desc" : "New API key for Global Testing",
    "roles" : [ "GLOBAL_READ_ONLY", "GLOBAL_USER_ADMIN" ]
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
  "desc" : "New API key for Global Testing",
  "id" : "5d669ce780eef52a42cf0e1e",
  "links" : [ {
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/null/apiKeys/5d669ce780eef52a42cf0e1e",
    "rel" : "self"
  } ],
  "privateKey" : "8d080e57-5fd6-495c-9388-fe348ed1796f",
  "publicKey" : "cfswjfck",
  "roles" : [ {
    "roleName" : "GLOBAL_READ_ONLY"
  }, {
    "roleName" : "GLOBAL_USER_ADMIN"
  } ]
}
```
