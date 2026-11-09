<!-- Converted from troubleshooting/backup-restore-failures.txt (reStructuredText). Includes are inlined. -->

# Troubleshoot Backup and Restore Failures

	:local:
	:backlinks: none
	:depth: 2
	:class: singlecol

Backup and restore operations for deployments managed by Ops Manager
can fail for a variety of reasons, including agent connectivity issues, disk
space constraints, or oplog inconsistencies.

This page describes how to confirm backup and restore failures, outlines common
causes and resolutions, and provides guidance on what to collect before
contacting support. If the issue persists after you complete the steps below,
contact technical-support.

## Prerequisite Checks

Before you investigate the root cause of a backup or restore failure, confirm
that a failure has occurred by checking the relevant status indicators in the
Ops Manager UI or API.

### Check for Backup Failures

Use the following methods to confirm that a backup job or snapshot has failed.

#### Check Snapshot Status

To confirm whether a snapshot failed:

**Step 1: Navigate to snapshots in the Ops Manager UI.**

a. Click Admin.
#. Click Backups.
#. Click Snapshots.

**Step 2: Search for the replica set or deployment.**

**Step 3: Review the State column.**

The column shows whether the snapshot succeeded, is running, or failed.

You can also click JSON next to a snapshot to view additional
fields, including:

- `status`
- `createdDate`
- `completedDate`
- `totalDuration`
- `transferSpeed`

These fields help confirm whether the backup completed successfully.

For a description of all snapshot states, see
`Backup Overview`.

#### Check the Backup Jobs Page

To check for issues with ongoing backup jobs:

**Step 1: Navigate to the Backup Jobs page.**

a. Click Admin.
#. Click Backup.
#. Click Jobs.

**Step 2: Find your replica set or cluster.**

**Step 3: Look for highlighted fields.**

Fields such as Last Snapshot, Last Oplog, or
Head Time might appear highlighted when delayed, indicating a
problem with the backup process.

For more information, see `Jobs`.

#### Check Backup Logs

To review error messages from backup jobs:

**Step 1: Navigate to logs.**

a. Click Admin.
#. Click Logs.

**Step 2: Filter for backup jobs.**

The logs display error messages grouped by time, which can help diagnose why a
backup job failed.

#### Check Alerts

Ops Manager generates alerts that indicate failures or issues with backup jobs,
including:

- "Backup has reached a high number of retries"
- "Backup is in an unexpected state"
- "Replica set has a late snapshot"

For a full list of backup-related alert conditions, see
`Alert Conditions`.

#### Query the API for Incomplete Snapshots

To retrieve snapshots that have not completed, query the Ops Manager API using
the `completed=false` query parameter:

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots?completed=false"
```

The response includes a `results` array where each object represents a
snapshot. The `complete` field indicates whether the snapshot finished
successfully.

**Note:**

The snapshot API does not provide a named failure status. A snapshot
with `complete: false` may still be in progress or may have failed.

For more information, see
`Get All Snapshots for One Cluster`.

### Check for Restore Failures

Use the following methods to confirm that a restore job has failed.

#### Check the Restores Page

To view the status of restore jobs in the Ops Manager UI:

**Step 1: Click Deployment.**

**Step 2: Click your cluster or replica set.**

**Step 3: Click the Backup tab.**

**Step 4: Click Restores.**

The Restores page shows a table of the last 300 restore jobs. Check
the Status column to identify jobs with the following states:

- `FAILED`
- `CANCELED`
- `IN_PROGRESS`
- `FINISHED`

Click a row to view more details about that specific restore operation.

For more information, see `Restores`.

#### Query the API for Failed Restore Jobs

To retrieve restore jobs programmatically, query the Ops Manager API:

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs"
```

The response includes a `results` array where each object represents a
restore job. The `statusName` field indicates the job state. Possible values
include:

- `FINISHED`
- `IN_PROGRESS`
- `BROKEN`
- `KILLED`

Restore jobs with a `statusName` of `BROKEN` or `KILLED` are considered
failed.

To filter for failed jobs using `jq`:

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs" \
  | jq '.results[] | select(.statusName=="BROKEN" or .statusName=="KILLED")'
```

For more information, see
`Get All Restore Jobs for One Cluster`.

## Common Issues and Resolutions

The following sections describe common causes of backup and restore failures and
how to resolve them.

### Backup Failures

The following sections describe common causes of backup failures and how to
resolve them.

#### Insufficient Disk Space

A lack of free disk space on the replica set member nodes can cause the
cluster to enter an unhealthy state, leading to backup failures.

To resolve this issue, increase the available storage capacity on the `dbPath`
of the affected nodes. Monitor disk usage regularly to prevent recurrence.

#### MongoDB Agent Is Down or Unstable

The backup process depends on the MongoDB Agent running continuously. If the
agent stops or keeps restarting, backups fail.

Symptoms include:

- Alerts such as "Backup oplog is behind"
- No oplog slices received for an hour

To resolve this issue:

**Step 1: Verify that the agent process is running on the host.**

**Step 2: Check the agent logs.**

The agent logs are typically located at:

```bash
/var/log/mongodb-mms-automation/backup-agent.log
```

**Step 3: Fix any permission issues or configuration errors causing restarts.**

For more information, see
`Fix Backup Oplog Issues`.

#### Agent Cannot Reach the Replica Set

The backup agent must maintain a connection to the replica set. Failures can
occur due to network connectivity issues, an unavailable MongoDB node, or an
authentication failure.

Symptoms in the agent logs include:

- `server selection timeout`
- `Authentication failed`

To resolve this issue:

**Step 1: Test connectivity from the backup agent host.**

```bash
mongosh "mongodb://host:port"
```

**Step 2: Verify network access and credentials.**

Confirm the following:

- Network access between the agent host and replica set members
- Replica set availability
- Backup user credentials and required roles

For more information, see
`Fix Backup Oplog Issues`.

#### Oplog Issues

If the oplog is too small or the backup agent cannot keep up with write
activity, the backup falls behind and eventually fails.

Symptoms include the following alerts:

- "Backup requires a resync"
- "Backup oplog is behind"

To resolve this issue:

- Increase the oplog size so the oplog window covers enough history (a minimum
  of 24 hours is recommended).
- If the backup has fallen too far behind, resync the backup.

#### Backup Job Fails to Bind to a Backup Daemon

A backup job requires a Backup Daemon with enough space to store a local
copy of the backed-up replica set. If no daemon has sufficient space, the
job fails to bind. To resolve this issue, add an additional Backup Daemon
to increase capacity.

This issue can also occur when no primary is detected in the replica set.
To resolve this, ensure the replica set is healthy and has a primary before
you retry the backup.

For more information, see
`Backup FAQ`.

### Restore Failures

The following sections describe common causes of restore failures and how to
resolve them.

#### Attempting to Restore a Single Shard in a Sharded Cluster

When you restore a sharded cluster, you must restore all shards. The restore
process fails if you attempt to restore a single shard in isolation.

For more information, see
`Restore Limitations`.

#### Mismatched Settings Between Backup and Target Database

An automated restore can fail when certain storage settings of the source backup
and the target database do not match. If a restore attempt fails, Ops Manager
displays any mismatched settings.

For a list of settings that must match, see
`Potential Causes for Automated Restore Failure`.

#### Oplog Gaps During Point-in-Time Restore

Point-in-time restores require a continuous oplog history. If there is a gap in
the oplog, the restore fails.

Common causes of oplog gaps include:

- The backup agent stopped tailing the oplog.
- The oplog rolled over before the agent processed it.
- Cluster topology changes occurred.
- A Feature Compatibility Version (FCV) change occurred.
- A restore was attempted across MongoDB version changes.

To resolve this issue:

- Restore from the latest valid snapshot taken before the oplog gap, or
- Wait until a new snapshot is created, then perform the restore again.

For more information, see
`Restore from a Specific Point in Time`.

#### Insufficient Disk Space on the Restore Host

If the target host does not have enough storage for the snapshot files and
restored database, the restore fails.

To resolve this issue:

**Step 1: Check the size of the database you are restoring.**

```javascript
db.stats()
```

**Step 2: Ensure sufficient disk space on the target host.**

Verify that the `dbPath` has enough free disk space to accommodate the
restored data before proceeding.

For more information about the `dbStats` command, see `dbStats`.

## Diagnostics to Collect for More Support

If the issue persists, collect the following information before contacting
technical-support:

- Complete error messages from the Ops Manager UI or API
- Backup agent log files
- MongoDB server version
- Ops Manager version
- Relevant MongoDB server logs
- Output from the Restores page or API restore job query

## Related Issues

- manual-troubleshooting-replica-set-no-primary
- manual-troubleshooting-replication-lag

## Learn More

- `Backup Overview`
- `Restore Overview`
- `Fix Backup Oplog Issues`
