<!-- Converted from reference/api/kmip-keys/rotate-master-key.txt (reStructuredText). Includes are inlined. -->

# Rotate the KMIP Master Key ID

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

**Important:**

This endpoint works with backups of MongoDB databases running FCV
4.0 or earlier. Backups of MongoDB databases running FCV
4.2 or later use the
deployment's encryption setting.

Use the `PUT` HTTP (Hypertext Transfer Protocol) method with the following endpoint to rotate the
KMIP (Key Management Interoperability) master key.  Issue one `PUT` request for each shard and
another `PUT` request for the config server replica set.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
PUT /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey
```

## Request Parameters

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| `{GROUP-ID}` | string | Required | Unique identifier of the project to which the encryption key belongs. |
| `{CLUSTER-ID}` | string | Required | Unique identifier of the cluster to which the encryption keys belongs. |

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
| `groupId` | string | Unique identifier of the project to which the encryption key belongs. |
| `clusterId` | string | Unique identifier of the cluster to which the encryption keys belongs. |
| `encryptionKeyUUID` | string | Unique identifier of the KMIP (Key Management Interoperability) master key. This key encrypts and restores the head databases for an encrypted backup. FCV `4.2` and later use backup cursors instead of `head databases`. For more information, see backup-daemon. For more information on backup encryption for FCV 4.2 or later, see encrypt-snapshots. |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --include \
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/encryptionKey"
```

### Example Response

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
HTTP/1.1 201 Created
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

This endpoint returns an empty JSON (Javascript Object Notation) object.
