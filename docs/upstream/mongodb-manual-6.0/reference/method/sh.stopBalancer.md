<!-- Converted from reference/method/sh.stopBalancer.txt (reStructuredText). Includes are inlined. -->

# sh.stopBalancer()

## Definition

**`sh.stopBalancer(timeout, interval)`**

**Changed in version:** 6.0

Disables the balancer in a sharded cluster.

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0.3, `sh.stopBalancer()`
also disables auto-splitting for the sharded cluster.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `balancerStop` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The method can take the following options:

| Parameter | Type | Description |
|---|---|---|
| `timeout` | integer | Time limit for disabling the balancer. Defaults to 60000 milliseconds. |
| `interval` | integer | The interval (in milliseconds) at which to check if the balancing round has stopped. |

If you omit both options, MongoDB disables the balancer indefinitely.

**Important:**

Leaving the balancer disabled for extended periods of time can lead to
unbalanced shards, which degrade cluster performance. Only disable the
balancer if necessary, and ensure that you re-enable the balancer when maintenance is complete.

You can only run `sh.stopBalancer()` on a
`mongos` instance. `sh.stopBalancer()` errors
if run on `mongod` instance.

The `mongosh` shell method is a wrapper around the
`balancerStop` command.

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

## Behavior

If a balancing round is in progress, the operation waits for balancing
to complete.
   

## Learn More

- `sh.enableBalancing()`
- `sh.disableBalancing()`
- `sh.getBalancerState()`
- `sh.isBalancerRunning()`
- `sh.setBalancerState()`
- `sh.startBalancer()`
- `sh.waitForBalancer()`
- `sh.waitForBalancerOff()`
