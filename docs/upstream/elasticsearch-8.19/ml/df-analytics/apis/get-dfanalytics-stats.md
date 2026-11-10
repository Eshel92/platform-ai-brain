<!-- Converted from ml/df-analytics/apis/get-dfanalytics-stats.asciidoc (AsciiDoc). Includes are inlined. -->

# Get {dfanalytics-jobs} statistics API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Retrieves usage information for {dfanalytics-jobs}.

## Request

`GET _ml/data_frame/analytics/<data_frame_analytics_id>/_stats` +

`GET _ml/data_frame/analytics/<data_frame_analytics_id>,<data_frame_analytics_id>/_stats` +

`GET _ml/data_frame/analytics/_stats` +

`GET _ml/data_frame/analytics/_all/_stats` +

`GET _ml/data_frame/analytics/*/_stats`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.

## Path parameters

`<data_frame_analytics_id>`::
(Optional, string)
Identifier for the {dfanalytics-job}. If you do not specify this option, the API
returns information for the first hundred {dfanalytics-jobs}.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
 Specifies what to do when the request:
* Contains wildcard expressions and there are no {dfanalytics-jobs} that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `data_frame_analytics` array
when there are no matches and the subset of results when there are partial
matches. If this parameter is `false`, the request returns a `404` status code
when there are no matches or only partial matches.
`from`::
(Optional, integer) 
Skips the specified number of {dfanalytics-jobs}. The default value is `0`.
`size`::
(Optional, integer) 
Specifies the maximum number of {dfanalytics-jobs} to obtain. The default value
is `100`.
`verbose`::
(Optional, Boolean)
Defines whether the stats response should be verbose. The default value is `false`.

## Response body

`data_frame_analytics`::
(array)
An array of objects that contain usage information for {dfanalytics-jobs}, which
are sorted by the `id` value in ascending order.
**Properties of {dfanalytics-job} usage resources**
`analysis_stats`:::
(object)
An object containing information about the analysis job.
**Properties of `analysis_stats`**
=====
`classification_stats`::::
(object)
An object containing information about the {classanalysis} job.
**Properties of `classification_stats`**
======
`hyperparameters`::::
(object)
An object containing the parameters of the {classanalysis} job.
**Properties of `hyperparameters`**
=======
`alpha`::::
(double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This parameter affects loss calculations by acting as a multiplier of
the tree depth. Higher alpha values result in shallower trees and faster
training times. By default, this value is calculated during hyperparameter
optimization. It must be greater than or equal to zero.
`class_assignment_objective`::::
(string)
Defines the objective to optimize when assigning class labels:
`maximize_accuracy` or `maximize_minimum_recall`. When maximizing accuracy,
class labels are chosen to maximize the number of correct predictions. When
maximizing minimum recall, labels are chosen to maximize the minimum recall for
any class. Defaults to `maximize_minimum_recall`.
`downsample_factor`::::
(double)
Advanced configuration option. Controls the fraction of data that is used to
compute the derivatives of the loss function for tree training. A small value
results in the use of a small fraction of the data. If this value is set to be
less than 1, accuracy typically improves. However, too small a value may result
in poor convergence for the ensemble and so require more trees. For more
information about shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Stochastic_gradient_boosting).
By default, this value is calculated during hyperparameter optimization. It
must be greater than zero and less than or equal to 1.
`eta`::::
(double)
Advanced configuration option. The shrinkage applied to the weights. Smaller
values result in larger forests which have a better generalization error.
However, larger forests cause slower training. For more information about
shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Shrinkage).
By default, this value is calculated during hyperparameter optimization. It must
be a value between 0.001 and 1.
`eta_growth_rate_per_tree`::::
(double)
Advanced configuration option. Specifies the rate at which `eta` increases for
each new tree that is added to the forest. For example, a rate of 1.05
increases `eta` by 5% for each extra tree. By default, this value is calculated
during hyperparameter optimization. It must be between 0.5 and 2.
`feature_bag_fraction`::::
(double)
Advanced configuration option. Defines the fraction of features that will be
used when selecting a random bag for each candidate split. By default, this
value is calculated during hyperparameter optimization.
`gamma`::::
(double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies a linear penalty associated with the size
of individual trees in the forest. A high gamma value causes training to prefer
small trees. A small gamma value results in larger individual trees and slower
training. By default, this value is calculated during hyperparameter
optimization. It must be a nonnegative value.
`lambda`::::
(double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies an L2 regularization term which applies to
leaf weights of the individual trees in the forest. A high lambda value causes
training to favor small leaf weights. This behavior makes the prediction
function smoother at the expense of potentially not being able to capture
relevant relationships between the features and the {depvar}. A small lambda
value results in large individual trees and slower training. By default, this
value is calculated during hyperparameter optimization. It must be a nonnegative
value.
`max_attempts_to_add_tree`::::
(integer)
If the algorithm fails to determine a non-trivial tree (more than a single
leaf), this parameter determines how many of such consecutive failures are
tolerated. Once the number of attempts exceeds the threshold, the forest
training stops.
`max_optimization_rounds_per_hyperparameter`::::
(integer)
Advanced configuration option.
A multiplier responsible for determining the maximum number of
hyperparameter optimization steps in the Bayesian optimization procedure.
The maximum number of steps is determined based on the number of undefined
hyperparameters times the maximum optimization rounds per hyperparameter.
By default, this value is calculated during hyperparameter optimization.
`max_trees`::::
(integer)
Advanced configuration option. Defines the maximum number of decision trees in
the forest. The maximum value is 2000. By default, this value is calculated
during hyperparameter optimization.
`num_folds`::::
(integer)
The maximum number of folds for the cross-validation procedure.
`num_splits_per_feature`::::
(integer)
Determines the maximum number of splits for every feature that can occur in a
decision tree when the tree is trained.
`soft_tree_depth_limit`::::
(double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This soft limit combines with the `soft_tree_depth_tolerance` to
penalize trees that exceed the specified depth; the regularized loss increases
quickly beyond this depth. By default, this value is calculated during
hyperparameter optimization. It must be greater than or equal to 0.
`soft_tree_depth_tolerance`::::
(double)
Advanced configuration option. This option controls how quickly the regularized
loss increases when the tree depth exceeds `soft_tree_depth_limit`. By default,
this value is calculated during hyperparameter optimization. It must be greater
than or equal to 0.01.
=======

`iteration`::::
(integer)
The number of iterations on the analysis.
`timestamp`::::
(date)
The timestamp when the statistics were reported in milliseconds since the epoch.
`timing_stats`::::
(object)
An object containing time statistics about the {dfanalytics-job}.
**Properties of `timing_stats`**
=======
`elapsed_time`::::
(integer)
Runtime of the analysis in milliseconds.
`iteration_time`::::
(integer)
Runtime of the latest iteration of the analysis in milliseconds.
=======

`validation_loss`::::
(object)
An object containing information about validation loss.
**Properties of `validation_loss`**
=======
`fold_values`::::
Validation loss values for every added decision tree during the forest growing
procedure.
`loss_type`::::
(string)
The type of the loss metric. For example, `binomial_logistic`.
=======
======

`outlier_detection_stats`::::
(object)
An object containing information about the {oldetection} job.
**Properties of `outlier_detection_stats`**
======
`parameters`::::
(object)
The list of job parameters specified by the user or determined by algorithmic 
heuristics.
**Properties of `parameters`**
=======
`compute_feature_influence`::::
(Boolean)
Specifies whether the feature influence calculation is enabled. Defaults to
`true`.
`feature_influence_threshold`::::
(double)
The minimum {olscore} that a document needs to have in order to calculate its
{fiscore}. Value range: 0-1 (`0.1` by default).
`method`::::
(string)
The method that {oldetection} uses. Available methods are `lof`, `ldof`,
`distance_kth_nn`, `distance_knn`, and `ensemble`. The default value is
`ensemble`, which means that {oldetection} uses an ensemble of different methods
and normalises and combines their individual {olscores} to obtain the overall
{olscore}.
`n_neighbors`::::
(integer)
Defines the value for how many nearest neighbors each method of {oldetection}
uses to calculate its {olscore}. When the value is not set, different values are
used for different ensemble members. This default behavior helps improve the
diversity in the ensemble; only override it if you are confident that the value
you choose is appropriate for the data set.
`outlier_fraction`::::
(double)
The proportion of the data set that is assumed to be outlying prior to
{oldetection}. For example, 0.05 means it is assumed that 5% of values are real
outliers and 95% are inliers.
`standardization_enabled`::::
(Boolean)
If `true`, the following operation is performed on the columns before computing
outlier scores: (x_i - mean(x_i)) / sd(x_i). Defaults to `true`. For more
information about this concept, see
[Wikipedia](https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization)).
=======

`timestamp`::::
(date)
The timestamp when the statistics were reported in milliseconds since the epoch.
`timing_stats`::::
(object)
An object containing time statistics about the {dfanalytics-job}.
**Property of `timing_stats`**
=======
`elapsed_time`::::
(integer)
Runtime of the analysis in milliseconds.
=======
======

`regression_stats`::::
(object)
An object containing information about the {reganalysis} job.
**Properties of `regression_stats`**
======
`hyperparameters`::::
(object)
An object containing the parameters of the {reganalysis} job.
**Properties of `hyperparameters`**
=======
`alpha`::::
(double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This parameter affects loss calculations by acting as a multiplier of
the tree depth. Higher alpha values result in shallower trees and faster
training times. By default, this value is calculated during hyperparameter
optimization. It must be greater than or equal to zero.
`downsample_factor`::::
(double)
Advanced configuration option. Controls the fraction of data that is used to
compute the derivatives of the loss function for tree training. A small value
results in the use of a small fraction of the data. If this value is set to be
less than 1, accuracy typically improves. However, too small a value may result
in poor convergence for the ensemble and so require more trees. For more
information about shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Stochastic_gradient_boosting).
By default, this value is calculated during hyperparameter optimization. It
must be greater than zero and less than or equal to 1.
`eta`::::
(double)
Advanced configuration option. The shrinkage applied to the weights. Smaller
values result in larger forests which have a better generalization error.
However, larger forests cause slower training. For more information about
shrinkage, refer to
[this wiki article](https://en.wikipedia.org/wiki/Gradient_boosting#Shrinkage).
By default, this value is calculated during hyperparameter optimization. It must
be a value between 0.001 and 1.
`eta_growth_rate_per_tree`::::
(double)
Advanced configuration option. Specifies the rate at which `eta` increases for
each new tree that is added to the forest. For example, a rate of 1.05
increases `eta` by 5% for each extra tree. By default, this value is calculated
during hyperparameter optimization. It must be between 0.5 and 2.
`feature_bag_fraction`::::
(double)
Advanced configuration option. Defines the fraction of features that will be
used when selecting a random bag for each candidate split. By default, this
value is calculated during hyperparameter optimization.
`gamma`::::
(double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies a linear penalty associated with the size
of individual trees in the forest. A high gamma value causes training to prefer
small trees. A small gamma value results in larger individual trees and slower
training. By default, this value is calculated during hyperparameter
optimization. It must be a nonnegative value.
`lambda`::::
(double)
Advanced configuration option. Regularization parameter to prevent overfitting
on the training data set. Multiplies an L2 regularization term which applies to
leaf weights of the individual trees in the forest. A high lambda value causes
training to favor small leaf weights. This behavior makes the prediction
function smoother at the expense of potentially not being able to capture
relevant relationships between the features and the {depvar}. A small lambda
value results in large individual trees and slower training. By default, this
value is calculated during hyperparameter optimization. It must be a nonnegative
value.
`max_attempts_to_add_tree`::::
(integer)
If the algorithm fails to determine a non-trivial tree (more than a single
leaf), this parameter determines how many of such consecutive failures are
tolerated. Once the number of attempts exceeds the threshold, the forest
training stops.
`max_optimization_rounds_per_hyperparameter`::::
(integer)
Advanced configuration option.
A multiplier responsible for determining the maximum number of
hyperparameter optimization steps in the Bayesian optimization procedure.
The maximum number of steps is determined based on the number of undefined
hyperparameters times the maximum optimization rounds per hyperparameter.
By default, this value is calculated during hyperparameter optimization.
`max_trees`::::
(integer)
Advanced configuration option. Defines the maximum number of decision trees in
the forest. The maximum value is 2000. By default, this value is calculated
during hyperparameter optimization.
`num_folds`::::
(integer)
The maximum number of folds for the cross-validation procedure.
`num_splits_per_feature`::::
(integer)
Determines the maximum number of splits for every feature that can occur in a
decision tree when the tree is trained.
`soft_tree_depth_limit`::::
(double)
Advanced configuration option. Machine learning uses loss guided tree growing, which
means that the decision trees grow where the regularized loss decreases most
quickly. This soft limit combines with the `soft_tree_depth_tolerance` to
penalize trees that exceed the specified depth; the regularized loss increases
quickly beyond this depth. By default, this value is calculated during
hyperparameter optimization. It must be greater than or equal to 0.
`soft_tree_depth_tolerance`::::
(double)
Advanced configuration option. This option controls how quickly the regularized
loss increases when the tree depth exceeds `soft_tree_depth_limit`. By default,
this value is calculated during hyperparameter optimization. It must be greater
than or equal to 0.01.
=======

`iteration`::::
(integer)
The number of iterations on the analysis.
`timestamp`::::
(date)
The timestamp when the statistics were reported in milliseconds since the epoch.
`timing_stats`::::
(object)
An object containing time statistics about the {dfanalytics-job}.
**Propertis of `timing_stats`**
=======
`elapsed_time`::::
(integer)
Runtime of the analysis in milliseconds.
`iteration_time`::::
(integer)
Runtime of the latest iteration of the analysis in milliseconds.
=======

`validation_loss`::::
(object)
An object containing information about validation loss.
**Properties of `validation_loss`**
=======
`fold_values`::::
(array of strings)
Validation loss values for every added decision tree during the forest growing
procedure.
`loss_type`::::
(string)
The type of the loss metric. For example, `binomial_logistic`.
=======
======
=====

`assignment_explanation`:::
(string)
For running jobs only, contains messages relating to the selection of a node to 
run the job.

`data_counts`:::
(object)
An object that provides counts for the quantity of documents skipped, used in
training, or available for testing.
**Properties of `data_counts`**
=====
`skipped_docs_count`::::
(integer)
The number of documents that are skipped during the analysis because they 
contained values that are not supported by the analysis. For example, 
{oldetection} does not support missing fields so it skips documents with missing 
fields. Likewise, all types of analysis skip documents that contain arrays with 
more than one element.

`test_docs_count`::::
(integer)
The number of documents that are not used for training the model and can be used 
for testing.

`training_docs_count`::::
(integer)
The number of documents that are used for training the model.
=====

`id`:::
(string)
The unique identifier of the {dfanalytics-job}.

`memory_usage`:::
(Optional, object)
An object describing memory usage of the analytics. It is present only after the 
job is started and memory usage is reported.
**Properties of `memory_usage`**
=====
`memory_reestimate_bytes`::::
(long)
This value is present when the `status` is `hard_limit` and it
is a new estimate of how much memory the job needs.

`peak_usage_bytes`::::
(long)
The number of bytes used at the highest peak of memory usage.

`status`::::
(string)
The memory usage status. May have one of the following values:
* `ok`: usage stayed below the limit.
* `hard_limit`: usage surpassed the configured memory limit.

`timestamp`::::
(date)
The timestamp when memory usage was calculated.
=====

`node`:::
(object)
Contains properties for the node that runs the job. This information is 
available only for running jobs.
**Properties of `node`**
=====
`attributes`::::
(object)
Lists node attributes such as `ml.machine_memory` or `ml.max_open_jobs` settings.
`ephemeral_id`::::
(string)
The ephemeral ID of the node.
`id`::::
(string)
The unique identifier of the node.
`name`::::
(string)
The node name.

`transport_address`::::
(string)
The host and port where transport HTTP connections are accepted.
=====

`progress`:::
(array) The progress report of the {dfanalytics-job} by phase.
**Properties of phase objects**
=====
`phase`::::
(string) Defines the phase of the {dfanalytics-job}. Possible phases: 
* `reindexing`, 
* `loading_data`, 
* `computing_outliers` (for {oldetection} only),
* `feature_selection` (for {regression} and {classification} only),
* `coarse_parameter_search` (for {regression} and {classification} only),
* `fine_tuning_parameters` (for {regression} and {classification} only),
* `final_training` (for {regression} and {classification} only),
* `writing_results`,
* `inference` (for {regression} and {classification} only).
To learn more about the different phases, refer to
{ml-docs}/ml-dfa-phases.html[How a {dfanalytics} job works].
    
`progress_percent`::::
(integer) The progress that the {dfanalytics-job} has made expressed in 
percentage.
=====

`state`:::
(string) The status of the {dfanalytics-job}, which can be one of the following
values: `failed`, `started`, `starting`,`stopping`, `stopped`.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

The following API retrieves usage information for the
{ml-docs}/ml-dfa-finding-outliers.html#weblogs-outliers[{oldetection} {dfanalytics-job} example]:

```console
GET _ml/data_frame/analytics/weblog-outliers/_stats
```

```console-result
{
  "count" : 1,
  "data_frame_analytics" : [
    {
      "id" : "weblog-outliers",
      "state" : "stopped",
      "progress" : [
        {
          "phase" : "reindexing",
          "progress_percent" : 100
        },
        {
          "phase" : "loading_data",
          "progress_percent" : 100
        },
        {
          "phase" : "computing_outliers",
          "progress_percent" : 100
        },
        {
          "phase" : "writing_results",
          "progress_percent" : 100
        }
      ],
      "data_counts" : {
        "training_docs_count" : 1001,
        "test_docs_count" : 0,
        "skipped_docs_count" : 0
      },
      "memory_usage" : {
        "timestamp" : 1626264770206,
        "peak_usage_bytes" : 328011,
        "status" : "ok"
      },
      "analysis_stats" : {
        "outlier_detection_stats" : {
          "timestamp" : 1626264770206,
          "parameters" : {
            "n_neighbors" : 0,
            "method" : "ensemble",
            "compute_feature_influence" : true,
            "feature_influence_threshold" : 0.1,
            "outlier_fraction" : 0.05,
            "standardization_enabled" : true
          },
          "timing_stats" : {
            "elapsed_time" : 32
          }
        }
      }
    }
  ]
}
```
