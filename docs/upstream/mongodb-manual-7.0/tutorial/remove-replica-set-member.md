<!-- Converted from tutorial/remove-replica-set-member.txt (reStructuredText). Includes are inlined. -->

# Remove Members from a Self-Managed Replica Set

To remove a member of a replica set use either of the
following procedures.

## Remove a Member Using `rs.remove()`

1. Shut down the `mongod` instance for the member you wish to
   remove. To shut down the instance, connect using
   `mongosh` and use the `db.shutdownServer()`
   method.

#. Connect to the replica set's current primary. To determine
   the current primary, use `db.hello()` while connected to
   any member of the replica set.

#. Use `rs.remove()` in either of the following forms to
   remove the member:

   ```javascript
   rs.remove("mongod3.example.net:27017")
   rs.remove("mongod3.example.net")
   ```

   MongoDB may disconnect the shell briefly if the replica set needs to elect a
   new primary. The shell then automatically reconnects in such cases. The
   shell may display a `DBClientCursor::init call() failed` error even
   though the command succeeds.

## Remove a Member Using `rs.reconfig()`

You can remove a member by reconfiguring the replica set 
using a replica configuration
document where that member 
is removed from the `members` array.

`rs.reconfig()` allows adding or removing no more than `1` 
`voting` member at a time. To remove multiple voting 
members from the replica set, issue a series of `rs.reconfig()` 
operations to remove one member at a time. See 
replSetReconfig-cmd-single-node for more information.

### Procedure

1. Shut down the `mongod` instance for the member you wish to
   remove. To shut down the instance, connect using
   `mongosh` and use the `db.shutdownServer()`
   method.

#. Connect to the replica set's current primary. To determine
   the current primary, use `db.hello()` while connected to
   any member of the replica set.

#. Issue the `rs.conf()` method to view the current
   configuration document and determine the position in the
   `members` array of the member to remove:

   **Example:**

   `mongod_C.example.net` is in position `2` of the
   following configuration file:

   ```javascript
   {
       "_id" : "rs",
       "version" : 7,
       "members" : [
           {
               "_id" : 0,
               "host" : "mongod_A.example.net:27017"
           },
           {
               "_id" : 1,
               "host" : "mongod_B.example.net:27017"
           },
           {
               "_id" : 2,
               "host" : "mongod_C.example.net:27017"
           }
       ]
   }
   ```

#. Assign the current configuration document to the variable `cfg`:

   ```javascript
   cfg = rs.conf()
   ```

#. Modify the `cfg` object to remove the member.

   **Example:**

   To remove `mongod_C.example.net:27017` use the following
   JavaScript operation:

   ```javascript
   cfg.members.splice(2,1)
   ```

#. Overwrite the replica set configuration document with the new
   configuration by issuing the following:

   ```javascript
   rs.reconfig(cfg)
   ```

#. To confirm the new configuration, issue `rs.conf()`.

   For the example above the output would be:

   ```javascript
   {
       "_id" : "rs",
       "version" : 8,
       "members" : [
           {
               "_id" : 0,
               "host" : "mongod_A.example.net:27017"
           },
           {
               "_id" : 1,
               "host" : "mongod_B.example.net:27017"
           }
       ]
   }
   ```
