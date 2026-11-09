<!-- Converted from reference/method/Mongo.getDB.txt (reStructuredText). Includes are inlined. -->

# Mongo.getDB() (mongosh method)

## Description

**`Mongo.getDB(<database>)`**

Provides access to database objects from
`mongosh` or from a JavaScript file.

The `Mongo.getDB()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `database` | string | The name of the database to access. |

                  

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

The following example instantiates a new connection to the MongoDB
instance running on the localhost interface and returns a reference
to `"myDatabase"`:

```javascript
db = new Mongo().getDB("myDatabase");
```

**See also:**

`Mongo()` and /reference/method/connect
