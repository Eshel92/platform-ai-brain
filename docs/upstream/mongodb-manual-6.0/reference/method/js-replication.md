<!-- Converted from reference/method/js-replication.txt (reStructuredText). Includes are inlined. -->

# Replication Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

| Name | Description |
|---|---|
| `rs.add()` | Adds a member to a replica set. |
| `rs.addArb()` | Adds an arbiter to a replica set. |
| `rs.conf()` | Returns the replica set configuration document. |
| `rs.freeze()` | Prevents the current member from seeking election as primary for a period of time. |
| `rs.help()` | Returns basic help text for replica set functions. |
| `rs.initiate()` | Initializes a new replica set. |
| `rs.printReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the primary. |
| `rs.printSecondaryReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the secondaries. |
| `rs.reconfig()` | Reconfigures a replica set by applying a new replica set configuration object. |
| `rs.reconfigForPSASet()` | Safely perform some reconfiguration changes on a primary-secondary-arbiter (PSA) replica set or on a replica set that is changing to a PSA architecture. |
| `rs.remove()` | Remove a member from a replica set. |
| `rs.status()` | Returns a document with information about the state of the replica set. |
| `rs.stepDown()` | Causes the current primary to become a secondary which forces an election. |
| `rs.syncFrom()` | Sets the member that this replica set member will sync from, overriding the default sync target selection logic. |
