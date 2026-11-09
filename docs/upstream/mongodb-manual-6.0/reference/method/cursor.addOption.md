<!-- Converted from reference/method/cursor.addOption.txt (reStructuredText). Includes are inlined. -->

# cursor.addOption()

## Definition

**`cursor.addOption(flag)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**Note:** Deprecated since v3.2

Starting in v3.2, the `cursor.addOption()` operator is
deprecated in `mongo`. Use available cursor
methods instead.

Used to change query behavior by setting the flags listed below.

The `cursor.addOption()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `flag` | flag | For `mongosh`, you can use the cursor flags listed below. For the driver-specific list, see your `driver documentation`. |

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

## Flags

`mongosh` provides several additional cursor flags to
modify the behavior of the cursor.

| Flag | Description |
|---|---|
| .. data:: DBQuery.Option.tailable | Sets the cursor not to close once the last data is received, allowing the query to continue returning data added after the initial results were exhausted. |
| .. data:: DBQuery.Option.slaveOk | Allows querying of a replica secondary. |
| .. data:: DBQuery.Option.noTimeout | Prevents the server from timing out idle cursors. |
| .. data:: DBQuery.Option.awaitData | For use with `DBQuery.Option.tailable`. Sets the cursor to block the query thread when no data is available and await data for a set time instead of immediately returning no data. The cursor returns no data only if the timeout expires. |
| .. data:: DBQuery.Option.exhaust | Sets the cursor to return all data returned by the query at once rather than splitting the results into batches. |
| .. data:: DBQuery.Option.partial | Sets the cursor to return partial data from a query against a sharded cluster in which some shards do not respond rather than throwing an error. |

## Example

The following example adds the `DBQuery.Option.tailable` flag and the
`DBQuery.Option.awaitData` flag to ensure that the query returns a
tailable cursor. The sequence
creates a cursor. After returning the full result set, it waits for the
default interval of 1000 milliseconds so that it can capture
and return additional data added during the query:

```javascript
var t = db.myCappedCollection;
var cursor = t.find().addOption(DBQuery.Option.tailable).
                      addOption(DBQuery.Option.awaitData)
```

**Warning:**

Adding incorrect wire protocol flags can cause problems and/or
extra server load.
