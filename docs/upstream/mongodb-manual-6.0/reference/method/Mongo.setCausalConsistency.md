<!-- Converted from reference/method/Mongo.setCausalConsistency.txt (reStructuredText). Includes are inlined. -->

# Mongo.setCausalConsistency()

## Definition

**`Mongo.setCausalConsistency(<boolean>)`**

Enables or disables causal consistency
on the connection object. Causal consistency is disabled on the
connection object by default.

**Note:**

The `Mongo` connection object may have causal consistency
disabled even though sessions may have causal consistency enabled
or vice versa. See `Mongo.startSession()`.

To enable causal consistency for the connection object, call the
method without any argument:

```javascript
var conn = Mongo("localhost:27017");
conn.setCausalConsistency();
```

The method also can accept a boolean argument:

- `true` to enable causal consistency:

  ```javascript
  conn.setCausalConsistency(true);
  ```

- `false` to disable causal consistency:

  ```javascript
  conn.setCausalConsistency(false);
  ```

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

The following `mongosh` operation enables causal
consistency on the `Mongo` connection object associated with
`mongosh`'s global `db` variable:

```javascript
db.getMongo().setCausalConsistency();
```

**See also:**

- `db.getMongo()`
