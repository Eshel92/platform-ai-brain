<!-- Part 2 of 13 of victoriametrics/README.md (split because the page is big). -->

## vmui

VictoriaMetrics provides UI for query troubleshooting and exploration. The UI is available at `http://victoriametrics:8428/vmui`
(or at `http://<vmselect>:8481/select/<accountID>/vmui/` in [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/)).

> See [VMUI at VictoriaMetrics playground](https://play.victoriametrics.com?g0.expr=up).

VMUI provides the following features:

* `Query` tab for ad-hoc queries in MetricsQL, supporting time series, tables and histogram representation
* `Raw Query` tab {{% available_from "v1.107.0" %}} for viewing [raw samples](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#raw-samples). Helps in debugging of [unexpected query results](https://docs.victoriametrics.com/victoriametrics/troubleshooting/#unexpected-query-results).
* Explore:
  * [Metrics explorer](#metrics-explorer) - automatically builds graphs for selected metrics;
  * [Cardinality explorer](#cardinality-explorer) - stats about existing metrics in TSDB;
  * [Top queries](#top-queries) - shows most frequently executed queries;
  * [Active queries](#active-queries) - shows currently executed queries;
* Tools:
  * [Trace analyzer](#query-tracing) - explore query traces loaded from JSON;
  * [Query analyzer](#query-tracing) - explore query results and traces loaded from JSON. See `Export query` button below;
  * [WITH expressions playground](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/expand-with-exprs) - test how WITH expressions work;
  * [Metric relabel debugger](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/relabeling) - debug [relabeling](#relabeling) rules.
  * [Downsampling filters debugger](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/downsampling-filters-debug) {{% available_from "v1.105.0" %}} - debug [downsampling](#downsampling) configs.
  * [Retention filters debugger](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/retention-filters-debug) {{% available_from "v1.105.0" %}} - debug [retention filter](#retention-filters) configs.
* `Dashboards` tab for viewing [predefined dashboards](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmui/README.md#predefined-dashboards) - [See it in playground](https://play.victoriametrics.com/select/0/prometheus/graph/#/dashboards)
* `Alerting` {{% available_from "v1.125.0" %}} for displaying groups and rules from the [vmalert](https://docs.victoriametrics.com/victoriametrics/vmalert/) service.
  The tab is available only if [VictoriaMetrics single-node](https://docs.victoriametrics.com/victoriametrics/#vmalert) or
  [vmselect](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#vmalert) are configured with `-vmalert.proxyURL` command-line flag.

**Querying:**

Enter the MetricsQL query in `Query` field and hit `Enter`. Multi-line queries can be entered by pressing `Shift-Enter`.

VMUI provides auto-completion for [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/) functions, metric names, label names and label values.
The auto-completion can be enabled by checking the `Autocomplete` toggle. When the auto-completion is disabled, it can
still be triggered for the current cursor position by pressing `ctrl+space`.

To correlate between multiple queries on the same graph click `Add Query` button and enter an additional query.
Results for all the queries are displayed simultaneously on the same graph.

Results of a particular query can be hidden by clicking the `eye` icon on the right side of the input field.
Clicking on the `eye` icon while holding the `ctrl` key hides results of all other queries.

VMUI automatically adjusts the interval between datapoints on the graph depending on the horizontal resolution and on the selected time range.
The step value can be customized by changing `Step` value in the top-right corner.

Clicking on the line on graph pins the tooltip. User can pin multiple tooltips. Press `x` icon to unpin the tooltip.

Query history can be navigated by holding `Ctrl` (or `Cmd` on MacOS) and pressing `up` or `down` arrows on the keyboard while the cursor is located in the query input field.

VMUI automatically switches from graph view to heatmap view when the query returns [histogram](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#histogram) buckets
(both [Prometheus histograms](https://prometheus.io/docs/concepts/metric_types/#histogram)
and [VictoriaMetrics histograms](https://valyala.medium.com/improving-histogram-usability-for-prometheus-and-grafana-bc7e5df0e350) are supported).
Try, for example, [this query](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/?g0.expr=sum%28rate%28vm_promscrape_scrape_duration_seconds_bucket%29%29+by+%28vmrange%29&g0.range_input=24h&g0.end_input=2023-04-10T17%3A46%3A12&g0.relative_time=last_24_hours&g0.step_input=31m).
To disable heatmap view press on settings icon in the top-right corner of graph area and disable `Histogram mode` toggle.

**Time range:**

The time range for graphs can be adjusted in multiple ways:

* Click on time picker in the top-right corner to select a relative (`Last N minutes`) or absolute time range (specify `From` and `To`);
* Zoom-in into graph by click-and-drag motion over the graph area;
* When hovering cursor over the graph area, hold `ctrl` (or `cmd` on MacOS) and scroll up or down to zoom out or zoom in;
* When hovering cursor over the graph area, hold `ctrl` (or `cmd` on MacOS) and drag the graph to the left / right to move the displayed time range into the future / past.

**Legend:**

Legend is displayed below the graph area.
Clicking on item in legend hides all other items from displaying. Clicking on the item while holding the `ctrl` key hides
only this item.

Clicking on the label-value pair in item automatically copies it into buffer, so it can be pasted later.

There are additional visualization settings in the top right-corner of the legend view: switching to table view,
hiding common labels, etc.

**Troubleshooting:**

When querying the [backfilled data](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#backfilling)
or during [query troubleshooting](https://docs.victoriametrics.com/victoriametrics/troubleshooting/#unexpected-query-results),
it may be useful disabling response cache by clicking `Disable cache` checkbox.

Query can be [traced](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#query-tracing)
by clicking on `Trace query` toggle below query input area and executing query again. Once trace is generated, click
on it to expand for more details.

The query and its trace can be exported by clicking on `debug` icon in top right corner of trace block. The exported file
file can be loaded again in VMUI on `Tools=>Query Analyzer` page.

`Raw query` page allows displaying raw, unmodified data. It can be useful for seeing the actual scrape interval or detecting
sample duplicates.

### Top queries

[VMUI](#vmui) provides `top queries` tab, which can help determining the following query types:

* the most frequently executed queries;
* queries with the biggest average execution duration;
* queries that took the most summary time for execution;
* queries with the highest memory usage.

This information is obtained from the `/api/v1/status/top_queries` HTTP endpoint.

### Active queries

[VMUI](#vmui) provides `active queries` tab, which shows currently execute queries.
It provides the following information per each query:

* The query itself, together with the time range and step args passed to [/api/v1/query_range](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#range-query).
* The duration of the query execution.
* The client address, who initiated the query execution.

This information is obtained from the `/api/v1/status/active_queries` HTTP endpoint.

### Metrics explorer

[VMUI](#vmui) provides an ability to explore metrics exported by a particular `job` / `instance` in the following way:

1. Open the `vmui` at `http://victoriametrics:8428/vmui/`.
1. Click the `Explore Prometheus metrics` tab.
1. Select the `job` you want to explore.
1. Optionally select the `instance` for the selected job to explore.
1. Select metrics you want to explore and compare.

It is possible to change the selected time range for the graphs in the top right corner.

### Cardinality explorer

VictoriaMetrics provides an ability to explore [time series cardinality](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#cardinality)
at `Explore cardinality` tab in [vmui](#vmui):

* [Metric](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#what-is-a-metric) names with the highest number of series.
* [Labels](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#labels) with the highest number of series.
* Values with the highest number of series for the selected label (aka `focusLabel`).
* `label=name` pairs with the highest number of series.
* Labels with the highest number of unique values.
* Read usage statistics of metric names, based on [metric name usage tracker](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#track-ingested-metrics-usage).
  Shows the number of times the metric name was queried (`Requests count`), and the last time (`Last request`) when it was queried.

Note that [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/)
may show lower than expected number of unique label values for labels with small number of unique values.
This is because of [implementation limits](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/5a6e617b5e41c9170e7c562aecd15ee0c901d489/app/vmselect/netstorage/netstorage.go#L1039-L1045).

By default, cardinality explorer analyzes time series for the **current date**. It provides the ability to **select different day at the top right corner**.
By default, all the time series for the selected date are analyzed. To narrow down the analysis specify [series selector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors).

Cardinality explorer is built on top of [/api/v1/status/tsdb](#tsdb-stats).

Resources:

* [cardinality explorer playground](https://play.victoriametrics.com/select/accounting/1/6a716b0f-38bc-4856-90ce-448fd713e3fe/prometheus/graph/#/cardinality).
* [Cardinality explorer blog post](https://victoriametrics.com/blog/cardinality-explorer/).
* [skills/victoriametrics-cardinality-analysis](https://github.com/VictoriaMetrics/skills/blob/main/plugins/diagnostics/skills/victoriametrics-cardinality-analysis/SKILL.md) for [agent-assisted](https://docs.victoriametrics.com/ai-tools/#agent-skills) analysis.

For monitoring or alerting on cardinality, use [vmestimator](https://docs.victoriametrics.com/victoriametrics/vmestimator/).
vmestimator measures metrics cardinality across [arbitrary label dimensions](https://docs.victoriametrics.com/victoriametrics/vmestimator/#basic) in real time and exposes the [results as metrics](https://docs.victoriametrics.com/victoriametrics/vmestimator/#cardinality-metrics).

### Cardinality explorer statistic inaccuracy

In [cluster version of VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) each vmstorage tracks the stored time series individually.
vmselect requests stats via [/api/v1/status/tsdb](#tsdb-stats) API from each vmstorage node and merges the results by summing per-series stats.
This may lead to inflated values when samples for the same time series are spread across multiple vmstorage nodes
due to [replication](#replication) or [rerouting](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-availability).


## How to apply new config to VictoriaMetrics

VictoriaMetrics is configured via command-line flags, so it must be restarted when new command-line flags should be applied:

* Send `SIGINT` signal to VictoriaMetrics process in order to gracefully stop it.
* Wait until the process stops. This can take a few seconds.
* Start VictoriaMetrics with the new command-line flags.

Prometheus doesn't drop data during VictoriaMetrics restart. See [this article](https://grafana.com/blog/whats-new-in-prometheus-2-8-wal-based-remote-write/) for details. The same applies also to [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/).


## How to scrape Prometheus exporters such as [node-exporter](https://github.com/prometheus/node_exporter)

VictoriaMetrics can be used as drop-in replacement for Prometheus for scraping targets configured in `prometheus.yml` config file
according to [the specification](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file).
Just set `-promscrape.config` command-line flag to the path to `prometheus.yml` config - and VictoriaMetrics should start scraping the configured targets.
If the provided configuration file contains [unsupported options](https://docs.victoriametrics.com/victoriametrics/vmagent/#unsupported-prometheus-config-sections),
then either delete them from the file or just pass `-promscrape.config.strictParse=false` command-line flag to VictoriaMetrics, so it will ignore unsupported options.

The file pointed by `-promscrape.config` may contain `%{ENV_VAR}` placeholders, which are substituted by the corresponding `ENV_VAR` environment variable values.

See also:

* [scrape config examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/)
* [the list of supported service discovery types for Prometheus scrape targets](https://docs.victoriametrics.com/victoriametrics/sd_configs/)

VictoriaMetrics also supports [importing data in Prometheus exposition format](#how-to-import-data-in-prometheus-exposition-format).

See also [vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/), which can be used as drop-in replacement for Prometheus.
