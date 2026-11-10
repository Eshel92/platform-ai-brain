<!-- Converted from ml/df-analytics/apis/put-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Create {dfanalytics-jobs} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Instantiates a {dfanalytics-job}.

## Request

`PUT _ml/data_frame/analytics/<data_frame_analytics_id>`

## Prerequisites

Requires the following privileges:

* cluster: `manage_ml` (the `machine_learning_admin` built-in role grants this
  privilege)
* source indices: `read`, `view_index_metadata`
* destination index: `read`, `create_index`, `manage` and `index`

**Note:** The {dfanalytics-job} remembers which roles the user who created it had at
the time of creation. When you start the job, it performs the analysis using
those same roles. If you provide
secondary authorization headers,
those credentials are used instead.

## Description

This API creates a {dfanalytics-job} that performs an analysis on the source
indices and stores the outcome in a destination index.

If the destination index does not exist, it is created automatically when you
start the job. See start-dfanalytics.

If you supply only a subset of the {regression} or {classification} parameters,
{ml-docs}/hyperparameters.html[hyperparameter optimization] occurs. It
determines a value for each of the undefined parameters.

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

`analysis`::
(Required, object)
The analysis configuration, which contains the information necessary to perform
one of the following types of analysis: {classification}, {oldetection}, or
{regression}.
**Properties of `analysis`**
`classification`:::
(Required^*^, object)
The configuration information necessary to perform
{ml-docs}/ml-dfa-classification.html[{classification}].
**Tip:** Advanced parameters are for fine-tuning {classanalysis}. They are set
automatically by hyperparameter optimization to give the minimum validation
error. It is highly recommended to use the default values unless you fully
understand the function of these parameters.
**Properties of `classification`**
=====
`alpha`::::
(Optional, double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This parameter affects loss calculations by acting as a multiplier of
the tree depth. Higher alpha values result in shallower trees and faster
training times. By default, this value is calculated during hyperparameter
optimization. It must be greater than or equal to zero.
`class_assignment_objective`::::
(Optional, string)
Defines the objective to optimize when assigning class labels:
`maximize_accuracy` or `maximize_minimum_recall`. When maximizing accuracy,
class labels are chosen to maximize the number of correct predictions. When
maximizing minimum recall, labels are chosen to maximize the minimum recall for
any class. Defaults to `maximize_minimum_recall`.
`dependent_variable`::::
(Required, string)
Defines which field of the document is to be predicted.
This parameter is supplied by field name and must match one of the fields in
the index being used to train. If this field is missing from a document, then
that document will not be used for training, but a prediction with the trained
model will be generated for it. It is also known as continuous target variable.
The data type of the field must be numeric (`integer`, `short`, `long`, `byte`),
categorical (`ip` or `keyword`), or boolean. There must be no more than 100
different values in this field.

`downsample_factor`::::
(Optional, double)
Advanced configuration option. Controls the fraction of data that is used to
compute the derivatives of the loss function for tree training. A small value
results in the use of a small fraction of the data. If this value is set to be
less than 1, accuracy typically improves. However, too small a value may result
in poor convergence for the ensemble and so require more trees. For more
information about shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Stochastic_gradient_boosting).
By default, this value is calculated during hyperparameter optimization. It
must be greater than zero and less than or equal to 1.
`early_stopping_enabled`::::
(Optional, Boolean)
Advanced configuration option.
Specifies whether the training process should finish if it is not finding any
better performing models. If disabled, the training process can take significantly
longer and the chance of finding a better performing model is unremarkable.
By default, early stoppping is enabled.
`eta`::::
(Optional, double)
Advanced configuration option. The shrinkage applied to the weights. Smaller
values result in larger forests which have a better generalization error.
However, larger forests cause slower training. For more information about
shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Shrinkage).
By default, this value is calculated during hyperparameter optimization. It must
be a value between 0.001 and 1.
`eta_growth_rate_per_tree`::::
(Optional, double)
Advanced configuration option. Specifies the rate at which `eta` increases for
each new tree that is added to the forest. For example, a rate of 1.05
increases `eta` by 5% for each extra tree. By default, this value is calculated
during hyperparameter optimization. It must be between 0.5 and 2.
`feature_bag_fraction`::::
(Optional, double)
Advanced configuration option. Defines the fraction of features that will be
used when selecting a random bag for each candidate split. By default, this
value is calculated during hyperparameter optimization.
`feature_processors`::::
(Optional, list)
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
**Properties of `feature_processors`**
======
`frequency_encoding`::::
(object)
The configuration information necessary to perform frequency encoding.
**Properties of `frequency_encoding`**
=======
`feature_name`::::
(Required, string)
The resulting feature name.
`field`::::
(Required, string)
The name of the field to encode.
`frequency_map`::::
(Required, object)
The resulting frequency map for the field value. If the field value is missing
from the `frequency_map`, the resulting value is `0`.
=======

`multi_encoding`::::
(object)
The configuration information necessary to perform multi encoding. It allows
multiple processors to be changed together. This way the output of a processor
can then be passed to another as an input.
**Properties of `multi_encoding`**
=======
`processors`::::
(Required, array)
The ordered array of custom processors to execute. Must be more than 1.
=======

`n_gram_encoding`::::
(object)
The configuration information necessary to perform n-gram encoding. Features
created by this encoder have the following name format:
`<feature_prefix>.<ngram><string position>`. For example, if the
`feature_prefix` is `f`, the feature name for the second unigram in a string is
`f.11`.
**Properties of `n_gram_encoding`**
=======
`feature_prefix`::::
(Optional, string)
The feature name prefix. Defaults to `ngram_<start>_<length>`.
`field`::::
(Required, string)
The name of the text field to encode.
`length`::::
(Optional, integer)
Specifies the length of the n-gram substring. Defaults to `50`. Must be greater
than `0`.
`n_grams`::::
(Required, array)
Specifies which n-grams to gather. It’s an array of integer values where the
minimum value is 1, and a maximum value is 5.
`start`::::
(Optional, integer)
Specifies the zero-indexed start of the n-gram substring. Negative values are
allowed for encoding n-grams of string suffixes. Defaults to `0`.
=======

`one_hot_encoding`::::
(object)
The configuration information necessary to perform one hot encoding.
**Properties of `one_hot_encoding`**
=======
`field`::::
(Required, string)
The name of the field to encode.
`hot_map`::::
(Required, string)
The one hot map mapping the field value with the column name.
=======

`target_mean_encoding`::::
(object)
The configuration information necessary to perform target mean encoding.
**Properties of `target_mean_encoding`**
=======
`default_value`::::
(Required, integer)
The default value if field value is not found in the `target_map`.
`feature_name`::::
(Required, string)
The resulting feature name.
`field`::::
(Required, string)
The name of the field to encode.
`target_map`::::
(Required, object)
The field value to target mean transition map.
=======

======

`gamma`::::
(Optional, double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies a linear penalty associated with the size
of individual trees in the forest. A high gamma value causes training to prefer
small trees. A small gamma value results in larger individual trees and slower
training. By default, this value is calculated during hyperparameter
optimization. It must be a nonnegative value.
`lambda`::::
(Optional, double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies an L2 regularization term which applies to
leaf weights of the individual trees in the forest. A high lambda value causes
training to favor small leaf weights. This behavior makes the prediction
function smoother at the expense of potentially not being able to capture
relevant relationships between the features and the {depvar}. A small lambda
value results in large individual trees and slower training. By default, this
value is calculated during hyperparameter optimization. It must be a nonnegative
value.
`max_optimization_rounds_per_hyperparameter`::::
(Optional, integer)
Advanced configuration option.
A multiplier responsible for determining the maximum number of
hyperparameter optimization steps in the Bayesian optimization procedure.
The maximum number of steps is determined based on the number of undefined
hyperparameters times the maximum optimization rounds per hyperparameter.
By default, this value is calculated during hyperparameter optimization.
`max_trees`::::
(Optional, integer)
Advanced configuration option. Defines the maximum number of decision trees in
the forest. The maximum value is 2000. By default, this value is calculated
during hyperparameter optimization.
`num_top_classes`::::
(Optional, integer)
Defines the number of categories for which the predicted probabilities are
reported. It must be non-negative or -1. If it is -1 or greater than the total
number of categories, probabilities are reported for all categories; if you have
a large number of categories, there could be a significant effect on the size of your destination index. Defaults to 2.
**Note:** To use the
{ml-docs}/ml-dfa-classification.html#ml-dfanalytics-class-aucroc[AUC ROC]
evaluation method, `num_top_classes` must be set to `-1` or a value greater than
or equal to the total number of categories.

`num_top_feature_importance_values`::::
(Optional, integer)
Advanced configuration option. Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document to return.
By default, it is zero and no {feat-imp} calculation occurs.

`prediction_field_name`::::
(Optional, string)
Defines the name of the prediction field in the results.
Defaults to `<dependent_variable>_prediction`.
`randomize_seed`::::
(Optional, long)
Defines the seed for the random generator that is used to pick training data. By
default, it is randomly generated. Set it to a specific value to use the same
training data each time you start a job (assuming other related parameters such
as `source` and `analyzed_fields` are the same).
`soft_tree_depth_limit`::::
(Optional, double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This soft limit combines with the `soft_tree_depth_tolerance` to
penalize trees that exceed the specified depth; the regularized loss increases
quickly beyond this depth. By default, this value is calculated during
hyperparameter optimization. It must be greater than or equal to 0.
`soft_tree_depth_tolerance`::::
(Optional, double)
Advanced configuration option. This option controls how quickly the regularized
loss increases when the tree depth exceeds `soft_tree_depth_limit`. By default,
this value is calculated during hyperparameter optimization. It must be greater
than or equal to 0.01.
`training_percent`::::
(Optional, integer)
Defines what percentage of the eligible documents that will
be used for training. Documents that are ignored by the analysis (for example
those that contain arrays with more than one value) won’t be included in the
calculation for used percentage. Defaults to `100`.
=====
`outlier_detection`:::
(Required^*^, object)
The configuration information necessary to perform
{ml-docs}/ml-dfa-finding-outliers.html[{oldetection}]:
**Properties of `outlier_detection`**
=====
`compute_feature_influence`::::
(Optional, Boolean)
Specifies whether the feature influence calculation is enabled. Defaults to
`true`.
`feature_influence_threshold`::::
(Optional, double)
The minimum {olscore} that a document needs to have in order to calculate its
{fiscore}. Value range: 0-1 (`0.1` by default).
`method`::::
(Optional, string)
The method that {oldetection} uses. Available methods are `lof`, `ldof`,
`distance_kth_nn`, `distance_knn`, and `ensemble`. The default value is
`ensemble`, which means that {oldetection} uses an ensemble of different methods
and normalises and combines their individual {olscores} to obtain the overall
{olscore}.
`n_neighbors`::::
(Optional, integer)
Defines the value for how many nearest neighbors each method of {oldetection}
uses to calculate its {olscore}. When the value is not set, different values are
used for different ensemble members. This default behavior helps improve the
diversity in the ensemble; only override it if you are confident that the value
you choose is appropriate for the data set.
`outlier_fraction`::::
(Optional, double)
The proportion of the data set that is assumed to be outlying prior to
{oldetection}. For example, 0.05 means it is assumed that 5% of values are real
outliers and 95% are inliers.
`standardization_enabled`::::
(Optional, Boolean)
If `true`, the following operation is performed on the columns before computing
outlier scores: (x_i - mean(x_i)) / sd(x_i). Defaults to `true`. For more
information about this concept, see
[Wikipedia](https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization)).
=====
`regression`:::
(Required^*^, object)
The configuration information necessary to perform
{ml-docs}/ml-dfa-regression.html[{regression}].
**Tip:** Advanced parameters are for fine-tuning {reganalysis}. They are set
automatically by hyperparameter optimization to give the minimum validation
error. It is highly recommended to use the default values unless you fully
understand the function of these parameters.
**Properties of `regression`**
=====
`alpha`::::
(Optional, double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This parameter affects loss calculations by acting as a multiplier of
the tree depth. Higher alpha values result in shallower trees and faster
training times. By default, this value is calculated during hyperparameter
optimization. It must be greater than or equal to zero.
`dependent_variable`::::
(Required, string)
Defines which field of the document is to be predicted.
This parameter is supplied by field name and must match one of the fields in
the index being used to train. If this field is missing from a document, then
that document will not be used for training, but a prediction with the trained
model will be generated for it. It is also known as continuous target variable.
The data type of the field must be numeric.

`downsample_factor`::::
(Optional, double)
Advanced configuration option. Controls the fraction of data that is used to
compute the derivatives of the loss function for tree training. A small value
results in the use of a small fraction of the data. If this value is set to be
less than 1, accuracy typically improves. However, too small a value may result
in poor convergence for the ensemble and so require more trees. For more
information about shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Stochastic_gradient_boosting).
By default, this value is calculated during hyperparameter optimization. It
must be greater than zero and less than or equal to 1.
`early_stopping_enabled`::::
(Optional, Boolean)
Advanced configuration option.
Specifies whether the training process should finish if it is not finding any
better performing models. If disabled, the training process can take significantly
longer and the chance of finding a better performing model is unremarkable.
By default, early stoppping is enabled.
`eta`::::
(Optional, double)
Advanced configuration option. The shrinkage applied to the weights. Smaller
values result in larger forests which have a better generalization error.
However, larger forests cause slower training. For more information about
shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Shrinkage).
By default, this value is calculated during hyperparameter optimization. It must
be a value between 0.001 and 1.
`eta_growth_rate_per_tree`::::
(Optional, double)
Advanced configuration option. Specifies the rate at which `eta` increases for
each new tree that is added to the forest. For example, a rate of 1.05
increases `eta` by 5% for each extra tree. By default, this value is calculated
during hyperparameter optimization. It must be between 0.5 and 2.
`feature_bag_fraction`::::
(Optional, double)
Advanced configuration option. Defines the fraction of features that will be
used when selecting a random bag for each candidate split. By default, this
value is calculated during hyperparameter optimization.
`feature_processors`::::
(Optional, list)
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
`gamma`::::
(Optional, double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies a linear penalty associated with the size
of individual trees in the forest. A high gamma value causes training to prefer
small trees. A small gamma value results in larger individual trees and slower
training. By default, this value is calculated during hyperparameter
optimization. It must be a nonnegative value.
`lambda`::::
(Optional, double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies an L2 regularization term which applies to
leaf weights of the individual trees in the forest. A high lambda value causes
training to favor small leaf weights. This behavior makes the prediction
function smoother at the expense of potentially not being able to capture
relevant relationships between the features and the {depvar}. A small lambda
value results in large individual trees and slower training. By default, this
value is calculated during hyperparameter optimization. It must be a nonnegative
value.
`loss_function`::::
(Optional, string)
The loss function used during {regression}. Available options are `mse` (mean
squared error), `msle` (mean squared logarithmic error),  `huber` (Pseudo-Huber
loss). Defaults to `mse`.
Refer to
{ml-docs}/dfa-regression-lossfunction.html[Loss functions for {regression} analyses]
to learn more.

`loss_function_parameter`::::
(Optional, double)
A positive number that is used as a parameter to the `loss_function`.

`max_optimization_rounds_per_hyperparameter`::::
(Optional, integer)
Advanced configuration option.
A multiplier responsible for determining the maximum number of
hyperparameter optimization steps in the Bayesian optimization procedure.
The maximum number of steps is determined based on the number of undefined
hyperparameters times the maximum optimization rounds per hyperparameter.
By default, this value is calculated during hyperparameter optimization.
`max_trees`::::
(Optional, integer)
Advanced configuration option. Defines the maximum number of decision trees in
the forest. The maximum value is 2000. By default, this value is calculated
during hyperparameter optimization.
`num_top_feature_importance_values`::::
(Optional, integer)
Advanced configuration option. Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document to return.
By default, it is zero and no {feat-imp} calculation occurs.

`prediction_field_name`::::
(Optional, string)
Defines the name of the prediction field in the results.
Defaults to `<dependent_variable>_prediction`.
`randomize_seed`::::
(Optional, long)
Defines the seed for the random generator that is used to pick training data. By
default, it is randomly generated. Set it to a specific value to use the same
training data each time you start a job (assuming other related parameters such
as `source` and `analyzed_fields` are the same).
`soft_tree_depth_limit`::::
(Optional, double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This soft limit combines with the `soft_tree_depth_tolerance` to
penalize trees that exceed the specified depth; the regularized loss increases
quickly beyond this depth. By default, this value is calculated during
hyperparameter optimization. It must be greater than or equal to 0.
`soft_tree_depth_tolerance`::::
(Optional, double)
Advanced configuration option. This option controls how quickly the regularized
loss increases when the tree depth exceeds `soft_tree_depth_limit`. By default,
this value is calculated during hyperparameter optimization. It must be greater
than or equal to 0.01.
`training_percent`::::
(Optional, integer)
Defines what percentage of the eligible documents that will
be used for training. Documents that are ignored by the analysis (for example
those that contain arrays with more than one value) won’t be included in the
calculation for used percentage. Defaults to `100`.
=====

`analyzed_fields`::
(Optional, object)
Specify `includes` and/or `excludes` patterns to select which fields will be
included in the analysis. The patterns specified in `excludes` are applied last,
therefore `excludes` takes precedence. In other words, if the same field is
specified in both `includes` and `excludes`, then the field will not be included
in the analysis.
The supported fields for each type of analysis are as follows:

* {oldetection-cap} requires numeric or boolean data to analyze. The algorithms
don't support missing values therefore fields that have data types other than
numeric or boolean are ignored. Documents where included fields contain missing
values, null values, or an array are also ignored. Therefore the `dest` index
may contain documents that don't have an {olscore}.
* {regression-cap} supports fields that are numeric, `boolean`, `text`,
`keyword`, and `ip`. It is also tolerant of missing values. Fields that are
supported are included in the analysis, other fields are ignored. Documents
where included fields contain an array with two or more values are also
ignored. Documents in the `dest` index that don’t contain a results field are
not included in the {reganalysis}.
* {classification-cap} supports fields that are numeric, `boolean`, `text`,
`keyword`, and `ip`. It is also tolerant of missing values. Fields that are
supported are included in the analysis, other fields are ignored. Documents
where included fields contain an array with two or more values are also ignored.
Documents in the `dest` index that don’t contain a results field are not
included in the {classanalysis}. {classanalysis-cap} can be improved by mapping
ordinal variable values to a single number. For example, in case of age ranges,
you can model the values as "0-14" = 0, "15-24" = 1, "25-34" = 2, and so on.

If `analyzed_fields` is not set, only the relevant fields will be included. For
example, all the numeric fields for {oldetection}. For more information about
field selection, see explain-dfanalytics.
**Properties of `analyzed_fields`**
`excludes`:::
(Optional, array)
An array of strings that defines the fields that will be excluded from the
analysis. You do not need to add fields with unsupported data types to
`excludes`, these fields are excluded from the analysis automatically.

`includes`:::
(Optional, array)
An array of strings that defines the fields that will be included in the
analysis.

`description`::
(Optional, string)
A description of the job.
`dest`::
(Required, object)
The destination configuration, consisting of `index` and optionally
`results_field` (`ml` by default).
**Properties of `dest`**
`index`:::
(Required, string) Defines the _destination index_ to store the results of the
{dfanalytics-job}.

`results_field`:::
(Optional, string) Defines the name of the field in which to store the results
of the analysis. Defaults to `ml`.
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
`source`::
(object)
The configuration of how to source the analysis data. It requires an `index`.
Optionally, `query`, `runtime_mappings`, and `_source` may be specified.
**Properties of `source`**
`index`:::
(Required, string or array) Index or indices on which to perform the analysis.
It can be a single index or index pattern as well as an array of indices or
patterns.
**Warning:** If your source indices contain documents with the same IDs, only the
document that is indexed last appears in the destination index.

`query`:::
(Optional, object) The Elasticsearch query domain-specific language (DSL).
This value corresponds to the query object in an Elasticsearch search POST body. All the
options that are supported by Elasticsearch can be used, as this object is passed
verbatim to Elasticsearch. By default, this property has the following value:
`{"match_all": {}}`.

`runtime_mappings`:::
(Optional, object) Definitions of runtime fields that will become part of the
mapping of the destination index.

`_source`:::
(Optional, object) Specify `includes` and/or `excludes` patterns to select which
fields will be present in the destination. Fields that are excluded cannot be
included in the analysis.
**Properties of `_source`**
=====
`includes`::::
(array) An array of strings that defines the fields that will be included in the
destination.

`excludes`::::
(array) An array of strings that defines the fields that will be excluded from
the destination.
=====

## Examples

### Preprocessing actions example

The following example shows how to limit the scope of the analysis to certain
fields, specify excluded fields in the destination index, and use a query to
filter your data before analysis.

```console
PUT _ml/data_frame/analytics/model-flight-delays-pre
{
  "source": {
    "index": [
      "kibana_sample_data_flights" <1>
    ],
    "query": { <2>
      "range": {
        "DistanceKilometers": {
          "gt": 0
        }
      }
    },
    "_source": { <3>
      "includes": [],
      "excludes": [
        "FlightDelay",
        "FlightDelayType"
      ]
    }
  },
  "dest": { <4>
    "index": "df-flight-delays",
    "results_field": "ml-results"
  },
  "analysis": {
  "regression": {
    "dependent_variable": "FlightDelayMin",
    "training_percent": 90
    }
  },
  "analyzed_fields": { <5>
    "includes": [],
    "excludes": [
      "FlightNum"
    ]
  },
  "model_memory_limit": "100mb"
}
```

<1> Source index to analyze.
<2> This query filters out entire documents that will not be present in the
destination index.
<3> The `_source` object defines fields in the data set that will be included or
excluded in the destination index.
<4> Defines the destination index that contains the results of the analysis and
the fields of the source index specified in the `_source` object. Also defines
the name of the `results_field`.
<5> Specifies fields to be included in or excluded from the analysis. This does
not affect whether the fields will be present in the destination index, only
affects whether they are used in the analysis.

In this example, we can see that all the fields of the source index are included
in the destination index except `FlightDelay` and `FlightDelayType` because
these are defined as excluded fields by the `excludes` parameter of the
`_source` object. The `FlightNum` field is included in the destination index,
however it is not included in the analysis because it is explicitly specified as
excluded field by the `excludes` parameter of the `analyzed_fields` object.

### {oldetection-cap} example

The following example creates the `loganalytics` {dfanalytics-job}, the analysis
type is `outlier_detection`:

```console
PUT _ml/data_frame/analytics/loganalytics
{
  "description": "Outlier detection on log data",
  "source": {
    "index": "logdata"
  },
  "dest": {
    "index": "logdata_out"
  },
  "analysis": {
    "outlier_detection": {
      "compute_feature_influence": true,
      "outlier_fraction": 0.05,
      "standardization_enabled": true
    }
  }
}
```

The API returns the following result:

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
  "model_memory_limit" : "1gb",
  "allow_lazy_start" : false,
  "max_num_threads" : 1
}

```

### {regression-cap} examples

The following example creates the `house_price_regression_analysis`
{dfanalytics-job}, the analysis type is `regression`:

```console
PUT _ml/data_frame/analytics/house_price_regression_analysis
{
  "source": {
    "index": "houses_sold_last_10_yrs"
  },
  "dest": {
    "index": "house_price_predictions"
  },
  "analysis":
    {
      "regression": {
        "dependent_variable": "price"
      }
    }
}
```

The API returns the following result:

```console-result
{
  "id" : "house_price_regression_analysis",
  "create_time" : 1656364845151,
  "version" : "8.4.0",
  "authorization" : {
    "roles" : [
      "superuser"
    ]
  },
  "source" : {
    "index" : [
      "houses_sold_last_10_yrs"
    ],
    "query" : {
      "match_all" : { }
    }
  },
  "dest" : {
    "index" : "house_price_predictions",
    "results_field" : "ml"
  },
  "analysis" : {
    "regression" : {
      "dependent_variable" : "price",
      "prediction_field_name" : "price_prediction",
      "training_percent" : 100.0,
      "randomize_seed" : -3578554885299300212,
      "loss_function" : "mse",
      "early_stopping_enabled" : true
    }
  },
  "model_memory_limit" : "1gb",
  "allow_lazy_start" : false,
  "max_num_threads" : 1
}

```

The following example creates a job and specifies a training percent:

```console
PUT _ml/data_frame/analytics/student_performance_mathematics_0.3
{
 "source": {
   "index": "student_performance_mathematics"
 },
 "dest": {
   "index":"student_performance_mathematics_reg"
 },
 "analysis":
   {
     "regression": {
       "dependent_variable": "G3",
       "training_percent": 70,  <1>
       "randomize_seed": 19673948271  <2>
     }
   }
}
```

<1> The percentage of the data set that is used for training the model.
<2> The seed that is used to randomly pick which data is used for training.

The following example uses custom feature processors to transform the
categorical values for `DestWeather` into numerical values using one-hot,
target-mean, and frequency encoding techniques:

```console
PUT _ml/data_frame/analytics/flight_prices
{
  "source": {
    "index": [
      "kibana_sample_data_flights"
    ]
  },
  "dest": {
    "index": "kibana_sample_flight_prices"
  },
  "analysis": {
    "regression": {
      "dependent_variable": "AvgTicketPrice",
      "num_top_feature_importance_values": 2,
      "feature_processors": [
        {
          "frequency_encoding": {
            "field": "DestWeather",
            "feature_name": "DestWeather_frequency",
            "frequency_map": {
              "Rain": 0.14604811155570188,
              "Heavy Fog": 0.14604811155570188,
              "Thunder & Lightning": 0.14604811155570188,
              "Cloudy": 0.14604811155570188,
              "Damaging Wind": 0.14604811155570188,
              "Hail": 0.14604811155570188,
              "Sunny": 0.14604811155570188,
              "Clear": 0.14604811155570188
            }
          }
        },
        {
          "target_mean_encoding": {
            "field": "DestWeather",
            "feature_name": "DestWeather_targetmean",
            "target_map": {
              "Rain": 626.5588814585794,
              "Heavy Fog": 626.5588814585794,
              "Thunder & Lightning": 626.5588814585794,
              "Hail": 626.5588814585794,
              "Damaging Wind": 626.5588814585794,
              "Cloudy": 626.5588814585794,
              "Clear": 626.5588814585794,
              "Sunny": 626.5588814585794
            },
            "default_value": 624.0249512020454
          }
        },
        {
          "one_hot_encoding": {
            "field": "DestWeather",
            "hot_map": {
              "Rain": "DestWeather_Rain",
              "Heavy Fog": "DestWeather_Heavy Fog",
              "Thunder & Lightning": "DestWeather_Thunder & Lightning",
              "Cloudy": "DestWeather_Cloudy",
              "Damaging Wind": "DestWeather_Damaging Wind",
              "Hail": "DestWeather_Hail",
              "Clear": "DestWeather_Clear",
              "Sunny": "DestWeather_Sunny"
            }
          }
        }
      ]
    }
  },
  "analyzed_fields": {
    "includes": [
      "AvgTicketPrice",
      "Cancelled",
      "DestWeather",
      "FlightDelayMin",
      "DistanceMiles"
    ]
  },
  "model_memory_limit": "30mb"
}
```

**Note:** These custom feature processors are optional; automatic
{ml-docs}/ml-feature-encoding.html[feature encoding] still occurs for all
categorical features.

### {classification-cap} example

The following example creates the `loan_classification` {dfanalytics-job}, the
analysis type is `classification`:

```console
PUT _ml/data_frame/analytics/loan_classification
{
  "source" : {
    "index": "loan-applicants"
  },
  "dest" : {
    "index": "loan-applicants-classified"
  },
  "analysis" : {
    "classification": {
      "dependent_variable": "label",
      "training_percent": 75,
      "num_top_classes": 2
    }
  }
}
```
