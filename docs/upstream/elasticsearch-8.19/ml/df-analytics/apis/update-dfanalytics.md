<!-- Converted from ml/df-analytics/apis/update-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Update {dfanalytics-jobs} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Updates an existing {dfanalytics-job}.

## Request

`POST _ml/data_frame/analytics/<data_frame_analytics_id>/_update`

## Prerequisites

Requires the following privileges:

* cluster: `manage_ml` (the `machine_learning_admin` built-in role grants this 
  privilege)
* source indices: `read`, `view_index_metadata`
* destination index: `read`, `create_index`, `manage` and `index`

**Note:** The {dfanalytics-job} remembers which roles the user who updated it had at
the time of the update. When you start the job, it performs the analysis using
those same roles. If you provide
secondary authorization headers, 
those credentials are used instead.

## Description

This API updates an existing {dfanalytics-job} that performs an analysis on the source
indices and stores the outcome in a destination index.

## Path parameters

`<data_frame_analytics_id>`::
(Required, string)
Identifier for the {dfanalytics-job}. This identifier can contain lowercase
alphanumeric characters (a-z and 0-9), hyphens, and underscores. It must start
and end with alphanumeric characters.

## Request body

`allow_lazy_start`::
(Optional, Boolean) 
Specifies whether this job can start when there is insufficient machine learning node 
capacity for it to be immediately assigned to a node. The default is `false`; if
a machine learning node with capacity to run the job cannot immediately be found, the API
returns an error. However, this is also subject to the cluster-wide
`xpack.ml.max_lazy_ml_nodes` setting. See advanced-ml-settings. If this
option is set to `true`, the API does not return an error and the job waits in
the `starting` state until sufficient machine learning node capacity is available.

`description`::
(Optional, string)
A description of the job.
`max_num_threads`::
(Optional, integer)
The maximum number of threads to be used by the analysis.
The default value is `1`. Using more threads may decrease the time
necessary to complete the analysis at the cost of using more CPU.
Note that the process may use additional threads for operational
functionality other than the analysis itself.

`_meta`::
(Optional, object)
Advanced configuration option. Contains custom metadata about the job. For
example, it can contain custom URL information.
`model_memory_limit`::
(Optional, string)
The approximate maximum amount of memory resources that are permitted for
analytical processing. The default value for {dfanalytics-jobs} is `1gb`. If
you specify a value for the `xpack.ml.max_model_memory_limit` setting, an error
occurs when you try to create jobs that have `model_memory_limit` values greater
than that setting value. For more information, see
ml-settings.

## Examples

### Updating model memory limit example

The following example shows how to update the model memory limit for the existing {dfanalytics} configuration.

```console
POST _ml/data_frame/analytics/loganalytics/_update
{
  "model_memory_limit": "200mb"
}
```

When the job is updated, the response contains its configuration with
the updated values. For example:

```console-result
{
  "id" : "loganalytics",
  "create_time" : 1656364565517,
  "version" : "8.4.0",
  "authorization" : {
    "roles" : [
      "superuser"
    ]
  },
  "description" : "Outlier detection on log data",
  "source" : {
    "index" : [
      "logdata"
    ],
    "query" : {
      "match_all" : { }
    }
  },
  "dest" : {
    "index" : "logdata_out",
    "results_field" : "ml"
  },
  "analysis" : {
    "outlier_detection" : {
      "compute_feature_influence" : true,
      "outlier_fraction" : 0.05,
      "standardization_enabled" : true
    }
  },
  "model_memory_limit" : "200mb",
  "allow_lazy_start" : false,
  "max_num_threads" : 1
}
```
