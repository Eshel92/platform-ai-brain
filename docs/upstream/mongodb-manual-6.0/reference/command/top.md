<!-- Converted from reference/command/top.txt (reStructuredText). Includes are inlined. -->

# top

**`top`**

`top` is an administrative command that returns usage statistics 
for each collection. You can use `top` metrics to compare the 
relative performance of your collections against each other.

**Important:**

The `top` command must be run against a
mongod instance. Running
`top` against a mongos
instance returns an error. 

## Definition

   
For every collection, `top` returns the amount of `time`, in 
microseconds, that each event takes to execute and a 
`count` of how many times each event has executed. The `time` and 
`count` metrics reset only after you restart your `mongod` 
instance.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

Issue the `top` command against the admin database:

```javascript
db.runCommand(
   { 
     top: 1 
   }
)
```

## Event Fields

The `top` command returns usage statistics for the following event 
fields: 

| Field | Description |
|---|---|
| `total` | The combination of all `readLock` and `writeLock` operations. |
| `readLock` | Usage statistics for operations that use read locks. These operations include but are not limited to queries and aggregations. |
| `writeLock` | Usage statistics for operations that use write locks. These operations include but are not limited to inserting, updating, and removing documents. |
| `queries` | Usage statistics for query operations such as `find`. The `queries.time` and `queries.count` fields also update `readLock.time` and increment `readLock.count`. |
| `getmore` | Usage statistics for `getMore` operations. |
| `insert` | Usage statistics for `insert` operations. The `insert.time` and `insert.count` fields also update `writeLock.time` and increment `writeLock.count`. |
| `update` | Usage statistics for `update` operations. The `update.time` and `update.count` fields also update `writeLock.time` and increment `writeLock.count`. |
| `remove` | Usage statistics for `delete` operations. The `remove.time` and `remove.count` fields also update `writeLock.time` and increment `writeLock.count`. |
| `commands` | Usage statistics for operations such as aggregations, index creation, and index removal. Depending on the type of command, the `commands.time` and `commands.count` fields update the `writeLock` fields or the `readLock` fields. For example, aggregation operations increment `readLock.time` and `readLock.count`. Index creation increments `writeLock.time` and `writeLock.count`. |

## Example

The output of the `top` command resembles the following output:

```javascript
{
  "totals" : {
     note: "all times in microseconds",
     "records.users" : {
                  "total" : {
                          "time" : 305277,
                          "count" : 2825
                  },
                  "readLock" : {
                          "time" : 305264,
                          "count" : 2824
                  },
                  "writeLock" : {
                          "time" : 13,
                          "count" : 1
                  },
                  "queries" : {
                          "time" : 305264,
                          "count" : 2824
                  },
                  "getmore" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "insert" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "update" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "remove" : {
                          "time" : 0,
                          "count" : 0
                  },
                  "commands" : {
                          "time" : 0,
                          "count" : 0
                  }
          }
}
```

## Learn More

- faq-concurrency-locking
