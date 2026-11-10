<!-- Converted from ilm/ilm-actions.asciidoc (AsciiDoc). Includes are inlined. -->

## Index lifecycle actions

Allocate::
Move shards to nodes with different performance characteristics
and reduce the number of replicas.

Delete::
Permanently remove the index.

Force merge::
Reduce the number of index segments and purge deleted documents.

Migrate::
Move the index shards to the data tier that corresponds
to the current ILM phase.

Read only::
Block write operations to the index.

Rollover::
Remove the index as the write index for the rollover alias and
start indexing to a new index.

Downsample::
Aggregates an index's time series data and stores the results in a new read-only
index. For example, you can downsample hourly data into daily or weekly summaries.

Searchable snapshot::
Take a snapshot of the managed index in the configured repository
and mount it as a searchable snapshot.

Set priority::
Lower the priority of an index as it moves through the lifecycle
to ensure that hot indices are recovered first.

Shrink::
Reduce the number of primary shards by shrinking the index into a new index.

Unfollow::
Convert a follower index to a regular index.
Performed automatically before a rollover, shrink, or searchable snapshot action.

Wait for snapshot::
Ensure that a snapshot exists before deleting the index.

(See `ilm/actions/ilm-allocate.md`)
(See `ilm/actions/ilm-delete.md`)
(See `ilm/actions/ilm-forcemerge.md`)
(See `ilm/actions/ilm-migrate.md`)
(See `ilm/actions/ilm-readonly.md`)
(See `ilm/actions/ilm-rollover.md`)
(See `ilm/actions/ilm-downsample.md`)
(See `ilm/actions/ilm-searchable-snapshot.md`)
(See `ilm/actions/ilm-set-priority.md`)
(See `ilm/actions/ilm-shrink.md`)
(See `ilm/actions/ilm-unfollow.md`)
(See `ilm/actions/ilm-wait-for-snapshot.md`)
