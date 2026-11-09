<!-- Converted from reference/method/sh.waitForBalancerOff.txt (reStructuredText). Includes are inlined. -->

# sh.waitForBalancerOff()

## Definition

**`sh.waitForBalancerOff(timeout, interval)`**

Internal method that waits until the balancer is not running.

| Parameter | Type | Description |
|---|---|---|
| `timeout` | integer | Milliseconds to wait. |
| `interval` | integer | Milliseconds to sleep. |

**See also:**

- `sh.enableBalancing()`
- `sh.disableBalancing()`
- `sh.getBalancerState()`
- `sh.isBalancerRunning()`
- `sh.setBalancerState()`
- `sh.startBalancer()`
- `sh.stopBalancer()`
- `sh.waitForBalancer()`

## Compatibility

This method is available in deployments hosted in the following environments: 

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
