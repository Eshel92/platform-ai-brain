<!-- Converted from reference/method/sh.waitForBalancer.txt (reStructuredText). Includes are inlined. -->

# sh.waitForBalancer()

## Definition

**`sh.waitForBalancer(wait, timeout, interval)`**

Waits for a change in the state of the balancer.
`sh.waitForBalancer()` is an internal method, which takes
the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `wait` | boolean | Optional. Set to `true` to ensure the balancer is now active. The default is `false`, which waits until balancing stops and becomes inactive. |
| `timeout` | integer | Milliseconds to wait. |
| `interval` | integer | Milliseconds to sleep. |

          
          

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
