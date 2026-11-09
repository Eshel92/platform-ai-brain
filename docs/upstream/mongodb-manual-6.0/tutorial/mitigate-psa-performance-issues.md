<!-- Converted from tutorial/mitigate-psa-performance-issues.txt (reStructuredText). Includes are inlined. -->

# Mitigate Performance Issues with a Self-Managed PSA Replica Set

## Overview

In a three-member replica set with a primary-secondary-arbiter (PSA)
architecture or a sharded cluster with three-member PSA shards, a
data-bearing node that is down or lagged can lead to performance issues.

If one data-bearing node goes down, the other node becomes the primary.
Writes with `w:1 <` continue to succeed in this
state but writes with write concern `"majority"` cannot
succeed and the commit point starts to lag. If your PSA replica set
contains a lagged secondary and your replica set requires two nodes to
majority commit a change, your commit point also lags.

With a lagged commit point, two things can affect your cluster
performance:

- The storage engine keeps **all** changes that happen after the commit
  point on disk to retain a durable history. The extra I/O from
  these writes tends to increase over time. This can greatly impact
  write performance and increase cache pressure.
- MongoDB allows the oplog to grow past its
  configured size limit to avoid deleting the `majority commit
  point`.

To reduce the cache pressure and increased write traffic, set
`votes: 0` and `priority: 0` for the node that is unavailable or lagging. For
write operations issued with "majority", only voting members are
considered to determine the number of nodes needed to perform a majority
commit. Setting the configuration of the node to `votes: 0` reduces the number of nodes required to commit a
write with write concern `"majority"` from two to one and
allows these writes to succeed.

Once the secondary is caught up, you can use the
`rs.reconfigForPSASet()` method to set `votes` back to `1`.

**Note:**

In earlier versions of MongoDB,
`enableMajorityReadConcern` and
`--enableMajorityReadConcern` were configurable allowing you
to disable the default read concern `"majority"` which
had a similar effect.

## Procedure

To reduce the cache pressure and increased write traffic for a
deployment with a three-member primary-secondary-arbiter (PSA)
architecture, set `{ votes: 0, priority: 0 }` for the secondary that
is unavailable or lagging:

```javascript
cfg = rs.conf();
cfg["members"][<array_index>]["votes"] = 0;
cfg["members"][<array_index>]["priority"] = 0;
rs.reconfig(cfg);
```

If you want to change the configuration of the secondary later, use the
`rs.reconfigForPSASet()` method.
