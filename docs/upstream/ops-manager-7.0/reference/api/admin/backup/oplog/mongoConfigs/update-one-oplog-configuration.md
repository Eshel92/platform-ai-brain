<!-- Converted from reference/api/admin/backup/oplog/mongoConfigs/update-one-oplog-configuration.txt (reStructuredText). Includes are inlined. -->

# Update One Oplog Configuration

Updates the configuration of one oplog store.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
PUT /oplog/mongoConfigs/{OPLOG-CONFIG-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| OPLOG-CONFIG-ID | string | The unique identifier that represents this Oplog configuration. |

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

* - Name
  - Type
  - Description

* - assignmentEnabled
  - boolean
  - *Optional.* Flag indicating whether this `oplog store` can 
    be assigned backup jobs.

* - encryptedCredentials
  - boolean
  - *Optional.* Flag indicating whether the username and password for 
    this oplog store were encrypted using the
    credentialstool.

* - labels
  - array of strings
  - *Optional.* Array of tags to manage which 
    backup jobs Ops Manager can assign to which 
    `oplog stores`. 

    Setting these tags limits which backup jobs this oplog
    store can process. If omitted, this oplog store can only
    process backup jobs for projects that do not use labels to filter
    their jobs.

* - maxCapacityGB
  - number
  - .. include:: /includes/api/maxCapacityGB-description.rst

* - uri
  - string
  - A comma-separated list of hosts in the `<hostname:port>`
    format that can be used to access this `oplog store`.

* - ssl
  - boolean
  - *Optional.* Flag indicating whether this oplog store only accepts 
    connections encrypted using 
    TLS (Transport Layer Security).

* - writeConcern
  - string
  - *Optional.* The write concern used for this `oplog store`.

    The accepted values for this option are:

    - `ACKNOWLEDGED`
    - `W2`
    - `JOURNALED`
    - `MAJORITY`

    To learn about write acknowledgement levels in MongoDB, see 
    Write Concern.

## Response

* - Name
  - Type
  - Description

* - assignmentEnabled
  - boolean
  - Flag indicating whether this `oplog store` can be assigned
    backup jobs.

* - encryptedCredentials
  - boolean
  - Flag indicating whether the username and password for this 
    oplog store were encrypted using the 
    credentialstool.

* - id
  - string
  - The unique name that labels this `oplog store`.

* - labels
  - array of strings
  - Array of tags to manage which 
    backup jobs Ops Manager can assign to which 
    `oplog stores`. 

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - maxCapacityGB
  - number
  - .. include:: /includes/api/maxCapacityGB-description.rst

* - uri
  - string
  - A comma-separated list of hosts in the `<hostname:port>`
    format that can be used to access this `oplog store`.

* - ssl
  - boolean
  - Flag indicating whether this oplog store only accepts 
    connections encrypted using 
    TLS (Transport Layer Security).

* - usedSize
  - number
  - The amount of backup capacity in MB (megabytes) that
    the existing backups consume.

* - writeConcern
  - string
  - The write concern used for this `oplog store`.

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
 --header 'Content-Type: application/json' \ 
 --include \ 
 --request PUT 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/mongoConfigs/{OPLOG-CONFIG-ID}?pretty=true' \ 
 --data '{
  "assignmentEnabled" : true,
  "encryptedCredentials" : false,
  "labels" : [ "l1", "l2" ],
  "maxCapacityGB" : 8,
  "uri" : "mongodb://localhost:27017",
  "ssl" : true,
  "writeConcern" : "W2"
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
  "assignmentEnabled" : true,
  "encryptedCredentials" : false,
  "id" : "{CONFIG-ID}",
  "labels" : [ "l1", "l2" ],
  "links" : [ {
    "href" : "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/mongoConfigs/{OPLOG-CONFIG-ID}",
    "rel" : "self"
  }],
  "maxCapacityGB" : 8,
  "uri" : "mongodb://localhost:27017",
  "ssl" : true,
  "usedSize" : 222,
  "writeConcern" : "W2"
}
```
