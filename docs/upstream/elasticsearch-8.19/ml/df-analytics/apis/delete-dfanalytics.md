<!-- Converted from ml/df-analytics/apis/delete-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete {dfanalytics-jobs} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Deletes an existing {dfanalytics-job}.

## Request

`DELETE _ml/data_frame/analytics/<data_frame_analytics_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Path parameters

`<data_frame_analytics_id>`::
(Required, string)
Identifier for the {dfanalytics-job}.

## Query parameters

`force`::
  (Optional, Boolean) If `true`, it deletes a job that is not stopped; this method is
  quicker than stopping and deleting the job.

`timeout`::
  (Optional, time units) The time to wait for the job to be deleted.
  Defaults to 1 minute.

## Examples

The following example deletes the `loganalytics` {dfanalytics-job}:

```console
DELETE _ml/data_frame/analytics/loganalytics
```

The API returns the following result:

```console-result
{
  "acknowledged" : true
}
```
