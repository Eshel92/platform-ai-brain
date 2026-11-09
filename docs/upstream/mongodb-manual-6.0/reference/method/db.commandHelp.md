<!-- Converted from reference/method/db.commandHelp.txt (reStructuredText). Includes are inlined. -->

# db.commandHelp()

## Description

**`db.commandHelp(command)`**

Displays help text for the specified database command. See
the /reference/command.

The `db.commandHelp()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `command` | string | The name of a database command. |

          
          

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0, M2, M5, M10+, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
