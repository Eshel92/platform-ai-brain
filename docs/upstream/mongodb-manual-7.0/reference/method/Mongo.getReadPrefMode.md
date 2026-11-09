<!-- Converted from reference/method/Mongo.getReadPrefMode.txt (reStructuredText). Includes are inlined. -->

# Mongo.getReadPrefMode() (mongosh method)

**`Mongo.getReadPrefMode()`**

:returns: The current read preference mode for the
          `Mongo()` connection object.

See /core/read-preference for an introduction to read
preferences in MongoDB. Use `getReadPrefMode()` to
return the current read preference mode, as in the following
example:

```javascript
db.getMongo().getReadPrefMode()
```

Use the following operation to return and print the current read
preference mode:

```javascript
print(db.getMongo().getReadPrefMode());
```

This operation will return one of the following read preference
modes:

- `primary`
- `primaryPreferred`
- `secondary`
- `secondaryPreferred`
- `nearest`

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**See also:**

- /core/read-preference
- `readPref()`
- `setReadPref()`
- `getReadPrefTagSet()`
