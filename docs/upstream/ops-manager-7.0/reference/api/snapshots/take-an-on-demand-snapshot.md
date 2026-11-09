<!-- Converted from reference/api/snapshots/take-an-on-demand-snapshot.txt (reStructuredText). Includes are inlined. -->

# Create an On-Demand Snapshot

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /groups/{groupId}/clusters/{clusterId}/snapshots/onDemandSnapshot
```

## Required Permissions

You must have the `Global Backup Admin` to 
take an on-demand snapshot.

## Request Parameters

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| GROUP-ID | string | Unique identifier of your project from your project settings. |
| CLUSTER-ID | string | Unique identifier of the cluster that the snapshot represents. |

### Request Query Parameters

| Name | Type | Necessity | Description | Example |
|---|---|---|---|---|
| retentionDays | number | Required | Integer that indicates the number of days the on-demand snapshot will be retained. Must be greater than 0. | `15` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --include \
 --request POST "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{groupId}/clusters/{clusterId}/snapshots/onDemandSnapshot"
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
   "clusterName": "myCluster",
   "description": "On demand snapshot request complete .",
   "timestamp": {
       "increment": 1,
       "time": 1719518976,
       "date": "2024-06-27T20:09:36Z"
   }
}
```
