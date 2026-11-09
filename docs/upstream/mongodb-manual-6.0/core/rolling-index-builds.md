<!-- Converted from core/rolling-index-builds.txt (reStructuredText). Includes are inlined. -->

# Rolling Index Builds

Rolling index builds are an alternative to the default index
builds. Rolling indexes build indexes on the
applicable nodes sequentially and may reduce the performance impact of
an index build if your deployment matches one of the following cases:

- If your average CPU utilization exceeds (N-1)/N-10% where N is the
  number of CPU threads available to mongod
- If the WiredTiger cache fill ratio regularly exceeds 90%

If your deployment does not meet this criteria, use the
default index build. 

## Considerations

- Rolling index builds hide at most one replica set member at a time,
  starting with the secondary members, and build the index on that member
  as a standalone. 

- Rolling index builds require at least one replica set
  election.

**Note:**

For information about creating indexes in Atlas, refer to the 
index management page in the Atlas 
documentation.

## Tutorials

To create rolling index builds, use the following tutorials:

- index-building-replica-sets
- index-build-on-sharded-clusters
