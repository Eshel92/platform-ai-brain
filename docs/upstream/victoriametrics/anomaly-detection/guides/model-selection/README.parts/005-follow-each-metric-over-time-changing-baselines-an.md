<!-- Part 5 of 7 of anomaly-detection/guides/model-selection/README.md (split because the page is big). -->

### Changing baselines and calendar effects

**Start with [Temporal Envelope](https://docs.victoriametrics.com/anomaly-detection/components/models/#temporal-envelope) (`temporal_envelope`).** Choose this **when normal behavior combines growth, changing levels, and calendar patterns**. The expected range can follow a [trend](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend "A sustained increase or decrease in the usual level of a time series."), smooth or step-shaped [seasonalities](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "Patterns that repeat at regular intervals, such as daily or weekly."), and persistent level shifts together. Each series is modeled independently in this recipe.

**Example:** checkout traffic grows gradually, rises and falls smoothly each day, and is lower on weekends. A traffic migration adds a lasting 35 requests/s from January 12. That new level may initially be flagged, then learned. A separate three-hour surge and three-hour drop should still stand out from the evolving daily pattern.

<div class="collapse-group mb-3">

{{% collapse name="Use for: evolving baselines and calendar patterns" %}}

- Service traffic with smooth daily demand, weekday/weekend differences, and gradual growth.
- CPU or power usage whose usual range changes with workload and calendar schedules.
- Business activity with recurring calendar effects and an evolving normal level.
- Metrics affected by accepted traffic migrations or capacity changes, when a new level should eventually become normal.

The model learns what the metric usually does at that time and how its baseline evolves. Decide which persistent shifts should become normal based on their business impact.

{{% /collapse %}}

{{% collapse name="Choose another recipe if…" %}}

**A simpler baseline, a custom cycle, or a different comparison better matches the question.**

- **Stable data without calendar patterns:** start with [Online Z-score](#steady-baseline-small-fluctuations) or [Online MAD](#steady-baseline-with-extreme-values). Their simpler ranges can be easier to inspect and tune.
- **Fixed plateaus or custom-duration cycles dominate:** consider [Online Seasonal Quantile](#predictable-repeating-patterns), especially for schedules such as a repeating two-week production plan with three-hour slots. Temporal Envelope's seasonal presets follow calendar patterns. Seasonal Quantile also supports custom-duration cycles.
- **The relationship between signals matters:** use [multivariate models](#watch-related-signals-together). An independently plausible CPU value and RAM value can still form an unusual pair.
- **One entity differs from comparable entities now:** use a [peer-group model](#find-the-odd-one-out) when the comparison should be with its peers at the same timestamp.

{{% /collapse %}}

{{% collapse name="Try it" %}}

**A growing service, daily and weekend patterns, a new level, and two brief incidents.**

[Open the Temporal Envelope playground](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=14d&g0.end_input=2026-01-22T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_evolving_rate%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520hour_utc%2520%253D%2520%28time%28%29%2520%2525%252086400%29%2520%252F%25203600%252C%255Cn%2520%2520days_since_start%2520%253D%2520%28time%28%29%2520-%25201767225600%29%2520%252F%252086400%252C%255Cn%2520%2520%2523%2520Unix%2520epoch%2520was%2520Thursday.%2520Number%2520weekdays%2520from%2520Monday%253D0%2520to%2520Sunday%253D6.%255Cn%2520%2520weekday%2520%253D%2520floor%28time%28%29%2520%252F%252086400%2520%252B%25203%29%2520%2525%25207%252C%255Cn%2520%2520weekend%2520%253D%2520weekday%2520%253E%253D%2520bool%25205%252C%255Cn%2520%2520daily%2520%253D%252060%2520%2A%2520sin%28%28hour_utc%2520-%25206%29%2520%252F%252024%2520%2A%25206.283185307179586%29%252C%255Cn%2520%2520baseline%2520%253D%2520150%2520%252B%25202%2520%2A%2520days_since_start%2520%252B%2520daily%2520-%252025%2520%2A%2520weekend%252C%255Cn%2520%2520mixed%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%252042%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%2520%253D%252010%2520%2A%2520%28mixed%2520-%2520floor%28mixed%29%2520-%25200.5%29%252C%255Cn%2520%2520migration%2520%253D%2520time%28%29%2520%253E%253D%2520bool%25201768176000%252C%255Cn%2520%2520surge%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768730400%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768741200%29%252C%255Cn%2520%2520drop%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768874400%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768885200%29%255Cn%29%255Cnlabel_set%28baseline%2520%252B%2520noise%2520%252B%252035%2520%2A%2520migration%2520%252B%2520100%2520%2A%2520surge%2520-%252070%2520%2A%2520drop%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-west%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C500%255D%252C%2522detectionDirection%2522%253A%2522both%2522%252C%2522minDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522minRelDevFromExpected%2522%253A%255B10%252C10%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minRelDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522temporal_envelope%2522%252C%2522settings%2522%253A%257B%2522seasonalities%2522%253A%255B%2522hod_smooth%2522%252C%2522weekpart_plateau%2522%255D%252C%2522quantiles%2522%253A%255B0.25%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522alpha%2522%253A0.005%252C%2522loss_reactivity%2522%253A3.0%252C%2522changepoint_window%2522%253A16%252C%2522min_n_samples_seen%2522%253A96%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522temporal_envelope%2522%252C%2522seasonalities%2522%253A%255B%2522hod_smooth%2522%252C%2522weekpart_plateau%2522%255D%252C%2522quantiles%2522%253A%255B0.25%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522alpha%2522%253A0.005%252C%2522loss_reactivity%2522%253A3.0%252C%2522changepoint_window%2522%253A16%252C%2522min_n_samples_seen%2522%253A96%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=28d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true).

1. Select **Execute Query** to inspect `checkout_evolving_rate`. The two-week view shows smooth daily cycles over a rising baseline, with lower weekend traffic.
2. Select **Detect Anomalies** to fit and run Temporal Envelope chronologically.
3. Inspect the lasting increase from **January 12, 2026, 00:00 UTC**, then the surge on **January 18, 10:00–13:00 UTC** and drop on **January 20, 02:00–05:00 UTC**. Compare the learned expected range before and after the level change, and during the two brief incidents.

| Setting | Prepared value | Why |
| --- | --- | --- |
| Inference range | January 8 → January 22, 2026, UTC | A focused two-week view of the changes |
| Query step / infer every | `15m` / `15m` | Score each observation in order |
| Fit window / fit every | `28d` / `1000w` | Four weeks of daily and weekend context, with one initial fit |
| Seasonalities | `hod_smooth`, `weekpart_plateau` | A smooth hour-of-day pattern plus weekday/weekend levels |
| Exact | `true` | Imitate production scheduling without future observations changing earlier predictions |
| Streaks | On, minimum `2` points | Connect consecutive incident flags |
| Query policies | Both directions, minimum relative deviation `10%` | Scale business tolerance with the expected traffic |

This [online model](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) keeps learning as new data arrives, so regular refits are optional.

**What to expect:** the center follows the daily curve and gradual growth. The January 12 increase is a <strong title="A lasting shift in the usual level or pattern.">changepoint</strong>. It can receive high scores before the model adapts. The later short surge and drop are separate departures from the new baseline. Scores can fade during an incident, and returning to normal can briefly be flagged while the model catches up. The query is deterministic, and values use requests per second. Use impact and SLO checks to confirm recovery after a lasting change, as the score can fall through adaptation.

{{% /collapse %}}

{{% collapse name="Copy the configuration" %}}

These **reader**, **models**, and **schedulers** sections use a periodic scheduler for continuous scoring. The playground above replays the dated traffic example with the same fit window and cadence. Keep the writer and license settings from the [Quickstart](https://docs.victoriametrics.com/anomaly-detection/quickstart/#example), and use a test writer destination.

```yaml
reader:
  class: vm
  datasource_url: https://play.victoriametrics.com/select/0/prometheus
  sampling_period: 15m
  queries:
    checkout_evolving_rate:
      expr: |
        WITH (
          hour_utc = (time() % 86400) / 3600,
          days_since_start = (time() - 1767225600) / 86400,
          # Unix epoch was Thursday. Number weekdays from Monday=0 to Sunday=6.
          weekday = floor(time() / 86400 + 3) % 7,
          weekend = weekday >= bool 5,
          daily = 60 * sin((hour_utc - 6) / 24 * 6.283185307179586),
          baseline = 150 + 2 * days_since_start + daily - 25 * weekend,
          mixed = sin(time() / 900 * 12.9898 + 42) * 43758.5453,
          noise = 10 * (mixed - floor(mixed) - 0.5),
          migration = time() >= bool 1768176000,
          surge = (time() >= bool 1768730400) * (time() < bool 1768741200),
          drop = (time() >= bool 1768874400) * (time() < bool 1768885200)
        )
        label_set(baseline + noise + 35 * migration + 100 * surge - 70 * drop,
          "__name__", "demo_http_requests_per_second", "region", "eu-west", "service", "checkout")
      detection_direction: both  # Investigate unexpected surges and drops.
      min_rel_dev_from_expected: [10, 10]  # Require at least 10% deviation from the expected value.
      data_range: [0, 500]  # Demo intake's configured capacity is 500 requests/s.

models:
  envelope_checkout_rate:  # Choose a unique model alias.
    class: temporal_envelope  # Select univariate Temporal Envelope.
    queries: [checkout_evolving_rate]  # Connect to one or more reader query aliases.
    schedulers: [evolving_traffic_demo]  # Connect to one or more scheduler aliases.
    seasonalities: [hod_smooth, weekpart_plateau]  # Daily curves and weekday/weekend levels.
    quantiles: [0.25, 0.75]  # Lower and upper residual quantiles. The center is learned separately.
    iqr_threshold: 2.0  # Control the width of the expected range.
    alpha: 0.005  # Trend Reactivity: how quickly the baseline follows lasting changes.
    loss_reactivity: 3.0  # Limit how strongly brief deviations influence learning.
    changepoint_window: 16  # Look for a lasting shift over 16 observations, about four hours here.
    min_n_samples_seen: 96  # Require one day's worth of valid observations before non-neutral scoring.
    clip_predictions: true  # Keep predicted ranges within the query's valid data range.

schedulers:
  evolving_traffic_demo:
    class: periodic  # Run continuously on incoming data.
    fit_window: 28d  # Four repetitions of the weekly pattern.
    fit_every: 1000w  # Learning continues between these very infrequent full refits.
    infer_every: 15m
```

For production, replace the generated expression with your request-rate query and choose history that covers the calendar patterns you enable. The deliberately long `fit_every: 1000w` highlights learning between full refits. Adjust sampling and scheduling to the decisions you need to make.

{{% /collapse %}}

{{% collapse name="Tuning hints: calendar context, reactivity, and lasting changes" %}}

**Check each behavior separately.** Inspect normal daily/weekend cycles, adaptation to the migration, and detection of the brief surge and drop. Recheck all three after changing one setting.

**Use representative calendar context.** Enable patterns covered by fit history, and set the query's [`tz`](https://docs.victoriametrics.com/anomaly-detection/components/reader/#per-query-parameters) for local operating hours. Add holiday context when the metric responds to those events and representative history is available.

For range width, reactivity, shift detection, and warmup settings, use the [Temporal Envelope parameter reference](https://docs.victoriametrics.com/anomaly-detection/components/models/#temporal-envelope). Keep impact or SLO alerts for changes that must remain actionable after the model adapts.

{{% /collapse %}}

</div>
