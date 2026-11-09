<!-- Converted from data-center-awareness.txt (reStructuredText). Includes are inlined. -->

# Data Center Awareness

MongoDB provides a number of features that allow application
developers and database administrators to customize the behavior of a
sharded cluster or replica set deployment so that
MongoDB may be *more* "data center aware," or allow operational
and location-based separation.

MongoDB also supports workload isolation based on functional parameters, to ensure
that certain `mongod` instances are only used for reporting workloads
or that certain high-frequency portions of a sharded collection only exist on
specific shards.

The following documents, *found either in this section or other sections
of this manual*, provide information on customizing a deployment for
operation- and location-based separation:

/core/workload-isolation
   MongoDB lets you specify that certain application operations use
   certain `mongod` instances.

/core/zone-sharding
   A zone represents one or more ranges of shard key values for a
   sharded collection. MongoDB routes reads and writes for sharded
   data covered by a zone only to shards inside that zone. For use in
   managing data distribution and deployment patterns.

/tutorial/manage-shard-zone
   Administrative tasks related to configuring zones in sharded
   clusters

## Further Reading

- The /reference/write-concern and /core/read-preference
  documents, which address capabilities related to data center
  awareness.

- /tutorial/deploy-geographically-distributed-replica-set.
