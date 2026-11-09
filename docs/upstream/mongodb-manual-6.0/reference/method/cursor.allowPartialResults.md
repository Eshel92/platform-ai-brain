<!-- Converted from reference/method/cursor.allowPartialResults.txt (reStructuredText). Includes are inlined. -->

# cursor.allowPartialResults()

## Definition

**`cursor.allowPartialResults()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

When used with `db.collection.find()` operations against a
sharded collection, returns partial results, rather than an error,
if one or more queried shards are unavailable.

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

## Syntax

The `cursor.allowPartialResults()` method has the following
syntax:

```javascript
db.collection.find(<query>, <projection>).allowPartialResults()
```
