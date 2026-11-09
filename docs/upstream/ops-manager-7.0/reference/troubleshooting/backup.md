<!-- Converted from reference/troubleshooting/backup.txt (reStructuredText). Includes are inlined. -->

# Backup

## Logs Display `MongodVersionException`

The `MongodVersionException` can occur if the
Backup Daemon\'s host cannot access the
internet to download the version or versions of MongoDB required
for the backed-up databases. Each database requires a version of
MongoDB that matches the database's version. Specifically, for each
instance you must run the latest stable release of that release
series.

If the Daemon runs without access to the internet, see
/tutorial/configure-local-mode to install the appropriate
binaries.

## Insufficient Oplog Size Error

If you have set the `mms.backup.minimumOplogWindowHours`, Ops Manager checks to see if the cluster's oplogs can store a given number of hours of data. It bases on recent oplog usage patterns from the last 24 hours.

If the oplogs lack capacity, the oplogs may have turned over
multiple times. This creates a gap between where a backup
ends and an oplog starts.

If this oplog size check fails:

- You cannot enable backups
- Ops Manager displays the following:

  **Warning:**

  Insufficient oplog size: The oplog window must be at least
  <duration> hours over the last 24 hours for all members of
  replica set <deploymentName>. Please increase the oplog.

If possible, wait to start a backup until the oplog has had
sufficient time to meet the size requirement.

**Warning:**

Do not change the minimum oplog size unless you are certain
smaller backups still provide useful backups.

MongoDB recommends only changing this value temporarily to permit
a test backup job to execute. The minimum oplog size value should
be reset to the default as soon as possible.

Understanding the risks given, you can start backups using this
changed minimum value. Once you pass the 24 hour mark, you should
reset this minimum value to preserve the sanity check for the
global Ops Manager installation going forward.
