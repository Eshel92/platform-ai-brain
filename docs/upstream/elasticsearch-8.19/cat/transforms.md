<!-- Converted from cat/transforms.asciidoc (AsciiDoc). Includes are inlined. -->

### cat transforms API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the get transforms API.

Returns configuration and usage information about transforms.

#### Request

`GET /_cat/transforms/<transform_id>` +

`GET /_cat/transforms/_all` +

`GET /_cat/transforms/*` +

`GET /_cat/transforms`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `monitor_transform`
cluster privileges to use this API. The built-in `transform_user` role has these
privileges. For more information, see security-privileges and
built-in-roles.

#### Path parameters

`<transform_id>`::
(Optional, string)
Identifier for the transform. It can be a transform identifier or a wildcard
expression. If you do not specify one of these options, the API returns
information for all transforms.

#### Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no transforms that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `transforms` array when
there are no matches and the subset of results when there are partial matches.

If this parameter is `false`, the request returns a `404` status code when there
are no matches or only partial matches.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`from`::
(Optional, integer)
Skips the specified number of transforms. The default value is `0`.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default
columns. If you explicitly specify one or more columns, it returns only the
specified columns.
Valid columns are:

`changes_last_detection_time`, `cldt`:::
(Default)
The timestamp when changes were last detected in the source indices.
`checkpoint`, `cp`:::
(Default)
The sequence number for the checkpoint.

`checkpoint_duration_time_exp_avg`, `cdtea`, `checkpointTimeExpAvg`:::
Exponential moving average of the duration of the checkpoint, in milliseconds.
`checkpoint_progress`, `c`, `checkpointProgress`:::
(Default)
The progress of the next checkpoint that is currently in progress.

`create_time`, `ct`, `createTime`:::
The time the transform was created.

`delete_time`, `dtime`:::
The amount of time spent deleting, in milliseconds.
`description`, `d`:::
The description of the transform.

`dest_index`, `di`, `destIndex`:::
The _destination index_ for the transform.

In the case of a `pivot` transform, the mappings of the destination
index are deduced based on the source fields when possible. If alternate
mappings are required, use the Create index API
prior to starting the transform.

In the case of a `latest` transform, the mappings are never deduced. If dynamic
mappings for the destination index are undesirable, use the
Create index API prior to starting the transform.
`documents_deleted`, `docd`:::
The number of documents that have been deleted from the destination index due to
the retention policy for this transform.
`documents_indexed`, `doci`:::
The number of documents that have been indexed into the destination index
for the transform.
`docs_per_second`, `dps`:::
Specifies a limit on the number of input documents per second. This setting
throttles the transform by adding a wait time between search requests. The
default value is `null`, which disables throttling.
`documents_processed`, `docp`:::
(Default)
The number of documents that have been processed from the source index of
the transform.
`frequency`, `f`:::
The interval between checks for changes in the source indices when the
transform is running continuously. The minimum value is `1s` and the maximum
is `1h`. The default value is `1m`.
`id`:::
(Default)
Identifier for the transform.
`index_failure`, `if`:::
The number of indexing failures.
`index_time`, `itime`:::
The amount of time spent indexing, in milliseconds.
`index_total`, `it`:::
The number of index operations.
`indexed_documents_exp_avg`, `idea`:::
Exponential moving average of the number of new documents that have been
indexed.
`last_search_time`, `lst`, `lastSearchTime`:::
(Default)
The timestamp of the last search in the source indices. This field is only
shown if the transform is running.
`max_page_search_size`, `mpsz`:::
Defines the initial page size to use for the composite aggregation for each
checkpoint. If circuit breaker exceptions occur, the page size is dynamically
adjusted to a lower value. The minimum value is `10` and the maximum is `65,536`.
The default value is `500`.
`pages_processed`, `pp`:::
The number of search or bulk index operations processed. Documents are
processed in batches instead of individually.
`pipeline`, `p`:::
The unique identifier for an ingest pipeline.
`processed_documents_exp_avg`, `pdea`:::
Exponential moving average of the number of documents that have been
processed.
`processing_time`, `pt`:::
The amount of time spent processing results, in milliseconds.
`reason`, `r`:::
If a transform has a `failed` state, this property provides details about the
reason for the failure.
`search_failure`, `sf`:::
The number of search failures.
`search_time`, `stime`:::
The amount of time spent searching, in milliseconds.
`search_total`, `st`:::
The number of search operations on the source index for the transform.
`source_index`, `si`, `sourceIndex`:::
(Default)
The _source indices_ for the transform. It can be a single index, an index
pattern (for example, `"my-index-*"`), an array of indices (for example,
`["my-index-000001", "my-index-000002"]`), or an array of index patterns (for
example, `["my-index-*", "my-other-index-*"]`. For remote indices use the syntax
`"remote_name:index_name"`.
**Note:** If any indices are in remote clusters then the master node and at least
one transform node must have the `remote_cluster_client` node role.
`state`, `s`:::
(Default)
The status of the transform, which can be one of the following values:
* `aborting`: The transform is aborting.
* `failed`: The transform failed. For more information about the failure,
check the reason field.
* `indexing`: The transform is actively processing data and creating new
documents.
* `started`: The transform is running but not actively indexing data.
* `stopped`: The transform is stopped.
* `stopping`: The transform is stopping.
`transform_type`, `tt`:::
Indicates the type of transform: `batch` or `continuous`.

`trigger_count`, `tc`:::
The number of times the transform has been triggered by the scheduler. For
example, the scheduler triggers the transform indexer to check for updates
or ingest new data at an interval specified in the
`frequency` property.
`version`, `v`:::
The version of Elasticsearch that existed on the node when the transform was
created.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`size`::
(Optional, integer)
Specifies the maximum number of transforms to obtain. The default value is
`100`.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET /_cat/transforms?v=true&format=json
```

```console-result
[
  {
    "id" : "ecommerce_transform",
    "state" : "started",
    "checkpoint" : "1",
    "documents_processed" : "705",
    "checkpoint_progress" : "100.00",
    "changes_last_detection_time" : null
  }
]
```
