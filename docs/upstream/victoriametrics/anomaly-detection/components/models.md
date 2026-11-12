---
title: Models
description: "Model types and configuration. Built-in and custom anomaly detection models."
weight: 1
menu:
  docs:
    identifier: "vmanomaly-models"
    parent: "vmanomaly-components"
    weight: 1
tags:
  - metrics
  - enterprise
aliases:
  - /anomaly-detection/components/models.html
  - /anomaly-detection/components/models/custom_model.html
  - /anomaly-detection/components/models/models.html
---
This section covers the `Models` component of VictoriaMetrics Anomaly Detection (commonly referred to as [`vmanomaly`](https://docs.victoriametrics.com/anomaly-detection/)) and provides a guide on how to configure the service.

- `vmanomaly` includes various **[built-in models](#built-in-models)**.
- You can also integrate a **custom model**—see the [custom model guide](#custom-model-guide) for more details.
- Models have **different types and properties**—refer to the [model types section](#model-types) for more information.

> Models can be dumped to disk {{% available_from "v1.13.0" anomaly %}} instead of being stored in RAM. This option **slightly reduces inference speed but significantly decreases RAM usage**, particularly useful for larger setups. For more details, see the [relevant FAQ section](https://docs.victoriametrics.com/anomaly-detection/faq/#on-disk-mode).

> The `models` configuration section supports multiple models through aliases{{% available_from "v1.10.0" anomaly %}}. The old, flat `model` section is deprecated and will be removed in a future version. If a configuration contains both sections, `vmanomaly` uses only `models`:

```yaml
models:
  model_univariate_1:
    class: 'zscore_online'
    z_threshold: 2.5
    queries: ['query_alias2']  # referencing queries defined in `reader` section
  model_multivariate_1:
    class: 'temporal_envelope_multivariate'
    seasonalities: ['hod_smooth', 'dow_smooth']
    provide_series: ['anomaly_score']
    # if there is no explicit `queries` arg, then the model will be run on ALL queries found in reader section
# ...
```  

Old-style configs (< [1.10.0](https://docs.victoriametrics.com/anomaly-detection/changelog/#v1100))

```yaml
model:
    class: "zscore"  # or 'model.zscore.ZscoreModel' until v1.13.0
    z_threshold: 3.0
    # no explicit `queries` arg is provided
# ...
```

will be **implicitly** converted to

```yaml
models:
  default_model:  # default model alias, backward compatibility
    class: "model.zscore.ZscoreModel"
    z_threshold: 3.0
    # queries arg is created and propagated with all query aliases found in `queries` arg of `reader` section
    queries: ['q1', 'q2', 'q3']  # i.e., if your `queries` in `reader` section has exactly q1, q2, q3 aliases
# ...
```

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `models.parts/`)

- `001-common-args.md`: Common args
- `002-model-types-peer-outlier.md`: Model types … Peer Outlier
- `003-built-in-models-autotuned.md`: Built-in Models › AutoTuned
- `004-built-in-models-temporal-envelope-online-mad.md`: Built-in Models › Temporal Envelope … Online MAD
- `005-built-in-models-online-seasonal-quantile-rolling-q.md`: Built-in Models › Online Seasonal Quantile … [Rolling Quantile](https://en.wikipedia.org/wiki/Quantile)
- `006-built-in-models-prophet-https-facebook-github-io-p.md`: Built-in Models › [Prophet](https://facebook.github.io/prophet/) … [Holt-Winters](https://en.wikipedia.org/wiki/Exponential_smoothing)
- `007-built-in-models-seasonal-trend-decomposition-https.md`: Built-in Models › [Seasonal Trend Decomposition](https://en.wikipedia.org/wiki/Seasonal_adjustment) … Custom Model Guide
- `008-deprecations.md`: Deprecations
