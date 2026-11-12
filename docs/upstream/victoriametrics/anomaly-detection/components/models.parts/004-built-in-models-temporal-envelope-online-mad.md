<!-- Part 4 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

### Temporal Envelope

{{% available_from "v1.30.0" anomaly %}} Temporal Envelope is the preferred online model for complex operational and business metrics. It learns an evolving expected range from robust trend, calendar and holiday patterns, persistent level shifts, uncertainty, and optional future forecasts. The model adapts during inference while limiting the lasting influence of short-lived spikes.

> [!TIP]
> To evaluate improvements in trend and seasonal stability, consider the [experimental implementations](#experimental-temporal-envelope-implementations) below. Compare them with the default on representative data before adopting one.

{{% available_from "v1.30.1" anomaly %}} When the fit window ends in a recently established level, the model initializes its adaptive state from that recent regime while preserving supported calendar structure. This improves the first periodic predictions after a level shift and reduces false seasonal oscillation without requiring additional configuration.

> `TemporalEnvelopeModel` is [univariate](#univariate-models) and [online](#online-models). `TemporalEnvelopeMultivariateModel` also learns normal cross-series relationships as a [multivariate](#multivariate-models) model.

Use it for:

- infrastructure, application, or business metrics with trends and daily, weekly, monthly, or holiday behavior;
- deployments, traffic migrations, and capacity changes that create persistent shifts, including short-horizon forecasts through `forecast_at`;
- aligned related metrics where each channel keeps its own temporal pattern while their joint behavior contributes to one anomaly score.

For simple profiles without strong trend or seasonality, prefer [Online MAD](#online-mad) or [Online Z-score](#online-z-score). Existing [Prophet](#prophet) and [Isolation Forest](#isolation-forest-multivariate) configurations can be migrated to the corresponding univariate or multivariate Temporal Envelope form.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - `temporal_envelope` or the full class name `model.online.TemporalEnvelopeModel`.
- `model_version` (`v1` or `v2`, default `v1`) {{% available_from "v1.32.0" anomaly %}} - selects the implementation for either Temporal Envelope class. See [experimental implementations](#experimental-temporal-envelope-implementations) before switching.
- `quantiles` (list[float], default `[0.25, 0.75]`) - two ordered probabilities used as the base lower and upper residual boundaries. Values must be within `[0, 1]`.
- `iqr_threshold` (float, default `2.0`) - primary data-derived interval-width control. Higher values widen the ordinary residual envelope and produce fewer detections. Values from `1` to `4` are a practical experimentation range.
- `alpha` (float, default `0.005`) - **Trend Reactivity**. Higher values follow persistent level and trend changes faster; lower values produce steadier expectations. Values from `0.0025` to `0.02` are a practical experimentation range.
- `loss_reactivity` (float, default `5.0`) - controls how readily new deviations influence the model. Higher values adapt more readily; lower values reduce the influence of spikes. Values from `1` to `5` are a good starting range.
- `min_n_samples_seen` (integer, default `16`) - observations each model or group must see before anomaly scores are trusted. State and forecasts continue learning during warmup, while anomaly scores remain zero. Approximate warmup duration is this value multiplied by the query step.
- `changepoint_window` (integer, default `16`) - consecutive same-direction residuals required before treating a deviation as a persistent level shift. Use a value longer than ordinary anomaly bursts; approximate confirmation time is this value multiplied by the query step.
- `seasonalities` (list[string], default `['hod_smooth', 'dow_smooth']`) - recurring calendar patterns to model. Use an empty list when calendar patterns are known to be irrelevant. Supported presets are:
  - hour of day: `hod_smooth`, `hod_spiky`, `hod_plateau`;
  - day of week: `dow_smooth`, `dow_spiky`, `dow_plateau`;
  - weekday versus weekend: `weekpart_plateau`;
  - month of year: `month_smooth`, `month_plateau`.
- `holidays` (object, default `{}`) - known country holidays and special events. Supported keys are `countries` (country codes or names), `special_events` (recurring `MM-DD` or one-off `YYYY-MM-DD` dates), and `group` (whether configured events share one learned response). Holiday response shape is learned from data rather than configured publicly.
- `forecast_at` (list[string], default `[]`) - positive future offsets such as `['1h', '1d']`. Each offset adds point and, when requested through `provide_series`, lower and upper forecast series.

Preset suffixes describe expected profile shape: `smooth` represents gradual recurring curves, `spiky` represents narrow phase peaks, and `plateau` represents sustained calendar levels. Choose only profiles supported by the data. Calendar and holiday features use civil time from the configured query timezone, so hour/day profiles remain aligned across daylight-saving-time transitions.

Temporal Envelope also supports the [common model arguments](#common-args), including `queries`, `schedulers`, `provide_series`, `scale`, and `clip_predictions`. Configure `data_range`, `detection_direction`, `min_dev_from_expected`, `min_rel_dev_from_expected`, and query timezone under the corresponding [reader query](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters). The multivariate variant applies these business policies independently to each input channel {{% available_from "v1.30.2" anomaly %}}, so one model can represent combinations such as temperature above expected, power above expected, and clock below expected.

The multivariate variant uses `class: temporal_envelope_multivariate` or `model.online.TemporalEnvelopeMultivariateModel` and adds:

- `dependency_rank` (integer, default `8`) - compact rank used to represent cross-channel dependencies. Set it to `0` to disable dependency features.
- `score_aggregation` (`max`, `mean`, or `l2`; default `l2`) - combines per-channel boundary deviations into one anomaly score. `l2` uses their root-mean-square magnitude.
- `groupby` (list[string], optional) - metric label names used to fit a separate multivariate model for each unique label-value combination.
- `max_channels` (integer, default `1000`) - hard safety limit for input time series in one model instance.
- `recommended_max_channels` (integer, default `100`) - advisory limit; larger inputs up to `max_channels` are accepted with a warning because high-dimensional estimates may be less stable and more expensive.
- `random_state` (integer, default `42`) - seed used for reproducible dependency features.

The multivariate model emits only the joint `anomaly_score` by default to keep output cardinality bounded. Explicitly request channel-level `y`, `yhat`, `yhat_lower`, and `yhat_upper` families through `provide_series` only when those diagnostics are needed and the downstream cardinality is acceptable.

{{% /collapse %}}

{{% collapse name="Configuration examples" %}}

Univariate monitoring with calendar and holiday behavior:

```yaml
models:
  operations_envelope:
    class: temporal_envelope
    queries: [request_rate, latency]
    seasonalities: [hod_smooth, dow_smooth, weekpart_plateau]
    alpha: 0.005
    loss_reactivity: 5
    iqr_threshold: 2
    changepoint_window: 16
    holidays:
      countries: [US]
      special_events: ['12-24']
      group: true
    forecast_at: [1h, 1d]
    provide_series: [anomaly_score, yhat, yhat_lower, yhat_upper]
```

Multivariate monitoring with one dependency model per cluster:

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

For independent per-series detection, use `temporal_envelope`. Use `temporal_envelope_multivariate` only when the relationship between aligned series is itself meaningful; each channel still learns its own trend and calendar patterns.

{{% /collapse %}}

</div>

#### Experimental Temporal Envelope implementations

> [!NOTE]
> These opt-in research candidates let you evaluate improvements before they become the default. Behavior and state formats may evolve. V1 remains the default; compare detection quality and resource use on representative history before adopting another implementation. Switching implementations requires a fresh fit.

##### V2

{{% available_from "v1.32.0" anomaly %}} V2 targets more stable trend and calendar-seasonal learning, particularly around trend changes and seasonal transitions.

Select `model_version: v2` with either `temporal_envelope` or `temporal_envelope_multivariate`:

```yaml
models:
  seasonal:
    class: temporal_envelope
    model_version: v2
    seasonalities: [hod_smooth, dow_smooth]
# ...
```

V2 learns and forecasts seasonal patterns in civil time, using the query timezone, including daylight-saving transitions. It retains the public Temporal Envelope configuration and query-policy interface. Check `GET /api/v1/model/schema?model_class=temporal_envelope` in the [interactive API reference](https://docs.victoriametrics.com/anomaly-detection/components/server/#interactive-api-reference) for supported settings, and tune the selected implementation rather than transferring parameters on the assumption of identical behavior.

> [!WARNING]
> Switching between v1 and v2 requires a fresh fit; their learned state is not interchangeable. Snapshots are compressed losslessly in v1.32.0, while older raw snapshots remain readable. Rolling back to v1.31.1 or earlier requires resetting persisted state, refitting models, and removing every `model_version: v2` setting. See [state compatibility](https://docs.victoriametrics.com/anomaly-detection/migration/#compatibility-matrix).


### Online MAD

> `OnlineMADModel` is a [univariate](#univariate-models), [online](#online-models) model.

The MAD model is a robust method for anomaly detection that is *less sensitive* to outliers in data compared to standard deviation-based models. It considers a point as an anomaly if the absolute deviation from the median is significantly large. This is the online approximate version, based on [t-digests](https://www.sciencedirect.com/science/article/pii/S2665963820300403) for online quantile estimation{{% available_from "v1.15.0" anomaly %}}.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.online.OnlineMADModel"` (or `mad_online` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `threshold` (float, optional) - The threshold multiplier for the MAD to determine anomalies. Defaults to `2.5`. Higher values will identify fewer points as anomalies.
- `min_n_samples_seen` (int, optional) - the minimum number of samples to be seen (`n_samples_seen_` property) before computing the anomaly score. Otherwise, the **anomaly score will be 0**, as there is not enough data to trust the model's predictions. Defaults to 16.
- `history_strength` (float, optional) - {{% available_from "v1.30.0" anomaly %}} strength of the initial history learned by `fit`. Values above `1` preserve fitted quantiles initially but reduce the leverage of subsequent updates. Defaults to `1`.
- `decay` (float, optional) - exponential forgetting factor in `(0, 1]`. Defaults to `1.0` (no forgetting). Values below `1` reduce the weight of older observations so the online baseline can adapt without periodic refitting; faster forgetting can also absorb sustained anomalies. See [decay](#decay) for background.
- `compression` (int, optional) - the compression parameter for  underlying [t-digest](https://www.sciencedirect.com/science/article/pii/S2665963820300403). Higher values mean higher accuracy but higher memory usage. By default 100.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}


```yaml
models:
  your_desired_alias_for_a_model:
    class: "mad_online"  # or 'model.online.OnlineMADModel'
    threshold: 2.5
    min_n_samples_seen: 128  # i.e. calculate it as full seasonality / data freq
    history_strength: 2  # retain fitted history as a stronger prior
    decay: 1.0  # no forgetting; use a value below 1 for an adapting baseline
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
