<!-- Converted from reference/api/clusters/clusters-get-all-key.txt (reStructuredText). Includes are inlined. -->

# Get All Clusters in All Projects

Get details for all clusters in all projects available to the 
programmatic API key making the request.

## Required Roles

You can successfully call this endpoint with any assigned role.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /api/public/v1.0/clusters
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

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

Each **result** is one project.

* - Name
  - Type
  - Description

* - `clusters`
  - array of objects
  - Objects that describe the clusters in each project that the API
    key is authorized to view.

* - `clusters.[n].alertCount`
  - integer
  - Number of open alerts.

* - `clusters.[n].authEnabled`
  - boolean
  - Specifies if authentication is required to access the nodes
    in the cluster.

* - `clusters.[n].availability`
  - string
  -  Availability of the cluster. Values include:

     - `available`: All nodes in the cluster are available.
     - `warning`: Some nodes in the cluster are available. At 
       least one node is unavailable.
     - `unavailable`: The cluster is unavailable. The cluster
       does not have a primary node.
     - `dead`: The cluster is inactive.

* - `clusters.[n].backupEnabled`
  - boolean
  - Specifies if backup is enabled for the cluster.

* - `clusters.[n].clusterId`
  - string
  - Unique identifier of the Ops Manager cluster.

* - `clusters.[n].dataSizeBytes`
  - number
  - Total size of the data stored on each node in the cluster in 
    bytes.

* - `clusters.[n].name`
  - string
  - Name of the cluster as it appears in Ops Manager.

* - `clusters.[n].nodeCount`
  - integer
  - Number of nodes in the cluster.

* - `clusters.[n].sslEnabled`
  - boolean
  - Specifies if SSL (Secure Sockets Layer) authentication is required to access the nodes
    in the cluster.

* - `clusters.[n].type`
  - string
  - The type of MongoDB cluster. Values include:

    - `replica set`: replica set
    - `sharded cluster`: sharded cluster
    - `standalone`: standalone

* - `clusters.[n].versions`
  - array of strings
  - Version of MongoDB that each node in the cluster is running.

* - `groupId`
  - string
  - Unique identifier of the project.

* - `groupName`
  - string
  - Name of the project to which the returned clusters belong.

* - `orgId` 
  - string
  - Unique identifier for the organization that owns the project to
    which the returned clusters belong.

* - `orgName`
  - string
  - Name of the organization that owns the project to
    which the returned clusters belong.

* - `planType`
  - string
  - Plan type.

    In Ops Manager, this value is always Ops Manager.

* - `tags`
  - array of strings
  - Tags applied to the project.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/clusters?pretty=true"
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
      "href": "https://example.com:8080/api/public/v1.0/clusters",
      "rel": "self"
    }
  ],
  "results": [
    {
      "clusters": [
        {
          "alertCount": 0,
          "authEnabled": true,
          "availability": "available",
          "backupEnabled": false,
          "clusterId": "5e6bc0352e41683c191c8956",
          "dataSizeBytes": 0,
          "name": "Cluster1",
          "nodeCount": 3,
          "sslEnabled": true,
          "type": "replica set",
          "versions": [
            "4.2.3"
          ]
        },
        {
          "alertCount": 0,
          "authEnabled": true,
          "availability": "available",
          "backupEnabled": false,
          "clusterId": "5e6bc60ba4c3f47a54d8fe95",
          "dataSizeBytes": 0,
          "name": "Cluster2",
          "nodeCount": 3,
          "sslEnabled": true,
          "type": "replica set",
          "versions": [
            "4.2.3"
          ]
        }
      ],
      "groupId": "5df90932f10fab675508b0e5",
      "groupName": "az",
      "orgId": "5df7a168f10fab3a149357fb",
      "orgName": "jww-12-16",
      "planType": "Ops Manager",
      "tags": [

      ]
    },
    {
      "clusters": [
        {
          "alertCount": 0,
          "authEnabled": true,
          "availability": "available",
          "backupEnabled": false,
          "clusterId": "5e6bbf6a9de0d35b1527dd93",
          "dataSizeBytes": 0,
          "name": "Cluster0",
          "nodeCount": 3,
          "sslEnabled": true,
          "type": "replica set",
          "versions": [
            "4.2.3"
          ]
        }
      ],
      "groupId": "5df90590f10fab5e33de2305",
      "groupName": "jww-12-17",
      "orgId": "5df7a168f10fab3a149357fb",
      "orgName": "jww-12-16",
      "planType": "Ops Manager",
      "tags": [

      ]
    },
    {
      "clusters": [
        {
          "alertCount": 0,
          "authEnabled": true,
          "availability": "dead",
          "backupEnabled": false,
          "clusterId": "5e6be93fd434591c4ca765f6",
          "dataSizeBytes": 0,
          "name": "Cluster0",
          "nodeCount": 0,
          "sslEnabled": true,
          "type": "replica set",
          "versions": [
            "4.2.3"
          ]
        }
      ],
      "groupId": "5df90923f10fab675508b065",
      "groupName": "gcp",
      "orgId": "5df7a168f10fab3a149357fb",
      "orgName": "jww-12-16",
      "planType": "Ops Manager",
      "tags": [

      ]
    }
  ],
  "totalCount": 3
}
```
