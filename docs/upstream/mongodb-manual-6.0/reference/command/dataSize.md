<!-- Converted from reference/command/dataSize.txt (reStructuredText). Includes are inlined. -->

# dataSize

## Definition

**`dataSize`**

The `dataSize` command returns the size in bytes for
the specified data.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

   

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     dataSize: <string>,
     keyPattern: <document>,
     min: <document>,
     max: <document>,
     estimate: <boolean>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `dataSize` | string | The name of the target collection. |
| `keyPattern` | document | Optional. The collection's key pattern to examine. The collection must have an index with the corresponding pattern. Otherwise `dataSize` returns an error message. |
| `min` | document | Optional. The lower bound of the key range to be examined. |
| `max` | document | Optional. The upper bound of the key range to be examined. |
| `estimate` | boolean | Optional. When `true`, `dataSize` estimates the data size by assuming that all documents in the specified range are uniformly sized as per the collection's average object size. The collection's average object size is obtained from the `avgObjSize` field in the output of the `collStats` command. Defaults to false. |

       

## Example

The following operation runs the `dataSize` command on the
`database.collection` collection, specifying a key pattern of `{field: 1}`
with the lower bound of the range of keys to be examined being `{field: 10}`
and the upper bound of the key to be examined being `{field: 100}`.

```javascript
db.runCommand({ dataSize: "database.collection", keyPattern: { field: 1 }, min: { field: 10 }, max: { field: 100 } })
```

This returns a document with the size in bytes for all matching
documents. Replace `database.collection` with the database and
collection from your deployment.

The amount of time required to return `dataSize` depends on the
amount of data in the collection.
