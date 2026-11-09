<!-- Converted from core/read-preference-mechanics.txt (reStructuredText). Includes are inlined. -->

# Server Selection Algorithm

MongoDB drivers use a Server Selection algorithm to choose which
replica set member to use or, when connected to multiple
`mongos` instances, which `mongos` instance to use.

Server selection occurs once per operation.

**Note:**

Transactions that contain
read operations must use read preference `primary`. All
operations in a given transaction must route to the same member.

## Read Preference for Replica Sets

Server selection occurs once per operation and is governed by the
read preference and `localThresholdMS`
settings to determine member eligibility for reads. The read preference
is re-evaluated for each operation.

| Read Preference Mode | Selection Process |
|---|---|
| `primary` (Default) | #. The driver selects the primary. |
| `secondary` | #. The driver assembles a list of eligible secondary members. maxStalenessSeconds and tag sets specified in the read preference can further restrict the eligibility of the members. #. If the list of eligible members is not empty, the driver determines which eligible member is the "closest" (i.e. the member with the lowest average network round-trip-time) and calculates a latency window by adding the average round-trip-time of this "closest" server and the `localThresholdMS`. The  driver uses this latency window to pare down the list of eligible members to those members that fall within this window. #. From this list of eligible members that fall within the latency window, the  driver randomly chooses an eligible member. |
| `nearest` | #. The driver assembles a list of eligible members (primary and secondaries). maxStalenessSeconds and tag sets  specified in the read preference can further limit the eligibility of the members. #. If the list of eligible members is not empty, the driver determines which eligible member is the "closest" (i.e. the member with the lowest average network round-trip-time) and calculates a latency window by adding the average round-trip-time of this "closest" server and the `localThresholdMS` [#default-threshold]_. The driver uses this latency window to pare down the list of eligible members to those members that fall within this window. #. From this list of eligible members that fall within the latency window, the driver randomly chooses an eligible member. |
| `primaryPreferred` | #. If the primary is available, driver selects the primary. #. If the primary is unavailable, server selection follows the process for the read preference `secondary` to select an eligible secondary member. |
| `secondaryPreferred` | #. Following the server selection process for the read preference `secondary`, if a list of eligible secondary members is non-empty, driver chooses an eligible secondary member. #. Otherwise, if the list is empty, driver selects the primary. |

## Read Preference for Sharded Clusters

### Load Balancing

If there is more than one `mongos` instance in the connection
seed list, the driver determines which `mongos` is the
"closest" (that is, the member with the lowest average network
round-trip-time) and calculates the latency window by adding the
average round-trip-time of this "closest" `mongos` instance
and the `localThresholdMS`. The driver load balances randomly
across the `mongos` instances that fall within the latency
window.

**Note:**

`localThresholdMS` biases server selection toward
lower-latency local targets. The setting can't remove the
cross-region network topology that a single private endpoint
creates or guarantee all connections remain in the local
region. In this configuration, a client can still connect
through a `mongos` in another region.

### Read Preference and Shards

For sharded clusters that have replica set shards, `mongos`
applies the read preference when reading from the shards. Server
selection is governed by the read preference and `replication.localPingThresholdMs`
settings. The read preference is re-evaluated for each operation.

#### Hedged Reads

`mongos` supports hedged reads for 
non-`primary` read preferences modes. 
That is, `mongos` can send an additional read to another member, 
if available, to hedge the read operation if using non-`primary` 
read preferences. The additional read sent to 
hedge the read operation uses the `maxTimeMS` value of
`maxTimeMSForHedgedReads`.

Hedged reads are supported for the following operations:

- `collStats`
- `count`
- `dataSize`
- `dbStats`
- `distinct`
- `filemd5`
- `find`
- `listCollections`
- `listIndexes`
- `planCacheListFilters`

To use hedged reads:

- the `mongos` must have enabled support for hedged reads
  (Default). See the `readHedgingMode` parameter.

- Non-`primary` read preferences must
  enable use of hedged reads.

* - Read Preference Mode
  - Selection Process

* - `primary` (Default)

  - #. The `mongos` selects the primary.

* - `secondary`

  - #. The `mongos` assembles a list of eligible secondary members.
       maxStalenessSeconds and tag
       sets specified
       in the read preference can further restrict the
       eligibility of the members.

    #. If the list of eligible members is not empty, the
       `mongos` determines which eligible member is
       the "closest" (i.e. the member with the lowest average
       network round-trip-time) and calculates a latency window
       by adding the average round-trip-time of this "closest"
       server and the `replication.localPingThresholdMs`
       (or `--localThreshold`
       command line option). The `mongos` uses this
       latency window to pare down the list of eligible members
       to those members that fall within this window.

    #. From this list of eligible members that fall within the
       latency window, the `mongos` randomly chooses
       an eligible member. If using hedged reads, `mongos` selects a
       second eligible member if available.

* - `nearest`

  - #. The `mongos` assembles a list of eligible members (primary and
       secondaries). maxStalenessSeconds and tag sets specified
       in the read preference can further limit the eligibility
       of the members.

    #. If the list of eligible members is not empty, the 
       `mongos` determines which eligible member is
       the "closest" (i.e. the member with the lowest average
       network round-trip-time) and calculates a latency window
       by adding the average round-trip-time of this "closest"
       server and the `replication.localPingThresholdMs`
       (or `--localThreshold`
       command line option) [#default-threshold]_. The
       `mongos` uses this latency window to pare
       down the list of eligible members to those members that
       fall within this window.

    #. From this list of eligible members that fall within the
       latency window, the `mongos` randomly chooses
       an eligible member. If using hedged reads, `mongos` selects a
       second eligible member if available.

* - `primaryPreferred`

  - #. If the primary is available, `mongos` selects the primary.

    #. If the primary is unavailable or if `mongos` is
       using hedged reads, server
       selection follows the process for the read preference
       `secondary`. For hedged reads, 

       - If the primary is available, `mongos`
         selects a single eligible secondary, if available.

       - If the primary is unavailable, `mongos`
         selects two eligible secondaries, if available.

* - `secondaryPreferred`

  - #. Following the server selection process for the read
       preference `secondary`, if a list of eligible secondary
       members is non-empty, `mongos` chooses an eligible secondary. If using
       hedged reads,
       `mongos` selects another secondary if
       available.

    #. If the list of eligible secondary
       members is empty or if `mongos` is using hedged
       reads and only one eligible
       secondary is available, `mongos` selects the
       primary.
