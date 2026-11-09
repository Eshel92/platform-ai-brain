<!-- Converted from reference/api/organizations/organization-get-all-projects.txt (reStructuredText). Includes are inlined. -->

# Get All Projects in an Organization

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /orgs/{ORG-ID}/groups
```

## Request Parameters

### Request Path Parameters

| Path Element | Type | Description |
|---|---|---|
| ORG-ID | Required. | The unique identifier for the organization whose information you want to retrieve. |

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Description | Default |
|---|---|---|---|
| `pageNum` | integer | Page number (1-based). | `1` |
| `itemsPerPage` | integer | Number of items to return per page, up to a maximum of 500. | `100` |
| `pretty` | boolean | Displays response in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format. | `false` |
| `envelope` | boolean | Specifies whether or not to wrap the response in an envelope. | `false` |
| `name` | string | Human-readable label of the project to use to filter the returned list. Performs a case-insensitive search for a project, which is prefixed by the specified `name`, within the organization. For example, if you specify a `name` query parameter of `project1`, Ops Manager returns the project named `project1`, but would not return a project named `project123`. | None |

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

Each **result** is one project.

| Name | Type | Description |
|---|---|---|
| activeAgentCount | integer | The number of active monitoring, automation, and Backups in the project. |
| hostCounts | Document | Describes the host types and number of each host type for the cluster. |
| hostCounts.arbiter | integer | The number of arbiter hosts in the cluster. |
| hostCounts.config | integer | The number of sharded cluster configuration server hosts in the cluster. |
| hostCounts.mongos | integer | The number of mongos hosts in the cluster. |
| hostCounts.primary | integer | The number of primary hosts in the cluster. |
| hostCounts.secondary | integer | The number of secondary hosts in the cluster. |
| id | string | The unique identifier for the project. |
| links | object array | .. include:: /includes/api/links-explanation.rst |
| name | string | The name of the cluster. |
| orgId | string | The unique identifier for the parent organization of the project. |
| publicApiEnabled | boolean | The status of API access to the cluster. |
| replicaSetCount | integer | The number of replica sets in the cluster. |
| shardCount | integer | The number of shards in the cluster. |

## Example Request

```shell
curl --user "{username:apiKey}" \
  --include \
  --header "Content-Type: application/json" \
  --digest GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/groups"
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

```http
{
  "links": [
    {

    }
  ],
  "results": [
    {
      "activeAgentCount": 0,
      "hostCounts": {
        "arbiter": 0,
        "config": 0,
          "mongos": 0,
        "primary": 1,
        "secondary": 2
        },
      "id": "{PROJECT-ID}",
      "links": [
        {

        }
      ],
      "name": "Production Cluster",
      "orgId": "{ORG-ID}",
      "publicApiEnabled": true,
      "replicaSetCount": 1,
      "shardCount": 0
    },
    {
      "activeAgentCount": 0,
      "hostCounts": {
        "arbiter": 0,
        "config": 0,
          "mongos": 0,
        "primary": 1,
        "secondary": 2
        },
      "id": "{PROJECT-ID}",
      "lastActiveAgent": "2017-10-26T02:39:59Z",
      "links": [
        {

        }
      ],
      "name": "Staging Cluster",
      "orgId": "{ORG-ID}",
      "publicApiEnabled": true,
      "replicaSetCount": 1,
      "shardCount": 0
    }
  ],
  "totalCount": 2
}
```
