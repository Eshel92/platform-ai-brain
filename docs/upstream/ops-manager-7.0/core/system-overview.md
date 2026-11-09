<!-- Converted from core/system-overview.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Architecture

An Ops Manager installation includes hosts that run the Ops Manager Application and
hosts that serve and store application data and snapshots.

(Figure: /images/ops-manager-overview.png)

The Ops Manager Application requires a dedicated `Application Database`
and, if you enabled backups, `Snapshot Stores`.

## Ops Manager Application

The Ops Manager Application provides the user interface and the HTTP (Hypertext Transfer Protocol) services
the MongoDB Agent uses to transmit data to and from Ops Manager. These are
all stateless and start automatically when the Ops Manager Application starts.
Multiple instances of the Ops Manager Application can run if each instance uses
the same configuration and the same application database. Users and
Agents can interact with any instance.

By default, the Ops Manager Application runs on port `8080` and contains the
web interface for managing Ops Manager users, monitoring of MongoDB hosts,
and managing host backups.

For a list of Ops Manager's default ports and health-check endpoints, see
/reference/firewall-configuration.

## Backup Daemon Service

You can configure any Ops Manager instance to perform backup snapshot
maintenance work, such as a grooms and managing
file system snapshot files on the file system store by running the Backup Daemon. To learn how to start,
check the status of, stop, and restart the Backup Daemon on a server,
see Start and Stop the Backup Daemon.

How the Backup Daemon performs depends upon the
MongoDB version compatibility
of your database. This Feature Compatibility Version ranges from the
current version to one version earlier. For example, with MongoDB 4.4,
the FCV can be `4.2` or `4.4`. Backup functionality changed with
FCV `4.2`.

The Backup Daemon service provides the following services for databases:

- Runs groom jobs, incremental filesystem snapshots, other backup
  related jobs 
- Performs some state updates to the backup job
- Perform a queryable restore

Client applications can't communicate with the daemon. Its state and job
queues come from the mms-application-database. Ops Manager creates
snapshots from the database being backed up. For incremental backups
using file system stores, the daemon is responsible for creating
snapshots.

Multiple Backup Daemons can scale
horizontally to run more concurrent jobs when needed and can provide
*manual* failover.

If you run multiple Backup Daemons, Ops Manager selects the Backup Daemon
to use when a user enables backup for a deployment. The
`head database`
resides with the daemon's host.

## Dedicated Storage for Operational Data

### Ops Manager Application Database

Ops Manager uses a dedicated MongoDB database to store the Ops Manager\'s
operational data. The application database runs as a
replica set to ensure redundancy and high availability. This
replica set hosts *only* Ops Manager data. Before installing Ops Manager,
you must provision the application database.
This database contains application metadata:

- Monitoring data collected from the MongoDB Agents.

- Metadata for Ops Manager users, projects, hosts, monitoring data, and
  backup state.

For topology and specifications, see
mms-application-database-specifications.

### Snapshot Storage

Ops Manager creates snapshots of deployments to back up your databases.
You can have Ops Manager store these snapshots in
`snapshot stores`. Snapshot stores can be local
databases, local file systems, or cloud-based data stores. There can
be more than one snapshot store per project. Ops Manager writes the
recent history of the deployment database to a separate database
regardless of where the snapshots are written.

Snapshot storage include two components:

#### Snapshot Stores

Snapshots can be written to one of three target storage systems:

| System | Storage Method | Learn More |
|---|---|---|
| blockstore | A MongoDB database stored in a local host. | /tutorial/manage-blockstore-storage |
| `S3 snapshot store` | A cloud data store in S3-compatible storage. | /tutorial/manage-s3-blockstore-storage |
| `file system store` | A local file system in the directory of your choosing. | /tutorial/manage-filestore-storage |

#### Oplog Store

The `Oplog Store` retains the
oplog entries that the `Backup Daemon` applies to its
local copies of your backed-up deployments.

**See also:**

To learn about the requirements and procedures for Oplog Stores,
see /tutorial/manage-oplog-storage.
