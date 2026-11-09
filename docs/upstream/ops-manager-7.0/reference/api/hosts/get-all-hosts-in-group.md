<!-- Converted from reference/api/hosts/get-all-hosts-in-group.txt (reStructuredText). Includes are inlined. -->

# Get All Hosts in One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Get all MongoDB hosts in a project. Use the **CLUSTER-ID** query
parameter to only get the hosts that belong to the specified
cluster. The response sorts the hosts alphabetically by
**HOSTNAME:PORT**.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/hosts
```

```http
GET /groups/{PROJECT-ID}/hosts?clusterId={CLUSTER-ID}
```

### Request Path Parameters

| Parameter | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique identifier of the project that owns this MongoDB host. |

### Request Query Parameters

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

| Parameter | Type | Necessity | Description |
|---|---|---|---|
| CLUSTER-ID | string | Required | Unique identifier of the cluster in which this MongoDB process belongs. |

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

Each **result** is one host.

* - Name
  - Type
  - Description

* - aliases
  - array of strings
  - Array of alternate hostname and port combinations that Ops Manager
    discovered for the MongoDB process. These combinations can
    include hostnames, FQDN (fully qualified domain name)\s, IPv4 (Internet Protocol version 4) addresses, and IPv6 (Internet Protocol version 6)
    addresses.

* - alertsEnabled
  - boolean
  - `true` if this MongoDB process has alerts enabled.

* - authMechanismName
  - string
  - Authentication mechanism used to connect to this MongoDB
    process. This displays only one of the following values:

    - `MONGODB_CR` (This covers SCRAM-SHA-1, SCRAM-SHA-256, and MONGODB-CR.)
    - `GSSAPI`
    - `PLAIN`
    - `MONGODB_X509`
    - `NONE`

* - clusterId
  - string
  - Unique identifier of the cluster to which the MongoDB
    process belongs.

* - created
  - date
  - Date Ops Manager created or first discovered this MongoDB process.

* - groupId
  - string
  - Unique identifier of the `group` that owns this host.

* - hasStartupWarnings
  - boolean
  - `true` if this MongoDB process had startup warnings.

* - hidden
  - boolean
  - `true` if host is displayed in the Ops Manager UI. Hosts set to
    `true` are omitted from API (Application Programming Interface) responses.

* - hiddenSecondary
  - boolean
  - `true` if this host is a 
    hidden secondary.

* - hostEnabled
  - boolean
  - `true` if the MongoDB process currently enabled.

* - hostname
  - string
  - Primary hostname as Ops Manager can best determine. This can be a
    hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6) address.

* - id
  - string
  - Unique identifier.

* - ipAddress
  - string
  - IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6) address associated with the `hostname` of
    this MongoDB process. Additional accessible IPv4 (Internet Protocol version 4) or IPv6 (Internet Protocol version 6)
    addresses may be displayed in the `aliases` array.

* - journalingEnabled
  - boolean
  - `true` if journaling is enabled for this MongoDB process.

* - lastDataSizeBytes
  - number
  - Uncompressed size of the host's databases on disk in
    bytes excluding indexes. `lastDataSizeBytes` *does not*
    include the data in the
    local database.

* - lastIndexSizeBytes
  - number
  - Uncompressed size of the host's database indexes on disk
    in bytes. This number *does not* include the size of the
    index for the local
    database.

* - lastPing
  - date
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the last ping for this MongoDB process
    was received.

* - lastRestart
  - date
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when this process last restarted. If the
    MongoDB process has never been restarted, the `lastRestart`
    field is omitted.

* - links
  - array
  - Array that includes one or more links to sub-resources and/or
    related resources. The relations between URLs are explained
    in the [Web Linking Specification](http://tools.ietf.org/html/rfc5988). At minimum, a
    `links` array contains one link called `self`.

* - logsEnabled
  - boolean
  - `true` if Ops Manager is collecting logs for this MongoDB
    process.

* - lowUlimit
  - boolean
  - `true` if this MongoDB process's host has a low `ulimit`
    setting.

* - port
  - number
  - Port on which the MongoDB process listens.

* - profilerEnabled
  - boolean
  - `true` if Ops Manager collects profile information from this
    MongoDB process.

* - replicaSetName
  - string
  - Name of the replica set this process belongs to. Only present
    if this process is part of a replica set.

* - replicaStateName
  - string
  - Current state of this MongoDB process within a replica set.
    Only present if this process is part of a replica set. See
    Replica Set Member States
    for possible values.

* - shardName
  - string
  - Name of the shard to which this process belongs. Only present
    if the process is part of a sharded cluster.

* - secondaryDelaySecs
  - number
  - Number of seconds this replica set member's data 
    trails the primary. If this value is set to `0`, 
    the member is not configured as a delayed member. 
    For additional details on secondary delays, see 
    Delayed Replica Set Members

* - sslEnabled
  - boolean
  - `true` if TLS (Transport Layer Security)/SSL (Secure Sockets Layer) and is enabled for this MongoDB
    process.

* - systemInfo
  - object
  - Object that contains RAM and CPU information for this MongoDB 
    process' server as reported by the operating system or 
    container.

* - systemInfo.memSizeMB
  - number
  - Amount of RAM in megabytes.

* - systemInfo.numCores
  - number
  - Number of CPU cores.

* - typeName
  - string
  - Type for this MongoDB process. Possible values are:

    - `STANDALONE`
    - `REPLICA_PRIMARY`
    - `REPLICA_SECONDARY`
    - `REPLICA_ARBITER`
    - `RECOVERING`
    - `SHARD_MONGOS`
    - `SHARD_CONFIG`
    - `SHARD_STANDALONE`
    - `SHARD_PRIMARY`
    - `SHARD_SECONDARY`
    - `NO_DATA`

    The type for new hosts added to Ops Manager will be `NO_DATA`
    until the Monitoring receives its first ping.

* - uptimeMsec
  - number
  - Number of milliseconds since this process last restarted.

* - version
  - string
  - Version of MongoDB running for this process.

**Note:**

Some hosts don't return **clusterId**. This occurs when a `mongos`
process routes data operations to shards that don't store data.
Ops Manager doesn't assign a **clusterId** to some non-data bearing nodes.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/hosts?pretty=true"
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
  "totalCount" : 2,
  "results" : [
    {
      "alertsEnabled" : true,
      "aliases": [ "{HOSTNAME}:26000", "{IP-ADDRESS}:26000" ],
      "authMechanismName" : "SCRAM-SHA-1",
      "clusterId" : "{CLUSTER-ID}",
      "created" : "2014-04-22T19:56:50Z",
      "groupId" : "{PROJECT-ID}",
      "hasStartupWarnings" : false,
      "hidden" : false,
      "hostEnabled" : true,
      "hostname" : "{HOSTNAME}",
      "id" : "{HOST-ID}",
      "ipAddress": "127.0.0.1",
      "journalingEnabled" : false,
      "lastDataSizeBytes" : 633208918,
      "lastIndexSizeBytes" : 101420524,
      "lastPing" : "2016-08-18T11:23:41Z",
      "links" : [  ],
      "logsEnabled" : false,
      "lowUlimit" : false,
      "muninEnabled" : false,
      "port" : 26000,
      "profilerEnabled" : false,
      "replicaSetName": "rs1",
      "replicaStateName" : "PRIMARY",
      "sslEnabled" : true,
      "systemInfo" : {
        "memSizeMB" : 65536,
        "numCores" : 16
      },
      "typeName": "REPLICA_PRIMARY",
      "uptimeMsec": 1827300394,
      "username" : "mongo",
      "version" : "4.0.0"
    },
    {

    }
  ]
}
```

**Note:**

Although Ops Manager returns **muninEnabled** in the response,
[Munin](http://munin-monitoring.org/) is unsupported as of
Ops Manager 4.4.
