<!-- Converted from reference/method/sh.removeRangeFromZone.txt (reStructuredText). Includes are inlined. -->

# sh.removeRangeFromZone() (mongosh method)

## Definition

**`sh.removeRangeFromZone(namespace, minimum, maximum)`**

Removes the association between a range of shard key values and a
zone.

`sh.removeRangeFromZone()` takes the following fields:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the sharded collection to associate with the zone. The collection must be sharded for the operation to succeed. |
| `minimum` | document | The inclusive lower bound of the range of shard key values. Specify each field of the shard key in the form of `<fieldname> : <value>`. The value must be of the same BSON type or types as the shard key. |
| `maximum` | document | The exclusive upper bound of the range of shard key values. Specify each field of the shard key in the form of `<fieldname> : <value>`. The value must be of the same BSON type or types as the shard key. |

Use `sh.removeRangeFromZone()` to remove the association between
unused, out of date, or conflicting shard key ranges and a zone.

If no range matches the minimum and maximum bounds passed to
`sh.removeRangeFromZone()`, nothing is removed.

Only run `sh.removeRangeFromZone()` when connected to a
`mongos` instance.

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

## Behavior

`sh.removeRangeFromZone()` doesn't remove the association between
a zone and a shard. It also doesn't remove the zone itself.

See the zone manual page for more information on zones
in sharded clusters.

### Balancer

Removing the association between a range and a zone removes the constraints
keeping chunks covered by the range on the shards inside that zone. During the
next balancer round, the balancer may migrate chunks that were previously
covered by the zone.

See the documentation for the sharded cluster balancer for more information on how migrations work in a sharded
cluster.

### Security

For sharded clusters running with authentication, you
must authenticate as either:

- a user whose privileges include the specified actions on various
  collections in the `config` database:

  - `find` on the `config.shards` collection

  - `find`, `update`, and `remove`
    on the `config.tags` collection;
    
  or, alternatively

- a user whose privileges include `enableSharding` on the
  cluster resource.

The `clusterAdmin` or `clusterManager` built-in roles have
the appropriate permissions for running `sh.removeRangeFromZone()`.
See the documentation page for Role-Based Access Control for more information.

## Example

Given a sharded collection `exampledb.collection` with a shard key of ``{ a
: 1 }`, the following operation removes the range with a lower bound of `1``
and an upper bound of `10`:

```javascript
sh.removeRangeFromZone( "exampledb.collection",
                { a : 1 },
                { a : 10 }
              )
```

The `min` and `max` must match exactly the bounds of the target range.
The following operation attempts to remove the previously created range, but
specifies `{ a : 0 }` as the `min` bound:

```javascript
admin = db.getSiblingDB("admin")
admin.runCommand(
   {
      updateZoneKeyRange : "exampledb.collection",
      min : { a : 0 },
      max : { a : 10 },
      zone : null
   }
)
```

While the range of `{ a : 0 }` and `{ a : 10 }` encompasses the existing
range, it is not an exact match and therefore
`sh.removeRangeFromZone()` does not remove anything.

### Compound Shard Key

Given a sharded collection `exampledb.collection` with a shard key of 
`{ a : 1, b : 1 }`, the following operation removes the range with a lower
bound of `{ a : 1, b : 1}` and an upper bound of `{ a : 10, b : 10 }`:

```javascript
sh.removeRangeFromZone( "exampledb.collection",
                { a : 1, b : 1 },
                { a : 10, b : 10 }
              )
```

                 
Given the previous example, if there was an existing range with a lower bound
of `{ a : 1, b : 5 }` and an upper bound of `{ a : 10, b : 1 }`, the
operation would *not* remove that range, as it is not an exact match of the
minimum and maximum passed to `sh.removeRangeFromZone()`.
