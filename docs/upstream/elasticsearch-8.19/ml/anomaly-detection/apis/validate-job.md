<!-- Converted from ml/anomaly-detection/apis/validate-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Validate anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Validates anomaly detection job configuration information.

## Request

`POST _ml/anomaly_detectors/_validate`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API enables you to validate the anomaly detection job configuration before you
create the job.

## Request body

For a list of the properties that you can specify in the body of this API,
see ml-put-job-request-body.

## Examples

```console
POST _ml/anomaly_detectors/_validate
{
  "description": "Unusual response times by airlines",
  "analysis_config": {
    "bucket_span": "300S",
    "detectors": [
      {
        "function": "metric",
        "field_name": "responsetime",
        "by_field_name": "airline" } ],
    "influencers": [ "airline" ]
  },
  "data_description": {
    "time_field": "time",
    "time_format": "yyyy-MM-dd'T'HH:mm:ssX"
  }
}
```

When the validation is complete, you receive the following results:

```console-result
{
  "acknowledged": true
}
```
