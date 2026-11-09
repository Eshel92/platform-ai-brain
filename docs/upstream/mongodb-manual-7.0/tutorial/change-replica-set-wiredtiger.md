<!-- Converted from tutorial/change-replica-set-wiredtiger.txt (reStructuredText). Includes are inlined. -->

# Change a Self-Managed Replica Set to WiredTiger

**Note:**

- .. include:: /includes/collMod-note.rst

- You must upgrade to WiredTiger. MongoDB removed the deprecated MMAPv1 
  storage engine in version 4.2. 

Use this tutorial to update a replica set to use WiredTiger. The procedure updates the replica set in a
rolling fashion to avoid downtime.

## Considerations

Replica sets can have members with different storage engines. As such,
you can update members to use the WiredTiger storage engine in a
rolling fashion.

### PSA 3-member Architecture

The `"majority"` read concern, available for WiredTiger, 
is enabled by default. However, in three-member replica sets with a 
primary-secondary-arbiter (PSA) architecture, you can disable the 
`"majority"` read concern. 
Disabling the `"majority"` read concern for a three-member 
PSA architecture avoids possible cache-pressure build up.

The procedure
below disables `"majority"` read concern for
PSA architecture by including
`--enableMajorityReadConcern false`.  

**Note:**

Disabling `"majority"` read concern has no effect on change
streams availability.

For more information on PSA architecture and read concern
`"majority"`,
see disable-read-concern-majority.

### Default Bind to Localhost

MongoDB binaries, `mongod` and
`mongos`, bind to `localhost` by default.

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

The following procedure updates the replica set in a rolling fashion.
The procedure updates the secondary members first, then steps
down the primary, and updates the stepped-down member.

To update a member to WiredTiger, the procedure removes a member's
data, starts `mongod` with WiredTiger, and performs an
initial sync.

### A. Update the secondary members to WiredTiger.

Update the secondary members one at a time:

**Step 1: Shut down the secondary member.**

In `mongosh`, shut down the secondary.

```sh
use admin
db.shutdownServer()
```

**Step 2: Prepare a data directory for the new `mongod` running with WiredTiger.**

Prepare a data directory for the new `mongod` instance that
will run with the WiredTiger storage engine. `mongod` must have read
and write permissions for this directory. You can either delete the
contents of the stopped secondary member's current data directory or
create a new directory entirely.

`mongod` with WiredTiger will not start with data files created with
a different storage engine.

**Step 3: Update configuration for WiredTiger.**

Remove any MMAPv1 configuration options from the `mongod`
instance configuration.

**Step 4: Start `mongod` with WiredTiger.**

Start `mongod`, specifying `wiredTiger` as the
`--storageEngine` and the prepared data directory for
WiredTiger as the `--dbpath`.

Specify additional options as appropriate, such as
`--bind_ip`.

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

tabs:
   - id: general
     name: General Use (For Most Architectures)
     content: |

       ```bash
       mongod --storageEngine wiredTiger --dbpath <newWiredTigerDBPath> --replSet <replSetName> --bind_ip localhost,<hostname(s)|ip address(es)>
       ```

   - id: psa36
     name: PSA Architecture
     content: |

       **Important:**

       If you are running a three-member PSA architecture, include
       `--enableMajorityReadConcern false` 
       to disable read concern `majority`. See rs-mmapv1-wt-4.0-psa.

       ```bash
       mongod --storageEngine wiredTiger --dbpath <newWiredTigerDBPath> --replSet <replSetName> --bind_ip localhost,<hostname(s)|ip address(es)> --enableMajorityReadConcern false
       ```

Since no data exists in the `--dbpath`, the `mongod` will perform an
initial sync. The length of the
initial sync process depends on the size of the database and network
connection between members of the replica set.

You can also specify the options in a configuration file. To specify the storage engine, use
the `storage.engine` setting.

Repeat the steps for the remaining secondary members, updating them one
at a time.

### B. Step down the primary.

**Important:**

If updating all members of the replica set to use WiredTiger, ensure
that all secondary members have been updated first before updating
the primary.

Once all the secondary members have been upgraded to WiredTiger,
connect `mongosh` to the primary and use
`rs.stepDown()` to step down the primary and force an election
of a new primary.

```javascript
rs.stepDown()
```

### C. Update the stepped down primary.

When the primary has stepped down and become a secondary, update the
secondary to use WiredTiger as before:

**Step 1: Shut down the secondary member.**

In `mongosh`, shut down the secondary.

```sh
use admin
db.shutdownServer()
```

**Step 2: Prepare a data directory for the new `mongod` running with WiredTiger.**

Prepare a data directory for the new `mongod` instance that
will run with the WiredTiger storage engine. `mongod` must have read
and write permissions for this directory. You can either delete the
contents of the stopped secondary member's current data directory or
create a new directory entirely.

`mongod` with WiredTiger will not start with data files created with
a different storage engine.

**Step 3: Update configuration for WiredTiger.**

Remove any MMAPv1 configuration options from the `mongod`
instance configuration.

**Step 4: Start `mongod` with WiredTiger.**

Start `mongod`, specifying `wiredTiger` as the
`--storageEngine` and the prepared data directory for
WiredTiger as the `--dbpath`.

Specify additional options as appropriate, such as
`--bind_ip`.

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

tabs:
   - id: general
     name: General Use (For Most Architectures)
     content: |

       ```bash
       mongod --storageEngine wiredTiger --dbpath <newWiredTigerDBPath> --replSet <replSetName> --bind_ip localhost,<hostname(s)|ip address(es)>
       ```

   - id: psa36
     name: PSA Architecture
     content: |

       **Important:**

       If you are running a three-member PSA architecture, include
       `--enableMajorityReadConcern false` 
       to disable read concern `majority`. See rs-mmapv1-wt-4.0-psa.

       ```bash
       mongod --storageEngine wiredTiger --dbpath <newWiredTigerDBPath> --replSet <replSetName> --bind_ip localhost,<hostname(s)|ip address(es)> --enableMajorityReadConcern false
       ```

Since no data exists in the `--dbpath`, the `mongod` will perform an
initial sync. The length of the
initial sync process depends on the size of the database and network
connection between members of the replica set.

You can also specify the options in a configuration file. To specify the storage engine, use
the `storage.engine` setting.
