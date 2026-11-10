<!-- Converted from settings/logs-ui-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Logs settings in Kibana

You do not need to configure any settings to use the Logs app in Kibana. It is enabled by default.

The Kibana logs can be found per operating system under:

* Linux, DEB or RPM package: /var/log/kibana/kibana.log
* Linux, tar.gz package: $KIBANA_HOME/log/kibana.log
* Windows: $KIBANA_HOME\log\kibana.log

#### General Logs settings

deprecated:[8.18.0] `xpack.infra.sources.default.fields.message`::
Fields used to display messages in the Logs app. Defaults to `['message', '@message']`.

`xpack.infra.alerting.inventory_threshold.group_by_page_size`::
Controls the size of the composite aggregations used by the Inventory Threshold to retrieve all the hosts. Defaults to `10_000`.

`xpack.infra.alerting.metric_threshold.group_by_page_size`::
Controls the size of the composite aggregations used by the Metric Threshold group by feature. Defaults to `10_000`.
