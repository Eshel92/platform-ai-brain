<!-- Converted from reference/api/admin/backup/snapshot/s3Configs/get-one-s3-blockstore-configuration-by-id.txt (reStructuredText). Includes are inlined. -->

# Get One S3 Blockstore Configuration by ID

Retrieves the configuration of one s3 blockstore.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| S3-BLOCKSTORE-CONFIG-ID | string | The unique name that labels this S3 blockstore configuration. |

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

* - acceptedTos
  - boolean
  - Flag that indicates whether or not you accepted the terms of
    service for using S3-compatible storage with Ops Manager. You
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
    S3-compatible storage blockstore were encrypted using the
    credentialstool.

* - id
  - string
  - Name that uniquely identifies this S3-compatible storage blockstore.

* - labels
  - array of strings
  - Array of tags to manage which
    backup jobs Ops Manager can assign to which
    `S3 blockstores`.

* - links
  - object array
  - .. include:: /includes/api/links-explanation.rst

* - loadFactor
  - integer
  - Positive, non-zero integer that expresses how much backup work
    this `snapshot store` performs compared to another
    snapshot store. This option is needed only if more than one
    snapshot store is in use.

    To learn more about Load Factor, see Edit One Existing Blockstore.

* - pathStyleAccessEnabled
  - boolean
  - Flag that indicates the style of this endpoint.

    | Value | S3 Blockstore Endpoint Style | Example |
    |---|---|---|
    | `true` | Path-style URL (Uniform Resource Locator) endpoint | `s3.amazonaws.com/<bucket>` |
    | `false` | Virtual-host-style URL (Uniform Resource Locator) endpoint | `<bucket>.s3.amazonaws.com` |

    To review the S3-compatible storage bucket URL (Uniform Resource Locator) conventions, see the
    `AWS S3 documentation`.

* - s3AuthMethod
  - string
  - Method used to authorize access to the S3-compatible storage bucket specified in `s3BucketName`.

    Accepted values for this option are: `KEYS`, `IAM_ROLE`.

    |  |  |
    |---|---|
    | `KEYS` or None | Ops Manager uses `awsAccessKey` and `awsSecretKey` to authorize access to S3-compatible storage bucket specified in `s3BucketName`. |
    | `IAM_ROLE` | Ops Manager uses an AWS (Amazon Web Services) IAM (Identity and Access Management) role to authorize access to S3-compatible storage bucket specified in `s3BucketName`. `awsAccessKey` and `awsSecretKey` fields are ignored. To learn more, see the `AWS documentation` |

* - s3BucketEndpoint
  - string
  - URL (Uniform Resource Locator) that Ops Manager uses to access this S3-compatible storage bucket.

* - s3BucketName
  - string
  - Name of the S3-compatible storage bucket that hosts the S3-compatible storage blockstore.

* - s3MaxConnections
  - integer
  - Positive integer indicating the maximum number of connections
    to this S3-compatible storage blockstore.

* - s3RegionOverride
  - string
  - Region where your S3-compatible storage bucket resides. This field applies only
    if your S3-compatible storage store's **s3BucketEndpoint** doesn't
    support region scoping.

    Ops Manager returns this field only if you included it when you
    created or updated this S3-compatible storage blockstore.

* - sseEnabled
  - boolean
  - Flag that indicates whether this S3-compatible storage blockstore enables
    `server-side encryption`.

* - ssl
  - boolean
  - Flag that indicates whether this S3-compatible storage blockstore only accepts
    connections encrypted using TLS (Transport Layer Security).

* - uri
  - string
  - Connection String
    that connects to the metadata database for this S3-compatible storage blockstore.
    This database stores the locations of the blocks in the AWS (Amazon Web Services)
    S3-compatible storage bucket.

* - writeConcern
  - string
  - Write concern used for this blockstore.

    Ops Manager returns one of the following values:

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
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}?pretty=true' 
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
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}",
      "rel": "self"
    }
  ],
  "loadFactor": 50,
  "s3BucketEndpoint": "http://example.com/backupbucket",
  "s3BucketName": "buck1",
  "uri": "mongodb://localhost:27017",
  "ssl": true,
  "writeConcern": "W2"
}
```
