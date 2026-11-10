<!-- Converted from cat/thread_pool.asciidoc (AsciiDoc). Includes are inlined. -->

### cat thread pool API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the nodes info API.

Returns thread pool statistics for each node in a cluster. Returned information
includes all built-in thread pools and custom thread
pools.

#### Request

`GET /_cat/thread_pool/<thread_pool>`

`GET /_cat/thread_pool`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Path parameters

`<thread_pool>`::
(Optional, string) Comma-separated list of thread pool names used to limit the
request. Accepts wildcard expressions.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default
columns in the order listed below. If you explicitly specify one or more
columns, it only returns the specified columns.

Valid columns are:

`node_name`::
(Default) Node name, such as `I8hydUG`.

`name`::
(Default) Name of the thread pool, such as `analyze` or `generic`.

`active`, `a`::
(Default) Number of active threads in the current thread pool.

`queue`,`q`::
(Default) Number of tasks in the queue for the current thread pool.

`rejected`, `r`::
(Default) Number of tasks rejected by the thread pool executor.

`completed`, `c`::
Number of tasks completed by the thread pool executor.

`core`, `cr`::
Configured core number of active threads allowed in the current thread pool.

`ephemeral_id`,`eid`::
Ephemeral node ID.

`host`, `h`::
Hostname for the current node.

`ip`, `i`::
IP address for the current node.

`keep_alive`, `k`::
Configured keep alive time for threads.

`largest`, `l`::
Highest number of active threads in the current thread pool.

`max`, `mx`::
Configured maximum number of active threads allowed in the current thread pool.

`node_id`, `id`::
ID of the node, such as `k0zy`.

`pid`, `p`::
Process ID of the running node.

`pool_size`, `psz`::
Number of threads in the current thread pool.

`port`, `po`::
Bound transport port for the current node.

`queue_size`, `qs`::
Maximum number of tasks permitted in the queue for the current thread pool.

`size`, `sz`::
Configured fixed number of active threads allowed in the current thread pool.

`type`, `t`::
Type of thread pool. Returned values are `fixed`, `fixed_auto_queue_size`, `direct`, or `scaling`.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

##### Example with default columns

```console
GET /_cat/thread_pool
```

The API returns the following response:

```txt
node-0 analyze             0 0 0
...
node-0 fetch_shard_started 0 0 0
node-0 fetch_shard_store   0 0 0
node-0 flush               0 0 0
...
node-0 write               0 0 0
```

##### Example with explicit columns

The following API request returns the `id`, `name`, `active`, `rejected`, and
`completed` columns. The request limits returned information to the `generic`
thread pool.

```console
GET /_cat/thread_pool/generic?v=true&h=id,name,active,rejected,completed
```

The API returns the following response:

```txt
id                     name    active rejected completed
0EWUhXeBQtaVGlexUeVwMg generic      0        0        70
```
