<!-- Converted from reference/method/Mongo.getReadPrefTagSet.txt (reStructuredText). Includes are inlined. -->

# Mongo.getReadPrefTagSet()

**`Mongo.getReadPrefTagSet()`**

:returns: The current read preference tag set for the
          `Mongo()` connection object.

See /core/read-preference for an introduction to read
preferences and tag sets in MongoDB. Use
`getReadPrefTagSet()` to return the current read
preference tag set, as in the following example:

```javascript
db.getMongo().getReadPrefTagSet()
```

Use the following operation to return and print the current read
preference tag set:

```javascript
printjson(db.getMongo().getReadPrefTagSet());
```

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
