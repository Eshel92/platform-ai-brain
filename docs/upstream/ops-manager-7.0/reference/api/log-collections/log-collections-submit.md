<!-- Converted from reference/api/log-collections/log-collections-submit.txt (reStructuredText). Includes are inlined. -->

# Create a Log Collection Job

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

When you create a log collection job, Ops Manager starts a background job to
download the logs from the specified Ops Manager deployment. Use this
endpoint to create a new log collection job.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /groups/{GROUP-ID}/logCollectionJobs
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| GROUP-ID | string | Required | Unique 24-hexadecimal digit string that identifies the log collection request job. |

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

* - Name
  - Type
  - Necessity
  - Description

* - resourceType
  - string
  - Required
  - Type of resource from which to collect logs. Must be one of the
    following values:

    - `CLUSTER`, for a sharded cluster.
    - `PROCESS`, for a node in the replica set.
    - `REPLICASET`, for a replica set.`

* - resourceName
  - string
  - Required
  - Name of the resource from which to collect logs.
    The resource type defines the value:

    - For the `CLUSTER` `resourceType`, the value is the name of
      the deployment or the `CLUSTER-ID`.
      For example, `my-deployment`.

      - To obtain this value, use the
        /groups/{GROUP-ID}/clusters/{CLUSTER-ID} endpoint.

    - For the `PROCESS` `resourceType`, the value is
      the name of the replica set followed by the node name. 
      For example, `Cluster0-shard-1-node-0`.

      - To obtain this value, use the /groups/{PROJECT-ID}/automationConfig endpoint. 
        The value is located in the `processes.name` parameter.

      To obtain the name of the replica set, the list of
      nodes, and other information, access the cluster and run
      `rs.conf()._id`
      and `rs.status()`.

    - For the `REPLICASET` `resourceType`, the value is
      the name of the replica set in the cluster followed
      by the shard name. For example, `test-123abc-shard-0`.

* - sizeRequestedPerFileBytes
  - number
  - Required
  - Size for each log file in bytes.

* - logTypes
  - array
  - Required
  - Array of strings specifying the types of logs to collect. Each
    array element must be one of the following values:

    - `AUTOMATION_AGENT`
    - `BACKUP_AGENT`
    - `MONITORING_AGENT`
    - `MONGODB`
    - `FTDC`

* - redacted
  - boolean
  - Required
  - If set to `true`, emails, hostnames, IP addresses, and
    namespaces in API responses involving this job are replaced with
    random string values.

## Response

| Name | Type | Description |
|---|---|---|
| id | string | Unique identifier of the created log collection job. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{GROUP-ID}/logCollectionJobs?pretty=true" \
     --data '
       {
         "resourceType": "PROCESS",
         "resourceName": "my_deployment_1",
         "redacted": true,
         "sizeRequestedPerFileBytes": 10000000,
         "logTypes": [
             "FTDC",
             "MONGODB",
             "AUTOMATION_AGENT"
         ]
       }'
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

```json
{ "id": "5c81086e014b76a3d85e1113" }
```
