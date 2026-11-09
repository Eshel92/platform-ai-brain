<!-- Converted from reference/command/getAuditConfig.txt (reStructuredText). Includes are inlined. -->

# getAuditConfig (database command)

## Definition

**`getAuditConfig`**

**New in version:** 5.0

`getAuditConfig` is an administrative command that
retrieves audit configurations from `mongod` and
`mongos` server instances.

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
     getAuditConfig: 1 
   } 
)
```

## Behavior

Auditing must be enabled to use
`getAuditConfig`.

Nodes that are not participating in a runtime audit configuration
return their current configuration file settings for
`auditLog.filter` and `setParameter.auditAuthorizationSuccess`.

Nodes that are participating in the runtime audit synthesize their
current configuration from memory. Configuration updates are
distributed via the oplog mechanism which means updates on
`mongod` nodes are distributed to secondary nodes very
quickly. However, the distribution mechanism is different on
`mongos` nodes. `mongos` nodes have to 
`poll` the primary server
at regular intervals for configuration updates. You may see stale data
due to polling delay if you run `setAuditConfig` on the
primary server and `getAuditConfig` on a shard before the shard has polled the primary server
for updated configuration details.

**Note:**

If you are writing automated audit scripts, note that the quoting
style and the types used to represent the cluster signature differ
between `mongosh` and the legacy `mongo` shell. In `mongosh`
the types are Binary and Long. The corresponding types in the legacy
shell are BinData and NumberLong.

```javascript
// mongosh
signature: {
   hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
   keyId: Long("0")
}

// mongo
"signature" : {
```

			      "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			      "keyId" : Long(0)
		    }

## Examples

Run `getAuditConfig` on the `admin` database .

```javascript
db.adminCommand({getAuditConfig: 1})
```

The example server is configured to audit read and write operations. It
has a filter which captures the desired operations and the
`auditAuthorizationSuccess` value has been set to `true`.

```javascript
{
  generation: ObjectId("60e73e74680a655705f16525"),
  filter: {
    atype: 'authCheck',
    'param.command': {
      '$in': [ 'find', 'insert', 'delete', 'update', 'findandmodify' ]
    }
  },
  auditAuthorizationSuccess: true,
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp(1, 1625767540),
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
    }
  },
  operationTime: Timestamp(1, 1625767540)
}
```

**See also:**

`db.adminCommand`, `setAuditConfig`,
configure audit filters
