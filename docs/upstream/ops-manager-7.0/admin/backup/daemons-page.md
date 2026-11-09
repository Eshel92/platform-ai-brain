<!-- Converted from admin/backup/daemons-page.txt (reStructuredText). Includes are inlined. -->

# Daemons

This page lists all active `Backup Daemons` and
provides configuration options. Ops Manager automatically detects Backup
Daemons and displays them here. You can reconfigure daemons from this
page. Changes can take up to 5 minutes to take effect.

Click Pre-Configure New Daemon at the bottom of the page if
you want to add a daemon but do not want it to take new jobs. Type the
`<machine>:/<roothead path>/` in the text field above
Pre-Configure New Daemon. *You must include a slash at the end* (`/`) or 
the Backup Daemon won't run and instead generates a Java exception error in the 
Backup Daemon logs.
Click the button to configure the new Backup Daemon.

For each daemon, the page lists the server name, configuration,
`head` space used, head space free, the number of
replica sets backed up, the percentage of time the Backup Daemon
Service was busy, and job runtime counts by 1 minute, 10 minutes,
60 minutes, less than or equal to 180 minutes, and greater than 180
minutes.

The page includes the following fields and links to manage and
configure daemons:

* - Item
  - Action

* - Show Detailed JSON
  - Click this link to display the Backup Daemon JSON (Javascript Object Notation). When the
    JSON (Javascript Object Notation) displays, the View raw runtime data link
    appears following the code to view the raw data.

* - Move all heads
  - Click this link to move all the Backup Daemon jobs that live on
    this daemon to a new daemon location.

    #. Click the link.
    #. Click the location.
    #. Click Move all heads.

* - Delete Daemon
  - Click this link to delete the Backup Daemon.

    You must restart the daemon to reconfigure the daemon after
    deletion.

* - Assignment
  - Select this to allow the daemon to process more jobs. If the
    daemon's disk fills, clear this so the host is not overloaded.

* - Backup Jobs
  - Select this to allow the daemon to process more backup jobs.
    Clear this when performing maintenance on a daemon's host.

* - Queryable Restore Jobs
  - Select this to allow the daemon to process `queryable backups`.

    For the fastest possible restore time, configure a dedicated queryable restore
    daemon by selecting Queryable Restore Jobs and clearing the checkboxes
    for the other daemon roles, for example, Garbage Collection and Resource Usage.

* - Resource Usage
  - Select this to collect data for this daemon. This includes the
    following data for each backup job run on this daemon:

    - project
    - storage that head database uses
    - storage that the snapshot store uses
    - oplog operations

    Navigate to the Resource Usage page
    to review the collected data.

* - Garbage Collection
  - Select this to allow the daemon to schedule groom jobs
    to remove unused blocks and expired snapshots.

* - Head Disk Type
  - From this menu, select SSD (solid-state drive) or HDD (hard disk drive) storage.

    If you select SSD (solid-state drive), Ops Manager sends jobs to this daemon only when:

    - The job generates a volume of oplog data that meets or exceeds
      a threshold of 1 GBph (Gigabytes per hour), or
    - Ops Manager has no available HDD (hard disk drive) daemon to handle the job.

* - Deployment Id
  - Unique identifier of the Deployment Region
    in which to run the daemon.

* - Assignment Labels
  - Type one or more labels that can be used to assign the daemon
    to a specific project.

* - Number of Workers
  - Type the number of concurrent backup tasks this daemon should
    process at one time.

    To query a snapshot of a sharded cluster, the
    `Backup Daemon` requires at least one worker for the
    config server, one
    worker for each shard, and one worker for the
    `mongos` instance.

    To query a snapshot of a replica set, the Backup Daemon
    requires at least one worker for the replica set.

    For example, if you restore a queryable backup from a 3-shard cluster with 1 shard router 
    (mongos), you need 
    this value to be at least `5`:

    - 1 per shard (`3`) +
    - 1 for the config server (`1`) +
    - 1 for the `mongos`

    When the queryable backup begins, the Backup Daemon spins
    up 5 or more workers to manage these components.
