<!-- Converted from reference/api/access-list-get-for-ip-address.txt (reStructuredText). Includes are inlined. -->

# Get Access List for an IP Address

Retrieves an access list entity if the value of `IP-ADDRESS` equals the
value of the entity's `ipAddress` field. This does not retrieve an
object where the value of `IP-ADDRESS` is contained within the values
allowed by the `cidrBlock` field.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| USER-ID | string | *(Required.)* Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project. |
| `ACCESS-LIST-ENTRY` | string | The IP or CIDR (Classless Inter-Domain Routing) address. If the entry includes a subnet mask, such as `192.0.2.0/24`, use the URL-encoded value `%2F` for the forward slash `/`. |

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

This endpoint doesn't use HTTP request body parameters.

## Response

| Name | Type | Description |
|---|---|---|
| `cidrBlock` | string | A CIDR-notated range of IP addresses. |
| `created` | date | The date this IP address was added to the access list. |
| `ipAddress` | string | An IP address in the access list. |
| `lastUsed` | date | The date of the most recent request that originated from this IP address. Note that this field is *only* updated when a resource that is protected by the access list is accessed. |
| `lastUsedAddress` | string | The address from which the last call to the API was issued. |
| `count` | number | The total number of requests that originated from this IP address. Note that this field is *only* updated when a resource that is protected by the access list is accessed. |
| `links` | array | Links to related sub-resources. All links arrays in responses contain at least one link called `self`. The relations between URLs are explained in the [Web Linking Specification](https://tools.ietf.org/html/rfc5988). |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/users/{USER-ID}/accessList/192.0.2.0%2F24"
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
            "href": "https://<ops-manager-host>/api/public/v1.0/users/{USER-ID}/accessList/?pageNum=1&itemsPerPage=100",
            "rel": "self"
        }
    ],
    "results": [
        {
            "cidrBlock": "192.0.2.0/24",
            "count": 0,
            "created": "2019-11-01T15:18:12Z",
            "links": [
                {
                    "href": "https://<ops-manager-host>/api/public/v1.0/users/{USER-ID}/accessList/192.0.2.0%2F24",
                    "rel": "self"
                }
            ]
        },
    ],
    "totalCount": 1
}
```
