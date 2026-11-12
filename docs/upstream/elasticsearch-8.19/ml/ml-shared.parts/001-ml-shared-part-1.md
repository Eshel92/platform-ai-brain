<!-- Part 1 of 3 of ml/ml-shared.md (split because the page is big). -->

<!-- Converted from ml/ml-shared.asciidoc (AsciiDoc). Includes are inlined. -->

tag::adaptive-allocation[]
Adaptive allocations configuration object.
If enabled, the number of allocations of the model is set based on the current load the process gets.
When the load is high, a new model allocation is automatically created (respecting the value of `max_number_of_allocations` if it's set).
When the load is low, a model allocation is automatically removed (respecting the value of `min_number_of_allocations` if it's set).
If `adaptive_allocations` is enabled, do not set the number of allocations manually.
end::adaptive-allocation[]

tag::adaptive-allocation-enabled[]
If `true`, `adaptive_allocations` is enabled.
Defaults to `false`.
end::adaptive-allocation-enabled[]

tag::adaptive-allocation-max-number[]
Specifies the maximum number of allocations to scale to.
If set, it must be greater than or equal to `min_number_of_allocations`.
end::adaptive-allocation-max-number[]

tag::adaptive-allocation-min-number[]
Specifies the minimum number of allocations to scale to.
If set, it must be greater than or equal to `0`.
If not defined, the deployment scales to `0`.
end::adaptive-allocation-min-number[]

tag::aggregations[]
If set, the datafeed performs aggregation searches. Support for aggregations is
limited and should be used only with low cardinality data. For more information,
see
{ml-docs}/ml-configuring-aggregation.html[Aggregating data for faster performance].
end::aggregations[]

tag::allow-lazy-open[]
Advanced configuration option. Specifies whether this job can open when there is
insufficient machine learning node capacity for it to be immediately assigned to a node. The
default value is `false`; if a machine learning node with capacity to run the job cannot
immediately be found, the open anomaly detection jobs API returns an
error. However, this is also subject to the cluster-wide
`xpack.ml.max_lazy_ml_nodes` setting; see advanced-ml-settings. If this
option is set to `true`, the open anomaly detection jobs API does not
return an error and the job waits in the `opening` state until sufficient machine learning
node capacity is available.
end::allow-lazy-open[]

tag::allow-no-match-datafeeds[]
Specifies what to do when the request:
* Contains wildcard expressions and there are no datafeeds that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `datafeeds` array when
there are no matches and the subset of results when there are partial matches.
If this parameter is `false`, the request returns a `404` status code when there
are no matches or only partial matches.
end::allow-no-match-datafeeds[]

tag::allow-no-match-deployments[]
Specifies what to do when the request:
* Contains wildcard expressions and there are no deployments that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty array when there are no
matches and the subset of results when there are partial matches. If this
parameter is `false`, the request returns a `404` status code when there are no
matches or only partial matches.
end::allow-no-match-deployments[]

tag::allow-no-match-dfa-jobs[]
 Specifies what to do when the request:
* Contains wildcard expressions and there are no {dfanalytics-jobs} that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `data_frame_analytics` array
when there are no matches and the subset of results when there are partial
matches. If this parameter is `false`, the request returns a `404` status code
when there are no matches or only partial matches.
end::allow-no-match-dfa-jobs[]

tag::allow-no-match-jobs[]
Specifies what to do when the request:
* Contains wildcard expressions and there are no jobs that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `jobs` array
when there are no matches and the subset of results when there are partial
matches. If this parameter is `false`, the request returns a `404` status code
when there are no matches or only partial matches.
end::allow-no-match-jobs[]

tag::allow-no-match-models[]
Specifies what to do when the request:
* Contains wildcard expressions and there are no models that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty array when there are no
matches and the subset of results when there are partial matches. If this
parameter is `false`, the request returns a `404` status code when there are no
matches or only partial matches.
end::allow-no-match-models[]

tag::analysis[]
Defines the type of {dfanalytics} you want to perform on your source index. For
example: `outlier_detection`. See ml-dfa-analysis-objects.
end::analysis[]

tag::analysis-config[]
The analysis configuration, which specifies how to analyze the data. After you
create a job, you cannot change the analysis configuration; all the properties
are informational.
end::analysis-config[]

tag::analysis-limits[]
Limits can be applied for the resources required to hold the mathematical models
in memory. These limits are approximate and can be set per job. They do not
control the memory used by other processes, for example the Elasticsearch Java processes.
end::analysis-limits[]

tag::assignment-explanation-anomaly-jobs[]
For open anomaly detection jobs only, contains messages relating to the selection
of a node to run the job.
end::assignment-explanation-anomaly-jobs[]

tag::assignment-explanation-datafeeds[]
For started datafeeds only, contains messages relating to the selection of a
node.
end::assignment-explanation-datafeeds[]

tag::assignment-explanation-dfanalytics[]
Contains messages relating to the selection of a node.
end::assignment-explanation-dfanalytics[]

tag::assignment-memory-basis[]
Indicates where to find the memory requirement that is used to decide where the
job runs. The possible values are:
* `model_memory_limit`: The job's memory requirement is calculated on the basis
that its model memory will grow to the `model_memory_limit` specified in the
`analysis_limits` of its config.
* `current_model_bytes`: The job's memory requirement is calculated on the basis
that its current model memory size is a good reflection of what it will be in
the future.
* `peak_model_bytes`: The job's memory requirement is calculated on the basis
that its peak model memory size is a good reflection of what the model size will
be in the future.
end::assignment-memory-basis[]

tag::background-persist-interval[]
Advanced configuration option. The time between each periodic persistence of the
model. The default value is a randomized value between 3 to 4 hours, which
avoids all jobs persisting at exactly the same time. The smallest allowed value
is 1 hour.
**Tip:** For very large models (several GB), persistence could take 10-20 minutes,
so do not set the `background_persist_interval` value too low.

end::background-persist-interval[]

tag::bucket-allocation-failures-count[]
The number of buckets for which new entities in incoming data were not processed
due to insufficient model memory. This situation is also signified by a
`hard_limit: memory_status` property value.
end::bucket-allocation-failures-count[]

tag::bucket-count[]
The number of buckets processed.
end::bucket-count[]

tag::bucket-count-anomaly-jobs[]
The number of bucket results produced by the job.
end::bucket-count-anomaly-jobs[]

tag::bucket-span[]
The size of the interval that the analysis is aggregated into, typically between
`5m` and `1h`. This value should be either a whole number of days or equate to a
whole number of buckets in one day;
deprecated:[8.1, Values that do not meet these recommendations are deprecated and will be disallowed in a future version].
If the anomaly detection job uses a datafeed with
{ml-docs}/ml-configuring-aggregation.html[aggregations], this value must also be
divisible by the interval of the date histogram aggregation. The default value
is `5m`. For more information, see
{ml-docs}/ml-ad-run-jobs.html#ml-ad-bucket-span[Bucket span].
end::bucket-span[]

tag::bucket-span-results[]
The length of the bucket in seconds. This value matches the `bucket_span`
that is specified in the job.
end::bucket-span-results[]

tag::bucket-time-exponential-average[]
Exponential moving average of all bucket processing times, in milliseconds.
end::bucket-time-exponential-average[]

tag::bucket-time-exponential-average-hour[]
Exponentially-weighted moving average of bucket processing times
calculated in a 1 hour time window, in milliseconds.
end::bucket-time-exponential-average-hour[]

tag::bucket-time-maximum[]
Maximum among all bucket processing times, in milliseconds.
end::bucket-time-maximum[]

tag::bucket-time-minimum[]
Minimum among all bucket processing times, in milliseconds.
end::bucket-time-minimum[]

tag::bucket-time-total[]
Sum of all bucket processing times, in milliseconds.
end::bucket-time-total[]

tag::by-field-name[]
The field used to split the data. In particular, this property is used for
analyzing the splits with respect to their own history. It is used for finding
unusual values in the context of the split.
end::by-field-name[]

tag::calendar-id[]
A string that uniquely identifies a calendar.
end::calendar-id[]

tag::categorization-analyzer[]
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
end::categorization-analyzer[]

tag::categorization-examples-limit[]
The maximum number of examples stored per category in memory and in the results
data store. The default value is 4. If you increase this value, more examples
are available, however it requires that you have more storage available. If you
set this value to `0`, no examples are stored.
**Note:** The `categorization_examples_limit` only applies to analysis that uses
categorization. For more information, see
{ml-docs}/ml-configuring-categories.html[Categorizing log messages].
end::categorization-examples-limit[]

tag::categorization-field-name[]
If this property is specified, the values of the specified field will be
categorized. The resulting categories must be used in a detector by setting
`by_field_name`, `over_field_name`, or `partition_field_name` to the keyword
`mlcategory`. For more information, see
{ml-docs}/ml-configuring-categories.html[Categorizing log messages].
end::categorization-field-name[]

tag::categorization-filters[]
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
end::categorization-filters[]

tag::categorization-status[]
The status of categorization for the job. Contains one of the following values:
* `ok`: Categorization is performing acceptably well (or not being used at all).
* `warn`: Categorization is detecting a distribution of categories that suggests
the input data is inappropriate for categorization. Problems could be that there
is only one category, more than 90% of categories are rare, the number of
categories is greater than 50% of the number of categorized documents, there are
no frequently matched categories, or more than 50% of categories are dead.

end::categorization-status[]

tag::categorized-doc-count[]
The number of documents that have had a field categorized.
end::categorized-doc-count[]

tag::char-filter[]
One or more character filters. In addition to the
built-in character filters, other plugins can provide more character filters.
This property is optional. If it is not specified, no character filters are
applied prior to categorization. If you are customizing some other aspect of the
analyzer and you need to achieve the equivalent of `categorization_filters`
(which are not permitted when some other aspect of the analyzer is customized),
add them here as
pattern replace character filters.
end::char-filter[]

tag::chunking-config[]
Datafeeds might be required to search over long time periods, for several
months or years. This search is split into time chunks in order to ensure the
load on Elasticsearch is managed. Chunking configuration controls how the size of these
time chunks are calculated and is an advanced configuration option.
end::chunking-config[]

tag::class-assignment-objective[]
Defines the objective to optimize when assigning class labels:
`maximize_accuracy` or `maximize_minimum_recall`. When maximizing accuracy,
class labels are chosen to maximize the number of correct predictions. When
maximizing minimum recall, labels are chosen to maximize the minimum recall for
any class. Defaults to `maximize_minimum_recall`.
end::class-assignment-objective[]

tag::compute-feature-influence[]
Specifies whether the feature influence calculation is enabled. Defaults to
`true`.
end::compute-feature-influence[]

tag::custom-preprocessor[]
(Optional, Boolean)
Boolean value indicating if the analytics job created the preprocessor
or if a user provided it. This adjusts the feature importance calculation.
When `true`, the feature importance calculation returns importance for the
processed feature. When `false`, the total importance of the original field
is returned. Default is `false`.
end::custom-preprocessor[]

tag::custom-rules[]
An array of custom rule objects, which enable you to customize the way detectors
operate. For example, a rule may dictate to the detector conditions under which
results should be skipped. Kibana refers to custom rules as _job rules_. For more
examples, see
{ml-docs}/ml-configuring-detector-custom-rules.html[Customizing detectors with custom rules].
end::custom-rules[]

tag::custom-rules-actions[]
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
end::custom-rules-actions[]

tag::custom-rules-scope[]
An optional scope of series where the rule applies. A rule must either
have a non-empty scope or at least one condition. By default, the scope includes
all series. Scoping is allowed for any of the fields that are also specified in
`by_field_name`, `over_field_name`, or `partition_field_name`. To add a scope
for a field, add the field name as a key in the scope object and set its value
to an object with the following properties:
end::custom-rules-scope[]

tag::custom-rules-scope-filter-id[]
The id of the filter to be used.
end::custom-rules-scope-filter-id[]

tag::custom-rules-scope-filter-type[]
Either `include` (the rule applies for values in the filter) or `exclude` (the
rule applies for values not in the filter). Defaults to `include`.
end::custom-rules-scope-filter-type[]

tag::custom-rules-conditions[]
An optional array of numeric conditions when the rule applies. A rule must
either have a non-empty scope or at least one condition. Multiple conditions are
combined together with a logical `AND`. A condition has the following
properties:
end::custom-rules-conditions[]

tag::custom-rules-conditions-applies-to[]
Specifies the result property to which the condition applies. The available
options are `actual`, `typical`, `diff_from_typical`, `time`. If your detector
uses `lat_long`, `metric`, `rare`, or `freq_rare` functions, you can only
specify conditions that apply to `time`.
end::custom-rules-conditions-applies-to[]

tag::custom-rules-conditions-operator[]
Specifies the condition operator. The available options are `gt` (greater than),
`gte` (greater than or equals), `lt` (less than) and `lte` (less than or
equals).
end::custom-rules-conditions-operator[]

tag::custom-rules-conditions-value[]
The value that is compared against the `applies_to` field using the `operator`.
end::custom-rules-conditions-value[]

tag::custom-rules-params[]
A set of parameter objects that customize the actions defined in the custom rules
actions array. The available parameters (depending on the specified actions) include:
`force_time_shift`.
end::custom-rules-params[]

tag::custom-rules-params-force-time-shift[]
Set `time_shift_amount` to the signed number of seconds by which you want to shift the time.
end::custom-rules-params-force-time-shift[]

tag::custom-settings[]
Advanced configuration option. Contains custom metadata about the job. For
example, it can contain custom URL information as shown in
{ml-docs}/ml-configuring-url.html[Adding custom URLs to machine learning results].
end::custom-settings[]

tag::daily-model-snapshot-retention-after-days[]
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
end::daily-model-snapshot-retention-after-days[]

tag::data-description[]
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
end::data-description[]

tag::datafeed-id[]
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.
end::datafeed-id[]

tag::datafeed-id-wildcard[]
Identifier for the datafeed. It can be a datafeed identifier or a wildcard
expression.
end::datafeed-id-wildcard[]

tag::dead-category-count[]
The number of categories created by categorization that will never be assigned
again because another category's definition makes it a superset of the dead
category. (Dead categories are a side effect of the way categorization has no
prior training.)
end::dead-category-count[]

tag::delayed-data-check-config[]
Specifies whether the datafeed checks for missing data and the size of the
window. For example: `{"enabled": true, "check_window": "1h"}`.
The datafeed can optionally search over indices that have already been read in
an effort to determine whether any data has subsequently been added to the
index. If missing data is found, it is a good indication that the `query_delay`
option is set too low and the data is being indexed after the datafeed has passed
that moment in time. See
{ml-docs}/ml-delayed-data-detection.html[Working with delayed data].
This check runs only on real-time datafeeds.
end::delayed-data-check-config[]

tag::delayed-data-check-config-check-window[]
The window of time that is searched for late data. This window of time ends with
the latest finalized bucket. It defaults to `null`, which causes an appropriate
`check_window` to be calculated when the real-time datafeed runs. In particular,
the default `check_window` span calculation is based on the maximum of `2h` or
`8 * bucket_span`.
end::delayed-data-check-config-check-window[]

tag::delayed-data-check-config-enabled[]
Specifies whether the datafeed periodically checks for delayed data. Defaults to
`true`.
end::delayed-data-check-config-enabled[]

tag::dependent-variable[]
Defines which field of the document is to be predicted.
This parameter is supplied by field name and must match one of the fields in
the index being used to train. If this field is missing from a document, then
that document will not be used for training, but a prediction with the trained
model will be generated for it. It is also known as continuous target variable.
end::dependent-variable[]

tag::deployment-id[]
A unique identifier for the deployment of the model.
end::deployment-id[]

tag::desc-results[]
If true, the results are sorted in descending order.
end::desc-results[]

tag::description-dfa[]
A description of the job.
end::description-dfa[]

tag::dest[]
The destination configuration, consisting of `index` and optionally
`results_field` (`ml` by default).
**Properties of `dest`**
`index`:::
(Required, string) Defines the _destination index_ to store the results of the
{dfanalytics-job}.

`results_field`:::
(Optional, string) Defines the name of the field in which to store the results
of the analysis. Defaults to `ml`.
end::dest[]

tag::detector-description[]
A description of the detector. For example, `Low event rate`.
end::detector-description[]

tag::detector-field-name[]
The field that the detector uses in the function. If you use an event rate
function such as `count` or `rare`, do not specify this field.
**Note:** The `field_name` cannot contain double quotes or backslashes.

end::detector-field-name[]

tag::detector-index[]
A unique identifier for the detector. This identifier is based on the order of
the detectors in the `analysis_config`, starting at zero.
end::detector-index[]

tag::dfas-alpha[]
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This parameter affects loss calculations by acting as a multiplier of
the tree depth. Higher alpha values result in shallower trees and faster
training times. By default, this value is calculated during hyperparameter
optimization. It must be greater than or equal to zero.
end::dfas-alpha[]

tag::dfas-downsample-factor[]
Advanced configuration option. Controls the fraction of data that is used to
compute the derivatives of the loss function for tree training. A small value
results in the use of a small fraction of the data. If this value is set to be
less than 1, accuracy typically improves. However, too small a value may result
in poor convergence for the ensemble and so require more trees. For more
information about shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Stochastic_gradient_boosting).
By default, this value is calculated during hyperparameter optimization. It
must be greater than zero and less than or equal to 1.
end::dfas-downsample-factor[]

tag::dfas-early-stopping-enabled[]
Advanced configuration option.
Specifies whether the training process should finish if it is not finding any
better performing models. If disabled, the training process can take significantly
longer and the chance of finding a better performing model is unremarkable.
By default, early stoppping is enabled.
end::dfas-early-stopping-enabled[]

tag::dfas-eta-growth[]
Advanced configuration option. Specifies the rate at which `eta` increases for
each new tree that is added to the forest. For example, a rate of 1.05
increases `eta` by 5% for each extra tree. By default, this value is calculated
during hyperparameter optimization. It must be between 0.5 and 2.
end::dfas-eta-growth[]

tag::dfas-feature-bag-fraction[]
The fraction of features that is used when selecting a random bag for each
candidate split.
end::dfas-feature-bag-fraction[]

tag::dfas-feature-processors[]
Advanced configuration option. A collection of feature preprocessors that modify
one or more included fields. The analysis uses the resulting one or more
features instead of the original document field. However, these features are
ephemeral; they are not stored in the destination index. Multiple
`feature_processors` entries can refer to the same document fields. Automatic
categorical {ml-docs}/ml-feature-encoding.html[feature encoding] still occurs
for the fields that are unprocessed by a custom processor or that have
categorical values. Use this property only if you want to override the automatic
feature encoding of the specified fields. Refer to
{ml-docs}/ml-feature-processors.html[{dfanalytics} feature processors] to learn
more.
end::dfas-feature-processors[]

tag::dfas-feature-processors-feat-name[]
The resulting feature name.
end::dfas-feature-processors-feat-name[]

tag::dfas-feature-processors-field[]
The name of the field to encode.
end::dfas-feature-processors-field[]

tag::dfas-feature-processors-frequency[]
The configuration information necessary to perform frequency encoding.
end::dfas-feature-processors-frequency[]

tag::dfas-feature-processors-frequency-map[]
The resulting frequency map for the field value. If the field value is missing
from the `frequency_map`, the resulting value is `0`.
end::dfas-feature-processors-frequency-map[]

tag::dfas-feature-processors-multi[]
The configuration information necessary to perform multi encoding. It allows
multiple processors to be changed together. This way the output of a processor
can then be passed to another as an input.
end::dfas-feature-processors-multi[]

tag::dfas-feature-processors-multi-proc[]
The ordered array of custom processors to execute. Must be more than 1.
end::dfas-feature-processors-multi-proc[]

tag::dfas-feature-processors-ngram[]
The configuration information necessary to perform n-gram encoding. Features
created by this encoder have the following name format:
`<feature_prefix>.<ngram><string position>`. For example, if the
`feature_prefix` is `f`, the feature name for the second unigram in a string is
`f.11`.
end::dfas-feature-processors-ngram[]

tag::dfas-feature-processors-ngram-feat-pref[]
The feature name prefix. Defaults to `ngram_<start>_<length>`.
end::dfas-feature-processors-ngram-feat-pref[]

tag::dfas-feature-processors-ngram-field[]
The name of the text field to encode.
end::dfas-feature-processors-ngram-field[]

tag::dfas-feature-processors-ngram-length[]
Specifies the length of the n-gram substring. Defaults to `50`. Must be greater
than `0`.
end::dfas-feature-processors-ngram-length[]

tag::dfas-feature-processors-ngram-ngrams[]
Specifies which n-grams to gather. It’s an array of integer values where the
minimum value is 1, and a maximum value is 5.
end::dfas-feature-processors-ngram-ngrams[]

tag::dfas-feature-processors-ngram-start[]
Specifies the zero-indexed start of the n-gram substring. Negative values are
allowed for encoding n-grams of string suffixes. Defaults to `0`.
end::dfas-feature-processors-ngram-start[]

tag::dfas-feature-processors-one-hot[]
The configuration information necessary to perform one hot encoding.
end::dfas-feature-processors-one-hot[]

tag::dfas-feature-processors-one-hot-map[]
The one hot map mapping the field value with the column name.
end::dfas-feature-processors-one-hot-map[]

tag::dfas-feature-processors-target-mean[]
The configuration information necessary to perform target mean encoding.
end::dfas-feature-processors-target-mean[]

tag::dfas-feature-processors-target-mean-default[]
The default value if field value is not found in the `target_map`.
end::dfas-feature-processors-target-mean-default[]

tag::dfas-feature-processors-target-mean-map[]
The field value to target mean transition map.
end::dfas-feature-processors-target-mean-map[]

tag::dfas-iteration[]
The number of iterations on the analysis.
end::dfas-iteration[]

tag::dfas-max-attempts[]
If the algorithm fails to determine a non-trivial tree (more than a single
leaf), this parameter determines how many of such consecutive failures are
tolerated. Once the number of attempts exceeds the threshold, the forest
training stops.
end::dfas-max-attempts[]

tag::dfas-max-optimization-rounds[]
Advanced configuration option.
A multiplier responsible for determining the maximum number of
hyperparameter optimization steps in the Bayesian optimization procedure.
The maximum number of steps is determined based on the number of undefined
hyperparameters times the maximum optimization rounds per hyperparameter.
By default, this value is calculated during hyperparameter optimization.
end::dfas-max-optimization-rounds[]

tag::dfas-num-folds[]
The maximum number of folds for the cross-validation procedure.
end::dfas-num-folds[]

tag::dfas-num-splits[]
Determines the maximum number of splits for every feature that can occur in a
decision tree when the tree is trained.
end::dfas-num-splits[]

tag::dfas-soft-limit[]
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This soft limit combines with the `soft_tree_depth_tolerance` to
penalize trees that exceed the specified depth; the regularized loss increases
quickly beyond this depth. By default, this value is calculated during
hyperparameter optimization. It must be greater than or equal to 0.
end::dfas-soft-limit[]

tag::dfas-soft-tolerance[]
Advanced configuration option. This option controls how quickly the regularized
loss increases when the tree depth exceeds `soft_tree_depth_limit`. By default,
this value is calculated during hyperparameter optimization. It must be greater
than or equal to 0.01.
end::dfas-soft-tolerance[]

tag::dfas-timestamp[]
The timestamp when the statistics were reported in milliseconds since the epoch.
end::dfas-timestamp[]

tag::dfas-timing-stats[]
An object containing time statistics about the {dfanalytics-job}.
end::dfas-timing-stats[]

tag::dfas-timing-stats-elapsed[]
Runtime of the analysis in milliseconds.
end::dfas-timing-stats-elapsed[]

tag::dfas-timing-stats-iteration[]
Runtime of the latest iteration of the analysis in milliseconds.
end::dfas-timing-stats-iteration[]

tag::dfas-validation-loss[]
An object containing information about validation loss.
end::dfas-validation-loss[]

tag::dfas-validation-loss-fold[]
Validation loss values for every added decision tree during the forest growing
procedure.
end::dfas-validation-loss-fold[]

tag::dfas-validation-loss-type[]
The type of the loss metric. For example, `binomial_logistic`.
end::dfas-validation-loss-type[]

tag::earliest-record-timestamp[]
The timestamp of the earliest chronologically input document.
end::earliest-record-timestamp[]

tag::empty-bucket-count[]
The number of buckets which did not contain any data. If your data
contains many empty buckets, consider increasing your `bucket_span` or using
functions that are tolerant to gaps in data such as `mean`, `non_null_sum` or
`non_zero_count`.
end::empty-bucket-count[]

tag::eta[]
Advanced configuration option. The shrinkage applied to the weights. Smaller
values result in larger forests which have a better generalization error.
However, larger forests cause slower training. For more information about
shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Shrinkage).
By default, this value is calculated during hyperparameter optimization. It must
be a value between 0.001 and 1.
end::eta[]

tag::exclude-frequent[]
Contains one of the following values: `all`, `none`, `by`, or `over`. If set,
frequent entities are excluded from influencing the anomaly results. Entities
can be considered frequent over time or frequent in a population. If you are
working with both over and by fields, then you can set `exclude_frequent` to
`all` for both fields, or to `by` or `over` for those specific fields.
end::exclude-frequent[]

tag::exclude-interim-results[]
If `true`, the output excludes interim results. Defaults to `false`, which means interim results are included.
end::exclude-interim-results[]

tag::failed-category-count[]
The number of times that categorization wanted to create a new category but
couldn't because the job had hit its `model_memory_limit`. This count does not
track which specific categories failed to be created. Therefore you cannot use
this value to determine the number of unique categories that were missed.
end::failed-category-count[]

tag::feature-bag-fraction[]
Advanced configuration option. Defines the fraction of features that will be
used when selecting a random bag for each candidate split. By default, this
value is calculated during hyperparameter optimization.
end::feature-bag-fraction[]

tag::feature-influence-threshold[]
The minimum {olscore} that a document needs to have in order to calculate its
{fiscore}. Value range: 0-1 (`0.1` by default).
end::feature-influence-threshold[]

tag::filter[]
One or more token filters. In addition to the built-in
token filters, other plugins can provide more token filters. This property is
optional. If it is not specified, no token filters are applied prior to
categorization.
end::filter[]

tag::filter-id[]
A string that uniquely identifies a filter.
end::filter-id[]

tag::forecast-total[]
The number of individual forecasts currently available for the job. A value of
`1` or more indicates that forecasts exist.
end::forecast-total[]

tag::exclude-generated[]
Indicates if certain fields should be removed from the configuration on
retrieval. This allows the configuration to be in an acceptable format to be retrieved
and then added to another cluster. Default is false.
end::exclude-generated[]

tag::frequency[]
The interval at which scheduled queries are made while the datafeed runs in real
time. The default value is either the bucket span for short bucket spans, or,
for longer bucket spans, a sensible fraction of the bucket span. For example:
`150s`. When `frequency` is shorter than the bucket span, interim results for
the last (partial) bucket are written then eventually overwritten by the full
bucket results. If the datafeed uses aggregations, this value must be divisible
by the interval of the date histogram aggregation.
end::frequency[]

tag::frequent-category-count[]
The number of categories that match more than 1% of categorized documents.
end::frequent-category-count[]

tag::from[]
Skips the specified number of {dfanalytics-jobs}. The default value is `0`.
end::from[]

tag::from-models[]
Skips the specified number of models. The default value is `0`.
end::from-models[]

tag::function[]
