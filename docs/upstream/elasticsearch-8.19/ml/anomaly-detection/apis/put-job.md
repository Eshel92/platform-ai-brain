<!-- Converted from ml/anomaly-detection/apis/put-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Create anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Instantiates an anomaly detection job.

## Request

`PUT _ml/anomaly_detectors/<job_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

If you include a `datafeed_config`, you must also have `read` index privileges
on the source index.

## Description

**Important:**
* You must use Kibana or this API to create an anomaly detection job. Do not put
a job directly to the `.ml-config` index using the Elasticsearch index API. If Elasticsearch
security features are enabled, do not give users `write` privileges on the
`.ml-config` index.
* If you include a `datafeed_config` and Elasticsearch security features are enabled,
your datafeed remembers which roles the user who created it had at the time of
creation and runs the query using those same roles. If you provide
secondary authorization headers, those
credentials are used instead.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job. This identifier can contain lowercase
alphanumeric characters (a-z and 0-9), hyphens, and underscores. It must start
and end with alphanumeric characters.

## Request body

`allow_lazy_open`::
(Optional, Boolean)
Advanced configuration option. Specifies whether this job can open when there is
insufficient machine learning node capacity for it to be immediately assigned to a node. The
default value is `false`; if a machine learning node with capacity to run the job cannot
immediately be found, the open anomaly detection jobs API returns an
error. However, this is also subject to the cluster-wide
`xpack.ml.max_lazy_ml_nodes` setting; see advanced-ml-settings. If this
option is set to `true`, the open anomaly detection jobs API does not
return an error and the job waits in the `opening` state until sufficient machine learning
node capacity is available.
[[put-analysisconfig]]`analysis_config`::
(Required, object)
The analysis configuration, which specifies how to analyze the data. After you
create a job, you cannot change the analysis configuration; all the properties
are informational.
**Properties of `analysis_config`**
`bucket_span`:::
(time units)
The size of the interval that the analysis is aggregated into, typically between
`5m` and `1h`. This value should be either a whole number of days or equate to a
whole number of buckets in one day;
deprecated:[8.1, Values that do not meet these recommendations are deprecated and will be disallowed in a future version].
If the anomaly detection job uses a datafeed with
{ml-docs}/ml-configuring-aggregation.html[aggregations], this value must also be
divisible by the interval of the date histogram aggregation. The default value
is `5m`. For more information, see
{ml-docs}/ml-ad-run-jobs.html#ml-ad-bucket-span[Bucket span].
`categorization_analyzer`:::
(object or string)
If `categorization_field_name` is specified, you can also define the analyzer
that is used to interpret the categorization field. This property cannot be used
at the same time as `categorization_filters`. The categorization analyzer
specifies how the `categorization_field` is interpreted by the categorization
process. The syntax is very similar to that used to define the `analyzer` in the
Analyze endpoint. For more information, see
{ml-docs}/ml-configuring-categories.html[Categorizing log messages].
The `categorization_analyzer` field can be specified either as a string or as an
object. If it is a string it must refer to a
built-in analyzer or one added by another plugin. If it
is an object it has the following properties:
**Properties of `categorization_analyzer`**
=====
`char_filter`::::
(array of strings or objects)
One or more character filters. In addition to the
built-in character filters, other plugins can provide more character filters.
This property is optional. If it is not specified, no character filters are
applied prior to categorization. If you are customizing some other aspect of the
analyzer and you need to achieve the equivalent of `categorization_filters`
(which are not permitted when some other aspect of the analyzer is customized),
add them here as
pattern replace character filters.
`tokenizer`::::
(string or object)
The name or definition of the tokenizer to use after
character filters are applied. This property is compulsory if
`categorization_analyzer` is specified as an object. Machine learning provides
a tokenizer called `ml_standard` that tokenizes in a way that has been
determined to produce good categorization results on a variety of log
file formats for logs in English. If you want to use that tokenizer but
change the character or token filters, specify `"tokenizer": "ml_standard"`
in your `categorization_analyzer`. Additionally, the `ml_classic` tokenizer
is available, which tokenizes in the same way as the non-customizable
tokenizer in old versions of the product (before 6.2). `ml_classic` was
the default categorization tokenizer in versions 6.2 to 7.13, so if you
need categorization identical to the default for jobs created in these
versions, specify `"tokenizer": "ml_classic"` in your `categorization_analyzer`.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently.
`filter`::::
(array of strings or objects)
One or more token filters. In addition to the built-in
token filters, other plugins can provide more token filters. This property is
optional. If it is not specified, no token filters are applied prior to
categorization.
=====
`categorization_field_name`:::
(string)
If this property is specified, the values of the specified field will be
categorized. The resulting categories must be used in a detector by setting
`by_field_name`, `over_field_name`, or `partition_field_name` to the keyword
`mlcategory`. For more information, see
{ml-docs}/ml-configuring-categories.html[Categorizing log messages].
`categorization_filters`:::
(array of strings)
If `categorization_field_name` is specified, you can also define optional
filters. This property expects an array of regular expressions. The expressions
are used to filter out matching sequences from the categorization field values.
You can use this functionality to fine tune the categorization by excluding
sequences from consideration when categories are defined. For example, you can
exclude SQL statements that appear in your log files. For more information, see
{ml-docs}/ml-configuring-categories.html[Categorizing log messages]. This
property cannot be used at the same time as `categorization_analyzer`. If you
only want to define simple regular expression filters that are applied prior to
tokenization, setting this property is the easiest method. If you also want to
customize the tokenizer or post-tokenization filtering, use the
`categorization_analyzer` property instead and include the filters as
`pattern_replace` character filters. The effect is exactly the same.
`detectors`:::
(array) An array of detector configuration objects. Detector configuration
objects specify which data fields a job analyzes. They also specify which
analytical functions are used. You can specify multiple detectors for a job.
**Note:** If the `detectors` array does not contain at least one detector,
no analysis can occur and an error is returned.
**Properties of `detectors`**
=====
`by_field_name`::::
(string)
The field used to split the data. In particular, this property is used for
analyzing the splits with respect to their own history. It is used for finding
unusual values in the context of the split.
[[put-customrules]]`custom_rules`::::
(array)
An array of custom rule objects, which enable you to customize the way detectors
operate. For example, a rule may dictate to the detector conditions under which
results should be skipped. Kibana refers to custom rules as _job rules_. For more
examples, see
{ml-docs}/ml-configuring-detector-custom-rules.html[Customizing detectors with custom rules].
**Properties of `custom_rules`**
======

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
=======
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
=======

`scope`:::
(object)
An optional scope of series where the rule applies. A rule must either
have a non-empty scope or at least one condition. By default, the scope includes
all series. Scoping is allowed for any of the fields that are also specified in
`by_field_name`, `over_field_name`, or `partition_field_name`. To add a scope
for a field, add the field name as a key in the scope object and set its value
to an object with the following properties:
**Properties of `scope`**
=======
`filter_id`::::
(string)
The id of the filter to be used.
`filter_type`::::
(string)
Either `include` (the rule applies for values in the filter) or `exclude` (the
rule applies for values not in the filter). Defaults to `include`.
=======
======

`detector_description`::::
(string)
A description of the detector. For example, `Low event rate`.
`detector_index`::::
(integer)
A unique identifier for the detector. This identifier is based on the order of
the detectors in the `analysis_config`, starting at zero.
If you specify a value for this property, it is ignored.

`exclude_frequent`::::
(string)
Contains one of the following values: `all`, `none`, `by`, or `over`. If set,
frequent entities are excluded from influencing the anomaly results. Entities
can be considered frequent over time or frequent in a population. If you are
working with both over and by fields, then you can set `exclude_frequent` to
`all` for both fields, or to `by` or `over` for those specific fields.
`field_name`::::
(string)
The field that the detector uses in the function. If you use an event rate
function such as `count` or `rare`, do not specify this field.
**Note:** The `field_name` cannot contain double quotes or backslashes.

`function`::::
(string)
The analysis function that is used. For example, `count`, `rare`, `mean`, `min`,
`max`, and `sum`. For more information, see
{ml-docs}/ml-functions.html[Function reference].
`over_field_name`::::
(string)
The field used to split the data. In particular, this property is used for
analyzing the splits with respect to the history of all splits. It is used for
finding unusual values in the population of all splits. For more information,
see {ml-docs}/ml-configuring-populations.html[Performing population analysis].
`partition_field_name`::::
(string)
The field used to segment the analysis. When you use this property, you have
completely independent baselines for each value of this field.
`use_null`::::
(Boolean)
Defines whether a new series is used as the null series when there is no value
for the by or partition fields. The default value is `false`.
=====

`influencers`:::
(array of strings)
A comma separated list of influencer field names. Typically these can be the by,
over, or partition fields that are used in the detector configuration. You might
also want to use a field name that is not specifically named in a detector, but
is available as part of the input data. When you use multiple detectors, the use
of influencers is recommended as it aggregates results for each influencer
entity.
`latency`:::
(time units)
The size of the window in which to expect data that is out of time order. The
default value is 0 (no latency). If you specify a non-zero value, it must be
greater than or equal to one second. For more information about time units, see
time-units.
**Note:** Latency is only applicable when you send data by using
the post data API.

`model_prune_window`:::
(Optional, time units)
Advanced configuration option.
Affects the pruning of models that have not been updated for the given time
duration. The value must be set to a multiple of the `bucket_span`. If set too
low, important information may be removed from the model. Typically, set to
`30d` or longer. If not set, model pruning only occurs if the model memory
status reaches the soft limit or the hard limit. For jobs created in 8.1 and
later, the default value is the greater of `30d` or 20 times `bucket_span`.
`multivariate_by_fields`:::
(Boolean)
This functionality is reserved for internal use. It is not supported for use in
customer environments and is not subject to the support SLA of official GA
features.
If set to `true`, the analysis will automatically find correlations between
metrics for a given `by` field value and report anomalies when those
correlations cease to hold. For example, suppose CPU and memory usage on host A
is usually highly correlated with the same metrics on host B. Perhaps this
correlation occurs because they are running a load-balanced application.
If you enable this property, then anomalies will be reported when, for example,
CPU usage on host A is high and the value of CPU usage on host B is low. That
is to say, you'll see an anomaly when the CPU of host A is unusual given
the CPU of host B.

**Note:** To use the `multivariate_by_fields` property, you must also specify
`by_field_name` in your detector.

`per_partition_categorization`:::
(Optional, object)
Settings related to how categorization interacts with partition fields.
**Properties of `per_partition_categorization`**
=====
`enabled`::::
(Boolean)
To enable this setting, you must also set the partition_field_name property to
the same value in every detector that uses the keyword mlcategory. Otherwise,
job creation fails.
`stop_on_warn`::::
(Boolean)
This setting can be set to true only if per-partition categorization is enabled.
If true, both categorization and subsequent anomaly detection stops for
partitions where the categorization status changes to `warn`. This setting makes
it viable to have a job where it is expected that categorization works well for
some partitions but not others; you do not pay the cost of bad categorization
forever in the partitions where it works badly.
=====

`summary_count_field_name`:::
(string)
If this property is specified, the data that is fed to the job is expected to be
pre-summarized. This property value is the name of the field that contains the
count of raw data points that have been summarized. The same
`summary_count_field_name` applies to all detectors in the job.
**Note:** The `summary_count_field_name` property cannot be used with the `metric`
function.

[[put-analysislimits]]`analysis_limits`::
(Optional, object)
Limits can be applied for the resources required to hold the mathematical models
in memory. These limits are approximate and can be set per job. They do not
control the memory used by other processes, for example the Elasticsearch Java processes.
**Properties of `analysis_limits`**
`categorization_examples_limit`:::
(long)
The maximum number of examples stored per category in memory and in the results
data store. The default value is 4. If you increase this value, more examples
are available, however it requires that you have more storage available. If you
set this value to `0`, no examples are stored.
**Note:** The `categorization_examples_limit` only applies to analysis that uses
categorization. For more information, see
{ml-docs}/ml-configuring-categories.html[Categorizing log messages].
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

`background_persist_interval`::
(Optional, time units)
Advanced configuration option. The time between each periodic persistence of the
model. The default value is a randomized value between 3 to 4 hours, which
avoids all jobs persisting at exactly the same time. The smallest allowed value
is 1 hour.
**Tip:** For very large models (several GB), persistence could take 10-20 minutes,
so do not set the `background_persist_interval` value too low.

[[put-customsettings]]`custom_settings`::
(Optional, object)
Advanced configuration option. Contains custom metadata about the job. For
example, it can contain custom URL information as shown in
{ml-docs}/ml-configuring-url.html[Adding custom URLs to machine learning results].
[[put-dailymodelsnapshotretentionafterdays]]`daily_model_snapshot_retention_after_days`::
(Optional, long)
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
[[put-datadescription]]`data_description`::
(Required, object)
The data description defines the format of the input data when you send data to
the job by using the post data API. Note that when using a
datafeed, only the `time_field` needs to be set, the rest of the properties are
automatically set. When data is received via the post data API,
it is not stored in Elasticsearch. Only the results for anomaly detection are retained.
**Properties of `data_description`**
`format`:::
  (string) Only `xcontent` format is supported at this time, and this is the
  default value.

`time_field`:::
  (string) The name of the field that contains the timestamp.
  The default value is `time`.

`time_format`:::
(string)
The time format, which can be `epoch`, `epoch_ms`, or a custom pattern. The
default value is `epoch`, which refers to UNIX or Epoch time (the number of
seconds since 1 Jan 1970). The value `epoch_ms` indicates that time is measured
in milliseconds since the epoch. The `epoch` and `epoch_ms` time formats accept
either integer or real values. +
**Note:** Custom patterns must conform to the Java `DateTimeFormatter` class.
When you use date-time formatting patterns, it is recommended that you provide
the full date, time and time zone. For example: `yyyy-MM-dd'T'HH:mm:ssX`.
If the pattern that you specify is not sufficient to produce a complete
timestamp, job creation fails.

[[put-datafeedconfig]]`datafeed_config`::
(Optional, object) The {ml-docs}/ml-dfeeds.html[datafeed], which retrieves data
from Elasticsearch for analysis by the job. You can associate only one datafeed with each
anomaly detection job.
**Properties of `datafeed`**
`aggregations`:::
(Optional, object)
If set, the datafeed performs aggregation searches. Support for aggregations is
limited and should be used only with low cardinality data. For more information,
see
{ml-docs}/ml-configuring-aggregation.html[Aggregating data for faster performance].
`chunking_config`:::
(Optional, object)
Datafeeds might be required to search over long time periods, for several
months or years. This search is split into time chunks in order to ensure the
load on Elasticsearch is managed. Chunking configuration controls how the size of these
time chunks are calculated and is an advanced configuration option.
**Properties of `chunking_config`**
=====
`mode`:::
(string)
There are three available modes:
* `auto`: The chunk size is dynamically calculated. This is the default and
recommended value when the datafeed does not use aggregations.
* `manual`: Chunking is applied according to the specified `time_span`. Use this
mode when the datafeed uses aggregations.
* `off`: No chunking is applied.
`time_span`:::
(time units)
The time span that each search will be querying. This setting is only applicable
when the mode is set to `manual`. For example: `3h`.
=====

`datafeed_id`:::
(Optional, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.
Defaults to the same ID as the anomaly detection job.

`delayed_data_check_config`:::
(Optional, object)
Specifies whether the datafeed checks for missing data and the size of the
window. For example: `{"enabled": true, "check_window": "1h"}`.
The datafeed can optionally search over indices that have already been read in
an effort to determine whether any data has subsequently been added to the
index. If missing data is found, it is a good indication that the `query_delay`
option is set too low and the data is being indexed after the datafeed has passed
that moment in time. See
{ml-docs}/ml-delayed-data-detection.html[Working with delayed data].
This check runs only on real-time datafeeds.
**Properties of `delayed_data_check_config`**
=====
`check_window`::
(time units)
The window of time that is searched for late data. This window of time ends with
the latest finalized bucket. It defaults to `null`, which causes an appropriate
`check_window` to be calculated when the real-time datafeed runs. In particular,
the default `check_window` span calculation is based on the maximum of `2h` or
`8 * bucket_span`.
`enabled`::
(Boolean)
Specifies whether the datafeed periodically checks for delayed data. Defaults to
`true`.
=====

`frequency`:::
(Optional, time units)
The interval at which scheduled queries are made while the datafeed runs in real
time. The default value is either the bucket span for short bucket spans, or,
for longer bucket spans, a sensible fraction of the bucket span. For example:
`150s`. When `frequency` is shorter than the bucket span, interim results for
the last (partial) bucket are written then eventually overwritten by the full
bucket results. If the datafeed uses aggregations, this value must be divisible
by the interval of the date histogram aggregation.
`indices`:::
(Required, array)
An array of index names. Wildcards are supported. For example:
`["it_ops_metrics", "server*"]`.
**Note:** If any indices are in remote clusters then the master nodes and the machine learning nodes need to have the
`remote_cluster_client` role.

`indices_options`:::
(Optional, object)
Specifies index expansion options that are used during search.
For example:
```
{
   "expand_wildcards": ["all"],
   "ignore_unavailable": true,
   "allow_no_indices": "false",
   "ignore_throttled": true
}
```
For more information about these options, see api-multi-index.
`max_empty_searches`:::
(Optional,integer)
If a real-time datafeed has never seen any data (including during any initial
training period) then it will automatically stop itself and close its associated
job after this many real-time searches that return no documents. In other words,
it will stop after `frequency` times `max_empty_searches` of real-time
operation. If not set then a datafeed with no end time that sees no data will
remain started until it is explicitly stopped. By default this setting is not
set.
`query`:::
(Optional, object)
The Elasticsearch query domain-specific language (DSL). This value corresponds to the
query object in an Elasticsearch search POST body. All the options that are supported by
Elasticsearch can be used, as this object is passed verbatim to Elasticsearch. By default, this
property has the following value: `{"match_all": {"boost": 1}}`.
`query_delay`:::
(Optional, time units)
The number of seconds behind real time that data is queried. For example, if
data from 10:04 a.m. might not be searchable in Elasticsearch until 10:06 a.m., set this
property to 120 seconds. The default value is randomly selected between `60s`
and `120s`. This randomness improves the query performance when there are
multiple jobs running on the same node. For more information, see
{ml-docs}/ml-delayed-data-detection.html[Handling delayed data].
`runtime_mappings`:::
(Optional, object)
Specifies runtime fields for the datafeed search.
For example:
```
{
  "day_of_week": {
    "type": "keyword",
    "script": {
      "source": "emit(doc['@timestamp'].value.dayOfWeekEnum.getDisplayName(TextStyle.FULL, Locale.ENGLISH))"
    }
  }
}
```

`script_fields`:::
(Optional, object)
Specifies scripts that evaluate custom expressions and returns script fields to
the datafeed. The detector configuration objects in a job can contain functions
that use these script fields. For more information, see
{ml-docs}/ml-configuring-transform.html[Transforming data with script fields]
and Script fields.
`scroll_size`:::
(Optional, unsigned integer)
The `size` parameter that is used in Elasticsearch searches when the datafeed does not use
aggregations. The default value is `1000`. The maximum value is the value of
`index.max_result_window` which is 10,000 by default.

`description`::
  (Optional, string) A description of the job.

`groups`::
(Optional, array of strings)
A list of job groups. A job can belong to no groups or many.
`model_plot_config`::
(Optional, object)
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

[[put-modelsnapshotretentiondays]]`model_snapshot_retention_days`::
(Optional, long)
Advanced configuration option, which affects the automatic removal of old model
snapshots for this job. It specifies the maximum period of time (in days) that
snapshots are retained. This period is relative to the timestamp of the most
recent snapshot for this job. The default value is `10`, which means snapshots
ten days older than the newest snapshot are deleted. For more information, refer
to {ml-docs}/ml-ad-run-jobs.html#ml-ad-model-snapshots[Model snapshots].
[[put-renormalizationwindowdays]]`renormalization_window_days`::
(Optional, long)
Advanced configuration option. The period over which adjustments to the score
are applied, as new data is seen. The default value is the longer of 30 days or
100 `bucket_spans`.
[[put-resultsindexname]]`results_index_name`::
(Optional, string)
A text string that affects the name of the machine learning results index. The default value
is `shared`, which generates an index named `.ml-anomalies-shared`.
[[put-resultsretentiondays]]`results_retention_days`::
(Optional, long)
Advanced configuration option. The period of time (in days) that results are
retained. Age is calculated relative to the timestamp of the latest bucket
result. If this property has a non-null value, once per day at 00:30 (server
time), results that are the specified number of days older than the latest
bucket result are deleted from Elasticsearch. The default value is null, which means all
results are retained. Annotations generated by the system also count as results
for retention purposes; they are deleted after the same number of days as
results. Annotations added by users are retained forever.

## Examples

Create an anomaly detection job and datafeed:

```console
PUT _ml/anomaly_detectors/test-job1?pretty
{
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "detector_description": "Sum of bytes",
        "function": "sum",
        "field_name": "bytes"
      }
    ]
  },
  "data_description": {
    "time_field": "timestamp",
    "time_format": "epoch_ms"
  },
  "analysis_limits": {
    "model_memory_limit": "11MB"
  },
  "model_plot_config": {
    "enabled": true,
    "annotations_enabled": true
  },
  "results_index_name": "test-job1",
  "datafeed_config":
  {
    "indices": [
    "kibana_sample_data_logs"
    ],
    "query": {
      "bool": {
        "must": [
          {
            "match_all": {}
          }
        ]
      }
    },
    "runtime_mappings": {
      "hour_of_day": {
        "type": "long",
        "script": {
          "source": "emit(doc['timestamp'].value.getHour());"
        }
      }
    },
    "datafeed_id": "datafeed-test-job1"
  }
}
```

The API returns the following results:

```js
{
  "job_id" : "test-job1",
  "job_type" : "anomaly_detector",
  "job_version" : "8.4.0",
  "create_time" : 1656087283340,
  "datafeed_config" : {
    "datafeed_id" : "datafeed-test-job1",
    "job_id" : "test-job1",
    "authorization" : {
      "roles" : [
        "superuser"
      ]
    },
    "query_delay" : "61499ms",
    "chunking_config" : {
      "mode" : "auto"
    },
    "indices_options" : {
      "expand_wildcards" : [
        "open"
      ],
      "ignore_unavailable" : false,
      "allow_no_indices" : true,
      "ignore_throttled" : true
    },
    "query" : {
      "bool" : {
        "must" : [
          {
            "match_all" : { }
          }
        ]
      }
    },
    "indices" : [
      "kibana_sample_data_logs"
    ],
    "scroll_size" : 1000,
    "delayed_data_check_config" : {
      "enabled" : true
    },
    "runtime_mappings" : {
      "hour_of_day" : {
        "type" : "long",
        "script" : {
          "source" : "emit(doc['timestamp'].value.getHour());"
        }
      }
    }
  },
  "analysis_config" : {
    "bucket_span" : "15m",
    "detectors" : [
      {
        "detector_description" : "Sum of bytes",
        "function" : "sum",
        "field_name" : "bytes",
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
  "model_snapshot_retention_days" : 10,
  "daily_model_snapshot_retention_after_days" : 1,
  "results_index_name" : "custom-test-job1",
  "allow_lazy_open" : false
}
```
