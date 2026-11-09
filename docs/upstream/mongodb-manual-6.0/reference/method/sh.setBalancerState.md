<!-- Converted from reference/method/sh.setBalancerState.txt (reStructuredText). Includes are inlined. -->

# sh.setBalancerState()

## Description

**`sh.setBalancerState(state)`**

Enables or disables the balancer.

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0.3,
`sh.setBalancerState()` also enables auto-splitting if
enabling the balancer and disables auto-splitting if disabling the
balancer.

Use `sh.getBalancerState()` to determine if the balancer is
currently enabled or disabled and `sh.isBalancerRunning()`
to check its current state.

   `balancerStop` commands

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `balancerStart` and.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**Important:**

You can only run `sh.setBalancerState()` on a
`mongos` instance. `sh.setBalancerState()`
errors if run on `mongod` instance.

The `sh.setBalancerState()` method has the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| `state` | boolean | Set this to `true` to enable the balancer and `false` to disable it. Leaving the balancer disabled for extended periods of time can lead to unbalanced shards, which degrade cluster performance. Only disable the balancer if necessary, and ensure that you re-enable the balancer when maintenance is complete. |

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Learn More

- `sh.enableBalancing()`
- `sh.disableBalancing()`
- `sh.getBalancerState()`
- `sh.isBalancerRunning()`
- `sh.startBalancer()`
- `sh.stopBalancer()`
- `sh.waitForBalancer()`
- `sh.waitForBalancerOff()`
