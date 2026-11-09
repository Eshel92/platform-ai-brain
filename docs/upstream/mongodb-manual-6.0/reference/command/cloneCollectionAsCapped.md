<!-- Converted from reference/command/cloneCollectionAsCapped.txt (reStructuredText). Includes are inlined. -->

# cloneCollectionAsCapped

## Definition

**`cloneCollectionAsCapped`**

The `cloneCollectionAsCapped` command creates a new
capped collection from an existing, non-capped collection
within the same database. The operation does not affect the
original non-capped collection.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters or in serverless instances.
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
     cloneCollectionAsCapped: <existing collection>, 
     toCollection: <capped collection>,
     size: <capped size>,
     writeConcern: <document>,
     comment: <any>  
   }
)
```

### Command Fields

The command takes the following fields:

| Field | Description |
|---|---|
| cloneCollectionAsCapped | The name of the existing collection to copy. |
| toCollection | The name of the new capped collection to create. The name of the new capped collection must be distinct and cannot be the same as that of the original existing collection. |
| size | The maximum size,in bytes,  for the capped collection. |
| writeConcern | Optional. A document expressing the write concern of the `drop` command. Omit to use the default write concern. |
| `comment` | .. include:: /includes/extracts/comment-content.rst |

The command copies an `existing collection` and creates a new
`capped collection` with a maximum size specified by the ``capped
size`` in bytes.  

To replace the original non-capped collection with a
capped collection, use the `convertToCapped` command.

## Behavior

If the `capped size` is less than the size of the source collection,
then not all documents in the source collection will exist in the destination
capped collection.

This holds a database exclusive lock for the duration of the operation.
Other operations which lock the same database will be blocked until the
operation completes. See faq-concurrency-operations-locks for
operations that lock the database.
