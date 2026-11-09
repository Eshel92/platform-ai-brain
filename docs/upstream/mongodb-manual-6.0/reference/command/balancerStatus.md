<!-- Converted from reference/command/balancerStatus.txt (reStructuredText). Includes are inlined. -->

# balancerStatus

## Definition

**`balancerStatus`**

Returns a document that contains information about the status of the
balancer.

You can only issue the `balancerStatus` against the
`admin` database.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.isBalancerRunning`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     balancerStatus: 1 
   } 
)
```

## Output Document

The following is an example of a document returned by the command:

```json
{
   "mode" : "full",
   "inBalancerRound" : false,
   "numBalancerRounds" : NumberLong(86),
   "ok" : 1
}
```

* - Field
  - Description

* - `"mode"`

  - A string that specifies whether the balancer thread is running
    or stopped. Possible values are:

    - "full"
        Balancer thread is running but not necessarily in a
        balancing round.

    - "off"
        Balancer thread is stopped. No chunk balancing can occur in
        this mode.

* - `"inBalancerRound"`

  - A boolean that specifies if the balancer is in a
    balancing round. If `inBalancerRound=true`, it is now
    distributing chunks.

    `inBalancerRound` can be `true` when `mode=off`. If you turn the balancer
    off while it's in a balancing round, the server lets it finish
    rather than interrupting it.

* - `"numBalancerRounds"`

  - The number of balancer rounds which have occurred since the
    config servers were started. This value is not persisted and is
    reset to 0 upon restart of the config servers.

## Example

Connect to a `mongos` instance and issue the following command:

```javascript
db.adminCommand( { balancerStatus: 1 } )
```
