<!-- Converted from reference/method/cursor.itcount.txt (reStructuredText). Includes are inlined. -->

# cursor.itcount()

## Definition

**`cursor.itcount()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Counts the number of documents remaining in a cursor.

`itcount()` is similar to `cursor.count()`, but
actually executes the query on an existing iterator, exhausting its contents
in the process.

The `itcount()` method has the following
prototype form:

```javascript
db.collection.find(<query>).itcount()
```

**See also:**

`cursor.count()`

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
