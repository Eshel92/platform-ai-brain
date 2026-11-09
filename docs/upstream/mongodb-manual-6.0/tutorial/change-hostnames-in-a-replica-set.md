<!-- Converted from tutorial/change-hostnames-in-a-replica-set.txt (reStructuredText). Includes are inlined. -->

# Change Hostnames in a Self-Managed Replica Set

For most replica sets, the hostnames in the 
`members[n].host` field never change. However, if the
organization's needs change, you might need to migrate some or all host names.

**Note:** Always use resolvable hostnames for the value of the

set configuration to avoid confusion and complexity.

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

## Overview

This document provides two separate procedures for changing the
hostnames in the `members[n].host`
field. Use either of the following approaches:

- Change hostnames without disrupting availability. This approach ensures your
  applications will always be able to read and write data to the replica
  set, but the approach can take a long time and may incur downtime at
  the application layer.

  If you use the first procedure, you must configure your applications
  to connect to the replica set at both the old and new locations, which
  often requires a restart and reconfiguration at the application layer
  and which may affect the availability of your applications.
  Re-configuring applications is beyond the scope of this document.

- Stop all members running on the old hostnames at once. This approach has a shorter
  maintenance window, but the replica set will be unavailable during
  the operation.

**See also:**

- Replica Set Reconfiguration Process
- /tutorial/deploy-replica-set
- /tutorial/expand-replica-set

## Assumptions

Given a replica set with three members:

- `database0.example.com:27017` (the primary)

- `database1.example.com:27017`

- `database2.example.com:27017`

And with the following `rs.conf()` output:

```javascript
{
    "_id" : "rs",
    "version" : 3,
    "members" : [
        {
            "_id" : 0,
            "host" : "database0.example.com:27017"
        },
        {
            "_id" : 1,
            "host" : "database1.example.com:27017"
        },
        {
            "_id" : 2,
            "host" : "database2.example.com:27017"
        }
    ]
}
```

The following procedures change the members' hostnames as follows:

- `mongodb0.example.net:27017` (the primary)

- `mongodb1.example.net:27017`

- `mongodb2.example.net:27017`

Use the most appropriate procedure for your deployment.

## Change Hostnames while Maintaining Replica Set Availability

This procedure uses the above assumptions.

#. For each secondary in the replica set, perform the
   following sequence of operations:

   a. Stop the secondary.

   #. Restart the secondary at the new location.

   #. Connect `mongosh` to the replica set's primary. In
      our example, the primary runs on port `27017` so you would
      issue the following command:

      ```bash
      mongosh --port 27017
      ```

   #. Use `rs.reconfig()` to update the replica set
      configuration document with
      the new hostname.

      For example, the following sequence of commands updates the
      hostname for the secondary at the array index `1` of the
      `members` array (i.e. `members[1]`) in the replica set
      configuration document:

      ```javascript
      cfg = rs.conf()
      cfg.members[1].host = "mongodb1.example.net:27017"
      rs.reconfig(cfg)
      ```

      For more information on updating the configuration document, see
      replica-set-reconfiguration-usage.

   #. Make sure your client applications are able to access the
      set at the new location and that the secondary has a chance to
      catch up with the other members of the set.

      Repeat the above steps for each non-primary member of the set.

#. Connect `mongosh` to the primary and step down the
   primary using the `rs.stepDown()` method:

   ```javascript
   rs.stepDown()
   ```

   The replica set elects another member to the become primary.

#. When the step down succeeds, shut down the old primary.

#. Start the `mongod` instance that will become the new primary
   in the new location.

#. Connect to the current primary, which was just elected, and update
   the replica set configuration document with the hostname of the node that
   is to become the new primary.

   For example, if the old primary was at position `0` and the new
   primary's hostname is `mongodb0.example.net:27017`, you would run:

   ```javascript
   cfg = rs.conf()
   cfg.members[0].host = "mongodb0.example.net:27017"
   rs.reconfig(cfg)
   ```

#. Connect `mongosh` to the new primary.

#. To confirm the new configuration, call `rs.conf()` in
   `mongosh`.

   Your output should resemble:

   ```javascript
   {
       "_id" : "rs",
       "version" : 4,
       "members" : [
           {
               "_id" : 0,
               "host" : "mongodb0.example.net:27017"
           },
           {
               "_id" : 1,
               "host" : "mongodb1.example.net:27017"
           },
           {
               "_id" : 2,
               "host" : "mongodb2.example.net:27017"
           }
       ]
   }
   ```

## Change All Hostnames at the Same Time

This procedure uses the above assumptions.

### Prerequisites

The following procedure reads and updates the `system.replset`
collection in the `local` database.

If your deployment enforces access control, the user performing the procedure must have
`find` and `update` privilege actions on the
`system.replset` collection.

To create a role that provides the necessary privileges:

#. Log in as a user with privileges to manage users and roles, such as
   a user with `userAdminAnyDatabase` role. The following
   procedure uses the `myUserAdmin` created in
   /tutorial/enable-authentication.

   ```javascript
   mongosh --port 27017 -u myUserAdmin --authenticationDatabase 'admin' -p 
   ```

#. Create a user role that provides the necessary privileges on the
   `system.replset` collection in the `local` database:

   ```javascript
   db.adminCommand( { 
      createRole: "systemreplsetRole",
      privileges: [
         { resource: { db: "local", collection: "system.replset" }, actions: ["find","update"] } 
      ],
      roles: []
   } );
   ```

#. Grant the role to the user who will be performing the rename
   procedure. For example, the following assumes an existing user
   `"userPerformingRename"` in the `admin` database.

   ```javascript
   use admin
   db.grantRolesToUser( "userPerformingRename", [ { role: "systemreplsetRole", db: "admin" } ] ); 
   ```

### Procedure

#. Stop all members in the replica set.

#. Restart each member *on a different port* and *without* using the
   `--replSet` run-time option. Changing
   the port number during maintenance prevents clients from connecting
   to this host while you perform maintenance. Use the member's usual
   `--dbpath`, which in this
   example is `/data/db1`. Use a command that resembles the following:

   **Warning:**

   Before binding to a non-localhost (e.g. publicly accessible) 
   IP address, ensure you have secured your cluster from unauthorized
   access. For a complete list of security recommendations, see 
   /administration/security-checklist. At minimum, consider 
   enabling authentication and 
   hardening network infrastructure.

   ```bash
   mongod --dbpath /data/db1/ --port 37017 --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

   **Important:**

   To avoid configuration updates due to IP address changes, use DNS
   hostnames instead of IP addresses. It is particularly important to
   use a DNS hostname instead of an IP address when configuring replica
   set members or sharded cluster members.

   Use hostnames instead of IP addresses to configure clusters across a
   split network horizon. Starting in MongoDB 5.0, nodes that are only
   configured with an IP address fail startup validation and do not start.

      
#. For each member of the replica set, perform the following sequence
   of operations:

   a. Connect `mongosh` to the `mongod`
      running on the new, temporary port. For example, for a member
      running on a temporary port of `37017`, you would issue this
      command:

      ```bash
      mongosh --port 37017
      ```

      If running with access control, connect as a user with
      appropriate privileges. See
      repl-set-change-hostname-prereq.

      ```bash
      mongosh --port 37017 -u userPerformingRename --authenticationDatabase=admin  -p
      ```

   #. Edit the replica set configuration manually. The replica set
      configuration is the only document in the `system.replset`
      collection in the `local` database. 

      |

      To change the hostnames, edit the replica set configuration to
      provide the new hostnames and ports for all members of the
      replica set.

      #. Switch to the `local` database.

         ```javascript
         use local
         ```

      #. Create a JavaScript variable for the configuration document.
         Modify the value of the `_id` field to match your replica
         set.

         ```javascript
         cfg = db.system.replset.findOne( { "_id": "rs0" } )
         ```

      #. Provide new hostnames and ports for each member of the replica
         set. Modify the hostnames and ports to match your replica set.

         ```javascript
         cfg.members[0].host = "mongodb0.example.net:27017"
         cfg.members[1].host = "mongodb1.example.net:27017"
         cfg.members[2].host = "mongodb2.example.net:27017"
         ```

      #. Update the hostnames and ports in the `system.replset`
         collection:

         ```javascript
         db.system.replset.updateOne( { "_id": "rs0" }, { $set: cfg } )
         ```

      #. Verify the changes:

         ```javascript
         db.system.replset.find( {}, { "members.host": 1 } )
         ```

   #. Stop the `mongod` process on the member.

#. After re-configuring all members of the set, start each
   `mongod` instance in the normal way: use the usual port
   number and use the `--replSet` option. For
   example:

   **Warning:**

   Before binding to a non-localhost (e.g. publicly accessible) 
   IP address, ensure you have secured your cluster from unauthorized
   access. For a complete list of security recommendations, see 
   /administration/security-checklist. At minimum, consider 
   enabling authentication and 
   hardening network infrastructure.

   ```bash
   mongod --dbpath /data/db1/ --port 27017 --replSet rs0 --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

#. Connect to one of the `mongod` instances
   using `mongosh`. For example:

   ```bash
   mongosh --port 27017
   ```

#. To confirm the new configuration, call `rs.conf()` in
   `mongosh`.

   Your output should resemble:

   ```javascript
   {
       "_id" : "rs0",
       "version" : 4,
       "members" : [
           {
               "_id" : 0,
               "host" : "mongodb0.example.net:27017"
           },
           {
               "_id" : 1,
               "host" : "mongodb1.example.net:27017"
           },
           {
               "_id" : 2,
               "host" : "mongodb2.example.net:27017"
           }
       ]
   }
   ```
