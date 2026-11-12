<!-- Part 2 of 7 of anomaly-detection/guides/model-selection/README.md (split because the page is big). -->

### Steady baseline, small fluctuations

**Start with [Online Z-score](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-z-score) (`zscore_online`).** A separate model is fitted for each series to estimate its average level and usual spread. An [anomaly score](https://docs.victoriametrics.com/anomaly-detection/faq/#what-is-anomaly-score "A measure of how unusual an observation is. Scores above 1 cross the model's expected range.") above `1` is assigned to values far enough from that level.

**Example:** CPU utilization normally stays near 45%, with gentle oscillations and point-to-point noise. A brief rise to about 70% or fall to about 25% deserves investigation even though neither reaches an 80% high-CPU threshold. The example query also returns a healthy instance that normally stays near 20%. A separate model is fitted for each series, so each instance is scored against its own history.

<div class="collapse-group mb-3">

{{% collapse name="Use for: a stable normal range" %}}

- CPU utilization across instances with different normal ranges, learned separately for each instance.
- Request latency for a stable route, after choosing an aggregation and sample interval that avoid sparse or very noisy results.
- Sensor temperatures around a stable operating point.
- Business ratios with enough observations per sample and no strong daily or weekly variation.

The important property is a stable average and spread, without frequent extreme values. Standard deviation is useful for describing the usual variation around that average. Check the threshold against your own data to understand its effect on [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive "Normal behavior incorrectly flagged as anomalous.").

{{% /collapse %}}

{{% collapse name="Choose another recipe if…" %}}

**Strong patterns, frequent outliers, or sparse samples can make this baseline unreliable.**

- **Large [repeating peaks](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "A pattern that repeats at regular intervals, such as daily or weekly."):** a single expected range either becomes too wide to catch incidents or flags normal peaks repeatedly. Use [Online Seasonal Quantile](#predictable-repeating-patterns) or [Temporal Envelope](#changing-baselines-and-calendar-effects).
- **Frequent or very large [outliers](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#outlier "Values far from most other observations. Their significance depends on context."):** they pull the average and widen its range, potentially hiding later incidents. Consider [Online MAD](#steady-baseline-with-extreme-values).
- **A sustained [trend](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend "A sustained increase or decrease in the usual level of a time series.") or a new operating level:** this model can initially flag a <strong title="A lasting shift in the usual level or pattern.">changepoint</strong>, then gradually absorb it. Use [Temporal Envelope](#changing-baselines-and-calendar-effects) when these changes are normal.
- **Mostly zero or sparse counts:** check the aggregation interval and event volume first. A standard deviation around a near-zero baseline may not express business significance.

{{% /collapse %}}

{{% collapse name="Try it" %}}

**Two instances, two CPU incidents.**

[Open the prepared metrics playground](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=30d&g0.end_input=2026-01-31T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522cpu_utilization%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520%2523%2520Timestamp-based%2520noise%2520stays%2520the%2520same%2520across%2520fit%2520and%2520display%2520windows.%255Cn%2520%2520mixed%28seed%29%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%2520seed%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%28seed%29%2520%253D%25200.05%2520%2A%2520%28mixed%28seed%29%2520-%2520floor%28mixed%28seed%29%29%2520-%25200.5%29%252C%255Cn%2520%2520%2523%2520Subtle%2520waves%2520%280.3%2520percentage%2520points%2520each%29%252C%2520without%2520a%2520calendar%2520pattern.%255Cn%2520%2520fluctuation%28seed%29%2520%253D%2520noise%28seed%29%255Cn%2520%2520%2520%2520%252B%25200.003%2520%2A%2520sin%28time%28%29%2520%252F%2520%2811%2520%2A%25203600%29%2520%252B%2520seed%29%255Cn%2520%2520%2520%2520%252B%25200.003%2520%2A%2520sin%28time%28%29%2520%252F%2520%285%2520%2A%25203600%29%2520%252B%2520seed%2520%2A%25200.7%29%252C%255Cn%2520%2520rise%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768046400%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768057200%29%252C%255Cn%2520%2520fall%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768888800%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768899600%29%255Cn%29%255Cnlabel_set%280.45%2520%252B%2520fluctuation%2842%29%2520%252B%25200.25%2520%2A%2520rise%2520-%25200.20%2520%2A%2520fall%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_cpu_utilization_ratio%255C%2522%252C%2520%255C%2522instance%255C%2522%252C%2520%255C%2522checkout-01%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%255Cnor%2520label_set%280.20%2520%252B%2520fluctuation%2843%29%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_cpu_utilization_ratio%255C%2522%252C%2520%255C%2522instance%255C%2522%252C%2520%255C%2522checkout-02%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C1%255D%252C%2522detectionDirection%2522%253A%2522both%2522%252C%2522minDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522minRelDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522zscore_online%2522%252C%2522settings%2522%253A%257B%2522z_threshold%2522%253A3%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.998%252C%2522history_strength%2522%253A1.0%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522zscore_online%2522%252C%2522z_threshold%2522%253A3%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.998%252C%2522history_strength%2522%253A1.0%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=3d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=false).

1. Select **Execute Query** to inspect the two synthetic CPU-utilization series.
2. Select **Detect Anomalies** to run Online Z-score with the prepared settings.
3. Inspect `checkout-01` on **January 10, 2026, 12:00–15:00 UTC** and **January 20, 2026, 06:00–09:00 UTC**. The rise and fall should cross the expected range and have scores above `1`. The other instance should remain within its own range.

| Setting | Prepared value | Why |
| --- | --- | --- |
| Inference range | January 1, 2026, 00:00 UTC → January 31, 2026, 00:00 UTC | Fixed 30-day example |
| Query step | `15m` | Four observations per hour per instance |
| Fit window | `3d` | Initialize from the preceding three days of healthy data |
| Fit every | `1000w` | Longer than this example, so there is one initial fit |
| Exact | `true` | Imitate production scheduling: score chronologically, without future observations updating earlier predictions |
| Infer every | `15m` | Update once per query sample |
| Streaks | On, minimum `2` points | Connect consecutive anomalous points and omit isolated flags |

This [online model](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) keeps learning as new data arrives, so regular refits are optional.

Times in this guide are UTC. The UI may display the same instants in your selected timezone.

**What to expect:** gentle oscillations and small noisy deviations stay inside each instance's expected range, without a strong daily or weekly pattern. Each three-hour incident affects twelve observations on `checkout-01`, with consecutive flagged observations connected by a line when Streaks is enabled. Scores may taper as the model learns from the incident. The other instance remains healthy. Values use ratios: `0.45` means 45% CPU utilization. The query generates demonstration data.

The query depends only on timestamps and fixed constants. Its small noise is generated by a deterministic mixing function, so the value at a timestamp is unchanged when the fit and display windows differ. Seeded [`rand`](https://docs.victoriametrics.com/metricsql/#rand) functions reproduce a sequence from the beginning of a request. Changing the request start can assign different values to the same timestamps.

If using your own [UI](https://docs.victoriametrics.com/anomaly-detection/ui/), copy the query from the configuration below and the settings from this table. The public playground needs network access. The configuration remains readable offline.

{{% /collapse %}}

{{% collapse name="Copy the configuration" %}}

These **reader**, **models**, and **schedulers** sections use a [periodic scheduler](https://docs.victoriametrics.com/anomaly-detection/components/scheduler/#periodic-scheduler) to score current data continuously. The playground above replays its fixed historical dates with the same fit window and cadence. Keep the writer and license configuration from the [Quickstart](https://docs.victoriametrics.com/anomaly-detection/quickstart/#example). Use a test destination for the demo results written by this configuration.

```yaml
reader:
  class: vm
  datasource_url: https://play.victoriametrics.com/select/0/prometheus
  sampling_period: 15m
  queries:
    cpu_utilization:
      expr: |
        WITH (
          # Timestamp-based noise stays the same across fit and display windows.
          mixed(seed) = sin(time() / 900 * 12.9898 + seed) * 43758.5453,
          noise(seed) = 0.05 * (mixed(seed) - floor(mixed(seed)) - 0.5),
          # Subtle waves (0.3 percentage points each), without a calendar pattern.
          fluctuation(seed) = noise(seed)
            + 0.003 * sin(time() / (11 * 3600) + seed)
            + 0.003 * sin(time() / (5 * 3600) + seed * 0.7),
          rise = (time() >= bool 1768046400) * (time() < bool 1768057200),
          fall = (time() >= bool 1768888800) * (time() < bool 1768899600)
        )
        label_set(0.45 + fluctuation(42) + 0.25 * rise - 0.20 * fall,
          "__name__", "demo_cpu_utilization_ratio", "instance", "checkout-01", "service", "checkout")
        or label_set(0.20 + fluctuation(43),
          "__name__", "demo_cpu_utilization_ratio", "instance", "checkout-02", "service", "checkout")
      detection_direction: both  # When spikes and drops matter. Use above_expected or below_expected for one direction.
      data_range: [0, 1]  # Utilization is expressed as a ratio.

models:
  zscore_steady_cpu:  # Choose a unique alias for this model configuration.
    class: zscore_online  # Select the Online Z-score model.
    queries: [cpu_utilization]  # Connect to one or more aliases defined in reader.queries.
    schedulers: [steady_cpu_demo]  # Connect to one or more aliases defined in schedulers.
    z_threshold: 3  # Set the expected range to three standard deviations from the mean.
    min_n_samples_seen: 96  # One day's worth of 15-minute samples per instance.
    decay: 0.998          # Slower adaptation. History weight halves in ~3.6d at 15m steps.
    history_strength: 1.0  # Give fit history its ordinary weight.

schedulers:
  steady_cpu_demo:
    class: periodic  # Run continuously on incoming data.
    fit_window: 3d
    fit_every: 1000w  # Learning continues between these very infrequent full refits.
    infer_every: 15m
```

`queries` and `schedulers` explicitly bind the model to this example. Query-level [business policies](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters) apply consistently if you later compare models.

For production, replace the synthetic expression with your utilization query, for example `1 - avg by (instance, service) (rate(node_cpu_seconds_total{mode="idle"}[5m]))` if those labels exist in your data. Adjust the inference cadence to your response-time requirements. The deliberately long `fit_every: 1000w` highlights online learning: the model keeps updating between full refits. `fit_window` supplies the initial history at each fit. The model continues learning from observations after that window.

{{% /collapse %}}

{{% collapse name="Tuning hints: warmup, sensitivity, adaptation, and business context" %}}

**Give new series time to warm up.** `min_n_samples_seen: 96` requires 96 valid observations per series, including fit data, before non-neutral scoring. At `15m`, that is one day's worth of regularly sampled data. Missing samples extend the wait. Until warmup completes, the score is `0` because the model needs more history. Check warmup status before interpreting zero scores as healthy. The three-day fit normally warms up both demo instances. This recipe uses `96` to allow more warmup than the default `16`.

**Adjust sensitivity.** `z_threshold: 3` places the initial expected range three standard deviations from the mean. Raise it to tolerate larger fluctuations or lower it to investigate smaller changes. Adjust this starting value to your data and investigation needs. Review [false positives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-positive "Normal behavior incorrectly flagged as anomalous.") and [false negatives](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#false-negative "Actual anomalies that the model does not flag.") (missed incidents) on representative data before enabling alerts.

**Choose how quickly to adapt.** This recipe uses `decay: 0.998` for slower adaptation, helping limit abrupt changes in the expected range after brief incidents. Older information loses half its weight after about 346 new observations (roughly 3.6 days at `15m`). Values closer to `1` adapt more slowly. Setting `1` retains all observations since the latest fit. Faster adaptation can help track an accepted new level, but can also absorb a persistent incident sooner. Retest after changing the sample cadence.

**Weight fit history when appropriate.** `history_strength: 1` gives the fit data its ordinary weight. With representative, similar history, `2` makes that initial evidence twice as influential against subsequent updates. A one-week fit with strength `2` still covers only one week and supplies the same number of valid warmup samples. Use it to adjust adaptation while retaining enough history to cover the patterns you need.

**Apply domain knowledge to each query.** This example uses `detection_direction: both` to show a rise and a fall. Use `above_expected` if only CPU rises matter for your service, or `below_expected` for a conversion-rate drop. Consider [`min_dev_from_expected`](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-deviation-from-expected) to ignore negligible changes: for a utilization ratio, `0.02` means two percentage points. Place these policies under `reader.queries.<alias>`.

[Open the spikes-only comparison](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=30d&g0.end_input=2026-01-31T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522cpu_utilization%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520%2523%2520Timestamp-based%2520noise%2520stays%2520the%2520same%2520across%2520fit%2520and%2520display%2520windows.%255Cn%2520%2520mixed%28seed%29%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%2520seed%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%28seed%29%2520%253D%25200.05%2520%2A%2520%28mixed%28seed%29%2520-%2520floor%28mixed%28seed%29%29%2520-%25200.5%29%252C%255Cn%2520%2520%2523%2520Subtle%2520waves%2520%280.3%2520percentage%2520points%2520each%29%252C%2520without%2520a%2520calendar%2520pattern.%255Cn%2520%2520fluctuation%28seed%29%2520%253D%2520noise%28seed%29%255Cn%2520%2520%2520%2520%252B%25200.003%2520%2A%2520sin%28time%28%29%2520%252F%2520%2811%2520%2A%25203600%29%2520%252B%2520seed%29%255Cn%2520%2520%2520%2520%252B%25200.003%2520%2A%2520sin%28time%28%29%2520%252F%2520%285%2520%2A%25203600%29%2520%252B%2520seed%2520%2A%25200.7%29%252C%255Cn%2520%2520rise%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768046400%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768057200%29%252C%255Cn%2520%2520fall%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768888800%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768899600%29%255Cn%29%255Cnlabel_set%280.45%2520%252B%2520fluctuation%2842%29%2520%252B%25200.25%2520%2A%2520rise%2520-%25200.20%2520%2A%2520fall%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_cpu_utilization_ratio%255C%2522%252C%2520%255C%2522instance%255C%2522%252C%2520%255C%2522checkout-01%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%255Cnor%2520label_set%280.20%2520%252B%2520fluctuation%2843%29%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_cpu_utilization_ratio%255C%2522%252C%2520%255C%2522instance%255C%2522%252C%2520%255C%2522checkout-02%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C1%255D%252C%2522detectionDirection%2522%253A%2522above_expected%2522%252C%2522minDevFromExpected%2522%253A%255B0.02%252C0.02%255D%252C%2522minRelDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522zscore_online%2522%252C%2522settings%2522%253A%257B%2522z_threshold%2522%253A3%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.998%252C%2522history_strength%2522%253A1.0%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522zscore_online%2522%252C%2522z_threshold%2522%253A3%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.998%252C%2522history_strength%2522%253A1.0%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=3d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true). This keeps the same data and model, names the query `cpu_utilization`, and sets **Query overrides** to `detection_direction: above_expected`, `data_range: [0, 1]`, and `min_dev_from_expected: [0.02, 0.02]`. Select **Detect Anomalies**: only the January 10 rise should score above `1`, while the January 20 fall should score `0`. The two-percentage-point minimum deviation is smaller than either incident, so direction is what changes this example's results. To apply these policies in YAML, replace the query's policy fields with:

```yaml
detection_direction: above_expected
data_range: [0, 1]
min_dev_from_expected: [0.02, 0.02]  # Two percentage points of utilization.
```

**Match scheduling to the decision.** The example's `15m` step and inference cadence are for an easy-to-inspect demo. Short incidents may require finer sampling. Slower business KPIs may need coarser aggregation. Keep **Exact** enabled for causal online backtests and set **Infer Every** deliberately. A periodic refit resets learned state using its fit window. Check whether that history contains incidents that could become part of the new baseline.

**Separate detection from paging.** An anomaly score is evidence of unusual behavior. Combine it with impact, persistence, and existing safety or SLO rules when deciding to page. See the [alerting guide](https://docs.victoriametrics.com/anomaly-detection/guides/guide-vmanomaly-vmalert/) and [alert-fatigue guidance](https://docs.victoriametrics.com/anomaly-detection/faq/#preventing-alert-fatigue).

{{% /collapse %}}

</div>
