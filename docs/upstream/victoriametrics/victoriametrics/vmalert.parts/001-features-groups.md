<!-- Part 1 of 6 of victoriametrics/vmalert.md (split because the page is big). -->

## Features

* Integration with VictoriaMetrics, VictoriaLogs, VictoriaTraces, Graphite and Prometheus compatible storages. See [Integrations](https://docs.victoriametrics.com/victoriametrics/vmalert/#integrations) for details;
* Prometheus [alerting rules definition format](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/#defining-alerting-rules)
  support;
* Integration with [Alertmanager](https://github.com/prometheus/alertmanager) starting from [Alertmanager v0.16.0-alpha](https://github.com/prometheus/alertmanager/releases/tag/v0.16.0-alpha.0);
* Keeps the alerts [state on restarts](#alerts-state-on-restarts);
* Graphite datasource can be used for alerting and recording rules. See [these docs](#graphite);
* Recording and Alerting rules backfilling (aka `replay`). See [these docs](#rules-backfilling);
* Lightweight and without extra dependencies.
* Supports [reusable templates](#reusable-templates) for annotations;
* Load of recording and alerting rules from local filesystem, URL, GCS and S3;
* Detect alerting rules which [don't match any series](https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4039).


## Limitations

* `vmalert` execute queries against remote datasource which has reliability risks because of the network.
  It is recommended to configure alerts thresholds and rules expressions with the understanding that network
  requests may fail;
* `vmalert` executes rules within a group sequentially, but persistence of execution results to remote
  storage is asynchronous. Hence, user shouldn't rely on chaining of recording rules when result of previous
  recording rule is reused in the next one. See how to [chain groups](https://docs.victoriametrics.com/victoriametrics/vmalert/#chaining-groups).


## QuickStart

To start using `vmalert` you will need the following things:

* list of rules - PromQL/MetricsQL/LogsQL/GraphiteQL expressions to execute;
* datasource address - a storage that [vmalert integrates with](https://docs.victoriametrics.com/victoriametrics/vmalert/#integrations) for executing queries;
* notifier address [optional] - reachable [Alert Manager](https://github.com/prometheus/alertmanager) instance for processing,
  aggregating alerts, and sending notifications. Please note, notifier address also supports Consul and DNS Service Discovery via
  [config file](https://docs.victoriametrics.com/victoriametrics/vmalert/#notifier-configuration-file).
* remote write address [optional] - [remote write](https://docs.victoriametrics.com/victoriametrics/vmagent/#victoriametrics-remote-write-protocol)
  compatible storage to persist rules and alerts state info. To persist results to multiple destinations use vmagent
  configured with multiple remote writes as a proxy;
* remote read address [optional] - Prometheus querying API compatible datasource to restore alerts state from.

You can use the existing [docker-compose environment](https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/deployment/docker#victoriametrics-single-server)
as an example. It already contains vmalert configured with the list of alerting rules and integrated with Alert Manager and VictoriaMetrics.

Alternatively, build `vmalert` from sources:

```sh
git clone https://github.com/VictoriaMetrics/VictoriaMetrics
cd VictoriaMetrics
make vmalert
```

Then run `vmalert`:

```sh
./bin/vmalert -rule=alert.rules \            # Path to the file with rules configuration. Supports wildcard and HTTP URL (S3/GCS are available in Enterprise).
    -datasource.url=http://localhost:8428 \  # VictoriaMetrics URL to query for rules evaluation. See other available Integrations above.
    -notifier.url=http://localhost:9093 \    # AlertManager URL (required if alerting rules are used)
    -notifier.url=http://127.0.0.1:9093 \    # AlertManager replica URL
    -remoteWrite.url=http://localhost:8428 \ # Remote write compatible storage to persist rules and alerts state info (required if recording rules are used)
    -remoteRead.url=http://localhost:8428 \  # Prometheus querying API compatible datasource to restore alerts state from
    -external.label=cluster=east-1 \         # External label to be applied for each rule
    -external.label=replica=a                # Multiple external labels may be set
```

> _To validate the syntax of configured rules simply run vmalert with `-rule` and `-dryRun` cmd-line flags._

Note there's a separate `-remoteWrite.url` command-line flag to allow writing results of
alerting/recording rules into a different storage than the initial data that's
queried. This allows using `vmalert` to aggregate data from a short-term,
high-frequency, high-cardinality storage into a long-term storage with
decreased cardinality and a bigger interval between samples.
See also [stream aggregation](https://docs.victoriametrics.com/victoriametrics/stream-aggregation/).

See the full list of configuration flags in [configuration](#configuration) section.

If you run multiple `vmalert` services for the same datasource or AlertManager and need to distinguish the results or alerts, 
specify different `-external.label` command-line flags to indicate which `vmalert` generated them. 
If rule result metrics have label that conflict with `-external.label`, `vmalert` will automatically rename
it with prefix `exported_`.

Configuration for [recording](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)
and [alerting](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) rules is very
similar to Prometheus rules and configured using YAML. Configuration examples may be found
in [testdata](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/app/vmalert/config/testdata) folder.

Every `rule` belongs to a `group` and every configuration file may contain arbitrary number of groups:

```yaml
groups:
  [ - <rule_group> ]
```


## Groups

Each group has the following attributes:

```yaml
# The name of the group. Must be unique within a file.
name: <string>

# How often rules in the group are evaluated.
[ interval: <duration> | default = -evaluationInterval flag ]

# Optional
# Group will be evaluated at the exact offset in the range of [0...interval].
# E.g. for Group with `interval: 1h` and `eval_offset: 5m` the evaluation will
# start at 5th minute of the hour.
# `eval_offset` also supports negative values, which means the evaluation will start at `interval-abs(eval_offset)` within [0...interval],
# For example, `eval_offset: -6m` is equivalent to `eval_offset: 4m` for `interval: 10m`.
# `interval` must be specified if `eval_offset` is used, and the `abs(eval_offset)` cannot exceed `interval`.
# `eval_offset` cannot be used with `eval_delay`, as group will be executed at the exact offset and `eval_delay` is ignored.
[ eval_offset: <duration> ]

# Optional
# Adjust the `time` parameter of group evaluation requests to compensate intentional query delay from the datasource.
# By default, the value is inherited from the `-rule.evalDelay` cmd-line flag - see its description for details.
# If group has `latency_offset` set in `params`, then it is recommended to set `eval_delay` equal to `latency_offset`.
# See https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5155 and https://docs.victoriametrics.com/victoriametrics/keyconcepts/#query-latency.
[ eval_delay: <duration> ]

# Limit limits the number of alerts or recording results a single rule within this group can produce.
# If exceeded, the rule will be marked with an error and all its results will be discarded.
# 0 means no limit.
[ limit: <integer> | default = -rule.resultsLimit flag]

# How many rules execute at once within a group. Increasing concurrency may speed
# up group's evaluation duration (exposed via `vmalert_iteration_duration_seconds` metric).
[ concurrency: <integer> | default = 1 ]

# Optional type for expressions inside rules to override the `-rule.defaultRuleType(default is "prometheus")` cmd-line flag.
# Supported values: "graphite", "prometheus" and "vlogs"(check https://docs.victoriametrics.com/victorialogs/vmalert/ for details).
[ type: <string> ]

# Optional
# The evaluation timestamp will be aligned with group's interval,
# instead of using the actual timestamp that evaluation happens at.
#
# It is enabled by default to get more predictable results
# and to visually align with graphs plotted via Grafana or vmui.
# When comparing with raw queries, remember to use `step` equal to evaluation interval.
#
# See https://github.com/VictoriaMetrics/VictoriaMetrics/issues/5049
# Available starting from v1.95
[ eval_alignment: <bool> | default true]

# Optional list of HTTP URL parameters
# applied for all rules requests within a group
# For example:
#  params:
#    nocache: ["1"]                # disable caching for vmselect
#    denyPartialResponse: ["true"] # fail if one or more vmstorage nodes returned an error
#    extra_label: ["env=dev"]      # apply additional label filter "env=dev" for all requests
# see more details at https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#prometheus-querying-api-enhancements
params:
  [ <string>: [<string>, ...]]

# Optional list of HTTP headers in form `header-name: value`
# applied for all rules requests within a group
# For example:
#  headers:
#    - "CustomHeader: foo"
#    - "CustomHeader2: bar"
# Headers set via this param have priority over headers set via `-datasource.headers` flag.
headers:
  [ <string>, ...]

# Optional list of HTTP headers in form `header-name: value`
# applied for all alert notifications sent to notifiers
# generated by rules of this group.
# It has higher priority over headers defined in notifier config.
# For example:
#  notifier_headers:
#    - "TenantID: foo"
notifier_headers:
  [ <string>, ...]

# Optional list of labels added to every rule within a group.
# It has priority over the external labels.
# Labels are commonly used for adding environment
# or tenant-specific tag.
labels:
  [ <labelname>: <labelvalue> ... ]

rules:
  [ - <rule> ... ]

# Enable debug mode for all rules in the group.
# This can be overridden by the `debug` field in rule.
[ debug: <bool> | default = false ]
```

### Rules

Every rule contains an `expr` field for the expression to evaluate against the configured datasource.
Depending on `group.type` value or `-rule.defaultRuleType` cmd-line flag expression can be one of the following types:
- `prometheus` (default) - [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) or [MetricsQL](https://docs.victoriametrics.com/victoriametrics/metricsql/) expression.
- `vlogs` - [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/vmalert/) expression.
- `graphite` - [Graphite](https://graphite.readthedocs.io/en/stable/render_api.html) expression.

There are two types of Rules:

* [Alerting](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerting-rules) -
  Alerting rules allow defining alert conditions via `expr` field and to send notifications to
  [Alertmanager](https://github.com/prometheus/alertmanager) if execution result is not empty ([Prometheus alerting rules docs](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules)).
* [Recording](https://docs.victoriametrics.com/victoriametrics/vmalert/#recording-rules) -
  Recording rules allow defining `expr` which result will be then backfilled to configured
  `-remoteWrite.url`. Recording rules are used to precompute frequently needed or computationally
  expensive expressions and save their result as a new set of time series ([Prometheus recording rules docs](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/)).

> `vmalert` forbids defining duplicates - rules with the same combination of name, expression and labels within one group.

#### Alerting rules

The syntax for alerting rule is the following:

```yaml
# The name of the alert. Must be a valid metric name.
alert: <string>

# The expression to evaluate. The expression language depends on the type value.
# By default, PromQL/MetricsQL expression is used. Other available types are "graphite" and "vlogs".
# See https://docs.victoriametrics.com/victoriametrics/vmalert/#integrations
expr: <string>

# Alerts are considered firing once they have been returned for this long.
# Alerts which have not yet been fired for long enough are considered pending.
# If param is omitted or set to 0 then alerts will be immediately considered
# as firing once they return.
[ for: <duration> | default = 0s ]

# Alert will continue firing for this long even when the alerting expression no longer has results.
# This allows you to delay alert resolution.
[ keep_firing_for: <duration> | default = 0s ]

# Whether to print debug information into logs.
# Information includes alerts state changes and requests sent to the datasource.
# Please note, that if rule's query params contain sensitive
# information - it will be printed to logs.
# Logs are printed with INFO level, so make sure that -loggerLevel=INFO to see the output.
[ debug: <bool> | default = false ]

# Defines the number of rule's updates entries stored in memory
# and available for view on rule's Details page.
# Overrides `rule.updateEntriesLimit` value for this specific rule.
# Available starting from https://docs.victoriametrics.com/victoriametrics/changelog/#v1860
[ update_entries_limit: <integer> | default 0 ]

# Labels to add or overwrite labels from other external label sources, such as group labels, for each alert.
# Labels are merged with labels received from `expr` evaluation and uniquely identify each generated alert.
#
# In case of conflicts, original labels are kept with prefix `exported_`.
# As a special case, specifying a label with an empty string value removes the label from the result if it exists 
# in the original query result; otherwise, it is ignored.
#
# Labels only support limited templating variables in https://docs.victoriametrics.com/victoriametrics/vmalert/#templating,
# including `$labels`, `$value` and `$expr`, to avoid breaking alert states or causing cardinality issue with results.
# Note: be careful set dynamic label values like `$value`, because each time the $value changes - the new alert will be
# generated which also break `for` condition.
labels:
  [ <labelname>: <tmpl_string> ]

# Annotations to add to each generated alert.
# Annotations could contain arbitrary dynamically generated data or templates - see https://docs.victoriametrics.com/victoriametrics/vmalert/#templating
annotations:
  [ <labelname>: <tmpl_string> ]
```

#### Recording rules

The syntax for recording rules is the following:

```yaml
# The name of the time series to output to. Must be a valid metric name.
record: <string>

# The expression to evaluate. The expression language depends on the type value.
# By default, PromQL/MetricsQL expression is used. Other available types are "graphite" and "vlogs".
# See https://docs.victoriametrics.com/victoriametrics/vmalert/#integrations
expr: <string>

# Labels to add or overwrite labels from other external label sources, such as group labels, before storing the result.
#
# In case of conflicts, original labels are kept with prefix `exported_`.
# As a special case, specifying a label with an empty string value removes the label from the result if it exists 
# in the original query result; otherwise, it is ignored.
#
# Labels do not support templating in https://docs.victoriametrics.com/victoriametrics/vmalert/#templating due to cardinality concerns. See https://github.com/VictoriaMetrics/VictoriaMetrics/issues/8171.
labels:
  [ <labelname>: <labelvalue> ]

# Whether to print debug information into logs.
# Information includes requests sent to the datasource.
# information - it will be printed to logs.
# Logs are printed with INFO level, so make sure that -loggerLevel=INFO to see the output.
[ debug: <bool> | default = false ]

# Defines the number of rule updates entries stored in memory
# and available for view on rule Details page.
# Overrides `rule.updateEntriesLimit` value for this specific rule.
[ update_entries_limit: <integer> | default 0 ]
```

For recording rules to work `-remoteWrite.url` must be specified.
