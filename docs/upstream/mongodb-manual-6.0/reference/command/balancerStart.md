<!-- Converted from reference/command/balancerStart.txt (reStructuredText). Includes are inlined. -->

# balancerStart

## Definition

**`balancerStart`**

Starts the balancer thread.  The command does not wait for a
balancing round to start.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.startBalancer`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
This is because of balancing policy improvements. Auto-splitting commands 
still exist, but do not perform an operation. For details, see
release-notes-6.0-balancing-policy-changes.

In MongoDB versions earlier than 6.0, the command enables
auto-splitting for the sharded cluster. To disable auto-splitting
when the balancer is enabled, you can use
`sh.disableAutoSplit()`.

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
