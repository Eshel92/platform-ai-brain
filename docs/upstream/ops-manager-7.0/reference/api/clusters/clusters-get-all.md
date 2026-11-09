<!-- Converted from reference/api/clusters/clusters-get-all.txt (reStructuredText). Includes are inlined. -->

# Get All Clusters in One Project

Retrieve details for all clusters in one project.

## Required Roles

You can successfully call this endpoint with any assigned role.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /groups/{PROJECT-ID}/clusters
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `PROJECT-ID` | string | Unique identifier for the project. |

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

### Response Parameters

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

Each **result** is one cluster.

* - Name
  - Type
  - Description

* - `clusterName`
  - string
  - Display name of the cluster. Note that `mongod` itself doesn't
    allow you to name a cluster; Ops Manager supplies this name and you can
    update it. For a replica set within a sharded cluster, the
    cluster name is the name of its parent cluster.

* - `groupId`
  - string
  - Unique identifier of the project to which the cluster belongs.

* - `id`
  - string
  - Unique identifier of the cluster.

* - `lastHeartbeat`
  - date
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when Ops Manager most recently processed a ping from
    this cluster. 

* - `replicaSetName`
  - string
  - Replica set name. Ops Manager returns this value when a cluster has a
    `typeName` of `REPLICA_SET` or `CONFIG_SERVER_REPLICA_SET`.

* - `shardName`
  - string
  - Shard name. Ops Manager returns this value when a cluster has a
    `typeName` of `SHARDED` or a `REPLICA_SET` that part of a
    sharded cluster. 

* - `typeName`
  - string
  - Cluster type. Ops Manager may return:

    | `typeName` | Description |
    |---|---|
    | `REPLICA_SET` | A replica set. |
    | `SHARDED` | A sharded cluster where each shard is a standalone instance. No shards are replica sets. |
    | `SHARDED_REPLICA_SET` | A sharded cluster that contains at least one shard that is a replica set. |
    | `CONFIG_SERVER_REPLICA_SET` | Config servers deployed as a replica set. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/clusters?pretty=true"
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
  "links": [
    {
      "href": "https://example.com:8080/api/public/v1.0/groups/5e84b94c003f2d6370004f4e/clusters?pageNum=1&itemsPerPage=100",
      "rel": "self"
    }
  ],
  "results": [
    {
      "clusterName": "myRS",
      "groupId": "5e84b94c003f2d6370004f4e",
      "id": "5e8ba20e87d9396ca9b96bd0",
      "lastHeartbeat": "2020-06-10T14:51:28Z",
      "links": [
        {
          "href": "https://example.com:8080/api/public/v1.0/groups/5e84b94c003f2d6370004f4e/clusters/5e8ba20e87d9396ca9b96bd0",
          "rel": "self"
        }
      ],
      "replicaSetName": "myRS",
      "typeName": "REPLICA_SET"
    },
    {
      "clusterName": "cm-clstr-repl",
      "groupId": "5e84b94c003f2d6370004f4e",
      "id": "5e84e393395ec72bfc888f6c",
      "lastHeartbeat": "2020-06-10T15:20:08Z",
      "links": [
        {
          "href": "https://example.com:8080/api/public/v1.0/groups/5e84b94c003f2d6370004f4e/clusters/5e84e393395ec72bfc888f6c",
          "rel": "self"
        }
      ],
      "replicaSetName": "cm-clstr-repl",
      "typeName": "REPLICA_SET"
    }
  ],
  "totalCount": 2
}
```
