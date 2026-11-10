<!-- Converted from cluster/tasks.asciidoc (AsciiDoc). Includes are inlined. -->

### Task management API

beta::["The task management API is new and should still be considered a beta feature. The API may change in ways that are not backwards compatible.",https://github.com/elastic/elasticsearch/issues/51628]

**New API reference**
For the most up-to-date API details, refer to [task management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-tasks).

Returns information about the tasks currently executing in the cluster.

#### Request

`GET /_tasks/<task_id>`

`GET /_tasks`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The task management API returns information
about tasks currently executing
on one or more nodes in the cluster.

#### Path parameters

`<task_id>`::
(Optional, string) ID of the task to return
(`node_id:task_number`).

#### Query parameters

`actions`::
(Optional, string)
Comma-separated list or wildcard expression
of actions used to limit the request.

Omit this parameter to return all actions.
`detailed`::
(Optional, Boolean)
If `true`,
the response includes detailed information about shard recoveries.
Defaults to `false`.
`group_by`::
(Optional, string)
Key used to group tasks in the response.

Possible values are:

`nodes`::
(Default)
Node ID

`parents`::
Parent task ID

`none`::
Do not group tasks.
`nodes`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.
`parent_task_id`::
(Optional, string)
Parent task ID
used to limit returned information.

To return all tasks,
omit this parameter
or use a value of `-1`.
`timeout`::
(Optional, time units)
Period to wait for each node to respond. If a node does not respond before its
timeout expires, the response does not include its information. However, timed out
nodes are included in the response's `node_failures` property. Defaults to `30s`.

`wait_for_completion`::
(Optional, Boolean) If `true`, the request blocks until all found tasks are complete.
Defaults to `false`.

#### Response codes

`404` (Missing resources)::
If `<task_id>` is specified but not found, this code indicates that there
are no resources that match the request.

#### Examples

```console
GET _tasks <1>
GET _tasks?nodes=nodeId1,nodeId2 <2>
GET _tasks?nodes=nodeId1,nodeId2&actions=cluster:* <3>
```

<1> Retrieves all tasks currently running on all nodes in the cluster.
<2> Retrieves all tasks running on nodes `nodeId1` and `nodeId2`. See cluster-nodes for more info about how to select individual nodes.
<3> Retrieves all cluster-related tasks running on nodes `nodeId1` and `nodeId2`.

The API returns the following result:

```console-result
{
  "nodes" : {
    "oTUltX4IQMOUUVeiohTt8A" : {
      "name" : "H5dfFeA",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1:9300",
      "tasks" : {
        "oTUltX4IQMOUUVeiohTt8A:124" : {
          "node" : "oTUltX4IQMOUUVeiohTt8A",
          "id" : 124,
          "type" : "direct",
          "action" : "cluster:monitor/tasks/lists[n]",
          "start_time_in_millis" : 1458585884904,
          "running_time_in_nanos" : 47402,
          "cancellable" : false,
          "parent_task_id" : "oTUltX4IQMOUUVeiohTt8A:123"
        },
        "oTUltX4IQMOUUVeiohTt8A:123" : {
          "node" : "oTUltX4IQMOUUVeiohTt8A",
          "id" : 123,
          "type" : "transport",
          "action" : "cluster:monitor/tasks/lists",
          "start_time_in_millis" : 1458585884904,
          "running_time_in_nanos" : 236042,
          "cancellable" : false
        }
      }
    }
  }
}
```

##### Retrieve information from a particular task

It is also possible to retrieve information for a particular task. The following
example retrieves information about task `oTUltX4IQMOUUVeiohTt8A:124`:

```console
GET _tasks/oTUltX4IQMOUUVeiohTt8A:124
```

If the task isn't found, the API returns a 404.

To retrieve all children of a particular task:

```console
GET _tasks?parent_task_id=oTUltX4IQMOUUVeiohTt8A:123
```

If the parent isn't found, the API does not return a 404.

##### Get more information about tasks

You can also use the `detailed` request parameter to get more information about
the running tasks. This is useful to distinguish tasks from each other but
is more costly to execute. For example, fetching all searches using the `detailed`
request parameter:

```console
GET _tasks?actions=*search&detailed
```

The API returns the following result:

```console-result
{
  "nodes" : {
    "oTUltX4IQMOUUVeiohTt8A" : {
      "name" : "H5dfFeA",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1:9300",
      "tasks" : {
        "oTUltX4IQMOUUVeiohTt8A:464" : {
          "node" : "oTUltX4IQMOUUVeiohTt8A",
          "id" : 464,
          "type" : "transport",
          "action" : "indices:data/read/search",
          "description" : "indices[test], types[test], search_type[QUERY_THEN_FETCH], source[{\"query\":...}]",
          "start_time_in_millis" : 1483478610008,
          "running_time_in_nanos" : 13991383,
          "cancellable" : true,
          "cancelled" : false
        }
      }
    }
  }
}
```

The new `description` field contains human readable text that identifies the
particular request that the task is performing such as identifying the search
request being performed by a search task like the example above. Other kinds of
tasks have different descriptions, like `_reindex` which
has the source and the destination, or `_bulk` which just has the
number of requests and the destination indices. Many requests will only have an
empty description because more detailed information about the request is not
easily available or particularly helpful in identifying the request.

==============================

`_tasks` requests with `detailed` may also return a `status`. This is a report
of the internal status of the task. As such its format varies from task to task.
While we try to keep the `status` for a particular task consistent from version
to version this isn't always possible because we sometimes change the
implementation. In that case we might remove fields from the `status` for a
particular request so any parsing you do of the status might break in minor
releases.

==============================

##### Wait for completion

The task API can also be used to wait for completion of a particular task. The
following call will block for 10 seconds or until the task with id
`oTUltX4IQMOUUVeiohTt8A:12345` is completed.

```console
GET _tasks/oTUltX4IQMOUUVeiohTt8A:12345?wait_for_completion=true&timeout=10s
```

You can also wait for all tasks for certain action types to finish. This command
will wait for all `reindex` tasks to finish:

```console
GET _tasks?actions=*reindex&wait_for_completion=true&timeout=10s
```

##### Task Cancellation

If a long-running task supports cancellation, it can be cancelled with the cancel
tasks API. The following example cancels task `oTUltX4IQMOUUVeiohTt8A:12345`:

```console
POST _tasks/oTUltX4IQMOUUVeiohTt8A:12345/_cancel
```

The task cancellation command supports the same task selection parameters as the
list tasks command, so multiple tasks can be cancelled at the same time. For
example, the following command will cancel all reindex tasks running on the
nodes `nodeId1` and `nodeId2`.

```console
POST _tasks/_cancel?nodes=nodeId1,nodeId2&actions=*reindex
```

A task may continue to run for some time after it has been cancelled because it
may not be able to safely stop its current activity straight away, or because
Elasticsearch must complete its work on other tasks before it can process the
cancellation. The list tasks API will continue to list these cancelled tasks
until they complete. The `cancelled` flag in the response to the list tasks API
indicates that the cancellation command has been processed and the task will
stop as soon as possible. To troubleshoot why a cancelled task does not
complete promptly, use the list tasks API with the `?detailed` parameter to
identify the other tasks the system is running and also use the
cluster-nodes-hot-threads API to obtain detailed information about the work
the system is doing instead of completing the cancelled task.

##### Task Grouping

The task lists returned by task API commands can be grouped either by nodes
(default) or by parent tasks using the `group_by` parameter. The following
command will change the grouping to parent tasks:

```console
GET _tasks?group_by=parents
```

The grouping can be disabled by specifying `none` as a `group_by` parameter:

```console
GET _tasks?group_by=none
```

##### Identifying running tasks

The `X-Opaque-Id` header, when provided on the HTTP request header, is going to
be returned as a header in the response as well as in the `headers` field for in
the task information. This allows to track certain calls, or associate certain
tasks with the client that started them:

```sh
curl -i -H "X-Opaque-Id: 123456" "http://localhost:9200/_tasks?group_by=parents"
```

The API returns the following result:

```js
HTTP/1.1 200 OK
X-Opaque-Id: 123456 <1>
content-type: application/json; charset=UTF-8
content-length: 831

{
  "tasks" : {
    "u5lcZHqcQhu-rUoFaqDphA:45" : {
      "node" : "u5lcZHqcQhu-rUoFaqDphA",
      "id" : 45,
      "type" : "transport",
      "action" : "cluster:monitor/tasks/lists",
      "start_time_in_millis" : 1513823752749,
      "running_time_in_nanos" : 293139,
      "cancellable" : false,
      "headers" : {
        "X-Opaque-Id" : "123456" <2>
      },
      "children" : [
        {
          "node" : "u5lcZHqcQhu-rUoFaqDphA",
          "id" : 46,
          "type" : "direct",
          "action" : "cluster:monitor/tasks/lists[n]",
          "start_time_in_millis" : 1513823752750,
          "running_time_in_nanos" : 92133,
          "cancellable" : false,
          "parent_task_id" : "u5lcZHqcQhu-rUoFaqDphA:45",
          "headers" : {
            "X-Opaque-Id" : "123456" <3>
          }
        }
      ]
    }
  }
}
```
<1> id as a part of the response header
<2> id for the tasks that was initiated by the REST request
<3> the child task of the task initiated by the REST request
