<!-- Converted from tutorial/adjust-replica-set-member-priority.txt (reStructuredText). Includes are inlined. -->

# Adjust Priority for a Self-Managed Replica Set Member

## Overview

The `priority` settings of replica set members affect both the timing
and the outcome of elections for
primary. Higher-priority members are more likely to call elections, and
are more likely to win. Use this setting to ensure that some members are
more likely to become primary and that others can never become primary.

The value of the member's
`priority` setting determines the
member's `priority` in elections. The higher the number,
the higher the priority.

## Considerations

To modify priorities, you update the `members`
array in the replica configuration object. The array index begins with
`0`. Do **not** confuse this index value with the value of the replica
set member's `members[n]._id` field in the
array.

The value of `priority` can be any
floating point (i.e. decimal) number between `0` and `1000`. The
default value for the `priority` field is `1`.

To block a member from seeking election as primary, assign it a priority
of `0`. Hidden members and
delayed members have
`priority` set to `0`. 

Arbiters have priority `0`. 

Adjust priority settings during a scheduled maintenance window.
Reconfiguring priority can force the current primary to step down,
leading to an election. Before an election, the primary closes all open
client connections.

### Priority and Votes

`members[n].priority` and `members[n].votes`
have the following relationship:

- .. include:: /includes/fact-rs-non-voting-priority-restriction.rst

- .. include:: /includes/fact-rs-nonzero-priority-vote-restriction.rst

As such, increasing a non-voting member's `priority`
*requires* setting `votes` to `1` and increases
the number of voting replica set members. Before increasing the 
priority of a non-voting member, consider the following:

- MongoDB replica sets can have no more than 
  `7 voting members`.
  If the replica set already has 7 voting members, you cannot modify the
  priority of any remaining members in the replica set to be greater
  than `0`.

- Replica reconfiguration can add or remove no more than *one* voting member at 
  a time. To change multiple non-voting members to have a priority greater than 
  `0`, issue a series of `replSetReconfig` or 
  `rs.reconfig()` operations to modify one member at a time. See
  replSetReconfig-cmd-single-node for more information.

## Procedure

**Warning:**

- The `rs.reconfig()` shell method can force the current
  primary to step down, which causes an election. When the primary steps down, the
  `mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.

- .. include:: /includes/warning-mixed-version-rs-config.rst

**Step 1: Copy the replica set configuration to a variable.**

In `mongosh`, use `rs.conf()` to retrieve
the replica set configuration and assign it to a variable. For
example:

```javascript
cfg = rs.conf()
```

**Step 2: Change each member's priority value.**

Change each member's `members[n].priority`
value, as configured in the `members`
array.

```javascript
cfg.members[0].priority = 0.5
cfg.members[1].priority = 2
cfg.members[2].priority = 2
```

This sequence of operations modifies the value of `cfg` to set the
priority for the first three members defined in the
`members` array.

**Step 3: Assign the replica set the new configuration.**

Use `rs.reconfig()` to apply the new configuration.

```javascript
rs.reconfig(cfg)
```

This operation updates the configuration of the replica set using
the configuration defined by the value of `cfg`.
