<!-- Converted from tutorial/manage-chained-replication.txt (reStructuredText). Includes are inlined. -->

# Self-Managed Chained Replication

Starting in version 2.0, MongoDB supports chained replication. A
chained replication occurs when a secondary member replicates
from another secondary member instead of from the primary. This
might be the case, for example, if a secondary selects its replication
source based on ping time and if the closest member is another
secondary. The replication source for the operation is the
member from which the data is read.

Chained replication can reduce load on the primary. But chained
replication can also result in increased replication lag, depending on
the topology of the network.

You can use the `settings.chainingAllowed`
setting in /reference/replica-configuration to disable chained
replication for situations where chained replication is causing lag.

MongoDB enables chained replication by default. This procedure
describes how to disable it and how to re-enable it.

**Note:**

If you disable chained replication, the `replSetSyncFrom` command 
and `rs.syncFrom()` method have no effect.

## Disable Chained Replication

To disable chained replication, set the
`settings.chainingAllowed`
field in /reference/replica-configuration to `false`.

You can use the following sequence of commands to set
`settings.chainingAllowed` to
`false`:

1. Copy the configuration settings into the `cfg` object:

   ```javascript
   cfg = rs.config()
   ```

#. Take note of whether the current configuration settings contain the
   `settings` embedded document. If they do, skip this step.

   **Warning:** To avoid data loss, skip this step if the configuration

   settings contain the `settings` embedded document.

   If the current configuration settings **do not** contain the
   `settings` embedded document, create the embedded document by issuing the
   following command:

   ```javascript
   cfg.settings = { }
   ```

#. Issue the following sequence of commands to set
   `settings.chainingAllowed` to
   `false`:

   ```javascript
   cfg.settings.chainingAllowed = false
   rs.reconfig(cfg)
   ```

## Re-enable Chained Replication

To re-enable chained replication, set
`settings.chainingAllowed` to `true`.
You can use the following sequence of commands:

```javascript
cfg = rs.config()
cfg.settings.chainingAllowed = true
rs.reconfig(cfg)
```
