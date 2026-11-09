<!-- Converted from reference/method/sh.enableBalancing.txt (reStructuredText). Includes are inlined. -->

# sh.enableBalancing() (mongosh method)

## Description

**`sh.enableBalancing(namespace)`**

Enables the balancer for the specified namespace of the sharded collection.

**Important:**

You can only run `sh.enableBalancing()` on a
`mongos` instance. `sh.enableBalancing()`
errors if run on `mongod` instance.

The `sh.enableBalancing()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the collection. |

**Important:**

`sh.enableBalancing()` does not *start*
balancing. Rather, it allows balancing of this collection the
next time the balancer runs.

For more information on the balancing process, see
/tutorial/manage-sharded-cluster-balancer and
sharding-balancing.

## Compatibility

This method is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
