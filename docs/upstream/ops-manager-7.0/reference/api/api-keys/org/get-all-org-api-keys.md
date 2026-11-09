<!-- Converted from reference/api/api-keys/org/get-all-org-api-keys.txt (reStructuredText). Includes are inlined. -->

# Get All API Keys

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /orgs/{ORG-ID}/apiKeys
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | The unique identifier for the organization whose API keys you want to retrieve. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |

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

Each **result** is one API key.

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
 --include \
 --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys?pretty=true"
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
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfc70b6d97029d82e3f6/apiKeys?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "desc" : "Test Docs Service User",
    "id" : "5c47503320eef5699e1cce8d",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/5980cfc70b6d98829d82e3f6/apiKeys/5c47503ae0eef5699e1cce8d",
      "rel" : "self"
    } ],
    "privateKey" : "********-****-****-db2c132ca78d",
    "publicKey" : "ewmaqvdo",
    "roles" : [ {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_OWNER"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_READ_ONLY"
    }, {
      "orgId" : "5980cfc70b6d97029d82e3f6",
      "roleName" : "ORG_MEMBER"
    } ]
  } ],
  "totalCount" : 1
}
```
