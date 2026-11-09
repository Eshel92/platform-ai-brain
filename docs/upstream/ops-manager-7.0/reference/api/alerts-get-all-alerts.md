<!-- Converted from reference/api/alerts-get-all-alerts.txt (reStructuredText). Includes are inlined. -->

# Get All Alerts

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/alerts
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | *(Required.)* Project identifier. |

### Request Query Parameters

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

* - Name
  - Type
  - Necessity
  - Description

* - `status`
  - string
  - Optional
  - Specify a status to return only those alerts with
    the specified status. Omit to return all alerts.

    Ops Manager accepts the following values:

    - `TRACKING`
         To return alerts with `TRACKING` status. If an alert's
         configuration specifies a
         notification delay, Ops Manager assigns the alert the
         `TRACKING` status until the delay period ends. After the
         delay, Ops Manager sets the status to `OPEN`, if the condition
         persists.

         If an alert's configuration has multiple notifications,
         each with its own notification delay, Ops Manager uses the
         smallest delay value to determine when to move the alert
         from `TRACKING` to `OPEN`.

    - `OPEN`
         To return all open alerts.

    - `CLOSED`
         To return all closed alerts.

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

Each **result** is one alert.

* - Name
  - Type
  - Description

* - | `acknowledged`
    | `Until`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) until which the alert has been acknowledged.

    Ops Manager returns this value if the alert has been acknowledged.

* - | `acknowledgement`
    | `Comment`
  - string
  - Comment left by the user who acknowledged the alert.

    Ops Manager returns this value if the alert has been acknowledged.

* - | `acknowledging`
    | `Username`
  - string
  - Username of the user who acknowledged the alert.

    Ops Manager returns this value if the alert has been acknowledged.

* - `alertConfigId`
  - string
  - Unique identifier for the alert configuration that triggered
    this alert.

* - `clusterId`
  - string
  - Unique identifier for the cluster to which this alert applies.

    Ops Manager returns this value if
    `"eventTypeName" : "SHARDED_CLUSTER"`

* - `clusterName`
  - string
  - Name of the cluster to which this alert applies.

    Ops Manager returns this value if
    `"eventTypeName" : "SHARDED_CLUSTER"`

* - `created`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was opened.

* - `currentValue`
  - object
  - Current value of the metric that triggered the alert.

    Ops Manager returns this value if
    `"eventTypeName" : "OUTSIDE_METRIC_THRESHOLD"`.

* - | `currentValue`
    | `.number`
  - number
  - Value of the metric.

* - | `currentValue`
    | `.units`
  - string
  - Units for the value. Value depends on the type of metric.

    For example, a metric that measures memory consumption would have a byte
    measurement, while a metric that measures time would have a
    time unit.

    Ops Manager can return:

    - `RAW`
    - `BITS`
    - `BYTES`
    - `KILOBITS`
    - `KILOBYTES`
    - `MEGABITS`
    - `MEGABYTES`
    - `GIGABITS`
    - `GIGABYTES`
    - `TERABYTES`
    - `PETABYTES`
    - `MILLISECONDS`
    - `SECONDS`
    - `MINUTES`
    - `HOURS`
    - `DAYS`

* - `eventTypeName`
  - string
  - Name of the event that triggered the alert.

    Accepted values are: 

    **Agent**

    - `AUTOMATION_AGENT_DOWN`
    - `AUTOMATION_AGENT_UP`
    - `BACKUP_AGENT_CONF_CALL_FAILURE`
    - `BACKUP_AGENT_DOWN`
    - `BACKUP_AGENT_UP`
    - `BACKUP_AGENT_VERSION_BEHIND`
    - `BACKUP_AGENT_VERSION_CURRENT`
    - `MONITORING_AGENT_DOWN`
    - `MONITORING_AGENT_UP`
    - `MONITORING_AGENT_VERSION_BEHIND`
    - `MONITORING_AGENT_VERSION_CURRENT`
    - `NEW_AGENT`

    **Automation Configuration**

    - `AUTOMATION_CONFIG_PUBLISHED_AUDIT`

    **Backup**
    - `BAD_CLUSTERSHOTS`
    - `CLUSTER_BLACKLIST_UPDATED_AUDIT`
    - `CLUSTER_CHECKKPOINT_UPDATED_AUDIT`
    - `CLUSTER_CREDENTIAL_UPDATED_AUDIT`
    - `CLUSTER_SNAPSHOT_SCHEDULE_UPDATED_AUDIT`
    - `CLUSTER_STATE_CHANGED_AUDIT`
    - `CLUSTER_STORAGE_ENGINE_UPDATED_AUDIT`
    - `CLUSTERSHOT_DELETED_AUDIT`
    - `CLUSTERSHOT_EXPIRY_UPDATED_AUDIT`
    - `CONSISTENT_BACKUP_CONFIGURATION`
    - `GOOD_CLUSTERSHOT`
    - `INCONSISTENT_BACKUP_CONFIGURATION`
    - `INITIAL_SYNC_FINISHED_AUDIT`
    - `INITIAL_SYNC_STARTED_AUDIT`
    - `OPLOG_BEHIND`
    - `OPLOG_CURRENT`
    - `RESTORE_REQUESTED_AUDIT`
    - `RESYNC_PERFORMED`
    - `RESYNC_REQUIRED`
    - `RS_BLACKLIST_UPDATED_AUDIT`
    - `RS_CREDENTIAL_UPDATED_AUDIT`
    - `RS_ROTATE_MASTER_KEY_AUDIT`
    - `RS_SNAPSHOT_SCHEDULE_UPDATED_AUDIT`
    - `RS_STATE_CHANGED_AUDIT`
    - `RS_STORAGE_ENGINE_UPDATED_AUDIT`
    - `SNAPSHOT_DELETED_AUDIT`
    - `SNAPSHOT_EXPIRY_UPDATED_AUDIT`
    - `SYNC_PENDING_AUDIT`
    - `SYNC_REQUIRED_AUDIT`

    **BI Connector**

    - `BI_CONNECTOR_DOWN`
    - `BI_CONNECTOR_UP`

    **Cluster**

    - `CLUSTER_MONGOS_IS_MISSING`
    - `CLUSTER_MONGOS_IS_PRESENT`
    - `SHARD_ADDED`
    - `SHARD_REMOVED`

    **Data Explorer Accessed**

    - `DATA_EXPLORER`
    - `DATA_EXPLORER_CRUD`

    **Host**

    - `ATTEMPT_KILLOP_AUDIT`
    - `ATTEMPT_KILLSESSION_AUDIT`
    - `DB_PROFILER_DISABLE_AUDIT`
    - `DB_PROFILER_ENABLE_AUDIT`
    - `DISABLE_HOST_AUDIT`
    - `HIDE_AND_DISABLE_HOST_AUDIT`
    - `HIDE_HOST_AUDIT`
    - `HOST_DOWN`
    - `HOST_DOWNGRADED`
    - `HOST_IP_CHANGED_AUDIT`
    - `HOST_NOW_PRIMARY`
    - `HOST_NOW_SECONDARY`
    - `HOST_NOW_STANDALONE`
    - `HOST_RECOVERED`
    - `HOST_RECOVERING`
    - `HOST_SECURITY_CHECKUP_NOT_MET`
    - `HOST_SSL_CERTIFICATE_CURRENT`
    - `HOST_SSL_CERTIFICATE_STALE`
    - `HOST_UP`
    - `HOST_UPGRADED`
    - `INSIDE_METRIC_THRESHOLD`
    - `NEW_HOST`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `PAUSE_HOST_AUDIT`
    - `RESUME_HOST_AUDIT`
    - `UNDELETE_HOST_AUDIT`
    - `VERSION_BEHIND`
    - `VERSION_CHANGED`
    - `VERSION_CURRENT`

    **Organization**

    - `ALL_ORG_USERS_HAVE_MFA`
    - `ORG_API_KEY_ADDED`
    - `ORG_API_KEY_DELETED`
    - `ORG_EMPLOYEE_ACCESS_RESTRICTED`
    - `ORG_EMPLOYEE_ACCESS_UNRESTRICTED`
    - `ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED`
    - `ORG_PUBLIC_API_ACCESS_LIST_REQUIRED`
    - `ORG_RENAMED`
    - `ORG_TWO_FACTOR_AUTH_OPTIONAL`
    - `ORG_TWO_FACTOR_AUTH_REQUIRED`
    - `ORG_USERS_WITHOUT_MFA`

    **Project**

    - `ALL_USERS_HAVE_MULTI_FACTOR_AUTH`
    - `USERS_WITHOUT_MULTI_FACTOR_AUTH`

    **Replica Set**

    - `CONFIGURATION_CHANGED`
    - `ENOUGH_HEALTHY_MEMBERS`
    - `MEMBER_ADDED`
    - `MEMBER_REMOVED`
    - `MULTIPLE_PRIMARIES`
    - `NO_PRIMARY`
    - `ONE_PRIMARY`
    - `TOO_FEW_HEALTHY_MEMBERS`
    - `TOO_MANY_ELECTIONS`
    - `TOO_MANY_UNHEALTHY_MEMBERS`

    **Team**

    - `TEAM_ADDED_TO_GROUP`
    - `TEAM_CREATED`
    - `TEAM_DELETED`
    - `TEAM_NAME_CHANGED`
    - `TEAM_REMOVED_FROM_GROUP`
    - `TEAM_ROLES_MODIFIED`
    - `TEAM_UPDATED`
    - `USER_ADDED_TO_TEAM`

    **User**

    - `INVITED_TO_GROUP`
    - `INVITED_TO_ORG`
    - `JOIN_GROUP_REQUEST_APPROVED_AUDIT`
    - `JOIN_GROUP_REQUEST_DENIED_AUDIT`
    - `JOINED_TEAM`
    - `REMOVED_FROM_TEAM`
    - `REQUESTED_TO_JOIN_GROUP`

    For a complete list of events included in the Ops Manager audit 
    log, see Audit Events.

* - `groupId`
  - string
  - Unique identifier of the group for which this alert was opened.

* - `hostId`
  - string
  - unique identifier for the host to which the metric pertains.

    Ops Manager returns this value if `"eventTypeName"` was set to one
    of the following:

    - `HOST_DOWN`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REPLICA_SET`

* - `hostnameAndPort`
  - string
  - Hostname and port of each host to which the alert applies. This
    can be a hostname, an FQDN (fully qualified domain name), an IPv4 (Internet Protocol version 4) address, or an IPv6 (Internet Protocol version 6)
    address.

    Ops Manager returns this value if `"eventTypeName"` was set to one
    of the following:

    - `HOST_DOWN`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REPLICA_SET`

* - `id`
  - string
  - Unique identifier for the alert.

* - `lastNotified`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the last notification was sent for this
    alert. Ops Manager returns this value if notifications have been sent.

* - `links`
  - array of objects
  - .. include:: /includes/api/links-explanation.rst

* - `metricName`
  - string
  - Name of the measurement whose value went outside the
    threshold.

    Ops Manager returns this value if `"eventTypeName"` was set to
    `OUTSIDE_METRIC_THRESHOLD`.

    For possible values, see measurement-types-for-alerts-api.

* - `replicaSetName`
  - string
  - Name of the replica set.

    Ops Manager returns this value if `"eventTypeName"` was set to one
    of the following:

    - `BACKUP`
    - `HOST_DOWN`
    - `OUTSIDE_METRIC_THRESHOLD`
    - `REPLICA_SET`

* - `resolved`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was closed.

    Ops Manager returns this value if `"status" : "CLOSED"`.

* - `status`
  - string
  - Current state of the alert. Ops Manager can return one of the
    following:

    - `TRACKING`

      The alert condition exists but has not persisted beyond the
      defined notification delay. For details, see
      api-alert-status.

    - `OPEN`
    - `CLOSED`
    - `CANCELLED`

* - `sourceTypeName`
  - string
  - Type of host being backed up when ``"eventTypeName" :
    "BACKUP"``. Ops Manager can return one of the following:

    - `REPLICA_SET`
    - `SHARDED_CLUSTER`
    - `CONFIG_SERVER`

* - `tags`
  - string array
  - Identifying labels set for this alert.

* - `updated`
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the alert was last updated.

### Measurement Types for Alerts

The `alerts` resource returns measurement types in the `metricName`
field. The field is present only if `eventTypeName` is set to
`OUTSIDE_METRIC_THRESHOLD`.

### Host Measurements

* - - `ASSERT_REGULAR`
    - `ASSERT_WARNING`
    - `ASSERT_MSG`
    - `ASSERT_USER`

  - Rate of asserts for a MongoDB process found in the 
    `asserts` document that the
    serverStatus
    command generates.

* - - `BACKGROUND_FLUSH_AVG`

  - Amount of data flushed in the background.

* - - `CACHE_BYTES_READ_INTO`
    - `CACHE_BYTES_WRITTEN_FROM`
    - `CACHE_DIRTY_BYTES`
    - `CACHE_USED_BYTES`
    - `TICKETS_AVAILABLE_READS`
    - `TICKETS_AVAILABLE_WRITE`

  - Amount of bytes in the WiredTiger
    storage engine cache and tickets found in the
    `wiredTiger.cache` and
    `wiredTiger.concurrentTransactions` documents
    that the
    serverStatus
    command generates.

* - - `CONNECTIONS`

  - Number of connections to a MongoDB process found in the
    `connections` document that the
    serverStatus
    command generates.

* - - `CURSORS_TOTAL_OPEN`
    - `CURSORS_TOTAL_TIMED_OUT`

  - Number of cursors for a MongoDB
    process found in the `metrics.cursor` document 
    that the 
    serverStatus
    command generates.

* - - `EXTRA_INFO_PAGE_FAULTS`
    - `GLOBAL_ACCESSES_NOT_IN_MEMORY`
    - `GLOBAL_PAGE_FAULT_EXCEPTIONS_THROWN`

  - Numbers of `Memory Issues` and `Page Faults` for a MongoDB
    process.

* - - `GLOBAL_LOCK_CURRENT_QUEUE_TOTAL`
    - `GLOBAL_LOCK_CURRENT_QUEUE_READERS`
    - `GLOBAL_LOCK_CURRENT_QUEUE_WRITERS`

  - Number of operations waiting on locks for the MongoDB process
    that the 
    serverStatus 
    command generates. Ops Manager computes these values based on the
    type of storage engine.

* - - `INDEX_COUNTERS_BTREE_ACCESSES`
    - `INDEX_COUNTERS_BTREE_HITS`
    - `INDEX_COUNTERS_BTREE_MISSES`
    - `INDEX_COUNTERS_BTREE_MISS_RATIO`

  - Number of index btree operations.

* - - `JOURNALING_COMMITS_IN_WRITE_LOCK`
    - `JOURNALING_MB`
    - `JOURNALING_WRITE_DATA_FILES_MB`

  - Number of journaling operations.

* - - `MEMORY_RESIDENT`
    - `MEMORY_VIRTUAL`
    - `MEMORY_MAPPED`
    - `COMPUTED_MEMORY`

  - Amount of memory for a MongoDB process found in the
    `mem` document that the
    serverStatus command collects.

* - - `NETWORK_BYTES_IN`
    - `NETWORK_BYTES_OUT`
    - `NETWORK_NUM_REQUESTS`

  - Amount of throughput for MongoDB process found in the
    `network` document that the 
    serverStatus command collects.

* - - `OPLOG_RATE_GB_PER_HOUR`
    - `OPLOG_MASTER_TIME`
    - `OPLOG_MASTER_LAG_TIME_DIFF`
    - `OPLOG_SLAVE_LAG_MASTER_TIME`

  - Durations and throughput of the MongoDB process'
    oplog.

* - - `DB_STORAGE_TOTAL`
    - `DB_DATA_SIZE_TOTAL`

  - On-disk storage space as collected from the MongoDB `dbStats`
    command.

* - - `OPCOUNTER_CMD`
    - `OPCOUNTER_QUERY`
    - `OPCOUNTER_UPDATE`
    - `OPCOUNTER_DELETE`
    - `OPCOUNTER_GETMORE`
    - `OPCOUNTER_INSERT`

  - Rate of database operations on a MongoDB process since the
    process last started found in the `opcounters` document that the 
    serverStatus command collects.

* - - `OPCOUNTER_REPL_CMD`
    - `OPCOUNTER_REPL_UPDATE`
    - `OPCOUNTER_REPL_DELETE`
    - `OPCOUNTER_REPL_INSERT`

  - Rate of database operations on MongoDB
    secondaries found in the
    `opcountersRepl` document that the
    serverStatus
    command collects.

* - - `DOCUMENT_METRICS_RETURNED`
    - `DOCUMENT_METRICS_INSERTED`
    - `DOCUMENT_METRICS_UPDATED`
    - `DOCUMENT_METRICS_DELETED`

  - Average rate of documents returned, inserted, updated, or
    deleted per second during a selected time period.

* - - `OPERATIONS_SCAN_AND_ORDER`

  - Average rate for operations per second during a selected time
    period that perform a sort but cannot perform the sort using an
    index.

* - - `OP_EXECUTION_TIME_READS`
    - `OP_EXECUTION_TIME_WRITES`
    - `OP_EXECUTION_TIME_COMMANDS`

  - Average execution time in milliseconds per read, write, or
    command operation during a selected time period.

    *Available to hosts running MongoDB 3.4 or later.*

* - - `RESTARTS_IN_LAST_HOUR`

  - Number of times the host restarted within the previous hour.

* - - `SYSTEM_MEMORY_USED`
    - `SYSTEM_MEMORY_FREE`
    - `SYSTEM_MEMORY_AVAILABLE`

  - Physical memory usage, in bytes.

* - - `SYSTEM_NETWORK_BYTES_IN`
    - `SYSTEM_NETWORK_BYTES_OUT`

  - Network throughput in bytes per second.

* - - `SWAP_USAGE_USED`
    - `SWAP_USAGE_FREE`

  - Total amount swap space in use.

|  |  |
|---|---|
| - `QUERY_EXECUTOR_SCANNED` | Average rate per second to scan index items during queries and query-plan evaluations found in the value of `totalKeysExamined` from the explain command. |
| - `QUERY_EXECUTOR_SCANNED_OBJECTS` | Average rate of documents scanned per second during queries and query-plan evaluations found in the value of `totalDocsExamined` from the explain command. |
| - `QUERY_TARGETING_SCANNED_PER_RETURNED` | Ratio of the number of index items scanned to the number of documents returned. |
| - `QUERY_TARGETING_SCANNED_OBJECTS_PER_RETURNED` | Ratio of the number of documents scanned to the number of documents returned. |

## Example Request

The following returns all `OPEN` alerts:

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
     --header 'Accept: application/json' \
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/alerts?status=OPEN&pretty=true"
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
  "links" : [ {
    "href" : "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/alerts?status=OPEN&pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "alertConfigId" : "5953c5f380eef53887615fd4",
    "created" : "2019-07-18T23:43:50Z",
    "eventTypeName" : "MONITORING_AGENT_DOWN",
    "groupId" : "{PROJECT-ID}",
    "id" : "5d31043680eef5280d3664e0",
    "lastNotified" : "2019-09-25T11:50:08Z",
    "links" : [ {
      "href" : "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/alerts/5d31043680eef5280d3664e0",
      "rel" : "self"
    } ],
    "status" : "OPEN",
    "tags" : [ ],
    "updated" : "2019-07-18T23:43:50Z"
  } ],
  "totalCount" : 1
}
```
