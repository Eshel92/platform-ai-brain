<!-- Converted from reference/command/replSetMaintenance.txt (reStructuredText). Includes are inlined. -->

# replSetMaintenance (database command)

## Definition

**`replSetMaintenance`**

The `replSetMaintenance` admin command enables or disables the
maintenance mode for a secondary member of a replica
set.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     replSetMaintenance: <boolean> 
   }
)
```

## Behavior

Consider the following behavior when running the
`replSetMaintenance` command:

- You cannot run the command on the Primary.

- You must run the command against the `admin` database.

- When enabled `replSetMaintenance: true`, the member enters the
  `RECOVERING` state. While the secondary is `RECOVERING`:

  - The member is not accessible for read operations.

  - The member continues to sync its oplog from the Primary.

- When a node receives a `replSetMaintenance: true` request, it
  adds a maintenance mode task to a queue of tasks. If the queue of
  tasks was empty and now is not, the node will transition to
  `RECOVERING` state and begin to reject read requests. When a node
  receives a `replSetMaintenance: false` request, it removes a
  maintenance mode task from the queue (even if that task was
  initiated by a different client). If the request empties 
  the maintenance mode task queue, the node will return to 
  `SECONDARY` state.
    
- If you want to prevent a node from servicing reads, consider using
  /core/replica-set-hidden-member instead.
