<!-- Converted from reference/api/api-keys/global/create-one-global-access-list.txt (reStructuredText). Includes are inlined. -->

# Create One Global Access List Entry

Create one Global Access List Entry for Ops Manager.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /admin/accessList
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

Specify a document that represents one access list entry you want to add.

When you submit a `POST` request containing a `cidrBlock` value which is not already present 
in the access list, Ops Manager adds those entries to the list of existing entries in the
access list. Ops Manager does not set the access list to only contain the
entries specified in the request.

| Name | Type | Necessity | Description |
|---|---|---|---|
| `description` | string | Required | Description of the Global Access List Entry. Must be between 1 and 250 characters in length. |
| `cidrBlock` | string | Required | Access list entry in IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6) CIDR (Classless Inter-Domain Routing) notation to be added. |

## Response

| Name | Type | Description |
|---|---|---|
| `cidrBlock` | string | Range of IP addresses in an access list in IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6) CIDR (Classless Inter-Domain Routing) notation. |
| `created` | string | Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when you added this CIDR (Classless Inter-Domain Routing) block to the Global Access List. |
| `description` | string | Explanation of the purpose of this Global Access List Entry. |
| `id` | string | Unique identifier for this Global Access List Entry. |
| `type` | string | Scope of the Global Access List Entry. |
| `updated` | string | Timestamp, in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when you last changed the CIDR (Classless Inter-Domain Routing) block of this Global Access List Entry. |

## Example Request

```sh
curl --user '{USER-ID}:{API-KEY}' --digest \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--include \
--request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/admin/accessList?pretty=true" \
--data '
  {
    "cidrBlock"  : "127.0.0.1/32",
    "description" : "Docs Example"
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
  "cidrBlock" : "127.0.0.1/32",
  "created" : "2019-09-04T17:45:33Z",
  "description" : "Docs Example",
  "expires" : null,
  "id" : "5d6ff83dff4ab7133648b584",
  "lastUsed" : null,
  "type" : "GLOBAL_ROLE",
  "updated" : "2019-09-04T17:45:33Z"
}
```
