<!-- Part 8 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

## Deprecations

{{% collapse name="Deprecated model types and models" %}}

Here is a list of all deprecated model types and specific models with respective version info and suggestions for migration.

### Deprecated types

[Rolling models](#rolling-models) - starting from [v1.28.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1280) all rolling models are deprecated in favor of their online counterparts with respective documentation adjustments. **Now every model class is [non-rolling](#non-rolling-models)**.

#### Rolling Models

> Rolling models as a class were deprecated {{% deprecated_from "v1.28.0" anomaly %}} in favor of [online models](#online-models), which provide similar benefits with additional advantages. Respective rolling models are refactored into online models (e.g., [RollingQuantile](#rolling-quantile)). Existing configurations that use rolling models' aliases will continue to function, with less limitations (e.g. no constraint on `fit_every` == `infer_every`). **Description below is kept for older deployments and hyperlinks consistency**.

A rolling model is a model that, once trained, **cannot be (naturally) used to make inference on data, not seen during its fit phase**.

An instance of rolling model is **simultaneously fit and used for inference** during its `infer` method call.

As a result, such model instances are **not stored** between consecutive re-fit calls (defined by `fit_every` [arg](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#periodic-scheduler) in `PeriodicScheduler`), leading to **lower RAM** consumption.

Such models put **more pressure** on your reader's source, i.e. if your model should be fit on large amount of data (say, 14 days with 1-minute resolution) and at the same time you have **frequent inference** (say, once per minute) on new chunks of data - that's because such models require (fit + infer) window of data to be fit first to be used later in each inference call.

> Rolling models require `fit_every` to be either unset or explicitly set equal to `infer_every` in [PeriodicScheduler](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#periodic-scheduler).

**Examples:** [RollingQuantile](#rolling-quantile), **prior to [v1.28.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1280)** where it become online model.

![vmanomaly-model-type-rolling](model-type-rolling.webp)

#### Non-Rolling Models

> The section is moved to deprecations as **Every model class is now {{% available_from "v1.28.0" anomaly %}} non-rolling**. Configurations that used rolling models' aliases will continue to function, with less limitations (e.g. no constraint on `fit_every` == `infer_every`). **Description below is kept for older deployments and hyperlinks consistency**.

Everything that is not classified as [rolling](#rolling-models). 

Produced models can be explicitly used to **infer on data, not seen during its fit phase**, thus, it **doesn't require re-fit procedure**.

Such models put **less pressure** on your reader's source, i.e. if you fit on large amount of data (say, 14 days with 1-minute resolution) but do it occasionally (say, once per day), at the same time you have **frequent inference**(say, once per minute) on new chunks of data

> However, it's still highly recommended, to keep your model up-to-date with tendencies found in your data as it evolves in time.

Produced model instances are **stored in-memory** between consecutive re-fit calls (defined by `fit_every` [arg](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#periodic-scheduler) in `PeriodicScheduler`), leading to **higher RAM** consumption.

**Examples:** [Prophet](#prophet)

![vmanomaly-model-type-non-rolling](model-type-non-rolling.webp)

### Deprecated models

#### [Z-score](https://en.wikipedia.org/wiki/Standard_score)

> `ZScoreModel` is a [univariate](#univariate-models), [offline](#offline-models) model. {{% deprecated_from "v1.28.4" anomaly %}} Was removed in favor of its online version to improve data efficiency and reduce user confusion. **Configs that used this model (where model's class is `zscore` or `model.zscore.ZscoreModel`) will continue to work, with a warning raised while actually changed to the online version under the hood. Suggestion is to replace it with `zscore_online` or `model.online.OnlineZscoreModel` class explicitly to get [online model benefits](https://docs.victoriametrics.com/anomaly-detection/faq/#online-models) for data querying by reducing `fit_every` frequency**.

Model is useful for initial testing and for simpler data ([de-trended](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend) data without strict [seasonality](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality) and with anomalies of similar magnitude as your "normal" data).

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.zscore.ZscoreModel"` (or `zscore` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `z_threshold` (float, optional) - [standard score](https://en.wikipedia.org/wiki/Standard_score) for calculation boundaries and anomaly score. Defaults to `2.5`.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}

```yaml
models:
  your_desired_alias_for_a_model:
    class: "zscore"  # or 'model.zscore.ZscoreModel' until v1.13.0
    z_threshold: 3.5
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

#### [MAD (Median Absolute Deviation)](https://en.wikipedia.org/wiki/Median_absolute_deviation)

> `MADModel` is a [univariate](#univariate-models), [offline](#offline-models) model. {{% deprecated_from "v1.28.4" anomaly %}} Was removed in favor of its online version to improve data efficiency and reduce user confusion. **Configs that used this model (where model's class is `mad` or `model.mad.MADModel`) will continue to work, with a warning raised while actually changed to the online version under the hood. Suggestion is to replace it with `mad_online` or `model.online.OnlineMADModel` class explicitly to get [online model benefits](https://docs.victoriametrics.com/anomaly-detection/faq/#online-models) for data querying by reducing `fit_every` frequency**.

The MAD model is a robust method for anomaly detection that is *less sensitive* to outliers in data compared to standard deviation-based models. It considers a point as an anomaly if the absolute deviation from the median is significantly large.

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.mad.MADModel"` (or `mad` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `threshold` (float, optional) - The threshold multiplier for the MAD to determine anomalies. Defaults to `2.5`. Higher values will identify fewer points as anomalies.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}


```yaml
models:
  your_desired_alias_for_a_model:
    class: "mad"  # or 'model.mad.MADModel' until v1.13.0
    threshold: 2.5
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

{{% /collapse %}}
