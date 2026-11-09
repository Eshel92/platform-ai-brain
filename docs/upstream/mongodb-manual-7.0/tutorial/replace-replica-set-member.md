<!-- Converted from tutorial/replace-replica-set-member.txt (reStructuredText). Includes are inlined. -->

# Replace a Self-Managed Replica Set Member

If you need to change the hostname of a replica set member without
changing the configuration of that member or the set, you can use the
operation outlined in this tutorial. For example if you must
re-provision systems or rename hosts, you can use this pattern to
minimize the scope of that change.

## Operation

To change the hostname for a replica set member modify the
`members[n].host` field. The value of
`members[n]._id` field will not change
when you reconfigure the set.

See /reference/replica-configuration and
`rs.reconfig()` for more information.

**Note:**

Any replica set configuration change can trigger the current
primary to step down, which forces an election. During the election, the current shell
session and clients connected to this replica set disconnect,
which produces an error even when the operation succeeds.

## Example

To change the hostname to `mongo2.example.net` for the replica set
member configured at `members[0]`, issue the following sequence of
commands:

```javascript
cfg = rs.conf()
cfg.members[0].host = "mongo2.example.net"
rs.reconfig(cfg)
```
