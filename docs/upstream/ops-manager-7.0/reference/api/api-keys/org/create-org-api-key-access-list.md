<!-- Converted from reference/api/api-keys/org/create-org-api-key-access-list.txt (reStructuredText). Includes are inlined. -->

# Create Access List Entries for One Organization API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Create one or more new access list entries for the specified
API Key.

## Resource

```http
POST /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | Unique identifier for the organization to which the target API (Application Programming Interface) Key belongs. Use the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |
| `API-KEY-ID` | string | Unique identifier for the Organization API (Application Programming Interface) Key for which you want to create a new access list entry. |

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

Specify an array of documents, where each document represents one
access list entry you want to add to the project. You must specify an
array even if you are only associating a single access list entry to the
project.

When you submit a `POST` request containing `ipAddress` or
`cidrBlock` values which are not already present in the access list,
Ops Manager adds those entries to the list of existing entries in the
access list. Ops Manager does not set the access list to only contain the
entries specified in the request.

**Note:**

Ops Manager supports up to 500 API (Application Programming Interface) Keys within a single
organization.

In the following table, `[i]` represents an array index.

| Name | Type | Description |
|---|---|---|
| `[i].ipAddress` | string | IP address to be added to the access list for the API key. This field is mutually exclusive with the `cidrBlock` field. |
| `[i].cidrBlock` | string | Access list entry in CIDR (Classless Inter-Domain Routing) notation to be added for the API key. This field is mutually exclusive with the `ipAddress` field. |

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

Each object within the `results` array is one access list entry.

| Name | Type | Description |
|---|---|---|
| `cidrBlock` | string | CIDR-notated range of IP addresses in the access list. |
| `count` | number | Total number of requests that have originated from this IP address. |
| `created` | date | Date this IP address was added to the access list. |
| `ipAddress` | string | IP address in the access list. |
| `lastUsed` | date | Date of the most recent request that originated from this IP address. This field only appears if at least one request has originated from this IP address, and is only updated when a resource is retrieved from the access list. |
| `lastUsedAddress` | string | IP address from which the last call to the API was issued. This field only appears if at least one request has originated from this IP address. |
| `links` | array | An array of documents, representing a link to one or more sub-resources and/or related resources such as list pagination. See api-linking for more information. |

## Example Request

```sh
curl --user '{USER-ID}:{API-KEY}' --digest \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--include \
--request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList?pretty=true" \
--data '
  [{
    "ipAddress" : "77.54.32.11"
  }]'
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
    "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "cidrBlock" : "206.252.195.126/32",
    "count" : 47,
    "created" : "2019-01-24T16:26:37Z",
    "ipAddress" : "206.252.195.126",
    "lastUsed" : "2019-01-25T16:32:47Z",
    "lastUsedAddress" : "206.252.195.126",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/206.252.195.126",
      "rel" : "self"
    } ]
  }, {
    "cidrBlock" : "76.54.32.11/32",
    "count" : 0,
    "created" : "2019-01-24T21:09:05Z",
    "ipAddress" : null,
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/76.54.32.11",
      "rel" : "self"
    } ]
  } ],
  "totalCount" : 2
}
```
