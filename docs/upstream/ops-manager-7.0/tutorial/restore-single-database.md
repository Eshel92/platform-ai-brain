<!-- Converted from tutorial/restore-single-database.txt (reStructuredText). Includes are inlined. -->

# Restore a Single Database or Collection

To restore a single database or a collection (or specific documents)
from a snapshot, you can use the
Queryable Backup to export a
single database or collection to restore to the target deployment.

## Considerations

Before you attempt a restore, ensure the host for your target
deployment has sufficient storage space for the restore files and the
restored database, plus additional space for dataset growth. Use
db.stats() to find the current
database size.

**Important:**

Use the latest versions of `MongoDB Database Tools`,
which include `mongodump` and `mongorestore`.
Use  the latest version of `mongosh`.

Older versions of `mongodump` include an issue
that can cause keys in collection options to be dumped in the wrong order.
To learn more, see [TOOLS-3411](https://jira.mongodb.org/browse/TOOLS-3411).

## Restore a Database or Collection from Queryable Backup

You can use a queryable backup snapshot
to export data for a database or a collection and restore to the target
deployment. The following procedure connects to the queryable backup
instance via Ops Manager-provided tunnel [#manual-connect]_.

**Note:**

If the Daemon runs without access to the internet, see
/tutorial/configure-local-mode to install the appropriate
binaries.

**Step 1: Go to Backup view and click the Overview tab.**

For the deployment whose backup you want to query, click
`ellipsis` under Options column then select
Query.

You can also click the deployment to view its snapshots and click
the Query button under the Actions column.

**Step 2: Open a Backup Tunnel to the Queryable Snapshot.**

#. Select the snapshot to query and click Next.

#. Start the process to query a snapshot. You will be
   prompted for 2-factor verification.

#. Select Backup Tunnel as the connection method to the
   queryable snapshot. [#manual-connect]_

#. Select your Platform and download.

#. Uncompress the downloaded file.

   **Note:**

   Wait for the Queryable Snapshot to mount before you
   continue. Snapshot mount time depends on the size of the
   snapshot. Verify the snapshot is mounted by navigating to
   Continuous Backup and selecting the Restore
   History tab. When the snapshot is mounted, the Status
   column reports the date and time of the mount operation.

#. Open a terminal or command prompt and go to the uncompressed
   <tunnel> directory. Run the executable to start the tunnel.

   The default port for the tunnel is `27017`. To change the port,
   use the `--local` flag, as in the following example:

   ```javascript
   ./<tunnel executable> --local localhost:27020
   ```

   **Note:**

   If you change the port, you must include the port information
   when connecting.

**Step 3: Use `mongodump` to export a single database or collection from the queryable backup.**

To export the data for a database,
   Include the following `mongodump` options to
   connect to the tunnel [#manual-connect]_:

   - `--port` set to the port for the tunnel

   - `--db` set to the name of the database to export

   - `--out` set to an empty directory to
     output the data dump.

     **Important:**

     Ensure that the user running `mongodump` can write to
     the specified directory.

   ```sh
   mongodump --port <port for tunnel> --db <single-database> --out <data-dump-path>
   ```

   **Example:**

   To connect to a tunnel running on port `27020` to dump out
   data from the `test` database to
   `/mydata/restoredata/` directory:

   ```sh
   mongodump --port 27020 --db test --out /mydata/restoredata/
   ```

   `mongodump` outputs the `test` database files into the
   `/mydata/restoredata/test/` directory.

   If the `mongodump` is not in your `PATH`, specify the path
   for the tool.

To export the data for a collection,
   include the following options to connect to the tunnel [#manual-connect]_:

   - `--port` set to the port for the tunnel.

   - `--db` set to the name of the database to export.

   - `--collection` for a single
     collection.

   - `--out` set to an empty directory to
     output the data dump.

     **Important:**

     Ensure that the user running `mongodump` can
     write to the specified directory.

   ```sh
   mongodump --port <port for tunnel> \
             --db <single-database> \
             --collection <collection-name> \
             --out <data-dump-path>
   ```

   **Example:**

   To connect to a tunnel running on port `27020` to dump out
   data from the `restaurants` collection from `test`
   database to `/mydata/restoredata/` directory:

   ```sh
   mongodump --port 27020 \
             --db test \
             --collection restaurants \
             --out /mydata/restoredata/
   ```

   `mongodump` outputs the `restaurants` collection data into
   the `/mydata/restoredata/test/restaurants.bson` file.

**Step 4: Use `mongorestore` to restore the single database or collection.**

To restore a single database,
   Include the following  `mongorestore` options:

   - `--port` set to the port of the destination cluster.

   - `--db` set to the name of the destination database.

   Optionally, you can include `--drop` to
   drop the database in the destination cluster if the database
   already exists.

```sh
mongorestore --port <port> --db <destination database> <data-dump-path/database> --drop
```

For example, to restore from the `/mydata/restoredata/test`
directory to a new database `restoredTest`:

```sh
mongorestore --port 27017 --db restoredTest /mydata/restoredata/test --drop
```

The example assumes that the destination replica set's primary or
the destination sharded cluster's `mongos` listens on port
`27017`.

To restore a single collection,
   Include the following `mongorestore` options:

   - `--port` set to the port of the destination cluster.

   - `--db` set to the name of the destination database.

   Optionally, you can include `--drop` to
   drop the collection in the destination cluster if the collection
   already exists.

```sh
mongorestore --port <port> --db <destination database> --collection <collection-name> <data-dump-path/dbname/collection.bson> --drop
```

For example, to restore from the
`/mydata/restoredata/test/restaurants.bson` data file to a new
collection `rest2` in the `test2` database:

```sh
mongorestore --port 27017 --db test2 --collection rest2 /mydata/restoredata/test/restaurants.bson --drop
```

The example assumes that the destination replica set's primary or
the destination sharded cluster's `mongos` listens on port
`27017`.

**Step 5: Terminate the queryable instance.**

Once you have finished, you can terminate the
queryable instance:

#. Go to the Restore History and hover over the
   Status column for the deployment item.

#. Click Cancel.

**Important:** Rotate Master Key after Restoring Snapshots Encrypted with AES256-GCM

If you restore an
encrypted snapshot that Ops Manager
encrypted with AES256-GCM (Advanced Encryption Standards 256-bit Galois/Counter Mode),
rotate your master key
after completing the restore.
