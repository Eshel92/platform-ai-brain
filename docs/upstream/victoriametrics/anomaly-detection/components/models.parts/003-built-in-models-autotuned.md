<!-- Part 3 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

### AutoTuned
Selecting model [hyperparameters](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)) can require detailed knowledge of both the model and the data. The `AutoTunedModel` wrapper searches supported parameters during each fit. At minimum, configure `tuned_class_name` and the expected upper bound for anomalous observations through `optimization_params.anomaly_percentage`.

The wrapper follows the selected model's grouping: one model per series for univariate detection, one per aligned group for multivariate detection, and one per query-isolated population for peer-group detection. {{% available_from "v1.31.0" anomaly %}} To tune `peer_outlier`, set `tuned_class_name: peer_outlier` and put any grouping labels in `optimization_params.frozen_params.groupby`. Validation keeps population snapshots intact. Keep `optimized_business_params: []` and define stable business policies on the queries. Use [shared tuning](#shared-asynchronous-autotune-workflow) to obtain a concrete configuration without retuning on every fit; capacity estimates for that configuration exclude the tuning search.

> For a univariate `tuned_class_name`, a [query](#queries) returning multiple series produces one independently tuned model per unique labelset. Using the concrete class directly instead gives those models the same configured hyperparameters. For example:
> ```yaml
> models:
>   # this may result in 1 model per each unique labelset with different hyperparameters, such as z_threshold
>   autotuned_model:
>     class: 'auto'
>     tuned_class_name: 'zscore_online'
>     optimization_params:
>       anomaly_percentage: 0.01
>     queries: ['your_query']
> ```
> will produce **one model per each unique labelset** found in `your_query` results, with **different hyperparameters**, such as `z_threshold`, while
> ```yaml
> models:
>   # this will result in 1 model per each timeseries returned by the query,
>   # with the same hyperparameters, such as z_threshold
>   zscore_model:
>     class: 'zscore_online'
>     z_threshold: 3  # all models will have the same z_threshold, but different parameters, such as mean, std, etc.
>     queries: ['your_query']
> ```
> will produce **one model per each timeseries** returned by `your_query`, with **the same** hyperparameters, such as `z_threshold`, but different parameters, such as mean, std, etc.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.auto.AutoTunedModel"` (or `auto` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `tuned_class_name` (string) - [Built-in model class](#built-in-models) to wrap, i.e. `zscore_online`
- `optimization_params` (dict) - Optimization parameters for *unsupervised* model tuning. Control percentage of found anomalies, as well as a tradeoff between time spent and the accuracy. The higher `timeout` and `n_trials` are, the better model configuration can be found for `tuned_class_name`, but the longer it takes and vice versa. Set `n_jobs` to `-1` to use all the CPUs available, it makes sense if only you have a big dataset to train on during `fit` calls, otherwise overhead isn't worth it.
  - `anomaly_percentage` (float) - Expected percentage of anomalies that can be seen in training data, from `[0, 0.5)` interval (i.e. 0.01 means it's expected ~ 1% of anomalies to be present in training data). This is a *required* parameter.
  - `optimized_business_params` (list[string]) - {{% available_from "v1.15.0" anomaly %}} Experimental optimization of model-level business parameters is {{% deprecated_from "v1.30.2" anomaly %}}. Keep this list empty and configure stable `detection_direction`, `min_dev_from_expected`, and `min_rel_dev_from_expected` policies on [`reader.queries.<alias>`](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters) instead.
  - `seed` (int) - Random seed for reproducibility and deterministic nature of underlying optimizations.
  - `validation_scheme` (string) - {{% available_from "v1.25.1" anomaly %}} the validation scheme to use for hyperparameter tuning, either `regular` (time-based default) or `leaky` (regular cross-validation with  `n_splits` folds, where each fold is a time-based split of the data). The `leaky` scheme is recommended for `anomaly_percentage` ~ 0%, as it allows the model to "see" all the datapoints at least once during the optimization process, which can lead to better results in such cases. Defaults to `regular`.
  - `n_splits` (int) - How many folds to create for hyperparameter tuning out of your data. The higher, the longer it takes but the better the results can be. Defaults to 3.
  - `train_val_ratio` (float) - {{% available_from "v1.25.1" anomaly %}} the ratio of training to validation data size when constructing folds, e.g. setting it to 2 will result in 2/3 of the data being used for training and 1/3 for validation in each of the splits. Defaults to 3 (3/4 of the data for training and 1/4 for validation). Isn't used when `validation_scheme` is set to `leaky`.
  - `n_trials` (int) - How many trials to sample from hyperparameter search space. The higher, the longer it takes but the better the results can be. Defaults to 128.
  - `timeout` (float) - How many seconds in total can be spent on each model to tune hyperparameters. The higher, the longer it takes, allowing to test more trials out of defined `n_trials`, but the better the results can be.
  - `exact` (boolean) - {{% available_from "v1.30.0" anomaly %}} evaluate online models causally during validation: predict from the current state, then update it with newly observed data. Set this to `true` when production uses exact online inference. Defaults to `false` for backward compatibility.
  - `optimize_complexity` (boolean) - {{% available_from "v1.30.0" anomaly %}} prefer a smaller fitted model state when validation quality is effectively tied. Defaults to `true`.
  - `frozen_params` (dict) - {{% available_from "v1.30.0" anomaly %}} model-specific parameters that **must remain fixed** while the remaining search space is tuned. Nested dictionaries are merged recursively. Use this for non-optimizable context such as configured holidays or multivariate `groupby`; `class` cannot be frozen.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}

```yaml
# ...
models:
  your_desired_alias_for_a_model:
    class: 'auto'  # or 'model.auto.AutoTunedModel' until v1.13.0
    tuned_class_name: 'zscore_online'
    optimization_params:
      anomaly_percentage: 0.004  # required. i.e. we expect <= 0.4% of anomalies to be present in training data
      seed: 42  # fix reproducibility & determinism
      n_splits: 3  # how much folds are created for internal cross-validation
      validation_scheme: 'regular'  # either 'regular' (time-based default) or 'leaky' (cross-validation with n_splits folds)
      train_val_ratio: 3  # how much training data to use in each fold vs validation, e.g. 3 means 3/4 of the data for fit and 1/4 for infer

      n_trials: 128  # how many configurations to sample from search space during optimization
      timeout: 10  # how many seconds to spend on optimization for each trained model during `fit` phase call
      n_jobs: 1  # how many jobs in parallel to launch. Consider making it > 1 only if you have fit window containing > 10000 datapoints for each series
      optimized_business_params: []  # business-specific params to include in optimization, if not set - defaults to empty list, meaning no business params will be optimized, which is a recommended option as business arguments are better set by stakeholders rather than algorithms
      exact: true  # causally validate online models the same way they run in production
      optimize_complexity: true  # prefer smaller fitted state when quality is tied
      frozen_params:
        history_strength: 2
  # ...
```

{{% /collapse %}}

</div>

![AutoTunedModel tuning and inference lifecycle](autotune.svg)

#### Shared asynchronous autotune workflow

{{% available_from "v1.30.0" anomaly %}} Agents, the UI, and external automation can tune one shared configuration across a bounded sample of query results without adding an `auto` wrapper to the production configuration:

1. Inspect the query with `GET /api/v1/timeseries/characteristics` to identify trend, calendar seasonality, changepoints, gaps, and intermittent behavior.
2. Start a task with `POST /api/v1/autotune/tasks`. Provide the actual query (or named queries), the candidate model class, the same query `step` used in production, and a bounded `limit`.
3. Poll `GET /api/v1/autotune/tasks/{task_id}` until `status` is `done`; cancel unnecessary work with `DELETE` on the same path.
4. Validate and deploy `result_data.data.modelConfig`, which is a concrete configuration for the selected model class.

> [!TIP]
> Use [skills](https://docs.victoriametrics.com/ai-tools/#agent-skills) where abovementioned workflow is automated. Also, [AI Copilot](https://docs.victoriametrics.com/anomaly-detection/ui/#ai-assistance) can generate a tuned model configuration to interactively backtest in UI, based on the query data characteristics and user's anomaly expectations.

The examples below are JSON bodies for `POST /api/v1/autotune/tasks`. Replace the example `datasource_url` with an address reachable from vmanomaly and adjust `start` and `end` (Unix seconds) to your data. The examples select 2026-08-10 00:00 UTC through 2026-09-09 00:00 UTC. See the server’s [interactive API reference](https://docs.victoriametrics.com/anomaly-detection/components/server/#interactive-api-reference) for the running version’s request schemas.

<div class="collapse-group mb-3">

{{% collapse name="Univariate online-model example" %}}

```json
{
  "datasource_url": "http://victoriametrics:8428",
  "start": 1786320000,
  "end": 1788912000,
  "query": "sum(rate(http_requests_total[5m])) by (service)",
  "tuned_class_name": "temporal_envelope",
  "anomaly_percentage": 0.01,
  "step": "5m",
  "limit": 100,
  "use_profile_hints": true,
  "optimization_params": {
    "exact": true,
    "n_splits": 3,
    "n_trials": 64,
    "timeout": 60,
    "optimize_complexity": true
  },
  "frozen_params": {
    "holidays": {
      "countries": [
        "US"
      ],
      "group": true
    }
  }
}
```

{{% /collapse %}}

{{% collapse name="Multivariate named-query example with grouping" %}}

{{% available_from "v1.30.5" anomaly %}} Tune request rate and error rate jointly, with one multivariate input group per `service`. Both expressions must return data for every service included in the study; an absent error series is not automatically treated as zero.

```json
{
  "datasource_url": "http://victoriametrics:8428",
  "start": 1786320000,
  "end": 1788912000,
  "queries": {
    "request_rate": {
      "expr": "sum by (service) (rate(http_requests_total{service!=\"\"}[5m]))",
      "data_range": [
        0,
        "inf"
      ]
    },
    "error_rate": {
      "expr": "sum by (service) (rate(http_requests_total{service!=\"\",status=~\"5..\"}[5m]))",
      "data_range": [
        0,
        "inf"
      ],
      "detection_direction": "above_expected"
    }
  },
  "tuned_class_name": "temporal_envelope_multivariate",
  "anomaly_percentage": 0.01,
  "step": "5m",
  "limit": 100,
  "optimization_params": {
    "exact": true,
    "n_splits": 3,
    "n_trials": 64,
    "timeout": 60,
    "optimize_complexity": true
  },
  "frozen_params": {
    "groupby": [
      "service"
    ],
    "score_aggregation": "l2"
  }
}
```

For each candidate configuration, the server fits and evaluates separate models for the aligned service groups and aggregates their validation scores in one study. The result is one shared model configuration for all groups. `frozen_params.groupby` keeps grouping fixed, while the named queries retain their individual business policies. `limit` applies separately to each expression; ensure it is large enough to retain all required channels for the intended groups.

{{% /collapse %}}

</div>

The requested anomaly percentage is treated as an alert-volume constraint rather than a target that must be reached in every validation fold. Model-specific search ranges may be narrowed using the sampled characteristics, while `frozen_params` preserves operator-supplied context. For online models, `exact: true` usually gives the most representative choice when production inference is causal.

> There are some expected limitations of Autotune mode:
> - It can't be made on your [custom model](#custom-model-guide).
> - It can't be applied to itself (like `tuned_class_name: 'model.auto.AutoTunedModel'`)
