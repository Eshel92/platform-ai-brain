<!-- Converted from reference/command/getLastError.txt (reStructuredText). Includes are inlined. -->

:orphan:

# getLastError (database command)

**`getLastError`**

Removed in MongoDB 5.1. 

Any code explicitly using `getLastError`,  `db.getLastError()`, or
`db.getLastErrorObj()` should instead use the CRUD API to issue the
write with the desired write concern.
Information about the success or failure of the write operation will be
provided directly by the driver as a return value.

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
