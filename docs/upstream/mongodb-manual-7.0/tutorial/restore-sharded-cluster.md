<!-- Converted from tutorial/restore-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Restore a Self-Managed Sharded Cluster from Snapshots

This procedure restores a sharded cluster from an existing backup
snapshot, such as Logical Volume Manager (LVM) snapshots. The
source and target sharded cluster must have the same number of shards.
For information on creating LVM snapshots for all components of a
sharded cluster, see backup-sharded-lvm.

**Note:**

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which maintain the atomicity guarantees of
transactions across shards:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)

## Considerations

For encrypted storage engines that
use `AES256-GCM` encryption mode, `AES256-GCM` requires that every
process use a unique counter block value with the key.

For encrypted storage engine
configured with `AES256-GCM` cipher:

- Restoring from Hot Backup
      If you restore from files taken through "hot"
      backup while the `mongod` is running, MongoDB
      detects "dirty" keys on startup and automatically rolls over
      the database key to avoid IV (Initialization Vector) reuse.

- Restoring from Cold Backup
      However, if you restore from files taken through "cold" backup
      while the `mongod` is not running, MongoDB
      does not detect "dirty" keys on startup, and reuse of IV voids
      confidentiality and integrity guarantees.

      To avoid the reuse of the keys after
      restoring from a cold filesystem snapshot, MongoDB adds a new
      command-line option `--eseDatabaseKeyRollover`. When started with the
      `--eseDatabaseKeyRollover` option, the `mongod`
      instance rolls over the database keys configured with
      `AES256-GCM` cipher and exits.

## A. (Optional) Review Replica Set Configurations

This procedure initiates a new replica set for the 
Config Server Replica Set (CSRS) and each shard replica set using
the default configuration. To use a different replica set
configuration for your restored CSRS and shards, you must
reconfigure the replica set(s).

If your source cluster is running correctly and is accessible, connect a
`mongo` shell to the primary replica set member
in each replica set. Next, run `rs.conf()` to view the
replica configuration document.

If you cannot access one or more components of the source sharded 
cluster, please reference any existing internal documentation to 
reconstruct the configuration requirements for each shard replica set 
and the config server replica set.

## B. Prepare the Target Host for Restoration

Storage Space Requirements
  Ensure the target host hardware has sufficient open storage space
  for the restored data. If the target host contains existing sharded
  cluster data that you want to keep, ensure that you have enough 
  storage space for both the existing data and the restored data.

LVM Requirements
  For LVM snapshots, you must have at least one LVM managed
  volume group and a logical volume with enough free space for the
  extracted snapshot data.

MongoDB Version Requirements
  Ensure the target host and source host have the same MongoDB Server
  version. To check the version of MongoDB available on a host machine,
  run `mongod --version` from the terminal or shell.

  For complete documentation on installation, see
  /installation.

Shut Down Running MongoDB Processes
  If restoring to an existing cluster, shut down the 
  `mongod` or `mongos` 
  process on the target host.

  For hosts running `mongos`, connect a 
  `mongo` shell to the `mongos` and
  run `db.shutdownServer()` from the `admin` database:

  ```javascript
  use admin
  db.shutdownServer()
  ```

  For hosts running a `mongod`, connect a 
  `mongo` shell to the `mongod` and
  run `db.hello()`:

  * If `isWritablePrimary` is false, the `mongod` is a
    secondary member of a replica set. You
    can shut it down by running `db.shutdownServer()` from
    the `admin` database.

  * If `isWritablePrimary` is true, the `mongod` is the
    primary member of a replica set. Shut down
    the secondary members of the replica set *first*. Use
    `rs.status()` to identify the other members of
    the replica set.

    The primary automatically steps down after it detects a
    majority of members are offline. After it steps down
    (`db.hello` returns
    `isWritablePrimary: false`), you can
    safely shut down the `mongod`.

Prepare Data Directory
  Create a directory on the target host for the restored database
  files. Ensure that the user that runs the 
  `mongod` has read, write, and execute permissions
  for all files and subfolders in that directory:

  ```bash
  sudo mkdir /path/to/mongodb
  sudo chown -R mongodb:mongodb /path/to/mongodb
  sudo chmod -R 770 /path/to/mongodb
  ```

  Substitute `/path/to/mongodb` with the path to the data directory
  you created. On RHEL (Red Hat Enterprise Linux) / CentOS,
  Amazon Linux, and SUSE, the default username is `mongod`.

Prepare Log Directory
  Create a directory on the target host for the 
  `mongod` log files. Ensure that the user that 
  runs the `mongod` has read, write, and execute 
  permissions for all files and subfolders in that directory:

  ```bash
  sudo mkdir /path/to/mongodb/logs
  sudo chown -R mongodb:mongodb /path/to/mongodb/logs
  sudo chmod -R 770 /path/to/mongodb/logs
  ```

  Substitute `/path/to/mongodb/logs` with the path to the log 
  directory you created. On RHEL (Red Hat Enterprise Linux) /
  CentOS, Amazon Linux, and SUSE, the default username is `mongod`.

Create Configuration File
  This procedure assumes starting a `mongod`
  with a configuration file. 

  Create the configuration file in your preferred location. Ensure that
  the user that runs the `mongod` has read and
  write permissions on the configuration file:

  ```bash
  sudo touch /path/to/mongod.conf
  sudo chown mongodb:mongodb /path/to/mongodb/mongod.conf
  sudo chmod 644 /path/to/mongodb/mongod.conf
  ```

  On RHEL (Red Hat Enterprise Linux) / CentOS, Amazon Linux,
  and SUSE, the default username is `mongod`.

  Open the configuration file in your preferred text editor and
  modify at it as required by your deployment. Alternatively,
  if you have access to the original configuration file for the
  `mongod`, copy it to your preferred location
  on the target host.

  **Important:**

  Validate that your configuration file includes the following
  settings:

  - `storage.dbPath` must be set to the path to your
    preferred data directory.

  - `systemLog.path` must be set to the path to your
    preferred log directory

  - `net.bindIp` must include the IP address of the
    host machine.

  - `replication.replSetName` has the same value across
    each member in any given replica set.

  - `sharding.clusterRole` has the same value across each
    member in any given replica set. 

  - You must also specify the same startup options for your new deployment that were specified in
    the snapshot.

## C. Restore Config Server Replica Set

**Step 1: Restore the CSRS primary `mongod` data files.**

Select the tab that corresponds to your preferred backup method:

tabs:
  - id: lvm
    name: "LVM Snapshot"
    content: |
      1. Mount the LVM snapshot on the target host machine. 
         The specific steps for mounting an LVM snapshot depends on 
         your LVM configuration.

         The following example assumes an LVM snapshot created 
         using the lvm-backup-operation step in the
         /tutorial/backup-with-filesystem-snapshots 
         procedure.

         ```bash
         lvcreate --size 250GB --name mongod-datafiles-snapshot vg0
         gzip -d -c mongod-datafiles-snapshot.gz | dd o/dev/vg0/mongod-datafiles-snapshot
         mount /dev/vg0/mongod-datafiles-snapshot /snap/mongodb
         ```

         This example may not apply to all possible LVM 
         configurations. Refer to the LVM documentation for your 
         system for more complete guidance on LVM restoration.

      #. Copy the `mongod` data files from the
         snapshot mount to the data directory created in
         B. Prepare the Target Host for Restoration:

         ```bash
         cp -a /snap/mongodb/path/to/mongodb /path/to/mongodb
         ```

         The `-a` option recursively copies the contents of
         the source path to the destination path while preserving
         folder and file permissions.

      #. Comment out or omit the following 
         configuration file settings:

         ```yaml
         #replication
         #  replSetName: myCSRSName
         #sharding
         #  clusterRole: configsvr
         ```

         To start the `mongod` using a 
         configuration file, specify the 
         `--config` option in the 
         command line specifying the full path to the 
         configuration file.

         ```bash
         mongod --config /path/to/mongodb/mongod.conf
         ```

         If you are restoring from a 
         `namespace-filtered` 
         snapshot, specify the `--restore` option.

         ```bash
         mongod --config /path/to/mongod/mongod.conf --restore
         ```

         If you have `mongod` configured to 
         run as a system service, start it using the recommended 
         process for your system service manager.

         After the `mongod` starts, connect 
         to it using the `mongo` shell.

  - id: other
    name: "Other Backup Files (NOT mongodump)"
    content: |
      1. Make the data files stored in your selected backup medium
         accessible on the host. This may require mounting the 
         backup volume, opening the backup in a software utility, 
         or using another tool to extract the data to disk. Refer 
         to the documentation for your preferred backup tool for 
         instructions on accessing the data contained in the 
         backup. 

      #. Copy the `mongod` data files from the
         backup data location to the data directory created in
         B. Prepare the Target Host for Restoration:

         ```bash
         cp -a /backup/mongodb/path/to/mongodb /path/to/mongodb
         ```

         The `-a` option recursively copies the contents of
         the source path to the destination path while preserving
         folder and file permissions.

      #. Comment out or omit the following 
         configuration file settings:

         ```yaml
         #replication
         #  replSetName: myCSRSName
         #sharding
         #  clusterRole: configsvr
         ```

      #. To start the `mongod` using a 
         configuration file, specify the 
         `--config` option in the 
         command line specifying the full path to the 
         configuration file.

         ```bash
         mongod --config /path/to/mongodb/mongod.conf
         ```

         If restoring from a 
         `namespace-filtered` 
         snapshot, also specify the  `--restore` option.

         ```bash
         mongod --config /path/to/mongod/mongod.conf --restore
         ```

         **Note:** Cloud Manager or Ops Manager Only

         If performing a manual restoration of a Cloud Manager 
         or Ops Manager backup, you must specify the 
         `disableLogicalSessionCacheRefresh` server parameter
         prior to startup.

         ```bash
         mongod --config /path/to/mongodb/mongod.conf \
           --setParameter disableLogicalSessionCacheRefresh=true
         ```

         If you have `mongod` configured to 
         run as a system service, start it using the recommended 
         process for your system service manager.

         After the `mongod` starts, connect 
         to it using the `mongo` shell.

**Step 2: Drop the `local` database.**

Use `db.dropDatabase()` to drop the `local` database:

```javascript
use local
db.dropDatabase()
```

**Step 3: Insert the filtered file list into the local database.**

This step is only required if you are restoring from a 
namespace-filtered snapshot.

For each shard, locate the filtered file list with the following name
format: `<shardRsID>-filteredFileList.txt`. This file contains a
list of JSON objects with the following format:

```javascript
{
   "filename":"file1", 
   "ns":"sampleDb1.sampleCollection1", 
   "uuid": "3b241101-e2bb-4255-8caf-4136c566a962"
}
```

Add each JSON object from each shard file to a new 
`db.systems.collections_to_restore` collection in your `local` 
database. You can ignore entries with empty `ns` or `uuid` 
fields. When inserting entries, the `uuid` field must be inserted 
as type `UUID`.

**Step 4: Run the filtered file restore command.**

This step is only required if you are restoring from a 
namespace-filtered snapshot.

After inserting all entries, run the following commands:

```bash
use admin
db.runCommand({"_configsvrRunRestore":1})
```

**Step 4: For any planned or completed shard hostname or replica set name changes, update the metadata in `config.shards`.**

You can skip this step if all of the following are true:

* No shard member host machine hostname has or will change during this procedure.
* No shard replica set name has or will change during this procedure.

Issue the following `find()` method on the 
`shards` collection in the config-database.
Replace `<shardName>` with the name of the shard. By default the 
shard name is its replica set name. If you added the shard
using the `addShard` command *and* specified a custom
`name`, you must specify that `name` to `<shardName>`.

```javascript
use config
db.shards.find( { "_id" : "<shardName>" } )
```

This operation returns a document that
resembles the following:

```javascript
{  
   "_id" : "shard1",  
   "host" : "myShardName/alpha.example.net:27018,beta.example.net:27018,charlie.example.net:27018", 
   "state" : 1 
}
```

**Important:**

The `_id` value must match the `shardName` value in the
`_id : "shardIdentity"` document on the corresponding shard.
When restoring the shards later in this procedure, validate that
the `_id` field in `shards` matches the 
`shardName` value on the shard. 

Use the `updateOne()` method to update the
`hosts` string to reflect the planned replica set name and
hostname list for the shard. For example, the following operation 
updates the  `host` connection string for the shard with `"_id" : "shard1"`:

```javascript
db.shards.updateOne(
  { "_id" : "shard1" },
  { $set : { "host" : "myNewShardName/repl1.example.net:27018,repl2.example.net:27018,repl3.example.net:27018" } }
)
```

Repeat this process until all shard metadata accurately reflects
the planned replica set name and hostname list for each shard in the 
cluster.

**Note:**

If you do not know the shard name, issue the 
`find()` method on the `shards`
collection with an empty filter document `{}`:

```javascript
use config
db.shards.find({})
```

Each document in the result set represents one shard in the 
cluster. For each document, check the `host` field for a 
connection string that matches the shard in question, i.e. a 
matching replica set name and member hostname list. Use the `_id` 
of that document in place of `<shardName>`.

**Step 5: Restart the `mongod` as a new single-node replica set.**

Shut down the
`mongod`. Uncomment or add the following
configuration file options:

```yaml
replication
  replSetName: myNewCSRSName
sharding
  clusterRole: configsvr
```

If you want to change the replica set name, you must update
the `replSetName` field with the new name
before proceeding.

Start the `mongod` with the updated
configuration file:

```bash
mongod --config /path/to/mongodb/mongod.conf
```

If you have `mongod` configured to run as a
system service, start it using the recommended process for your
system service manager.

After the `mongod` starts, connect to it using
the `mongo` shell.

**Step 6: Initiate the new replica set.**

Initiate the replica set using `rs.initiate()` with the 
default settings. 

```javascript
rs.initiate()
```

Once the operation completes, use `rs.status()` to check
that the member has become the primary. 

**Step 7: Add additional replica set members.**

For each replica set member in the CSRS, start the
`mongod` on its host machine. Once you have
started up all remaining members of the cluster successfully, 
connect a `mongo` shell to the primary replica
set member. From the primary, use the `rs.add()` method to 
add each member of the replica set. Include the replica set name as 
the prefix, followed by the hostname and port of the member's 
`mongod` process:

```javascript
rs.add("config2.example.net:27019")
rs.add("config3.example.net:27019")
```

If you want to add the member with specific replica 
`member` configuration settings, you can pass a 
document to `rs.add()` that defines the member hostname
and any `members` settings your deployment requires.

```javascript
rs.add(
 {
   "host" : "config2.example.net:27019",
   priority: <int>,
   votes: <int>,
   tags: <int>
 }
)
```

Each new member performs an 
initial sync to catch up to the
primary. Depending on factors such as the amount of data to sync, your
network topology and health, and the power of each host machine,
initial sync may take an extended period of time to complete. 

The replica set may elect a new primary while you add additional 
members. Use `rs.status()` to identify which member is
the current primary. You can only run `rs.add()` from the
primary.

**Step 7: Configure any additional required replication settings.**

The `rs.reconfig()` method updates the replica set
configuration based on a configuration document passed in as a
parameter. You must run `reconfig()`
against the primary member of the replica set.

Reference the original configuration file output of the replica set as 
identified in step A. Review Replica Set Configurations 
and apply settings as needed.

## D. Restore Each Shard Replica Set

**Step 1: Restore the shard primary `mongod` data files.**

Select the tab that corresponds to your preferred backup method:

tabs:

  - id: lvm
    name: "LVM Snapshot"
    content: |

      1. Mount the LVM snapshot on the target host machine. 
         The specific steps for mounting an LVM snapshot depends on 
         your LVM configuration.

         The following example assumes an LVM snapshot created 
         using the lvm-backup-operation step in the
         /tutorial/backup-with-filesystem-snapshots 
         procedure.

         ```bash
         lvcreate --size 250GB --name mongod-datafiles-snapshot vg0
         gzip -d -c mongod-datafiles-snapshot.gz | dd o/dev/vg0/mongod-datafiles-snapshot
         mount /dev/vg0/mongod-datafiles-snapshot /snap/mongodb
         ```

         This example may not apply to all possible LVM 
         configurations. Refer to the LVM documentation for your 
         system for more complete guidance on LVM restoration.

      #. Copy the `mongod` data files from the
         snapshot mount to the data directory created in
         B. Prepare the Target Host for Restoration:

         ```bash
         cp -a /snap/mongodb/path/to/mongodb /path/to/mongodb
         ```

         The `-a` option recursively copies the contents of
         the source path to the destination path while preserving
         folder and file permissions.

      #. Comment out or omit the following 
         configuration file settings:

         ```yaml
         #replication
         #  replSetName: myShardName
         #sharding
         #  clusterRole: shardsvr
         ```

         To start the `mongod` using a 
         configuration file, specify the 
         `--config` option in the command
         line specifying the full path to the configuration file:

         ```bash
         mongod --config /path/to/mongodb/mongod.conf
         ```

         If you have `mongod` configured to 
         run as a system service, start it using the recommended 
         process for your system service manager.

         After the `mongod` starts, connect 
         to it using the `mongo` shell.

  - id: other
    name: "Other Backup Files (NOT mongodump)"
    content: |

      1. Make the data files stored in your selected backup medium
         accessible on the host. This may require mounting the 
         backup volume, opening the backup in a software utility, 
         or using another tool to extract the data to disk. Refer 
         to the documentation for your preferred backup tool for 
         instructions on accessing the data contained in the 
         backup. 

      #. Copy the `mongod` data files from the
         backup data location to the data directory created in
         B. Prepare the Target Host for Restoration:

         ```bash
         cp -a /backup/mongodb/path/to/mongodb /path/to/mongodb
         ```

         The `-a` option recursively copies the contents of
         the source path to the destination path while preserving
         folder and file permissions.

      #. Comment out or omit the following 
         configuration file settings:

         ```yaml
         #replication
         #  replSetName: myShardName
         #sharding
         #  clusterRole: shardsvr
         ```

      #. To start the `mongod` using a 
         configuration file, specify the 
         `--config` option in the command
         line specifying the full path to the configuration file:

         ```bash
         mongod --config /path/to/mongodb/mongod.conf
         ```

         **Note:** Cloud Manager or Ops Manager Only

         If performing a manual restoration of a Cloud Manager 
         or Ops Manager backup, you must specify the 
         `disableLogicalSessionCacheRefresh` server parameter
         prior to startup:

         ```bash
         mongod --config /path/to/mongodb/mongod.conf \
           --setParameter disableLogicalSessionCacheRefresh=true
         ```

         If you have `mongod` configured to 
         run as a system service, start it using the recommended 
         process for your system service manager.

         After the `mongod` starts, connect 
         to it using the `mongo` shell.

**Step 2: Create a temporary user with the `__system` role.**

During this procedure you will modify documents in the
`admin.system.version` collection. For clusters enforcing
authentication, only the `__system`
role grants permission to modify this collection. You can skip this
step if the cluster does not enforce authentication.

**Warning:**

The `__system` role entitles its holder to take any action 
against any object in the database. This procedure includes
instructions for removing the user created in this step. **Do not**
keep this user active beyond the scope of this procedure. 

Consider creating this user with the `clientSource`
authentication restriction
configured such that only the specified hosts can 
authenticate as the privileged user.

a. Authenticate as a user with the `userAdmin` role on the
   `admin` database or
   `userAdminAnyDatabase` role:

   ```javascript
   use admin
   db.auth("myUserAdmin","mySecurePassword")
   ```

#. Create a user with the `__system` role:

   ```javascript
   db.createUser(
     {
       user: "mySystemUser",
       pwd: "<replaceMeWithAStrongPassword>",
       roles: [ "__system" ]
     }
   )
   ```

   Passwords should be random, long, and complex to ensure system
   security and to prevent or delay malicious access. 

#. Authenticate as the privileged user:

   ```javascript
   db.auth("mySystemUser","<replaceMeWithAStrongPassword>")
   ```

**Step 3: Drop the `local` database.**

Use `db.dropDatabase()` to drop the `local` database:

```javascript
use local
db.dropDatabase()
```

**Step 4: Remove the `minOpTimeRecovery` document from the `admin.system.versions` collection.**

To update the sharding internals, issue the following 
`deleteOne()` method on the 
`system.version` collection in the 
`admin` database:

```javascript
use admin
db.system.version.deleteOne( { _id: "minOpTimeRecovery" } )
```

**Note:**

The `system.version` collection is an 
internal, system collection. You should only modify it when when 
given specific instructions like these. 

**Step 5: For any CSRS hostname or replica set name changes, update shard metadata in each shard's identity document.**

You can skip this step if all of the following are true:

* The hostnames for any CSRS host did not change during this procedure.
* The CSRS replica set name did not change during this procedure.

The `system.version`
collection on the `admin` database contains metadata related
to the shard, including the CSRS connection string. If either the
CSRS name or any member hostnames changed while restoring the CSRS,
you must update this metadata.

Issue the following `find()` method on the 
`system.version` collection in the 
`admin` database:

```javascript
use admin
db.system.version.find( {"_id" : "shardIdentity" } )
```

The `find()` method returns a document that
resembles the following:

```javascript
{ 
  "_id" : "shardIdentity", 
  "clusterId" : ObjectId("2bba123c6eeedcd192b19024"), 
  "shardName" : "shard1", 
  "configsvrConnectionString" : "myCSRSName/alpha.example.net:27019,beta.example.net:27019,charlie.example.net:27019" }
```

The following `updateOne` method
updates the document such that the `host` string represents
the most current CSRS connection string:

```javascript
db.system.version.updateOne(
  { "_id" : "shardIdentity" },
  { $set : 
    { "configsvrConnectionString" : "myNewCSRSName/config1.example.net:27019,config2.example.net:27019,config3.example.net:27019"}
  } 
)
```

**Important:**

The `shardName` value must match the `_id` value in the 
`shards` collection on the CSRS. Validate
that the metadata on the CSRS match the metadata for the shard.
Refer to substep 3 in the
C. Restore Config Server Replica Set portion
of this procedure for instructions on viewing the
CSRS metadata.

**Step 6: Restart the `mongod` as a new single-node replica set.**

Shut down the
`mongod`. Uncomment or add the following
configuration file options:

```yaml
replication
  replSetName: myNewShardName
sharding
  clusterRole: shardsvr
```

If you want to change the replica set name, you must update
the `replSetName` field with the new name
before proceeding.

Start the `mongod` with the updated
configuration file:

```bash
mongod --config /path/to/mongodb/mongod.conf
```

If you have `mongod` configured to run as a
system service, start it using the recommended process for your
system service manager.

After the `mongod` starts, connect to it using
the `mongo` shell.

**Step 7: Initiate the new replica set.**

Initiate the replica set using `rs.initiate()` with the 
default settings. 

```javascript
rs.initiate()
```

Once the operation completes, use `rs.status()` to check
that the member has become the primary. 

**Step 8: Add additional replica set members.**

For each replica set member in the shard replica set, start the
`mongod` on its host machine. Once you have
started up all remaining members of the cluster successfully, 
connect a `mongo` shell to the primary replica
set member. From the primary, use the `rs.add()` method to 
add each member of the replica set. Include the replica set name as 
the prefix, followed by the hostname and port of the member's 
`mongod` process:

```javascript
rs.add("repl2.example.net:27018")
rs.add("repl3.example.net:27018")
```

If you want to add the member with specific replica 
`member` configuration settings, you can pass a 
document to `rs.add()` that defines the member hostname
and any `members` settings your deployment requires.

```javascript
rs.add(
 {
   "host" : "repl2.example.net:27018",
   priority: <int>,
   votes: <int>,
   tags: <int>
 }
)
```

Each new member performs an 
initial sync to catch up to the
primary. Depending on factors such as the amount of data to sync, your
network topology and health, and the power of each host machine,
initial sync may take an extended period of time to complete. 

The replica set may elect a new primary while you add additional 
members. Use `rs.status()` to identify which member is
the current primary. You can only run `rs.add()` from the
primary.

**Step 9: Configure any additional required replication settings.**

The `rs.reconfig()` method updates the replica set
configuration based on a configuration document passed in as a
parameter. You must run `reconfig()`
against the primary member of the replica set.

Reference the original configuration file output of the replica set as 
identified in step A. Review Replica Set Configurations 
and apply settings as needed.

**Step 10: Remove the temporary privileged user.**

For clusters enforcing authentication, remove the privileged user 
created earlier in this procedure:

a. Authenticate as a user with the `userAdmin` role on the
   `admin` database or
   `userAdminAnyDatabase` role:

   ```javascript
   use admin
   db.auth("myUserAdmin","mySecurePassword")
   ```

#. Delete the privileged user:

   ```javascript
   db.removeUser("mySystemUser")
   ```

## E. Restart Each `mongos`

Restart each `mongos` in the cluster. 

```bash
mongos --config /path/to/config/mongos.conf
```

Include all other command line options as required by your deployment.

If the CSRS replica set name or any member hostname changed, update the 
`mongos` configuration file setting 
`sharding.configDB` with updated configuration server 
connection string:

```yaml
sharding:
  configDB: "myNewCSRSName/config1.example.net:27019,config2.example.net:27019,config3.example.net:27019"
```

## F. Validate Cluster Accessibility

Connect a `mongo` shell to one of the 
`mongos` processes for the cluster. Use
`sh.status()` to check the overall cluster status. If 
`sh.status()` indicates that the balancer is not running, use 
`sh.startBalancer()` to restart the balancer. [#autosplit]_

To confirm that all shards are accessible and communicating, insert
test data into a temporary sharded collection. Confirm that data is
being split and migrated between each shard in your cluster. You can
connect a `mongo` shell to each shard primary and
use `db.collection.find()` to validate that the data was
sharded as expected.
