<!-- Part 1 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

## Common args

Common arguments supported by every model were introduced in [v1.10.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1100).

> [!WARNING]
> Configuring `data_range`, `detection_direction`, `min_dev_from_expected`, or `min_rel_dev_from_expected` at model level is deprecated {{% deprecated_from "v1.30.2" anomaly %}}. These stable KPI policies belong under [`reader.queries.<alias>`](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters), where they remain consistent across every [univariate](#univariate-models) or [multivariate](#multivariate-models) model that uses the query. Existing model-level values remain compatible as model-local fallbacks when an attached query does not define the corresponding field; an explicit query value is authoritative.

<div class="collapse-group">

{{% collapse name="Queries" %}}

### Queries

The `queries` argument selects the [reader queries](https://docs.victoriametrics.com/anomaly-detection/components/reader/#config-parameters) used to fit and run a particular model{{% available_from "v1.10.0" anomaly %}}. Every series returned by a selected query is passed to that model.

`queries` arg is supported for all [the built-in](#built-in-models) (as well as for [custom](#custom-model-guide)) models.

This arg is **backward compatible** - if there is no explicit `queries` arg, then the model, defined in a config, will be run on ALL queries found in reader section:

```yaml
models:
  model_alias_1:
    # ...
    # no explicit `queries` arg is provided
```

will be implicitly converted to

```yaml
models:
  model_alias_1:
    # ...
    # if not set, `queries` arg is created and propagated with all query aliases found in `queries` arg of `reader` section
    queries: ['q1', 'q2', 'q3']  # i.e., if your `queries` in `reader` section has exactly q1, q2, q3 aliases
```

{{% /collapse %}}

{{% collapse name="Schedulers" %}}

### Schedulers

The `schedulers` argument selects the [schedulers](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/) that run a particular model{{% available_from "v1.11.0" anomaly %}}.

`schedulers` arg is supported for all [the built-in](#built-in-models) (as well as for [custom](#custom-model-guide)) models.

This arg is **backward compatible** - if there is no explicit `schedulers` arg, then the model, defined in a config, will be attached to ALL the schedulers found in scheduler section:

```yaml
models:
  model_alias_1:
    # ...
    # no explicit `schedulers` arg is provided
```

will be implicitly converted to

```yaml
models:
  model_alias_1:
    # ...
    # if not set, `schedulers` arg is created and propagated with all scheduler aliases found in `schedulers` section
    schedulers: ['s1', 's2', 's3']  # i.e., if your `schedulers` section has exactly s1, s2, s3 aliases
```

{{% /collapse %}}

{{% collapse name="Provide series" %}}

### Provide series

The `provide_series` argument{{% available_from "v1.12.0" anomaly %}} limits the [model output](#vmanomaly-output) sent to the writer. For example, a model may produce `['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper']` by default, while the following configuration writes only `anomaly_score` for each input series:

```yaml
models:
  model_alias_1:
    # ...
    provide_series: ['anomaly_score']  # only `anomaly_score` metric will be available for writing back to the database
```

> If `provide_series` is not specified in model config, the model will produce its default [model-dependent output](#vmanomaly-output). The output can't be less than `['anomaly_score']`. Even if `timestamp` column is omitted, it will be implicitly added to `provide_series` list, as it's required for metrics to be properly written.

{{% /collapse %}}

{{% collapse name="Detection direction" %}}

### Detection direction
The `detection_direction` argument{{% available_from "v1.13.0" anomaly %}} can reduce [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive) when domain knowledge indicates that only values above or below the expected value are anomalous. Available values are `both`, `above_expected`, and `below_expected`. Configure it on the input query; model-level placement is {{% deprecated_from "v1.30.2" anomaly %}}.

Here's how the three options differ:

![detection_direction comparison](schema_detection_direction.webp)

With the default, backward-compatible `both` value, anomalies are tracked in both directions (`y > yhat` or `y < yhat`). This is useful when there is no domain expertise to filter the required direction.

When set to `above_expected`, anomalies are tracked only when `y > yhat`.

*Example metrics*: Error rate, response time, page load time, number of failed transactions - metrics where *lower values are better*, so **higher** values are typically tracked.

When set to `below_expected`, anomalies are tracked only when `y < yhat`. 

*Example metrics*: Service Level Agreement (SLA) compliance, conversion rate, Customer Satisfaction Score (CSAT) - metrics where *higher values are better*, so **lower** values are typically tracked.

One model can use multiple queries with different directions because the policy belongs to each query:

```yaml
reader:
  # ...
  queries:
    query_values_the_lower_the_better:
      expr: metricsql_expression1
      detection_direction: 'above_expected'  # query-level from v1.30.2; only y > yhat can be anomalous
    query_values_the_higher_the_better:
      expr: metricsql_expression2
      detection_direction: 'below_expected'  # query-level from v1.30.2; only y < yhat can be anomalous
    query_values_both_direction_matters:
      expr: metricsql_expression3
      detection_direction: 'both'  # query-level from v1.30.2; the default when omitted
models:
  model_all_directions:
    class: 'zscore_online'
    z_threshold: 3.0
    queries: [
      'query_values_the_lower_the_better',
      'query_values_the_higher_the_better',
      'query_values_both_direction_matters',
    ]
# other components like writer, schedule, monitoring
```

{{% /collapse %}}

{{% collapse name="Minimal deviation from expected" %}}

### Minimal deviation from expected

`min_dev_from_expected`{{% available_from "v1.13.0" anomaly %}} argument is designed to **reduce [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive)** in scenarios where deviations between the actual value (`y`) and the expected value (`yhat`) are **relatively** high. Such deviations can cause models to generate high [anomaly scores](https://docs.victoriametrics.com/anomaly-detection/faq/#what-is-anomaly-score). However, these deviations may not be significant enough in **absolute values** from a business perspective to be considered anomalies. This parameter ensures that anomaly scores for data points where `|y - yhat| < min_dev_from_expected` are explicitly set to 0. By default, if this parameter is not set, it is set to `0` to maintain backward compatibility. Configure it on the input query; model-level placement is {{% deprecated_from "v1.30.2" anomaly %}}.

> [!NOTE]
{{% available_from "v1.23.0" anomaly %}} The `min_dev_from_expected` argument can be a list of two float values, allowing separate thresholds for upper and lower deviations. This is useful when the acceptable deviation varies in different directions (e.g., `min_dev_from_expected: [0.01, 0.02]` means that the lower bound is `0.01` when `y` is less than `yhat` and the upper bound is `0.02` when `y` is greater than `yhat`). If only one value is provided, it is broadcasted to both directions, meaning that the same threshold is applied for both upper and lower deviations (e.g., `min_dev_from_expected: 0.01` means that the lower bound is `0.01` when `y` is less than `yhat` and the upper bound is also `0.01` when `y` is greater than `yhat`).

`min_dev_from_expected` must be >= 0. The higher the value of `min_dev_from_expected` is, the more significant the deviation must be to generate an anomaly score != 0. This helps in filtering out small *absolute* deviations that may not be meaningful in the context of the monitored metric.

*Example*: Consider a scenario where CPU utilization in specific mode is low and oscillates around 0.3% (0.003). A sudden spike to 1.3% (0.013) represents a +333% increase in **relative** terms, but only a +1 percentage point (0.01) increase in **absolute** terms, which may be negligible and not warrant an alert. Setting the `min_dev_from_expected` argument to `0.01` (1%) will ensure that all anomaly scores for deviations <= `0.01` are set to 0.

The visualization below demonstrates this concept. The narrow blue model prediction boundary is nested inside the wider green business protection boundary. Actual values outside the prediction boundary but still within `[yhat - min_dev_from_expected, yhat + min_dev_from_expected]` receive `anomaly_score = 0`; only values outside the green boundary remain anomalous.

![min_dev_from_expected](schema_min_dev_from_expected.webp)

Example config of how to use this param based on query results:

```yaml
# other components like writer, schedulers, monitoring ...
reader:
  # ...
  queries:
    # the usage of min_dev should reduce false positives here
    need_to_include_min_dev:
      expr: small_abs_values_metricsql_expression
      min_dev_from_expected: [5.0, 5.0]  # query-level from v1.30.2
    # min_dev is not really needed here
    normal_behavior:
      expr: no_need_to_exclude_small_deviations_metricsql_expression
models:
  zscore:
    class: 'zscore_online'
    z_threshold: 3
    queries: ['need_to_include_min_dev', 'normal_behavior']
```

{{% /collapse %}}

{{% collapse name="Minimal relative deviation from expected" %}}

### Minimal relative deviation from expected

{{% available_from "v1.29.1" anomaly %}} `min_rel_dev_from_expected` argument serves a similar purpose to `min_dev_from_expected` (see [section above](#minimal-deviation-from-expected)), but focuses on **relative deviations** rather than absolute ones. It is designed to reduce [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive) in scenarios where the relative deviation between the actual value (`y`) and the expected value (`yhat`) is high, but the absolute deviation is not significant enough to be considered an anomaly from a business perspective. This parameter ensures that anomaly scores for data points where `|y - yhat| / |yhat| < min_rel_dev_from_expected` are explicitly set to 0. By default, if this parameter is not set, it is set to `0` to maintain backward compatibility. Configure it on the input query; model-level placement is {{% deprecated_from "v1.30.2" anomaly %}}.

Parameter can be a list of two float values, *allowing separate thresholds for upper and lower relative deviations*. If only one value is provided, it is broadcasted to both directions.

> [!NOTE]
If both `min_dev_from_expected` [arg](#minimal-deviation-from-expected) and `min_rel_dev_from_expected` are set, the model will combine both filters. A data point will be considered anomalous (i.e., have an anomaly score != 0) only if it exceeds **both** the *absolute* deviation threshold defined by `min_dev_from_expected` and the *relative* deviation threshold defined by `min_rel_dev_from_expected`. This allows for more granular control over anomaly detection, ensuring that only significant deviations in both absolute and relative terms are flagged as anomalies.

The green business protection boundary below scales with `|yhat|`, while the model prediction boundary remains visible inside it. Actual values outside the blue boundary but inside the proportional green boundary receive `anomaly_score = 0`.

![min_rel_dev_from_expected](schema_min_rel_dev_from_expected.webp)


*Example*: Consider a scenario of monitoring incoming traffic to websites that typically receives *unknown in advance* requests per second (from tens to thousands). Setting absolute deviation threshold with `min_dev_from_expected` *may not be effective in reducing false positives*, as even a small increase in traffic (e.g., from 10 to 20 requests per second) can represent a 100% relative increase, which may be significant for that website. Instead, setting `min_rel_dev_from_expected` to smaller relative value - `[20, 40]` (20/40%) - will ensure that traffic drop from 10 to 8 requests per second (20% decrease) and traffic spike from 10 to 14 requests per second (40% increase) won't be considered anomalous, even if they exceed confidence intervals, thus, reducing false positives for small absolute deviations that are relatively significant.

Example of how to use this parameter in config:

```yaml
# other components like writer, schedulers, monitoring ...
reader:
  # ...
  queries:
    # the usage of min_rel_dev should reduce false positives here
    need_to_include_min_rel_dev:
      expr: small_abs_values_metricsql_expression
      min_rel_dev_from_expected: [10, 20]  # query-level from v1.30.2
    # min_rel_dev is not really needed here
    normal_behavior:
      expr: no_need_to_exclude_small_deviations_metricsql_expression
models:
  zscore:
    class: 'zscore_online'
    z_threshold: 3
    queries: ['need_to_include_min_rel_dev', 'normal_behavior']
```
  

{{% /collapse %}}

{{% collapse name="Group by" %}}

### Group by

> The `groupby` argument applies to [multivariate models](#multivariate-models) and [peer-group models](#peer-group-models). For peer groups {{% available_from "v1.31.0" anomaly %}}, it defines independent populations within each query; keep peer identity labels out of `groupby`.

The `groupby` argument{{% available_from "v1.13.0" anomaly %}} (`list[string]`) enables logical grouping within [multivariate models](#multivariate-models). When specified, **a separate multivariate model is trained for each unique combination of label values present in the `groupby` columns**.

For example, to perform multivariate anomaly detection at the machine level while avoiding interference between different entities, you can set `groupby: [host]` or `groupby: [instance]`. This ensures that a **separate multivariate** model is trained for each individual entity (e.g., per host). Below is a simplified example illustrating how to track multivariate anomalies using CPU, RAM, and network data for each host.

```yaml
# other config sections ...
reader:
  # other reader params ...
  # assume there are M unique hosts identified by the `host` label
  queries:
    # return one timeseries for each CPU mode per host, total = N*M timeseries
    cpu:
      expr: sum(rate(node_cpu_seconds_total[5m])) by (host, mode)
      data_range: [0, 'inf']
      detection_direction: both
      min_rel_dev_from_expected: [15, 15]
    # return one timeseries per host, total = 1*M timeseries
    ram:
      expr: |
        100 * (
          1 - node_memory_MemAvailable_bytes
          / node_memory_MemTotal_bytes
        )
      data_range: [0, 100]
      detection_direction: above_expected
      min_rel_dev_from_expected: [0, 15]
    # return one timeseries per host for both network receive and transmit data, total = 1*M timeseries
    network:
      expr: |
        sum(rate(node_network_receive_bytes_total[5m])) by (host)
        + sum(rate(node_network_transmit_bytes_total[5m])) by (host)
      data_range: [0, 'inf']
      detection_direction: below_expected
      min_rel_dev_from_expected: [20, 0]

models:
  envelope: # alias for the model
    class: temporal_envelope_multivariate
    seasonalities: [hod_smooth, dow_smooth]
    provide_series: [anomaly_score]
    # the multivariate model can be trained on 2+ timeseries returned by 1+ queries
    queries: [cpu, ram, network]
    # train a distinct multivariate model for each unique value found in the `host` label
    # a single multivariate model will be trained on (N + 1 + 1) timeseries, total = M models
    groupby: [host]
```

> [!TIP]
> {{% available_from "v1.30.2" anomaly %}} Multivariate Temporal Envelope applies each query's [`data_range`, `detection_direction`, and minimum relative deviation](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters) to every channel returned by that query before aggregating the joint anomaly score. The example detects CPU deviations in either direction, RAM increases of at least 15%, and network drops of at least 20% within each host model.

{{% /collapse %}}

{{% collapse name="Scale" %}}

### Scale

Previously available only to [ProphetModel](#prophet) and [OnlineQuantileModel](#online-seasonal-quantile),  the `scale` {{% available_from "v1.20.0" anomaly %}} parameter is now applicable to all models that support generating predictions (`yhat`, `yhat_lower`, `yhat_upper`). Also, it is **two-sided** now, represented as a list of two positive float values, allowing separate scaling for the intervals `[yhat, yhat_upper]` and `[yhat_lower, yhat]`. The new margins are calculated as:

- **Upper margin:** `|yhat_upper - yhat| * scale_upper`
- **Lower margin:** `|yhat - yhat_lower| * scale_lower`

For backward compatibility, the previous format (`scale: x`) remains supported and will be automatically converted to `scale: [x, x]`.

For example, setting `scale: [1.2, 0.75]` for particular model will:
- **Increase** the width of the lower confidence interval by **20%**.
- **Decrease** the width of the upper confidence boundary by **25%**.

Alternative visualization:

![two-sided scale comparison](schema_scale_overview_v2.webp)

The most common **use case** is when there is a preference to **widen one side** to blacklist smaller false positives (which otherwise would have [anomaly scores](https://docs.victoriametrics.com/anomaly-detection/faq/#how-is-anomaly-score-calculated) **only slightly higher than 1.0**, still making such data points **anomalous**), while **tightening the other side** to avoid missing true positives due to an overly loose margin (leading to [anomaly scores](https://docs.victoriametrics.com/anomaly-detection/faq/#how-is-anomaly-score-calculated) being slightly less than 1.0, making such data points **non-anomalous**).

```yaml
# other components like reader, writer, schedulers, monitoring ...
models:
  zscore_no_scale:
    class: 'zscore_online'
    z_threshold: 3
    # if not set, equals to [1.0, 1.0], meaning no scaling is applied
    # scale: [1.0, 1.0]
  zscore_scaled:
    class: 'zscore_online'
    z_threshold: 3
    # vs `zscore_no_scale`, increase lower confidence interval width by 1.2x, decrease upper confidence width by 25% (1.0 - 0.25 = 0.75), thus, making the model more conservative in flagging anomalies when y < yhat and more aggressive when y > yhat
    scale: [1.2, 0.75]
```

{{% /collapse %}}

{{% collapse name="Clip predictions" %}}

### Clip predictions

A post-processing step to **clip model predictions** (`yhat`, `yhat_lower`, and `yhat_upper` series) to the configured [`data_range` values](https://docs.victoriametrics.com/anomaly-detection/components/reader/#config-parameters) in `VmReader` is available.

This behavior is controlled by the boolean argument `clip_predictions` {{% available_from "v1.20.0" anomaly %}}:
- **Disabled by default** for backward compatibility.
- **Works** for models that generate predictions and estimates (e.g., [`ProphetModel`](#prophet)) by setting `clip_predictions` to `True` for respective model in `models` section.

The primary use case is to **align domain knowledge** about data behavior (defined via `data_range`) with what is shown in visualizations, such as in the [Grafana dashboard](https://docs.victoriametrics.com/anomaly-detection/presets/#grafana-dashboard). This ensures that predictions (`yhat`, `yhat_lower`, `yhat_upper`) are plotted consistently alongside real metric values (`y`) and remain within reasonable expected bounds.

> This parameter does not impact the generation of anomaly scores > 1 for datapoints where `y` falls outside the defined `data_range`.

```yaml
# other components like writer, schedulers, monitoring ...
reader:
  # ...
  queries:
    q1_clipped: 
      expr: 'q1_metricsql'
      data_range: [0, "inf"]
    q2_no_clip:
      expr: 'q2_metricsql'
      # if no data range defined, it will be implicitly converted to ["-inf", "inf"]
models:
  zscore_mixed:
    class: 'zscore_online'
    z_threshold: 3
    clip_predictions: True
    queries: [
      # `yhat`, `yhat_lower`, `yhat_upper` will be within [0, inf]
      # for all `zscore_mixed` instances that are fit on series returned by `q1_clipped` query
      # anomaly scores > 1 will still be produced for `y` outside of data_range
      'q1_clipped',
      # there will be no (explicit) clip of `yhat`, `yhat_lower`, `yhat_upper`
      # for all `zscore_mixed` instances that are fit on series returned by `q2_no_clip` query
      # even when `clip_predictions` arg is set, because data_range was not set for `q2_no_clip`
      'q2_no_clip',
    ]
  zscore_no_clip:
    class: 'zscore_online'
    z_threshold: 3
    # if not set, by default resolved to `clip_predictions: False`
    queries: [
      # `yhat`, `yhat_lower`, `yhat_upper` won't be clipped to [0, inf] 
      # even though `data_range` for `q1_clipped` is set
      # however, anomaly scores > 1 will still be produced for y outside of data_range
      'q1_clipped',
      # there will be no (explicit) clip of yhat, yhat_lower, yhat_upper  
      # for all `zscore_mixed` instances that are fit on series returned by `q2_no_clip` query
      # as `clip_predictions` arg is not set, regardless of data_range for `q2_no_clip`
      'q2_no_clip',
    ]
```

{{% /collapse %}}

{{% collapse name="Score outside data range" %}}

### Score outside data range

The `anomaly_score_outside_data_range` {{% available_from "v1.20.0" anomaly %}} parameter allows overriding the default **anomaly score (`1.01`)** assigned when actual values (`y`) fall **outside the defined `data_range` if defined in [reader](https://docs.victoriametrics.com/anomaly-detection/components/reader/)**. This provides greater flexibility for **alerting rule configurations** and enables **clearer visual differentiation** between different types of anomalies:

- By default, `y` values **outside `data_range`** trigger an anomaly score of `1.01`, which serves as a basic alerting rule.
- However, some users may require **higher anomaly scores** (e.g., `> 1.2`) to **trigger alerts reliably** in their monitoring setups.

**How it works**
- If **not set**, the **default value (`1.01`)** is used for backward compatibility.
- If defined at the **service level** (`settings` [section](https://docs.victoriametrics.com/anomaly-detection/components/settings/#anomaly-score-outside-data-range)), it applies to all models **unless overridden at the model level**.
- If set **per model**, it takes **priority over the global setting**.

**Example (override)**

```yaml
settings:
  # other parameters ...
  # all the models in `models` section will inherit this value unless overridden at the model level
  anomaly_score_outside_data_range: 1.2

models:
  model_score_override:
    class: 'zscore_online'
    # explicitly set, takes priority over `settings`'s value
    anomaly_score_outside_data_range: 1.5
  model_score_from_settings_level:
    class: 'zscore_online'
    # inherits from `settings`, will be `1.2`, same as setting
    # anomaly_score_outside_data_range: 1.2
```

**Example (default vs custom)**

```yaml
models:
  model_default_score:
    class: 'zscore_online'
    # default anomaly score (1.01) is applied when y is outside data_range, same as setting
    # anomaly_score_outside_data_range: 1.01
  model_higher_out_of_data_range_score:
    class: 'zscore_online'
    # explicitly set, takes priority over `settings`'s value
    anomaly_score_outside_data_range: 3.0  
```

{{% /collapse %}}

{{% collapse name="Decay" %}}

### Decay

> The `decay` argument works only in combination with [online models](#online-models) like [`OnlineMADModel`](#online-mad), [`ZScoreOnlineModel`](#online-z-score) or [`OnlineQuantileModel`](#online-seasonal-quantile).

The `decay` {{% available_from "v1.23.0" anomaly %}} argument is used to control the (exponential) **decay factor** for online models, which determines how quickly the model adapts to new data. It is a positive float value from `(0.0, 1.0]` interval, where:
- Value `1.0` means no decay (the model treats all data points equally, without giving more weight to recent ones). This is the default value for backward compatibility.
- Values less than `1.0` mean that the model will give more weight to recent data, effectively "forgetting" older data over time.

Roughly speaking, for the recent N datapoints model processes `decay` = `d` means that these datapoints will contribute to the model as [1 - d^X] percent of total importance, for example decay of
- `0.99` means that 100 recent datapoints will contribute as [1 - 0.99^100] = 63.23% of total importance
- `0.999` means that 1000 recent datapoints will contribute as [1 - 0.999^1000] = 63.23% of total importance

For example, if the model is updated every 5 minutes (`scheduler.infer_every`), on five 1-minute datapoints and there is a need to keep the last 1 day of data as the most impactful, setting `decay: 0.996` will ensure that the model has the last (86400/60) = 1440 datapoints contributing as [1 - 0.996^1440] = 99.6% of total importance, without the need to re-train the model on all 1440 datapoints every day with `fit_every: 1d` (which would be the limitation for [offline models](#offline-models)).

Example config:

```yaml
# other components like writer, schedulers, monitoring ...
reader:
  # ...
  queries:
    q1: metricsql_expression1
    # ...

models:
  online_zscore:
    class: 'zscore_online'
    z_threshold: 3.0
    decay: 0.996  # decay factor for online model, default is 1.0
    queries: ['q1']
```

{{% /collapse %}}

</div>
