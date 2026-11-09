<!-- Converted from tutorial/recover-data-following-unexpected-shutdown.txt (reStructuredText). Includes are inlined. -->

# Recover a Self-Managed Standalone after Unexpected Shutdown

**Warning:**

The following procedure applies to standalone `mongod`
instance version 7.0. For other MongoDB versions, refer to
the corresponding version of the manual.

Do not use this tutorial to recover a member of a replica
set. Instead, you should either restore from a backup or resync from another member of the set, as
described in /tutorial/resync-replica-set-member.

**Tip:**

If you are running with journaling enabled, there is
almost never any need to run repair since the server can use the
journal files to restore the data files to a clean state automatically.
However, you may need to run repair in cases where you need to recover
from a disk-level data corruption.

Disk-level data corruption or missing data files can prevent
`mongod` instance from starting, and journal files may be
insufficient to recover automatically:

```none
2018-10-24T18:05:18.248-04:00 W STORAGE  [initandlisten] Detected unclean shutdown - mongod.lock is not empty.

...

2018-10-24T17:24:53.122-04:00 E STORAGE  [initandlisten] Failed to get the cursor for uri: table:collection-2-6854866147293273505
2018-10-24T17:24:53.122-04:00 E STORAGE  [initandlisten] This may be due to missing data files. ...

...

***aborting after fassert() failure
```

In such cases, your `dbPath` contains a non-empty
`mongod.lock` file.

The following procedure uses `mongod --repair` to recover from
these cases:

**Warning:**

Only use `mongod --repair` if you have no other options.
The operation removes and does not save any corrupt data during the
repair process.

For the WiredTiger storage engine, `mongod --repair`:

- Rebuilds all indexes for collections with one or more inconsistent 
  indexes.

- Discards corrupt data.

- Creates empty/stub files for missing data/metadata files.

## Procedure

**Important:**

Run the repair operation as the same user that normally runs the
`mongod` process to avoid changing the permissions of the
MongoDB data files.

**Step 1: Create a backup of the data files.**

Create a backup copy of the data files in the `--dbpath`.

**Step 2: Start `mongod` with `--repair`.**

To repair the data files, start the `mongod` instance with
the `--repair` option.

Issue a command similar to the following for your standalone:

```sh
mongod --dbpath /data/db --repair
```

Upon completion, the `dbpath` should contain the repaired data files and an empty `mongod.lock` file. [#manual-removal]_

**Note:**

If the repair fails to complete for any reason, you
must restart the instance with the `--repair` option to complete the repair.
