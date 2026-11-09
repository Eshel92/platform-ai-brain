<!-- Converted from reference/command/setAuditConfig.txt (reStructuredText). Includes are inlined. -->

# setAuditConfig

## Definition

**`setAuditConfig`**

**New in version:** 5.0

`setAuditConfig` is an administrative command that
sets new audit configurations for `mongod` and
`mongos` server instances at runtime.

Use the `db.adminCommand( { command } )` 
method to run `setAuditConfig` against the `admin` 
database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     setAuditConfig: 1, 
     filter: <Filter Document>,
     auditAuthorizationSuccess: <Boolean> 
   }
)
```

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `setAuditConfig` | integer | Run `setAuditConfig` |
| `filter` | document | An audit filter |
| `auditAuthorizationSuccess` | boolean | Log all, or only failed access authorizations |

 

## Behavior

Enable Auditing to use
`setAuditConfig` at runtime.

`auditAuthorizationSuccess` enables auditing of authorization success for the authCheck action. The parameter value must be
`true` to audit read and write operations. However, when
`auditAuthorizationSuccess` is `false` auditing has less
performance impact because the audit system only
logs authorization failures.

Configuration updates are distributed via the oplog mechanism
which means updates on `mongod` nodes are distributed to
secondary nodes very quickly. There is a different distribution
mechanism on `mongos` nodes. `mongos` nodes
have to `poll` the primary
server at regular intervals for configuration updates. You may see
stale data due to polling delay if you run `setAuditConfig`
on the primary server and `getAuditConfig` on a
shard before the shard has polled the primary server
for updated configuration details.

## Examples

In these examples the audit messages have been reformatted. They appear
on a single line in the log file.

### Audit Collection Creation and Deletion

Enable auditing when a collection is created or deleted.

```javascript
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter:
         {
            atype:
               {
                  $in: [ "createCollection", "dropCollection" ]
               }
         },
      auditAuthorizationSuccess: false
   }
)
```

When the `inventory` collection is created in the `sales` database,
the audit system will log a message like this:

```javascript
.. copyable: false

{
   "atype" : "createCollection",
   "ts" : { "$date" : "2021-08-09T13:45:05.372+00:00" },
   "uuid" : { "$binary" : "RKU/YLizS6K9se2GUU7ZVQ==", "$type" : "04" },
   "local" : { "ip" : "127.0.0.1", "port" : 27502 },
   "remote" : { "ip" : "127.0.0.1", "port" : 51918 },
   "users" : [],
   "roles" : [],
   "param" : { "ns" : "sales.inventory" },
   "result" : 0
}
```

When the `inventory` collection is dropped from the `sales`
database, the audit system will log a message like this:

```javascript
.. copyable: false

{
   "atype" : "dropCollection",
   "ts" : { "$date" : "2021-08-09T13:45:00.661+00:00" },
   "uuid" : { "$binary" : "0gle4/pSQli+LUcz43ykag==", "$type" : "04" },
   "local" : { "ip" : "127.0.0.1", "port" : 27502 },
   "remote" : { "ip" : "127.0.0.1", "port" : 51928 },
   "users" : [],
   "roles" : [],
   "param" : { "ns" : "sales.inventory" },
   "result" : 0
}
```

### Audit Document Interactions

Set `auditAuthorizationSuccess` to `true` and create a
filter which includes actions of interest to audit read and write
operations.

```javascript
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter:
         {
            atype: "authCheck",
            "param.command":
               {
                  $in: [ "find", "insert", "delete", "update", "findandmodify" ]
               }
         },
      auditAuthorizationSuccess: true
   }
)
```

Search the `inventory` collection in the `sales` database using the
`find` command to create an audit log entry like this one:

```javascript
.. copyable: false

{
   "atype" : "authCheck",
   "ts" : { "$date" : "2021-08-09T15:28:10.788+00:00" },
   "uuid" : { "$binary" : "ngwRt5CRTZqgE4TsfleoqQ==", "$type" : "04" },
   "local" : { "ip" : "127.0.0.1", "port" : 27502 },
   "remote" : { "ip" : "127.0.0.1", "port" : 51930 },
   "users" : [],
   "roles" : [],
   "param" : {
      "command" : "find",
      "ns" : "sales.inventory",
      "args" : {
         "find" : "inventory",
         "filter" : { "widget" : 1 },
         "lsid" : { "id" : { "$binary" : "FNWNxiitQ8GHKrHx8eJSbg==", "$type" : "04" } },
         "$clusterTime" : { "clusterTime" : { "$timestamp" : { "t" : 1628521381, "i" : 1 } },
         "signature" : { "hash" : { "$binary" : "AAAAAAAAAAAAAAAAAAAAAAAAAAA=", "$type" : "00" },
         "keyId" : { "$numberLong" : "0" } } },
         "$db" : "sales"
      }
   },
   "result" : 0
}
```

**See also:**

`db.adminCommand`, `getAuditConfig`,
configure audit filters
