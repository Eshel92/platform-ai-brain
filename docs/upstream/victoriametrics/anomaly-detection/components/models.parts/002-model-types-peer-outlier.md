<!-- Part 2 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

## Model types

Models are classified along **two dimensions**: input/output topology and update strategy.

By input data handling:
- [Univariate models](#univariate-models) - models fit/used per each individual time series, producing **individual** [output](#vmanomaly-output)
- [Multivariate models](#multivariate-models) - models fit/used on a set of time series simultaneously, producing shared [output](#vmanomaly-output)
- [Peer-group models](#peer-group-models) - models fit/used on a changing population within one query, producing individual [output](#vmanomaly-output) for each member.

By update strategy:
- [Offline models](#offline-models) - models that require **full re-fit** on a defined `fit_window` of data to update their parameters defined by `fit_every` schedule in [scheduler](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#periodic-scheduler)
- [Online (incremental) models](#online-models) {{% available_from "v1.15.0" anomaly %}} - models that support **incremental updates** of their parameters on each `infer_every` step, even on a single datapoint, without the need for a full re-fit on a `fit_window` of data. This is a recommended approach to reduce data burden from VictoriaMetrics or other data sources.

### Univariate Models

For a visual introduction, see [a metric compared with its own history](https://docs.victoriametrics.com/anomaly-detection/guides/model-selection/#follow-each-metric-over-time).

For a univariate model, **one separate model instance** is fitted and used for each time series returned by its selected [queries](#queries).

For example, a univariate model attached to three [MetricsQL queries](https://docs.victoriametrics.com/victoriametrics/metricsql/), each returning five time series, creates 15 model instances. Each instance produces its own [output](#vmanomaly-output).

If during an inference, you got a series having **new labelset** (not present in any of fitted models), the inference will be skipped until you get a model, trained particularly for such labelset during forthcoming re-fit step.

**Implications:** Univariate models are a go-to default, when your queries returns **changing** amount of **individual** time series of **different** magnitude, [trend](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend) or [seasonality](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality), so you won't be mixing incompatible data with different behavior within a single fit model (context isolation).

**Examples:** [Temporal Envelope](#temporal-envelope), [Online MAD](#online-mad), [Online Z-score](#online-z-score), [Online Seasonal Quantile](#online-seasonal-quantile)

![Univariate model lifecycle](model-lifecycle-univariate.svg)


### Multivariate Models

For a visual introduction, see [connected signals with an unusual combination](https://docs.victoriametrics.com/anomaly-detection/guides/model-selection/#watch-related-signals-together).

For a multivariate model, **one shared model instance** is fitted and used across all aligned time series returned by its selected [queries](#queries).

For example, if you have some **multivariate** model to use 3 [MetricQL queries](https://docs.victoriametrics.com/victoriametrics/metricsql/), each returning 5 time series, there will be one shared model created in total. Once fit, this model will expect **exactly 15 time series with exact same labelsets as an input**. This model will produce **one shared [output](#vmanomaly-output)**.

> {{% available_from "v1.30.2" anomaly %}} Multivariate Temporal Envelope and Isolation Forest accept matching input channels in any order. The channel set must still match the fitted model exactly: missing, extra, and duplicate channels are rejected, while a matching set is restored to learned fit order before inference or online updates.

> {{% available_from "v1.16.0" anomaly %}} N models — one for each N unique combinations of label values specified in the `groupby` [common argument](#group-by) — can be trained. This allows for context separation (e.g., one model per host, region, or other relevant grouping label), leading to improved accuracy and faster training. See an example [here](#group-by).

If during an inference, you got a **different amount of series** or some series having a **new labelset** (not present in any of fitted models), the inference will be skipped until you get a model, trained particularly for such labelset during forthcoming re-fit step. 

**Implications:** Multivariate models are a go-to default, when your queries returns **fixed** amount of **individual** time series (say, some aggregations), to be used for adding cross-series (and cross-query) context, useful for catching [collective anomalies](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-2/#collective-anomalies) or [novelties](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-2/#novelties) (expanded to multi-input scenario). For example, you may set it up for anomaly detection of CPU usage in different modes (`idle`, `user`, `system`, etc.) and use its cross-dependencies to detect **unseen (in fit data)** behavior.

**Recommended:** [Temporal Envelope](#temporal-envelope). Existing [Isolation Forest](#isolation-forest-multivariate) configurations can migrate to its multivariate form.

![Multivariate model lifecycle](model-lifecycle-multivariate.svg)

The following configuration applies a multivariate Temporal Envelope model to the same aligned input series:

```yaml
models:
  service_dependency_envelope:
    class: temporal_envelope_multivariate
    queries: [request_rate, error_rate, latency]
    groupby: [cluster]
    dependency_rank: 8
    score_aggregation: l2
    seasonalities: [hod_smooth, dow_smooth]
    provide_series: [anomaly_score]

```


### Peer-group Models

For a visual introduction, see [an entity compared with its peers](https://docs.victoriametrics.com/anomaly-detection/guides/model-selection/#find-the-odd-one-out).

For a peer-group model {{% available_from "v1.31.0" anomaly %}}, **one shared model instance per query and group** compares comparable entities at each timestamp and produces a **separate anomaly score for each peer**. Unlike multivariate models, the population is not a fixed set of channels. Unlike univariate models, each member does not need its own fitted model.

Each query defines an independent population; queries are never pooled together. Use `groupby` to divide it by labels such as `service` or `region`. Retain identity labels such as `instance` in the query results, but leave them out of `groupby`. For example, two queries each returning three services create six group models, regardless of how many instances belong to each service.

**Membership and cold starts:**

- A new peer joining an existing, warmed-up group can be scored using the group's learned state without a separate per-peer fit.
- Missing or departed peers do not invalidate the remaining population. Scoring still requires enough valid, aligned peers at that timestamp (`min_peer_count` for [Peer Outlier](#peer-outlier)).
- A new query/group identity needs its own fitted model and warmup; it cannot reuse another group's state. Membership changes within an existing group do not reset that group's warmup.

**Implications:** Use peer groups for comparable replicas, load balancers or hosts with similar roles. They detect unusual members relative to their population, rather than replacing temporal detection for changes shared by the whole population.

**Implementation:** [Peer Outlier](#peer-outlier), an online model. See its configuration, assumptions and parameters below.

![Peer-group model lifecycle: fit per query and group, score each peer, and reuse group state when membership changes](model-lifecycle-peer-group.svg)

### Online Models

> Online models are best used **in combination with [stateful service](https://docs.victoriametrics.com/anomaly-detection/components/settings/#state-restoration) {{% available_from "v1.24.0" anomaly %}} to ensure that the model state is preserved if the service restarts and any aggregated model updates are not lost**. E.g. if the model was already trained on many weeks of data and is being updated on new datapoints every minute, there is no need to re-train it from scratch on the same data after each restart, as it can continue to update restored state on new datapoints. Also it is worth setting [retention policy](https://docs.victoriametrics.com/anomaly-detection/components/settings/#retention) {{% available_from "v1.28.1" anomaly %}} for such models to periodically clean up outdated artifacts, e.g. due to high churn rate of unique labelsets in input data.

Online (incremental) models {{% available_from "v1.15.0" anomaly %}} allow defining a smaller frame `fit_window` and less frequent `fit` calls to reduce the data burden from VictoriaMetrics. They make incremental updates to model parameters during each `infer_every` call, even on a single datapoint.
If the model doesn't support online mode, it's called **offline** (its parameters are only updated during `fit` calls).

Main differences between offline and online:

**Fit stage**
- Both types have a `fit` stage, run on the `fit_window` data frame.
- For offline models, `fit_window` should contain enough data to train the model (e.g., 2 seasonal periods).
- For online models, training can start gradually from smaller chunks (e.g., 1 hour).

**Infer stage**
- Both types have an `infer` stage, run on new datapoints (timestamps > last seen timestamp of the previous `infer` call).
- Offline models use a pre-trained (during `fit` call) *static* model to make every `infer` call until the next `fit` call, when the model is completely re-trained.
- Online models use a pre-trained (during `fit` call) *dynamic* model, which is gradually updated during each `infer` call with new datapoints. However, to prevent the model from accumulating outdated behavior, each `fit` call resets the model from scratch.

**Strengths**:

- The ability to distribute data processing between the initial `fit` and subsequent `infer` calls. For example, a model may start with ten one-minute samples and then update from each new ten-sample chunk rather than repeatedly fetching a large fit window.
- The model can adapt to new data patterns (gradually updating itself during each `infer` call) without needing to wait for the next `fit` call and one big re-training.
- Slightly faster training/updating times compared to similar offline models.
- See the corresponding [FAQ section](https://docs.victoriametrics.com/anomaly-detection/faq/#online-models) for additional benefits in data-intensive setups.

**Limitations**:

- Until the online model sees enough data (especially if the data shows strong seasonality), its predictions might be unstable, producing more [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive) (`anomaly_score > 1`) or making [false negative predictions, skipping real anomalies](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-negative).

Each of the ([built-in](#built-in-models) or [custom](#custom-model-guide)) online models (like [`OnlineZscoreModel`](#online-z-score)) shares the following common parameters and properties:
- `n_samples_seen_` (int) - this model *property* refers to the number of datapoints the model was trained on and increases from 0 (before the first `fit`) with each consecutive `infer` call.
- `min_n_samples_seen` (int), optional - the minimum number of samples required before the model emits a non-neutral [anomaly score](https://docs.victoriametrics.com/anomaly-detection/faq/#what-is-anomaly-score). Until then, the anomaly score is `0`. For example, 288 samples cover one day at a five-minute sampling interval.


### Offline models

Every other model that isn't [online](#online-models). Offline models are completely re-trained during `fit` call and aren't updated during consecutive `infer` calls.

> [!NOTE]
> Built-in offline model classes are planned for deprecation in a future release in favor of online counterparts. For complex temporal data, prefer [Temporal Envelope](#temporal-envelope), which supports incremental adaptation, forecasting, and both univariate and multivariate operation.



## Built-in Models 


### Overview

> [!TIP]
> For a practical path from metric behavior to a model configuration, see [Choose a model for your metrics](https://docs.victoriametrics.com/anomaly-detection/guides/model-selection/). It includes reproducible playground examples and tuning hints.

Built-in models support 2 groups of arguments:

- **Model-specific arguments** - please refer to the collapsed *Model-specific arguments* section for each model below.
- Arguments to **inner model** (say, [Facebook's Prophet](https://facebook.github.io/prophet/docs/quick_start#python-api)), passed inside `args` argument as key-value pairs, that will be directly given to the model during initialization to allow granular control. Optional.

> For users who may not be familiar with Python data types such as `list[dict]`, a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp) in Python is a data structure that stores data values in key-value pairs. This structure allows for efficient data retrieval and management.


**Models**:
- [Peer Outlier](#peer-outlier) - an online model for finding unusual members of comparable peer populations, with independent grouping and changing membership.
- [AutoTuned](#autotuned) - designed to take the cognitive load off the user, allowing any of built-in models below to be re-tuned for best hyperparameters on data seen during each `fit` phase of the algorithm. Tradeoff is between increased computational time and optimized results / simpler maintenance.
- [Temporal Envelope](#temporal-envelope) - the preferred **online model for complex operational data** with trends, changepoints, multiple calendar patterns, holidays, capable of [forecasting](https://docs.victoriametrics.com/anomaly-detection/faq/#forecasting). Its multivariate form also learns cross-series relationships.
- [Online Z-score](#online-z-score) - useful for initial testing and for simpler data ([de-trended](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend) data without strict [seasonality](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality) and with anomalies of similar magnitude as your "normal" data)
- [MAD](#online-mad) - similarly to [Z-score](#online-z-score), is effective for **identifying outliers in relatively consistent data**. Useful for detecting sudden, stark deviations from the median, being less prone to outlier's magnitude than z-score.
- [Rolling Quantile](#rolling-quantile) - best for **data with evolving patterns**, as it adapts to changes over a rolling window.
- [Online Seasonal Quantile](#online-seasonal-quantile) - best used on **[de-trended](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend) data with strong (possibly multiple) [seasonalities](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality)**. Can act as a (slightly less powerful) [online](#online-models) replacement to [`ProphetModel`](#prophet).
- [Seasonal Trend Decomposition](#seasonal-trend-decomposition) - similarly to Holt-Winters, is best for **data with pronounced [seasonal](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality) and [trend](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend) components**
- [Prophet](#prophet) - an offline model retained for existing deployments. Migrate forecasting and seasonal anomaly-detection configurations to [Temporal Envelope](#temporal-envelope), unless Prophet-specific decomposition output must be preserved.
- [Isolation forest (Multivariate)](#isolation-forest-multivariate) - an offline model retained for existing univariate and multivariate deployments. Migrate to the corresponding [Temporal Envelope](#temporal-envelope) form for online adaptation and temporal or cross-series context.
- [Holt-Winters](#holt-winters) - an offline model retained for existing trend and single-seasonality configurations. Migrate these configurations to [Temporal Envelope](#temporal-envelope).
- [Custom model](#custom-model-guide) - benefit from your own models and expertise to better support your **unique use case**.



### Peer Outlier

**Experimental.** `peer_outlier` {{% available_from "v1.31.0" anomaly %}} (`model.online.PeerOutlierModel`) is an online implementation of [peer-group detection](#peer-group-models). Use it to detect unusual resource utilization or other measurements among comparable replicas or hosts. A snapshot needs at least `min_peer_count` aligned peers to train or score.

```yaml
models:
  cpu_peers:
    class: peer_outlier
    queries: [cpu_utilization]
    groupby: [service]
    min_peer_count: 5
    epsilon_quantile: 0.75
    tolerance: 4.0
    decay: 1.0
    clip_predictions: true
reader:
  queries:
    cpu_utilization:
      expr: '100 * (1 - avg by (service, instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])))'
      data_range: [0, 100]
# other components like writer, schedulers, monitoring ...
```

The model learns historical cross-sectional spread and residual distributions. Its accepted peer range can be asymmetric; it is not a statistical confidence interval. It relies on a strict-majority normal population, so it is not intended to detect a coordinated change affecting every peer. Use a [temporal model](#temporal-envelope) alongside it when shared shifts matter.

| Parameter | Default | Meaning |
| --- | --- | --- |
| `groupby` | omitted | Labels defining independent populations within each query. |
| `min_peer_count` | `5` | Minimum aligned peers; must be at least `3`. |
| `epsilon_quantile` | `0.75` | Historical spread quantile, strictly between `0` and `1`. Higher values tolerate wider populations. |
| `tolerance` | `4.0` | Positive multiplier for the learned neighborhood and accepted range; not a number of standard deviations. |
| `decay` | `1.0` | Weight decay per valid snapshot, in `(0, 1]`. Values below `1` prioritize recent populations. |
| `min_n_samples_seen` | derived | Minimum effective valid snapshots before scoring. When omitted, the upper tail must have at least eight observations: `ceil(8 / (1 - epsilon_quantile))`, or `32` with defaults. Scores remain zero during warmup. |

The effective warmup must be reachable with the selected decay. Shared [domain-knowledge parameters](#common-args), including query-level policies, still apply. Set `data_range` and `clip_predictions: true` to keep predictions within known physical bounds; absence of negative training observations alone does not impose a zero lower bound. Configure model parameters at the top level; nonempty `args` is rejected.

Use the [peer-group investigation view](https://docs.victoriametrics.com/anomaly-detection/ui/#peer-group-investigation) to inspect the accepted range, rank anomalous peers and compare group activity.
