<!-- Converted from troubleshooting.asciidoc (AsciiDoc). Includes are inlined. -->

# Troubleshooting

This section provides a series of troubleshooting solutions aimed at helping users
fix problems that an Elasticsearch deployment might encounter.

****
If you're using Elastic Cloud Hosted, then you can use AutoOps to monitor your cluster. AutoOps significantly simplifies cluster management with performance recommendations, resource utilization visibility, real-time issue detection and resolution paths. For more information, refer to [Monitor with AutoOps](https://www.elastic.co/guide/en/cloud/current/ec-autoops.html).
****

### General

* Fix common cluster issues
* Several troubleshooting issues can be diagnosed using the
health API.

### Data

* Fix watermark errors caused by low disk space
* Add a missing tier to the system
* Allow Elasticsearch to allocate the data in the system
* Allow Elasticsearch to allocate the index
* Indices mix index allocation filters with data tiers node roles to move through data tiers
* Configuring source mode in mappings is deprecated and replaced by an index setting
* Not enough nodes to allocate all shard replicas
* Total number of shards for an index on a single node exceeded
* Total number of shards per node has been reached
* Troubleshooting data corruption

### Management

* Start index lifecycle management
* Start snapshot lifecycle management

### Capacity

* Fix data nodes out of disk
* Fix master nodes out of disk
* Fix other role nodes out of disk

### Snapshot and restore

* Restore data from snapshot
* Troubleshooting broken repositories
* Troubleshooting repeated snapshot failures

### Other issues

* Troubleshooting an unstable cluster
* Troubleshooting discovery
* Troubleshooting monitoring
* Troubleshooting transforms
* Troubleshooting Watcher
* Troubleshooting searches
* Troubleshooting shards capacity
* Troubleshooting an unbalanced cluster
* Troubleshooting remote clusters

### Contact us

If none of these guides relate to your issue, or you need further assistance,
then you can contact us as follows:

* If you have an active subscription, you have several options:

** Go directly to the [Support Portal](http://support.elastic.co)

** From the Elasticsearch Service Console, go to the
 [Support page](https://cloud.elastic.co/support{ess-baymax}), or select the
 support icon that looks like a life preserver on any page.

** Contact us by email: support@elastic.co

**Tip:**
If you contact us by email, use the email address that you registered with so
that we can help you more quickly. If you are using a distribution list as your
registered email, you can also register a second email address with us. Just
open a case to let us know the name and email address you want to add.

* For users without an active subscription, visit the
[Elastic community forums](https://discuss.elastic.co/) and get answers from
the experts in the community, including people from Elastic.

(See `troubleshooting/fix-common-cluster-issues.md`)
(See `troubleshooting/data/add-tier.md`)
(See `troubleshooting/data/enable-cluster-allocation.md`)
(See `troubleshooting/data/enable-index-allocation.md`)
(See `troubleshooting/data/data-tiers-mixed-with-node-attr.md`)
(See `troubleshooting/data/increase-tier-capacity.md`)
(See `troubleshooting/data/increase-shard-limit.md`)
(See `troubleshooting/data/increase-cluster-shard-limit.md`)
(See `troubleshooting/data/source-mode-setting.md`)
(See `troubleshooting/corruption-issues.md`)
(See `troubleshooting/disk/fix-data-node-out-of-disk.md`)
(See `troubleshooting/disk/fix-master-node-out-of-disk.md`)
(See `troubleshooting/disk/fix-other-node-out-of-disk.md`)
(See `troubleshooting/data/start-ilm.md`)
(See `troubleshooting/data/start-slm.md`)
(See `troubleshooting/data/restore-from-snapshot.md`)
(See `troubleshooting/snapshot/add-repository.md`)
(See `troubleshooting/snapshot/repeated-snapshot-failures.md`)
(See `troubleshooting/troubleshooting-unstable-cluster.md`)
(See `troubleshooting/discovery-issues.md`)
(See `monitoring/troubleshooting.md`)
(See `transform/troubleshooting.md`)
(See `watcher/troubleshooting.md`)
(See `troubleshooting/troubleshooting-searches.md`)
(See `troubleshooting/troubleshooting-shards-capacity.md`)
(See `troubleshooting/troubleshooting-unbalanced-cluster.md`)
(See `troubleshooting/diagnostic.md`)
