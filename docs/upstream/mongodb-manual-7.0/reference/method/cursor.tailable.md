<!-- Converted from reference/method/cursor.tailable.txt (reStructuredText). Includes are inlined. -->

# cursor.tailable() (mongosh method)

## Definition

**`cursor.tailable()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Marks the cursor as tailable
keeping it open even when the client exhausts all results.

For use against a capped collection only. Using 
`tailable()` against a non-capped collection returns an error.

`cursor.tailable()` uses the following syntax:

```javascript
cursor.tailable( { awaitData : <boolean> } )
```

`~cursor.tailable()` has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `awaitData` | boolean | Optional. For use with `DBQuery.Option.tailable`. Sets the cursor to block the query thread when no data is available and await data for a set time instead of immediately returning no data. The cursor returns no data only if the timeout expires. By default, if `maxTimeMS` is set on the command that created the cursor, then the timeout for `awaitData` is the remaining time. Otherwise, the default timeout is 1000 milliseconds. You can set a timeout when running `getMore` on a cursor with `awaitData` enabled. Defaults to `false`. |

:returns:
   The cursor that `~cursor.tailable()` is attached to.

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

## Behavior

A tailable cursor performs a collection scan over a capped collection. 
It remains open even after reaching the end of the collection. 
Applications can continue to iterate the tailable cursor as 
new data is inserted into the collection.

If `awaitData` is `true`, when the cursor reaches the end of 
the capped collection, `mongod` blocks the query thread 
for the timeout interval and waits for new data to arrive. When new 
data is inserted into the capped collection, `mongod` signals the 
blocked thread to wake and return the next batch to the client.

See tailable-cursors-landing-page.
