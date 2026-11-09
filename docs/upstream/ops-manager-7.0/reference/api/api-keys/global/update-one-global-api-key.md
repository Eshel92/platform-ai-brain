<!-- Converted from reference/api/api-keys/global/update-one-global-api-key.txt (reStructuredText). Includes are inlined. -->

# Update One Global API Key

Update values of one Global API (Application Programming Interface) Key from Ops Manager using the unique
identifier for that Key.

To find a specific Global API (Application Programming Interface) Key,
get the list of Global API Keys,
then find the `{API-KEY-ID}` you need.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /admin/apiKeys/{API-KEY-ID}
```

## Required Roles

Requires that the API (Application Programming Interface) Key calling this endpoint have the
`Global Owner` role.

Requires that the API (Application Programming Interface) Key calling this endpoint have the
`Global Read Only` role.

## Request Parameters

### Request Path Parameters

All request path parameters are required.

| Name | Type | Description |
|---|---|---|
| `API-KEY-ID` | string | Unique identifier for the Global API (Application Programming Interface) key you want to update. |

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

You must provide one or both of the two body parameters.

* - Name
  - Type
  - Necessity
  - Description

* - `desc`
  - string
  - Conditional
  - Description of the key. This parameter is optional; however, the
    request must contain either a `desc` parameter or a `roles`
    parameter. If `desc` is provided, it must be between 1 and 250
    characters long.

* - `roles`
  - string array
  - Conditional
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
  - Redacted Private key for this Global API (Application Programming Interface) Key.

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
curl --user "{USERNAME}:{APIKEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/admin/apiKeys/{API-KEY-ID}?pretty=true" \
  --data '{
    "desc" : "Updated API key description for test purposes"
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
  "created": "2019-09-04T15:37:40Z",
  "desc": "Updated API key description for test purposes",
  "globalRoles": ["GLOBAL_READ_ONLY"],
  "groupRoles": [],
  "numGroups": 0,
  "orgRoles": [],
  "orgRolesString": "",
  "privateKey": "********-****-****-cfe60e9f1f72",
  "userId": "5d6fda44ff4ab7133648a852",
  "username": "dczverfw"
}
```
