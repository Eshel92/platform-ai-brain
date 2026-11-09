<!-- Converted from core/sharding-change-a-shard-key.txt (reStructuredText). Includes are inlined. -->

# Change a Shard Key

The ideal shard key allows MongoDB to distribute documents evenly
throughout the cluster while facilitating common query patterns. A
suboptimal shard key can lead to uneven data distribution and the
following problems:

- Jumbo chunks
- Uneven load distribution
- Decreased query performance over time

To address these issues, MongoDB allows you to change your shard key:

- Starting in MongoDB 5.0, you can reshard a collection by changing a collection's shard key.
- You can refine a shard key by adding a suffix field 
  or fields to the existing shard key.

Data distribution fixes are most effective when you 
reshard a collection. If you want to improve data distribution and your
cluster meets the criteria to reshard,
you should reshard the collection instead of refining the shard key. If
your cluster doesn't meet the criteria to reshard, you should 
refine the shard key.

For more information on common performance and scaling issues and advice
on how to fix them, read shardkey-troubleshoot-shard-keys.
