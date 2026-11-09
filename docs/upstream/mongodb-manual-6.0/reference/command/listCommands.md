<!-- Converted from reference/command/listCommands.txt (reStructuredText). Includes are inlined. -->

# listCommands

## Definition

**`listCommands`**

The `listCommands` command generates a list of all
database commands implemented for the current `mongod` or
`mongos` instance.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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
     listCommands: 1 
   } 
)
```
