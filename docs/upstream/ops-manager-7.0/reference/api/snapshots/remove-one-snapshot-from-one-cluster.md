<!-- Converted from reference/api/snapshots/remove-one-snapshot-from-one-cluster.txt (reStructuredText). Includes are inlined. -->

# Remove One Snapshot from a Cluster

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
DELETE /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}
```

## Required Permissions

You must have the `Global Backup Admin` or 
`Global Owner` role to delete a snapshot that is within 
Point-in-Time restore window.

## Request Parameters

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the snapshot. |
| CLUSTER-ID | string | Unique identifier of the cluster that the snapshot represents. |
| SNAPSHOT-ID | string | Unique identifier of the snapshot. |

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
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --include \
 --request DELETE "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots/{SNAPSHOT-ID}"
```

## Example Response

This endpoint doesn't return a response body.
