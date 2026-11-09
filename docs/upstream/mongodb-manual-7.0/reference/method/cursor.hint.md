<!-- Converted from reference/method/cursor.hint.txt (reStructuredText). Includes are inlined. -->

# cursor.hint() (mongosh method)

## Definition

**`cursor.hint(index)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Call this method on a query to override MongoDB's default index
selection and query optimization process.
Use `db.collection.getIndexes()` to return the list of
current indexes on a collection.

The `cursor.hint()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `index` | string or document | The index to "hint" or force MongoDB to use when performing the query. Specify the index either by the index name or by the index specification document. You can also specify `{ $natural : 1 }` to force the query to perform a forwards collection scan, or `{ $natural : -1 }` for a reverse collection scan. |

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

- When an index filter exists for the query
  shape, MongoDB ignores the `hint()`.

- .. include:: /includes/fact-hint-text-query-restriction.rst

- If you use `hint()` on a hidden index or an index that doesn't exist, the operation
  returns an error.

- On a time series collections, you
  can only specify hints using the index name, not the index key
  pattern.

### $natural

**`$natural`**

Use `$natural` with `cursor.hint()` to perform a collection scan to
return documents in natural order.

For usage, see hint-collection-scans.

**Note:**

Prior to MongoDB 7.0, `$natural` accepts incorrect type values, 
such as `0`, `NaN`, "X", and `-0.01`. After MongoDB 7.0, if you pass any value 
other than `1` and `-1` to `$natural`, MongoDB returns an error. 

## Examples

### Specify an Index

The following example returns all documents in the collection named
`users` using the index on the `age` field.

```javascript
db.users.find().hint( { age: 1 } )
```

You can also specify the index using the index name:

```javascript
db.users.find().hint( "age_1" )
```

### Force Collection Scans

You can specify `{ $natural : 1 }` to force the query to perform a forwards
collection scan:

```javascript
db.users.find().hint( { $natural : 1 } )
```

You can also specify `{ $natural : -1 }` to force the query to perform a 
reverse collection scan:

```javascript
db.users.find().hint( { $natural : -1 } )
```

**See also:**

- /indexes
- /core/query-plans
- index-filters
