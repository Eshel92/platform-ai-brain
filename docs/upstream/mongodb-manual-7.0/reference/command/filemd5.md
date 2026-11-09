<!-- Converted from reference/command/filemd5.txt (reStructuredText). Includes are inlined. -->

# filemd5 (database command)

**Important:** Deprecated command

This command is deprecated and its use is discouraged as MD5 is no
longer considered cryptographically secure.

## Definition

**`filemd5`**

The `filemd5` command returns the md5 hash for a single
file stored using the GridFS specification. Client libraries
use this command to verify that files are correctly written to MongoDB.
The command takes the `files_id` of the file in question and the
name of the GridFS root collection as arguments. 

## Compatibility

This command is available in deployments hosted in the following environments: 

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

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     filemd5: ObjectId("4f1f10e37671b50e4ecd2776"), 
     root: "fs" 
   }
)
```

MongoDB computes the `filemd5` using all data in the GridFS file object
pulled sequentially from each chunk in the `chunks` collection.
