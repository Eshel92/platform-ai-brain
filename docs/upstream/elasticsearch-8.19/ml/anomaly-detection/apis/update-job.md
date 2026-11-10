<!-- Converted from ml/anomaly-detection/apis/update-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Update anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Updates certain properties of an anomaly detection job.

## Request

`POST _ml/anomaly_detectors/<job_id>/_update`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Request body

The following properties can be updated after the job is created:

`allow_lazy_open`::
(Boolean)
Advanced configuration option. Specifies whether this job can open when there is
insufficient machine learning node capacity for it to be immediately assigned to a node. The
default value is `false`; if a machine learning node with capacity to run the job cannot
immediately be found, the open anomaly detection jobs API returns an
error. However, this is also subject to the cluster-wide
`xpack.ml.max_lazy_ml_nodes` setting; see advanced-ml-settings. If this
option is set to `true`, the open anomaly detection jobs API does not
return an error and the job waits in the `opening` state until sufficient machine learning
node capacity is available.
**Note:** If the job is open when you make the update, you must stop the datafeed,
close the job, then reopen the job and restart the datafeed for the changes to take effect.

[[update-analysislimits]]`analysis_limits`::
(Optional, object)
Limits can be applied for the resources required to hold the mathematical models
in memory. These limits are approximate and can be set per job. They do not
control the memory used by other processes, for example the Elasticsearch Java processes.
You can update the `analysis_limits` only while the job is closed.
**Properties of `analysis_limits`**
`model_memory_limit`:::
(long or string)
The approximate maximum amount of memory resources that are required for
analytical processing. Once this limit is approached, data pruning becomes
more aggressive. Upon exceeding this limit, new entities are not modeled. The
default value for jobs created in version 6.1 and later is `1024mb`. If the
`xpack.ml.max_model_memory_limit` setting has a value greater than `0` and less
than `1024mb`, however, that value is used instead. If
`xpack.ml.max_model_memory_limit` is not set, but
`xpack.ml.use_auto_machine_memory_percent` is set, then the default
`model_memory_limit` will be set to the largest size that could be assigned in
the cluster, capped at `1024mb`. The default value is relatively small to
ensure that high resource usage is a conscious decision. If you have jobs that
are expected to analyze high cardinality fields, you will likely need to use a
higher value.
**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently.
If you specify a number instead of a string, the units are assumed to be MiB.
Specifying a string is recommended for clarity. If you specify a byte size unit
of `b` or `kb` and the number does not equate to a discrete number of megabytes,
it is rounded down to the closest MiB. The minimum valid value is 1 MiB. If you
specify a value less than 1 MiB, an error occurs. For more information about
supported byte size units, see byte-units.
If you specify a value for the `xpack.ml.max_model_memory_limit` setting, an
error occurs when you try to create jobs that have `model_memory_limit` values
greater than that setting value. For more information, see ml-settings.
=======
* You cannot decrease the `model_memory_limit` value below the current usage. To
determine the current usage, refer to the `model_bytes` value in
the get job stats API.
* If the `memory_status` property in the
`model_size_stats` object has a value of
`hard_limit`, this means that it was unable to process some data. You might want
to re-run the job with an increased `model_memory_limit`.
=======

**Note:**

`background_persist_interval`::
(time units)
Advanced configuration option. The time between each periodic persistence of the
model. The default value is a randomized value between 3 to 4 hours, which
avoids all jobs persisting at exactly the same time. The smallest allowed value
is 1 hour.
**Tip:** For very large models (several GB), persistence could take 10-20 minutes,
so do not set the `background_persist_interval` value too low.

**Note:** If the job is open when you make the update, you must stop the datafeed,
close the job, then reopen the job and restart the datafeed for the changes to take effect.

[[update-customsettings]]`custom_settings`::
(object)
Advanced configuration option. Contains custom metadata about the job. For
example, it can contain custom URL information as shown in
{ml-docs}/ml-configuring-url.html[Adding custom URLs to machine learning results].
`daily_model_snapshot_retention_after_days`::
(long)
Advanced configuration option, which affects the automatic removal of old model
snapshots for this job. It specifies a period of time (in days) after which only
the first snapshot per day is retained. This period is relative to the timestamp
of the most recent snapshot for this job. Valid values range from `0` to
`model_snapshot_retention_days`. For new jobs, the default value is `1`. For
jobs created before version 7.8.0, the default value matches
`model_snapshot_retention_days`. For more information, refer to
{ml-docs}/ml-ad-run-jobs.html#ml-ad-model-snapshots[Model snapshots].
**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently.
`description`::
(string) A description of the job.

`detectors`::
(array) An array of detector update objects.
**Properties of `detectors`**

`custom_rules`:::
(array)
An array of custom rule objects, which enable you to customize the way detectors
operate. For example, a rule may dictate to the detector conditions under which
results should be skipped. Kibana refers to custom rules as _job rules_. For more
examples, see
{ml-docs}/ml-configuring-detector-custom-rules.html[Customizing detectors with custom rules].
**Properties of `custom_rules`**
=====

`actions`:::
(array)
The set of actions to be triggered when the rule applies. If
more than one action is specified the effects of all actions are combined. The
available actions include:

* `skip_result`: The result will not be created. This is the default value.
Unless you also specify `skip_model_update`, the model will be updated as usual
with the corresponding series value.
* `skip_model_update`: The value for that series will not be used to update the
model. Unless you also specify `skip_result`, the results will be created as
usual. This action is suitable when certain values are expected to be
consistently anomalous and they affect the model in a way that negatively
impacts the rest of the results.
* `force_time_shift`: This action will shift the time inside the anomaly detector by a specified
amount. This is useful, e.g. to quickly adapt to the daylight saving time events that
are known beforehand. This action requires a `force_time_shift` parameter
in the `params` object.
`params`:::
(object)
A set of parameter objects that customize the actions defined in the custom rules
actions array. The available parameters (depending on the specified actions) include:
`force_time_shift`.
**Properties of `params`**
=======
`force_time_shift`::::
(object)
Set `time_shift_amount` to the signed number of seconds by which you want to shift the time.
=======

`conditions`:::
(array)
An optional array of numeric conditions when the rule applies. A rule must
either have a non-empty scope or at least one condition. Multiple conditions are
combined together with a logical `AND`. A condition has the following
properties:
**Properties of `conditions`**
======

`applies_to`::::
(string)
Specifies the result property to which the condition applies. The available
options are `actual`, `typical`, `diff_from_typical`, `time`. If your detector
uses `lat_long`, `metric`, `rare`, or `freq_rare` functions, you can only
specify conditions that apply to `time`.
`operator`::::
(string)
Specifies the condition operator. The available options are `gt` (greater than),
`gte` (greater than or equals), `lt` (less than) and `lte` (less than or
equals).
`value`::::
(double)
The value that is compared against the `applies_to` field using the `operator`.
======

`scope`:::
(object)
An optional scope of series where the rule applies. A rule must either
have a non-empty scope or at least one condition. By default, the scope includes
all series. Scoping is allowed for any of the fields that are also specified in
`by_field_name`, `over_field_name`, or `partition_field_name`. To add a scope
for a field, add the field name as a key in the scope object and set its value
to an object with the following properties:
**Properties of `scope`**
======
`filter_id`::::
(string)
The id of the filter to be used.
`filter_type`::::
(string)
Either `include` (the rule applies for values in the filter) or `exclude` (the
rule applies for values not in the filter). Defaults to `include`.
======
=====

`description`:::
(string)
A description of the detector. For example, `Low event rate`.
`detector_index`:::
(integer)
A unique identifier for the detector. This identifier is based on the order of
the detectors in the `analysis_config`, starting at zero.
If you want to update a specific detector, you must use this identifier. You
cannot, however, change the `detector_index` value for a detector.

`groups`::
(array of strings)
A list of job groups. A job can belong to no groups or many.
`model_plot_config`::
(object)
This advanced configuration option stores model information along with the
results. It provides a more detailed view into anomaly detection.
**Warning:** If you enable model plot it can add considerable overhead to the
performance of the system; it is not feasible for jobs with many entities.

Model plot provides a simplified and indicative view of the model and its
bounds. It does not display complex features such as multivariate correlations
or multimodal data. As such, anomalies may occasionally be reported which cannot
be seen in the model plot.

Model plot config can be configured when the job is created or updated later. It
must be disabled if performance issues are experienced.
**Properties of `model_plot_config`**
`annotations_enabled`:::
(Boolean)
If true, enables calculation and storage of the model change annotations
for each entity that is being analyzed. Defaults to `enabled`.
`enabled`:::
(Boolean)
If true, enables calculation and storage of the model bounds for each entity
that is being analyzed. By default, this is not enabled.
`terms`:::
experimental[] (string)
Limits data collection to this comma separated list of partition or by field
values. If terms are not specified or it is an empty string, no filtering is
applied. For example, "CPU,NetworkIn,DiskWrites". Wildcards are not supported.
Only the specified `terms` can be viewed when using the Single Metric Viewer.

`model_prune_window`::
(time units)
Advanced configuration option.
Affects the pruning of models that have not been updated for the given time
duration. The value must be set to a multiple of the `bucket_span`. If set too
low, important information may be removed from the model. Typically, set to
`30d` or longer. If not set, model pruning only occurs if the model memory
status reaches the soft limit or the hard limit. For jobs created in 8.1 and
later, the default value is the greater of `30d` or 20 times `bucket_span`.
`model_snapshot_retention_days`::
(long)
Advanced configuration option, which affects the automatic removal of old model
snapshots for this job. It specifies the maximum period of time (in days) that
snapshots are retained. This period is relative to the timestamp of the most
recent snapshot for this job. The default value is `10`, which means snapshots
ten days older than the newest snapshot are deleted. For more information, refer
to {ml-docs}/ml-ad-run-jobs.html#ml-ad-model-snapshots[Model snapshots].
`per_partition_categorization`:::
(object)
Settings related to how categorization interacts with partition fields.
**Properties of `per_partition_categorization`**
`enabled`:::
(Boolean)
To enable this setting, you must also set the partition_field_name property to
the same value in every detector that uses the keyword mlcategory. Otherwise,
job creation fails.
`stop_on_warn`:::
(Boolean)
This setting can be set to true only if per-partition categorization is enabled.
If true, both categorization and subsequent anomaly detection stops for
partitions where the categorization status changes to `warn`. This setting makes
it viable to have a job where it is expected that categorization works well for
some partitions but not others; you do not pay the cost of bad categorization
forever in the partitions where it works badly.

`renormalization_window_days`::
(long)
Advanced configuration option. The period over which adjustments to the score
are applied, as new data is seen. The default value is the longer of 30 days or
100 `bucket_spans`.
**Note:** If the job is open when you make the update, you must stop the datafeed,
close the job, then reopen the job and restart the datafeed for the changes to take effect.

`results_retention_days`::
(long)
Advanced configuration option. The period of time (in days) that results are
retained. Age is calculated relative to the timestamp of the latest bucket
result. If this property has a non-null value, once per day at 00:30 (server
time), results that are the specified number of days older than the latest
bucket result are deleted from Elasticsearch. The default value is null, which means all
results are retained. Annotations generated by the system also count as results
for retention purposes; they are deleted after the same number of days as
results. Annotations added by users are retained forever.

## Examples

```console
POST _ml/anomaly_detectors/low_request_rate/_update
{
  "description":"An updated job",
  "detectors": {
    "detector_index": 0,
    "description": "An updated detector description"
  },
  "groups": ["kibana_sample_data","kibana_sample_web_logs"],
  "model_plot_config": {
    "enabled": true
  },
  "renormalization_window_days": 30,
  "background_persist_interval": "2h",
  "model_snapshot_retention_days": 7,
  "results_retention_days": 60
}
```

When the anomaly detection job is updated, you receive a summary of the job
configuration information, including the updated property values. For example:

```js
{
  "job_id" : "low_request_rate",
  "job_type" : "anomaly_detector",
  "job_version" : "8.4.0",
  "create_time" : 1656105950893,
  "finished_time" : 1656105965744,
  "model_snapshot_id" : "1656105964",
  "custom_settings" : {
    "created_by" : "ml-module-sample",
    "custom_urls" : [
      {
        "url_name" : "Raw data",
        "url_value" : "discover#/?_g=(time:(from:'$earliest$',mode:absolute,to:'$latest$'))&_a=(index:'90943e30-9a47-11e8-b64d-95841ca0b247')"
      },
      {
        "url_name" : "Data dashboard",
        "url_value" : "dashboards#/view/edf84fe0-e1a0-11e7-b6d5-4dc382ef7f5b?_g=(time:(from:'$earliest$',mode:absolute,to:'$latest$'))&_a=(filters:!(),query:(language:kuery,query:''))"
      }
    ]
  },
  "groups" : [
    "kibana_sample_data",
    "kibana_sample_web_logs"
  ],
  "description" : "An updated job",
  "analysis_config" : {
    "bucket_span" : "1h",
    "summary_count_field_name" : "doc_count",
    "detectors" : [
      {
        "detector_description" : "An updated detector description",
        "function" : "low_count",
        "detector_index" : 0
      }
    ],
    "influencers" : [ ],
    "model_prune_window" : "30d"
  },
  "analysis_limits" : {
    "model_memory_limit" : "11mb",
    "categorization_examples_limit" : 4
  },
  "data_description" : {
    "time_field" : "timestamp",
    "time_format" : "epoch_ms"
  },
  "model_plot_config" : {
    "enabled" : true,
    "annotations_enabled" : true
  },
  "renormalization_window_days" : 30,
  "background_persist_interval" : "2h",
  "model_snapshot_retention_days" : 7,
  "daily_model_snapshot_retention_after_days" : 1,
  "results_retention_days" : 60,
  "results_index_name" : "custom-low_request_rate",
  "allow_lazy_open" : false
}
```
