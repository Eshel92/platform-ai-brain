<!-- Converted from reference/method/js-cursor.txt (reStructuredText). Includes are inlined. -->

# Cursor Methods

**Note:** `mongosh` Methods

The methods listed on this table of contents page are
`mongosh` methods.  This is *not* the documentation for
`Node.js` or other programming language specific driver methods.

In most cases, `mongosh` methods work the same way as the
legacy `mongo` shell methods. However, some legacy methods
are unavailable in `mongosh`.

For MongoDB API drivers, refer to the language specific
`MongoDB driver` documentation.

These methods modify the way that the underlying query is executed.

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

| Name | Description |
|---|---|
| `cursor.addOption()` | Adds special wire protocol flags that modify the behavior of the query. |
| `cursor.allowDiskUse()` | Allows MongoDB to use temporary files on disk to store data exceeding the 100 megabyte system memory limit while processing an in-memory sort operation. |
| `cursor.allowPartialResults()` | Allows `db.collection.find()` operations against a sharded collection to return partial results, rather than an error, if one or more queried shards are unavailable. |
| `cursor.batchSize()` | Controls the number of documents MongoDB will return to the client in a single network message. |
| `cursor.close()` | Close a cursor and free associated server resources. |
| `cursor.isClosed()` | Returns `true` if the cursor is closed. |
| `cursor.collation()` | Specifies the collation for the cursor returned by the `db.collection.find()`. |
| `cursor.comment()` | Attaches a comment to the query to allow for traceability in the logs and the system.profile collection. |
| `cursor.count()` | Modifies the cursor to return the number of documents in the result set rather than the documents themselves. |
| `cursor.explain()` | Reports on the query execution plan for a cursor. |
| `cursor.forEach()` | Applies a JavaScript function for every document in a cursor. |
| `cursor.hasNext()` | Returns true if the cursor has documents and can be iterated. |
| `cursor.hint()` | Forces MongoDB to use a specific index for a query. |
| `cursor.isExhausted()` | Returns `true` if the cursor is closed *and* there are no objects remaining in the batch. |
| `cursor.itcount()` | Computes the total number of documents in the cursor client-side by fetching and iterating the result set. |
| `cursor.limit()` | Constrains the size of a cursor's result set. |
| `cursor.map()` | Applies a function to each document in a cursor and collects the return values in an array. |
| `cursor.max()` | Specifies an exclusive upper index bound for a cursor. For use with `cursor.hint()` |
| `cursor.maxAwaitTimeMS()` | Specifies a limit in milliseconds to wait for the next query result update. |
| `cursor.maxTimeMS()` | Specifies a cumulative time limit in milliseconds for processing operations on a cursor. |
| `cursor.min()` | Specifies an inclusive lower index bound for a cursor. For use with `cursor.hint()` |
| `cursor.next()` | Returns the next document in a cursor. |
| `cursor.noCursorTimeout()` | Instructs the server to avoid closing a cursor automatically after a period of inactivity. |
| `cursor.objsLeftInBatch()` | Returns the number of documents left in the current cursor batch. |
| `cursor.pretty()` | Configures the cursor to display results in an easy-to-read format. |
| `cursor.readConcern()` | Specifies a read concern for a `find()` operation. |
| `cursor.readPref()` | Specifies a read preference to a cursor to control how the client directs queries to a replica set. |
| `cursor.returnKey()` | Modifies the cursor to return index keys rather than the documents. |
| `cursor.showRecordId()` | Adds an internal storage engine ID field to each document returned by the cursor. |
| `cursor.size()` | Returns a count of the documents in the cursor after applying `skip()` and `limit()` methods. |
| `cursor.skip()` | Returns a cursor that begins returning results only after passing or skipping a number of documents. |
| `cursor.sort()` | Returns results ordered according to a sort specification. |
| `cursor.tailable()` | Marks the cursor as tailable. Only valid for cursors over capped collections. |
| `cursor.toArray()` | Returns an array that contains all documents returned by the cursor. |
| `cursor.tryNext()` | Returns the next element in the iteration if available or else null. |
