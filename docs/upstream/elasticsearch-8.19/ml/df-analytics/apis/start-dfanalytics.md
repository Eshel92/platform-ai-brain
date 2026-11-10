<!-- Converted from ml/df-analytics/apis/start-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Start {dfanalytics-jobs} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Starts a {dfanalytics-job}.

## Request

`POST _ml/data_frame/analytics/<data_frame_analytics_id>/_start`

## Prerequisites

Requires the following privileges:

* cluster: `manage_ml` (the `machine_learning_admin` built-in role grants this 
  privilege)
* source indices: `read`, `view_index_metadata`
* destination index: `read`, `create_index`, `manage` and `index`

## Description

A {dfanalytics-job} can be started and stopped multiple times throughout its 
lifecycle.

If the destination index does not exist, it is created automatically the first
time you start the {dfanalytics-job}. The `index.number_of_shards` and
`index.number_of_replicas` settings for the destination index are copied from
the source index. If there are multiple source indices, the destination index
copies the highest setting values. The mappings for the destination index are
also copied from the source indices. If there are any mapping conflicts, the job
fails to start.

If the destination index exists, it is used as is. You can therefore set up the
destination index in advance with custom settings and mappings.

**Important:** When Elasticsearch security features are enabled, the {dfanalytics-job}
remembers which user created it and runs the job using those credentials. If you 
provided secondary authorization headers
when you created the job, those credentials are used.

## Path parameters

`<data_frame_analytics_id>`::
(Required, string)
Identifier for the {dfanalytics-job}. This identifier can contain lowercase
alphanumeric characters (a-z and 0-9), hyphens, and underscores. It must start
and end with alphanumeric characters.

## Query parameters

`timeout`::
(Optional, time units) 
Controls the amount of time to wait until the {dfanalytics-job} starts. Defaults
to 20 seconds.

## Response body

`acknowledged`::
  (Boolean) For a successful response, this value is always `true`. On failure, an
  exception is returned instead.

`node`::
  (string) The ID of the node that the job was started on.
  If the job is allowed to open lazily and has not yet been assigned to a node, this value is an empty string.

## Examples

The following example starts the `loganalytics` {dfanalytics-job}:

```console
POST _ml/data_frame/analytics/loganalytics/_start
```

When the {dfanalytics-job} starts, you receive the following results:

```console-result
{
  "acknowledged" : true,
  "node" : "node-1"
}
```
