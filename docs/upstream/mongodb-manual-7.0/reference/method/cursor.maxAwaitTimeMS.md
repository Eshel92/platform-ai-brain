<!-- Converted from reference/method/cursor.maxAwaitTimeMS.txt (reStructuredText). Includes are inlined. -->

# cursor.maxAwaitTimeMS() (mongosh method)

## Definition

**`cursor.maxAwaitTimeMS(<time limit>)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Specifies the maximum time for the server to wait for new documents
that match a tailable cursor
query on a capped collection. For
more information on iterating a cursor returned by a query, see:
read-operations-cursors.

The `maxAwaitTimeMS()` method has the following
prototype form:

```javascript
db.collection.find(
   { <query> },
   { <projection> }
).tailable( { awaitData: true } ).maxAwaitTimeMS( <milliseconds> )
```

The `maxAwaitTimeMS()` method has the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| `milliseconds` | integer | Specifies a maximum wait time for new documents. |

**Important:**

This method, `maxAwaitTimeMS()`, sets a limit on how
long a tailable cursor waits
for the next response. `maxTimeMS()` sets a limit on
total processing time.

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

## Example

Query the capped `sales` collection
to find agent Mary Kay's weekly sales totals:

```javascript
db.sales.find( 
   { agent: "Mary Kay" },
   { _id: 0, agent: 1, weeklyTotal: 1  }
).tailable( { awaitData: true } ).maxAwaitTimeMS( 1000 )
```

The highlighted line creates a tailable cursor on the `sales` collection. The
`maxAwaitTimeMS()` sets a one second maximum wait time
for the next cursor update.
