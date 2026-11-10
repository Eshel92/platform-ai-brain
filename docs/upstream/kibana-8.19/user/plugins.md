<!-- Converted from user/plugins.asciidoc (AsciiDoc). Includes are inlined. -->

# Kibana plugins

Implement add-on functionality for Kibana with plug-in modules.

**Plugin compatibility**
==============================================

The Kibana plugin interfaces are in a state of constant development.  We cannot provide backwards compatibility for plugins due to the high rate of change.  Kibana enforces that the installed plugins match the version of Kibana.  
Plugin developers must release a new version of their plugin for each new Kibana release.

==============================================

## Known plugins

The known plugins were tested for Kibana *5.x*, so we are unable to guarantee compatibility with your version of Kibana. The Kibana installer rejects any plugins that haven't been published for your specific version of Kibana. 

**Important:** Known plugins are developed and maintained outside of Elastic. They are not supported by Elastic. If you encounter an issue with a community plugin, contact the plugin's owner.

### Apps

* [LogTrail](https://github.com/sivasamyk/logtrail) - View, analyze, search and tail log events in realtime with a developer/sysadmin friendly interface
* [Own Home](https://github.com/wtakase/kibana-own-home) (wtakase) - enables multi-tenancy
* [Shard Allocation](https://github.com/asileon/kibana_shard_allocation) (asileon) - visualize elasticsearch shard allocation
* [Wazuh](https://github.com/wazuh/wazuh-kibana-app) - Wazuh provides host-based security visibility using lightweight multi-platform agents.
* [Indices View](https://github.com/TrumanDu/indices_view) - View indices related information.
* [Analyze UI](https://github.com/johtani/analyze-api-ui-plugin) (johtani) - UI for elasticsearch _analyze API
* [Cleaner](https://github.com/TrumanDu/cleaner) (TrumanDu)- Setting index ttl.
* [ElastAlert Kibana Plugin](https://github.com/bitsensor/elastalert-kibana-plugin) (BitSensor) - UI to create, test and edit ElastAlert rules
* [AI Analyst](https://github.com/query-ai/queryai-kibana-plugin) (Query.AI) - App providing: NLP queries, automation, ML visualizations and insights

### Timelion Extensions

* [mathlion](https://github.com/fermiumlabs/mathlion) (fermiumlabs) - enables equation parsing and advanced math under Timelion

### Visualizations

* [3D Charts](https://github.com/virusu/3D_kibana_charts_vis) (virusu)
* [3D Graph](https://github.com/JuanCarniglia/area3d_vis) (JuanCarniglia)
* [Bmap](https://github.com/TrumanDu/bmap)(TrumanDu) - integrated echarts for map visualization
* [C3JS Visualizations](https://github.com/mstoyano/kbn_c3js_vis) (mstoyano)
* [Calendar Visualization](https://github.com/aaronoah/kibana_calendar_vis) (aaronoah)
* [Cohort analysis](https://github.com/elo7/cohort) (elo7)
* [Colored Metric Visualization](https://github.com/DeanF/health_metric_vis) (deanf)
* [Dendrogram](https://github.com/JuanCarniglia/dendrogram_vis) (JuanCarniglia)
* [Dotplot](https://github.com/dlumbrer/kbn_dotplot) (dlumbrer)
* [Dropdown](https://github.com/AnnaGerber/kibana_dropdown) (AnnaGerber)
* [Enhanced Table](https://github.com/fbaligand/kibana-enhanced-table) (fbaligand)
* [Enhanced Tilemap](https://github.com/nreese/enhanced_tilemap) (nreese)
* [Extended Metric](https://github.com/ommsolutions/kibana_ext_metrics_vis) (ommsolutions)
* [Flexmonster Pivot Table & Charts](https://github.com/flexmonster/pivot-kibana) - a customizable pivot table component for advanced data analysis and reporting.
* [Funnel Visualization](https://github.com/outbrain/ob-kb-funnel) (roybass)
* [Gauge](https://github.com/sbeyn/kibana-plugin-gauge-sg) (sbeyn)
* [Health Metric](https://github.com/clamarque/Kibana_health_metric_vis) (clamarque)
* [Insight](https://github.com/tshoeb/Insight) (tshoeb) - Multidimensional data exploration
* [Line](https://github.com/sbeyn/kibana-plugin-line-sg) (sbeyn)
* [Milestones](https://github.com/walterra/kibana-milestones-vis) (walterra)
* [Navigation](https://github.com/varundbest/navigation) (varundbest)
* [Network Plugin](https://github.com/dlumbrer/kbn_network) (dlumbrer)
* [Percent](https://github.com/amannocci/kibana-plugin-metric-percent) (amannocci)
* [Polar](https://github.com/dlumbrer/kbn_polar) (dlumbrer)
* [Radar](https://github.com/dlumbrer/kbn_radar) (dlumbrer)
* [Search-Tables](https://github.com/dlumbrer/kbn_searchtables) (dlumbrer)
* [Status Light](https://github.com/Smeds/status_light_visualization) (smeds)
* [Swimlanes](https://github.com/prelert/kibana-swimlane-vis) (prelert)
* [Traffic](https://github.com/sbeyn/kibana-plugin-traffic-sg) (sbeyn)
* [Transform Visualization](https://github.com/PhaedrusTheGreek/transform_vis) (PhaedrusTheGreek)
* [Vega-based visualizations](https://github.com/nyurik/kibana-vega-vis) (nyurik) - Support for user-defined graphs, external data sources, maps, images, and user-defined interactivity.
* [VR Graph Visualizations](https://github.com/Camichan/kbn_aframe) (Camichan)
* [Sankey-Visualization](https://github.com/uniberg/kbn_sankey_vis) (uniberg)

### Other

* [Time filter as a dashboard panel](https://github.com/nreese/kibana-time-plugin) Widget to view and edit the time range from within dashboards.

* [Kibana-API](https://github.com/Webiks/kibana-API.git) (webiks) Exposes an API with Kibana functionality.
Use it to create, edit and embed visualizations, and also to search inside an embedded dashboard.

* [Markdown Doc View](https://github.com/sw-jung/kibana_markdown_doc_view) (sw-jung) - A plugin for custom doc view using markdown+handlebars template.
* [Datasweet Formula](https://github.com/datasweet-fr/kibana-datasweet-formula) (datasweet) - enables calculated metric on any standard Kibana visualization.

**Note:** To add your plugin to this page, open a {kib-repo}tree/{branch}/docs/plugins/known-plugins.asciidoc[pull request].

## Install plugins

Use the following command to install a plugin:

bin/kibana-plugin install <package name or URL>

When you specify a plugin name without a URL, the plugin tool attempts to download an official Elastic plugin, such as:

$ bin/kibana-plugin install x-pack

### Install plugins from an arbitrary URL

You can download official Elastic plugins simply by specifying their name. You
can alternatively specify a URL or file path to a specific plugin, as in the following
examples:

$ bin/kibana-plugin install https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-{version}.zip

or

$ bin/kibana-plugin install file:///local/path/to/custom_plugin.zip

You can specify URLs that use the HTTP, HTTPS, or `file` protocols.

### Proxy support for plugin installation

Kibana supports plugin installation via a proxy. It uses the `http_proxy` and `https_proxy`
environment variables to detect a proxy for HTTP and HTTPS URLs.

It also respects the `no_proxy` environment variable to exclude specific URLs from proxying.

You can specify the environment variable directly when installing plugins:

$ http_proxy="<PROXY_URL>.local:4242" bin/kibana-plugin install <package name or URL>

## Update and remove plugins

To update a plugin, remove the current version and reinstall the plugin.

To remove a plugin, use the `remove` command, as in the following example:

$ bin/kibana-plugin remove x-pack

You can also remove a plugin manually by deleting the plugin's subdirectory under the `plugins/` directory.

**Note:** Removing a plugin will result in an "optimize" run which will delay the next start of Kibana.

## Configure the plugin manager

By default, the plugin manager provides you with feedback on the status of the activity you've asked the plugin manager
to perform. You can control the level of feedback for the `install` and `remove` commands with the `--quiet` and
`--silent` options. Use the `--quiet` option to suppress all non-error output. Use the `--silent` option to suppress all
output.

By default, plugin manager installation requests do not time out. Use the `--timeout` option, followed by a time, to
change this behavior, as in the following examples:

**Waits for 30 seconds before failing**
bin/kibana-plugin install --timeout 30s sample-plugin

**Waits for 1 minute before failing**
bin/kibana-plugin install --timeout 1m sample-plugin

### Plugins and custom Kibana configurations

Use the `-c` or `--config` options with the `install` and `remove` commands to specify the path to the configuration file
used to start Kibana. By default, Kibana uses the configuration file `config/kibana.yml`. When you change your installed
plugins, the `bin/kibana-plugin` command restarts the Kibana server. When you are using a customized configuration file,
you must specify the path to that configuration file each time you use the `bin/kibana-plugin` command.

### Plugin manager exit codes

0:: Success
64:: Unknown command or incorrect option parameter
74:: I/O error
70:: Other error
