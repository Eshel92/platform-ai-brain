<!-- Converted from reference/method/Mongo.getDBs.txt (reStructuredText). Includes are inlined. -->

# Mongo.getDBs() (mongosh method)

## Description

**`Mongo.getDBs()`**

Returns information about all available databases.
`Mongo.getDBs()` uses the `listDatabases`
command.

The `Mongo.getDBs()` method doesn't take any parameters.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

To list the available databases and metadata for the local MongoDB
instance:

```javascript
db.getMongo().getDBs()
```

The `db.getMongo()` method returns the connection to the
current MongoDB instance. The `Mongo.getDBs()` output
resembles:

```javascript
{
 databases: [
   { name: 'admin', sizeOnDisk: Long("225280"), empty: false },
   { name: 'config', sizeOnDisk: Long("212992"), empty: false },
   { name: 'local', sizeOnDisk: Long("2400256"), empty: false },
   { name: 'test', sizeOnDisk: Long("303104"), empty: false }
 ],
 totalSize: Long("3141632"),
 totalSizeMb: Long("2"),
 ok: 1,
 '$clusterTime': {
   clusterTime: Timestamp({ t: 1640186473, i: 1 }),
   signature: {
     hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
     keyId: Long("0")
   }
 },
 operationTime: Timestamp({ t: 1640186473, i: 1 })
 } 
```

The databases are listed in the highlighted lines.
