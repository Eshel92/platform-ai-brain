<!-- Converted from reference/command/ping.txt (reStructuredText). Includes are inlined. -->

# ping (database command)

## Definition

**`ping`**

The `ping` command is a no-op used to test whether a
server is responding to commands. This command will return
immediately even if the server is write-locked:

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     ping: 1 
   }
)
```

The value (e.g. `1` above) does not impact the behavior of the
command.
