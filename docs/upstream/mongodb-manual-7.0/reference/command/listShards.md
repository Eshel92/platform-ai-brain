<!-- Converted from reference/command/listShards.txt (reStructuredText). Includes are inlined. -->

# listShards (database command)

## Definition

**`listShards`**

The `listShards` command returns a list of the configured
shards in a sharded cluster. `listShards` is only
available on `mongos` instances and must be issued against
the `admin` database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
  { 
    listShards: 1 
  }
)
```

## Example

The following operation runs `listShards` against the
`mongos` `admin` database:

```javascript
db.adminCommand({ listShards: 1 })
```

The following document is an example of the output from a
`listShards` command:

```javascript
{
  "shards": [
    {
      "_id": "shard01",
      "host": "shard01/host1:27018,host2:27018,host3:27018",
      "state": 1
    },
    {
      "_id": "shard02",
      "host": "shard02/host4:27018,host5:27018,host6:27018",
      "tags": [ "NYC" ],
      "state": 1
    },
    {
      "_id": "shard03",
      "host": "shard03/host7:27018,host8:27018,host9:27018",
      "state": 1
    }
  ],
  "ok": 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510716515, 1),
     "signature" : {
        "hash" : BinData(0,"B2ViX7XLzFLS5Fl9XEuFXbwKIM4="),
        "keyId" : Long("6488045157173166092")
     }
  },
  "operationTime" : Timestamp(1510716515, 1)
}
```

## Output

`listShards` returns a document that includes:

- A `shards` field which contains an array of documents, each
  describing one shard. Each document may contain the following fields:

  | Field | Description |
  |---|---|
  | `_id` | The name of the shard. |
  | `host` | The hostname of the shard. If the shard is a replica set, `host` lists the hostname of each mongod instance in the replica set. |
  | `draining` | If true, indicates that /reference/command/removeShard has been called for this shard and it is in the process of being drained. |
  | `tags` | A list of zones to which the shard belongs. |
  | `state` | An internal field used during the /reference/command/addShard sequence to ensure that all steps and configuration necessary to add the shard to the cluster are completed. |

- The `ok` status field, the `operationTime` field, and the
  `$clusterTime` field for the operation. For details on these
  fields, see command-response.
