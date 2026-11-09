<!-- Converted from reference/api/admin/backup/oplog/s3Configs/get-one-s3-oplog-configuration-by-id.txt (reStructuredText). Includes are inlined. -->

# Get One S3 Oplog Configuration by ID

Retrieves the configuration of one s3 oplog store.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
GET /oplog/s3Configs/{S3-OPLOG-CONFIG-ID}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| S3-OPLOG-CONFIG-ID | string | The unique identifier that represents this S3 Oplog configuration. |

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
 --request GET 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/s3Configs/{S3-OPLOG-CONFIG-ID}?pretty=true' 
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
  "customCertificates" : [{
    "filename" : "CA.pem",
    "certString" : "-----BEGIN CERTIFICATE-----\nMIIDljCCAn4CCQDJjCHAkAafFTANBgkqhkiG9w0BAQsFADCBjDELMAkGA1UEBhMC\nVVMxCzAJBgNVBAgMAk5ZMQwwCgYDVQQHDANOWUMxEDAOBgNVBAoMB01vbmdvREIx\nDDAKBgNVBAsMA1NXRTEZMBcGA1UEAwwQZXJpbm1jbnVsdHkudGVjaDEnMCUGCSqG\nSIb3DQEJARYYZXJpbi5tY251bHR5QG1vbmdvZGIuY29tMB4XDTIxMDYxMTE1MzY0\nMVoXDTIxMDcxMTE1MzY0MVowgYwxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJOWTEM\nMAoGA1UEBwwDTllDMRAwDgYDVQQKDAdNb25nb0RCMQwwCgYDVQQLDANTV0UxGTAX\nBgNVBAMMEGVyaW5tY251bHR5LnRlY2gxJzAlBgkqhkiG9w0BCQEWGGVyaW4ubWNu\ndWx0eUBtb25nb2RiLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB\nAOoAv1btxcEgDOdCgyz+/NtyFwa0h/3yGtj+WK7nMzcEntnxG5apHVRZ6eQ4ayZU\nhZNPbNWtcsbTEiRWyywMAd7/DbIa9GhsP1/P6Cv+TnO2krx8qVKQN93j8cme/b6g\n+yeEWMAM2rvfXq/fRTtJbH1Y6c4mYh4312mPrlEfgvAUQZh3DpJQNIVZ5MM2imp0\nfBgcggrNHUniLCT8ogUA4QII8CKIC4ONX4TNtXbsNtcCzKNqvOdcvWXLTYEJav34\nlaJs1YWJx2PSufgHo+JZUeANwwpztkYhr3nUGTD8fr7JF9CO7UlFBTFqs+PeaTJV\nEbnrF26NimsAmRgRPNLE170CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAe5hAkrhz\nClXg4HPq6U3ONEUVUqQ231gogeUIIQsfn4K89QIFnsm0DC1lE21qHNcD3iHECmDJ\n9R2tXdA0shbc+hM8OHbEW6U31dLrM369PUQmw0GOkFWlYHnX4ySt+zMAjlIrQe7C\nLErYSuLDpjuKvkdpvbcwgkarB9/FPCOhORpAZqduhwUOr28tZzT3/8L7w//+7Yhy\n5ihKgTcP/CmJ+MgLlZqBtQ7lkmKDWXIUlLSRDHEciVGSXgZBreUciNFeMHVvoluc\ndxdsxqMcXgyXwmv7Ck7tCjYRwzwlf3TrcKt8QFijWTbl1Z/3d0/zpjuvR21J0z/3\ns4tNMtQdG6/bHA==\n-----END CERTIFICATE-----"
  }],
  "encryptedCredentials": false,
  "id": "id",
  "labels": [
    "l1",
    "l2"
  ],
  "links": [
    {
      "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/oplog/s3Configs/{S3-OPLOG-CONFIG-ID}",
      "rel": "self"
    }
  ],
  "s3BucketEndpoint": "http://backup.example.com/oplog",
  "s3BucketName": "oplog",
  "uri": "mongodb://localhost:27017",
  "ssl": true,
  "writeConcern": "W2"
}
```
