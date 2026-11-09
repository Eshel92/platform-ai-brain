<!-- Converted from reference/method/rs.conf.txt (reStructuredText). Includes are inlined. -->

# rs.conf() (mongosh method)

## Definition

**`rs.conf()`**

Returns a document that contains the current replica set
configuration.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetGetConfig` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `replSetGetConfig` command
can specify a new option commitmentStatus: true when run on the primary. When
run with the option, the command includes in the output a
commitmentStatus
field. This output field indicates whether the replica set's
previous reconfig has been committed, so that the replica set is
ready to be reconfigured again. The option is only available with the `replSetGetConfig`

command.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Output Example

The following document provides a representation of a replica set
configuration document. The configuration of your replica set may
include only a subset of these settings:

```none
{
  _id: <string>,
  version: <int>,
  term: <int>,
  protocolVersion: <number>,
  writeConcernMajorityJournalDefault: <boolean>,
  configsvr: <boolean>,
  members: [
    {
      _id: <int>,
      host: <string>,
      arbiterOnly: <boolean>,
      buildIndexes: <boolean>,
      hidden: <boolean>,
      priority: <number>,
      tags: <document>,
      secondaryDelaySecs: <int>,
      votes: <number>
    },
    ...
  ],
  settings: {
    chainingAllowed : <boolean>,
    heartbeatIntervalMillis : <int>,
    heartbeatTimeoutSecs: <int>,
    electionTimeoutMillis : <int>,
    catchUpTimeoutMillis : <int>,
    getLastErrorModes : <document>,
    getLastErrorDefaults : <document>,
    replicaSetId: <ObjectId>
  }
}
```

For description of the configuration settings, see
/reference/replica-configuration.

**`rs.config()`**

`rs.config()` is an alias of `rs.conf()`.
