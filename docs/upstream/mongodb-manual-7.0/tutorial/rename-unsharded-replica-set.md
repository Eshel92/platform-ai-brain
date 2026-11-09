<!-- Converted from tutorial/rename-unsharded-replica-set.txt (reStructuredText). Includes are inlined. -->

# Rename a Self-Managed Replica Set

To rename a replica set, you must shut down all members of the replica 
set, then configure each member's `local` database with the new 
replica set name.

This procedure requires downtime.

## Prerequisites

- Ensure that your replica set is not sharded. The renaming procedure 
  is for unsharded replica sets only. 

- Before renaming a replica set, perform a full
  backup of your MongoDB deployment.

- When authentication is enabled, ensure that 
  your user role has `find`, `insert`, and `remove`
  privileges on the `system.replset` collection in each member's 
  `local` database.

  **Tip:**

  You can view the privileges for a role by issuing the `rolesInfo` 
  command with the `showPrivileges` and `showBuiltinRoles` fields both set to `true`.

## Procedure

**Step 1: Shut down replica set members.**

Follow the procedure in Stop a Replica Set
to confirm that replica set members are 
shut down.

**Warning:**

This step requires downtime as all replica members will need to be 
shut down.

**Step 2: Rename the replica set.**

Perform the following steps for each replica set member:

a. Start the replica set member on a different port without the
   `--replSet` option. 

#. Update the replica set name. 

   - If using a configuration file, set 
     `replication.replSetName` 
     to the new name. 

   - If using the `mongod` startup command with 
     the `--replSet` option, note down the 
     new replica set name for use in step f.

#. Connect to the replica set member. 

#. Update the replica set name in the local database with the following commands:

   ```javascript
   /* Set `newId` to the new replica set name */
   var newId = '<new replica set name>'

   var doc = db.getSiblingDB("local").system.replset.findOne()
   var oldId = doc._id
   doc._id = newId
   db.getSiblingDB("local").system.replset.insertOne(doc)
   db.getSiblingDB("local").system.replset.deleteOne({_id: oldId})
   ```

#. Shut down the replica set 
   member.

   **Note:** Ops Manager

   If you are using Ops Manager, you must stop Ops Manager
   from managing the replica set before you shut down the 
   replica set member. For more information on this procedure,
   see `Remove a Process from Ops Management`

#. Start the replica set member on its original port. 

   - If using a configuration file, ensure that 
     `replication.replSetName` is 
     set to the new replica set name.

   - If using the `mongod` startup command with 
     the `--replSet` option, pass the new 
     name of the replica set to the 
     `--replSet` option.
