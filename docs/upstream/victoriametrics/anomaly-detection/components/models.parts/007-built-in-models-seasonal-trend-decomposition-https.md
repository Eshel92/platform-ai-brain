<!-- Part 7 of 8 of anomaly-detection/components/models.md (split because the page is big). -->

### [Seasonal Trend Decomposition](https://en.wikipedia.org/wiki/Seasonal_adjustment)

> `StdModel` **is** {{% available_from "v1.28.0" anomaly %}} a [univariate](#univariate-models), [online](#online-models) model. It **was** {{% deprecated_from "v1.28.0" anomaly %}} a [univariate](#univariate-models), [rolling](#rolling-models), [offline](#offline-models) model.

Here we use Seasonal Decompose implementation from `statsmodels` [library](https://www.statsmodels.org/dev/generated/statsmodels.tsa.seasonal.seasonal_decompose). Parameters from this library can be passed to the model. Some parameters are specifically predefined in `vmanomaly` and can't be changed by user (`model`='additive', `two_sided`=False).

<div class="model-details">

{{% collapse name="Model-specific arguments" %}}

- `class` (string) - model class name `"model.std.StdModel"` (or `std` with class alias support{{% available_from "v1.13.0" anomaly %}})
- `period` (integer) -  Number of datapoints in one season.
- `z_threshold` (float, optional) - [standard score](https://en.wikipedia.org/wiki/Standard_score) for calculating boundaries to define anomaly score. Defaults to `2.5`.

{{% /collapse %}}

{{% collapse name="Configuration example" %}}


```yaml
models:
  your_desired_alias_for_a_model:
    class: "std"  # or 'model.std.StdModel' starting from v1.13.0
    period: 2
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

**Additional output metrics produced by Seasonal Trend Decomposition model**
- `resid` - The residual component of the data series.
- `trend` - The trend component of the data series.
- `seasonal` - The seasonal component of the data series.



## vmanomaly output

`vmanomaly` generates model-dependent output series. Their metric names can be configured in the writer section.

The default metrics produced by `vmanomaly` include:

- `anomaly_score`: This is the *primary* metric.
    - It is designed in such a way that values from 0.0 to 1.0 indicate non-anomalous data.
    - A value greater than 1.0 is generally classified as an anomaly, although this threshold can be adjusted in the alerting configuration.
    - The threshold is normalized to `1` across models, so alerting rules can consistently treat a score above `1` as anomalous.

- `yhat`: This represents the predicted expected value.

- `yhat_lower`: This indicates the predicted lower boundary.

- `yhat_upper`: This refers to the predicted upper boundary.

- `y`: This is the original value obtained from the query result.

> If an `infer` call receives `NaN` or infinite input values, the corresponding `anomaly_score` is `NaN`.



## vmanomaly monitoring metrics

Model behavior is exposed through [self-monitoring metrics](https://docs.victoriametrics.com/anomaly-detection/components/monitoring/#models-behaviour-metrics) at the configured `monitoring.pull.health_path` endpoint.



## Custom Model Guide

In addition to the [built-in models](#built-in-models), `vmanomaly` can load a custom Python model.

This guide shows how to:

- implement the `Model` interface;
- configure the custom model;
- mount the module into the `vmanomaly` container and run it.

> The file containing the model must be written in [Python](https://www.python.org/) 3.14 or later. A custom model runs inside the `vmanomaly` Python environment, so keep its dependencies compatible with the target image and keep the module available when restoring serialized model state after a restart.

<div class="collapse-group">

{{% collapse name="Custom model implementation guide" %}}

### 1. Custom model

Create `custom_model.py` with a `CustomModel` class derived from `Model`. A concrete model must implement:

- `__init__`, which must call `super().__init__(**kwargs)` so common model arguments are initialized;
- `fit`, which conditions the model on a DataFrame containing at least `timestamp` and `y`;
- `infer`, which returns a DataFrame whose first column is `timestamp` and which contains at least `anomaly_score`;
- `serialize`, which returns `bytes` suitable for on-disk storage;
- `deserialize`, which restores the same model from bytes or a file path.

Model-specific configuration is passed through the `args` mapping. The example below learns a stationary normal interval. It emits the standard forecast columns and uses the base-class anomaly-score calculation, so query policies such as `detection_direction`, `data_range`, and minimum deviations, together with model settings such as `scale`, continue to work.

```python
from pickle import dumps
from statistics import NormalDist

import numpy as np
import pandas as pd

from model.model import (
    PICKLE_PROTOCOL,
    Model,
    deserialize_basic,
)


class CustomModel(Model):
    """Simple univariate, offline custom model."""

    def __init__(self, percentage: float = 0.95, **kwargs):
        model_args = kwargs.get("args") or {}
        self.percentage = float(model_args.get("percentage", percentage))
        if not 0 < self.percentage < 1:
            raise ValueError("percentage must be between 0 and 1")

        super().__init__(**kwargs)
        self._mean = np.nan
        self._std = np.nan
        self._z_threshold = NormalDist().inv_cdf((1 + self.percentage) / 2)

    def fit(self, df: pd.DataFrame) -> None:
        values = df["y"].to_numpy(dtype=np.float64)
        self._mean = float(np.nanmean(values))
        self._std = float(np.nanstd(values))
        if not np.isfinite(self._mean) or not np.isfinite(self._std):
            raise ValueError("fit data must contain finite values")
        self._std = max(self._std, np.finfo(np.float64).eps)

    def infer(self, df: pd.DataFrame) -> pd.DataFrame:
        margin = self._z_threshold * self._std
        df_pred = df[["timestamp", "y"]].copy()
        df_pred["yhat"] = self._mean
        df_pred["yhat_lower"] = self._mean - margin
        df_pred["yhat_upper"] = self._mean + margin

        self._prepare_ci_columns(
            df_pred,
            scale=self.scale,
            clip_predictions=self.clip_predictions,
            data_range=self.data_range,
        )
        df_pred["anomaly_score"] = self.get_anomaly_score(
            df_pred,
            data_range=self.data_range,
            detection_direction=self.detection_direction,
            min_dev_from_expected=self.min_dev_from_expected,
            min_rel_dev_from_expected=self.min_rel_dev_from_expected,
            anomaly_score_outside_data_range=self.anomaly_score_outside_data_range,
        )

        if self.provide_series:
            return df_pred[self._assemble_output_columns()]
        return df_pred

    def serialize(self) -> bytes:
        return dumps(self, protocol=PICKLE_PROTOCOL)

    @staticmethod
    def deserialize(model: str | bytes) -> "CustomModel":
        return deserialize_basic(model)
```

`Model` is offline and uses the one-input-to-one-output service topology by default. A custom online model should derive from `OnlineModel` and implement causal update semantics; setting `is_online = True` alone is not sufficient.

{{% available_from "v1.30.3" anomaly %}} Custom models must use `ModelTopology` to declare how service-level input identities map to output identities. The topology controls orchestration, persistence, grouping, and output-label restoration; it does **not** describe the number of columns returned by `infer`.

- `ModelTopology.ONE_TO_ONE` is the default: the service maintains one model for each input series.
- `ModelTopology.MANY_TO_ONE` merges aligned input series into one model identity and one joint `anomaly_score`. The model may also return per-channel `y`, `yhat`, `yhat_lower`, `yhat_upper`, or `forecast_at` prediction columns; those diagnostics do not change its many-to-one topology.
- `ModelTopology.MANY_TO_MANY` is the `WideModel` extension contract for an online model that tracks a changing pool of peer series and restores an output identity for each entity.

For a custom many-to-one model, derive from `MultivariateModel` and declare the contract explicitly:

```python
from model.model import MultivariateModel
from model.topology import ModelTopology


class CustomMultivariateModel(MultivariateModel):
    topology = ModelTopology.MANY_TO_ONE

    # fit receives timestamp plus one value column per aligned input channel.
    # infer returns a joint anomaly_score and may include per-channel diagnostics.
```

The legacy `is_multivariate = True` class flag may still describe an algorithm internally, but it no longer selects service routing. A class that sets only that flag is orchestrated as one-to-one. Existing compatible built-in multivariate dumps continue to restore through their built-in class definitions.

For a changing peer pool, derive from `WideModel`. Its `fit` and `infer` methods consume a long DataFrame with `timestamp`, `entity_id`, and `y`; returned entity-level rows must retain `entity_id` so the service can restore the original labels. `WideModel` is a semantic extension contract, not a marker used only to store `topology`.

### 2. Configuration file

Create `config.yaml`. Set the model class to `custom` (an alias for `model.custom.CustomModel`) and put custom constructor parameters under `args`. Common model arguments remain at the model level.

```yaml
schedulers:
  s1:
    class: "periodic"
    infer_every: "1m"
    fit_every: "1h"
    fit_window: "1d"

models:
  custom_model:
    class: "custom"
    queries: [ingestion_rate, churn_rate]
    schedulers: [s1]
    args:
      percentage: 0.95

reader:
  datasource_url: "http://victoriametrics:8428/"
  sampling_period: "1m"
  queries:
    ingestion_rate:
      expr: "sum(rate(vm_rows_inserted_total)) by (type)"
    churn_rate:
      expr: "sum(rate(vm_new_timeseries_created_total[5m]))"

writer:
  datasource_url: "http://victoriametrics:8428/"
  metric_format:
    __name__: "custom_$VAR"
    for: "$QUERY_KEY"
    run: "test-format"

monitoring:
  # /metrics server.
  pull:
    port: 8080
  push:
    url: "http://victoriametrics:8428/"
    extra_labels:
      job: "vmanomaly-develop"
    config: "custom.yaml"
```

See the [component configuration reference](https://docs.victoriametrics.com/anomaly-detection/components/) for the remaining fields.

### 3. Running custom model

Pull the `vmanomaly` image:

```sh
docker pull victoriametrics/vmanomaly:v1.32.0
```

Mount the module at `/vmanomaly/src/model/custom.py`, which matches the configured import path `model.custom.CustomModel`. Validate the complete configuration with `--dryRun` before starting the long-running service.

```sh
docker run --rm \
  -v "$PWD/license:/license:ro" \
  -v "$PWD/custom_model.py:/vmanomaly/src/model/custom.py:ro" \
  -v "$PWD/config.yaml:/config.yaml:ro" \
  victoriametrics/vmanomaly:v1.32.0 \
  /config.yaml \
  --licenseFile=/license \
  --dryRun
```

After validation succeeds, remove `--dryRun` and optionally add `--watch`. See the [Docker installation guide](https://docs.victoriametrics.com/anomaly-detection/quickstart/#docker) for licensing and runtime options.


### Output

The writer emits one `custom_anomaly_score` series for each input series. It retains the input labels and adds the labels configured in `metric_format`:

```text
{__name__="custom_anomaly_score", for="ingestion_rate", model_alias="custom_model", scheduler_alias="s1", run="test-format"},
{__name__="custom_anomaly_score", for="churn_rate",     model_alias="custom_model", scheduler_alias="s1", run="test-format"}
```

{{% /collapse %}}

</div>
