<!-- Converted from ml/anomaly-detection/apis/delete-forecast.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete forecasts API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes forecasts from a machine learning job.

## Request

`DELETE _ml/anomaly_detectors/<job_id>/_forecast` +

`DELETE _ml/anomaly_detectors/<job_id>/_forecast/<forecast_id>` +

`DELETE _ml/anomaly_detectors/<job_id>/_forecast/_all`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

By default, forecasts are retained for 14 days. You can specify a different
retention period with the `expires_in` parameter in the
forecast jobs API. The delete forecast API enables you to delete
one or more forecasts before they expire.

**Note:** When you delete a job, its associated forecasts are deleted.

For more information, see
{ml-docs}/ml-ad-forecast.html[Forecasting the future].

## Path parameters

`<forecast_id>`::
(Optional, string) A comma-separated list of forecast identifiers. If you do not
specify this optional parameter or if you specify `_all` or `*` the API deletes all
forecasts from the job.

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`allow_no_forecasts`::
  (Optional, Boolean) Specifies whether an error occurs when there are no
  forecasts. In particular, if this parameter is set to `false` and there are no
  forecasts associated with the job, attempts to delete all forecasts return an
  error. The default value is `true`.

`timeout`::
  (Optional, time units) Specifies the period of time to wait
  for the completion of the delete operation. When this period of time elapses,
  the API fails and returns an error. The default value is `30s`.

## Examples

```console
DELETE _ml/anomaly_detectors/total-requests/_forecast/_all
```

If the request does not encounter errors, you receive the following result:

```js
{
  "acknowledged": true
}
```
