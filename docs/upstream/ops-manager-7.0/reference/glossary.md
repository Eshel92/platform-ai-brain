<!-- Converted from reference/glossary.txt (reStructuredText). Includes are inlined. -->

# Glossary

agent
   A lightweight program that provides an interface between your MongoDB
   processes and Ops Manager.

agent API key
   A unique identifier that authenticates a project's
   MongoDB Agents to Ops Manager. A project can have
   multiple agent API (Application Programming Interface) keys.

   **See also:**

   /tutorial/manage-agent-api-key

application database
   The dedicated set of MongoDB databases that store metadata for the
   Ops Manager installation and the managed MongoDB deployments.

   **See also:**

   mms-application-database

authentication mechanism
   A method to enable access to a MongoDB database. This is separate
   from authorization, which grants you permission to use certain
   actions on a MongoDB database.

   **See also:**

   /tutorial/edit-host-authentication-credentials

automation
   The assisted management of MongoDB processes through the Ops Manager
   interface. The MongoDB Agents installed on
   your MongoDB hosts allow you to deploy, configure, and update
   MongoDB processes directly from Ops Manager.

   **See also:**

   automation

Automation Agent
   The lightweight component that had automated common management
   tasks. The Automation Agent runs on every server that ran a
   mongod or mongos.

   **Note:**

   This has been replaced with the MongoDB Agent.

backing databases
   The collective term for the sets of MongoDB databases that support an
   Ops Manager deployment: the application database and the
   backup database(s).

   **See also:**

   /tutorial/prepare-backing-mongodb-instances

Backup Agent
   The lightweight component that had run within your data center and
   backed up MongoDB processes via the MongoDB wire protocol. No direct
   file system access was needed.

   **Note:**

   This has been replaced with the MongoDB Agent.

Backup Database
   The set of databases where onprem stores backup data. This
   includes the Oplog Store Database and any
   backup blockstore database or `S3 Snapshot Store`
   metadata database deployed.

   **See also:**

   - backup-database
   - /core/backup-overview

backup blockstore database
   The database that stores your snapshots. The
   database is also referred to simply as the *blockstore.* The
   blockstore uses a storage format that parses a snapshot into
   smaller chunks that allow Ops Manager to manage snapshot
   changes. You can administer blockstores from the
   blockstores-page. The blockstore is one type of
   Backup Database.

backup cursor
   A tailable cursor pointing to a list of
   backup files. Starting with FCV 4.2, Ops Manager uses
   backup cursors instead of 
   `head databases`.

Backup Daemon
   A required headless service to the Ops Manager Application that is
   responsible for backup snapshot maintenance work, such as
   a groom and managing file system snapshot files on the
   file system store

   While we no longer use a head database for backup
   snapshots, Backup Daemons are still a required component for
   Ops Manager backups and queryable backup to function.

   **See also:**

   backup-daemon

backup job
   The Ops Manager process that backs up MongoDB deployments.

   For FCV 4.0 and earlier, the `Backup Daemon` stores backups 
   locally as `head databases`. A sharded cluster 
   will have a different head database for each shard. 

   For FCV 4.2 and later, the WiredTiger storage engine takes snapshots
   of your deployment using backup cursors to 
   allow point-in-time copying of the WiredTiger files. Applications 
   can continue read and write operations on the database while 
   WiredTiger takes the snapshot.

   You can re-assign backup jobs among Backup Daemons.

   **See also:**

   jobs-page

batch
   The collection of jobs needed to restore a sharded cluster:
   one job for each shard and one job for the config server.

   Replica set restore jobs do not use batches.

block
   A MongoDB document that stores the compressed contents of a 64 KB to
   16 MB slice of the data and metadata of a file included in a
   snapshot. In dividing the snapshot, Ops Manager can back up data block
   by block instead of writing whole new copies of a snapshot.

blockstore

   **See also:**

   backup blockstore database

checkpoint
   A point in time between snapshots to which you can restore a sharded
   cluster. Ops Manager must stop the balancer each time it creates a
   checkpoint. Ops Manager doesn't require checkpoints and disables
   checkpoints by default.

   **Important:**

   You may use checkpoints for clusters that run MongoDB with
   Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
   MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

   **See also:**

   checkpoint

conf call
   A request from a MongoDB Agent to Ops Manager to get the latest
   configuration for that Agent's project including the nodes to which
   the Agent connects and what data to back up.

cluster
   In Ops Manager, *cluster* can refer to either a replica set or
   sharded cluster.

custom snapshot
   A backup of the state of your MongoDB deployment at a point in time
   between stored snapshots. Ops Manager builds a custom
   snapshot by applying oplog data to a stored snapshot.

   **See also:**

   /tutorial/nav/restore-overview

deduplication
   A process that eliminates redundant data. This data can be additional
   copies of database or file system documents or redundant data within
   those documents at the block level when written to a storage medium
   like spinning or solid state disks. Only unique documents or blocks
   are written to a storage medium. This process usually applies to
   backups or data archiving.

   **Example:**

   Each recipient in an email system may have their own copy of an
   email sent to the whole company. With deduplication, all copies of
   this except one are replaced with pointers to a single stored copy
   before backing up the email system. This effectively reduces the
   amount of storage capacity needed to back up this one email by 99
   percent.

deployment
   Usually refers to all the MongoDB processes that run within an Ops Manager
   `project`. *Deployment* can also refer to a specific set of
   MongoDB processes, such as a specific sharded cluster or
   replica set.

dirty bytes
   Data that has been updated in the WiredTiger cache but not flushed to
   disk.

excluded namespace
   A database or collection that Ops Manager will not back up, as designated
   by its namespace.

   **See also:**

   namespaces-filter

File System Store
   A directory on a server that stores your database backup
   snapshots as files. You can administer file system
   storage from the blockstores-page.

groom
   A job that removes unused blocks on a `blockstore` and that can
   move blocks from one blockstore to another. You can view and manage
   grooms from grooms-page and groom-priority-page.

group
   A distinct set of MongoDB processes and Ops Manager users. Synonymous with
   `project`.

   **See also:**

   /tutorial/manage-projects

head

   **See also:**

   `head database`

head database
   The copy of a backed-up deployment stored on the
   `Backup Daemon's` server. The daemon maintains
   a `head database` for each shard or
   replica set it backs up and creates periodic
   snapshots. The Daemon stores the head databases
   in the head directory.

   Starting with FCV 4.2, onprem uses
   backup cursors instead of 
   `head databases`.

head directory
   The dedicated disk partition on the
   `Backup Daemon's` host where the Backup Daemon
   stores the `head databases`. The daemon writes
   to this directory as the `mongodb-mms` user.

host
   A physical machine, virtual machine, or container that serves one or
   more MongoDB processes.

initial sync
   The MongoDB operation that replicates data from an existing
   replica set member to a new member. Ops Manager uses initial sync
   when creating a new `head database`.

   **See also:**

   - backup-initial-sync
   - Replica Set Data Synchronization in the MongoDB manual

job
   See backup job.

link-token
   A string that contains the information necessary to connect from
   Ops Manager to Atlas during a Live Migration from an Ops Manager deployment
   to a deployment in Atlas.

migration host
   A dedicated server with its own specially-configured MongoDB Agent configured for live migration.
   You run the Live Migration (push) process on the migration host to migrate
   your MongoDB deployment to Atlas.

   **See also:**

   - /tutorial/provision-migration-host
   - /tutorial/migrate-to-atlas

MongoDB Agent
   A lightweight agent that can monitor, manage, and back up
   your MongoDB databases.

   **See also:**

   /tutorial/nav/mongodb-agent

monitoring
   The real-time reporting, visualization, and alerting of the state of
   your MongoDB processes.

   **See also:**

   monitoring-functional-overview

Monitoring Agent
   The lightweight component that had run within your data center and
   monitored your MongoDB processes via the MongoDB wire protocol. No
   direct file system access was needed.

   **Note:**

   This has been replaced with the MongoDB Agent.

namespace
   The combination of the database name and collection name:

   ```javascript
   "database-name.collection-name"
   ```

oplog slice
   A compressed batch of entries for the tailed oplog of a
   backed-up shard or replica set. The MongoDB Agent creates an
   oplog slice and sends it to Ops Manager, which stores it in the
   Oplog Store Database.

   For FCV 4.0 and earlier, the `Backup Daemon` retrieves the 
   slice and applies it to the associated `head database`.

   For FCV 4.2 and later, onprem retrieves the slice and stores it
   in the Oplog Store Database.

   **See also:**

   oplog-stores-page

Oplog Store Database
   The database where Ops Manager stores oplog slices
   before applying them to a deployment's backup.

   **See also:**

   oplog-stores-page

Ops Manager Application
   The main Ops Manager component. The application provides the user
   interface for managing MongoDB deployments and provides endpoints for
   MongoDB Agents to transmit data.

   **See also:**

   mms-application-package

Ops Manager HTTP Service
   The interface through which the MongoDB Agent communicates
   with Ops Manager.

   **See also:**

   mms-http-service

ping
   A data transmission that the MongoDB Agent sends to Ops Manager to
   confirm that the Agent and its MongoDB processes are running and
   reachable.

point-in-time restore
   A database restoration that captures the state of your data at a
   moment in-between snapshots. Point-in-time
   restores take longer to perform than snapshot restores.

   **See also:**

   /tutorial/nav/restore-overview

process
   An instance of MongoDB running on a given host and port. The MongoDB
   database process is mongod. MongoDB also uses the
   mongos process to route operations in the
   sharded clusters.

   **See also:**

   MongoDB Package Components

project
   A distinct set of MongoDB processes and Ops Manager users. Synonymous with
   `group`.

   **See also:**

   /tutorial/manage-projects

Public API key
   A unique identifier that authenticates an Ops Manager user through the
   Ops Manager Administration API. The key belongs to 
   the user, as opposed to the `agent API key`, which belongs to 
   the project.

queryable backup
   A feature provided by Ops Manager in which Ops Manager quickly and securely makes
   a given snapshot accessible over a MongoDB connection string. You can
   use the connection string with standard MongoDB tools such as
   `mongosh` or mongodump to access the snapshot for read-only
   operations.

   Queryable backups start up quickly regardless of the snapshot's total
   data size. They are uniquely useful for restoring a small subset of
   data, such as a document that was accidentally deleted, or reading
   out a single collection with mongodump.

   **See also:**

   /tutorial/query-backup/

Recovery Point Objective
   The maximum tolerable age of backup files that must be recovered from
   storage for normal operations to resume after a failure or disaster
   occurs.

Recovery Time Objective
   The maximum tolerable length of time that a system can be offline
   after a failure or disaster occurs.

role
   The permissions granted to an Ops Manager or MongoDB user.

   **See also:**

   - /reference/user-roles for Ops Manager user roles
   - Built-in Roles in the
     MongoDB manual for MongoDB user roles

rolling restart
   A technique used to maintain cluster availability during maintenance 
   periods by updating nodes in a replica set one-by-one, always
   maintaining a primary node, until all nodes are updated.

   **See also:**

   rolling-restart-faq

S3 Snapshot Store
   An s3 bucket in aws that stores your database backup
   snapshots as blocks. You can administer s3
   blockstore storage from the blockstores-page.

   **See also:**

   /tutorial/manage-s3-blockstore-storage

server
   A physical or virtual machine that serves one or more MongoDB
   processes.

snapshot
   Single backup of your data that Ops Manager captures at a specific
   interval and stores as a snapshot in one of the following locations:

   - blockstore
   - `file system stores`
   - `S3 snapshot stores`

   Ops Manager creates snapshots in different ways depending on the
   fcv-link of the MongoDB database:

   - For fcv-link 4.0 or earlier, Ops Manager created snapshots from database copies kept on `head databases`.
   - For fcv-link 4.2 or later, Ops Manager creates snapshots from secondaries.

   The snapshot-frequency-and-retention determines the interval
   for taking snapshots and how long to store them.

   **See also:**

   - /core/backup-overview
   - custom snapshot

snapshot frequency and retention policy
   The schedule for how often to take snapshots and
   how long to store them.

   **See also:**

   snapshot-frequency-and-retention

snapshot store
   The location where your snapshots are stored.
   There are multiple types of snapshot stores, including:

   - `file system stores`
   - Blockstores
   - `S3 snapshot stores`

storage engine
   The database storage engine manages how data is stored on disk.
   MongoDB versions 3.0 and later offer multiple storage engines.

   **See also:**

   - Storage
   - MongoDB Storage FAQ in the MongoDB
     manual

sync store
   During `initial sync` of a backed-up deployment, Ops Manager
   briefly stores slices of the backed-up deployment in a temporary sync
   store on the Oplog Store Database. Ops Manager uses the storage
   while streaming slices to the Backup Daemon.

version manifest
   List of all released MongoDB versions that a particular version of
   Ops Manager supports. Ops Manager uses this list if running in
   local mode.
