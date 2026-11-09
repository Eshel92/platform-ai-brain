<!-- Converted from reference/api/api-keys/org/get-all-org-api-key-access-list.txt (reStructuredText). Includes are inlined. -->

# Get All Access List Entries for One Organization API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Retrieve information on all access list entries for the specified
API Key.

## Resource

```http
GET /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | Unique identifier for the organization to which the target API (Application Programming Interface) Key belongs. Request the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |
| `API-KEY-ID` | string | Unique identifier for the API (Application Programming Interface) Key for which you want to retrieve access list entries. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API (Application Programming Interface) keys for the specified organization to which the authenticated user has access. |

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

Each **result** is one access list entry.

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
curl --user "{USERNAME}:{APIKEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request GET "https://cloud.mongodb.com/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList?pretty=true"
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
  "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/599c510c80eef518f3b63fe1/apiKeys/5c49e72980eef544a218f8f8/accessList/?pretty=true&pageNum=1&itemsPerPage=100",
  "rel" : "self"
  } ],
  "results" : [ {
    "cidrBlock" : "147.58.184.16/32",
    "count" : 0,
    "created" : "2019-01-24T16:34:57Z",
    "ipAddress" : "147.58.184.16",
    "lastUsed" : "2019-01-24T20:18:25Z",
    "lastUsedAddress": "147.58.184.16",
    "links" : [ {
      "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/147.58.184.16",
      "rel" : "self"
    } ]
  }, {
    "cidrBlock" : "84.255.48.125/32",
    "count" : 0,
    "created" : "2019-01-24T16:26:37Z",
    "ipAddress" : null,
    "lastUsed" : "2019-01-24T20:18:25Z",
    "lastUsedAddress": "84.255.48.125",
    "links" : [ {
      "href" : "https://cloud.mongodb.com/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/206.252.195.126",
      "rel" : "self"
    } ]
  } ],
  "totalCount" : 2
}
```
