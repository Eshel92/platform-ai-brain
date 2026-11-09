<!-- Converted from reference/api/api-keys/org/get-one-org-api-key.txt (reStructuredText). Includes are inlined. -->

# Get One API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | The unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |
| `API-KEY-ID` | string | The unique identifier for the API key you want to retrieve. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API (Application Programming Interface) keys for the specified organization to which the authenticated user has access. |

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

### Response Elements

If you set the query element `envelope` to `true`, the response is wrapped
by the `content` object.

The HTTP response returns a JSON document that includes the following objects:

* - Name
  - Type
  - Description

* - `id`
  - string
  - Unique identifier for the API key

* - `links`
  - string
  - An array of documents, representing a link
    to one or more sub-resources and/or related resources such as
    list pagination. See api-linking for
    more information.

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

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}?pretty=true"
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
  "desc" : "Test Docs Service User",
  "id" : "5c47503880eef5662e1cce8d",
  "links" : [ {
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfc70b6d98229d82e3f6/apiKeys/5c47503880eef5662e1cce8d",
    "rel" : "self"
  } ],
  "privateKey" : "********-****-****-db2c132ca78d",
  "publicKey" : "ewmaqvdo",
  "roles" : [ {
    "orgId" : "5980cfc70b6d97029d82e3f6",
    "roleName" : "ORG_MEMBER"
  }, {
    "groupId" : "{PROJECT-ID}",
    "roleName" : "GROUP_READ_ONLY"
  }, {
    "groupId" : "{PROJECT-ID}",
    "roleName" : "GROUP_OWNER"
  } ]
}
```
