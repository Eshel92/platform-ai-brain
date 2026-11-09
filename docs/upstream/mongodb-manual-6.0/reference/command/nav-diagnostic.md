<!-- Converted from reference/command/nav-diagnostic.txt (reStructuredText). Includes are inlined. -->

# Diagnostic Commands

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

| Name | Description |
|---|---|
| `buildInfo` | Displays statistics about the MongoDB build. |
| `collStats` | Reports storage utilization statics for a specified collection. |
| `connPoolStats` | Reports statistics on the outgoing connections from this MongoDB instance to other MongoDB instances in the deployment. |
| `connectionStatus` | Reports the authentication state for the current connection. |
| `dataSize` | Returns the data size for a range of data. For internal use. |
| `dbHash` | Returns hash value a database and its collections. |
| `dbStats` | Reports storage utilization statistics for the specified database. |
| `explain` | Returns information on the execution of various operations. |
| `getCmdLineOpts` | Returns a document with the run-time arguments to the MongoDB instance and their parsed options. |
| `getLog` | Returns recent log messages. |
| `hostInfo` | Returns data that reflects the underlying host system. |
| `listCommands` | Lists all database commands provided by the current `mongod` instance. |
| `lockInfo` | Internal command that returns information on locks that are currently being held or pending. Only available for `mongod` instances. |
| `ping` | Internal command that tests intra-deployment connectivity. |
| `profile` | Interface for the database profiler. |
| `serverStatus` | Returns a collection metrics on instance-wide resource utilization and status. |
| `top` | Returns raw usage statistics for each database in the `mongod` instance. |
| `validate` | Internal command that scans for a collection's data and indexes for correctness. |
| `validateDBMetadata` | Checks that the stored metadata of a database/collection is valid within a particular API version. |
| `whatsmyuri` | Internal command that returns information on the current client. |
