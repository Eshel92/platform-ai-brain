<!-- Converted from reference/command/replSetGetConfig.txt (reStructuredText). Includes are inlined. -->

# replSetGetConfig

## Definition

**`replSetGetConfig`**

Returns a document that describes the current configuration of the replica set. 

**Tip:**

In `mongosh`, this command can also be run through the `rs.conf` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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

To run, `replSetGetConfig` must be issued against the
`admin` database. The command has the following syntax:

```javascript
db.adminCommand( 
   {
     replSetGetConfig: 1,
     commitmentStatus: <boolean>,
     comment: <any>
   } 
)
```

## Command Fields

| Field | Type | Description |
|---|---|---|
| `replSetGetConfig` | any | Any value |
| commitmentStatus | boolean | .. _replSetGetConfig-commitmentStatus: Optional. Specify `true` to include a commitmentStatus field in the output. The commitmentStatus output field indicates whether the replica set's previous reconfig has been committed, so that the replica set is ready to be reconfigured again. For details, see commitmentStatus Output Field. You can only specify `commitmentStatus: true` option when running the command on the primary. The command errors if run with `commitmentStatus: true` on a secondary. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

`mongosh` provides the `rs.conf()` method
that wraps the `replSetGetConfig` command:

```javascript
rs.conf();
```

## Output Example

The following is an example output of the `replSetGetConfig`
command run with commitmentStatus: true on the primary:

```javascript
{
   "config" : {
      "_id" : "myRepl",
      "version" : 180294,
      "term" : 1,
      "protocolVersion" : NumberLong(1),
      "writeConcernMajorityJournalDefault" : true,
      "members" : [
         {
            "_id" : 0,
            "host" : "m1.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : NumberLong(0),
            "votes" : 1
         },
         {
            "_id" : 1,
            "host" : "m2.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : NumberLong(0),
            "votes" : 1
         },
         {
            "_id" : 2,
            "host" : "m3.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {

            },
            "secondaryDelaySecs" : NumberLong(0),
            "votes" : 1
         }
      ],
      "settings" : {
         "chainingAllowed" : true,
         "heartbeatIntervalMillis" : 2000,
         "heartbeatTimeoutSecs" : 10,
         "electionTimeoutMillis" : 10000,
         "catchUpTimeoutMillis" : -1,
         "catchUpTakeoverDelayMillis" : 30000,
         "getLastErrorModes" : {

         },
         "getLastErrorDefaults" : {
            "w" : 1,
            "wtimeout" : 0
         },
         "replicaSetId" : ObjectId("5eaa1e9ac4d650aa7817623d")
      }
   },
   "commitmentStatus" : true, 
   "ok" : 1,
   "$clusterTime" : {
      "clusterTime" : Timestamp(1588212091, 1),
      "signature" : {
         "hash" : BinData(0,"veOHa2mOeRTzuR0LKqnzGxWV77k="),
         "keyId" : NumberLong("6821298283919441923")
      }
   },
   "operationTime" : Timestamp(1588212091, 1)
}
```

* - Field

  - Description

* - `config`

  - The replica set configuration. For description of each
    configuration settings, see
    /reference/replica-configuration.

* - commitmentStatus

  - .. _replSetGetConfig-output-commitmentStatus:

    A boolean that indicates whether the most recent replica set
    configuration has been committed; i.e.

    - The most recent replica set configuration for the primary has
      propagated to a majority of members, and 

    - The last write operation to the replica set with the previous
      configuration has been `majority-commited` in the new
      configuration.

    If `true`, then the configuration has been committed, and the
    replica set can be reconfigured. To reconfigure the replica set,
    see `replSetReconfig` command or the
    `mongosh` method `rs.reconfig()`.

    If `false`, then the configuration has not been committed, and
    the replica set cannot be reconfigured.

* - `ok`

  - A number that indicates whether the command has succeeded (`1`) or
    failed (`0`).

* - | `operationTime` 
    | `$clusterTime`

  - Returned with every command for a replica set. See
    db.adminCommand Response for
    details.

**See also:**

- `rs.conf()`
- `rs.reconfig()`
