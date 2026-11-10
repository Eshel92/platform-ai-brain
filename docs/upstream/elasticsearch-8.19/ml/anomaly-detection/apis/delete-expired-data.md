<!-- Converted from ml/anomaly-detection/apis/delete-expired-data.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete expired data API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes expired and unused machine learning data.

## Request

`DELETE _ml/_delete_expired_data` +

`DELETE _ml/_delete_expired_data/<job_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

Deletes all job results, model snapshots and forecast data that have exceeded
their `retention days` period. Machine learning state documents that are not
associated with any job are also deleted.

You can limit the request to a single or set of anomaly detection jobs by using a job 
identifier, a group name, a comma-separated list of jobs, or a wildcard 
expression. You can delete expired data for all anomaly detection jobs by using `_all`, 
by specifying `*` as the `<job_id>`, or by omitting the `<job_id>`.

## Path parameters

`<job_id>`::
(Optional, string)
Identifier for an anomaly detection job. It can be a job identifier, a group name, or a
wildcard expression.

## Query parameters

`requests_per_second`::
(Optional, float) The desired requests per second for the deletion processes.
The default behavior is no throttling.

`timeout`::
(Optional, string) How long can the underlying delete processes run until they are canceled.
The default value is `8h` (8 hours).

## Request body

You can also specify the query parameters (`requests_per_second` and
`timeout`) in the request body.

## Examples

```console
DELETE _ml/_delete_expired_data?timeout=1h
```

When the expired data is deleted, you receive the following response:

```console-result
{
  "deleted": true
}
```
