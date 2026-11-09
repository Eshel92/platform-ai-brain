<!-- Converted from reference/method/rs.printSecondaryReplicationInfo.txt (reStructuredText). Includes are inlined. -->

# rs.printSecondaryReplicationInfo() (mongosh method)

## Definition

**`rs.printSecondaryReplicationInfo()`**

Prints a formatted report of the replica set status from the
perspective of the secondary member of the set. The output is
identical to `db.printSecondaryReplicationInfo()`.

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

## Output

Example `rs.printSecondaryReplicationInfo()` output when run on a replica set with two secondary
members:

```javascript
source: m1.example.net:27002
{
  syncedTo: 'Mon Mar 01 2021 16:30:50 GMT-0800 (PST)',
  replLag: '0 secs (0 hrs) behind the primary '
}
---
source: m2.example.net:27003
{
  syncedTo: 'Mon Mar 01 2021 16:30:50 GMT-0800 (PST)',
  replLag: '0 secs (0 hrs) behind the primary '
}
```

**Note:**

The `rs.printSecondaryReplicationInfo()` method run in `mongosh` does
**not** return JSON. Use `rs.printSecondaryReplicationInfo()` for manual inspection, and
`rs.status()` in scripts.

A delayed member may show as `0`
seconds behind the primary when the inactivity period on the primary is
greater than the `members[n].secondaryDelaySecs` value.

A member may show a negative time value behind the primary when `rs.printSecondaryReplicationInfo()`
is run. This is expected if `rs.printSecondaryReplicationInfo()` is run after a secondary replicates
a write that follows a period of inactivity, but before the secondary
receives a heartbeat from the primary with the latest optime.

**Note:**

The lag reported by secondaries may not be representative of cluster
health. Negative values do not indicate that the secondary is ahead
of the primary.

To obtain the most current status for your replica set, run `rs.printSecondaryReplicationInfo()`
on the primary.
