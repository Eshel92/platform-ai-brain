<!-- Converted from reference/api/disk-get-one.txt (reStructuredText). Includes are inlined. -->

# Get a Disk Partition

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Retrieves a disk partition.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | *(Required.)* Unique identifier of the project where the disk partition resides. |
| HOST-ID | string | *(Required.)* Unique identifier of the host where the disk partition resides. |
| PARTITION-NAME | string | *(Required.)* The name of the disk partition that you want to retrieve. |

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
| `partitionName` | string | The name of the disk partition. |
| `links` | array | Links to related subresources. All `links` arrays in responses contain at least one link called `self`. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://<ops-manager-host>/api/public/v1.0/groups/533c5895b910306f21033a/hosts/814e70da8167883b9939608a12a/disks/xvdf"
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
  "links" : [],
  "partitionName" : "xvdf"
}
```
