<!-- Converted from reference/api/admin/backup/oplog/s3Configs/get-all-s3-oplog-configurations.txt (reStructuredText). Includes are inlined. -->

# Get All S3 Oplog Configurations

Retrieves the configurations of all s3 oplog stores.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /oplog/s3Configs
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

|  |  |  |  |
|---|---|---|---|
| assignableOnly | boolean | Flag indicating whether this S3 oplog store can be assigned new backup jobs. | `true` |

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

Each **result** is one s3 oplog store.

* - Name
  - Type
  - Description

* - acceptedTos
  - boolean
  - Flag that indicates whether or not you accepted the terms of
    service for using S3-compatible storage stores with Ops Manager. You
    must set this to `true` to create an S3-compatible storage store.

* - assignmentEnabled
  - boolean
  - Flag that indicates whether you can assign backup jobs to this
    data store.

* - awsAccessKey
  - string
  - AWS (Amazon Web Services) Access Key ID that can access the S3-compatible storage bucket specified in
    **s3BucketName**.

* - awsSecretKey
  - string
  - AWS (Amazon Web Services) Secret Access Key that can access the S3-compatible storage bucket
    specified in **s3BucketName**.

* - customCertificates
  - array
  - List of valid Certificate Authority certificates that apply to the
    associated S3-compatible storage bucket.

* - customCertificates[n].filename
  - string
  - Name that identifies the Certificate Authority PEM (Privacy-Enhanced Mail) file.

* - customCertificates[n].certString
  - string
  - Contents of the Certificate Authority PEM (Privacy-Enhanced Mail) file that comprise your
    Certificate Authority chain.

* - disableProxyS3
  - boolean
  - Flag that indicates whether the
    HTTP proxy should be
    used when connecting to S3-compatible storage.

* - encryptedCredentials
  - boolean
  - Flag that indicates whether the username and password for this
    S3-compatible storage oplog store were encrypted using the
    credentialstool.

* - id
  - string
  - Name that uniquely identifies this S3-compatible storage oplog store.

* - labels
  - array of strings
  - Array of tags to manage which
    backup jobs Ops Manager can assign to which
    S3-compatible storage oplog stores.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - pathStyleAccessEnabled
  - boolean
  - Flag that indicates the style of this endpoint.

    | Value | S3 Oplog Store Endpoint Style | Example |
    |---|---|---|
    | `true` | Path-style URL (Uniform Resource Locator) endpoint | `s3.amazonaws.com/<bucket>` |
    | `false` | Virtual-host-style URL (Uniform Resource Locator) endpoint | `<bucket>.s3.amazonaws.com` |

    To review the S3-compatible storage bucket URL (Uniform Resource Locator) conventions, see the
    `AWS S3 documentation`.

* - s3BucketEndpoint
  - string
  - URL (Uniform Resource Locator) that Ops Manager uses to access this S3-compatible storage bucket.

* - s3BucketName
  - string
  - Name of the S3-compatible storage bucket that hosts the S3-compatible storage oplog store.

* - s3RegionOverride
  - string
  - Region where your S3-compatible storage bucket resides. This field applies only
    if your S3-compatible storage store's **s3BucketEndpoint** doesn't
    support region scoping.

    Ops Manager returns this field only if you included it when you
    created or
    updated this S3-compatible storage
    oplog store.

* - sseEnabled
  - boolean
  - Flag that indicates whether this S3-compatible storage oplog store enables
    `server-side encryption`.

* - ssl
  - boolean
  - Flag that indicates whether this S3-compatible storage oplog store only accepts
    connections encrypted using TLS (Transport Layer Security).

* - uri
  - string
  - Connection String
    that connects to the metadata database for this S3-compatible storage oplog
    store. This database stores the locations of the blocks in the
    S3-compatible storage bucket.

* - writeConcern
  - string
  - Write concern used for this oplog store.

    Ops Manager returns one of the following values:

    - `ACKNOWLEDGED`
    - `W2`
    - `JOURNALED`
    - `MAJORITY`

    To learn about write acknowledgement levels in MongoDB, see
    Write Concern.

## Example Request

```sh
curl --user '{USERNAME}:{APIKEY}' --digest \ 
 --header 'Accept: application/json' \ 
 --include \ 
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/s3Configs?pretty=true' 
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
    "href" : "http://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/s3Configs?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
  "assignmentEnabled": true,
  "awsAccessKey": "access",
  "awsSecretKey": "secret",
  "encryptedCredentials": false,
  "id": "id",
  "labels": [
    "l1",
    "l2"
  ],
  "links": [
    {
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/s3Configs/{S3-OPLOG-ID}",
      "rel": "self"
    }
  ],
  "s3BucketEndpoint": "http://backup.example.com/oplog",
  "s3BucketName": "oplog",
  "uri": "mongodb://localhost:27017",
  "ssl": true,
  "writeConcern": "W2"
  } ],
  "totalCount" : 1
}
```
