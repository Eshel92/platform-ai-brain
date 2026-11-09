<!-- Converted from reference/command/appendOplogNote.txt (reStructuredText). Includes are inlined. -->

# appendOplogNote (database command)

## Definition

**`appendOplogNote`**

Writes a non-operational entry to the oplog.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

You can only run the `appendOplogNote` command on the `admin`
database.

The command has this syntax:

```javascript
db.adminCommand(
   {
      appendOplogNote: 1,
      data: <document>
   }
)
```

### Command Fields

| Field | Type | Description |
|---|---|---|
| `appendOplogNote` | any | Set to any value. You can use `appendOplogNote` to advance the change stream highwatermark token timestamp on idle shards with infrequent writes. To learn more about resume token types, see change-stream-resume-token. |
| `data` | document | The document to append to the oplog. |

## Example

To append a non-operational entry to the oplog, use the
`db.adminCommand` method:

```javascript
db.adminCommand(
   {
      appendOplogNote: 1,
      data: {
         msg: "Appending test message to oplog"
      }
   }
)
```

Example `oplog` entry:

```json
{
   op: "n",
   ns: "",
   o: { 
      msg: "Appending test message to oplog"
   }, 
   ts: Timestamp({ t: 1689177321, i: 1 }), 
   t: Long("1"), 
   v: Long("2"),
   wall: ISODate("2023-07-12T15:55:21.180Z")
}
```
