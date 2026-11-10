<!-- Converted from ccr/auto-follow.asciidoc (AsciiDoc). Includes are inlined. -->

### Manage auto-follow patterns

To replicate time series indices, you configure an auto-follow pattern so that
each new index in the series is replicated automatically. Whenever the name of
a new index on the remote cluster matches the auto-follow pattern, a
corresponding follower index is added to the local cluster.

**Note:** Auto-follow patterns only match open indices on the remote cluster that
have all primary shards started. Auto-follow patterns do not match indices that
can't be used for CCR such as closed indices or
{search-snaps}. Avoid using an auto-follow pattern
that matches indices with a read or write block. These
blocks prevent follower indices from replicating such indices.

You can also create auto-follow patterns for data streams. When a new backing
index is generated on a remote cluster, that index and its data stream are
automatically followed if the data stream name matches an auto-follow
pattern. If you create a data stream after creating the auto-follow pattern,
all backing indices are followed automatically.

The data streams replicated from a remote cluster by CCR are protected from
local rollovers. The promote data stream API
can be used to turn these data streams into regular data streams.

Auto-follow patterns are especially useful with
Index lifecycle management, which might continually create
new indices on the cluster containing the leader index.

To start using cross-cluster replication auto-follow patterns from Stack Management in Kibana, select
*Cross-Cluster Replication* from the side navigation and choose the
*Auto-follow patterns* tab.

#### Create auto-follow patterns

When you create an auto-follow pattern,
you are configuring a collection of patterns against a single remote cluster.
When an index is created in the remote cluster with a name that matches one of
the patterns in the collection, a follower index is configured in the local
cluster. The follower index uses the new index as its leader index.

Use the create auto-follow pattern API to add a
new auto-follow pattern configuration.

#### Retrieve auto-follow patterns

To view existing auto-follow patterns and make changes to the backing
patterns, access Kibana on your _remote_ cluster.

Select the auto-follow pattern that you want to view details about. From there,
you can make changes to the auto-follow pattern. You can also view your
follower indices included in the auto-follow pattern.

Use the get auto-follow pattern API to inspect
all configured auto-follow pattern collections.

#### Pause and resume auto-follow patterns

To pause and resume replication of auto-follow pattern collections,
access Kibana, select the auto-follow pattern,
and pause replication.

To resume replication, select the pattern and choose
*Manage pattern > Resume replication*.

Use the pause auto-follow pattern API to
pause auto-follow patterns.
Use the resume auto-follow pattern API to
resume auto-follow patterns.

#### Delete auto-follow patterns

To delete an auto-follow pattern collection,
access Kibana, select the auto-follow pattern,
and pause replication.

When the pattern status changes to Paused, choose
*Manage pattern > Delete pattern*.

Use the delete auto-follow pattern API to
delete a configured auto-follow pattern collection.
