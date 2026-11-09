<!-- Converted from core/replica-set-high-availability.txt (reStructuredText). Includes are inlined. -->

# Replica Set High Availability

Replica sets use elections to support 
high availability. 

/core/replica-set-elections
   Elections occur when the primary becomes unavailable and the
   replica set members autonomously select a new primary.

/core/replica-set-rollbacks
   A rollback reverts write operations on a former primary when the
   member rejoins the replica set after a failover.
