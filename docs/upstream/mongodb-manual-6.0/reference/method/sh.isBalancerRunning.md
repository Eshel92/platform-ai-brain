<!-- Converted from reference/method/sh.isBalancerRunning.txt (reStructuredText). Includes are inlined. -->

# sh.isBalancerRunning()

## Definition

**`sh.isBalancerRunning()`**

Returns a document describing the status of the balancer.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `balancerStatus` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

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

## Output Document

The following is an example of a document returned by the command:

```json
{
  mode: 'full',
  inBalancerRound: false,
  numBalancerRounds: Long("1143"),
  ok: 1,
  '$clusterTime': {
     clusterTime: Timestamp({ t: 1639753724, i: 3 }),
     signature: {
        hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
        keyId: Long("0")
     }
  },
  operationTime: Timestamp({ t: 1639753724, i: 3 })
}
```

* - Field
  - Description

* - `mode`

  - String that specifies whether the balancer thread is running
    or stopped. Possible values are:

    - "full"
        Balancer thread is running but not necessarily in a
        balancing round.

    - "off"
        Balancer thread is stopped. Chunk balancing cannot occur in
        this mode.

* - `inBalancerRound`

  - Boolean that specifies if the balancer is currently in a
    balancing round.

* - `numBalancerRounds`

  - Number of balancer rounds which have occurred since the
    config servers were started. This value is reset to 0 when 
    the config servers are restarted.

* - `ok`

  - See Command Response.

* - `$clusterTime`

  - See Command Response.

* - `operationTime`

  - See Command Response.

**See also:**

- `sh.enableBalancing()`
- `sh.disableBalancing()`
- `sh.getBalancerState()`
- `sh.setBalancerState()`
- `sh.startBalancer()`
- `sh.stopBalancer()`
- `sh.waitForBalancer()`
- `sh.waitForBalancerOff()`
