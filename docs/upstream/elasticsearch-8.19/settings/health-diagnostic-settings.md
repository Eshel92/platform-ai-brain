<!-- Converted from settings/health-diagnostic-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Health diagnostic settings in Elasticsearch

The following are the _expert-level_ settings available for configuring an internal diagnostics service.
The output of this service is currently exposed through the Health API Health API. It
is not recommended to change any of these from their default values.

#### Cluster level settings

`health.master_history.has_master_lookup_timeframe`::
(Static) The amount of time a node looks back to see if it has observed
a master at all, before moving on with other checks. Defaults to `30s` (30 seconds).

`master_history.max_age`::
(Static) The timeframe we record the master history
to be used for diagnosing the cluster health. Master node changes older than this time will not be considered when
diagnosing the cluster health. Defaults to `30m` (30 minutes).

`health.master_history.identity_changes_threshold`::
(Static) The number of master identity changes witnessed by a node that indicates the cluster is not healthy.
Defaults to `4`.

`health.master_history.no_master_transitions_threshold`::
(Static) The number of transitions to no master witnessed by a node that indicates the cluster is not healthy.
Defaults to `4`.

`health.node.enabled`::
(Dynamic) Enables the health node, which allows the health API to provide indications about
cluster wide health aspects such as disk space.

`health.reporting.local.monitor.interval`::
(Dynamic) Determines the interval in which each node of the cluster monitors aspects that
comprise its local health such as its disk usage.

`health.ilm.max_time_on_action`::
(Dynamic) The minimum amount of time an index has to be in an index lifecycle management (ILM) action before it is considered stagnant. Defaults to `1d` (1 day).

`health.ilm.max_time_on_step`::
(Dynamic) The minimum amount of time an index has to be in an ILM step before it is considered stagnant. Defaults to `1d` (1 day).

`health.ilm.max_retries_per_step`::
(Dynamic) The minimum amount of times an index has retried by an ILM step before it is considered stagnant. Defaults to `100`

`health.periodic_logger.enabled`::
(Dynamic) Enables the health periodic logger, which logs the health statuses of each health indicator along with the top level one as observed by the Health API.
Defaults to `false`.

`health.periodic_logger.poll_interval`::
(Dynamic, time unit value) How often Elasticsearch logs the health status of the cluster and of each health indicator as observed by the Health API.
Defaults to `60s` (60 seconds).
