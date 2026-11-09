<!-- Converted from tutorial/view-diagnostics.txt (reStructuredText). Includes are inlined. -->

# View Deployment Metrics

Ops Manager collects and displays metrics for your servers, databases,
and MongoDB processes in your deployments. All hardware metrics 
include metrics or individual charts for maximum values.

**Note:**

Ops Manager collects hardware metrics only if automation manages the process. 
A monitoring agent can only collect database metrics.

Monitor deployment metrics to identify performance issues and 
determine whether your current deployment meets your 
requirements. To learn more about the metrics available to monitor 
your deployments, see review-available-metrics.

## View Metrics

You can view metrics in the following ways:

Replica Sets
   View the metrics for a specific replica set in a 
   project.

Sharded Clusters
   View the metrics for a specific sharded cluster in a
   project.

MongoDB Processes
   View the metrics for a specific MongoDB process in an 
   Ops Manager cluster.

Real-Time Performance
   View real-time performance metrics for a specific Ops Manager 
   deployment in a project.

## Important Metrics

You can monitor the following metrics to quickly gauge the health of 
your deployment.

| Chart | Description |
|---|---|
| Connections | Number that indicates the total active connections to the deployment. Monitor connections to determine whether the current connection limits are sufficient. To learn more, see Fix Lost Primary. |
| Disk IOPS | Number that indicates the input operations per second. Monitor whether disk IOPS approaches the maximum provisioned IOPS. Determine whether the cluster can handle future workloads. To learn more, see Fix IOPS Issues and Fix Lost Primary. |
| Query Targeting | Number that indicates the efficiency of read operations run on MongoDB. Monitor query targeting metrics to identify inefficient queries. To learn more, see Fix Query Issues. |
| Normalized System CPU | Number that indicates CPU usage of all processes on the node, scaled to a range of 0-100% by dividing by the number of CPU cores. Monitor CPU usage to determine whether data is retrieved from disk instead of memory. To learn more, see Fix IOPS Issues, Fix Lost Primary, and Fix CPU Usage Issues. |
