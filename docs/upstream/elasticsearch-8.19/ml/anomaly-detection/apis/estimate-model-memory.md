<!-- Converted from ml/anomaly-detection/apis/estimate-model-memory.asciidoc (AsciiDoc). Includes are inlined. -->

# Estimate anomaly detection jobs model memory API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Makes an estimation of the memory usage for an anomaly detection job model. It is based 
on analysis configuration details for the job and cardinality estimates for the 
fields it references.

## Request

`POST _ml/anomaly_detectors/_estimate_model_memory`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Request body

`analysis_config`::
(Required, object) 
For a list of the properties that you can specify in the `analysis_config` 
component of the body of this API, see `analysis_config`.

`max_bucket_cardinality`::
(Required^\*^, object)
Estimates of the highest cardinality in a single bucket that is observed for 
influencer fields over the time period that the job analyzes data. To produce a 
good answer, values must be provided for all influencer fields. Providing values 
for fields that are not listed as `influencers` has no effect on the estimation. +
^*^It can be omitted from the request if there are no `influencers`.

`overall_cardinality`::
(Required^\*^, object) 
Estimates of the cardinality that is observed for fields over the whole time 
period that the job analyzes data. To produce a good answer, values must be 
provided for fields referenced in the `by_field_name`, `over_field_name` and 
`partition_field_name` of any detectors. Providing values for other fields has 
no effect on the estimation. +
^*^It can be omitted from the request if no detectors have a `by_field_name`, 
`over_field_name` or `partition_field_name`.

## Examples

```console
POST _ml/anomaly_detectors/_estimate_model_memory
{
  "analysis_config": {
    "bucket_span": "5m",
    "detectors": [
      {
        "function": "sum",
        "field_name": "bytes",
        "by_field_name": "status",
        "partition_field_name": "app"
      }
    ],
    "influencers": [ "source_ip", "dest_ip" ]
  },
  "overall_cardinality": {
    "status": 10,
    "app": 50
  },
  "max_bucket_cardinality": {
    "source_ip": 300,
    "dest_ip": 30
  }
}
```

The estimate returns the following result:

```console-result
{
  "model_memory_estimate": "21mb"
}
```
