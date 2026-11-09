<!-- Converted from reference/command/logApplicationMessage.txt (reStructuredText). Includes are inlined. -->

# logApplicationMessage

## Definition

**`logApplicationMessage`**

The `logApplicationMessage` command allows users to post
a custom message to the audit log. If
running with authorization, users must have `clusterAdmin`
role, or roles that inherit from `clusterAdmin`, to run
the command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
   

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {  
     logApplicationMessage: <string> 
   }
)
```

## Behavior

MongoDB associates these custom messages with the audit
operation `applicationMessage`,
and the messages are subject to any filtering.
