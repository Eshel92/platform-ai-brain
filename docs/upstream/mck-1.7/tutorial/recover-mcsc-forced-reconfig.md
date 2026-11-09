<!-- Converted from tutorial/recover-mcsc-forced-reconfig.txt (reStructuredText). Includes are inlined. -->

# Recover the Sharded Cluster if any of the Replica Sets Lose Majority

If your deployment has lost a voting majority in any of your shards or config 
server's replica sets, you must [restore from backups](https://www.mongodb.com/docs/manual/tutorial/backup-and-restore-tools/) to maintain the consistency 
and integrity of your stored data.

**Warning:**

The Kubernetes Operator doesn't support forced reconfiguration of a Sharded Cluster 
in the event of losing the voting majority. Performing forced reconfiguration 
might result in severe data loss and leave the sharded cluster in 
an inconsistent state.
