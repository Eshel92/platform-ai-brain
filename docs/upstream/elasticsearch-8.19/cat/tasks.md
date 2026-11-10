<!-- Converted from cat/tasks.asciidoc (AsciiDoc). Includes are inlined. -->

### cat task management API

beta::["The cat task management API is new and should still be considered a beta feature. The API may change in ways that are not backwards compatible.",https://github.com/elastic/elasticsearch/issues/51628]

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the task management API.

Returns information about tasks currently executing in the cluster,
similar to the task management API.

#### Request

`GET /_cat/tasks`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The cat task management API returns information
about tasks currently executing
on one or more nodes in the cluster.
It is a more compact view
of the JSON task management API.

#### Query parameters

`detailed`::
(Optional, Boolean)
If `true`,
the response includes detailed information about shard recoveries.
Defaults to `false`.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`nodes`::
(Optional, string)
Comma-separated list of node IDs or names used to limit the response. Supports
wildcard (`*`) expressions.

`parent_task_id`::
(Optional, string)
Parent task ID used to limit the response.

`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Response codes

`404` (Missing resources)::
If `<task_id>` is specified but not found, this code indicates that there
are no resources that match the request.

#### Examples

```console
GET _cat/tasks?v=true
```

The API returns the following response:

```console-result
action                         task_id                    parent_task_id             type      start_time    timestamp running_time ip             node
cluster:monitor/tasks/lists[n] oTUltX4IQMOUUVeiohTt8A:124 oTUltX4IQMOUUVeiohTt8A:123 direct    1458585884904 01:48:24  44.1micros   127.0.0.1:9300 oTUltX4IQMOUUVeiohTt8A
cluster:monitor/tasks/lists    oTUltX4IQMOUUVeiohTt8A:123 -                          transport 1458585884904 01:48:24  186.2micros  127.0.0.1:9300 oTUltX4IQMOUUVeiohTt8A
```
