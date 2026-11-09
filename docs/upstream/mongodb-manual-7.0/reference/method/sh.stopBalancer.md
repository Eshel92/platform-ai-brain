<!-- Converted from reference/method/sh.stopBalancer.txt (reStructuredText). Includes are inlined. -->

# sh.stopBalancer() (mongosh method)

## Definition

**`sh.stopBalancer(timeout, interval)`**

**Changed in version:** 7.0

Disables the balancer in a sharded cluster.

Starting in MongoDB 7.0, stopping the balancer also disables 
the AutoMerger for the 
sharded cluster.

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

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
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
