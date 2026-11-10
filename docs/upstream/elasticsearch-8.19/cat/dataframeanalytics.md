<!-- Converted from cat/dataframeanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

### cat {dfanalytics} API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the 
get data frame analytics jobs statistics API.

Returns configuration and usage information about {dfanalytics-jobs}.

#### Request

`GET /_cat/ml/data_frame/analytics/<data_frame_analytics_id>` +

`GET /_cat/ml/data_frame/analytics`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the following 
privileges:

* cluster: `monitor_ml`
  
For more information, see security-privileges and {ml-docs-setup-privileges}.

#### Path parameters

`<data_frame_analytics_id>`::
(Optional, string) 
Identifier for the {dfanalytics-job}. If you do not specify this option, the API
returns information for the first hundred {dfanalytics-jobs}.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default
columns. If you explicitly specify one or more columns, it returns only the
specified columns.
Valid columns are:

`assignment_explanation`, `ae`:::
Contains messages relating to the selection of a node.
`create_time`, `ct`, `createTime`:::
(Default)
The time when the {dfanalytics-job} was created.

`description`, `d`:::
A description of the job.
`dest_index`, `di`, `destIndex`:::
Name of the destination index.

`failure_reason`, `fr`, `failureReason`:::
Contains messages about the reason why a {dfanalytics-job} failed.

`id`:::
(Default)
Identifier for the {dfanalytics-job}.
`model_memory_limit`, `mml`, `modelMemoryLimit`:::
The approximate maximum amount of memory resources that are permitted for the 
{dfanalytics-job}.

`node.address`, `na`, `nodeAddress`:::
The network address of the node that the {dfanalytics-job} is assigned to.

`node.ephemeral_id`, `ne`, `nodeEphemeralId`:::
The ephemeral ID of the node that the {dfanalytics-job} is assigned to.

`node.id`, `ni`, `nodeId`:::
The unique identifier of the node that the {dfanalytics-job} is assigned to.

`node.name`, `nn`, `nodeName`:::
The name of the node that the {dfanalytics-job} is assigned to.

`progress`, `p`:::
The progress report of the {dfanalytics-job} by phase.

`source_index`, `si`, `sourceIndex`:::
Name of the source index.

`state`, `s`:::
(Default)
Current state of the {dfanalytics-job}.

`type`, `t`:::
(Default)
The type of analysis that the {dfanalytics-job} performs.

`version`, `v`:::
The Elasticsearch version number in which the {dfanalytics-job} was created.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
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

```console
GET _cat/ml/data_frame/analytics?v=true
```

```console-result
id               create_time              type             state
classifier_job_1 2020-02-12T11:49:09.594Z classification stopped
classifier_job_2 2020-02-12T11:49:14.479Z classification stopped
classifier_job_3 2020-02-12T11:49:16.928Z classification stopped
classifier_job_4 2020-02-12T11:49:19.127Z classification stopped
classifier_job_5 2020-02-12T11:49:21.349Z classification stopped
```
