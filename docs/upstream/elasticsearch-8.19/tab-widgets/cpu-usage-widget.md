<!-- Converted from tab-widgets/cpu-usage-widget.asciidoc (AsciiDoc). Includes are inlined. -->

* (Recommended) Enable {cloud}/ec-monitoring-setup.html[logs and metrics]. When logs and metrics are enabled, monitoring information is visible on Kibana's [Stack Monitoring](https://www.elastic.co/guide/en/kibana/8.19/xpack-monitoring.html) page. 
You can also enable the [CPU usage threshold alert](https://www.elastic.co/guide/en/kibana/8.19/kibana-alerts.html) to be notified about potential issues through email.

* From your deployment menu, view the {cloud}/ec-saas-metrics-accessing.html[**Performance**] page. On this page, you can view two key metrics:
** **CPU usage**: Your deployment's CPU usage, represented as a percentage.
** **CPU credits**: Your remaining CPU credits, measured in seconds of CPU time.

Elasticsearch Service grants {cloud}/ec-vcpu-boost-instance.html[CPU credits] per deployment
to provide smaller clusters with performance boosts when needed. High CPU
usage can deplete these credits, which might lead to {cloud}/ec-scenario_why_is_performance_degrading_over_time.html[performance degradation] and {cloud}/ec-scenario_why_are_my_cluster_response_times_suddenly_so_much_worse.html[increased cluster response times].

* Enable Elasticsearch monitoring. When logs and metrics are enabled, monitoring information is visible on Kibana's [Stack Monitoring](https://www.elastic.co/guide/en/kibana/8.19/xpack-monitoring.html) page.
You can also enable the [CPU usage threshold alert](https://www.elastic.co/guide/en/kibana/8.19/kibana-alerts.html) to be notified about potential issues through email.
