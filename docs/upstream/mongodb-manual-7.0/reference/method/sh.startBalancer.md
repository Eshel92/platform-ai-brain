<!-- Converted from reference/method/sh.startBalancer.txt (reStructuredText). Includes are inlined. -->

# sh.startBalancer() (mongosh method)

## Definition

**`sh.startBalancer(timeout, interval)`**

**Changed in version:** 7.0

Starts the balancer in a sharded cluster.

Starting in MongoDB 7.0, starting the balancer also enables 
the AutoMerger for the 
sharded cluster.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `balancerStart` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The method can take the following options:

| Parameter | Type | Description |
|---|---|---|
| `timeout` | integer | Optional. Time limit for enabling the balancer. Defaults to 60000 milliseconds. |
| `interval` | integer | Optional. The frequency (in milliseconds) at which to check if a balancing round has started. |

You can only run `sh.startBalancer()` on a
`mongos` instance. `sh.startBalancer()` errors
if run on `mongod` instance.

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

The `mongosh` shell method `sh.startBalancer()` 
is a wrapper around the `balancerStart` command. 
`sh.startBalancer()` runs the `balancerStart` command in the 
background and returns immediately. 

## Learn More

To learn how to configure the balancer for your cluster, see 
sharded-cluster-balancer.

To disable balancing for a specific collection, see 
disable-balancer-on-collection. 

To re-enable balancing on a specific collection, see 
enable-balancer-on-collection.

- `sh.getBalancerState()`
- `sh.isBalancerRunning()`
- `sh.setBalancerState()`
- `sh.stopBalancer()`
- `sh.waitForBalancer()`
- `sh.waitForBalancerOff()`
