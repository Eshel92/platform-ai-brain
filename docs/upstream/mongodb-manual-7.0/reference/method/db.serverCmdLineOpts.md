<!-- Converted from reference/method/db.serverCmdLineOpts.txt (reStructuredText). Includes are inlined. -->

# db.serverCmdLineOpts() (mongosh method)

**`db.serverCmdLineOpts()`**

Wraps the `getCmdLineOpts`
database command.

Returns a document that reports on the arguments and configuration
options used to start the `mongod` or `mongos` instance.

See configuration-options, `mongod`, and
`mongos` for additional information on
available MongoDB runtime options.

## Compatibility

This method is available in deployments hosted in the following environments: 

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
