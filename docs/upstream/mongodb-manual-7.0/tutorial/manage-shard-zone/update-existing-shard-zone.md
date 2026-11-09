<!-- Converted from tutorial/manage-shard-zone/update-existing-shard-zone.txt (reStructuredText). Includes are inlined. -->

# Update an Existing Shard Zone

After you specify a range of values for a shard zone, you can update the
shard zone range if your application's requirements change.

To update an existing shard zone, perform these steps:

#. Stop the balancer.

#. Remove the old range from the zone.

#. Update the zone's range.

#. Restart the balancer.

## About this Task

- Zone ranges are inclusive of the lower boundary and exclusive of the
  upper boundary.

- After you modify a zone, the balancer must migrate chunks to the
  appropriate zones based on the new range of values. Until balancing
  completes, some chunks may reside on the wrong shard given the
  configured zones for the sharded cluster.

## Before you Begin

To complete this tutorial, you must deploy a sharded cluster with a sharded collection and create a zone
to modify.

This example uses a sharded collection named `users` in the
`records` database, sharded by the `zipcode` field. 

**Step 1: Add a shard to a zone called NYC**

```none
sh.addShardToZone(<shard name>, "NYC")
```

**Step 2: Specify a range of zipcode values for the NYC zone**

```javascript
sh.updateZoneKeyRange("records.users", { zipcode: "10001" }, { zipcode: "10281" }, "NYC" )
```

## Steps

The following procedure modifies the range of `zipcode` values for the
`NYC` zone to be `11201` through `11240`.

**Step 1: Stop the balancer**

```javascript
sh.stopBalancer()
```

**Step 2: Remove the current NYC range from the zone**

```javascript
sh.removeRangeFromZone("records.user", { zipcode: "10001" }, { zipcode: "10281" } )
```

**Step 3: Update the zone key range for the NYC zone**

```javascript
sh.updateZoneKeyRange("records.users", { zipcode: "11201" }, { zipcode: "11240" }, "NYC" )
```

**Step 4: Restart the balancer**

```javascript
sh.startBalancer()
```

## Learn More

- `sh.removeRangeFromZone()`

- `sh.updateZoneKeyRange()`

- workload-isolation
