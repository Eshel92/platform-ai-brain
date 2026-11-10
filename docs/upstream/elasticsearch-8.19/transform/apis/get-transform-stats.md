<!-- Converted from transform/apis/get-transform-stats.asciidoc (AsciiDoc). Includes are inlined. -->

# Get transform statistics API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Retrieves usage information for transforms.

## Request

`GET _transform/<transform_id>/_stats`

`GET _transform/<transform_id>,<transform_id>/_stats` +

`GET _transform/_stats` +

`GET _transform/_all/_stats` +

`GET _transform/*/_stats` +

## Prerequisites

Requires the following privileges:

* cluster: `monitor_transform` (the `transform_user` built-in role grants this 
  privilege)
* destination index: `read`, `view_index_metadata`.

## Description

You can get statistics for multiple transforms in a single API
request by using a comma-separated list of identifiers or a wildcard expression.
You can get statistics for all transforms by using `_all`, by
specifying `*` as the `<transform_id>`, or by omitting the
`<transform_id>`.

## Path parameters

`<transform_id>`::
(Optional, string)
Identifier for the transform. It can be a transform identifier or a wildcard
expression. If you do not specify one of these options, the API returns
information for all transforms.

## Query parameters

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
`from`::
(Optional, integer)
Skips the specified number of transforms. The default value is `0`.
`size`::
(Optional, integer)
Specifies the maximum number of transforms to obtain. The default value is
`100`.

## Response body

The API returns an array of statistics objects for transforms, which are
sorted by the `id` value in ascending order. All of these properties are
informational; you cannot update their values.

`checkpointing`::
(object) Contains statistics about checkpoints.
**Properties of `checkpointing`**
`changes_last_detected_at`:::
(date)
The timestamp when changes were last detected in the source indices.
`last`:::
(object) Contains statistics about the last completed checkpoint. 
**Properties of `last`**
=====
`checkpoint`::::
(integer) The sequence number for the checkpoint.
`time_upper_bound_millis`::::
(date) When using time-based synchronization, this timestamp indicates the
upper bound of data that is included in the checkpoint.
`timestamp_millis`::::
(date) The timestamp of the checkpoint, which indicates when the checkpoint
was created.
=====

`last_search_time`:::
(date)
The timestamp of the last search in the source indices. This field is only
shown if the transform is running.
`next`:::
(object) Contains statistics about the next checkpoint that is currently in
progress. This object appears only when the transform `state` is `indexing`.
**Properties of `next`**
=====
`checkpoint`::::
(integer) The sequence number for the checkpoint.

`checkpoint_progress`::::
(object) Contains statistics about the progress of the checkpoint. For example,
it lists the `total_docs`, `docs_remaining`, `percent_complete`,
`docs_processed`, and `docs_indexed`. This information is available only for
batch transforms and the first checkpoint of {ctransforms}.

`time_upper_bound_millis`::::
(date) When using time-based synchronization, this timestamp indicates the
upper bound of data that is included in the checkpoint.

`timestamp_millis`::::
(date) The timestamp of the checkpoint, which indicates when the checkpoint was
created.
=====

`operations_behind`:::
(integer) The number of operations that have occurred on the source index but
have not been applied to the destination index yet. A high number can indicate
that the transform is failing to keep up. 

`health`::
(object) Health indicator for this transform.
**Properties of `health`**
`status`::
    (string) Health status of this transform. Statuses are:

   * `green`:
      The transform is healthy.

    * `unknown`:
      The health of the transform could not be determined.

    * `yellow`:
      The functionality of the transform is in a degraded state and may need 
      remediation to avoid the health becoming `red`.

    * `red`:
      The transform is experiencing an outage or is unavailable for use.

`issues`::
    (Optional, array) If a non-healthy status is returned, contains a list of issues
    of the transform.
**Properties of `issues`**
========
`issue`::
    (string) A description of the issue.

`details`::
    (Optional, string) Details about the issue.

`count`::
    (integer) Number of times the issue has occured since it started.

`first_occurrence`::
    (Optional, date) The timestamp this issue occured for the first time.
========

`id`::
(string)
Identifier for the transform.
`node`::
(object) For started transforms only, the node upon which the transform is
started.
**Properties of `node`**
`attributes`:::
(object) A list of attributes for the node.

`ephemeral_id`:::
(string) The node ephemeral ID.

`id`:::
(string) The unique identifier of the node. For example, "0-o0tOoRTwKFZifatTWKNw".

`name`:::
(string) The node name. For example, `0-o0tOo`.

`transport_address`:::
(string) The host and port where transport HTTP connections are accepted. For
example, `127.0.0.1:9300`.

`reason`::
(string)
If a transform has a `failed` state, this property provides details about the
reason for the failure.
`state`::
(string)
The status of the transform, which can be one of the following values:
* `aborting`: The transform is aborting.
* `failed`: The transform failed. For more information about the failure,
check the reason field.
* `indexing`: The transform is actively processing data and creating new
documents.
* `started`: The transform is running but not actively indexing data.
* `stopped`: The transform is stopped.
* `stopping`: The transform is stopping.
`stats`::
(object) An object that provides statistical information about the transform.
**Properties of `stats`**

`delete_time_in_ms`:::
(long)
The amount of time spent deleting, in milliseconds.
`documents_deleted`:::
(long)
The number of documents that have been deleted from the destination index due to
the retention policy for this transform.
`documents_indexed`:::
(long)
The number of documents that have been indexed into the destination index
for the transform.
`documents_processed`:::
(long)
The number of documents that have been processed from the source index of
the transform.
`exponential_avg_checkpoint_duration_ms`:::
(double)
Exponential moving average of the duration of the checkpoint, in milliseconds.
`exponential_avg_documents_indexed`:::
(double)
Exponential moving average of the number of new documents that have been
indexed.
`exponential_avg_documents_processed`:::
(double)
Exponential moving average of the number of documents that have been
processed.
`index_failures`:::
(long)
The number of indexing failures.
`index_time_in_ms`:::
(long)
The amount of time spent indexing, in milliseconds.
`index_total`:::
(long)
The number of index operations.
`pages_processed`:::
(long)
The number of search or bulk index operations processed. Documents are
processed in batches instead of individually.
`processing_time_in_ms`:::
(long)
The amount of time spent processing results, in milliseconds.
`processing_total`:::
(long)
The number of processing operations.
`search_failures`:::
(long)
The number of search failures.
`search_time_in_ms`:::
(long)
The amount of time spent searching, in milliseconds.
`search_total`:::
(long)
The number of search operations on the source index for the transform.
`trigger_count`:::
(long)
The number of times the transform has been triggered by the scheduler. For
example, the scheduler triggers the transform indexer to check for updates
or ingest new data at an interval specified in the
`frequency` property.
  

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request. 

## Examples

The following example skips for the first five transforms and
gets usage information for a maximum of ten results: 

```console
GET _transform/_stats?from=5&size=10
```

The following example gets usage information for the transform:

```console
GET _transform/ecommerce-customer-transform/_stats
```

The API returns the following results:

```console-result
{
  "count" : 1,
  "transforms" : [
    {
      "id" : "ecommerce-customer-transform",
      "state" : "started",
      "node" : {
        "id" : "cpTIGMsVQ8Gqwqlxxxxxxx",
        "name" : "my.home",
        "ephemeral_id" : "5-L21nFsQxxxxxxxxxx-xx",
        "transport_address" : "127.0.0.1:9300",
        "attributes" : { }
      },
      "stats" : {
        "pages_processed" : 78,
        "documents_processed" : 6027,
        "documents_indexed" : 68,
        "documents_deleted": 22,
        "delete_time_in_ms": 214,
        "trigger_count" : 168,
        "index_time_in_ms" : 412,
        "index_total" : 20,
        "index_failures" : 0,
        "search_time_in_ms" : 353,
        "search_total" : 78,
        "search_failures" : 0,
        "processing_time_in_ms" : 8,
        "processing_total" : 78,
        "exponential_avg_checkpoint_duration_ms" : 97.30637923893185,
        "exponential_avg_documents_indexed" : 2.2064915040974062,
        "exponential_avg_documents_processed" : 179.89419945785045
      },
      "checkpointing" : {
        "last" : {
          "checkpoint" : 20,
          "timestamp_millis" : 1585344558220,
          "time_upper_bound_millis" : 1585344498220
        },
        "changes_last_detected_at" : 1585344558219
      },
      "health": {
        "status": "green"
      }
    }
  ]
}
```
