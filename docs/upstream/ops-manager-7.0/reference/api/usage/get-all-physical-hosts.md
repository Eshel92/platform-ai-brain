<!-- Converted from reference/api/usage/get-all-physical-hosts.txt (reStructuredText). Includes are inlined. -->

# Retrieve All Physical Hosts

## Required Roles

This resource requires the
API Key to have
the `Global Owner` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /usage/groups
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

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

Each element in the **result** array is one physical host.

* - Response Element
  - Type
  - Description

* - hosts
  - array of objects
  - List of virtual hosts bound to the provided physical host.

* - | hosts
    | .[n].groupId
  - string
  - Unique identifier of the project into which Ops Manager places this
    virtual host.

* - | hosts
    | .[n].hostname
  - string
  - FQDN (fully qualified domain name) of the virtual host bound to the physical host.

* - id
  - string
  - Unique identifier of the physical host to which Ops Manager bound
    the virtual hosts.

* - name
  - string
  - Label you gave to the physical host.

* - serverType
  - string
  - Server Type of the physical host.

    Ops Manager returns one of the following values:

    - DEV_SERVER
    - TEST_SERVER
    - PRODUCTION_SERVER
    - RAM_POOL

    To learn more, see admin-console-general-mongodb-usage.

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/usage/groups?pretty=true"
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
  "links": [
    {
      "href": "http://<OpsManagerHost>:<Port>/api/public/v1.0/usage/groups?pageNum=1&itemsPerPage=100",
      "rel": "self"
    }
  ],
  "results": [
    {
      "hosts": [
        {
          "groupId": "{projectId1}",
          "hostname": "virtual.host.niivowqqlyjpkakk.internal.mongodb-7"
        },
        {
          "groupId": "{projectId1}",
          "hostname": "virtual.host.niivowqqlyjpkakk.internal.mongodb-8"
        }
      ],
      "id": "{physicalHostId1}",
      "name": "physicalHostA",
      "serverType": "DEV_SERVER"
    },
    {
      "hosts": [
        {
          "groupId": "{projectId2}",
          "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-0"
        },
        {
          "groupId": "{projectId2}",
          "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-1"
        }
      ],
      "id": "{physicalHostId2}",
      "name": "physicalHostB",
      "serverType": "DEV_SERVER"
    },
  ],
  "totalCount": 2
}
```
