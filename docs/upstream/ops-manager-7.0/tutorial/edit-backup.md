<!-- Converted from tutorial/edit-backup.txt (reStructuredText). Includes are inlined. -->

# Edit a Backup's Settings

Available backup settings depend on the FCV value of your MongoDB database. 

To edit Backup's settings:

1. Click Continuous Backup.
2. Overview tab.
   Ops Manager lists all available backups.
3. Click ellipsis-h next to each backup to access its
   settings.

## Backup Settings Available to All FCV (Feature Compatibility Version)\s

### Edit Snapshot Schedule and Retention Policy

**Step 1: Click Continuous Backup.**

**Step 2: On the row for the process, click the backup's ellipsis icon, then click Edit Snapshot Schedule.**

**Step 3: Configure the snapshot settings.**

a. Enter the following information as needed.
   To learn about retention values, see snapshot-frequency-and-retention.

   * - Take snapshots every ... hours and save for ... days

     - Sets how frequently, in hours, Ops Manager takes a base snapshot of
       the deployment and the number of days Ops Manager retains base
       snapshots.

   * - Create cluster checkpoint every ... minutes
       (Sharded Clusters only)

     - Sets how frequently, in minutes, Ops Manager creates a
       checkpoint in between snapshots of a sharded cluster.
       Checkpoints provide restore points that you can use to create
       custom *point-in-time* snapshots.

       **Important:**

       You may use checkpoints for clusters that run MongoDB with
       Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
       MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

   * - Store daily snapshots for

     - Sets the number of days that Ops Manager retains daily snapshots.

   * - Store weekly snapshots for

     - Sets the number of weeks that Ops Manager retains weekly snapshots.

   * - Store monthly snapshots for

     - Sets the number of months that Ops Manager retains monthly snapshots.

       Ops Manager takes monthly snapshots every 28 days, not by calendar month.

   * - Day of Week for Full Snapshot

     - Sets the day of the week when Ops Manager attempts to take a full snapshot. 
       This ensures a recent complete backup.

       Ops Manager sets the default value to Sunday.

   * - Allow point-in-time restores going back

     - Sets the number of days that Ops Manager retains oplogs alongside
       snapshots. To learn how snapshots and point-in-time restores work,
       see restore-overview.

   * - Reference Time of Day (UTC)

     - Sets the time of day at
       [UTC](https://www.timeanddate.com/time/aboututc.html) from
       which the snapshot schedule starts. When you change the value in
       Reference Time of Day, snapshots that are in progress
       or that are already scheduled remain unaffected. Only snapshots
       taken after you change the reference time follow the updated schedule.

       The following statements describe how Ops Manager behaves in relation
       to the value you specify in Reference Time of Day:

       - This value acts as a timer that Ops Manager uses for scheduling and then
         taking the next snapshot. This value isn't the same as the time
         when Ops Manager takes the next snapshot, but it is close to it. This
         value differs from the actual time that Ops Manager uses to take a
         snapshot by a small interval. You can't control this interval.
       - If you leave this value blank, Ops Manager interprets it as `null`,
         starts the timer for scheduling the next snapshot, and then takes
         the next snapshot after a short interval from the time when it
         took the previous snapshot.

       - If you change the time value in this field, Ops Manager uses the new
         time value as the starting time for scheduling the snapshot that
         will occur *after the currently scheduled snapshot*.
         In other words, for each snapshot that is already scheduled, Ops Manager uses
         the time it already established: either based on the `null` value
         plus a short interval, or based on the custom reference time value
         plus a short interval. If you change the reference time value in
         this field, the next scheduled snapshot will not happen sooner
         than the snapshot that is already scheduled.

         To review examples, see Snapshot Frequency and Retention.

b. Click Submit.

### Edit Security Credentials

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Select the backup's ellipsis icon and select Edit Credentials**

On the line listing the process, click the ellipsis icon and click
Edit Credentials.

**Step 3: Provide the authentication information.**

Enter the following information as needed and click Submit.

* - Auth Mechanism

  - The authentication mechanism
    that the MongoDB host uses.

    MongoDB Community options include:

    - Username/Password

    - X.509 Client Certificate

    MongoDB Enterprise options also include:

    - Kerberos
    - LDAP

* - DB Username

  - For `Username/Password` or `LDAP` authentication, the
    username used to authenticate the MongoDB Agent with the MongoDB
    deployment.

    See
    /tutorial/configure-mongodb-agent-for-scram or
    /tutorial/configure-mongodb-agent-for-ldap.

* - DB Password

  - For `Username/Password` or `LDAP` authentication, the
    password used to authenticate the MongoDB Agent with the MongoDB
    deployment.

* - Allows TLS for connections

  - If checked, Backup uses TLS (Transport Layer Security) to connect to MongoDB.

    See /tutorial/configure-mongodb-agent-for-tls.

### Modify the Storage Engine Your Backups Use

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Select the backup's ellipsis icon and select Edit Storage Engine**

On the line listing the process, click the ellipsis icon and click
Edit Storage Engine.

**Step 3: Select the storage engine.**

Select the storage engine. See: considerations-backup-storage-engine
for more about choosing an appropriate storage engine for your 
backup.

**Step 4: Select the sync source.**

Select the Sync source from which to create the new backup.
In order to use the new storage engine, Ops Manager must resync the backup on
the new storage engine.

**Step 5: Click Submit.**

## Backup Settings Available to FCV (Feature Compatibility Version) 4.2 and Later

### Edit the Preferred Member for Backup

When each snapshot starts, Ops Manager selects a replica set member
to run the snapshot. This automatically selected member should have the 
least performance impact on the replica set. You can override the 
default selection.

**Important:**

Use default selection whenever possible. This choice
ensures backup availability.

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Open the Select Preferred Member to Backup panel.**

On the line listing the process, click `ellipsis` then click
Select Preferred Member to Backup.

**Step 3: Choose a replica set member to create snapshots.**

Click Select a member manually.

**Step 4: Select an available member.**

From the Select an available member drop-down, select the
hostname and process port for the desired member.

**Note:**

If the selected member becomes unavailable, an error message 
appears in the panel. Ops Manager uses a default member until the 
selected member is available.

**Step 5: Click Submit.**

## Backup Settings Available to FCV (Feature Compatibility Version) 4.0 and Earlier

### Enable Cluster Checkpoints

**Important:**

You may use checkpoints for clusters that run MongoDB with
Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

Cluster checkpoints provide restore points in
between scheduled snapshots. You can use checkpoints to create custom
snapshots at points in time between regular snapshots.

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Select the backup's ellipsis icon and select Edit Snapshot Schedule.**

On the line listing the process, click the ellipsis icon and click
Edit Snapshot Schedule.

**Step 3: Enable cluster checkpoints.**

a. Select Create cluster checkpoint every.
b. Set the interval.
c. Click Submit.

### Edit the Namespaces Filter

The namespaces-filter specifies which databases and collections
Ops Manager backs up.

**Note:**

Namespace filtering is supported only for Ops Manager versions 
`6.0.8` and later. Your MongoDB deployments must have 
`featureCompatibilityVersion` values of `4.0` and earlier, 
or `6.0.1` and later.

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Select the backup's ellipsis icon and select Edit Namespaces Filter.**

**Step 3: Add or remove namespaces and click Submit.**
