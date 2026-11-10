<!-- Converted from ml/anomaly-detection/apis/forecast.asciidoc (AsciiDoc). Includes are inlined. -->

# Forecast jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Predicts the future behavior of a time series by using its historical behavior. 

## Request

`POST _ml/anomaly_detectors/<job_id>/_forecast`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

You can create a forecast job based on an anomaly detection job to extrapolate future 
behavior. Refer to
{ml-docs}/ml-ad-forecast.html[Forecasting the future]
and 
{ml-docs}/ml-limitations.html#ml-forecast-limitations[Forecast limitations] to 
learn more.

You can delete a forecast by using the 
Delete forecast API.

===============================

* Forecasts are not supported for jobs that perform population analysis; an
error occurs if you try to create a forecast for a job that has an
`over_field_name` property in its configuration.
* The job must be open when you create a forecast. Otherwise, an error occurs.
===============================

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`duration`::
  (Optional, time units) A period of time that indicates how far 
  into the future to forecast. For example, `30d` corresponds to 30 days. The 
  default value is 1 day. The forecast starts at the last record that was 
  processed.

`expires_in`::
  (Optional, time units) The period of time that forecast 
  results are retained. After a forecast expires, the results are deleted. The 
  default value is 14 days. If set to a value of `0`, the forecast is never 
  automatically deleted.

`max_model_memory`::
  (Optional, byte value) The maximum memory the forecast can use.
  If the forecast needs to use more than the provided amount, it will spool to
  disk. Default is 20mb, maximum is 500mb and minimum is 1mb. If set to 40% or
  more of the job's configured memory limit, it is automatically reduced to
  below that amount.

## Request body

You can also specify the query parameters (such as `duration` and
`expires_in`) in the request body.

## Examples

```console
POST _ml/anomaly_detectors/low_request_rate/_forecast
{
  "duration": "10d"
}
```

When the forecast is created, you receive the following results:
```js
{
  "acknowledged": true,
  "forecast_id": "wkCWa2IB2lF8nSE_TzZo"
}
```

You can subsequently see the forecast in the *Single Metric Viewer* in Kibana.
