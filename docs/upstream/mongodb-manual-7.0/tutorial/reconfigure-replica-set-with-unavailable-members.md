<!-- Converted from tutorial/reconfigure-replica-set-with-unavailable-members.txt (reStructuredText). Includes are inlined. -->

# Reconfigure Self-Managed Replica Set for Unavailable Members

To reconfigure a replica set when a **majority** of
members are available, use the `rs.reconfig()`
operation on
the current primary, following the example in the
Replica Set Reconfiguration Procedure.

This document provides steps for re-configuring a
replica set when *only* a **minority** of members are accessible.

You may need to use the procedure, for example, in a
geographically distributed replica set, where *no* local group of
members can reach a majority. See replica-set-elections for more
information on this situation.

## Reconfigure by Forcing the Reconfiguration

This procedure lets you recover while a majority of replica set
members are down or unreachable. You connect to any surviving member and
use the `force` option to the `rs.reconfig()`  method.

The `force` option forces a new configuration onto the member. Use this procedure only to
recover from catastrophic interruptions. Do not use `force` every
time you reconfigure. Also, do not use the `force` option in any automatic
scripts and do not use `force` when there is still a primary.

**Warning:**

Force reconfiguration can result in unexpected behavior, 
including rollback of
`"majority"` committed writes.

To force reconfiguration:

1. Back up a surviving member.

#. Connect to a surviving member and save the current configuration.
   Consider the following example commands for saving the configuration:

   ```javascript
   cfg = rs.conf()

   printjson(cfg)
   ```

#. On the same member, remove the down and unreachable members of the
   replica set from the `members` array by
   setting the array equal to the surviving members alone. Consider the
   following example, which uses the `cfg` variable created in the
   previous step:

   ```javascript
   cfg.members = [cfg.members[0] , cfg.members[4] , cfg.members[7]]
   ```

#. On the same member, reconfigure the set by using the
   `rs.reconfig()` command with the `force` option set to
   `true`:

   ```javascript
   rs.reconfig(cfg, {force : true})
   ```

   This operation forces the secondary to use the new configuration. The
   configuration is then propagated to all the surviving members listed
   in the `members` array. The replica set then elects a new primary.

   **Note:**

   When you use `force : true`, the version number in the replica
   set configuration increases significantly, by tens or hundreds
   of thousands. This is normal and designed to prevent set version
   collisions if you accidentally force re-configurations on both
   sides of a network partition and then the network partitioning
   ends.

#. If the failure or partition was only temporary, shut down or
   decommission the removed members as soon as possible.

**See also:**

/tutorial/resync-replica-set-member
