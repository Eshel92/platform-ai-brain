<!-- Converted from view-mongodb-process-metrics.txt (reStructuredText). Includes are inlined. -->

# View MongoDB Processes

To view the metrics for a specific MongoDB process in a
Ops Manager deployment, click on that process from the
Deployment view. The Ops Manager process view displays
three tabs for monitoring metrics for the process:

- The Status tab displays the process metrics Ops Manager
  collects from the selected mongod or
  mongos process.

- The Hardware tab displays hardware metrics for
  the host machine supporting the selected
  mongod or mongos
  process.

- The DB Stats tab displays the database metrics for the
  selected database.

Monitor deployment metrics to identify performance issues and 
determine whether your current deployment meets your 
requirements. To learn more about the metrics available to monitor 
your deployments, see review-available-metrics.

Ops Manager retrieves database metrics every 20 minutes by default but
adjusts frequency when necessary to reduce the impact on database
performance. If the collection of database statistics still affects
performance, you can disable collection by clicking
Settings from the left-hand navigation,
then Project Settings, and then setting
Collect Database Specific Statistics to No.

The view for each tab has three distinct sections:

## Chart Controls

Ops Manager provides the following controls for the Status,
Hardware, and DB Stats
views. Adjusting any of these options affects all charts displayed under
the selected view:

| Control | Function |
|---|---|
| Granularity | .. include:: /includes/extracts/monitor-view-control-granularity.rst |
| Zoom | .. include:: /includes/extracts/monitor-view-control-zoom.rst |
| Current Display | .. include:: /includes/extracts/monitor-view-control-current-display.rst |
| Add Chart | .. include:: /includes/extracts/monitor-view-control-add-chart.rst |
| Select Database | .. include:: /includes/extracts/monitor-view-control-select-database.rst |
| Display Opcounters on Separate Charts | .. include:: /includes/extracts/monitor-view-control-display-opcounters.rst |
| Display Timeline Annotations | .. include:: /includes/extracts/monitor-view-control-display-annotations.rst |

## Chart Display

When viewing charts, you can do the following:

| Task | Action |
|---|---|
| View a detailed description of a chart. | .. include:: /includes/extracts/monitor-chart-controls-description.rst |
| Expand a chart. | .. include:: /includes/extracts/monitor-chart-controls-expand.rst |
| Zoom in on a period of time. | .. include:: /includes/extracts/monitor-chart-controls-zoom.rst |
| View statistics at a particular time. | .. include:: /includes/extracts/monitor-chart-controls-point.rst |
| Move a chart. | .. include:: /includes/extracts/monitor-chart-controls-move.rst |
| Share a URL to the chart. | .. include:: /includes/extracts/monitor-chart-controls-share.rst |

## Chart Selection

Ops Manager displays the available metrics to chart for the
selected deployment under the Toggle Charts header.

- Charts marked with plus are inactive.
- Charts marked with  minus are active.

Click on any chart to toggle the chart state.
