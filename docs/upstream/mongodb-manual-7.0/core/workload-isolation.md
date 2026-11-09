<!-- Converted from core/workload-isolation.txt (reStructuredText). Includes are inlined. -->

# Workload Isolation in MongoDB Deployments

## Operational Overview

MongoDB includes a number of features that allow database
administrators and developers to isolate workload by functional or
geographical groupings.

This capability provides "data center awareness," which allows
applications to target MongoDB deployments with consideration of the
physical location of the `mongod` instances. MongoDB supports
segmentation of operations across different dimensions, which may
include multiple data centers and geographical regions in multi-data
center deployments, racks, networks, or power circuits in single
data center deployments.

MongoDB also supports workload isolation based on
functional or operational parameters, to ensure that certain
`mongod` instances are only used for reporting workloads or
that certain high-frequency portions of a sharded collection only
exist on specific shards.

Specifically, with MongoDB, you can:

- ensure write operations propagate to specific members of a replica
  set, or to specific members of replica sets.

- ensure that specific members of a replica set respond to queries.

- ensure that specific ranges of your shard key balance onto and
  reside on specific shards.

- combine the above features in a single distributed deployment, on a
  per-operation (for read and write operations) and collection (for
  chunk distribution in sharded clusters distribution) basis.

For full documentation of these features, see the following
documentation in the MongoDB Manual:

- Read Preferences, which controls how drivers
  help applications target read operations to members of a replica set.

- Write Concerns, which controls
  how MongoDB ensures that write operations propagate to members of a
  replica set.

- Replica Set Tags, which
  control how applications create and interact with custom groupings
  of replica set members to create custom application-specific read
  preferences and write concerns.
  
- Zones in sharded clusters, which allows MongoDB
  administrators to create zones that represent a group of 
  shards and associate one or more ranges of shard key values to
  these zones. You can associate each zone with one or more shards in the 
  cluster. A shard can associate with any number of zones. In a balanced 
  cluster, MongoDB directs reads and writes covered by a zone only to the 
  shards inside the zone.

**See also:**

Before adding workload isolation features to your application
and MongoDB deployment, become familiar with all documentation of
replication, and sharding.
