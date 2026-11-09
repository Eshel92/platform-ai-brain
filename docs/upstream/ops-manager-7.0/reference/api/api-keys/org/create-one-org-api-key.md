<!-- Converted from reference/api/api-keys/org/create-one-org-api-key.txt (reStructuredText). Includes are inlined. -->

# Create an API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /orgs/{ORG-ID}/apiKeys
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | Unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |

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

All body parameters are required.

* - Name
  - Type
  - Description

* - `desc`
  - string
  - Description of the API key. Must be between 1 and 250
    characters in length.

* - `roles`
  - string array
  - List of roles that the API key should have. There must
    be at least one role listed, and all roles must be valid for an
    Organization.

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
  - Private key for the API key. This key appears unredacted only
    at the time of creation.

* - `publicKey`
  - string
  - Public key for the API key

* - `roles`
  - object array
  - Roles that the API key has

* - `roles.orgId`
  - string
  - The `orgId` represents the Organization to
    which this role applies.

* - `roles.roleName`
  - string
  - The name of the role. The `users` resource returns all the
    roles the user has in either MongoDB Atlas or Ops Manager. Possible values
    are:

    | Role Value in API | Role |
    |---|---|
    | `ORG_OWNER` | `Organization Owner` |
    | `ORG_MEMBER` | `Organization Member` |
    | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
    | `ORG_READ_ONLY` | `Organization Read Only` |

## Example Request

**Note:**

The user who makes the request can be formatted either as
`{USERNAME}:{APIKEY}` or `{PUBLIC-KEY}:{PRIVATE-KEY}`.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request POST "https://<ops-manager-host>/api/public/v1.0/orgs/{ORG-ID}/apiKeys?pretty=true" \
  --data '{
    "desc" : "New API key for test purposes",
    "roles": ["ORG_MEMBER"]
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

**Note:**

The `privateKey` appears unredacted in the response body. This
example is redacted for security purposes.

```json
{
  "desc" : "New API key for test purposes",
  "id" : "{API-KEY-ID}",
  "links" : [ {
    "href" : "https://<ops-manager-host>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}",
    "rel" : "self"
  } ],
  "privateKey" : "********-****-****-db2c132ca78d",
  "publicKey" : "{PUBLIC-KEY}",
  "roles" : [ {
    "orgId" : "{ORG-ID}",
    "roleName" : "ORG_MEMBER"
  } ]
}
```
