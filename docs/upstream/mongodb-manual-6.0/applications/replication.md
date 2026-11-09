<!-- Converted from applications/replication.txt (reStructuredText). Includes are inlined. -->

# Replica Set Read and Write Semantics

From the perspective of a client application, whether a MongoDB
instance is running as a single server (i.e. "standalone") or a
replica set is transparent. However, MongoDB provides
additional read and write configurations for replica sets.

**Note:**

Sharded clusters where the shards are also
replica sets provide the same operational semantics with regards to
write and read operations.

/core/replica-set-write-concern
   Write concern describes the level of acknowledgment requested
   from MongoDB for write operations.

/core/read-preference
   Read preference specifies where (i.e. which members of the replica
   set) the drivers should direct the read operations.

/core/read-preference-mechanics
   Describes the mechanics of read preference.
