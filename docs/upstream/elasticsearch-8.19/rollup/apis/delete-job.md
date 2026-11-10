<!-- Converted from rollup/apis/delete-job.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete {rollup-jobs} API

deprecated::[8.11.0,"Rollups will be removed in a future version. Use downsampling instead."]

**New API reference**
For the most up-to-date API details, refer to [Rollup APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-rollup).

Deletes an existing {rollup-job}.

#### Request

`DELETE _rollup/job/<job_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage` or
`manage_rollup` cluster privileges to use this API. For more information, see
security-privileges.

#### Description

A job must be *stopped* first before it can be deleted. If you attempt to delete
a started job, an error occurs. Similarly, if you attempt to delete a
nonexistent job, an exception occurs.

===============================
When a job is deleted, that only removes the process that is actively monitoring
and rolling up data. It does not delete any previously rolled up data. This is
by design; a user may wish to roll up a static dataset. Because the dataset is
static, once it has been fully rolled up there is no need to keep the indexing
rollup job around (as there will be no new data). So the job can be deleted,
leaving behind the rolled up data for analysis.

If you wish to also remove the rollup data, and the rollup index only contains
the data for a single job, you can simply delete the whole rollup index. If the
rollup index stores data from several jobs, you must issue a delete-by-query
that targets the rollup job's ID in the rollup index.

```js
POST my_rollup_index/_delete_by_query
{
  "query": {
    "term": {
      "_rollup.id": "the_rollup_job_id"
    }
  }
}
```
===============================

#### Path parameters

`<job_id>`::
  (Required, string) Identifier for the job.

#### Response codes

`404` (Missing resources)::
  This code indicates that there are no resources that match the request. It
  occurs if you try to delete a job that doesn't exist.

#### {api-example-title}

If we have a rollup job named `sensor`, it can be deleted with:

```console
DELETE _rollup/job/sensor
```

Which will return the response:

```console-result
{
  "acknowledged": true
}
```
