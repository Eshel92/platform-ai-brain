<!-- Converted from tutorial/change-standalone-wiredtiger.txt (reStructuredText). Includes are inlined. -->

# Change a Self-Managed Standalone to WiredTiger

**Note:**

You must upgrade to WiredTiger. MongoDB removed the deprecated MMAPv1 storage 
engine in version 4.2. 

Use this tutorial to change the storage engine of a standalone
MongoDB instance to WiredTiger.

## Considerations

### `mongodump` and `mongorestore`

This tutorial uses the `mongodump` and
`mongorestore` utilities to export and import data.

- Ensure that these MongoDB package components are installed and
  updated on your system.

- Make sure you have sufficient drive space available for the
  `mongodump` export file and the data files of your new
  `mongod` instance running with WiredTiger.

### Default Bind to Localhost

MongoDB binaries, `mongod` and
`mongos`, bind to `localhost` by default.

The tutorial runs `mongodump` and
`mongorestore` from the same host as the
`mongod` they are connecting to. If run remotely,
`mongodump` and `mongorestore` must specify
the ip address or the associated hostname in order to connect to the
`mongod`.

### XFS and WiredTiger

With the WiredTiger storage engine, using XFS for data bearing nodes is
recommended on Linux. For more information, see
prod-notes-linux-file-system.

### MMAPv1 Only Restrictions

Once upgraded to WiredTiger, your WiredTiger deployment is **not**
subject to the following MMAPv1-only restrictions:

| MMAPv1 Restrictions | Short Description |
|---|---|
| Number of Namespaces | For MMAPv1, the number of namespaces is limited to the size of the namespace file divided by 628. |
| Size of Namespace File | For MMAPv1, namespace files can be no larger than 2047 megabytes. |
| Database Size | The MMAPv1 storage engine limits each database to no more than 16000 data files. |
| Data Size | For MMAPv1, a single `mongod` instance cannot manage a data set that exceeds maximum virtual memory address space provided by the underlying operating system. |
| Number of Collections in a Database | For the MMAPv1 storage engine, the maximum number of collections in a database is a function of the size of the namespace file and the number of indexes of collections in the database. |

## Procedure

**Step 1: Start the `mongod` you wish to change to WiredTiger.**

If `mongod` is already running, you can skip this step.

**Step 2: Export data using `mongodump`.**

```sh
mongodump --out=<exportDataDestination>
```

Specify additional options as appropriate, such as username and
password if running with authorization enabled. See
`mongodump` for available options.

**Step 3: Create a data directory for the new `mongod` running with WiredTiger.**

Create a data directory for the new `mongod` instance that
will run with the WiredTiger storage engine. `mongod` must have read
and write permissions for this directory.

`mongod` with WiredTiger will not start with data files created with
a different storage engine.

**Step 4: Update configuration for WiredTiger.**

Remove any MMAPv1 configuration options from the `mongod`
instance configuration.

**Step 5: Start `mongod` with WiredTiger.**

Start `mongod`, specifying `wiredTiger` as the
`--storageEngine` and the newly
created data directory for WiredTiger as the `--dbpath`.

Specify additional options as appropriate, such as
`--bind_ip`.

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

```sh
mongod --storageEngine wiredTiger --dbpath <newWiredTigerDBPath> --bind_ip localhost,<hostname(s)|ip address(es)>
```

You can also specify the options in a configuration file. To specify the storage engine, use
the `storage.engine` setting.

**Step 6: Upload the exported data using `mongorestore`.**

```sh
mongorestore <exportDataDestination>
```

Specify additional options as appropriate. See
`mongorestore` for available options.
