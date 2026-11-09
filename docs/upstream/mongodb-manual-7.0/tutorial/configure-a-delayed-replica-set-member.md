<!-- Converted from tutorial/configure-a-delayed-replica-set-member.txt (reStructuredText). Includes are inlined. -->

# Configure a Delayed Self-Managed Replica Set Member

To configure a delayed secondary member, set its
`members[n].priority` value to `0`, its
`members[n].hidden` value to `true`, and
its `members[n].secondaryDelaySecs` value to the
number of seconds to delay.

**Important:**

The length of the secondary
`members[n].secondaryDelaySecs` must
fit within the window of the oplog. If the oplog is shorter than
the `members[n].secondaryDelaySecs`
window, the delayed member cannot successfully replicate
operations.

When you configure a delayed member, the delay
applies both to replication and to the member's oplog. For
details on delayed members and their uses, see
/core/replica-set-delayed-member.

## Example

The following example sets a 1-hour delay on a secondary member
currently at the index `0` in the
`members` array. To set the delay, issue
the following sequence of operations in a `mongosh` session
that is connected to the primary:

```javascript
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[0].hidden = true
cfg.members[0].secondaryDelaySecs = 3600
rs.reconfig(cfg)
```

After the replica set reconfigures, the delayed secondary member cannot
become primary and is hidden from applications. The
`members[n].secondaryDelaySecs` value delays both
replication and the member's oplog by 3600 seconds (1 hour).

When updating the replica configuration object, access the replica set
members in the `members` array with the
**array index**. The array index begins with `0`. Do **not** confuse
this index value with the value of the
`members[n]._id` field in each document in
the `members` array.

**Warning:**

- The `rs.reconfig()` shell method can force the current
  primary to step down, which causes an election. When the primary steps down, the
  `mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.

- .. include:: /includes/warning-mixed-version-rs-config.rst

## Related Documents

- `members[n].secondaryDelaySecs`

- Replica Set Reconfiguration

- replica-set-oplog-sizing

- /tutorial/change-oplog-size tutorial

- /core/replica-set-elections
