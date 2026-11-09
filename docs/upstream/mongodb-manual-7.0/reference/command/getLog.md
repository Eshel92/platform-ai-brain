<!-- Converted from reference/command/getLog.txt (reStructuredText). Includes are inlined. -->

# getLog (database command)

## Definition

**`getLog`**

`getLog` is an administrative command that returns the most
recent 1024 logged `mongod` events. `getLog` *does not*
read log data from the `mongod` log file. It instead reads data
from a RAM cache of logged `mongod` events. To run
`getLog`, use the `db.adminCommand()` method.

`getLog` returns log data in escaped 
Relaxed Extended JSON v2.0 format. 
Previously, log data was returned as plaintext.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     getLog: <value> 
   } 
)
```

## Command Fields

The possible values for `getLog` are:

| Value | Description |
|---|---|
| `*` | Returns a list of the available values to the `getLog` command. |
| `global` | Returns the combined output of all recent log entries. |
| `startupWarnings` | Returns log entries that *may* contain errors or warnings from MongoDB's log from when the current process started. If `mongod` started without warnings, this filter may return an empty array. |

**Note:**

The `getLog` command no longer accepts the `rs` value, as this 
categorization of message type has been deprecated. Instead, log messages are 
now always identified by their component -
including *REPL* for replication messages. See
log-message-parsing-example-filter-component for log
parsing examples that filter on the component field.

## Output

If specified `*`, then the command returns a document with the
names of the other acceptable values.

Otherwise, the command returns a document that includes the following
fields:

- `totalLinesWritten` field that contains the number of log events

- `log` field that contains an array of log events

- A `db.adminCommand()` response document, containing status and timestamp
  information.

## Behavior

### Line Truncation

`getLog` truncates any event that contains more than 1024 characters. 

### Character Escaping

`getLog` returns log data in escaped Relaxed Extended JSON v2.0 format, using the following escape sequences 
to render log output as valid JSON:

| Character Represented | Escape Sequence |
|---|---|
| Quotation Mark (`"`) | `\"` |
| Backslash (`\`) | `\\` |
| Backspace (`0x08`) | `\b` |
| Formfeed (`0x0C`) | `\f` |
| Newline (`0x0A`) | `\n` |
| Carriage return (`0x0D`) | `\r` |
| Horizontal tab (`0x09`) | `\t` |

Control characters not listed above are escaped with `\uXXXX` where
"XXXX" is the unicode codepoint in hexadecimal. Bytes with invalid
UTF-8 encoding are replaced with the unicode replacement character
represented by `\ufffd`.

## Filtering

### Within `mongosh`

`getLog` output can be filtered to make results more
readable or to match on specific criteria.

The following operation prints just the `log` field (which contains
the array of all recent log events), and removes
character escaping from each log
message:

```javascript
db.adminCommand( { getLog:'global'} ).log.forEach(x => {print(x)})
```

This operation presents `getLog` output in the same format as
the MongoDB `log file`.

**Note:**

`getLog` only shows the most recent 1024 logged
`mongod` events, and is not a replacement for the
MongoDB `log file`.

### Outside `mongosh` with `jq`

When working with MongoDB structured logging, you can use the third-party
[jq command-line utility](https://stedolan.github.io/jq/) for easy 
pretty-printing of log entries, and powerful key-based matching and filtering.

`jq` is an open-source JSON parser, and is available for
Linux, Windows, and macOS.

To use `jq` with `getLog` output, you must use the
`--eval` option to `mongosh`.
The following operation uses `jq` to filter on the **REPL**
component to present only those log
messages associated with replication:

```javascript
mongosh --quiet --eval "db.adminCommand( { getLog:'global'} ).log.forEach(x => {print(x)})" | jq -c '. | select(.c=="REPL")'
```

Be sure to provide any necessary connection-specific parameters to
`mongosh` as needed, such as `--host` or `--port`.

See log-message-parsing for more examples of filtering log output
using `jq`. The `jq` syntax presented in each linked example can be
used with the above `mongo --eval` operation with minor adjustment.
For example, the following syntax adapts the linked "Counting Unique
Messages" example for use with `getLog`:

```javascript
mongosh --quiet --eval "db.adminCommand( { getLog:'global'} ).log.forEach(x => {print(x)})" | jq -r ".msg" | sort | uniq -c | sort -rn | head -10
```

## Examples

### Retrieve Available Log Filters

The following operation, run from `mongosh`,
returns the available log filters for passing to `getLog`:

```javascript
db.adminCommand( { getLog: "*" } )
```

The operation returns the following document:

```javascript
{ "names" : [ "global", "startupWarnings" ], "ok" : 1 }
```

### Retrieve Recent Events from Log

The following operation, run from `mongosh`,
retrieves the most recent `global` events for the
`mongod`:

```javascript
db.adminCommand( { getLog : "global" } )
```

The operation returns a document similar to the following:

```javascript
{
      "totalLinesWritten" : <num>,
      "log" : [
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"STORAGE\",  \"id\":4615611, \"ctx\":\"initandlisten\",\"msg\":\"MongoDB starting\",\"attr\":{\"pid\":12345,\"port\":27001,\"dbPath\":\"/var/lib/mongo\",\"architecture\":\"64-bit\",\"host\":\"server1.example.com\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"CONTROL\",  \"id\":23403,   \"ctx\":\"initandlisten\",\"msg\":\"Build Info\",\"attr\":{\"buildInfo\":{\"version\":\"4.4.0\",\"gitVersion\":\"328c35e4b883540675fb4b626c53a08f74e43cf0\",\"openSSLVersion\":\"OpenSSL 1.1.1c FIPS  28 May 2019\",\"modules\":[],\"allocator\":\"tcmalloc\",\"environment\":{\"distmod\":\"rhel80\",\"distarch\":\"x86_64\",\"target_arch\":\"x86_64\"}}}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"CONTROL\",  \"id\":51765,   \"ctx\":\"initandlisten\",\"msg\":\"Operating System\",\"attr\":{\"os\":{\"name\":\"CentOS Linux release 8.0.1905 (Core) \",\"version\":\"Kernel 4.18.0-80.11.2.el8_0.x86_64\"}}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"CONTROL\",  \"id\":21951,   \"ctx\":\"initandlisten\",\"msg\":\"Options set by command line\",\"attr\":{\"options\":{\"config\":\"/etc/mongod.conf\",\"net\":{\"bindIp\":\"127.0.0.1\",\"port\":27001},\"processManagement\":{\"fork\":true,\"timeZoneInfo\":\"/usr/share/zoneinfo\"},\"replication\":{\"replSetName\":\"repl-shard1\"},\"sharding\":{\"clusterRole\":\"shardsvr\"},\"storage\":{\"dbPath\":\"/var/lib/mongo\",\"journal\":{\"enabled\":true},\"wiredTiger\":{\"engineConfig\":{\"cacheSizeGB\":0.1}}},\"systemLog\":{\"destination\":\"file\",\"logAppend\":true,\"path\":\"/var/log/mongodb/mongod.log\"}}}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.873+00:00\"},\"s\":\"I\",  \"c\":\"STORAGE\",  \"id\":22270,   \"ctx\":\"initandlisten\",\"msg\":\"Storage engine to use detected by data files\",\"attr\":{\"dbpath\":\"/var/lib/mongo\",\"storageEngine\":\"wiredTiger\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.873+00:00\"},\"s\":\"I\",  \"c\":\"STORAGE\",  \"id\":22315,   \"ctx\":\"initandlisten\",\"msg\":\"wiredtiger_open config\",\"attr\":{\"config\":\"create,cache_size=102M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server1.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server2.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server3.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server4.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server5.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server6.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":23015,   \"ctx\":\"listener\",\"msg\":\"Listening on\",\"attr\":{\"address\":\"/tmp/mongodb-27001.sock\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":23015,   \"ctx\":\"listener\",\"msg\":\"Listening on\",\"attr\":{\"address\":\"127.0.0.1\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":23016,   \"ctx\":\"listener\",\"msg\":\"Waiting for connections\",\"attr\":{\"port\":27001,\"ssl\":\"off\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:15:10.392+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":22943,   \"ctx\":\"listener\",\"msg\":\"connection accepted\",\"attr\":{\"remote\":\"127.0.0.1:35724\",\"sessionId\":67,\"connectionCount\":30}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:15:10.393+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":51800,   \"ctx\":\"conn67\",\"msg\":\"client metadata\",\"attr\":{\"remote\":\"127.0.0.1:35724\",\"client\":\"conn67\",\"doc\":{\"application\":{\"name\":\"MongoDB Shell\"},\"driver\":{\"name\":\"MongoDB Internal Client\",\"version\":\"4.4.0\"},\"os\":{\"type\":\"Linux\",\"name\":\"CentOS Linux release 8.0.1905 (Core) \",\"architecture\":\"x86_64\",\"version\":\"Kernel 4.18.0-80.11.2.el8_0.x86_64\"}}}}"
      ],
      "ok" : 1,
      "$gleStats" : {
              "lastOpTime" : Timestamp(<ts>),
              "electionId" : ObjectId(<id>)
      },
      "lastCommittedOpTime" : Timestamp(<ts>),
      "$configServerState" : {
              "opTime" : {
                      "ts" : Timestamp(<ts>),
                      "t" : Long(8)
               }
      },
      "$clusterTime" : {
              "clusterTime" : Timestamp(<ts>),
              "signature" : {
                      "hash" : BinData(<bin>),
                      "keyId" : Long(0)
               }
      },
      "operationTime" : Timestamp(<ts>)
}
```
