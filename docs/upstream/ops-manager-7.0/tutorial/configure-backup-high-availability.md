<!-- Converted from tutorial/configure-backup-high-availability.txt (reStructuredText). Includes are inlined. -->

# Configure a Highly Available Ops Manager Backup Service

## Considerations

The following considerations apply to making backups highly available:

- The Ops Manager Application manages backups. To meet your backup needs, deploy
  a sufficient number of Ops Manager hosts with a load balancer.

- Ops Manager expects that all stores are available at all times. High
  availability of S3-compatible storage and filesystem stores is outside of the Ops Manager Application
  scope.

- Create a replica set rather
  than a standalone for each dedicated MongoDB process that hosts the
  Ops Manager Application and for each backing database. A backing database can
  include a MongoDB blockstore snapshot store, a MongoDB oplog store,
  or an S3-compatible storage metadata store.
  
  Ops Manager uses `w: 2` write concern,
  which requires acknowledgement from the primary and one
  secondary for each write operation. When deploying a replica set
  with members in many facilities, ensure that a single facility has enough
  votes to elect a primary, if needed. When choosing between facilities
  for this single facility, choose the facility that hosts the Ops Manager Application
  and application database. Place a majority of voting members and all the
  members that can become primary in this facility. Otherwise, network
  partitions could prevent the set from being able to form a majority. 

  To learn more, see:

  - Replica Sets Distributed Across Two or More Data Centers
  - Replica Set Elections

- If you choose to
  assign snapshot stores to specific data centers, consider each region's
  high availability requirements based on your deployment needs. For example,
  in some deployments, configuring a replica set may provide sufficient
  availability. If your deployment has 24/7 high availability requirements
  even if a data center goes down, configure enough nodes in each data
  center to accommodate writes. To learn more, see highly-available-deployment.

- Configure more than one `Backup Daemon` instance for
  queryable restore jobs and
  groom jobs, which are useful for large deployments.

  For each Backup Daemon, you can:

  - Assign Backup jobs.
    If you don't assign jobs to specific daemons and stores, Ops Manager uses
    all available Backup Daemons for each group.

  - Adjust the settings on the Daemon configuration
    page. For example, for the dedicated queryable Daemon host, you can
    clear all checkboxes except Queryable Restore Jobs.

## Additional Information

- You install the Backup Daemon component with the Ops Manager package.
  To run the Daemon, you must activate it. To learn more, select the
  procedure specific to your platform in the /installation section.

- To view all active Backup Daemons and access their configuration options,
  see Daemons.

- To start and stop a Backup Daemon on a server, see
  /tutorial/start-and-stop-backup-daemon.

- To move jobs from a lost Backup server to another Backup server, see
  /tutorial/move-jobs-to-new-backup-daemon.

- To make the Ops Manager Application highly available, see
  /tutorial/configure-application-high-availability.
