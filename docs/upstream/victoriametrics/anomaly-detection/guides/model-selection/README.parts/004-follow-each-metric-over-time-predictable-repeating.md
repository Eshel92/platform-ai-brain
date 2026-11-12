<!-- Part 4 of 7 of anomaly-detection/guides/model-selection/README.md (split because the page is big). -->

### Predictable repeating patterns

**Start with [Online Seasonal Quantile](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-seasonal-quantile) (`quantile_online`).** Choose this for **repeating plateaus**, where the usual level stays roughly constant within each time slot. A separate expected range is learned for each slot in the [repeating cycle](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "A pattern that repeats at regular intervals, such as daily or weekly."). Predictions form steps whose levels gradually update as new observations arrive.

**Example:** checkout traffic stays near 50 requests/s overnight and 200 requests/s during opening hours, 09:00–19:00 UTC. A drop to 50 during opening hours or a rise to 200 at night is a [contextual anomaly](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-2/#contextual-anomalies "A value that is unusual for its context, such as the time of day, even if ordinary at other times."): the value is familiar, but its timing is unusual. The query also returns a healthy region with its own lower levels. Each series is modeled separately.

<div class="collapse-group mb-3">

{{% collapse name="Use for: repeating plateaus" %}}

- Service traffic that switches between fairly steady opening-hours and overnight levels.
- Scheduled batch-processing throughput with repeatable active and idle periods.
- Hardware power usage that follows a stable shift schedule.
- Business activity with repeatable daily or weekly operating windows.
- Custom production cycles: for a line whose product mix and processing/cleaning schedule repeat every two weeks, three-hour slots can capture the usual throughput or power usage for each stage.

The normal level and spread should be fairly consistent when the same time slot returns. Place bucket boundaries at changes between operating periods, so each bucket mostly contains one normal level.

{{% /collapse %}}

{{% collapse name="Choose another recipe if…" %}}

**Smooth curves, mixed time slots, or changing baselines can make step-shaped predictions a poor fit.**

- **Smooth [seasonal curves](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "Patterns that repeat at regular intervals, such as daily or weekly."), such as sinusoids:** one nearly horizontal range covers the whole bucket. If the signal moves substantially within that interval, the expected value can be too high at one end and too low at the other. Narrow bounds can flag normal movement, while wide bounds can hide smaller incidents. Consider [Temporal Envelope](#changing-baselines-and-calendar-effects) for smooth patterns.
- **Neighboring hours with different normal levels:** a two-hour bucket can mix an hour near 50 requests/s with one near 200. Its shared center may represent neither hour well, and its range can become wide enough to accept both levels at the wrong time. Smaller, correctly aligned buckets help, provided enough history is available for each.
- **Normal [growth](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend "A sustained increase or decrease in the usual level of a time series."), shifting operating hours, or frequent level changes:** use [Temporal Envelope](#changing-baselines-and-calendar-effects) when these changes are expected. Fixed seasonal slots work best when the same operating periods recur.
- **Little repeated history or sparse samples:** a bucket cannot learn a dependable range from a few observations. Check aggregation and cycle coverage before making the buckets smaller.

Mixing different normal phases can widen the range and hide incidents. Robust quantiles reduce the influence of extreme values. Use suitable bucket boundaries to preserve the time context.

**See the smooth-curve limitation.** [Open the smooth-curve example with four-hour buckets](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=14d&g0.end_input=2026-01-17T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_request_rate%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520hour_utc%2520%253D%2520%28time%28%29%2520%2525%252086400%29%2520%252F%25203600%252C%255Cn%2520%2520%2523%2520A%2520smooth%2520daily%2520cycle%2520from%252050%2520to%2520200%2520requests%252Fs%252C%2520peaking%2520at%2520noon.%255Cn%2520%2520baseline%2520%253D%2520125%2520%252B%252075%2520%2A%2520sin%28%28hour_utc%2520-%25206%29%2520%252F%252024%2520%2A%25206.283185307179586%29%252C%255Cn%2520%2520mixed%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%252042%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%2520%253D%252010%2520%2A%2520%28mixed%2520-%2520floor%28mixed%29%2520-%25200.5%29%252C%255Cn%2520%2520slowdown%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768041000%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768044600%29%255Cn%29%255Cnlabel_set%28baseline%2520%252B%2520noise%2520-%252030%2520%2A%2520slowdown%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-west%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C500%255D%252C%2522detectionDirection%2522%253A%2522both%2522%252C%2522minDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522minRelDevFromExpected%2522%253A%255B10%252C10%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minRelDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522quantile_online%2522%252C%2522settings%2522%253A%257B%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25224h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522quantile_online%2522%252C%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25224h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=14d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true). Select **Detect Anomalies**, then inspect **January 10, 2026, 10:30–11:30 UTC**. A 30 requests/s drop in otherwise smooth daily traffic can stay inside the broad range learned for 08:00–12:00. [Compare the same curve with one-hour buckets](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=14d&g0.end_input=2026-01-17T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_request_rate%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520hour_utc%2520%253D%2520%28time%28%29%2520%2525%252086400%29%2520%252F%25203600%252C%255Cn%2520%2520%2523%2520A%2520smooth%2520daily%2520cycle%2520from%252050%2520to%2520200%2520requests%252Fs%252C%2520peaking%2520at%2520noon.%255Cn%2520%2520baseline%2520%253D%2520125%2520%252B%252075%2520%2A%2520sin%28%28hour_utc%2520-%25206%29%2520%252F%252024%2520%2A%25206.283185307179586%29%252C%255Cn%2520%2520mixed%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%252042%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%2520%253D%252010%2520%2A%2520%28mixed%2520-%2520floor%28mixed%29%2520-%25200.5%29%252C%255Cn%2520%2520slowdown%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768041000%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768044600%29%255Cn%29%255Cnlabel_set%28baseline%2520%252B%2520noise%2520-%252030%2520%2A%2520slowdown%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-west%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C500%255D%252C%2522detectionDirection%2522%253A%2522both%2522%252C%2522minDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522minRelDevFromExpected%2522%253A%255B10%252C10%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minRelDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522quantile_online%2522%252C%2522settings%2522%253A%257B%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25221h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522quantile_online%2522%252C%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25221h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=14d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true). Smaller buckets reveal the drop but can also flag normal within-hour movement. Set the Streaks minimum to `1` to inspect isolated flags.

These links use one region and the query below, shown over January 3–17, 2026, UTC to keep the slowdown near the center. They retain the recipe's 14-day fit history, quantiles, and 10% relative-deviation policy. Only the bucket width differs between the two links. For the coarse model settings, replace the query in the configuration below and set `min_subseason: 4h`.

```metricsql
WITH (
  hour_utc = (time() % 86400) / 3600,
  # A smooth daily cycle from 50 to 200 requests/s, peaking at noon.
  baseline = 125 + 75 * sin((hour_utc - 6) / 24 * 6.283185307179586),
  mixed = sin(time() / 900 * 12.9898 + 42) * 43758.5453,
  noise = 10 * (mixed - floor(mixed) - 0.5),
  slowdown = (time() >= bool 1768041000) * (time() < bool 1768044600)
)
label_set(baseline + noise - 30 * slowdown,
  "__name__", "demo_http_requests_per_second", "region", "eu-west", "service", "checkout")
```

{{% /collapse %}}

{{% collapse name="Try it" %}}

**Two regions, daily plateaus, and values arriving at the wrong time.**

[Open the plateau-pattern playground](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=14d&g0.end_input=2026-01-22T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_request_rate%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520hour_utc%2520%253D%2520%28time%28%29%2520%2525%252086400%29%2520%252F%25203600%252C%255Cn%2520%2520open%2520%253D%2520%28hour_utc%2520%253E%253D%2520bool%25209%29%2520%2A%2520%28hour_utc%2520%253C%2520bool%252019%29%252C%255Cn%2520%2520baseline%2520%253D%252050%2520%252B%2520150%2520%2A%2520open%252C%255Cn%2520%2520%2523%2520Small%2520timestamp-based%2520noise%252C%2520in%2520requests%2520per%2520second.%255Cn%2520%2520mixed%28seed%29%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%2520seed%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%28seed%29%2520%253D%252010%2520%2A%2520%28mixed%28seed%29%2520-%2520floor%28mixed%28seed%29%29%2520-%25200.5%29%252C%255Cn%2520%2520daytime_drop%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768035600%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768039200%29%252C%255Cn%2520%2520nighttime_rise%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768874400%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768885200%29%255Cn%29%255Cnlabel_set%28baseline%2520%252B%2520noise%2842%29%2520-%2520150%2520%2A%2520daytime_drop%2520%252B%2520150%2520%2A%2520nighttime_rise%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-west%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%255Cnor%2520label_set%280.6%2520%2A%2520baseline%2520%252B%2520noise%2843%29%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-east%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C500%255D%252C%2522detectionDirection%2522%253A%2522both%2522%252C%2522minDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522minRelDevFromExpected%2522%253A%255B10%252C10%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minRelDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522quantile_online%2522%252C%2522settings%2522%253A%257B%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25221h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522quantile_online%2522%252C%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25221h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=14d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true).

1. Select **Execute Query** to inspect `checkout_request_rate` for two regions. Both switch between overnight and opening-hours plateaus.
2. Select **Detect Anomalies** to run Online Seasonal Quantile with one-hour buckets.
3. Inspect `eu-west` on **January 10, 2026, 09:00–10:00 UTC**, when traffic drops to the overnight level, and **January 20, 02:00–05:00 UTC**, when it rises to the opening-hours level. Both incidents should cross the expected range. The regular daily transitions and `eu-east` should remain unflagged.

| Setting | Prepared value | Why |
| --- | --- | --- |
| Inference range | January 8 → January 22, 2026, UTC | Two weeks covering both incidents |
| Query step / infer every | `15m` / `15m` | Four observations per hour per series |
| Fit window / fit every | `14d` / `1000w` | Initialize from fourteen daily cycles, with no refit during the example |
| Seasonal interval / bucket | `1d` / `1h` | Keep 24 separate clock-hour ranges per series |
| Exact | `true` | Process observations chronologically, imitating production scheduling |
| Streaks | On, minimum `2` points | Connect consecutive flags in each incident |
| Query policies | Both directions, minimum relative deviation `10%` | Scale tolerance to each region's expected traffic |

This [online model](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-models) keeps learning as new data arrives, so regular refits are optional.

**What to expect:** the expected range steps between the low and high plateaus at 09:00 and 19:00 UTC. The daytime incident affects four observations, and the nighttime incident affects twelve. Values use requests per second. The two regions have separate expected ranges, even though one query returns both series.

[Compare with two-hour buckets](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=14d&g0.end_input=2026-01-22T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522checkout_request_rate%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520hour_utc%2520%253D%2520%28time%28%29%2520%2525%252086400%29%2520%252F%25203600%252C%255Cn%2520%2520open%2520%253D%2520%28hour_utc%2520%253E%253D%2520bool%25209%29%2520%2A%2520%28hour_utc%2520%253C%2520bool%252019%29%252C%255Cn%2520%2520baseline%2520%253D%252050%2520%252B%2520150%2520%2A%2520open%252C%255Cn%2520%2520%2523%2520Small%2520timestamp-based%2520noise%252C%2520in%2520requests%2520per%2520second.%255Cn%2520%2520mixed%28seed%29%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%2520seed%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%28seed%29%2520%253D%252010%2520%2A%2520%28mixed%28seed%29%2520-%2520floor%28mixed%28seed%29%29%2520-%25200.5%29%252C%255Cn%2520%2520daytime_drop%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768035600%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768039200%29%252C%255Cn%2520%2520nighttime_rise%2520%253D%2520%28time%28%29%2520%253E%253D%2520bool%25201768874400%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768885200%29%255Cn%29%255Cnlabel_set%28baseline%2520%252B%2520noise%2842%29%2520-%2520150%2520%2A%2520daytime_drop%2520%252B%2520150%2520%2A%2520nighttime_rise%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-west%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%255Cnor%2520label_set%280.6%2520%2A%2520baseline%2520%252B%2520noise%2843%29%252C%255Cn%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_http_requests_per_second%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-east%255C%2522%252C%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C500%255D%252C%2522detectionDirection%2522%253A%2522both%2522%252C%2522minDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522minRelDevFromExpected%2522%253A%255B10%252C10%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minRelDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522quantile_online%2522%252C%2522settings%2522%253A%257B%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25222h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522quantile_online%2522%252C%2522seasonal_interval%2522%253A%25221d%2522%252C%2522min_subseason%2522%253A%25222h%2522%252C%2522season_starts_from%2522%253A%25222026-01-01%2522%252C%2522quantiles%2522%253A%255B0.25%252C0.5%252C0.75%255D%252C%2522iqr_threshold%2522%253A2.0%252C%2522global_smoothing%2522%253A0.0%252C%2522min_n_samples_seen%2522%253A96%252C%2522decay%2522%253A0.99%252C%2522history_strength%2522%253A1.0%252C%2522compression%2522%253A100%252C%2522clip_predictions%2522%253Atrue%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=14d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true). Only `min_subseason` changes from `1h` to `2h`. Inspect 08:00–10:00 and 18:00–20:00 UTC: each coarse bucket now covers an hour from each plateau. Compare the wider range and less representative expected value with the one-hour version. The January 10 drop can disappear into that mixed range, even though its business meaning is unchanged.

{{% /collapse %}}

{{% collapse name="Copy the configuration" %}}

These **reader**, **models**, and **schedulers** sections use a periodic scheduler for continuous scoring. The playground above replays the dated plateau example with the same fit window and cadence. Keep the writer and license settings from the [Quickstart](https://docs.victoriametrics.com/anomaly-detection/quickstart/#example), and use a test writer destination.

```yaml
reader:
  class: vm
  datasource_url: https://play.victoriametrics.com/select/0/prometheus
  sampling_period: 15m
  queries:
    checkout_request_rate:
      expr: |
        WITH (
          hour_utc = (time() % 86400) / 3600,
          open = (hour_utc >= bool 9) * (hour_utc < bool 19),
          baseline = 50 + 150 * open,
          # Small timestamp-based noise, in requests per second.
          mixed(seed) = sin(time() / 900 * 12.9898 + seed) * 43758.5453,
          noise(seed) = 10 * (mixed(seed) - floor(mixed(seed)) - 0.5),
          daytime_drop = (time() >= bool 1768035600) * (time() < bool 1768039200),
          nighttime_rise = (time() >= bool 1768874400) * (time() < bool 1768885200)
        )
        label_set(baseline + noise(42) - 150 * daytime_drop + 150 * nighttime_rise,
          "__name__", "demo_http_requests_per_second", "region", "eu-west", "service", "checkout")
        or label_set(0.6 * baseline + noise(43),
          "__name__", "demo_http_requests_per_second", "region", "eu-east", "service", "checkout")
      detection_direction: both  # Unexpected traffic rises and falls both matter.
      min_rel_dev_from_expected: [10, 10]  # Ignore deviations smaller than 10% below/above the expected value.
      data_range: [0, 500]  # Demo intake's configured capacity is 500 requests/s.

models:
  quantile_daily_traffic:  # Choose a unique model alias.
    class: quantile_online  # Select Online Seasonal Quantile.
    queries: [checkout_request_rate]  # Connect to one or more reader query aliases.
    schedulers: [daily_traffic_demo]  # Connect to one or more scheduler aliases.
    seasonal_interval: 1d  # Repeat the same daily pattern.
    min_subseason: 1h  # Keep a separate range for each clock hour.
    season_starts_from: '2026-01-01'  # Align the demo's buckets to UTC midnight.
    quantiles: [0.25, 0.5, 0.75]  # Robust lower, central, and upper estimates.
    iqr_threshold: 2.0  # Widen the range to tolerate ordinary within-bucket noise.
    global_smoothing: 0.0  # Keep the time-specific ranges separate from the overall range.
    min_n_samples_seen: 96  # Total valid observations required before non-neutral scoring.
    decay: 0.99  # Let each time slot gradually adapt as it is observed again.
    history_strength: 1.0  # Give the initial fit its ordinary weight.
    compression: 100  # Starting accuracy/memory tradeoff for approximate quantiles.
    clip_predictions: true  # Keep predicted ranges within the query's valid data range.

schedulers:
  daily_traffic_demo:
    class: periodic  # Run continuously on incoming data.
    fit_window: 14d  # Fourteen daily cycles with 56 samples per hour slot.
    fit_every: 1000w  # Learning continues between these very infrequent full refits.
    infer_every: 15m
```

For the coarse-bucket comparison, change only `min_subseason: 1h` to `min_subseason: 2h`. For real traffic, replace the generated expression with your request-rate query, for example `sum by (region, service) (rate(http_requests_total{service="checkout"}[5m]))` if those labels exist. Choose the cycle and buckets from the resulting series, after aggregation.

{{% /collapse %}}

{{% collapse name="Tuning hints: bucket size, history, and sensitivity" %}}

**Align buckets with operating periods.** `min_subseason` sets the bucket width independently of the query step. Here `1h` holds four `15m` observations from the same clock hour each day. It divides `seasonal_interval: 1d` into 24 slots. A two-hour bucket mixes the 08:00 overnight hour with the 09:00 opening hour. Smaller buckets can follow a smooth curve more closely, but need more repeated cycles to estimate each slot reliably.

**Use custom cycles when the operation calls for them.** The cycle need not be a day or a week. For the two-week production plan above, `seasonal_interval: 2w` and `min_subseason: 3h` create 112 separate slots. Set `season_starts_from` to the plan's actual starting date and time, and use several complete cycles as fit history. For example, `fit_window: 6w` covers three repetitions. The slot width must divide the full cycle evenly, and its boundaries should keep different operating stages separate.

**Cover every slot before relying on it.** The `14d` fit supplies fourteen daily cycles and about 56 observations per hour slot. `min_n_samples_seen: 96` checks the total observations seen by a model. Inspect each bucket separately to confirm that it has enough observations. For a weekly schedule, use a weekly cycle with enough history to observe each weekday and weekend slot repeatedly. Increasing `history_strength` cannot supply missing weekdays or unseen operating periods.

**Use quantiles and IQR together.** The middle quantiles `[0.25, 0.5, 0.75]` reduce the influence of a few extreme values. `iqr_threshold` expands the resulting range using the spread within each bucket. Increasing it tolerates more variation but can hide incidents. Very wide quantiles near `0` and `1` can let rare extremes widen the range. Neither choice fixes a bucket that contains two different normal levels.

**Scale business tolerance with the expected traffic.** [`min_rel_dev_from_expected: [10, 10]`](https://docs.victoriametrics.com/anomaly-detection/components/models/#minimal-relative-deviation-from-expected) ignores deviations smaller than 10% below or above the expected value. That is about 5 requests/s when 50 is expected, or 20 requests/s when 200 is expected. The percentage is measured from the expected value. A sample must exceed both this tolerance and the model's expected range to be flagged.

**Distinguish global blending from a smooth seasonal curve.** `global_smoothing: 0` uses each slot's own distribution. Increasing it blends in the distribution across all times, which can reduce the contrast between overnight and opening-hours predictions. The bucket boundaries still produce steps.

**Match time and cadence to the schedule.** The generated pattern and bucket alignment use UTC. The UI may display those same instants in another timezone. Check local operating hours, daylight-saving changes, and the cycle reference point when applying the recipe. Keep the query step and inference cadence deliberate: changing them changes how many observations each slot receives.

**Let accepted changes adapt gradually.** `decay` below `1` gives new observations more influence when their slot is updated. A slot seen only during one clock hour adapts on a different wall-clock timescale from a continuously updated Z-score baseline. If changing levels or moving schedules are part of normal behavior, consider [Temporal Envelope](#changing-baselines-and-calendar-effects).

{{% /collapse %}}

</div>
