<!-- Part 7 of 7 of anomaly-detection/guides/model-selection/README.md (split because the page is big). -->

## Find the odd one out

Use [peer-group models](https://docs.victoriametrics.com/anomaly-detection/components/models/#peer-group-models) **when similar entities should behave alike at the same timestamp**. Start with [Peer Outlier](https://docs.victoriametrics.com/anomaly-detection/components/models/#peer-outlier) (`peer_outlier`, experimental, available from v1.31.0). Peer values are compared at the same timestamp, and a separate anomaly score is produced for each peer.

![Peer-group example: seven comparable checkout replicas use about 50 percent CPU, while checkout-08 stays near 84 percent. The steady but unusually high peer is highlighted.](peer-group-comparison.webp)

*checkout-08 stays steady but differs from seven comparable replicas at the same timestamp.*

<div class="collapse-group mb-3">

{{% collapse name="Examples: comparable replicas and hosts" %}}

- **SRE:** one of eight replicas uses more CPU than the others under comparable load.
- **APM:** one host has higher request latency than hosts serving similar work.
- **Hardware:** one disk runs hotter than comparable disks in the same operating conditions.

Separate different workloads, hardware classes, or regions into appropriate populations. A strict majority must behave normally. A shared failure across every peer may look normal to a peer comparison. Add a model that follows each metric over time when shared shifts also matter.

{{% /collapse %}}

</div>

### Uneven behavior across peers

**Start with [Peer Outlier](https://docs.victoriametrics.com/anomaly-detection/components/models/#peer-outlier) (`peer_outlier`).** Choose this **when one member behaves differently from a healthy majority**. One model is fitted for the population, and a separate score is produced for each peer present at a timestamp.

**Example:** checkout replicas in one region have the same CPU limits and serve similar traffic. Most use around 50% CPU, while `checkout-08` stays around 80%, including during the initial fit. Its own pattern is stable, but the difference from comparable replicas deserves investigation. During a three-hour load burst, all healthy replicas rise to about 65%, while `checkout-08` stays near 80%. The accepted peer range follows the majority, and the steady hot replica remains unusual.

<div class="collapse-group mb-3">

{{% collapse name="Use for: comparable entities under similar conditions" %}}

- Replicas of the same service with comparable traffic, resource limits, and deployment roles.
- Hosts of the same hardware class performing similar work.
- Disks, sensors, or other equipment operating under comparable conditions.

Normalize or separate different capacities and workloads before comparing them. A CPU ratio alone cannot account for different request costs or limits. Keep a strict healthy majority in each population.

{{% /collapse %}}

{{% collapse name="Choose another recipe if…" %}}

**A member's own history, a relationship between signals, or a shared change matters more.**

- **All replicas shift together:** add a [per-series model](#follow-each-metric-over-time) or an impact alert. A whole service becoming slower or busier can leave the peer relationships unchanged.
- **Members have different legitimate baselines:** separate the populations using suitable labels, normalize the query, or use per-series models. Examples include different instance sizes, leader/follower roles, or deliberately uneven traffic.
- **Several related metrics describe one entity:** use a [multivariate model](#watch-related-signals-together) to learn their relationship.
- **Too few valid peers or no dependable healthy majority:** improve the population definition or use another comparison. Missing collection data also needs its own monitoring.

{{% /collapse %}}

{{% collapse name="Try it" %}}

**Seven to eight replicas, one steady hot peer, and a spike across the healthy majority.** [Open the peer-group playground](https://play-vmanomaly.victoriametrics.com/metrics/vmui/#/?g0.range_input=3d&g0.end_input=2026-01-17T00%3A00%3A00Z&g0.relative_time=none&g0.step_input=15m&g0.tab=0&datasourceUrl=https%3A%2F%2Fplay.victoriametrics.com%2Fselect%2F0%2Fprometheus&query_config=%255B%257B%2522alias%2522%253A%2522replica_cpu%2522%252C%2522expr%2522%253A%2522WITH%2520%28%255Cn%2520%2520mixed%28seed%29%2520%253D%2520sin%28time%28%29%2520%252F%2520900%2520%2A%252012.9898%2520%252B%2520seed%29%2520%2A%252043758.5453%252C%255Cn%2520%2520noise%28seed%29%2520%253D%25200.004%2520%2A%2520%28mixed%28seed%29%2520-%2520floor%28mixed%28seed%29%29%2520-%25200.5%29%252C%255Cn%2520%2520majority_load%2520%253D%25200.15%2520%2A%2520%28time%28%29%2520%253E%253D%2520bool%25201768557600%29%2520%2A%2520%28time%28%29%2520%253C%2520bool%25201768568400%29%252C%255Cn%2520%2520level%2520%253D%25200.50%2520%252B%25200.04%2520%2A%2520sin%28time%28%29%2520%252F%252086400%2520%2A%25206.283185307179586%29%255Cn%2520%2520%2520%2520%252B%25200.015%2520%2A%2520sin%28time%28%29%2520%252F%2520%285%2520%2A%25203600%29%29%252C%255Cn%2520%2520peer%28name%252C%2520seed%252C%2520offset%29%2520%253D%2520label_set%28level%2520%252B%2520noise%28seed%29%2520%252B%2520offset%252C%255Cn%2520%2520%2520%2520%255C%2522__name__%255C%2522%252C%2520%255C%2522demo_cpu_utilization_ratio%255C%2522%252C%2520%255C%2522instance%255C%2522%252C%2520name%252C%255Cn%2520%2520%2520%2520%255C%2522service%255C%2522%252C%2520%255C%2522checkout%255C%2522%252C%2520%255C%2522region%255C%2522%252C%2520%255C%2522eu-west%255C%2522%29%255Cn%29%255Cnpeer%28%255C%2522checkout-01%255C%2522%252C%252042%252C%2520-0.015%2520%252B%2520majority_load%29%255Cnor%2520peer%28%255C%2522checkout-02%255C%2522%252C%252043%252C%2520-0.010%2520%252B%2520majority_load%29%255Cnor%2520peer%28%255C%2522checkout-03%255C%2522%252C%252044%252C%2520-0.005%2520%252B%2520majority_load%29%255Cnor%2520peer%28%255C%2522checkout-04%255C%2522%252C%252045%252C%25200.000%2520%252B%2520majority_load%29%255Cnor%2520peer%28%255C%2522checkout-05%255C%2522%252C%252046%252C%25200.005%2520%252B%2520majority_load%29%255Cnor%2520%28peer%28%255C%2522checkout-06%255C%2522%252C%252047%252C%25200.010%2520%252B%2520majority_load%29%2520if%2520on%28%29%2520%28time%28%29%2520%253C%25201768521600%29%29%255Cnor%2520%28peer%28%255C%2522checkout-07%255C%2522%252C%252048%252C%25200.015%2520%252B%2520majority_load%29%2520if%2520on%28%29%2520%28time%28%29%2520%253E%253D%25201768467600%29%29%255Cnor%2520peer%28%255C%2522checkout-08%255C%2522%252C%252049%252C%25200.300%29%2522%252C%2522enabled%2522%253Atrue%252C%2522dataRange%2522%253A%255B0%252C1%255D%252C%2522detectionDirection%2522%253A%2522above_expected%2522%252C%2522minDevFromExpected%2522%253A%255B0.05%252C0.05%255D%252C%2522minRelDevFromExpected%2522%253A%255B0%252C0%255D%252C%2522policyOverrides%2522%253A%257B%2522dataRange%2522%253Atrue%252C%2522detectionDirection%2522%253Atrue%252C%2522minDevFromExpected%2522%253Atrue%257D%257D%255D&model_config=%257B%2522modelType%2522%253A%2522peer_outlier%2522%252C%2522settings%2522%253A%257B%2522groupby%2522%253A%255B%2522service%2522%252C%2522region%2522%255D%252C%2522min_peer_count%2522%253A5%252C%2522epsilon_quantile%2522%253A0.75%252C%2522tolerance%2522%253A4.0%252C%2522decay%2522%253A0.999%252C%2522min_n_samples_seen%2522%253A32%252C%2522clip_predictions%2522%253Atrue%252C%2522provide_series%2522%253A%255B%2522anomaly_score%2522%252C%2522y%2522%252C%2522yhat%2522%252C%2522yhat_lower%2522%252C%2522yhat_upper%2522%255D%257D%252C%2522modelSpec%2522%253A%257B%2522class_name%2522%253A%2522peer_outlier%2522%252C%2522groupby%2522%253A%255B%2522service%2522%252C%2522region%2522%255D%252C%2522min_peer_count%2522%253A5%252C%2522epsilon_quantile%2522%253A0.75%252C%2522tolerance%2522%253A4.0%252C%2522decay%2522%253A0.999%252C%2522min_n_samples_seen%2522%253A32%252C%2522clip_predictions%2522%253Atrue%252C%2522provide_series%2522%253A%255B%2522anomaly_score%2522%252C%2522y%2522%252C%2522yhat%2522%252C%2522yhat_lower%2522%252C%2522yhat_upper%2522%255D%257D%252C%2522serverModelAlias%2522%253Anull%252C%2522isValidated%2522%253Atrue%257D&fit_window=1d&fit_every=1000w&infer_every=15m&exact=true&anomaly_threshold=1&anomaly_consecutive=true&anomaly_consecutive_points=2&advanced_options_open=true&show_business_boundaries=true).

1. Select **Execute Query**. The named query `replica_cpu` returns peers labeled by `service`, `region`, and `instance`. Eight identities appear over the replay, with seven or eight present at a time.
2. Select **Detect Anomalies**. Use the [peer-group investigation view](https://docs.victoriametrics.com/anomaly-detection/ui/#peer-group-investigation) to inspect `checkout-08`, which uses more CPU than its peers throughout the view, despite having a stable individual history.
3. Inspect **January 15, 2026, 09:00 UTC**, when a healthy `checkout-07` joins. Its accepted range is available immediately from the existing group's learned state. `checkout-06` leaves at **January 16, 00:00 UTC**, while the remaining peers continue to be compared.
4. Inspect **January 16, 10:00–13:00 UTC**, when all healthy replicas rise together from about 50% to 65% CPU. `checkout-08` stays near 80%. The accepted peer range should follow the majority, leaving the healthy replicas unflagged and the steady hot peer still unusual. Use a temporal model or service-level alert when this majority-wide change matters.

| Setting | Prepared value | Why |
| --- | --- | --- |
| Inference range | January 14 → January 17, 2026, UTC | A focused view of membership changes and a majority-wide spike |
| Query step / infer every | `15m` / `15m` | Compare aligned observations at each timestamp |
| Fit window / fit every | `1d` / `1000w` | Initialize the population once, then keep learning |
| Group by | `service`, `region` | Compare replicas serving the same workload and location |
| Minimum peers | `5` | Require enough valid members at each timestamp |
| Warmup | `32` effective valid population snapshots | About eight hours at this cadence, covered by the one-day fit |
| Exact | `true` | Imitate production scheduling with chronological updates |
| Streaks | On, minimum `2` points | Connect consecutive flags for each peer |
| Query policies | Above expected, minimum deviation `0.05` | Investigate CPU increases of at least five percentage points from the expected peer value |

**What to expect:** one population model produces a separate anomaly-score series for each replica. `checkout-08` should be flagged throughout, even while its distance from the majority shrinks during the spike. Other replicas, including the new member, should stay inside the accepted peer range. The range follows the majority at each timestamp. Values use ratios, so `0.8` means 80% CPU utilization.

{{% /collapse %}}

{{% collapse name="Copy the configuration" %}}

Keep the writer and license configuration from the [Quickstart](https://docs.victoriametrics.com/anomaly-detection/quickstart/#example). This periodic configuration runs continuously. The playground replays the fixed dates above with the same fit window and cadence.

```yaml
reader:
  datasource_url: https://play.victoriametrics.com/select/0/prometheus
  sampling_period: 15m
  queries:
    replica_cpu:  # One CPU-utilization series per comparable replica.
      expr: |
        WITH (
          mixed(seed) = sin(time() / 900 * 12.9898 + seed) * 43758.5453,
          noise(seed) = 0.004 * (mixed(seed) - floor(mixed(seed)) - 0.5),
          majority_load = 0.15 * (time() >= bool 1768557600) * (time() < bool 1768568400),
          level = 0.50 + 0.04 * sin(time() / 86400 * 6.283185307179586)
            + 0.015 * sin(time() / (5 * 3600)),
          peer(name, seed, offset) = label_set(level + noise(seed) + offset,
            "__name__", "demo_cpu_utilization_ratio", "instance", name,
            "service", "checkout", "region", "eu-west")
        )
        peer("checkout-01", 42, -0.015 + majority_load)
        or peer("checkout-02", 43, -0.010 + majority_load)
        or peer("checkout-03", 44, -0.005 + majority_load)
        or peer("checkout-04", 45, 0.000 + majority_load)
        or peer("checkout-05", 46, 0.005 + majority_load)
        or (peer("checkout-06", 47, 0.010 + majority_load) if on() (time() < 1768521600))
        or (peer("checkout-07", 48, 0.015 + majority_load) if on() (time() >= 1768467600))
        or peer("checkout-08", 49, 0.300)
      detection_direction: above_expected  # Investigate peers using unusually high CPU.
      min_dev_from_expected: [0.05, 0.05]  # Five percentage points from the expected peer value.
      data_range: [0, 1]  # CPU utilization expressed as a ratio.

models:
  peer_checkout_cpu:  # A model alias chosen for this recipe.
    class: peer_outlier
    queries: [replica_cpu]  # Connect the query defining this peer population.
    schedulers: [replica_peer_demo]  # Connect the schedule below.
    groupby: [service, region]  # Keep instance identity within the population.
    min_peer_count: 5  # Minimum aligned peers needed for a valid snapshot.
    epsilon_quantile: 0.75  # Learn a reference for the usual population spread.
    tolerance: 4.0  # Control how far a peer may lie from its normal neighbors.
    decay: 0.999  # Give recent population snapshots more influence.
    min_n_samples_seen: 32  # Effective valid snapshots for the group, independent of peer count.
    clip_predictions: true  # Keep the accepted range inside the query's data range.
    provide_series: [anomaly_score, y, yhat, yhat_lower, yhat_upper]  # Diagnostics for the demo.

schedulers:
  replica_peer_demo:
    class: periodic  # Compare current population snapshots continuously.
    fit_window: 1d
    fit_every: 1000w  # Learning continues between these very infrequent full refits.
    infer_every: 15m
```

For production, replace the generated expression with your CPU query. For example, use `1 - avg by (service, region, instance) (rate(node_cpu_seconds_total{mode="idle"}[5m]))` if those labels exist and the instances perform comparable work. Preserve identity labels and aggregate duplicate inputs before comparing peers.

{{% /collapse %}}

{{% collapse name="Hints: populations, warmup, and actionable differences" %}}

**Keep peer identity out of the grouping labels.** [`groupby: [service, region]`](https://docs.victoriametrics.com/anomaly-detection/components/models/#group-by) defines a population for each service and region. The `instance` label identifies members inside it. Grouping by `instance` would split the replicas into separate populations. Each named query keeps its own populations, even when their grouping labels match.

**Distinguish a new peer from a new population.** A peer joining an existing, warmed-up group uses that group's state. A new service or region needs its own fit and warmup. Here, `min_n_samples_seen: 32` requires effective history from valid snapshots with at least five aligned peers. Decay discounts older snapshots. A snapshot with eight peers still contributes one observation. Gaps or too few peers delay learning and scoring, so monitor collection health separately.

**Set the operational difference you care about.** This recipe investigates high CPU and uses a five-percentage-point minimum distance from the expected peer value. A value must also cross the accepted peer range to be flagged. Use `both` or `below_expected` when unexpectedly low utilization matters too. Inspect healthy deployment and autoscaling periods before adjusting sensitivity with `tolerance` or `epsilon_quantile`. See the [Peer Outlier reference](https://docs.victoriametrics.com/anomaly-detection/components/models/#peer-outlier).

**Keep shared failures visible.** The January 16 increase demonstrates a change affecting the healthy majority, while the unusual replica stays at its own level. Add a [temporal model](#follow-each-metric-over-time), a capacity rule, or an SLO alert alongside the peer comparison. Review the population when traffic routing, instance sizes, or deployment roles change.


{{% /collapse %}}

</div>


## Apply a recipe to your own metrics

1. Inspect the query output: units, aggregation, sample interval, missing data, and labels define what the model actually sees.
2. Pick the comparison and profile above. Check that the proposed model's assumptions match normal behavior.
3. Backtest on a period containing both normal behavior and known incidents. Change one setting at a time and inspect the scores and expected ranges.
4. Set query-level business policies and a production schedule. Connect actionable scores to [alerting](https://docs.victoriametrics.com/anomaly-detection/guides/guide-vmanomaly-vmalert/), then review results as the workload changes.

> [!TIP]
> **Try a recipe on your own data.** In [AI Copilot](https://docs.victoriametrics.com/anomaly-detection/ui/#ai-assistance), or your assistant with the [MCP server](https://docs.victoriametrics.com/ai-tools/#vmanomaly-mcp-server) or [agent skills](https://docs.victoriametrics.com/ai-tools/#agent-skills), share your query and the changes you care about. Ask: “Use this guide to recommend a model, validate its configuration, and suggest a backtest.”

For deployment, follow the [Quickstart](https://docs.victoriametrics.com/anomaly-detection/quickstart/). For interactive investigation, use the [UI](https://docs.victoriametrics.com/anomaly-detection/ui/). For parameter details and compatibility, use the [model reference](https://docs.victoriametrics.com/anomaly-detection/components/models/). For a short selection summary, use the [FAQ](https://docs.victoriametrics.com/anomaly-detection/faq/#choosing-the-right-model-for-vmanomaly).
