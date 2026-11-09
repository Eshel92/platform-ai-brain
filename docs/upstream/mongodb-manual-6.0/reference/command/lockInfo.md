<!-- Converted from reference/command/lockInfo.txt (reStructuredText). Includes are inlined. -->

# lockInfo

## Definition

**`lockInfo`**

Returns information on locks that are currently being held or
pending. `lockInfo` is an internal command available on
`mongod` instances only.

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
db.adminCommand( 
   { 
     lockInfo: 1 
   } 
)
```

## Output Example

The following is an example of the output from the
`lockInfo`:

```javascript
{
   "lockInfo" : [
      {
         "resourceId" : "{2305843009213693953: ParallelBatchWriterMode, 1}",
         "granted" : [
            {
               "mode" : "IS",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{6917529027641081857: Global, 1}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{4611686018427387905: ReplicationStateTransition, 1}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{10123292395995783581: Database, 899920359141007773, test}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      },
      {
         "resourceId" : "{12576221391967629173: Collection, 1047006345899159413, test.hugeindex}",
         "granted" : [
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "{ findandmodify: \"hugeindex\", query: { _id: 585.0 }, update: { $pop: { a: 1.0 } }, upsert: false, new: false, lsid: { id: UUID(\"dc611138-04c6-49b1-a7ac-161040dd9d65\") }, $db: \"test\" }",
               "clientInfo" : {
                  "desc" : "conn3",
                  "connectionId" : 3,
                  "client" : "127.0.0.1:55165",
                  "opid" : 28770
               }
            },
            {
               "mode" : "IX",
               "convertMode" : "NONE",
               "enqueueAtFront" : false,
               "compatibleFirst" : false,
               "debugInfo" : "index build: 29d48366-63ad-41e2-a689-69255a89c094",
               "clientInfo" : {
                  "desc" : "IndexBuildsCoordinatorMongod-0",
                  "opid" : 27437
               }
            }
         ],
         "pending" : [ ]
      }
   ],
   "ok" : 1
}
```

## Output Fields

**`lockInfo`**

An array of documents that report on the lock information. Each
document includes:

- `resourceId`

- `granted`

- `pending`

**`lockInfo.resourceId`**

The resource on which the locks are being held or pending.

**`lockInfo.granted`**

An array of documents. Each document provides information on
locks that are currently granted on the resource.

**`lockInfo.pending`**

An array of documents. Each document provides information on
locks that are currently pending on the resource.

### Lock Information

For each `granted` or `pending` lock
document, information include:

* - Field
  - Description

* - `mode`
  - Specifies the lock mode:

    | Lock Mode | Description |
    |---|---|
    | `S` | Shared |
    | `X` | Exclusive |
    | `IS` | Intent Shared |
    | `IX` | Intent Exclusive (IX) |

* - `convertMode`

  - Specifies the new lock mode for conversion.

* - `enqueueAtFront`

  - A boolean that indicates whether to put the lock at the front
    of the queue or the back in case of conflict.

* - `compatibleFirst`

  - A boolean that indicates to grant lock requests based on
    compatibility with already granted locks or to use the
    first-in-first-out (FIFO) order.

* - `debugInfo`

  - Information about the operation that issued the lock request.

* - `clientInfo`

  - A document detailing the client information.
