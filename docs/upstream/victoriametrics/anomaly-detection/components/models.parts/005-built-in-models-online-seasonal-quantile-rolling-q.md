<!-- Part 5 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

### Online Seasonal Quantile

> `OnlineQuantileModel` is a [univariate](#univariate-models), [online](#online-models) model.

Online (seasonal) quantile utilizes a set of approximate distributions, based on [t-digests](https://www.sciencedirect.com/science/article/pii/S2665963820300403) for online quantile estimation {{% available_from "v1.15.0" anomaly %}}.

Best used on **[de-trended](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend) data with strong (potentially multiple) [seasonalities](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality)**. Can act as a (slightly less flexible) replacement to [`ProphetModel`](#prophet).

It uses the `quantiles` triplet to calculate `yhat_lower`, `yhat`, and `yhat_upper` [output](#vmanomaly-output), respectively, for each of the `min_subseason` sub-intervals contained in `seasonal_interval`. For example, with '4d' + '2h' seasonality patterns (multiple), it will hold and update 24*4 / 2 = 48 consecutive estimates (each 2 hours long).

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.online.OnlineQuantileModel"` (or `quantile_online` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `quantiles` (list[float], optional) - The quantiles to estimate. `yhat_lower`, `yhat`, `yhat_upper` are the quantile order. By default (0.01, 0.5, 0.99).
- `iqr_threshold` (float, optional) - {{% available_from "v1.25.0" anomaly %}} The [interquartile range (IQR)](https://en.wikipedia.org/wiki/Interquartile_range) multiplier to increase the width of the prediction intervals. Defaults to 0 (no adjustment) for backward compatibility. If set > 0, the model will add IQR * `iqr_threshold` to `yhat_lower` and  `yhat_upper` (respecting `min_subseason` seasonal buckets). This is useful for data with high variance or outliers, as it helps to avoid false positives in anomaly detection. Best used with **robust** `quantiles` set to (0.25, 0.5, 0.75) or similar.
- `seasonal_interval` (string, optional) - the interval for the seasonal adjustment. If not set, the model will equal to a simple online quantile model. By default not set.
- `min_subseason` (str, optional) - the minimum interval to estimate quantiles for. By default not set. Note that the minimum interval should be a multiple of the seasonal interval, i.e. if seasonal_interval='2h', then min_subseason='15m' is valid, but '37m' is not.
- `use_transform` (bool, optional) - whether to internally apply a `log1p(abs(x)) * sign(x)` transformation to the data to stabilize internal quantile estimation. Does not affect the scale of produced output (i.e. `yhat`) By default False.
- `global_smoothing` (float, optional) - the smoothing parameter for the global quantiles. i.e. the output is a weighted average of the global and seasonal quantiles (if `seasonal_interval` and `min_subseason` args are set). Should be from `[0, 1]` interval, where 0 means no smoothing and 1 means using only global quantile values.
- `scale` (float, optional) - Is used to adjust the margins between `yhat` and [`yhat_lower`, `yhat_upper`]. New margin = `|yhat_* - yhat_lower| * scale`. Defaults to 1 (no scaling is applied). See `scale`[common arg](https://docs.victoriametrics.com/anomaly-detection/components/models/#scale) section for detailed instructions and 2-sided option.
- `season_starts_from` (str, optional) - the start date for the seasonal adjustment, as a reference point to start counting the intervals. By default '1970-01-01'.
- `min_n_samples_seen` (int, optional) - the minimum number of samples to be seen (`n_samples_seen_` property) before computing the anomaly score. Otherwise, the **anomaly score will be 0**, as there is not enough data to trust the model's predictions. Defaults to 16.
- `history_strength` (float, optional) - {{% available_from "v1.30.0" anomaly %}} strength of the initial history learned by `fit`. Values above `1` preserve fitted quantiles initially but reduce the leverage of subsequent updates. Defaults to `1`.
- `compression` (int, optional) - the compression parameter for the underlying [t-digests](https://www.sciencedirect.com/science/article/pii/S2665963820300403). Higher values mean higher accuracy but higher memory usage. By default 100.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}

Suppose we have a data with strong intra-day (hourly) and intra-week (daily) seasonality, data granularity is '5m' with up to 5% expected outliers present in data. Then you can apply similar config:

```yaml
models:
  your_desired_alias_for_a_model:
    class: "quantile_online"  # or 'model.online.OnlineQuantileModel'
    quantiles: [0.25, 0.5, 0.75]  # lowered to exclude anomalous edges, can be compensated by `scale` param > 1 and `iqr_threshold` > 0
    iqr_threshold: 2.5  # to increase prediction intervals' width to avoid false positives while still keeping the model robust
    seasonal_interval: '7d'  # longest seasonality (week, day) = week, starting from `season_starts_from`
    min_subseason: '1h'  # smallest seasonality (week, day, hour) = hour, will have its own quantile estimates
    min_n_samples_seen: 288 # 1440 / 5 - at least 1 full day, ideal = 1440 / 5 * 7 - one full week (seasonal_interval)
    history_strength: 2  # retain fitted history as a stronger prior
    scale: 1.1  # to compensate lowered quantile boundaries with wider intervals
    season_starts_from: '2024-01-01'  # interval calculation starting point, especially for uncommon seasonalities like '36h' or '12d'
    compression: 100  # higher values mean higher accuracy but higher memory usage
    provide_series: ['anomaly_score', 'yhat']  # common arg example
    # Common arguments for built-in model, if not set, default to
    # See https://docs.victoriametrics.com/anomaly-detection/components/models/#common-args
    #
    # provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper']
    # schedulers: [
    #   all scheduler aliases defined in `scheduler` section,
    # ]
    # queries: [
    #   all query aliases defined in `reader.queries` section,
    # ]
    # Configure detection_direction and minimum-deviation policies under reader.queries.<alias> (query-level from v1.30.2).
    # scale: [1.0, 1.0]  # if needed, prediction intervals' width can be increased (>1) or narrowed (<1)
    # clip_predictions: False  # if data_range for respective `queries` is set in reader, `yhat.*` columns will be clipped
    # anomaly_score_outside_data_range: 1.01  # auto anomaly score (1.01) if `y` (real value) is outside of data_range, if set
```

{{% /collapse %}}

</div>

Resulting metrics of the model are described [here](#vmanomaly-output).



### Online Z-score

> `OnlineZscoreModel` is a [univariate](#univariate-models), [online](#online-models) model.

Online version of existing [Z-score](#z-score) implementation with the same exact behavior and implications {{% available_from "v1.15.0" anomaly %}}.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.online.OnlineZscoreModel"` (or `zscore_online`with class alias support{{% available_from "v1.13.0" anomaly %}})
- `z_threshold` (float, optional) - [standard score](https://en.wikipedia.org/wiki/Standard_score) for calculation boundaries and anomaly score. Defaults to `2.5`.
- `min_n_samples_seen` (int, optional) - the minimum number of samples to be seen (`n_samples_seen_` property) before computing the anomaly score. Otherwise, the **anomaly score will be 0**, as there is not enough data to trust the model's predictions. Defaults to 16.
- `history_strength` (float, optional) - {{% available_from "v1.30.0" anomaly %}} strength of the initial history learned by `fit`. Values above `1` keep fitted mean and variance unchanged initially but reduce the leverage of subsequent updates. Defaults to `1`.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}

```yaml
models:
  your_desired_alias_for_a_model:
    class: "zscore_online"  # or 'model.online.OnlineZscoreModel'
    z_threshold: 3.5
    min_n_samples_seen: 128  # i.e. calculate it as full seasonality / data freq
    history_strength: 2  # retain fitted history as a stronger prior
    provide_series: ['anomaly_score', 'yhat']  # common arg example
    # Common arguments for built-in model, if not set, default to
    # See https://docs.victoriametrics.com/anomaly-detection/components/models/#common-args
    #
    # provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper']
    # schedulers: [
    #   all scheduler aliases defined in `scheduler` section,
    # ]
    # queries: [
    #   all query aliases defined in `reader.queries` section,
    # ]
    # Configure detection_direction and minimum-deviation policies under reader.queries.<alias> (query-level from v1.30.2).
    # scale: [1.0, 1.0]  # if needed, prediction intervals' width can be increased (>1) or narrowed (<1)
    # clip_predictions: False  # if data_range for respective `queries` is set in reader, `yhat.*` columns will be clipped
    # anomaly_score_outside_data_range: 1.01  # auto anomaly score (1.01) if `y` (real value) is outside of data_range, if set
```

{{% /collapse %}}

</div>

Resulting metrics of the model are described [here](#vmanomaly-output).



### [Rolling Quantile](https://en.wikipedia.org/wiki/Quantile)

> `RollingQuantileModel` **is** {{% available_from "v1.28.0" anomaly %}} a [univariate](#univariate-models), [online](#online-models) model. It **was** {{% deprecated_from "v1.28.0" anomaly %}} a [univariate](#univariate-models), [rolling](#rolling-models), [offline](#offline-models) model.

This model is best used on **data with short evolving patterns** (i.e. 10-100 datapoints of particular frequency), as it adapts to changes over a rolling window.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.rolling_quantile.RollingQuantileModel"` (or `rolling_quantile` with class alias support {{% available_from "v1.13.0" anomaly %}})
- `quantile` (float) - quantile value, from 0.5 to 1.0. This constraint is implied by 2-sided confidence interval.
- `window_steps` (integer) - size of the moving window. (see 'sampling_period')
- `iqr_threshold` (float, optional) - {{% available_from "v1.25.0" anomaly %}} The [interquartile range (IQR)](https://en.wikipedia.org/wiki/Interquartile_range) multiplier to increase the width of the prediction intervals. Defaults to 0 (no adjustment) for backward compatibility. If set > 0, the model will add half IQR * `iqr_threshold` to `yhat_lower` and  `yhat_upper`. This is useful for data with high variance or outliers, as it helps to avoid false positives in anomaly detection.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}

```yaml
models:
  your_desired_alias_for_a_model:
    class: "rolling_quantile"
    quantile: 0.9
    window_steps: 96
    iqr_threshold: 1
    # Common arguments for built-in model, if not set, default to
    # See https://docs.victoriametrics.com/anomaly-detection/components/models/#common-args
    #
    # provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper']
    # schedulers: [
    #   all scheduler aliases defined in `scheduler` section,
    # ]
    # queries: [
    #   all query aliases defined in `reader.queries` section,
    # ]
    # Configure detection_direction and minimum-deviation policies under reader.queries.<alias> (query-level from v1.30.2).
    # scale: [1.0, 1.0]  # if needed, prediction intervals' width can be increased (>1) or narrowed (<1)
    # clip_predictions: False  # if data_range for respective `queries` is set in reader, `yhat.*` columns will be clipped
    # anomaly_score_outside_data_range: 1.01  # auto anomaly score (1.01) if `y` (real value) is outside of data_range, if set
```

{{% /collapse %}}

</div>

Resulting metrics of the model are described [here](#vmanomaly-output).
