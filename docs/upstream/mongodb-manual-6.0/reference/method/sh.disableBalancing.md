<!-- Converted from reference/method/sh.disableBalancing.txt (reStructuredText). Includes are inlined. -->

# sh.disableBalancing()

## Description

**`sh.disableBalancing(namespace)`**

Disables the balancer for the
specified sharded collection. This does not affect the balancing of
chunks for other sharded collections in the same cluster.

**Important:**

You can only run `sh.disableBalancing()` on a
`mongos` instance. `sh.disableBalancing()`
errors if run on `mongod` instance.

The `sh.disableBalancing()` method has the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the collection. |

For more information on the balancing process, see
/tutorial/manage-sharded-cluster-balancer and
sharding-balancing.

## Compatibility

This method is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
