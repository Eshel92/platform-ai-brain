<!-- Converted from view-sharded-cluster-metrics.txt (reStructuredText). Includes are inlined. -->

# View Sharded Clusters

A sharded cluster is the set of nodes 
comprising a sharded MongoDB deployment. To view the metrics for a 
specific Ops Manager deployment in a project, click the 
Metrics button for that deployment. Alternatively, click on 
the name of the deployment to open the deployment overview, then click 
the Metrics tab.

Monitor deployment metrics to identify performance issues and 
determine whether your current deployment meets your 
requirements. To learn more about the metrics available to monitor 
your deployments, see review-available-metrics.

The Metrics view has three distinct sections:

## Chart Controls

Ops Manager provides the following controls for the
Metric view:

| Control | Function |
|---|---|
| Granularity | .. include:: /includes/extracts/monitor-view-control-granularity-sharded.rst |
| Zoom | .. include:: /includes/extracts/monitor-view-control-zoom.rst |
| Display Data | .. include:: /includes/extracts/monitor-view-control-display-data.rst |
| Current Display | .. include:: /includes/extracts/monitor-view-control-current-display.rst |
| Display | .. include:: /includes/extracts/monitor-view-control-display.rst |
| View | .. include:: /includes/extracts/monitor-view-control-view.rst |

## Chart Display

When viewing charts, you can do the following:

| Task | Action |
|---|---|
| Zoom in on a period of time. | .. include:: /includes/extracts/monitor-chart-controls-zoom.rst |
| View statistics at a particular time. | .. include:: /includes/extracts/monitor-chart-controls-point.rst |

## Data Sources

Ops Manager displays each data source that contributes to the metric
chart in a table below the chart. The table consists of the
following:

| Column | Description |
|---|---|
| Shard Name | When View is set to `SHARDS`, displays the name of each shard in the sharded cluster deployment. When View is set to `MONGOS` or `CONFIGS`, displays the name of each mongos or config server mongod process in the sharded cluster deployment. Click on a listed component to open the Metrics view for that component. |
| Alerts | Indicates if there are any open alerts for the listed shard or process. Click on the alert icon to open the Alerts view for that shard or process. To learn more about responding to open alerts, see /tutorial/manage-alerts-and-events. |
| Data Size | Only visible if View is set to `SHARDS`. Indicates the logical size of all documents and indexes on the shard. |
| Show | Only visible if View is set to `SHARDS` Indicates which replica set members to show on the selected chart. Select `Primaries`, `Secondaries` or `All`. |
| Read, Write, and Queued | Metric data related to the displayed chart. Hover over the corresponding column for a pop up with detailed information on the metrics shown. |
