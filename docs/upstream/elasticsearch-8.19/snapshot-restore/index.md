<!-- Converted from snapshot-restore/index.asciidoc (AsciiDoc). Includes are inlined. -->

# Snapshot and restore

A snapshot is a backup of a running Elasticsearch cluster. You can use snapshots to:

* Regularly back up a cluster with no downtime
* Recover data after deletion or a hardware failure
* Transfer data between clusters
* Reduce your storage costs by using <<searchable-snapshots,searchable
  snapshots>> in the cold and frozen data tiers

## The snapshot workflow

Elasticsearch stores snapshots in an off-cluster storage location called a snapshot
repository. Before you can take or restore snapshots, you must
register a snapshot repository on the cluster.
Elasticsearch supports several repository types with cloud storage options, including:

* AWS S3
* Google Cloud Storage (GCS)
* Microsoft Azure

After you register a snapshot repository, you can use
snapshot lifecycle management (SLM) to automatically take and manage
snapshots. You can then restore a snapshot to
recover or transfer its data.

## Snapshot contents

By default, a snapshot of a cluster contains the cluster state, all regular data
streams, and all regular indices. The cluster state includes:

* Persistent cluster settings
* Index templates
* Legacy index templates
* Ingest pipelines
* ILM policies
* Stored scripts
* For snapshots taken after 7.12.0, feature states
You can also take snapshots of only specific data streams or indices in the
cluster. A snapshot that includes a data stream or index automatically includes
its aliases. When you restore a snapshot, you can choose whether to restore
these aliases.

Snapshots don't contain or back up:

* Transient cluster settings
* Registered snapshot repositories
* Node configuration files
* Security configuration files

### Feature states

A feature state contains the indices and data streams used to store
configurations, history, and other data for an Elastic feature, such as Elasticsearch
security or Kibana.

**Tip:** To retrieve a list of feature states, use the Features API.

A feature state typically includes one or more <<system-indices,system indices
or system data streams>>. It may also include regular indices and data streams
used by the feature. For example, a feature state may include a regular index
that contains the feature's execution history. Storing this history in a regular
index lets you more easily search it.

In Elasticsearch 8.0 and later versions, feature states are the only way to back up and
restore system indices and system data streams.

## How snapshots work

Snapshots are automatically deduplicated to save storage space and reduce network
transfer costs. To back up an index, a snapshot makes a copy of the index's
segments and stores them in the snapshot repository. Since
segments are immutable, the snapshot only needs to copy any new segments created
since the repository's last snapshot.

Each snapshot is also logically independent. When you delete a snapshot, Elasticsearch
only deletes the segments used exclusively by that snapshot. Elasticsearch doesn't delete
segments used by other snapshots in the repository.

### Snapshots and shard allocation

A snapshot copies segments from an index's primary shards. When you start a
snapshot, Elasticsearch immediately starts copying the segments of any available primary
shards. If a shard is starting or relocating, Elasticsearch will wait for these processes
to complete before copying the shard's segments. If one or more primary shards
aren't available, the snapshot attempt fails.

Once a snapshot begins copying a shard's segments, Elasticsearch won't move the shard to
another node, even if rebalancing or shard allocation settings would typically
trigger reallocation. Elasticsearch will only move the shard after the snapshot finishes
copying the shard's data.

### Snapshot start and stop times

A snapshot doesn't represent a cluster at a precise point in time. Instead, each
snapshot includes a start and end time. The snapshot represents a view of each
shard's data at some point between these two times.

## Snapshot compatibility

To restore a snapshot to a cluster, the versions for the snapshot, cluster, and
any restored indices must be compatible.

### Snapshot version compatibility

You can't restore a snapshot to an earlier version of Elasticsearch. For example, you
can't restore a snapshot taken in 7.6.0 to a cluster running 7.5.0.

**Note:** This documentation is for Elasticsearch version {version}, which is not yet
released. The compatibility table above applies only to snapshots taken in a
released version of Elasticsearch. If you're testing a pre-release build of Elasticsearch then you
can still restore snapshots taken in earlier released builds as permitted by
this compatibility table. You can also take snapshots using your pre-release
build, and restore them using the same build. However once a pre-release build
of Elasticsearch has written to a snapshot repository you must not use the same
repository with other builds of Elasticsearch, even if the builds have the same version.
Different pre-release builds of Elasticsearch may use different and incompatible
repository layouts. If the repository layout is incompatible with the Elasticsearch build
in use then taking and restoring snapshots may result in errors or may appear to
succeed having silently lost some data. You should discard your repository
before using a different build.

### Index compatibility

Any index you restore from a snapshot must also be compatible with the current
cluster's version. If you try to restore an index created in an incompatible
version, the restore attempt will fail.

|====
| 5+^h| Cluster version
h| Index creation version   | 6.8        | 7.0–7.1    | 7.2–{prev-major-last} | 8.0–8.2    | 8.3-{minor-version}
| 5.0–5.6                   | ✓ | ✗  | ✗             | ✗  | ✓^[1]^
| 6.0–6.7                   | ✓ | ✓ | ✓            | ✗  | ✓^[1]^
| 6.8                       | ✓ | ✗  | ✓            | ✗  | ✓^[1]^
| 7.0–7.1                   | ✗  | ✓ | ✓            | ✓ | ✓
| 7.2–{prev-major-last}     | ✗  | ✗  | ✓            | ✓ | ✓
| 8.0–{minor-version}       | ✗  | ✗  | ✗             | ✓ | ✓
|====
[small]#1. Supported with archive indices.#

You can't restore an index to an earlier version of Elasticsearch. For example, you can't
restore an index created in 7.6.0 to a cluster running 7.5.0.

A compatible snapshot can contain indices created in an older incompatible
version. For example, a snapshot of a {prev-major-last} cluster can contain an
index created in 6.8. Restoring the 6.8 index to an {minor-version} cluster
fails unless you can use the archive functionality. Keep
this in mind if you take a snapshot before upgrading a cluster.

As a workaround, you can first restore the index to another cluster running the
latest version of Elasticsearch that's compatible with both the index and your current
cluster. You can then use reindex-from-remote to rebuild
the index on your current cluster. Reindex from remote is only possible if the
index's `_source` is enabled.

Reindexing from remote can take significantly longer than restoring a snapshot.
Before you start, test the reindex from remote process with a subset of the data
to estimate your time requirements.

## Warnings

### Other backup methods

**Taking a snapshot is the only reliable and supported way to back up a
cluster.** You cannot back up an Elasticsearch cluster by making copies of the data
directories of its nodes. There are no supported methods to restore any data
from a filesystem-level backup. If you try to restore a cluster from such a
backup, it may fail with reports of corruption or missing files or other data
inconsistencies, or it may appear to have succeeded having silently lost some of
your data.

A copy of the data directories of a cluster's nodes does not work as a backup
because it is not a consistent representation of their contents at a single
point in time. You cannot fix this by shutting down nodes while making the
copies, nor by taking atomic filesystem-level snapshots, because Elasticsearch has
consistency requirements that span the whole cluster. You must use the built-in
snapshot functionality for cluster backups.

### Repository contents

**Don’t modify anything within the repository or run processes that might
interfere with its contents.** If something other than Elasticsearch modifies the
contents of the repository then future snapshot or restore operations may fail,
reporting corruption or other data inconsistencies, or may appear to succeed
having silently lost some of your data.

You may however safely <<snapshots-repository-backup,restore a repository from a
backup>> as long as

. The repository is not registered with Elasticsearch while you are restoring its
contents.

. When you have finished restoring the repository its contents are exactly as
they were when you took the backup.

If you no longer need any of the snapshots in a repository, unregister it from
Elasticsearch before deleting its contents from the underlying storage.

Additionally, snapshots may contain security-sensitive information, which you
may wish to store in a dedicated repository.

(See `snapshot-restore/register-repository.md`)
(See `snapshot-restore/take-snapshot.md`)
(See `snapshot-restore/restore-snapshot.md`)
(See `snapshot-restore/../searchable-snapshots/index.md`)
