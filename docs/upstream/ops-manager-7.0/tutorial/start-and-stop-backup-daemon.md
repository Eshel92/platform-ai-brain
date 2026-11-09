<!-- Converted from tutorial/start-and-stop-backup-daemon.txt (reStructuredText). Includes are inlined. -->

# Start and Stop the Backup Daemon

The Ops Manager Application manages backups. To ensure high availability of backups,
deploy sufficient number of Ops Manager hosts with a load balancer. To learn
how to deploy Ops Manager with high availability, see
/tutorial/configure-application-high-availability.

Even though we recommend that you deploy Ops Manager with high
availability, you
must run at least one Backup Daemon on a server.

The following procedure demonstrates how to start and stop the
Backup Daemon on a server.

## Procedure

1. Start the Backup Daemon:

   ```sh
   /etc/init.d/mongodb-mms-backup-daemon start
   ```

#. Stop the Backup Daemon:

   ```sh
   /etc/init.d/mongodb-mms-backup-daemon stop
   ```

#. Restart the Backup Daemon:

   ```sh
   /etc/init.d/mongodb-mms-backup-daemon restart
   ```

#. Check the status of the Backup Daemon:

   ```sh
   /etc/init.d/mongodb-mms-backup-daemon status
   ```

## Additional Information

To move jobs from a lost Backup server to another Backup server, see
/tutorial/move-jobs-to-new-backup-daemon.
