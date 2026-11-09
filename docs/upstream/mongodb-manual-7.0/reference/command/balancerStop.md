<!-- Converted from reference/command/balancerStop.txt (reStructuredText). Includes are inlined. -->

# balancerStop (database command)

## Definition

**`balancerStop`**

Disables the balancer in a sharded cluster. If a balancing round is
in progress, the operation waits for balancing to complete.

You can only issue the `balancerStop` command against the
`admin` database on a `mongos` instance.

Starting in MongoDB 7.0, stopping the balancer also disables 
the AutoMerger for the 
sharded cluster.

**Important:**

Leaving the balancer disabled for extended periods of time can lead to
unbalanced shards, which degrade cluster performance. Only disable the
balancer if necessary, and ensure that you re-enable the balancer when maintenance is complete.

helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.stopBalancer`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     balancerStop: 1, 
     maxTimeMS: <number> 
   }
)
```

### Command Fields

| Field | Type | Description |
|---|---|---|
| `balancerStop` | any | Any value. |
| `maxTimeMS` | integer | Time limit for disabling the balancer. Defaults to 60000 milliseconds. |

       

## Example

To stop the balancer thread, connect to a `mongos` instance
and issue the following command:

```javascript
db.adminCommand( { balancerStop: 1 } )
```

## Learn More

- `sh.stopBalancer()`
- `balancerStart`
