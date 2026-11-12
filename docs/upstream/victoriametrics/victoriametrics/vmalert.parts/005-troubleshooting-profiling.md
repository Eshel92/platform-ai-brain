<!-- Part 5 of 6 of victoriametrics/vmalert.md (split because the page is big). -->

## Troubleshooting

### Common mistakes

Try the following tips to avoid common issues:

1. Always set [group's interval](https://docs.victoriametrics.com/victoriametrics/vmalert/#groups) to be **equal to or greater than**
   the [time series resolution](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series-resolution).
1. Don't set labels with dynamic values to `labels` [param](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerting-rules).
    * Example: setting `label: {{$value}}` to the rule will break its [alert state tracking](https://docs.victoriametrics.com/victoriametrics/vmalert/#alert-state)
      because every evaluation could change the `label` value. If you need to attach `$value` to the alert notification - add it to `annotations` instead.
1. vmalert runs [instant queries](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) during rule evaluation
   using the `step` parameter, which defaults  to `-datasource.queryStep` (default is `5m`).
   In VictoriaMetrics, `step` controls how far back the query can look for a recent datapoint.
   If [series resolution](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series-resolution)
   is `>=5m`, the query might return no data.
   * To fix this, set `-datasource.queryStep` to value at least **2x larger** than the resolution.
     You can also set `step` per group using the `params` setting.
1. Be careful when chaining rules. If rule B uses results from rule A, make sure rule A is evaluated with an
   interval **less than 5 minutes** (or less than `-datasource.queryStep`). Otherwise, rule B might get empty results during evaluation.
   See how to [chain groups](https://docs.victoriametrics.com/victoriametrics/vmalert/#chaining-groups).
1. Don't skip `[lookbehind-window]` in rollup functions.
   * Example: `rate(errors_total) > 0`. MetricsQL [allows omitting lookbehind window](https://docs.victoriametrics.com/victoriametrics/metricsql/#metricsql-features)
   but that works well only with [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
   For [instant requests](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#instant-query) setting window
   makes the query predictable.
1. Make sure the `[lookbehind-window]` in your expression is at least **2× larger** than [time series resolution](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series-resolution).
    * Example: in `rate(my_metric[2m]) > 0`, ensure that `my_metric` is scraped every 1 minute or better, every 30 seconds.
1. Increase `[lookbehind-window]` to help tolerate data delays.
   * Example: `max_over_time(node_memory_MemAvailable_bytes[10m]) > 0` will still work even if no data was present in the last 9 minutes.
1. Don't skip step in [subqueries](https://docs.victoriametrics.com/victoriametrics/metricsql/#subqueries).
   * Example: `sum(count_over_time((metric == 0)[1h:]))` is missing a step after `1h:`.
    In that case, the default step will be used (`-datasource.queryStep`) and may cause unexpected results compared to
    executing this query in vmui/Grafana, where step is adjusted differently.

See [practical examples for reducing alert noise](https://victoriametrics.com/blog/alerting-best-practices/#reducing-noise),
including aggregating alerts and configuring inhibition.

### Rule state

vmalert keeps the last `-rule.updateEntriesLimit` updates (or `update_entries_limit` [per-rule config](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerting-rules))
for each rule. You can see these updates in vmalert's [web UI](#web):

1. Open the `Groups` tab
2. Find the Group and rule you're interested in
3. Click the `Details` link next to rule's name and look at the `Last N updates` section:

![vmalert state](vmalert_state.webp)

The rows in this section show the rule's evaluations in order, along with their results.

Every state has the following attributes:

1. `Updated at` - the actual time when vmalert executed this rule.
1. `Execution timestamp` - the `time` param that was sent to the datasource with evaluation request.
1. `Series returned` - the number of series returned in this evaluation:
    * A recording rule with 0 series means it produced no results;
    * An alerting rule with 0 series means the rule is in inactive state.
1. `Series fetched` - the number of series scanned during execution. See [never-firing alerts](#never-firing-alerts).
1. `Duration` - how long it took to evaluate the rule.
    * If this time is close to or longer than the evaluation interval, some evaluations might be skipped.
    * See how to handle [slow queries](https://docs.victoriametrics.com/victoriametrics/troubleshooting/#slow-queries).
1. `cURL` - a sample HTTP request that vmalert sent to `-datasource.url` during evaluation.
    * It includes all headers and query parameters.
    * You can use this command to debug and see what the data source returned at that moment of time.
    * _Sensitive data is removed from the `curl` example – see the [security](#security) section for more info._

> If a specific entry shows **Series returned: 0**, but the **cURL command returns some data** when you execute it,
it likely means there was no data in the data source at the exact time the rule was evaluated.
See more about [data delay](#data-delay).

vmalert exposes `vmalert_recording_rules_last_evaluation_samples` for recording rules to represent the amount of series
returned during evaluations. The following alerting rule can be used to detect those recording rules that produce no data:

```yaml
      - alert: RecordingRulesNoData
        expr: vmalert_recording_rules_last_evaluation_samples < 1
        annotations:
          summary: "Recording rule {{ $labels.recording }} ({{ $labels.group }}) produces no data"
```

_See more about alerting rules in [Monitoring](#monitoring)._

### Alert state

Sometimes, it's hard to understand why a specific alert fired or not. Keep in mind the following:

* Alerts with `for: 0` (or not set) fire **immediately** after the evaluation.
* Alerts with `for > 0` fire **only after several evaluations in a row**, if the expression is true every time.

If evaluation returns error (i.e. datasource is unavailable), alert state doesn't change.
If at least one evaluation returns no data, then alert's `for` state resets.

See [how to tune the `for` parameter](https://victoriametrics.com/blog/alerting-best-practices/#the-for-param),
including its tradeoff with the query lookbehind window.

> Note: The alert state is tracked separately for each time series returned during evaluation.
> For example, if the 1st evaluation returns series A and B, and the 2nd evaluation returns only B – the alert will remain active **only for B**.

If `-remoteWrite.url` command-line flag is configured, vmalert will [persist alert's state](http://docs.victoriametrics.com/victoriametrics/vmalert/#alerts-state-on-restarts)
in form of time series `ALERTS` and `ALERTS_FOR_STATE` to the specified destination. Such time series can be then queried via
[vmui](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmui) or Grafana to track how
alerts state changed in time. See [query statistics dashboard](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/dashboards/alert-statistics.json) as example for tracking historical alerts state.

### Data delay

Data delay is one of the most common problems when running rules.

vmalert runs the configured rules at specific timestamps.
It expects that the needed data is already available in the configured `-datasource.url` **at the time** the rule is evaluated.

![vmalert expected evaluation](vmalert_ts_normal.gif)

Usually, troubles begin when data in `-datasource.url` is delayed or absent. In such cases, evaluations
may get an empty response from the datasource, produce empty recording rules or reset alerts state:

![vmalert evaluation when data is delayed](vmalert_ts_data_delay.gif)

> Please note, data delay is inevitable in distributed systems. And it is better to account for it rather than ignore it.

By default, recently written samples to VictoriaMetrics [aren't visible for queries](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-latency)
for up to `30s` (see `-search.latencyOffset` command-line flag at vmselect or VictoriaMetrics single-node).
Such delay is needed to eliminate the risk of incomplete data on the moment of querying. To compensate the latency in
timestamps for produced evaluation results, `-rule.evalDelay` is also set to `30s` by default.
If you expect data to be delayed for longer intervals (it gets buffered, queued, or just network is slow sometimes),
or you changed default value of `-search.latencyOffset` - consider increasing the `-rule.evalDelay` value accordingly.

See [common mistakes](#common-mistakes) for recommendations for dealing with sporadic or delayed data.

### Debug mode

vmalert allows configuring more detailed logging for specific rule starting from {{% available_from "v1.116.0" %}}.
Or for all rules within the [group](#groups) {{% available_from "v1.117.0" %}}.
Just set `debug: true` in configuration and vmalert will start printing additional log messages:

```sh
2026-08-20T08:21:29.464Z        info    VictoriaMetrics/app/vmalert/datasource/client.go:262    DEBUG datasource request: executing POST request with params "http://victoriametrics:8428/api/v1/query?query=up%7Bjob%3D~%22.%2A%28victoriametrics%7Cvmselect%7Cvminsert%7Cvmstorage%7Cvmagent%7Cvmalert%7Cvmsingle%7Cvmalertmanager%7Cvmauth%29.%2A%22%7D&step=300s&time=2026-08-20T08%3A20%3A00Z"
2026-08-20T08:21:29.465Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:20:00Z: query returned 0 series (series_fetched: 0, elapsed: 1.075166ms, isPartial: false)
...
2026-08-20T08:22:29.466Z        info    VictoriaMetrics/app/vmalert/datasource/client.go:262    DEBUG datasource request: executing POST request with params "http://victoriametrics:8428/api/v1/query?query=up%7Bjob%3D~%22.%2A%28victoriametrics%7Cvmselect%7Cvminsert%7Cvmstorage%7Cvmagent%7Cvmalert%7Cvmsingle%7Cvmalertmanager%7Cvmauth%29.%2A%22%7D&step=300s&time=2026-08-20T08%3A21%3A00Z"
2026-08-20T08:22:29.468Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:21:00Z: query returned 2 series (series_fetched: 2, elapsed: 2.055916ms, isPartial: false)
2026-08-20T08:22:29.469Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:21:00Z: alert 4671711516378822929 {alertgroup="vm-health",alertname="ServiceDown",instance="victoriametrics:8428",job="victoriametrics",severity="critical"} created in state PENDING
2026-08-20T08:22:29.469Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:21:00Z: alert 6230585559362831632 {alertgroup="vm-health",alertname="ServiceDown",instance="vmagent:8429",job="vmagent",severity="critical"} created in state PENDING
...
2026-08-20T08:23:29.463Z        info    VictoriaMetrics/app/vmalert/datasource/client.go:262    DEBUG datasource request: executing POST request with params "http://victoriametrics:8428/api/v1/query?query=up%7Bjob%3D~%22.%2A%28victoriametrics%7Cvmselect%7Cvminsert%7Cvmstorage%7Cvmagent%7Cvmalert%7Cvmsingle%7Cvmalertmanager%7Cvmauth%29.%2A%22%7D&step=300s&time=2026-08-20T08%3A22%3A00Z"
2026-08-20T08:23:29.465Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:22:00Z: query returned 2 series (series_fetched: 2, elapsed: 1.391416ms, isPartial: false)
2026-08-20T08:23:29.466Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:22:00Z: alert 4671711516378822929 {alertgroup="vm-health",alertname="ServiceDown",instance="victoriametrics:8428",job="victoriametrics",severity="critical"} PENDING => FIRING: 1m0s since becoming active at 2026-08-20 08:21:00 +0000 UTC
2026-08-20T08:23:29.466Z        info    VictoriaMetrics/app/vmalert/rule/alerting.go:273        DEBUG alerting rule "/etc/alerts/alerts-health.yml", "vm-health":"ServiceDown" (1340947595484135783) at 2026-08-20T08:22:00Z: alert 6230585559362831632 {alertgroup="vm-health",alertname="ServiceDown",instance="vmagent:8429",job="vmagent",severity="critical"} PENDING => FIRING: 1m0s since becoming active at 2026-08-20 08:21:00 +0000 UTC
```

Sensitive info is stripped from the `curl` examples - see [security](#security) section for more details.

### Flapping alerts

Transient alerts, that change state from inactive to firing too frequently, called **flapping alerts**.

The following expression will show how many times a specific rule switched its state over last 24h:

```promql
max(changes(vmalert_alerts_firing[24h])) by(group, alertname) > 0
```

How to reduce the chance for a rule to flap:

1. Use the `for <interval>:` setting with a value much larger than the `scrape_interval` for the series used in the expression.
   Note, the larger is `for`, the longer it takes for the alert to fire.
1. Set a `[lookbehind-window]` in rollup expressions (i.e. `rate(http_errors_total[<lookbehind-window>]) > 0`) to at least **2× the `scrape_interval`** for the selected series.
1. Use `keep_firing_for: <interval>` to delay alert resolution if the expression stops returning data.
   For example, for short CPU spikes, you may want to keep the alert active until CPU usage stays low for 5 minutes in a row.
1. Make sure your rule can handle possible [data delays](#data-delay) from the datasource.
1. Review the metric's past behavior to set a threshold that avoids triggering alerts too easily.

See [common mistakes](#common-mistakes) for rules config.

### Never-firing alerts

vmalert can detect {{% available_from "v1.91.0" %}} if alert's expression doesn't match any time series in runtime.
This problem usually happens when alerting expression selects time series which aren't present in the datasource (i.e. wrong `job` label)
or there is a typo in the series selector (i.e. `env=prodd`). Such alerting rules will be marked with special icon in
vmalert UI and exposed via `vmalert_alerting_rules_last_evaluation_series_fetched` metric. The metric value will
show how many time series were matched before the filtering by rule's expression. If metric value is `-1`, then
this feature is not supported by the datasource (old versions of VictoriaMetrics). The following expression can be
used to detect rules matching no series:

```
max(vmalert_alerting_rules_last_evaluation_series_fetched) by(group, alertname) == 0
```

See more details in this [GitHub Issue](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4039) and
read [Never-firing alerts](https://victoriametrics.com/blog/never-firing-alerts/) blogpost.

### Series with the same labelset

vmalert can produce the following error message:

```
result contains metrics with the same labelset during evaluation
```

The error means there is a collision between [time series](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#time-series)
during evaluation.

For example, a rule with `expr: {__name__=~"vmalert_alerts_.*"} > 0` returns two distinct time series in response:

```
{__name__="vmalert_alerts_pending",job="vmalert",alertname="HostContextSwitching"} 12
{__name__="vmalert_alerts_firing",job="vmalert",alertname="HostContextSwitching"} 0
```

As label `__name__` will be dropped during evaluation, leads to duplicated time series.
To fix this, use [label_replace](https://docs.victoriametrics.com/victoriametrics/metricsql/#label_replace) to preserve the distinct labelset.


## mTLS protection

By default `vmalert` accepts http requests at `8880` port (this port can be changed via `-httpListenAddr` command-line flags),
since it is expected it runs in an isolated trusted network.
[Enterprise version of vmagent](https://docs.victoriametrics.com/victoriametrics/enterprise/) supports the ability to accept [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication)
requests at this port, by specifying `-tls` and `-mtls` command-line flags. For example, the following command runs `vmalert`, which accepts only mTLS requests at port `8880`:

```sh
./vmalert -tls -mtls -remoteWrite.url=...
```

By default system-wide [TLS Root CA](https://en.wikipedia.org/wiki/Root_certificate) is used for verifying client certificates if `-mtls` command-line flag is specified.
It is possible to specify custom TLS Root CA via `-mtlsCAFile` command-line flag.


## Security

See general recommendations regarding [security](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#security).

vmalert [web UI](https://docs.victoriametrics.com/victoriametrics/vmalert/#web), logs, and exported metrics contain details such as [group](https://docs.victoriametrics.com/victoriametrics/vmalert/#groups) configurations, active alerts,
[alerts state](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerts-state-on-restarts), [notifiers configuration](https://docs.victoriametrics.com/victoriametrics/vmalert/#notifier-configuration-file). Consider limiting user's access
to them if this information is sensitive.
Specifically:
* Log messages, the UI, and exported metrics contain full path to the configured rule files. These file paths can be stripped 
  by enabling `-rule.stripFilePath` command-line flag {{% available_from "v1.143.0" %}};
* Datasource address is sanitized in log messages, UI and exported metrics, can be shown by enabling ` -datasource.showURL`;
* Notifier addresses are sanitized in log messages, UI and exported metrics, can be shown by enabling `-notifier.showURL`;
* Remote read address is sanitized in log messages, UI and exported metrics, can be shown by enabling ` --remoteRead.showURL`;
* Remote write address is sanitized in log messages, UI and exported metrics, can be shown by enabling ` -remoteWrite.showURL`.

[Alerts state](#alerts-state-on-restarts) page or [debug mode](#debug-mode) could emit additional information about configured
datasource URL, GET params and headers. Sensitive information such as passwords or auth tokens is stripped by default.
To disable stripping of such info pass `-datasource.showURL` cmd-line flag to vmalert.

See also [mTLS protection docs](#mtls-protection).


## Profiling

`vmalert` provides handlers for collecting the following [Go profiles](https://blog.golang.org/profiling-go-programs):

* Memory profile. It can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8880/debug/pprof/heap > mem.pprof
```

* CPU profile. It can be collected with the following command (replace `0.0.0.0` with hostname if needed):

```sh
curl http://0.0.0.0:8880/debug/pprof/profile > cpu.pprof
```

The command for collecting CPU profile waits for 30 seconds before returning.

The collected profiles may be analyzed with [go tool pprof](https://github.com/google/pprof).
It is safe sharing the collected profiles from security point of view, since they do not contain sensitive information.
