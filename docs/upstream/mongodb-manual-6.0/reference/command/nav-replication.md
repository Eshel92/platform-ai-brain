<!-- Converted from reference/command/nav-replication.txt (reStructuredText). Includes are inlined. -->

# Replication Commands

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

| Name | Description |
|---|---|
| `appendOplogNote` | Writes a non-operational entry to the oplog. |
| `applyOps` | Internal command that applies oplog entries to the current data set. |
| `hello` | Displays information about this member's role in the replica set, including whether it is the primary. |
| `replSetAbortPrimaryCatchUp` | Forces the elected primary to abort sync (catch up) then complete the transition to primary. |
| `replSetFreeze` | Prevents the current member from seeking election as primary for a period of time. |
| `replSetGetConfig` | Returns the replica set's configuration object. |
| `replSetGetStatus` | Returns a document that reports on the status of the replica set. |
| `replSetInitiate` | Initializes a new replica set. |
| `replSetMaintenance` | Enables or disables a maintenance mode, which puts a secondary node in a `RECOVERING` state. |
| `replSetReconfig` | Applies a new configuration to an existing replica set. |
| `replSetResizeOplog` | Dynamically resizes the oplog for a replica set member.  Available for WiredTiger storage engine only. |
| `replSetStepDown` | Forces the current primary to *step down* and become a secondary, forcing an election. |
| `replSetSyncFrom` | Explicitly override the default logic for selecting a member to replicate from. |
