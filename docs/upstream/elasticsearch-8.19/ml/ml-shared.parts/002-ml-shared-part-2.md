<!-- Part 2 of 3 of ml/ml-shared.md (split because the page is big). -->

The analysis function that is used. For example, `count`, `rare`, `mean`, `min`,
`max`, and `sum`. For more information, see
{ml-docs}/ml-functions.html[Function reference].
end::function[]

tag::gamma[]
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies a linear penalty associated with the size
of individual trees in the forest. A high gamma value causes training to prefer
small trees. A small gamma value results in larger individual trees and slower
training. By default, this value is calculated during hyperparameter
optimization. It must be a nonnegative value.
end::gamma[]

tag::groups[]
A list of job groups. A job can belong to no groups or many.
end::groups[]

tag::indices[]
An array of index names. Wildcards are supported. For example:
`["it_ops_metrics", "server*"]`.
**Note:** If any indices are in remote clusters then the master nodes and the machine learning nodes need to have the
`remote_cluster_client` role.

end::indices[]

tag::indices-options[]
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
end::indices-options[]

tag::runtime-mappings[]
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

end::runtime-mappings[]

tag::inference-config-classification-num-top-classes[]
Specifies the number of top class predictions to return. Defaults to 0.
end::inference-config-classification-num-top-classes[]

tag::inference-config-classification-num-top-feature-importance-values[]
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document. Defaults
to 0 which means no {feat-imp} calculation occurs.
end::inference-config-classification-num-top-feature-importance-values[]

tag::inference-config-classification-top-classes-results-field[]
Specifies the field to which the top classes are written. Defaults to
`top_classes`.
end::inference-config-classification-top-classes-results-field[]

tag::inference-config-classification-prediction-field-type[]
Specifies the type of the predicted field to write.
Valid values are: `string`, `number`, `boolean`. When `boolean` is provided
`1.0` is transformed to `true` and `0.0` to `false`.
end::inference-config-classification-prediction-field-type[]

tag::inference-config-nlp-tokenization[]
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
end::inference-config-nlp-tokenization[]

tag::inference-config-nlp-tokenization-bert[]
BERT-style tokenization is to be performed with the enclosed settings.
end::inference-config-nlp-tokenization-bert[]

tag::inference-config-nlp-tokenization-bert-ja[]
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
end::inference-config-nlp-tokenization-bert-ja[]

tag::inference-config-nlp-tokenization-do-lower-case[]
Specifies if the tokenization lower case the text sequence when building the
tokens.
end::inference-config-nlp-tokenization-do-lower-case[]

tag::inference-config-nlp-tokenization-span[]
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
end::inference-config-nlp-tokenization-span[]

tag::inference-config-nlp-tokenization-truncate[]
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

end::inference-config-nlp-tokenization-truncate[]

tag::inference-config-nlp-tokenization-truncate-deberta-v2[]
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

end::inference-config-nlp-tokenization-truncate-deberta-v2[]

tag::inference-config-nlp-tokenization-bert-with-special-tokens[]
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
end::inference-config-nlp-tokenization-bert-with-special-tokens[]

tag::inference-config-nlp-tokenization-bert-ja-with-special-tokens[]
Tokenize with special tokens if `true`.
end::inference-config-nlp-tokenization-bert-ja-with-special-tokens[]

tag::inference-config-nlp-tokenization-deberta-v2[]
DeBERTa-style tokenization is to be performed with the enclosed settings.
end::inference-config-nlp-tokenization-deberta-v2[]

tag::inference-config-nlp-tokenization-max-sequence-length[]
Specifies the maximum number of tokens allowed to be output by the tokenizer.
end::inference-config-nlp-tokenization-max-sequence-length[]

tag::inference-config-nlp-tokenization-deberta-v2-with-special-tokens[]
Tokenize with special tokens. The tokens typically included in DeBERTa-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation and sequence end.
end::inference-config-nlp-tokenization-deberta-v2-with-special-tokens[]

tag::inference-config-nlp-tokenization-roberta[]
RoBERTa-style tokenization is to be performed with the enclosed settings.
end::inference-config-nlp-tokenization-roberta[]

tag::inference-config-nlp-tokenization-roberta-add-prefix-space[]
Specifies if the tokenization should prefix a space to the tokenized input to the model.
end::inference-config-nlp-tokenization-roberta-add-prefix-space[]

tag::inference-config-nlp-tokenization-roberta-with-special-tokens[]
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
end::inference-config-nlp-tokenization-roberta-with-special-tokens[]

tag::inference-config-nlp-tokenization-mpnet[]
MPNet-style tokenization is to be performed with the enclosed settings.
end::inference-config-nlp-tokenization-mpnet[]

tag::inference-config-nlp-tokenization-mpnet-with-special-tokens[]
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
end::inference-config-nlp-tokenization-mpnet-with-special-tokens[]

tag::inference-config-nlp-tokenization-xlm-roberta[]
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
end::inference-config-nlp-tokenization-xlm-roberta[]

tag::inference-config-nlp-vocabulary[]
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
end::inference-config-nlp-vocabulary[]

tag::inference-config-nlp-fill-mask[]
Configuration for a fill_mask natural language processing (NLP) task. The
fill_mask task works with models optimized for a fill mask action. For example,
for BERT models, the following text may be provided: "The capital of France is
[MASK].". The response indicates the value most likely to replace `[MASK]`. In
this instance, the most probable token is `paris`.
end::inference-config-nlp-fill-mask[]

tag::inference-config-ner[]
Configures a named entity recognition (NER) task. NER is a special case of token
classification. Each token in the sequence is classified according to the
provided classification labels. Currently, the NER task requires the
`classification_labels` Inside-Outside-Beginning (IOB) formatted labels. Only
person, organization, location, and miscellaneous are supported.
end::inference-config-ner[]

tag::inference-config-pass-through[]
Configures a `pass_through` task. This task is useful for debugging as no
post-processing is done to the inference output and the raw pooling layer
results are returned to the caller.
end::inference-config-pass-through[]

tag::inference-config-nlp-question-answering[]
Configures a question answering natural language processing (NLP) task. Question
answering is useful for extracting answers for certain questions from a large
corpus of text.
end::inference-config-nlp-question-answering[]

tag::inference-config-text-classification[]
A text classification task. Text classification classifies a provided text
sequence into previously known target classes. A specific example of this is
sentiment analysis, which returns the likely target classes indicating text
sentiment, such as "sad", "happy", or "angry".
end::inference-config-text-classification[]

tag::inference-config-text-embedding[]
Text embedding takes an input sequence and transforms it into a vector of
numbers. These embeddings capture not simply tokens, but semantic meanings and
context. These embeddings can be used in a dense vector field
for powerful insights.
end::inference-config-text-embedding[]

tag::inference-config-text-embedding-size[]
The number of dimensions in the embedding vector produced by the model.
end::inference-config-text-embedding-size[]

tag::inference-config-text-expansion[]
The text expansion task works with sparse embedding models to transform an input sequence
into a vector of weighted tokens. These embeddings capture semantic meanings and
context and can be used in a sparse vector field for powerful insights.
end::inference-config-text-expansion[]

tag::inference-config-text-similarity[]
Text similarity takes an input sequence and compares it with another input sequence. This is commonly referred to
as cross-encoding. This task is useful for ranking document text when comparing it to another provided text input.
end::inference-config-text-similarity[]

tag::inference-config-text-similarity-span-score-func[]
Identifies how to combine the resulting similarity score when a provided text passage is longer than `max_sequence_length` and must be
automatically separated for multiple calls. This only is applicable when `truncate` is `none` and `span` is a non-negative
number. The default value is `max`. Available options are:
* `max`: The maximum score from all the spans is returned.
* `mean`: The mean score over all the spans is returned.
end::inference-config-text-similarity-span-score-func[]

tag::inference-config-text-similarity-text[]
This is the text with which to compare all document provided text inputs.
end::inference-config-text-similarity-text[]

tag::inference-config-regression-num-top-feature-importance-values[]
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document.
By default, it is zero and no {feat-imp} calculation occurs.
end::inference-config-regression-num-top-feature-importance-values[]

tag::inference-config-results-field[]
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
end::inference-config-results-field[]

tag::inference-config-mask-token[]
The string/token which will be removed from incoming documents and replaced with the inference prediction(s). In a response, this field contains the mask token for the specified model/tokenizer. Each model and tokenizer has a predefined mask token which cannot be changed. Thus, it is recommended not to set this value in requests. However, if this field is present in a request, its value must match the predefined value for that model/tokenizer, otherwise the request will fail.
end::inference-config-mask-token[]

tag::inference-config-results-field-processor[]
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
end::inference-config-results-field-processor[]

tag::inference-config-zero-shot-classification[]
Configures a zero-shot classification task. Zero-shot classification allows for
text classification to occur without pre-determined labels. At inference time,
it is possible to adjust the labels to classify. This makes this type of model
and task exceptionally flexible.
If consistently classifying the same labels, it may be better to use a
fine-tuned text classification model.
end::inference-config-zero-shot-classification[]

tag::inference-config-zero-shot-classification-classification-labels[]
The classification labels used during the zero-shot classification. Classification
labels must not be empty or null and only set at model creation. They must be all three
of ["entailment", "neutral", "contradiction"].

**Note:** This is NOT the same as `labels` which are the values that zero-shot is attempting to
      classify.
end::inference-config-zero-shot-classification-classification-labels[]

tag::inference-config-zero-shot-classification-hypothesis-template[]
This is the template used when tokenizing the sequences for classification.
The labels replace the `{}` value in the text. The default value is:
`This example is {}.`
end::inference-config-zero-shot-classification-hypothesis-template[]

tag::inference-config-zero-shot-classification-labels[]
The labels to classify. Can be set at creation for default labels, and
then updated during inference.
end::inference-config-zero-shot-classification-labels[]

tag::inference-config-zero-shot-classification-multi-label[]
Indicates if more than one `true` label is possible given the input.
This is useful when labeling text that could pertain to more than one of the
input labels. Defaults to `false`.
end::inference-config-zero-shot-classification-multi-label[]

tag::inference-metadata-feature-importance-feature-name[]
The feature for which this importance was calculated.
end::inference-metadata-feature-importance-feature-name[]
tag::inference-metadata-feature-importance-magnitude[]
The average magnitude of this feature across all the training data.
This value is the average of the absolute values of the importance
for this feature.
end::inference-metadata-feature-importance-magnitude[]
tag::inference-metadata-feature-importance-max[]
The maximum importance value across all the training data for this
feature.
end::inference-metadata-feature-importance-max[]
tag::inference-metadata-feature-importance-min[]
The minimum importance value across all the training data for this
feature.
end::inference-metadata-feature-importance-min[]

tag::influencers[]
A comma separated list of influencer field names. Typically these can be the by,
over, or partition fields that are used in the detector configuration. You might
also want to use a field name that is not specifically named in a detector, but
is available as part of the input data. When you use multiple detectors, the use
of influencers is recommended as it aggregates results for each influencer
entity.
end::influencers[]

tag::input-bytes[]
The number of bytes of input data posted to the anomaly detection job.
end::input-bytes[]

tag::input-field-count[]
The total number of fields in input documents posted to the anomaly detection job. This
count includes fields that are not used in the analysis. However, be aware that
if you are using a datafeed, it extracts only the required fields from the
documents it retrieves before posting them to the job.
end::input-field-count[]

tag::input-record-count[]
The number of input documents posted to the anomaly detection job.
end::input-record-count[]

tag::invalid-date-count[]
The number of input documents with either a missing date field or a date that
could not be parsed.
end::invalid-date-count[]

tag::is-interim[]
If `true`, this is an interim result. In other words, the results are calculated
based on partial input data.
end::is-interim[]

tag::job-id-anomaly-detection[]
Identifier for the anomaly detection job.
end::job-id-anomaly-detection[]

tag::job-id-data-frame-analytics[]
Identifier for the {dfanalytics-job}.
end::job-id-data-frame-analytics[]

tag::job-id-anomaly-detection-default[]
Identifier for the anomaly detection job. It can be a job identifier, a group name, or a
wildcard expression. If you do not specify one of these options, the API returns
information for all anomaly detection jobs.
end::job-id-anomaly-detection-default[]

tag::job-id-data-frame-analytics-default[]
Identifier for the {dfanalytics-job}. If you do not specify this option, the API
returns information for the first hundred {dfanalytics-jobs}.
end::job-id-data-frame-analytics-default[]

tag::job-id-anomaly-detection-list[]
An identifier for the anomaly detection jobs. It can be a job
identifier, a group name, or a comma-separated list of jobs or groups.
end::job-id-anomaly-detection-list[]

tag::job-id-anomaly-detection-wildcard[]
Identifier for the anomaly detection job. It can be a job identifier, a group name, or a
wildcard expression.
end::job-id-anomaly-detection-wildcard[]

tag::job-id-anomaly-detection-wildcard-list[]
Identifier for the anomaly detection job. It can be a job identifier, a group name, a
comma-separated list of jobs or groups, or a wildcard expression.
end::job-id-anomaly-detection-wildcard-list[]

tag::job-id-anomaly-detection-define[]
Identifier for the anomaly detection job. This identifier can contain lowercase
alphanumeric characters (a-z and 0-9), hyphens, and underscores. It must start
and end with alphanumeric characters.
end::job-id-anomaly-detection-define[]

tag::job-id-data-frame-analytics-define[]
Identifier for the {dfanalytics-job}. This identifier can contain lowercase
alphanumeric characters (a-z and 0-9), hyphens, and underscores. It must start
and end with alphanumeric characters.
end::job-id-data-frame-analytics-define[]

tag::job-id-datafeed[]
The unique identifier for the job to which the datafeed sends data.
end::job-id-datafeed[]

tag::output-memory-allocator-bytes[]
The amount of memory, in bytes, used to output anomaly detection job documents.
end::output-memory-allocator-bytes[]

tag::lambda[]
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies an L2 regularization term which applies to
leaf weights of the individual trees in the forest. A high lambda value causes
training to favor small leaf weights. This behavior makes the prediction
function smoother at the expense of potentially not being able to capture
relevant relationships between the features and the {depvar}. A small lambda
value results in large individual trees and slower training. By default, this
value is calculated during hyperparameter optimization. It must be a nonnegative
value.
end::lambda[]

tag::last-data-time[]
The timestamp at which data was last analyzed, according to server time.
end::last-data-time[]

tag::latency[]
The size of the window in which to expect data that is out of time order. The
default value is 0 (no latency). If you specify a non-zero value, it must be
greater than or equal to one second. For more information about time units, see
time-units.
**Note:** Latency is only applicable when you send data by using
the post data API.

end::latency[]

tag::latest-empty-bucket-timestamp[]
The timestamp of the last bucket that did not contain any data.
end::latest-empty-bucket-timestamp[]

tag::latest-record-timestamp[]
The timestamp of the latest chronologically input document.
end::latest-record-timestamp[]

tag::latest-sparse-record-timestamp[]
The timestamp of the last bucket that was considered sparse.
end::latest-sparse-record-timestamp[]

tag::max-empty-searches[]
If a real-time datafeed has never seen any data (including during any initial
training period) then it will automatically stop itself and close its associated
job after this many real-time searches that return no documents. In other words,
it will stop after `frequency` times `max_empty_searches` of real-time
operation. If not set then a datafeed with no end time that sees no data will
remain started until it is explicitly stopped. By default this setting is not
set.
end::max-empty-searches[]

tag::max-trees[]
Advanced configuration option. Defines the maximum number of decision trees in
the forest. The maximum value is 2000. By default, this value is calculated
during hyperparameter optimization.
end::max-trees[]

tag::max-trees-trained-models[]
The maximum number of decision trees in the forest. The maximum value is 2000.
By default, this value is calculated during hyperparameter optimization.
end::max-trees-trained-models[]

tag::meta[]
Advanced configuration option. Contains custom metadata about the job. For
example, it can contain custom URL information.
end::meta[]

tag::method[]
The method that {oldetection} uses. Available methods are `lof`, `ldof`,
`distance_kth_nn`, `distance_knn`, and `ensemble`. The default value is
`ensemble`, which means that {oldetection} uses an ensemble of different methods
and normalises and combines their individual {olscores} to obtain the overall
{olscore}.
end::method[]

tag::missing-field-count[]
The number of input documents that are missing a field that the anomaly detection job is
configured to analyze. Input documents with missing fields are still processed
because it is possible that not all fields are missing.
**Note:** If you are using datafeeds or posting data to the job in JSON format, a
high `missing_field_count` is often not an indication of data issues. It is not
necessarily a cause for concern.

end::missing-field-count[]

tag::mode[]
There are three available modes:
* `auto`: The chunk size is dynamically calculated. This is the default and
recommended value when the datafeed does not use aggregations.
* `manual`: Chunking is applied according to the specified `time_span`. Use this
mode when the datafeed uses aggregations.
* `off`: No chunking is applied.
end::mode[]

tag::model-bytes[]
The number of bytes of memory used by the models. This is the maximum value
since the last time the model was persisted. If the job is closed, this value
indicates the latest size.
end::model-bytes[]

tag::model-bytes-exceeded[]
The number of bytes over the high limit for memory usage at the last allocation
failure.
end::model-bytes-exceeded[]

tag::model-id[]
The unique identifier of the trained model.
end::model-id[]

tag::model-id-or-alias[]
The unique identifier of the trained model or a model alias.
end::model-id-or-alias[]

tag::model-memory-limit-ad[]
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
end::model-memory-limit-ad[]

tag::model-memory-limit-anomaly-jobs[]
The upper limit for model memory usage, checked on increasing values.
end::model-memory-limit-anomaly-jobs[]

tag::model-memory-limit-dfa[]
The approximate maximum amount of memory resources that are permitted for
analytical processing. The default value for {dfanalytics-jobs} is `1gb`. If
you specify a value for the `xpack.ml.max_model_memory_limit` setting, an error
occurs when you try to create jobs that have `model_memory_limit` values greater
than that setting value. For more information, see
ml-settings.
end::model-memory-limit-dfa[]

tag::model-memory-status[]
The status of the mathematical models, which can have one of the following
values:
* `ok`: The models stayed below the configured value.
* `soft_limit`: The models used more than 60% of the configured memory limit
and older unused models will be pruned to free up space. Additionally, in
categorization jobs no further category examples will be stored.
* `hard_limit`: The models used more space than the configured memory limit.
As a result, not all incoming data was processed.
end::model-memory-status[]

tag::model-plot-config[]
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
end::model-plot-config[]

tag::model-plot-config-annotations-enabled[]
If true, enables calculation and storage of the model change annotations
for each entity that is being analyzed. Defaults to `enabled`.
end::model-plot-config-annotations-enabled[]

tag::model-plot-config-enabled[]
If true, enables calculation and storage of the model bounds for each entity
that is being analyzed. By default, this is not enabled.
end::model-plot-config-enabled[]

tag::model-plot-config-terms[]
Limits data collection to this comma separated list of partition or by field
values. If terms are not specified or it is an empty string, no filtering is
applied. For example, "CPU,NetworkIn,DiskWrites". Wildcards are not supported.
Only the specified `terms` can be viewed when using the Single Metric Viewer.
end::model-plot-config-terms[]

tag::model-prune-window[]
Advanced configuration option.
Affects the pruning of models that have not been updated for the given time
duration. The value must be set to a multiple of the `bucket_span`. If set too
low, important information may be removed from the model. Typically, set to
`30d` or longer. If not set, model pruning only occurs if the model memory
status reaches the soft limit or the hard limit. For jobs created in 8.1 and
later, the default value is the greater of `30d` or 20 times `bucket_span`.
end::model-prune-window[]

tag::model-snapshot-id[]
A numerical character string that uniquely identifies the model snapshot. For
example, `1575402236000`.
end::model-snapshot-id[]

tag::model-snapshot-retention-days[]
Advanced configuration option, which affects the automatic removal of old model
snapshots for this job. It specifies the maximum period of time (in days) that
snapshots are retained. This period is relative to the timestamp of the most
recent snapshot for this job. The default value is `10`, which means snapshots
ten days older than the newest snapshot are deleted. For more information, refer
to {ml-docs}/ml-ad-run-jobs.html#ml-ad-model-snapshots[Model snapshots].
end::model-snapshot-retention-days[]

tag::model-timestamp[]
The timestamp of the last record when the model stats were gathered.
end::model-timestamp[]

tag::multivariate-by-fields[]
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

end::multivariate-by-fields[]

tag::n-neighbors[]
Defines the value for how many nearest neighbors each method of {oldetection}
uses to calculate its {olscore}. When the value is not set, different values are
used for different ensemble members. This default behavior helps improve the
diversity in the ensemble; only override it if you are confident that the value
you choose is appropriate for the data set.
end::n-neighbors[]

tag::node-address[]
The network address of the node.
end::node-address[]

tag::node-attributes[]
Lists node attributes such as `ml.machine_memory` or `ml.max_open_jobs` settings.
end::node-attributes[]

tag::node-datafeeds[]
For started datafeeds only, this information pertains to the node upon which the
datafeed is started.
end::node-datafeeds[]

tag::node-ephemeral-id[]
The ephemeral ID of the node.
end::node-ephemeral-id[]

tag::node-id[]
The unique identifier of the node.
end::node-id[]

tag::node-jobs[]
Contains properties for the node that runs the job. This information is
available only for open jobs.
end::node-jobs[]

tag::node-transport-address[]
The host and port where transport HTTP connections are accepted.
end::node-transport-address[]

tag::open-time[]
For open jobs only, the elapsed time for which the job has been open.
end::open-time[]

tag::out-of-order-timestamp-count[]
The number of input documents that have a timestamp chronologically
preceding the start of the current anomaly detection bucket offset by
the latency window. This information is applicable only when you provide
data to the anomaly detection job by using the post data API.
These out of order documents are discarded, since jobs require time
series data to be in ascending chronological order.
end::out-of-order-timestamp-count[]

tag::outlier-fraction[]
The proportion of the data set that is assumed to be outlying prior to
{oldetection}. For example, 0.05 means it is assumed that 5% of values are real
outliers and 95% are inliers.
end::outlier-fraction[]

tag::over-field-name[]
The field used to split the data. In particular, this property is used for
analyzing the splits with respect to the history of all splits. It is used for
finding unusual values in the population of all splits. For more information,
see {ml-docs}/ml-configuring-populations.html[Performing population analysis].
end::over-field-name[]

tag::partition-field-name[]
The field used to segment the analysis. When you use this property, you have
completely independent baselines for each value of this field.
end::partition-field-name[]

tag::peak-model-bytes[]
The peak number of bytes of memory ever used by the models.
end::peak-model-bytes[]

tag::per-partition-categorization[]
Settings related to how categorization interacts with partition fields.
end::per-partition-categorization[]

tag::per-partition-categorization-enabled[]
To enable this setting, you must also set the partition_field_name property to
the same value in every detector that uses the keyword mlcategory. Otherwise,
job creation fails.
end::per-partition-categorization-enabled[]

tag::per-partition-categorization-stop-on-warn[]
This setting can be set to true only if per-partition categorization is enabled.
If true, both categorization and subsequent anomaly detection stops for
partitions where the categorization status changes to `warn`. This setting makes
it viable to have a job where it is expected that categorization works well for
some partitions but not others; you do not pay the cost of bad categorization
forever in the partitions where it works badly.
end::per-partition-categorization-stop-on-warn[]

tag::prediction-field-name[]
Defines the name of the prediction field in the results.
Defaults to `<dependent_variable>_prediction`.
end::prediction-field-name[]

tag::processed-field-count[]
The total number of fields in all the documents that have been processed by the
anomaly detection job. Only fields that are specified in the detector configuration
object contribute to this count. The timestamp is not included in this count.
end::processed-field-count[]

tag::processed-record-count[]
The number of input documents that have been processed by the anomaly detection job.
This value includes documents with missing fields, since they are nonetheless
analyzed. If you use datafeeds and have aggregations in your search query, the
`processed_record_count` is the number of aggregation results processed, not the
number of Elasticsearch documents.
end::processed-record-count[]

tag::randomize-seed[]
Defines the seed for the random generator that is used to pick training data. By
default, it is randomly generated. Set it to a specific value to use the same
training data each time you start a job (assuming other related parameters such
as `source` and `analyzed_fields` are the same).
end::randomize-seed[]

tag::query[]
The Elasticsearch query domain-specific language (DSL). This value corresponds to the
query object in an Elasticsearch search POST body. All the options that are supported by
Elasticsearch can be used, as this object is passed verbatim to Elasticsearch. By default, this
property has the following value: `{"match_all": {"boost": 1}}`.
end::query[]

tag::query-delay[]
The number of seconds behind real time that data is queried. For example, if
data from 10:04 a.m. might not be searchable in Elasticsearch until 10:06 a.m., set this
property to 120 seconds. The default value is randomly selected between `60s`
and `120s`. This randomness improves the query performance when there are
multiple jobs running on the same node. For more information, see
{ml-docs}/ml-delayed-data-detection.html[Handling delayed data].
end::query-delay[]

tag::rare-category-count[]
The number of categories that match just one categorized document.
end::rare-category-count[]

tag::renormalization-window-days[]
Advanced configuration option. The period over which adjustments to the score
are applied, as new data is seen. The default value is the longer of 30 days or
100 `bucket_spans`.
end::renormalization-window-days[]

tag::results-index-name[]
A text string that affects the name of the machine learning results index. The default value
is `shared`, which generates an index named `.ml-anomalies-shared`.
end::results-index-name[]

tag::results-retention-days[]
Advanced configuration option. The period of time (in days) that results are
retained. Age is calculated relative to the timestamp of the latest bucket
result. If this property has a non-null value, once per day at 00:30 (server
time), results that are the specified number of days older than the latest
bucket result are deleted from Elasticsearch. The default value is null, which means all
results are retained. Annotations generated by the system also count as results
for retention purposes; they are deleted after the same number of days as
results. Annotations added by users are retained forever.
end::results-retention-days[]

tag::retain[]
If `true`, this snapshot will not be deleted during automatic cleanup of
snapshots older than `model_snapshot_retention_days`. However, this snapshot
will be deleted when the job is deleted. The default value is `false`.
end::retain[]

tag::script-fields[]
Specifies scripts that evaluate custom expressions and returns script fields to
the datafeed. The detector configuration objects in a job can contain functions
that use these script fields. For more information, see
{ml-docs}/ml-configuring-transform.html[Transforming data with script fields]
and Script fields.
end::script-fields[]

tag::scroll-size[]
The `size` parameter that is used in Elasticsearch searches when the datafeed does not use
aggregations. The default value is `1000`. The maximum value is the value of
`index.max_result_window` which is 10,000 by default.
end::scroll-size[]

tag::search-bucket-avg[]
The average search time per bucket, in milliseconds.
end::search-bucket-avg[]

tag::search-count[]
The number of searches run by the datafeed.
end::search-count[]

tag::search-exp-avg-hour[]
The exponential average search time per hour, in milliseconds.
end::search-exp-avg-hour[]

tag::search-time[]
The total time the datafeed spent searching, in milliseconds.
end::search-time[]

tag::size[]
Specifies the maximum number of {dfanalytics-jobs} to obtain. The default value
is `100`.
end::size[]

tag::size-models[]
Specifies the maximum number of models to obtain. The default value
is `100`.
end::size-models[]

tag::snapshot-id[]
Identifier for the model snapshot.
end::snapshot-id[]

tag::sparse-bucket-count[]
The number of buckets that contained few data points compared to the expected
number of data points. If your data contains many sparse buckets, consider using
a longer `bucket_span`.
end::sparse-bucket-count[]

tag::standardization-enabled[]
If `true`, the following operation is performed on the columns before computing
outlier scores: (x_i - mean(x_i)) / sd(x_i). Defaults to `true`. For more
information about this concept, see
[Wikipedia](https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization)).
end::standardization-enabled[]

tag::state-anomaly-job[]
The status of the anomaly detection job, which can be one of the following values:
* `closed`: The job finished successfully with its model state persisted. The
