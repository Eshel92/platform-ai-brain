<!-- Converted from reference/api/snapshot-schedule.txt (reStructuredText). Includes are inlined. -->

# Snapshot Schedule

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

This resource allows you to view and configure various properties of snapshot
creation and retention for a replica set or cluster.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for edit-snapshot-schedule.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule | Get the snapshot schedule for an instance. `CLUSTER-ID` must be the ID of either a replica set or a sharded cluster. |
| PATCH | /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID}/snapshotSchedule | Change the parameters of snapshot creation and retention. Any combination of the snapshot schedule's attributes can be modified. `CLUSTER-ID` must be the ID of either a replica set or a sharded cluster |
