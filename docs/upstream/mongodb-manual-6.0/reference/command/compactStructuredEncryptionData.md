<!-- Converted from reference/command/compactStructuredEncryptionData.txt (reStructuredText). Includes are inlined. -->

# compactStructuredEncryptionData

## Definition

**`compactStructuredEncryptionData`**

Compacts documents specified in the state collections and deletes 
redundant documents.

## Compatibility

This command is available in deployments hosted in the following environments: 

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
   

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
  {
    compactStructuredEncryptionData: <collection>,
    compactionTokens: {
       encryptedFieldPath: bindata,
       ...
    },
  }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `compactStructuredEncryptionData` | string | The name of the collection. |
| `compactionTokens` | document | A document that maps index fields to compaction tokens. |

   
The `mongosh` provides a wrapper method
`db.collection.compactStructuredEncryptionData()`.

## Required Access

The built-in roles `readWriteAnyDatabase` and 
`dbOwner` provide 
`compactStructuredEncryptionData` actions on resources.

## Example

See index compaction for an example.
