<!-- Converted from setup.asciidoc (AsciiDoc). Includes are inlined. -->

# Set up Elasticsearch

This section includes information on how to setup Elasticsearch and get it
running, including:

* Downloading
* Installing
* Starting
* Configuring

## Supported platforms

The matrix of officially supported operating systems and JVMs is available here:
link:/support/matrix[Support Matrix]. Elasticsearch is tested on the listed
platforms, but it is possible that it will work on other platforms too.

## Use dedicated hosts

In production, we recommend you run Elasticsearch on a dedicated host or as a primary
service. Several Elasticsearch features, such as automatic JVM heap sizing, assume it's
the only resource-intensive application on the host or container. For example,
you might run {metricbeat} alongside Elasticsearch for cluster statistics, but a
resource-heavy Logstash deployment should be on its own host.

(See `run-elasticsearch-locally.md`)
(See `setup/install.md`)
(See `setup/configuration.md`)
(See `setup/important-settings.md`)
(See `setup/secure-settings.md`)
(See `settings/audit-settings.md`)
(See `modules/indices/circuit_breaker.md`)
(See `modules/cluster.md`)
(See `settings/ccr-settings.md`)
(See `modules/discovery/discovery-settings.md`)
(See `settings/data-stream-lifecycle-settings.md`)
(See `modules/indices/fielddata.md`)
(See `modules/gateway.md`)
(See `settings/health-diagnostic-settings.md`)
(See `settings/ilm-settings.md`)
(See `modules/indices/index_management.md`)
(See `modules/indices/recovery.md`)
(See `modules/indices/indexing_buffer.md`)
(See `settings/inference-settings.md`)
(See `settings/license-settings.md`)
(See `settings/ml-settings.md`)
(See `settings/monitoring-settings.md`)
(See `modules/node.md`)
(See `modules/network.md`)
(See `modules/indices/query_cache.md`)
(See `path-settings-overview.md`)
(See `modules/indices/search-settings.md`)
(See `settings/security-settings.md`)
(See `modules/indices/request_cache.md`)
(See `settings/snapshot-settings.md`)
(See `settings/transform-settings.md`)
(See `modules/threadpool.md`)
(See `settings/notification-settings.md`)
(See `setup/advanced-configuration.md`)
(See `setup/sysconfig.md`)
(See `setup/bootstrap-checks.md`)
(See `setup/bootstrap-checks-xes.md`)
(See `setup/starting.md`)
(See `setup/stopping.md`)
(See `modules/discovery.md`)
(See `setup/add-nodes.md`)
(See `setup/restart-cluster.md`)
(See `modules/remote-clusters.md`)
(See `modules/plugins.md`)
