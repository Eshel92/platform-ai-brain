<!-- Converted from cluster/nodes-info.asciidoc (AsciiDoc). Includes are inlined. -->

### Nodes info API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns cluster nodes information.

#### Request

`GET /_nodes` +

`GET /_nodes/<node_id>` +

`GET /_nodes/<metric>` +

`GET /_nodes/<node_id>/<metric>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

The cluster nodes info API allows to retrieve one or more (or all) of
the cluster nodes information. All the nodes selective options are explained
here.

By default, it returns all attributes and core settings for a node.

#### Path parameters

`<metric>`::
(Optional, string)
Limits the information returned to the specific metrics. Supports a
comma-separated list, such as `http,ingest`.
**Valid values for `<metric>`**
`aggregations`::
Information about the available types of aggregation.

`http`::
Information about the HTTP interface of this node.

`indices`::
Node-level configuration related to indexing:

* `total_indexing_buffer`: the maximum size of the indexing buffer on this node.

`ingest`::
Information about ingest pipelines and processors.

`jvm`::
JVM information, including its name, its version, and its configuration.

`os`::
Operating system information, including its name and version.

`plugins`::
Details about the installed plugins and modules per node. The following
information is available for each plugin and module:

* `name`: plugin name
* `version`: version of Elasticsearch the plugin was built for
* `description`: short description of the plugin's purpose
* `classname`: fully-qualified class name of the plugin's entry point
* `has_native_controller`: whether or not the plugin has a native controller
process

`process`::
Process information, including the numeric process ID.

`settings`::
Lists all node settings in use as defined in the `elasticsearch.yml` file.

`thread_pool`::
Information about the configuration of each thread pool.

`transport`::
Information about the transport interface of the node.

If you use the full `GET /_nodes/<node_id>/<metric>` form of this API then you
can also request the metric `_all` to retrieve all metrics, or you can request
the metric `_none` to suppress all metrics and retrieve only the identity of
the node.

`<node_id>`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.

#### Response body

`build_hash`::
		Short hash of the last git commit in this release.

`host`::
		The node's host name.

`ip`::
		The node's IP address.

`name`::
		The node's name.

`total_indexing_buffer`::
		Total heap allowed to be used to hold recently indexed
		documents before they must be written to disk. This size is
		a shared pool across all shards on this node, and is
    controlled by Indexing Buffer settings.

`total_indexing_buffer_in_bytes`::
		Same as `total_indexing_buffer`, but expressed in bytes.

`transport_address`::
		Host and port where transport HTTP connections are accepted.

`version`::
		Elasticsearch version running on this node.

`transport_version`::
		The most recent transport version that this node can communicate with.

`index_version`::
		The most recent index version that this node can read.

`component_versions`::
		The version numbers of individual components loaded in this node.

The `os` flag can be set to retrieve information that concern the operating
system:

`os.refresh_interval_in_millis`::
		Refresh interval for the OS statistics

`os.name`::
		Name of the operating system (ex: Linux, Windows, Mac OS X)

`os.arch`::
		Name of the JVM architecture (ex: amd64, x86)

`os.version`::
		Version of the operating system

`os.available_processors`::
		Number of processors available to the Java virtual machine

`os.allocated_processors`::
	  The number of processors actually used to calculate thread pool size. This
		number can be set with the `node.processors`
		setting of a node and defaults to the number of processors reported by
		the OS.

The `process` flag can be set to retrieve information that concern the current
running process:

`process.refresh_interval_in_millis`::
		Refresh interval for the process statistics

`process.id`::
		Process identifier (PID)

`process.mlockall`::
		Indicates if the process address space has been successfully locked in memory

#### Query parameters

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`timeout`::
(Optional, time units)
Period to wait for each node to respond. If a node does not respond before its
timeout expires, the response does not include its information. However, timed out
nodes are included in the response's `_nodes.failed` property. Defaults to no
timeout.

#### Examples

```console
# return just process
GET /_nodes/process

# same as above
GET /_nodes/_all/process

# return just jvm and process of only nodeId1 and nodeId2
GET /_nodes/nodeId1,nodeId2/jvm,process

# same as above
GET /_nodes/nodeId1,nodeId2/info/jvm,process

# return all the information of only nodeId1 and nodeId2
GET /_nodes/nodeId1,nodeId2/_all
```

The `_all` flag can be set to return all the information - or you can omit it.

##### Example for plugins metric

If `plugins` is specified, the result will contain details about the installed
plugins and modules:

```console
GET /_nodes/plugins
```

The API returns the following response:

```console-result
{
  "_nodes": ...
  "cluster_name": "elasticsearch",
  "nodes": {
    "USpTGYaBSIKbgSUJR2Z9lg": {
      "name": "node-0",
      "transport_address": "192.168.17:9300",
      "host": "node-0.elastic.co",
      "ip": "192.168.17",
      "version": "{version}",
      "transport_version": 100000298,
      "index_version": 100000074,
      "component_versions": {
        "ml_config_version": 100000162,
        "transform_config_version": 100000096
      },
      "build_flavor": "default",
      "build_type": "{build_type}",
      "build_hash": "587409e",
      "roles": [
        "master",
        "data",
        "ingest"
      ],
      "attributes": {},
      "plugins": [
        {
          "name": "analysis-icu",
          "version": "{version}",
          "description": "The ICU Analysis plugin integrates Lucene ICU module into elasticsearch, adding ICU relates analysis components.",
          "classname": "org.elasticsearch.plugin.analysis.icu.AnalysisICUPlugin",
          "has_native_controller": false
        }
      ],
      "modules": [
        {
          "name": "lang-painless",
          "version": "{version}",
          "description": "An easy, safe and fast scripting language for Elasticsearch",
          "classname": "org.elasticsearch.painless.PainlessPlugin",
          "has_native_controller": false
        }
      ]
    }
  }
}
```

##### Example for ingest metric

If `ingest` is specified, the response contains details about the available
processors per node:

```console
GET /_nodes/ingest
```

The API returns the following response:

```console-result
{
  "_nodes": ...
  "cluster_name": "elasticsearch",
  "nodes": {
    "USpTGYaBSIKbgSUJR2Z9lg": {
      "name": "node-0",
      "transport_address": "192.168.17:9300",
      "host": "node-0.elastic.co",
      "ip": "192.168.17",
      "version": "{version}",
      "transport_version": 100000298,
      "index_version": 100000074,
      "component_versions": {
        "ml_config_version": 100000162,
        "transform_config_version": 100000096
      },
      "build_flavor": "default",
      "build_type": "{build_type}",
      "build_hash": "587409e",
      "roles": [],
      "attributes": {},
      "ingest": {
        "processors": [
          {
            "type": "date"
          },
          {
            "type": "uppercase"
          },
          {
            "type": "set"
          },
          {
            "type": "lowercase"
          },
          {
            "type": "gsub"
          },
          {
            "type": "convert"
          },
          {
            "type": "remove"
          },
          {
            "type": "fail"
          },
          {
            "type": "foreach"
          },
          {
            "type": "split"
          },
          {
            "type": "trim"
          },
          {
            "type": "rename"
          },
          {
            "type": "join"
          },
          {
            "type": "append"
          }
        ]
      }
    }
  }
}
```
