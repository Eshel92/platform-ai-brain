<!-- Converted from reference/method/cursor.close.txt (reStructuredText). Includes are inlined. -->

# cursor.close()

## Definition

**`cursor.close()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Instructs the server to close a cursor
and free associated server resources. The server will automatically close
cursors that have no remaining results, as well as cursors that have been
idle for a period of time and lack the `cursor.noCursorTimeout()`
option.

The `close()` method has the following
prototype form:

```javascript
db.collection.find(<query>).close()
```

## Compatibility

This method is available in deployments hosted in the following environments: 

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
