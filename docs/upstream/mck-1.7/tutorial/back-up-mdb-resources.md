<!-- Converted from tutorial/back-up-mdb-resources.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB Database Backups

You can configure continuous, automated backups for the MongoDB
databases that the Kubernetes Operator manages using the MongoDB custom
resource.

**Note:**

If you already configured backups for your MongoDB resources during
MongoDB database resource deployment, you don't need to complete the
following procedure.

## Considerations

Before you configure backups for MongoDB resources, see the following
considerations:

- If you set assignment labels using the Kubernetes Operator, the values that
  you set in the Kubernetes configuration file for assignment labels override
  the values defined in the `Ops Manager` UI. Assignment labels that you don't set
  using the Kubernetes Operator continue to use the values set in the `Ops Manager` UI.

- If you set a snapshot schedule field using the Kubernetes Operator, the value
  that you set in the Kubernetes configuration file for that field overrides
  the value defined in the `Ops Manager` UI. Snapshot schedule fields that you
  don't set using the Kubernetes Operator continue to use the value set in the
  `Ops Manager` UI.

  **Example:**

  - You set `backup.snapshotSchedule.snapshotIntervalHours=6` in
    the Kubernetes Operator.
  - You set the following values in the UI:

    - Snapshot Inverval: 10
    - Snapshot Retention Days: 5

  `Ops Manager` uses the following values for your deployment:

  - Snapshot Inverval: 6
  - Snapshot Retention Days: 5

- If you enable backups for your MongoDB database deployment using the 
  Kubernetes Operator, but you don't set a snapshot schedule using the 
  Kubernetes Operator, `Ops Manager` uses the snapshot schedule you set in the `Ops Manager` UI.
- If you enable backups for your MongoDB deployment, but you don't set
  a snapshot schedule at all, `Ops Manager` uses the default snapshot schedule.

## Prerequisites

Before you configure continuous backups for MongoDB resources, complete
the following tasks:

- Install the Kubernetes Operator.
- Deploy the Ops Manager application.
- Configure backups for the Ops Manager resource. In the linked procedure, see the
  steps for configuring backups. Continuous backups for MongoDB
  databases require that you set the `spec.backup.enabled`
  value in the Ops Manager resource specification to `true`.
- Deploy a replica set or a 
  sharded cluster.

## Procedure

**Step 1: Enable backups for your MongoDB database deployment.**

Add the `spec.backup.mode` setting to the config file for
your MongoDB database deployment and set its value to `enabled` as
shown in the following replica set example:

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
  name: <my-replica-set>
spec:
  members: 3
  version: "8.0.0"
  type: ReplicaSet
  opsManager:
    configMapRef:
      name: <my-project>
  credentials: <my-credentials>
  backup:
                      # Sets labels for the Backup Daemon.
    assignmentLabels: ["test1", "test2"]
    mode: enabled
```

To learn more about creating or editing a config file, see 
deploy a replica set or 
deploy a sharded cluster.

**Step 2: Set the snapshot schedule.**

Add any of the following snapshot schedule settings to the specification
file for the deployment. To learn how `Ops Manager` determines the snapshot
schedule if you don't set a snapshot schedule field using the Kubernetes Operator,]
see the considerations.

- `spec.backup.snapshotSchedule.snapshotIntervalHours`
- `spec.backup.snapshotSchedule.snapshotRetentionDays`
- `spec.backup.snapshotSchedule.dailySnapshotRetentionDays`
- `spec.backup.snapshotSchedule.weeklySnapshotRetentionWeeks`
- `spec.backup.snapshotSchedule.monthlySnapshotRetentionMonths`
- `spec.backup.snapshotSchedule.pointInTimeWindowHours`
- `spec.backup.snapshotSchedule.referenceHourOfDay`
- `spec.backup.snapshotSchedule.referenceMinuteOfHour`
- `spec.backup.snapshotSchedule.fullIncrementalDayOfWeek`
- `spec.backup.snapshotSchedule.clusterCheckpointIntervalMin`

**Step 3: Set the backup assignment labels.**

Add one or more `spec.backup.assignmentLabels` to the specification
file for the deployment. Use assignment labels to identify that specific
backup stores are associated with particular projects. Setting labels
in Kubernetes Operator overrides labels that you set in `Ops Manager`. To learn more,
see considerations.

See the example of the specification file with assignment labels earlier
in this procedure.

**Step 4: Check that the backup status is `STARTED`.**

Run the following command to check the status of the backups:

```sh
kubectl get mdb <resource-name> -n <metadata.namespace> -o yaml
```

The `status.backup.statusname` field indicates the status of the 
backup. The status displays `STARTED` when you successfully
configure backups.
