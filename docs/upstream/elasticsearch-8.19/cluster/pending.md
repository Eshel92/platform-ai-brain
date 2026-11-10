<!-- Converted from cluster/pending.asciidoc (AsciiDoc). Includes are inlined. -->

### Pending cluster tasks API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns cluster-level changes that have not yet been executed.

#### Request

`GET /_cluster/pending_tasks`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The pending cluster tasks API returns a list of any cluster-level changes (e.g. 
create index, update mapping, allocate or fail shard) which have not yet been 
executed.

**Note:** This API returns a list of any pending updates to the cluster state. These are distinct from the tasks reported by the
Task Management API which include periodic tasks and tasks initiated by the user, such as node stats, search queries, or create
index requests. However, if a user-initiated task such as a create index command causes a cluster state update, the activity of this task
might be reported by both task api and pending cluster tasks API.

#### Path parameters

`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Response body

`tasks`::
    (object) A list of pending tasks.
    
`insert_order`::
    (integer) The number that represents when the task has been inserted into 
    the task queue.
    
`priority`::
    (string) The priority of the pending task. The valid priorities in descending priority order are: `IMMEDIATE` > `URGENT` > `HIGH` > `NORMAL` > `LOW` > `LANGUID`. 
    
`source`::
    (string) A general description of the cluster task that may include a reason 
    and origin. 
    
`executing`::
    (boolean) True or false, indicating whether the pending tasks is currently getting executed or not.
    
`time_in_queue_millis`::
    (integer) The time expressed in milliseconds since the task is waiting for 
    being performed.
    
`time_in_queue`::
    (string) The time since the task is waiting for being performed.

#### Examples

Usually the request will return an empty list as cluster-level changes are fast. 
However, if there are tasks queued up, the response will look similar like this:

```js
{
   "tasks": [
      {
         "insert_order": 101,
         "priority": "URGENT",
         "source": "create-index [foo_9], cause [api]",
         "executing" : true,
         "time_in_queue_millis": 86,
         "time_in_queue": "86ms"
      },
      {
         "insert_order": 46,
         "priority": "HIGH",
         "source": "shard-started ([foo_2][1], node[tMTocMvQQgGCkj7QDHl3OA], [P], s[INITIALIZING]), reason [after recovery from shard_store]",
         "executing" : false,
         "time_in_queue_millis": 842,
         "time_in_queue": "842ms"
      },
      {
         "insert_order": 45,
         "priority": "HIGH",
         "source": "shard-started ([foo_2][0], node[tMTocMvQQgGCkj7QDHl3OA], [P], s[INITIALIZING]), reason [after recovery from shard_store]",
         "executing" : false,
         "time_in_queue_millis": 858,
         "time_in_queue": "858ms"
      }
  ]
}
```
