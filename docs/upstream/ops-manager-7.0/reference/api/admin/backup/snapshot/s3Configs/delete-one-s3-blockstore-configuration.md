<!-- Converted from reference/api/admin/backup/snapshot/s3Configs/delete-one-s3-blockstore-configuration.txt (reStructuredText). Includes are inlined. -->

# Delete One S3-Compatible Blockstore Configuration

Deletes the configuration of one s3 blockstore.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Resource

```http
DELETE /snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}
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

This endpoint does not have response elements.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --include \ 
 --request DELETE 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup/snapshot/s3Configs/{S3-BLOCKSTORE-CONFIG-ID}' 
```

## Example Response

This endpoint doesn't return a response body.
