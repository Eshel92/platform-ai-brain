<!-- Part 1 of 7 of anomaly-detection/guides/model-selection/README.md (split because the page is big). -->

## Choose what to compare

| Your question | Compare | Start here |
| --- | --- | --- |
| Has this metric changed unexpectedly? | Each series with its own history | [Follow each metric over time](#follow-each-metric-over-time) |
| Are these signals behaving unusually together? | Related signals for the same service or host | [Watch related signals together](#watch-related-signals-together) |
| Is one replica behaving differently from the others? | Comparable entities at the same time | [Find the odd one out](#find-the-odd-one-out) |

These are [univariate](https://docs.victoriametrics.com/anomaly-detection/components/models/#univariate-models "Each series is evaluated independently against its own history."), [multivariate](https://docs.victoriametrics.com/anomaly-detection/components/models/#multivariate-models "Related signals are evaluated together, with a joint decision per group."), and [peer-group](https://docs.victoriametrics.com/anomaly-detection/components/models/#peer-group-models "Comparable entities are evaluated against each other at the same timestamp.") models, respectively. The comparison determines the model type, including when one query returns many series.

> [!NOTE]
> **Inside each recipe in this guide:** a practical use case, when to use or avoid the model, copyable YAML, a reproducible UI playground with the query, model, and schedule already set, expected results, and tuning hints. Expand the sections you need.

For individual parameters, use the [model reference](https://docs.victoriametrics.com/anomaly-detection/components/models/#overview).


## Follow each metric over time

Use this **when each series has its own definition of normal**. For example, a query can return one CPU-utilization series for each of two instances. A separate model is fitted for each series, and anomaly scores are then produced for each instance.

![Univariate example: one CPU-utilization series stays near 40 percent, with an earlier unusual rise and a new rise to about 55 percent highlighted against its historical range.](univariate-comparison.webp)

*Suspicious values are compared with this instance's historical range.*

<div class="collapse-group mb-3">

{{% collapse name="Examples: infrastructure, application, hardware, and business metrics" %}}

- **SRE:** detect an unexpected rise in CPU utilization for one instance under steady load.
- **APM:** detect a latency increase for a route whose normal response time is stable. Use a seasonal recipe if traffic drives [regular daily changes](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "A pattern that repeats at regular intervals, such as daily or weekly.").
- **Hardware:** detect an unusual temperature change on one sensor. Retain fixed safety limits for overheating.
- **Business:** detect a drop in a conversion rate. Use a seasonal recipe when the expected rate has [daily or weekly patterns](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "A pattern that repeats at regular intervals, such as daily or weekly.").

Choose the profile below by inspecting the query's output after aggregation or rate calculation.

{{% /collapse %}}

</div>

| What normal data looks like | Starting model | Recipe |
| --- | --- | --- |
| One steady level, small fluctuations, few extreme values | [Online Z-score](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-z-score) | [Steady baseline, small fluctuations](#steady-baseline-small-fluctuations) |
| Mostly steady, but occasional extreme values should not distort the baseline | [Online MAD](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-mad) | [Steady baseline with extreme values](#steady-baseline-with-extreme-values) |
| Repeating plateaus with little [trend](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend "A sustained increase or decrease in the usual level of a time series."), including daily, weekly, or custom cycles, such as a two-week production plan with three-hour operating slots | [Online Seasonal Quantile](https://docs.victoriametrics.com/anomaly-detection/components/models/#online-seasonal-quantile) | [Predictable repeating patterns](#predictable-repeating-patterns) |
| [Trends](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#trend "A sustained increase or decrease in the usual level of a time series."), [seasonalities](https://victoriametrics.com/blog/victoriametrics-anomaly-detection-handbook-chapter-1/#seasonality "Patterns that repeat at regular intervals, such as daily or weekly."), changing levels, or additional calendar effects | [Temporal Envelope](https://docs.victoriametrics.com/anomaly-detection/components/models/#temporal-envelope) | [Changing baselines and calendar effects](#changing-baselines-and-calendar-effects) |
