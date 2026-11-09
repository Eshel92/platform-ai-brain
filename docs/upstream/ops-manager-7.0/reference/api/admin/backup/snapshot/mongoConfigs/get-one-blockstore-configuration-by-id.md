<!-- Converted from reference/api/admin/backup/snapshot/mongoConfigs/get-one-blockstore-configuration-by-id.txt (reStructuredText). Includes are inlined. -->

# Get One Blockstore Configuration by ID

Retrieves the configuration of one blockstore.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /snapshot/mongoConfigs/{BLOCKSTORE-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| BLOCKSTORE-ID | string | The unique name that labels this blockstore configuration. |

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

* - Name
  - Type
  - Description

* - assignmentEnabled
  - boolean
  - Flag indicating whether this `blockstore` can be assigned
    backup jobs.

* - encryptedCredentials
  - boolean
  - Flag indicating whether the username and password for this 
    blockstore were encrypted using the 
    credentialstool.

* - id
  - string
  - The unique name that labels this `blockstore`.

* - labels
  - array of strings
  - Array of tags to manage which 
    backup jobs Ops Manager can assign to which 
    `blockstores`. 

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - loadFactor
  - number
  - A positive, non-zero integer that expresses how much backup work
    this `snapshot store` should perform compared to another
    snapshot store. This option is needed only if more than one 
    snapshot store is in use.

    To learn more about Load Factor, see Edit One Existing Blockstore.

* - maxCapacityGB
  - number
  - .. include:: /includes/api/maxCapacityGB-description.rst

* - uri
  - string
  - A comma-separated list of hosts in the `<hostname:port>`
    format that can be used to access this `blockstore`.

* - ssl
  - boolean
  - Flag indicating whether this blockstore only accepts 
    connections encrypted using 
    TLS (Transport Layer Security).

* - usedSize
  - number
  - The amount of backup capacity in MB (megabytes) that
    the existing backups consume.

* - writeConcern
  - string
  - The write concern used for this `blockstore`.

    The accepted values for this option are:

    - `ACKNOWLEDGED`
    - `W2`
    - `JOURNALED`
    - `MAJORITY`

    To learn about write acknowledgement levels in MongoDB, see 
    Write Concern.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --header 'Accept: application/json' \ 
 --include \ 
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/mongoConfigs/{BLOCKSTORE-ID}?pretty=true' 
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
  "assignmentEnabled" : true,
  "encryptedCredentials" : false,
  "id" : "{BLOCKSTORE-CONFIG-ID}",
  "labels" : [ "l1", "l2" ],
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/mongoConfigs/{BLOCKSTORE-ID}",
    "rel" : "self"
  }],
  "loadFactor" : 2,
  "maxCapacityGB" : 8,
  "uri" : "mongodb://localhost:27017",
  "ssl" : true,
  "usedSize" : 222,
  "writeConcern" : "W2"
}
```
