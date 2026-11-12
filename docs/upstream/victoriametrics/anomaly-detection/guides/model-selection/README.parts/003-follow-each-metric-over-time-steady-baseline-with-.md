<!-- Part 3 of 7 of anomaly-detection/guides/model-selection/README.md (split because the page is big). -->

### Steady baseline with extreme values

**Start with [Online MAD](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-mad) (`mad_online`).** A separate model is fitted for each series to estimate its median and usual distance from that median. Occasional large [outliers](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#outlier "Values far from most other observations. Their significance depends on context.") have less influence on this baseline than on an average and standard deviation.

**Example:** checkout request latency normally stays near 200 ms. Two short spikes reach about one second, then latency settles at 260 ms after a deployment. This lasting increase is a <strong title="A lasting shift in the usual level or pattern.">changepoint</strong>. The spikes should not make the later 60 ms regression disappear into a wide normal range. Only increases matter here. Lower latency is welcome.

<div class="collapse-group mb-3">

{{% collapse name="Use for: a steady baseline with occasional large values" %}}

- Request latency with a stable typical level and sporadic slow samples.
- Processing or queue-wait durations interrupted by occasional long jobs.
- Sensor readings where a few extreme measurements should not distort the baseline.

The baseline should describe most observations. Robustness limits how much an extreme value changes that baseline. The extreme value can still receive a high anomaly score.

{{% /collapse %}}

{{% collapse name="Choose another recipe if…" %}}

**Predictable patterns, multiple operating modes, or sparse samples may need a different model or query.**

- **Strong daily or weekly variation:** use [Online Seasonal Quantile](#predictable-repeating-patterns) or [Temporal Envelope](#changing-baselines-and-calendar-effects), so normal peaks are compared with their calendar context.
- **Normal growth or frequent accepted level changes:** use [Temporal Envelope](#changing-baselines-and-calendar-effects). MAD initially treats an unfamiliar level as unusual and can later learn it. Decide whether a deployment-related change should be accepted based on its impact.
- **Several normal operating modes:** one median and spread can poorly describe their separate ranges. Check whether labels or query aggregation can separate the workloads.
- **Sparse or nearly constant results:** check the sampling interval and set a meaningful minimum deviation. A very narrow learned range can make tiny changes look significant.

{{% /collapse %}}

{{% collapse name="Try it" %}}

**Two latency spikes, then a lasting increase.**

[Open the MAD latency playground](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=30d&g0.end_input=2026-01-31T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_latency%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520%2523%2520Fixed%2520timestamp-based%2520noise%252C%2520in%2520seconds.%255Cn%2520%2520mixed%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%252042%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%2520%253D%25200.02%2520%2A%2520%28mixed%2520-%2520floor%28mixed%29%2520-%25200.5%29%252C%255Cn%2520%2520spike_1%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201767873600%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201767875400%29%252C%255Cn%2520%2520spike_2%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768564800%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768566600%29%252C%255Cn%2520%2520changed%2520%253D%2520time%28%29%2520%253E%253D%2520bool%25201768586400%255Cn%29%255Cnlabel_set%280.20%2520%252B%2520noise%2520%252B%25200.80%2520%2A%2520%28spike_1%2520%252B%2520spike_2%29%2520%252B%25200.06%2520%2A%2520changed%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_request_duration_seconds%255C%2522%252C%2520%255C%2522quantile%255C%2522%252C%2520%255C%25220.95%255C%2522%252C%255Cn%2520%2520%255C%2522route%255C%2522%252C%2520%255C%2522%252Fcheckout%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C5%255D%252C%2522detectionDirection%2522%253A%2522above_expected%2522%252C%2522minDevFromExpected%2522%253A%255B0.02%252C0.02%255D%252C%2522minRelDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522mad_online%2522%252C%2522settings%2522%253A%257B%2522threshold%2522%253A5.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522mad_online%2522%252C%2522threshold%2522%253A5.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=3d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true).

1. Select **Execute Query** to inspect one synthetic latency series, named `checkout_latency`.
2. Select **Detect Anomalies** to run Online MAD with the prepared settings.
3. Inspect the two spikes on **January 8 and January 16, 2026, 12:00–12:30 UTC**, then the lasting increase starting **January 16, 18:00 UTC**. MAD should flag both spikes and the beginning of the new level.

| Setting | Prepared value | Why |
| --- | --- | --- |
| Inference range | January 1 → January 31, 2026, UTC | Fixed 30-day comparison |
| Query step / infer every | `15m` / `15m` | Score each observation chronologically |
| Fit window / fit every | `3d` / `1000w` | One initial fit from the preceding three days |
| Exact | `true` | Imitate production scheduling without future observations changing earlier predictions |
| Streaks | On, minimum `2` points | Show the two-point spikes and consecutive flags after the shift |
| Query policies | Above expected, minimum deviation `0.02` seconds | Ignore improvements and changes smaller than 20 ms |

This [online model](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) keeps learning as new data arrives, so regular refits are optional.

**What to expect:** values use seconds: `0.2` means 200 ms. The series has timestamp-based noise, two 30-minute spikes, and a permanent 60 ms increase. There is no trend or calendar pattern to learn. As new observations arrive, the expected range can move and widen until the new level is no longer flagged. Use latency or SLO checks to confirm that the regression has been resolved.

[Compare with Online Z-score](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=30d&g0.end_input=2026-01-31T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_latency%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520%2523%2520Fixed%2520timestamp-based%2520noise%252C%2520in%2520seconds.%255Cn%2520%2520mixed%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%252042%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%2520%253D%25200.02%2520%2A%2520%28mixed%2520-%2520floor%28mixed%29%2520-%25200.5%29%252C%255Cn%2520%2520spike_1%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201767873600%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201767875400%29%252C%255Cn%2520%2520spike_2%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768564800%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768566600%29%252C%255Cn%2520%2520changed%2520%253D%2520time%28%29%2520%253E%253D%2520bool%25201768586400%255Cn%29%255Cnlabel_set%280.20%2520%252B%2520noise%2520%252B%25200.80%2520%2A%2520%28spike_1%2520%252B%2520spike_2%29%2520%252B%25200.06%2520%2A%2520changed%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_request_duration_seconds%255C%2522%252C%2520%255C%2522quantile%255C%2522%252C%2520%255C%25220.95%255C%2522%252C%255Cn%2520%2520%255C%2522route%255C%2522%252C%2520%255C%2522%252Fcheckout%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C5%255D%252C%2522detectionDirection%2522%253A%2522above_expected%2522%252C%2522minDevFromExpected%2522%253A%255B0.02%252C0.02%255D%252C%2522minRelDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522zscore_online%2522%252C%2522settings%2522%253A%257B%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522z_threshold%2522%253A3.0%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522zscore_online%2522%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522z_threshold%2522%253A3.0%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=3d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true). The comparison keeps the query, policies, dates, schedule, and decay the same, while changing the model and its threshold. The large spikes widen the Z-score range, which can hide the smaller increase that follows. Compare the expected ranges at the start of the level change. MAD's `threshold` and Z-score's `z_threshold` measure different spreads and need separate tuning.

{{% /collapse %}}

{{% collapse name="Copy the configuration" %}}

These **reader**, **models**, and **schedulers** sections use a periodic scheduler for continuous scoring. The playground above replays the dated latency example with the same fit window and cadence. Keep the writer and license settings from the [Quickstart](https://docs.victoriametrics.com/anomaly-detection/quickstart/#example) and use a test writer destination, as in the previous recipe.

```yaml
reader:
  class: vm
  datasource_url: https://play.victoriametrics.com/select/0/prometheus
  sampling_period: 15m
  queries:
    checkout_latency:
      expr: |
        WITH (
          # Fixed timestamp-based noise, in seconds.
          mixed = sin(time() / 900 * 12.9898 + 42) * 43758.5453,
          noise = 0.02 * (mixed - floor(mixed) - 0.5),
          spike_1 = (time() >= bool 1767873600) * (time() < bool 1767875400),
          spike_2 = (time() >= bool 1768564800) * (time() < bool 1768566600),
          changed = time() >= bool 1768586400
        )
        label_set(0.20 + noise + 0.80 * (spike_1 + spike_2) + 0.06 * changed,
          "__name__", "demo_request_duration_seconds", "quantile", "0.95",
          "route", "/checkout", "service", "checkout")
      detection_direction: above_expected  # Flag slower requests while allowing faster ones.
      min_dev_from_expected: [0.02, 0.02]  # Ignore deviations smaller than 20 ms.
      data_range: [0, 5]  # This demo service has a five-second request timeout.

models:
  mad_checkout_latency:
    class: mad_online
    queries: [checkout_latency]
    schedulers: [latency_demo]
    threshold: 5.0  # Multiplier of median absolute deviation, not standard deviation.
    min_n_samples_seen: 96  # One day's worth of 15-minute samples.
    decay: 0.99  # Favor recent observations so sustained changes can become normal.
    history_strength: 1.0
    compression: 100  # Starting accuracy/memory tradeoff for approximate quantiles.

schedulers:
  latency_demo:
    class: periodic  # Run continuously on incoming data.
    fit_window: 3d
    fit_every: 1000w  # Learning continues between these very infrequent full refits.
    infer_every: 15m
```

For the Z-score comparison, replace `class: mad_online` with `class: zscore_online`, replace `threshold: 5.0` with `z_threshold: 3.0`, and remove `compression`. Keep the query policies and schedule unchanged. Replace the generated expression with your latency query when applying the recipe to real data. Preserve its units and aggregation meaning.

{{% /collapse %}}

{{% collapse name="Tuning hints: outliers, persistence, and adaptation" %}}

**Start with representative history and warmup.** The three-day fit contains healthy data and exceeds `min_n_samples_seen: 96`. New series need 96 valid observations before non-neutral scores. Missing observations delay warmup. Include ordinary variability in fit history. A perfectly flat fit can produce an overly narrow range.

**Tune sensitivity in MAD units.** `threshold: 5.0` is a starting point for this query. Increase it to tolerate more variation or decrease it to investigate smaller departures. MAD measures distance from the median, so tune its threshold for the spread of your data. Check [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive "Normal behavior incorrectly flagged as anomalous.") and missed incidents on representative data.

**Set business significance in the query's units.** `detection_direction: above_expected` allows latency improvements. `min_dev_from_expected: [0.02, 0.02]` measures a 20 ms minimum distance from the expected value. A sample must also cross the model's expected range to be flagged. The two limits work together. See [minimum deviation](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-deviation-from-expected).

**Decide how long a new level should remain unusual.** With `decay: 0.99`, recent observations gain influence and a persistent increase can be absorbed. Values closer to `1` retain older evidence longer. Setting `history_strength` above `1` strengthens the initial fit history without adding time coverage. A shorter refit interval can also reset the baseline from recent data. Backtest these settings against the time you need to investigate a regression. Use impact or SLO checks to confirm recovery.

**Keep persistence separate from severity.** Streaks controls how consecutive flags are displayed in the UI. Configure alert persistence separately. The two large spikes can still be anomalies even though they barely move MAD's baseline. Decide whether to page using impact and persistence, and retain latency or SLO rules for regressions that must stay actionable after the model adapts. See the [alerting guide](https://docs.victoriametrics.com/anomaly-detection/guides/guide-vmanomaly-vmalert/).

{{% /collapse %}}

</div>
