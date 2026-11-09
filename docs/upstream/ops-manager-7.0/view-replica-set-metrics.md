<!-- Converted from view-replica-set-metrics.txt (reStructuredText). Includes are inlined. -->

# View Replica Set Deployments

A replica set in MongoDB is a group of 
`mongod` processes that maintain the same data set. To 
view the metrics for a specific Ops Manager replica set deployment
in a project, click the Metrics
button for that deployment. Alternatively, click on the name of
the deployment to open the deployment overview, then click the
Metrics tab.

Monitor deployment metrics to identify performance issues and 
determine whether your current deployment meets your 
requirements. To learn more about the metrics available to monitor 
your deployments, see review-available-metrics.

The Metrics view has three distinct sections:

## Chart Controls

Ops Manager provides the following controls for the Metric
view. Adjusting any of these options affects all charts
displayed under the Metrics view:

| Control | Function |
|---|---|
| Granularity | .. include:: /includes/extracts/monitor-view-control-granularity.rst |
| Zoom | .. include:: /includes/extracts/monitor-view-control-zoom.rst |
| Current Display | .. include:: /includes/extracts/monitor-view-control-current-display.rst |
| Toggle Members | .. include:: /includes/extracts/monitor-view-control-toggle-members.rst |
| Add Chart | .. include:: /includes/extracts/monitor-view-control-add-chart.rst |
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

Ops Manager displays the available metrics to chart for the selected
deployment under the Toggle Charts header. Metrics
are grouped into two sections:

MongoDB Metrics
  Metrics associated with the MongoDB process. For metrics
  related to database performance, such as
  DB Storage, Ops Manager presents the sum total across
  all databases in the deployment.

  If you enable
  Display Opcounters on Separate Charts,
  Ops Manager replaces the Opcounters option with the
  individual components of that chart.

Hardware Metrics
  Metrics associated with the host machines supporting the
  deployment.

  - Charts marked with plus are inactive.
  - Charts marked with  minus are active.

Click on any chart to toggle the chart state.
