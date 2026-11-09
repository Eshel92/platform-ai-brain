<!-- Converted from reference/command/balancerStart.txt (reStructuredText). Includes are inlined. -->

# balancerStart (database command)

## Definition

**`balancerStart`**

Starts the balancer thread.  The command does not wait for a
balancing round to start.

Starting in MongoDB 7.0, starting the balancer also enables 
the AutoMerger for the 
sharded cluster.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.startBalancer`.

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

You can only issue the
`balancerStart` against the `admin` database on a
`mongos` instance.

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     balancerStart: 1, 
     maxTimeMS: <number> 
   } 
)
```

### Command Fields

| Field | Type | Description |
|---|---|---|
| `balancerStart` | any | Any value. |
| `maxTimeMS` | integer | Optional. Time limit for enabling the balancer. Defaults to 60000 milliseconds. |

       

## Example

To start the balancer thread, connect to a `mongos` instance
and issue the following command:

```javascript
db.adminCommand( { balancerStart: 1 } )
```

**See also:**

- `sh.startBalancer()`
- `balancerStart`
