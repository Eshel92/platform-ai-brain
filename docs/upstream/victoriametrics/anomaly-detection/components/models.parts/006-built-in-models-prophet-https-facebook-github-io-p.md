<!-- Part 6 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

### [Prophet](https://facebook.github.io/prophet/)
`vmanomaly` uses the Facebook Prophet implementation for time series forecasting, with detailed usage provided in the [Prophet library documentation](https://facebook.github.io/prophet/docs/quick_start#python-api). All original Prophet parameters are supported and can be directly passed to the model via `args` argument.

> `ProphetModel` is a [univariate](#univariate-models), [offline](#offline-models) model.


> [!NOTE]
> Prophet is planned for deprecation in a future release. For new forecasting and anomaly-detection deployments, prefer the online [Temporal Envelope](#temporal-envelope) model unless Prophet-specific decomposition output is required.

> {{% available_from "v1.25.3" anomaly %}} Producing forecasts for future timestamps is now supported. To enable this, set the `forecast_at` argument to a list of relative future offsets (e.g., `['1h', '1d']`). The model will then generate forecasts for these future timestamps, which can be useful for planning and resource allocation. Output series are affected by [provide_series](#provide-series) argument, which need to include at least `yhat` for point-wise forecasts (and `yhat_lower` or/and `yhat_upper` for respective confidence intervals). See the example below for more details.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.prophet.ProphetModel"` (or `prophet` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `seasonalities` (list[dict], optional): Additional seasonal components to include in Prophet. See Prophet’s [`add_seasonality()`](https://facebook.github.io/prophet/docs/seasonality,_holiday_effects,_and_regressors#modeling-holidays-and-special-events:~:text=modeling%20the%20cycle-,Specifying,-Custom%20Seasonalities) documentation for details.
- `scale`{{% available_from "v1.18.0" anomaly %}} (float): Is used to adjust the margins between `yhat` and [`yhat_lower`, `yhat_upper`]. New margin = `|yhat_* - yhat_lower| * scale`. Defaults to 1 (no scaling is applied). See `scale`[common arg](https://docs.victoriametrics.com/anomaly-detection/components/models/#scale) section for detailed instructions and 2-sided option.
- `tz_aware`{{% available_from "v1.18.0" anomaly %}} (bool): Enables handling of timezone-aware timestamps. Default is `False`. Should be used with `tz_seasonalities` and `tz_use_cyclical_encoding` parameters.
- `tz_seasonalities`{{% available_from "v1.18.0" anomaly %}} (list[dict]): Specifies timezone-aware seasonal components. Requires `tz_aware=True`. Supported options include `minute`, `hod` (hour of day), `dow` (day of week), and `month` (month of year). {{% available_from "v1.18.2" anomaly %}} users can configure additional parameters for each seasonality, such as `fourier_order`, `prior_scale`, and `mode`. For more details, please refer to the **Timezone-unaware** configuration example below.
  > {{% available_from "v1.18.2" anomaly %}} the format for `tz_seasonalities` has been updated to enhance flexibility. Previously, it accepted a list of strings (e.g., `['hod', 'minute']`). Now, it follows the same structure as custom seasonalities defined in the `seasonalities` argument (e.g., `{"name": "hod", "fourier_order": 5, "mode": "additive"}`). This change is backward-compatible, so older configurations will be automatically converted to the new format using default values.
- `tz_use_cyclical_encoding`{{% available_from "v1.18.0" anomaly %}} (bool): If set to `True`, applies [cyclical encoding technique](https://www.kaggle.com/code/avanwyk/encoding-cyclical-features-for-deep-learning) to timezone-aware seasonalities. Should be used with `tz_aware=True` and `tz_seasonalities`.
- `forecast_at`{{% available_from "v1.25.3" anomaly %}} (list[str]): Specifies future relative offsets for which forecasts should be generated (e.g., `['1h', '1d']`). Works similarly to [predict_linear](https://docs.victoriametrics.com/victoriametrics/metricsql/#predict_linear) in MetricQL, but with more flexibility and seasonality support - produced series will have *the same timestamp* as the other [output](#vmanomaly-output) series, but with the forecasted value for the *future timestamp*. Defaults to `[]` (empty list, meaning no future forecasts are produced). If set, `provide_series` must include at least `yhat` for point-wise forecasts (and `yhat_lower` or/and `yhat_upper` for respective confidence intervals). For example, if `forecast_at` is set to `['1h', '1d']`, the model will produce forecasts for both the next hour and the next day, and these series can be accessed by `yhat_1h`, `yhat_lower_1h`, `yhat_upper_1h`, `yhat_1d`, `yhat_lower_1d`, and `yhat_upper_1d` in the output, respectively. See [FAQ](https://docs.victoriametrics.com/anomaly-detection/faq/#forecasting) for more details.

> [!WARNING]
> `forecast_at` parameter can lead to **significant increase in active timeseries** if you have a lot of time series returned by your queries, as it will produce additional series for each of the future timestamps specified in `forecast_at` (optionally multiplied by 1-3 if interval forecasts are included). For example, if you have 1000 time series returned by your query and set `forecast_at` to `[1h, 1d, 1w]`, and `provide_series` includes `yhat_lower` and `yhat_upper`, it will produce 1000 (series) * 3 (intervals) * 3 (predictions, point + interval) = 9000 additional timeseries. Consider using it only on small subset of metrics (e.g. grouped by `host` or `region`) to avoid this issue, as it also **proportionally (to the number of `forecast_at` elements) increases the timings of inference calls**.

- `compression` {{% available_from "v1.28.1" anomaly %}} (dict, optional): Configuration for downsampling input data before fitting the model. Useful for high-frequency data to reduce CPU and RAM/disk load and improve model performance. The `compression` block supports the following parameters:
  - `window` (str, required): Time window for downsampling (e.g., "5m", "1h").
  - `agg_method` (str, optional, default="mean"): Aggregation function to apply within each window. Supported values: "mean", "median".
  - `adjust_boundaries` (bool, optional, default=true): Whether to adjust confidence interval boundaries after downsampling. If true, `yhat_lower` and `yhat_upper` will be adjusted based on the aggregated vs original data variability.

{{% /collapse %}}

{{% collapse name="Configuration examples" %}}

Timezone-unaware example:

```yaml
models:
  your_desired_alias_for_a_model:
    class: 'prophet'  # or 'model.prophet.ProphetModel' until v1.13.0
    provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper', 'trend']
    # Common arguments for built-in model, if not set, default to
    # See https://docs.victoriametrics.com/anomaly-detection/components/models/#common-args
    #
    # provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper', 'trend']
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
    seasonalities:
      - name: 'hourly'
        period: 0.04166666666
        fourier_order: 30
        prior_scale: 20
    compression:  # downsample input data to reduce CPU/RAM load
      window: '30m'  # downsample to 30-minute intervals
      agg_method: 'mean'  # use mean aggregation within each window
      adjust_boundaries: true  # adjust yhat_lower/yhat_upper after downsampling
    # inner model args (key-value pairs) accepted by
    # https://facebook.github.io/prophet/docs/quick_start#python-api
    args:
      interval_width: 0.98  # see https://facebook.github.io/prophet/docs/uncertainty_intervals
      country_holidays: 'US'
```

Timezone-aware example:

```yaml
models:
  your_desired_alias_for_a_model:
    class: 'prophet'  # or 'model.prophet.ProphetModel' until v1.13.0
    provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper', 'trend']
    # Common arguments for built-in model, if not set, default to
    # See https://docs.victoriametrics.com/anomaly-detection/components/models/#common-args
    #
    # provide_series: ['anomaly_score', 'yhat', 'yhat_lower', 'yhat_upper', 'trend']
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
    tz_aware: True
    tz_use_cyclical_encoding: True
    tz_seasonalities: # intra-day + intra-week seasonality, no intra-year / sub-hour seasonality
      - name: 'hod'  # intra-day seasonality, hour of the day
        fourier_order: 5  # keep it 3-8 based on intraday pattern complexity
        prior_scale: 10
      - name: 'dow'  # intra-week seasonality, time of the week
        fourier_order: 2  # keep it 2-4, as dependencies are learned separately for each weekday
    compression:  # downsample input data to reduce CPU/RAM load
      window: '30m'  # downsample to 30-minute intervals
      agg_method: 'mean'  # use mean aggregation within each window
      adjust_boundaries: true  # adjust yhat_lower/yhat_upper after downsampling
    # inner model args (key-value pairs) accepted by
    # https://facebook.github.io/prophet/docs/quick_start#python-api
    args:
      interval_width: 0.98  # see https://facebook.github.io/prophet/docs/uncertainty_intervals
      country_holidays: 'US'
```

{{% /collapse %}}

</div>

> Apart from standard [`vmanomaly` output](#vmanomaly-output), Prophet model can provide additional metrics.

**Additional output metrics produced by FB Prophet**
Depending on chosen `seasonality` parameter FB Prophet can return additional metrics such as:
- `trend`, `trend_lower`, `trend_upper`
- `additive_terms`, `additive_terms_lower`, `additive_terms_upper`,
- `multiplicative_terms`, `multiplicative_terms_lower`, `multiplicative_terms_upper`,
- `daily`, `daily_lower`, `daily_upper`,
- `hourly`, `hourly_lower`, `hourly_upper`,
- `holidays`, `holidays_lower`, `holidays_upper`,
- and a number of columns for each holiday if `holidays` param is set

Resulting metrics of the model are described [here](#vmanomaly-output)


### [Isolation forest](https://en.wikipedia.org/wiki/Isolation_forest) (Multivariate)

> `IsolationForestModel` is a [univariate](#univariate-models), [offline](#offline-models) model.

> `IsolationForestMultivariateModel` is a [multivariate](#multivariate-models), [offline](#offline-models) model.

> [!NOTE]
> Both univariate `isolation_forest` and multivariate `isolation_forest_multivariate` are planned for deprecation in a future release. For new deployments, use the corresponding univariate or multivariate online [Temporal Envelope](#temporal-envelope) model.

Detects anomalies using binary trees. The algorithm has a linear time complexity and a low memory requirement, which works well with high-volume data. It can be used on both univariate and multivariate data, but it is more effective in multivariate case.

**Important**: Be aware of [the curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality). Don't use single multivariate model if you expect your queries to return many time series of less datapoints that the number of metrics. In such case it is hard for a model to learn meaningful dependencies from too sparse data hypercube.

Here we use Isolation Forest implementation from `scikit-learn` [library](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest). All parameters from this library can be passed to the model.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.isolation_forest.IsolationForestMultivariateModel"` (or `isolation_forest_multivariate` with class alias support {{% available_from "v1.13.0" anomaly %}})

- `contamination` (float or string, optional) - The amount of contamination of the data set, i.e. the proportion of outliers in the data set. Used when fitting to define the threshold on the scores of the samples. Default value - "auto". Should be either `"auto"` or be in the range (0.0, 0.5]. {{% available_from "v1.29.5" anomaly %}} Numeric strings, such as `"0.01"`, are accepted, while invalid non-finite values, such as `nan`, `inf`, and `-inf`, are rejected during config validation.

- `seasonal_features` (list of string) - List of seasonality to encode through [cyclical encoding](https://towardsdatascience.com/cyclical-features-encoding-its-about-time-ce23581845ca), i.e. `dow` (day of week). **Introduced in [1.12.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1120)**.
  - Empty by default for backward compatibility.
  - Example: `seasonal_features: ['dow', 'hod']`.
  - Supported seasonalities:
    - "minute" - minute of hour (0-59)
    - "hod" - hour of day (0-23)
    - "dow" - day of week (1-7)
    - "month" - month of year (1-12)

- `args` (dict, optional) - Inner model args (key-value pairs). See accepted params in [model documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest). Defaults to empty (not provided). Example:  {"random_state": 42, "n_estimators": 100}

{{% /collapse %}}

{{% collapse name="Configuration example" %}}


```yaml
models:
  your_desired_alias_for_a_model:
    # To use univariate model, substitute class argument with "model.isolation_forest.IsolationForestModel".
    class: "isolation_forest_multivariate" # or 'model.isolation_forest.IsolationForestMultivariateModel' until v1.13.0
    contamination: "0.01"
    provide_series: ['anomaly_score']
    seasonal_features: ['dow', 'hod']
    args:
      n_estimators: 100
      # i.e. to assure reproducibility of produced results each time model is fit on the same input
      random_state: 42
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
    # anomaly_score_outside_data_range: 1.01  # auto anomaly score (1.01) if `y` (real value) is outside of data_range, if set
```

{{% /collapse %}}

</div>

Resulting metrics of the model are described [here](#vmanomaly-output).


### [Holt-Winters](https://en.wikipedia.org/wiki/Exponential_smoothing)

> `HoltWinters` is a [univariate](#univariate-models), [offline](#offline-models) model.

> [!NOTE]
> Holt-Winters is planned for deprecation in a future release. For new deployments, prefer the online [Temporal Envelope](#temporal-envelope) model.

Here we use Holt-Winters Exponential Smoothing implementation from `statsmodels` [library](https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing). All parameters from this library can be passed to the model.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.holtwinters.HoltWinters"` (or `holtwinters` with class alias support{{% available_from "v1.13.0" anomaly %}})

- `frequency` (string) - Must be set equal to sampling_period. Model needs to know expected data-points frequency (e.g. '10m'). If omitted, frequency is guessed during fitting as **the median of intervals between fitting data timestamps**. During inference, if incoming data doesn't have the same frequency, then it will be interpolated.  E.g. data comes at 15 seconds resolution, and our resample_freq is '1m'. Then fitting data will be downsampled to '1m' and internal model is trained at '1m' intervals. So, during inference, prediction data would be produced at '1m' intervals, but interpolated to "15s" to match with expected output, as output data must have the same timestamps. As accepted by pandas.Timedelta (e.g. '5m').

- `seasonality` (string, optional) - As accepted by pandas.Timedelta.

- If `seasonal_periods` is not specified, it is calculated as `seasonality` / `frequency`
Used to compute "seasonal_periods" param for the model (e.g. '1D' or '1W').

- `z_threshold` (float, optional) - [standard score](https://en.wikipedia.org/wiki/Standard_score) for calculating boundaries to define anomaly score. Defaults to 2.5.


*Default model parameters*:

- If [parameter](https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing#statsmodels.tsa.holtwinters.ExponentialSmoothing-parameters) `seasonal` is not specified, default value will be `add`.

- If [parameter](https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing#statsmodels.tsa.holtwinters.ExponentialSmoothing-parameters) `initialization_method` is not specified, default value will be `estimated`.

- `args` (dict, optional) - Inner model args (key-value pairs). See accepted params in [model documentation](https://www.statsmodels.org/dev/generated/statsmodels.tsa.holtwinters.ExponentialSmoothing#statsmodels.tsa.holtwinters.ExponentialSmoothing-parameters). Defaults to empty (not provided). Example:  {"seasonal": "add", "initialization_method": "estimated"}

{{% /collapse %}}

{{% collapse name="Configuration example" %}}

```yaml
models:
  your_desired_alias_for_a_model:
    class: "holtwinters"  # or 'model.holtwinters.HoltWinters' until v1.13.0
    seasonality: '1d'
    frequency: '1h'
    # Inner model args (key-value pairs) accepted by statsmodels.tsa.holtwinters.ExponentialSmoothing
    args:
      seasonal: 'add'
      initialization_method: 'estimated'
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
