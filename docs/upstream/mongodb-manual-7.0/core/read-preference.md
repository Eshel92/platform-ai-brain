<!-- Converted from core/read-preference.txt (reStructuredText). Includes are inlined. -->

# Read Preference

Read preference describes how MongoDB clients route read operations to
the members of a replica set.

(Figure: /images/replica-set-read-preference.bakedsvg.svg)

By default, an application directs its read operations to the
primary member in a replica set (that is, read 
preference mode "primary"). But, clients can specify a read preference
to send read operations to secondaries.

Read preference consists of the read preference mode and optionally, a tag set list, the maxStalenessSeconds option, and the
hedged read option. Hedged read option is available for sharded
clusters for reads that use non-`primary` read preference.

## Read Preference Modes

The following table lists a brief summary of the read preference modes:

**Note:**

Non-`primary` read preference modes support 
hedged read on sharded clusters.

| Read Preference Mode | Description |
|---|---|
| `primary` | Default mode. Operations read from the current replica set primary. Transactions that contain read operations must use read preference `primary`. All operations in a given transaction must route to the same member. |
| `primaryPreferred` | Operations read from the primary if it is available. If it isn't, they read from eligible secondary members. Read preference `primaryPreferred` supports hedged reads on sharded clusters. |
| `secondary` | Operations read from eligible secondary members of the replica set. Read preference `secondary` supports hedged reads on sharded clusters. |
| `secondaryPreferred` | .. include:: /includes/secondaryPreferred-read-mode.rst Read preference `secondaryPreferred` supports hedged reads on sharded clusters. |
| `nearest` | Operations read from an eligible member that has a network latency within the latency window, regardless of whether it is primary or secondary. Read preference `nearest` supports hedged reads on sharded clusters and enables the hedged read option by default. |

- For all modes, a member is *available* when it responds to the client's
  periodic monitoring checks, which confirm that the member is reachable over
  the network and able to respond to requests.

- For all modes except `primary`, a member is *eligible* if it satisfies the
  read preference's maxStalenessSeconds
  option and any specified tag set lists.

- For all modes except `primary`, the `localThresholdMS`
  connection string option sets the local threshold that the client uses to
  calculate the latency window
  when choosing among eligible members.

**Important:**

Read preference modes provide no guarantee that an operation succeeds.
Availability and eligibility determine which members the client
considers, but a selected member can still reject an operation, such as when
it is under load.

For detailed description of the read preference modes, see
replica-set-read-preference-modes.

## Behavior

- All read preference modes except `primary` may return
  stale data because secondaries replicate
  operations from the primary in an asynchronous process.
  [#edge-cases-2-primaries]_ Ensure that your application can
  tolerate stale data if you choose to use a non-`primary`
  mode.

- Read preference does not affect the visibility of data.
  Clients can see the results of writes before they are
  acknowledged or have propagated to a majority of replica set
  members. For details, see
  /core/read-isolation-consistency-recency.

- Read preference does not affect
  causal consistency. The
  causal consistency guarantees provided by
  causally consistent sessions for read operations with
  `"majority"` read concern and write	operations with
  `"majority"` write concern hold across all members
  of the MongoDB deployment.	

**Warning:** Secondary Reads in a Sharded Cluster with Migrations Can Miss Documents

Long-running secondary reads in a sharded cluster can miss documents 
if migrations are occurring.

Before deleting a chunk during chunk migration, MongoDB waits for 
in-progress queries involving the chunk to complete on the shard 
primary and then waits an additional `orphanCleanupDelaySecs`
seconds. Queries that were initially run on a node that was primary, 
but continue after the node has stepped down to a secondary, will be 
treated as if they were initially executed on a secondary. That is, 
the server only waits for `orphanDelayCleanupSecs` if there are no 
queries targeting the chunk on the current primary.

Queries that target the chunk and are run on secondaries may miss 
documents if these queries take longer than 
`orphanCleanupDelaySecs`.

## Read Preference Modes

**`primary`**

All read operations use only the current replica set
primary. [#edge-cases-2-primaries]_ This is the default read
mode. If the primary is unavailable, read operations produce an
error or throw an exception.

The `primary` read preference mode is not compatible with
read preference modes that use tag set lists or maxStalenessSeconds. 
If you specify tag set lists or a `maxStalenessSeconds` value
with `primary`, the driver will produce an error.

Transactions that contain
read operations must use read preference `primary`. All
operations in a given transaction must route to the same member.

**`primaryPreferred`**

Operations read from the primary member of the set if it is
available. If the primary is unavailable, such as during failover
situations, operations read from secondary members that satisfy the
read preference's `maxStalenessSeconds` and tag set lists.

When the `primaryPreferred` read preference includes a maxStalenessSeconds value and there is no primary from which to read,
the client estimates how stale each
secondary is by comparing the secondary's last write
to that of the secondary with the most recent write. The client then directs the read operation to a
secondary whose estimated lag is less than or equal to `maxStalenessSeconds`.

When the read preference includes a tag set list (an array of tag
sets) and there is no primary from which to read,
the client attempts to find secondary members with matching tags
(trying the tag sets in order until a match is found). If
matching secondaries are found, the client selects a
random secondary from the nearest group of matching
secondaries. If no secondaries have matching tags, the read operation produces an error.

When the read preference includes a `maxStalenessSeconds` value
**and** a tag set list, the client filters by staleness first and
then by the specified tags. 

Read operations using the `primaryPreferred` mode may return stale data. Use the
`maxStalenessSeconds` option to avoid reading from secondaries
that the client estimates are overly stale.

**Note:**

Read preference `primaryPreferred` supports
hedged reads on sharded clusters.

**`secondary`**

Operations read *only* from the secondary members of the set.
If no secondaries are available, then this read operation produces an
error or exception.

Most replica sets have at least one secondary, but there are
situations where there may be no available secondary. For example, a
replica set with a primary, a secondary, and an
arbiter may not have any secondaries if a member is in
recovering state or unavailable.

When the `secondary` read preference includes a maxStalenessSeconds value,
the client estimates how stale each
secondary is by comparing the secondary's last write
to that of the primary. The client then directs the read operation to a
secondary whose estimated lag is less than or equal to `maxStalenessSeconds`.
If there is no primary, the client uses the secondary with the most
recent write for the comparison.

When the read preference includes a tag set list (an array of tag
sets),
the client attempts to find secondary members with matching tags
(trying the tag sets in order until a match is found). If
matching secondaries are found, the client selects a
random secondary from the nearest group of matching
secondaries. If no secondaries have matching tags, the read operation produces an error.

When the read preference includes a `maxStalenessSeconds` value
**and** a tag set list, the client filters by staleness first and
then by the specified tags. 

Read operations using the `secondary` mode may return stale data. Use the
`maxStalenessSeconds` option to avoid reading from secondaries
that the client estimates are overly stale.

**Note:**

Read preference `secondary` supports
hedged reads on sharded clusters.

**`secondaryPreferred`**

Operations read data from eligible secondary members of the replica 
set. If no eligible secondaries are available, operations read from the 
primary member.

When the `secondaryPreferred` read preference includes a maxStalenessSeconds value,
the client estimates how stale each
secondary is by comparing the secondary's last write
to that of the primary. The client then directs the read operation to a
secondary whose estimated lag is less than or equal to `maxStalenessSeconds`.
If there is no primary, the client uses the secondary with the most
recent write for the comparison. If there are no secondaries with
estimated lag less than or equal to `maxStalenessSeconds`, the
client directs the read operation to the replica set's primary.

When the read preference includes a tag set list (an array of tag
sets),
the client attempts to find secondary members with matching tags
(trying the tag sets in order until a match is found). If
matching secondaries are found, the client selects a
random secondary from the nearest group of matching
secondaries. If no secondaries have matching tags, the client ignores tags and reads from the primary.

When the read preference includes a `maxStalenessSeconds` value
**and** a tag set list, the client filters by staleness first and
then by the specified tags. 

Read operations using the `secondaryPreferred` mode may return stale data. Use the
`maxStalenessSeconds` option to avoid reading from secondaries
that the client estimates are overly stale.

**Note:**

Read preference `secondaryPreferred` supports
hedged reads on sharded clusters.

**`nearest`**

The driver reads from a member whose network latency falls within
the acceptable latency window. Reads in the `nearest` mode
do not consider whether a member is a primary or
secondary when routing read operations: primaries and
secondaries are treated equivalently.

Set this mode to minimize the effect of network latency
on read operations without preference for current or stale data.

When the read preference includes a maxStalenessSeconds value, the client estimates
how stale each secondary is by comparing the secondary's last write
to that of the primary, if available, or to the secondary with the
most recent write if there is no primary. The client will then
filter out any secondary whose estimated lag is greater than
`maxStalenessSeconds` and randomly direct the read to a remaining
member (primary or secondary) whose network latency falls within the
acceptable latency window.

If you specify a tag set list, the client attempts to
find a replica set member that matches the specified tag set lists and
directs reads to an arbitrary member from among the nearest
group.

When the read preference includes a `maxStalenessSeconds` value
**and** a tag set list, the client filters by staleness first and
then by the specified tags. From the remaining `mongod` instances, the client then
randomly directs the read to an instance that falls within the
acceptable latency window. The read preference member
selection
documentation describes the process in detail.

Read operations using the `nearest` mode may return stale data. Use the
`maxStalenessSeconds` option to avoid reading from secondaries
that the client estimates are overly stale.

**Note:**

Read preference `nearest`, by
default, specifies the use of hedged reads for reads on a sharded cluster.

**See also:**

To learn about use cases for specific read preference settings,
see read-preference-use-cases. 

## Configure Read Preference

When using a MongoDB driver, you can specify the read preference using
the driver's read preference API. See the driver `API
documentation`. You can also set the read preference (except
for the hedged read option) when connecting to the replica set or
sharded cluster. For an example, see
connection string.

For a given read preference, the MongoDB drivers use the same
member selection logic.

When using `mongosh`, see
`cursor.readPref()` and `Mongo.setReadPref()`. 

## Read Preference and Transactions

Transactions that contain
read operations must use read preference `primary`. All
operations in a given transaction must route to the same member.

## Additional Considerations

Consider the following points when using `$merge` or
`$out` stages in an aggregation pipeline:

- Starting in MongoDB 5.0, pipelines with a `$merge` stage can run on
  replica set secondary nodes if all the nodes in the cluster
  have the featureCompatibilityVersion set to `5.0`
  or higher and the read preference
  allows secondary reads.

  - `$merge` and `$out` stages run on secondary nodes, but write
    operations are sent to the primary node.

  - Not all driver versions support `$merge` operations sent to
    the secondary nodes. For details, see the `driver`
    documentation.

- In earlier MongoDB versions, pipelines with `$out` or `$merge`
  stages always run on the primary node and read preference isn't
  considered.

For `mapReduce` operations, only "inline"
`mapReduce` operations that do not write data support read
preference. Otherwise, `mapReduce` operations run on the
primary member.
