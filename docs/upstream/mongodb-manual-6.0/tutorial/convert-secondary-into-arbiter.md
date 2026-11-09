<!-- Converted from tutorial/convert-secondary-into-arbiter.txt (reStructuredText). Includes are inlined. -->

# Convert a Self-Managed Secondary to an Arbiter

If you have a secondary in a replica set that no
longer needs to hold data but that needs to remain in the set to
ensure that the set can elect a primary, you may convert the secondary to an
arbiter using either procedure in this
tutorial. Both procedures are operationally equivalent:

- You may operate the arbiter on the same port as the former secondary.
  In this procedure, you must shut down the secondary and remove its
  data before restarting and reconfiguring it as an arbiter.

  For this procedure, see replica-set-convert-secondary-to-arbiter-same-port.

- Run the arbiter on a new port. In this procedure, you can reconfigure
  the server as an arbiter before shutting down the instance running as
  a secondary.

  For this procedure, see replica-set-convert-secondary-to-arbiter.

## Convert Secondary to Arbiter and Reuse the Port Number

#. If your application is connecting directly to the secondary,
   modify the application so that MongoDB queries don't reach
   the secondary.

#. Shut down the secondary.

#. Remove the secondary from the replica set by calling
   the `rs.remove()` method. Perform this operation while connected to the current
   primary in `mongosh`:

   ```javascript
   rs.remove("<hostname><:port>")
   ```

#. Verify that the replica set no longer includes the secondary by
   calling the `rs.conf()` method in `mongosh`:

   ```javascript
   rs.conf()
   ```

#. Move the secondary's data directory to an archive folder. For example:

   ```bash
   mv /data/db /data/db-old
   ```

   **Note:** Optional

   You may remove the data instead.

#. Create a new, empty data directory to point to when restarting the
   `mongod` instance. You can reuse the previous name. For
   example:

   ```bash
   mkdir /data/db
   ```

#. Restart the `mongod` instance for the secondary, specifying
   the port number, the empty data directory, and the replica set. You
   can use the same port number you used before. Issue a command similar
   to the following:

   **Warning:**

   Before binding to a non-localhost (e.g. publicly accessible) 
   IP address, ensure you have secured your cluster from unauthorized
   access. For a complete list of security recommendations, see 
   /administration/security-checklist. At minimum, consider 
   enabling authentication and 
   hardening network infrastructure.

   ```bash
   mongod --port 27021 --dbpath /data/db --replSet rs  --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

#. In `mongosh` convert the secondary to an arbiter
   using the `rs.addArb()` method:

   ```javascript
   rs.addArb("<hostname><:port>")
   ```

#. Verify the arbiter belongs to the replica set by calling the
   `rs.conf()` method in `mongosh`.

   ```javascript
   rs.conf()
   ```

   The arbiter member should include the following:

   ```javascript
   "arbiterOnly" : true
   ```

## Convert Secondary to Arbiter Running on a New Port Number

#. If your application is connecting directly to the secondary
   or has a connection string referencing the secondary,
   modify the application so that MongoDB queries don't reach
   the secondary.

#. Create a new, empty data directory to be used with the new port
   number. For example:

   ```bash
   mkdir /data/db-temp
   ```

#. Start a new `mongod` instance on the new port number,
   specifying the new data directory and the existing replica
   set. Issue a command similar to the following:

   **Warning:**

   Before binding to a non-localhost (e.g. publicly accessible) 
   IP address, ensure you have secured your cluster from unauthorized
   access. For a complete list of security recommendations, see 
   /administration/security-checklist. At minimum, consider 
   enabling authentication and 
   hardening network infrastructure.

   ```bash
   mongod --port 27021 --dbpath /data/db-temp --replSet rs --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

#. In `mongosh` connected to the current primary,
   convert the new `mongod` instance to an arbiter using the `rs.addArb()`
   method:

   ```javascript
   rs.addArb("<hostname><:port>")
   ```

#. Verify the arbiter has been added to the replica set by calling the
   `rs.conf()` method in `mongosh`.

   ```javascript
   rs.conf()
   ```

   The arbiter member should include the following:

   ```javascript
   "arbiterOnly" : true
   ```

#. Shut down the secondary.

#. Remove the secondary from the replica set by calling
   the `rs.remove()` method in `mongosh`:

   ```javascript
   rs.remove("<hostname><:port>")
   ```

#. Verify that the replica set no longer includes the old secondary by
   calling the `rs.conf()` method in `mongosh`:

   ```javascript
   rs.conf()
   ```

#. Move the secondary's data directory to an archive folder. For example:

   ```bash
   mv /data/db /data/db-old
   ```

   **Note:** Optional

   You may remove the data instead.
