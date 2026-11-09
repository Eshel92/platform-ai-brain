<!-- Converted from reference/method/sh.getBalancerState.txt (reStructuredText). Includes are inlined. -->

# sh.getBalancerState()

**`sh.getBalancerState()`**

:returns: boolean

`sh.getBalancerState()` returns `true` when the
balancer is enabled and false if the balancer is
disabled. This does not reflect the current state of balancing
operations: use `sh.isBalancerRunning()` to check the
current state of the balancer.

**See also:**

- `sh.enableBalancing()`
- `sh.disableBalancing()`
- `sh.isBalancerRunning()`
- `sh.setBalancerState()`
- `sh.startBalancer()`
- `sh.stopBalancer()`
- `sh.waitForBalancer()`
- `sh.waitForBalancerOff()`

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
