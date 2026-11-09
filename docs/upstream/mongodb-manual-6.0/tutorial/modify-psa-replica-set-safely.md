<!-- Converted from tutorial/modify-psa-replica-set-safely.txt (reStructuredText). Includes are inlined. -->

# Modify a Self-Managed PSA Replica Set Safely

## Overview

When reconfiguring primary-secondary-arbiter (PSA) replica sets or
changing to a PSA architecture, you need to take special care in the
following cases:

- You want to reconfigure a secondary in an existing three-member
  replica set with a PSA architecture to become a voting, data-bearing
  node with a non-zero priority.
- You want to add a new voting, data-bearing node with a non-zero
  priority to an existing two-member replica set that contains one
  primary and one arbiter.

**Warning:**

If the secondary you are adding is lagged and the resulting replica
set is a PSA configuration, the first configuration change will
change the number of nodes that need to commit a change with
`"majority"`. In this case, your commit point will lag
until the secondary has caught up.

This document outlines the procedure for reconfiguring your replica set
in these specific cases **without** using the designated helper method
`rs.reconfigForPSASet`.

## Procedure

If you are performing one of the preceding operations, it is necessary
to reconfigure your replica set in two steps:

1. Reconfigure the replica set to add or modify a secondary with
   `{ votes: 1, priority: 0 }`.
2. Once the added or modified secondary has caught up with all
   committed writes, reconfigure the secondary to have a non-zero
   priority `{ votes: 1, priority: <num> }`.

The two-step approach avoids the possibility of rolling back
committed writes in the case of a failover to the new secondary
before the new secondary has all committed writes from the previous
primary.

To run the `rs.reconfigForPSASet()` method, you must connect
to the primary of the replica set.

**Step 1: Add or modify a secondary with votes 1 but priority 0**

To avoid rolling back uncommitted writes when adding or changing a
voting, data-bearing node, it is required that you add the node with
`{ priority: 0 }` first.

In `mongosh`, modify the replica set configuration. To
reconfigure an existing replica set, first retrieve the current
configuration with `rs.conf()`, modify the configuration
document as needed, and then pass the modified document to
`rs.reconfig()`:

```javascript
cfg = rs.conf();
cfg["members"] = [
  {
     // existing member or members
  },
  {
     "_id" : <num>,  // The array position of the new member in the
                     // ``members`` array.
     "host" : <host>,
     "arbiterOnly" : false,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 0,
     "tags" : { <tags> },
     "secondaryDelaySecs" : <num>,
     "votes" : 1
  },
  {
     // existing member or members
  }
]
rs.reconfig(cfg);
```

**Step 2: Reconfigure the secondary to have non-zero priority**

Once the secondary is caught up, set the prority to the desired
number. Before this reconfiguration succeeds, the secondary must
replicate all the writes that were committed when it had zero votes.
This is automatically checked when you issue the
`rs.reconfig()` command.

```javascript
cfg = rs.conf();
cfg["members"] = [
  {
     // existing member or members
  },
  {
     "_id" : <num>,  // The array position of the new member in the
                     // ``members`` array.
     "host" : <host>,
     "arbiterOnly" : false,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : <num>,
     "tags" : { <tags> },
     "secondaryDelaySecs" : <num>,
     "votes" : 1
  },
  {
     // existing member or members
  }
]
rs.reconfig(cfg);
```
