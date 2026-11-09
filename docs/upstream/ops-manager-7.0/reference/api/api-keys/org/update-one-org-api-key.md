<!-- Converted from reference/api/api-keys/org/update-one-org-api-key.txt (reStructuredText). Includes are inlined. -->

# Update an API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PATCH /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | Unique identifier for the organization whose API (Application Programming Interface) keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |
| `API-KEY-ID` | string | Unique identifier for the API (Application Programming Interface) key you want to update. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API (Application Programming Interface) keys to which the authenticated user has access for the specified organization. |

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

* - Name
  - Type
  - Required/Optional
  - Description

* - `desc`
  - string
  - Optional
  - Description of the key. This parameter is optional; however, the
    request must contain either a `desc` parameter or a `roles`
    parameter. If `desc` is provided, it must be between 1 and 250
    characters long.

* - `roles`
  - string array
  - Optional
  - List of roles that the API (Application Programming Interface) key should have. This parameter is
    optional; however, the request must contain either a `desc`
    parameter or a `roles` parameter. If `roles` is provided,
    there must be at least one role listed, and all roles must be
    valid for an Organization.

    Organization roles include:

    | Role Value in API | Role |
    |---|---|
    | `ORG_OWNER` | `Organization Owner` |
    | `ORG_MEMBER` | `Organization Member` |
    | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
    | `ORG_READ_ONLY` | `Organization Read Only` |

## Response

* - Name
  - Type
  - Description

* - `id`
  - string
  - Unique identifier for the API key

* - `desc`
  - string
  - Description of the API key

* - `privateKey`
  - string
  - Redacted private key for the API key

* - `publicKey`
  - string
  - Public key for the API key

* - `roles`
  - object array
  - Roles that the API key has

* - `roles.{ENTITY-ID}`
  - string
  - The `{ENTITY-ID}` represents the Organization or Project to
    which this role applies. Possible values are: `orgId` or
    `groupId`.

* - `roles.roleName`
  - string
  - The name of the role. The `users` resource returns all the roles the
    user has in either MongoDB Atlas or Ops Manager. Possible values are:

    - Organization Roles

      | Role Value in API | Role |
      |---|---|
      | `ORG_OWNER` | `Organization Owner` |
      | `ORG_MEMBER` | `Organization Member` |
      | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
      | `ORG_READ_ONLY` | `Organization Read Only` |

    - Project Roles

      Groups and projects are synonymous terms.

      - `GROUP_OWNER`
      - `GROUP_READ_ONLY`
      - `GROUP_DATA_ACCESS_ADMIN`
      - `GROUP_DATA_ACCESS_READ_WRITE`
      - `GROUP_DATA_ACCESS_READ_ONLY`
      - `GROUP_AUTOMATION_ADMIN`
      - `GROUP_BACKUP_ADMIN`
      - `GROUP_MONITORING_ADMIN`
      - `GROUP_OWNER`
      - `GROUP_USER_ADMIN`

## Example Request

**Note:**

The user who makes the request can be formatted either as
`{USERNAME}:{APIKEY}` or `{PUBLIC-KEY}:{PRIVATE-KEY}`.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}?pretty=true" \
  --data '{
    "desc" : "Updated :abbr:`API (Application Programming Interface)` key description for test purposes",
    "roles": ["ORG_MEMBER", "ORG_READ_ONLY"]
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
  "desc" : "Updated :abbr:`API (Application Programming Interface)` key description for test purposes",
  "id" : "5c47ba5127d9d61b9fd8a27b",
  "links" : [ {
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfc70b6d12029d82e3f6/apiKeys/5c47ba5127d9d61b9fd8a27b",
    "rel" : "self"
  } ],
  "privateKey" : "********-****-****-db2c132ca78d",
  "publicKey" : "kzurbulc",
  "roles" : [ {
    "orgId" : "5980cfc70b6d97029d82e3f6",
    "roleName" : "ORG_MEMBER"
  }, {
    "orgId" : "5980cfc70b6d97029d82e3f6",
    "roleName" : "ORG_READ_ONLY"
  } ]
}
```
