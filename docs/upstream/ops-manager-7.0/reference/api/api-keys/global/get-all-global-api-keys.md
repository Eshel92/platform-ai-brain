<!-- Converted from reference/api/api-keys/global/get-all-global-api-keys.txt (reStructuredText). Includes are inlined. -->

# Get All Global API Keys

Return all Global API (Application Programming Interface) Keys for Ops Manager.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /admin/apiKeys
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

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

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
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/admin/apiKeys?pretty=true"
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
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/admin/apiKeys?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "desc" : "Test Global API Key 1",
    "id" : "5d669ce780eef52a42cf0e1e",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/null/apiKeys/5d669ce780eef52a42cf0e1e",
      "rel" : "self"
    } ],
    "privateKey" : "********-****-****-54d9792d337d",
    "publicKey" : "zrefxaep",
    "roles" : [ {
      "roleName" : "GLOBAL_READ_ONLY"
    }, {
      "roleName" : "GLOBAL_BILLING_ADMIN"
    } ]
  }, {
    "desc" : "Test Global API Key 2",
    "id" : "5d6fec4180eef54728814b14",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/null/apiKeys/5d6fec4180eef54728814b14",
      "rel" : "self"
    } ],
    "privateKey" : "********-****-****-fe646723a586",
    "publicKey" : "qlgofmne",
    "roles" : [ {
      "roleName" : "GLOBAL_READ_ONLY"
    } ]
  }, {
    "desc" : "Test Global API Key 3",
    "id" : "5d6fecfc80eef547288207f3",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/null/apiKeys/5d6fecfc80eef547288207f3",
      "rel" : "self"
    } ],
    "privateKey" : "********-****-****-fe348ed1796f",
    "publicKey" : "cfswjfck",
    "roles" : [ {
      "roleName" : "GLOBAL_READ_ONLY"
    }, {
      "roleName" : "GLOBAL_BILLING_ADMIN"
    }, {
      "roleName" : "GLOBAL_USER_ADMIN"
    } ]
  } ],
  "totalCount" : 3
}
```
