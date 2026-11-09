<!-- Converted from reference/method/sh.disableAutoSplit.txt (reStructuredText). Includes are inlined. -->

# sh.disableAutoSplit

**Note:**

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

## Description

**`sh.disableAutoSplit()`**

Disables the autosplit flag in the `config.settings`
collection. When auto-splitting is enabled for a sharded cluster,
MongoDB automatically splits chunks based on the shard key values
the chunk represents to keep the chunks from growing too large.

You can only run `sh.disableAutoSplit()` from a
`mongosh` session that is connected to a
`mongos` instance. `sh.disableAutoSplit()`
errors if run on a `mongod` instance.

**Note:**

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0.3, `sh.stopBalancer()`
also disables auto-splitting for the sharded cluster.

**See also:**

- /tutorial/manage-sharded-cluster-balancer
- sharding-balancing
