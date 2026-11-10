<!-- Converted from settings/monitoring-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Monitoring settings in Kibana

By default, *{stack-monitor-app}* is enabled, but data collection is disabled.
When you first start Kibana monitoring, you are prompted to enable data
collection. If you are using {stack-security-features}, you must be signed in as
a user with the `cluster:manage` privilege to enable data collection. The
built-in `superuser` role has this privilege and the built-in `elastic` user has
this role.

You can adjust how monitoring data is
collected from Kibana and displayed in Kibana by configuring settings in the
`kibana.yml` file. There are also `monitoring.ui.elasticsearch.*` settings,
which support the same values as Kibana configuration settings.

To control how data is collected from your Elasticsearch nodes, you configure
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitoring-settings.html[`xpack.monitoring.collection`
settings] in `elasticsearch.yml`. To control how monitoring data is collected
from Logstash, configure monitoring settings in `logstash.yml`.

For more information, see
[Monitor a cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitor-elasticsearch-cluster.html).

#### General monitoring settings

`monitoring.cluster_alerts.email_notifications.enabled`::
deprecated:[7.11.0] 
When enabled, sends email notifications for Watcher alerts to the specified email address. The default is `true`. 

`monitoring.cluster_alerts.email_notifications.email_address` ::
deprecated:[7.11.0] 
When enabled, specifies the email address where you want to receive cluster alert notifications.

`monitoring.ui.ccs.enabled`::
Set to `true` (default) to enable [cross-cluster search](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-cross-cluster-search.html) of your monitoring data. The [`remote_cluster_client`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-remote-clusters.html#remote-cluster-settings) role must exist on each node.

`monitoring.ui.elasticsearch.hosts`::
Specifies the location of the Elasticsearch cluster where your monitoring data is stored.
By default, this is the same as `elasticsearch.hosts`. This setting enables
you to use a single Kibana instance to search and visualize data in your
production cluster as well as monitor data sent to a dedicated monitoring
cluster.

`monitoring.ui.elasticsearch.username`::
Specifies the username used by Kibana monitoring to establish a persistent connection
in Kibana to the Elasticsearch monitoring cluster and to verify licensing status on the Elasticsearch
monitoring cluster when using `monitoring.ui.elasticsearch.hosts`.
All other requests performed by *{stack-monitor-app}* to the monitoring Elasticsearch
cluster uses the authenticated user's credentials, which must be the same on
both the Elasticsearch monitoring cluster and the Elasticsearch production cluster.
If not set, Kibana uses the value of the `elasticsearch.username` setting.

`monitoring.ui.elasticsearch.password`::
Specifies the password used by Kibana monitoring to establish a persistent connection
in Kibana  to the Elasticsearch monitoring cluster and to verify licensing status on the Elasticsearch
monitoring cluster when using `monitoring.ui.elasticsearch.hosts`.
All other requests performed by *{stack-monitor-app}* to the monitoring Elasticsearch
cluster use the authenticated user's credentials, which must be the same on
both the Elasticsearch monitoring cluster and the Elasticsearch production cluster.
If not set, Kibana uses the value of the `elasticsearch.password` setting.

`monitoring.ui.elasticsearch.serviceAccountToken`::
Specifies a [service account token](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api-create-service-token.html) for the Elasticsearch cluster where your monitoring data is stored when using `monitoring.ui.elasticsearch.hosts`.  This setting is an alternative to using `monitoring.ui.elasticsearch.username` and `monitoring.ui.elasticsearch.password`.

`monitoring.ui.elasticsearch.pingTimeout`::
Specifies the time in milliseconds to wait for Elasticsearch to respond to internal
health checks. By default, it matches the `elasticsearch.pingTimeout` setting,
which has a default value of `30000`.

`monitoring.ui.elasticsearch.ssl`::
Shares the same configuration as `elasticsearch.ssl`. These settings configure encrypted communication between Kibana and the monitoring cluster.

#### Monitoring collection settings

These settings control how data is collected from Kibana.

`monitoring.kibana.collection.enabled`::
Set to `true` (default) to enable data collection from the Kibana NodeJS server
for Kibana dashboards to be featured in *{stack-monitor-app}*.

`monitoring.kibana.collection.interval` ::
Specifies the number of milliseconds to wait in between data sampling on the
Kibana NodeJS server for the metrics that are displayed in the Kibana dashboards.
Defaults to `10000` (10 seconds).

#### Monitoring UI settings

These settings adjust how *{stack-monitor-app}* displays monitoring data.
However, the defaults work best in most circumstances. For more information
about configuring Kibana, see
[Setting Kibana server properties](https://www.elastic.co/guide/en/kibana/8.19/settings.html).

`monitoring.ui.elasticsearch.logFetchCount`::
Specifies the number of log entries to display in *{stack-monitor-app}*.
Defaults to `10`. The maximum value is `50`.

[[monitoring-ui-enabled]] `monitoring.ui.enabled`::
Set to `false` to hide *{stack-monitor-app}*. The monitoring back-end
continues to run as an agent for sending Kibana stats to the monitoring
cluster. Defaults to `true`.

`monitoring.ui.logs.index`::
Specifies the name of the indices that are shown on the
*Logs* page in *{stack-monitor-app}*. The default value
is `filebeat-*`.

`monitoring.ui.metricbeat.index`::
deprecated:[8.1.1]
Used as a workaround to avoid querying `metricbeat-*` indices which are now no longer queried. The default value
is `metricbeat-*`.

`monitoring.ui.max_bucket_size`::
Specifies the number of term buckets to return out of the overall terms list when
performing terms aggregations to retrieve index and node metrics. For more
information about the `size` parameter, see
[Terms Aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-aggregations-bucket-terms-aggregation.html#search-aggregations-bucket-terms-aggregation-size).
Defaults to `10000`.

`monitoring.ui.min_interval_seconds` ::
Specifies the minimum number of seconds that a time bucket in a chart can
represent. Defaults to 10. If you modify the
`monitoring.ui.collection.interval` in `elasticsearch.yml`, use the same
value in this setting.

`monitoring.ui.kibana.reporting.stale_status_threshold_seconds`::
Specifies how many seconds can pass before the Kibana status reports are considered stale.
Defaults to `120`.

##### Monitoring UI container settings

*{stack-monitor-app}* exposes the Cgroup statistics that we collect for you to make
better decisions about your container performance, rather than guessing based on
the overall machine performance. If you are not running your applications in a
container, then Cgroup statistics are not useful.

`monitoring.ui.container.elasticsearch.enabled` ::
For Elasticsearch clusters that are running in containers, this setting changes the
*Node Listing* to display the CPU utilization based on the reported Cgroup
statistics. It also adds the calculated Cgroup CPU utilization to the
*Node Overview* page instead of the overall operating system's CPU
utilization. Defaults to `false`.

`monitoring.ui.container.logstash.enabled`::
For Logstash nodes that are running in containers, this setting
changes the Logstash *Node Listing* to display the CPU utilization
based on the reported Cgroup statistics. It also adds the
calculated Cgroup CPU utilization to the Logstash node detail
pages instead of the overall operating system’s CPU utilization. Defaults to `false`.
