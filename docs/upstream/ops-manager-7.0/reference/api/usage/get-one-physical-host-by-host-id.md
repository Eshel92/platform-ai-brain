<!-- Converted from reference/api/usage/get-one-physical-host-by-host-id.txt (reStructuredText). Includes are inlined. -->

# Retrieve One Physical Host

## Required Roles

This resource requires the
API Key to have
the `Global Owner` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /usage/groups/{physicalHostId}
```

### Request Path Parameters

Ops Manager requires all request path parameters:

| Path Parameter | Type | Description |
|---|---|---|
| physicalHostId | string | Unique identifier of the physical host to be retrieved. |

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
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/usage/groups/{physicalHostId}?pretty=true"
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
  "hosts": [
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-2"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-3"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-4"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-5"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-6"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-7"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-8"
    },
    {
      "groupId": "{PROJECT-ID}",
      "hostname": "virtual.host.lqhfcxlgzqtimcxf.internal.mongodb-9"
    }
  ],
  "id": "{PHYSICAL-HOST-ID}",
  "name": "physicalDevHostA",
  "serverType": "DEV_SERVER"
}
```
