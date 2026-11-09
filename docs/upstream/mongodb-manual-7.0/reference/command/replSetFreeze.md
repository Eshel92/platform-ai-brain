<!-- Converted from reference/command/replSetFreeze.txt (reStructuredText). Includes are inlined. -->

# replSetFreeze (database command)

## Definition

**`replSetFreeze`**

The `replSetFreeze` command prevents a replica set
member from seeking election for the specified number of
seconds. Use this command in conjunction with the
`replSetStepDown` command to make a different node in
the replica set a primary.

**Tip:**

In `mongosh`, this command can also be run through the `rs.freeze` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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
     replSetFreeze: <seconds> 
   }
)
```

## Behavior

If you want to unfreeze a replica set member before the specified number
of seconds has elapsed, you can issue the command with a seconds
value of `0`:

```javascript
db.runCommand(
   { 
     replSetFreeze: 0 
   }
)
```

Restarting the `mongod` process also unfreezes a replica
set member.

`replSetFreeze` is an administrative command, and you
must issue it against the admin database.
