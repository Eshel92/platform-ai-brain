<!-- Converted from reference/method/cursor.batchSize.txt (reStructuredText). Includes are inlined. -->

# cursor.batchSize()

## Definition

**`cursor.batchSize(size)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The maximum number of documents that can be returned in each batch of a query result.
By default, the initial batch size is the lesser of `101` documents or 16 mebibytes (MiB) worth of
documents. Subsequent batches have a maximum size of 16 MiB. This option
can enforce a smaller limit than 16 MiB, but not a larger one. When set, the `batchSize` is the lesser
of `batchSize` documents or 16 MiB worth of documents.

A `batchSize` of `0` means that the cursor is established, but no documents 
are returned in the first batch. 

**Note:**

If the batch size is too large, the cursor allocates more
resources than it requires, which can negatively impact
query performance.  If the batch size is too small, the
cursor requires more network round trips to retrieve the
query results, which can negatively impact query
performance.

Adjust `batchSize` to a value appropriate to your
database, load, and application needs.

The `batchSize()` method takes the
following field:

| Field | Type | Description |
|---|---|---|
| `size` | integer | The maximum number of documents that can be returned in each batch of a query result. The default initial batch size is the lesser or `101` documents or 16 mebibytes (MiB) worth of documents. Subsequent batches have a maximum size of 16 MiB. This option can enforce a smaller limit than 16 MiB, but not a larger one. The default applies to drivers and Mongo Shell. For details, see cursor-batches. |

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

## Example

The following example sets `batchSize` for the results of a query
(specifically, `find()`) to `10`:

```javascript
db.inventory.find().batchSize(10)
```

## Learn More

- cursor-batches
- `cursor.next()`
- `getMore`
