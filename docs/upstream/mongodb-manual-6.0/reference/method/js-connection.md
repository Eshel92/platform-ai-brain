<!-- Converted from reference/method/js-connection.txt (reStructuredText). Includes are inlined. -->

# Connection Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

| Name | Description |
|---|---|
| /reference/method/connect | Connects to a MongoDB instance and to a specified database on that instance. |
| `Mongo()` | Creates a new connection object. |
| `Mongo.getDB()` | Returns a database object. |
| `Mongo.getDBNames()` | Returns a list of databases. |
| `Mongo.getDBs()` | Returns a document with a list of databases and metadata. |
| `Mongo.getReadPrefMode()` | Returns the current read preference mode for the MongoDB connection. |
| `Mongo.getReadPrefTagSet()` | Returns the read preference tag set for the MongoDB connection. |
| `Mongo.getWriteConcern` | Returns the write concern for the connection object. |
| `Mongo.setCausalConsistency()` | Enables or disables causal consistency on the connection object. |
| `Mongo.setReadPref()` | Sets the read preference for the MongoDB connection. |
| `Mongo.setWriteConcern` | Sets the write concern for the connection object. |
| `Mongo.startSession()` | Starts a session on the connection object. |
| `Mongo.watch()` | Opens a change stream cursor for a deployment to report on all its non-`system` collections across all its databases, excluding the internal `admin`, `local`, and `config` databases. |
| `Session` | The session object. |
| `SessionOptions` | The options object for the session. |
