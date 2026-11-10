<!-- Converted from troubleshooting/fix-common-cluster-issues.asciidoc (AsciiDoc). Includes are inlined. -->

## Fix common cluster issues

This guide describes how to fix common errors and problems with Elasticsearch clusters.

****
If you're using Elastic Cloud Hosted, then you can use AutoOps to monitor your cluster. AutoOps significantly simplifies cluster management with performance recommendations, resource utilization visibility, real-time issue detection and resolution paths. For more information, refer to [Monitor with AutoOps](https://www.elastic.co/guide/en/cloud/current/ec-autoops.html).
****

Watermark errors::
Fix watermark errors that occur when a data node is critically low on disk space
and has reached the flood-stage disk usage watermark.

Circuit breaker errors::
Elasticsearch uses circuit breakers to prevent nodes from running out of JVM heap memory.
If Elasticsearch estimates an operation would exceed a circuit breaker, it stops
the operation and returns an error.

High CPU usage::
The most common causes of high CPU usage and their solutions.

High JVM memory pressure::
High JVM memory usage can degrade cluster performance and trigger circuit
breaker errors.

Red or yellow cluster status::
A red or yellow cluster status indicates one or more shards are missing or
unallocated. These unassigned shards increase your risk of data loss and can
degrade cluster performance.

Rejected requests::
When Elasticsearch rejects a request, it stops the operation and returns an error with a
`429` response code.

Task queue backlog::
A backlogged task queue can prevent tasks from completing and put the cluster
into an unhealthy state.

Diagnose unassigned shards::
There are multiple reasons why shards might get unassigned, ranging from 
misconfigured allocation settings to lack of disk space.

Troubleshooting an unstable cluster::
A cluster in which nodes leave unexpectedly is unstable and can create several 
issues.

Mapping explosion::
A cluster in which an index or index pattern as exploded with a high count of 
mapping fields which causes performance look-up issues for Elasticsearch and 
Kibana.

Hot spotting::
Hot spotting may occur in Elasticsearch when resource utilizations are unevenly
distributed across nodes.

(See `troubleshooting/common-issues/disk-usage-exceeded.md`)
(See `troubleshooting/common-issues/circuit-breaker-errors.md`)
(See `troubleshooting/common-issues/high-cpu-usage.md`)
(See `troubleshooting/common-issues/high-jvm-memory-pressure.md`)
(See `troubleshooting/common-issues/red-yellow-cluster-status.md`)
(See `troubleshooting/common-issues/rejected-requests.md`)
(See `troubleshooting/common-issues/task-queue-backlog.md`)
(See `troubleshooting/common-issues/mapping-explosion.md`)
(See `troubleshooting/common-issues/hotspotting.md`)
(See `troubleshooting/common-issues/diagnose-unassigned-shards.md`)
