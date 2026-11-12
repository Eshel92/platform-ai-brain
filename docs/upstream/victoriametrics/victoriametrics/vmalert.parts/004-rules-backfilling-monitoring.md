<!-- Part 4 of 6 of victoriametrics/vmalert.md (split because the page is big). -->

## Rules backfilling

vmalert supports alerting and recording rules backfilling (aka `replay`). In replay mode vmalert
can read the same rules configuration as normal, evaluate them on the given time range and backfill
results via remote write to the configured storage. vmalert supports only the `prometheus` datasource type for backfilling.

Please note, that response caching may lead to unexpected results during and after backfilling process.
In order to avoid this you need to reset cache contents or disable caching when using backfilling
as described in [backfilling docs](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#backfilling).

See a blogpost about [Rules backfilling via vmalert](https://victoriametrics.com/blog/rules-replay/).

### How it works

In `replay` mode vmalert works as a cli-tool and exits immediately after work is done.
To run vmalert in `replay` mode:

```sh
./bin/vmalert -rule=path/to/your.rules \        # path to files with rules you usually use with vmalert
    -datasource.url=http://localhost:8428 \     # Prometheus HTTP API compatible datasource
    -remoteWrite.url=http://localhost:8428 \    # remote write compatible storage to persist results
    -replay.timeFrom=2021-05-11T07:21:43Z \     # to start replay from
    -replay.timeTo=2021-05-29T18:40:43Z         # to finish replay by, optional. By default, set to the current time
```

The output of the command will look like the following:

```
Replay mode:
from:   2021-05-11 07:21:43 +0000 UTC   # set by -replay.timeFrom
to:     2021-05-29 18:40:43 +0000 UTC   # set by -replay.timeTo
max data points per request: 1000       # set by -replay.maxDatapointsPerQuery

Group "ReplayGroup"
interval:       1m0s
requests to make:       27
max range per request:  16h40m0s
> Rule "type:vm_cache_entries:rate5m" (ID: 1792509946081842725)
27 / 27 [----------------------------------------------------------------------------------------------------] 100.00% 78 p/s
> Rule "go_cgo_calls_count:rate5m" (ID: 17958425467471411582)
27 / 27 [-----------------------------------------------------------------------------------------------------] 100.00% ? p/s

Group "vmsingleReplay"
interval:       30s
requests to make:       54
max range per request:  8h20m0s
> Rule "RequestErrorsToAPI" (ID: 17645863024999990222)
54 / 54 [-----------------------------------------------------------------------------------------------------] 100.00% ? p/s
> Rule "TooManyLogs" (ID: 9042195394653477652)
54 / 54 [-----------------------------------------------------------------------------------------------------] 100.00% ? p/s
2021-06-07T09:59:12.098Z        info    app/vmalert/replay.go:68        replay finished! Imported 511734 samples
```

> In replay mode, groups are executed sequentially in the defined order. Within each group, rules are also executed sequentially,
regardless of the `concurrency` setting. This ensures that any potential chaining between rules is preserved (see `-replay.rulesDelay`).
If you want rules to run concurrently based on the `concurrency` setting, set `-replay.rulesDelay=0`.

vmalert sends rule's expression to [/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query) endpoint
of the configured `-datasource.url`. Returned data is then processed according to the rule type and
backfilled to `-remoteWrite.url` via [remote Write protocol](https://docs.victoriametrics.com/victoriametrics/vmagent/#victoriametrics-remote-write-protocol).
vmalert respects `evaluationInterval` value set by flag or per-group during the replay.
vmalert automatically disables caching on VictoriaMetrics side by sending `nocache=1` param. It allows
to prevent cache pollution and unwanted time range boundaries adjustment during backfilling.

Results of recording rules `replay` should match the results of normal rules evaluation.

Results of alerting rules `replay` are the time series reflecting the [state of the alert](#alerts-state-on-restarts).
To see if `replayed` alert has fired in the past use the following PromQL/MetricsQL expression:

```
ALERTS{alertname="your_alertname", alertstate="firing"}
```

Execute the query against storage which was used for `-remoteWrite.url` during the `replay`.

> Since alerting rule annotations are attached to alert messages sent to the notifier (such as Alertmanager), and vmalert does not send alert messages to notifier in replay mode, all rule annotations will be ignored.

### Additional configuration

There are following non-required `replay` flags:

* `-replay.maxDatapointsPerQuery` - the max number of data points expected to receive in one request.
  In two words, it affects the max time range for every `/query_range` request. The higher the value,
  the fewer requests will be issued during `replay`.
* `-replay.ruleRetryAttempts` - when datasource fails to respond vmalert will make this number of retries
  per rule before giving up.
* `-replay.rulesDelay` - delay between sequential rules execution. Important in cases if there are chaining
  (rules which depend on each other) rules. It is expected, that remote storage will be able to persist
  previously accepted data during the delay, so data will be available for the subsequent queries.
  Keep it equal or bigger than `-remoteWrite.flushInterval`. When set to `0`, allows executing rules within
  the group concurrently.
* `-replay.disableProgressBar` - whether to disable progress bar which shows progress work.
  Progress bar may generate a lot of log records, which is not formatted as standard VictoriaMetrics logger.
  It could break logs parsing by external system and generate additional load on it.
* `-replay.ruleEvaluationConcurrency` -  The maximum number of concurrent `/query_range` requests when replay recording rule or alerting rule with for=0.
  Increasing this value when replaying for a long time, since each request is limited by `-replay.maxDatapointsPerQuery`.
  The default value is `1`.

See full description for these flags in `./vmalert -help`.

### Limitations

* Graphite engine isn't supported yet;
* `query` template function is disabled for performance reasons (might be changed in future);
* `limit` group's param has no effect during replay (might be changed in future);
* `keep_firing_for` alerting rule param has no effect during replay (might be changed in future).


## Unit Testing for Rules

You can use `vmalert-tool` to test your alerting and recording rules like [promtool does](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/).
See more details in [vmalert-tool](https://docs.victoriametrics.com/victoriametrics/vmalert-tool/#unit-testing-for-rules).


## Monitoring

`vmalert` exports various metrics in Prometheus exposition format at `http://vmalert-host:8880/metrics` page.
See the [list of recommended alerting rules](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/deployment/docker/rules/alerts-vmalert.yml) to track the vmalert health.
We recommend setting up regular scraping of this page either through [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) or by Prometheus-compatible scraper,
so that the exported metrics may be analyzed later.

If you use Google Cloud Managed Prometheus for scraping metrics from VictoriaMetrics components, then pass `-metrics.exposeMetadata`
command-line to them, so they add `TYPE` and `HELP` comments per each exposed metric at `/metrics` page.
See [these docs](https://cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#missing-metric-type) for details.

Use the official [Grafana dashboard](https://grafana.com/grafana/dashboards/14950) for `vmalert` overview.
Graphs on this dashboard contain useful hints - hover the `i` icon in the top left corner of each graph in order to read it.
If you have suggestions for improvements or have found a bug - please open an issue on GitHub or add
a review to the dashboard.
