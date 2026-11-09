<!-- Converted from tutorial/configure-a-hidden-replica-set-member.txt (reStructuredText). Includes are inlined. -->

# Configure a Hidden Self-Managed Replica Set Member

Hidden members are part of a replica set but cannot become
primary and are invisible to client applications. Hidden members
may vote in elections. For
more information on hidden members and their uses, see
/core/replica-set-hidden-member.

## Considerations

The most common use of hidden nodes is to support 
backups. 

You can also use hidden nodes to support delayed
members. However, if you only need
to prevent a member from becoming primary, configure a 
priority 0 member.

If the `settings.chainingAllowed` setting
allows secondary members to sync from other secondaries, MongoDB by
default prefers non-hidden members over hidden members when selecting
a sync target. MongoDB will only choose hidden members as a last
resort. If you want a secondary to sync from a hidden member, use the
`replSetSyncFrom` database command to override the default
sync target. See the documentation for `replSetSyncFrom`
before using the command.

**See also:**

/tutorial/manage-chained-replication

## Examples

### Member Configuration Document

To configure a secondary member as hidden, set its
`members[n].priority` value to `0` and
set its `members[n].hidden` value to
`true` in its member configuration:

```javascript
{
  "_id" : <num>
  "host" : <hostname:port>,
  "priority" : 0,
  "hidden" : true
}
```

### Configuration Procedure

The following example hides the secondary member currently at the index
`0` in the `members` array. To configure
a hidden member, use the following sequence of operations in a
`mongosh` session that is connected to the primary,
specifying the member to configure by its array index in the
`members` array:

```javascript
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[0].hidden = true
rs.reconfig(cfg)
```

After re-configuring the set, this secondary member has a priority of
`0` so that it cannot become primary and is hidden. The other members
in the set will not advertise the hidden member in the
`hello` command or `db.hello()` method output.

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

- Replica Set Reconfiguration

- /core/replica-set-elections

- Read Preference
