<!-- Converted from reference/command/replSetResizeOplog.txt (reStructuredText). Includes are inlined. -->

# replSetResizeOplog (database command)

## Definition

**`replSetResizeOplog`**

`replSetResizeOplog` also supports specifying the minimum number 
of hours to preserve an oplog entry.

**Changed in version:** 5.0

To set the `replSetOplog` size in `mongosh`, use
the `Double()` constructor. 

`replSetResizeOplog` enables you to resize the oplog or
its minimum retention period dynamically without restarting the
`mongod` process. 

You must run this command against the `admin` database.

## Compatibility

This command is available in deployments hosted in the following environments: 

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

To resize the oplog in Atlas, see set-oplog-min-window.

## Syntax

The command has the following form:

```javascript
db.adminCommand(
   { 
     replSetResizeOplog: <int>, 
     size: <double>, 
     minRetentionHours: <double>
   }
 )
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `replSetResizeOplog`
  - int
  - Set to `1`. 

* - `size`
  - double
  - The maximum size of the oplog in megabytes.

    - The minimum size you can specify is 990 megabytes.

    - The maximum size you can specify is 1 petabytes.

    - Explicitly cast the `size` as a double in
      `mongosh` with `Double()`. See
      oplog-ex-change-size.

* - `minRetentionHours`
  - double
  - *Optional*. The minimum number of hours to preserve an oplog
    entry, where decimal values represent the fractions of an
    hour. For example, a value of `1.5` represents one hour and
    thirty minutes.

    The value must be greater than or equal to `0`. A value of
    `0` indicates that the `mongod` should
    truncate the oplog starting with the oldest entries to
    maintain the configured maximum oplog size.

    A `mongod` configured with
    `minRetentionHours` only removes an oplog entry *if*:

    - The oplog has reached the maximum configured size, *and* 

    - The oplog entry is older that the configured number of 
      hours based on the host system clock.

    To check the currently configured minimum oplog retention
    period, see the
    `oplogTruncation.oplogMinRetentionHours` in the
    output of the `serverStatus` command.

**See also:**

- `--oplogSize` / `replication.oplogSizeMB`
- `--oplogMinRetentionHours` / `storage.oplogMinRetentionHours`

## Behavior

You can use `replSetResizeOplog` on 
`mongod` instances running with the 
Wired Tiger storage engine or the 
in-memory storage engine. 

See the tutorial-change-oplog-size tutorial for a procedure
on using `replSetResizeOplog` command to resize the oplog.

The oplog can grow past its configured size
limit to avoid deleting the `majority commit point`.

You cannot drop the `local.oplog.rs` collection. For more information on this 
restriction, see oplog-coll-behavior.

`replSetResizeOplog` overrides the maximum oplog size or
minimum oplog retention period set at startup by:

- `replication.oplogSizeMB` / `--oplogSizeMB`, and

- `storage.oplogMinRetentionHours` /
  `--oplogMinRetentionHours`
  respectively.

The new oplog size persists after a server restart, unless
you use:

- `storage.oplogMinRetentionHours`, or

- `--oplogMinRetentionHours`.

**Important:**

Reducing the maximum oplog size results in truncation of the oldest
oplog entries until the oplog reaches the new configured size.

Similarly, reducing the minimum oplog retention period
results in truncation of oplog entries older that the specified
period *if* the oplog has exceeded the maximum configured size.

Oplog truncation due to reduced oplog size or retention period can
result in unexpected behavior from clients still reading those oplog
entries, including:

- Open change streams may become 
  invalidated

- Secondaries which have not replicated those oplog entries
  may require resynchronization.

- Backups using `mongodump` with 
  `--oplog` against the member may
  not capture entries prior to truncation.

### Minimum Oplog Retention Period

A `mongod` has the following behavior when configured with
a minimum oplog retention period:

- The oplog can grow without constraint so as to retain oplog entries
  for the configured number of hours. This may result in reduction or
  exhaustion of system disk space due to a combination of high write
  volume and large retention period.

- If the oplog grows beyond its maximum size, the `mongod` 
  may continue to hold that disk space even if the oplog returns to its
  maximum size *or* is configured for a smaller maximum size. See
  replSetResizeOplog-cmd-compact.

- The `mongod` compares the system wall clock to an 
  oplog entry creation wall clock time when enforcing oplog entry
  retention. Clock drift between cluster components may result in
  unexpected oplog retention behavior. See
  production-notes-clock-synchronization for more information on
  clock synchronization across cluster members.

### `replSetResizeOplog` Does Not Replicate To Other Members

Changing the oplog size or minimum oplog retention period 
of a given replica set member with `replSetResizeOplog` does
not change the oplog size of any other member in the replica set. You
must run `replSetResizeOplog` on each replica set member in
your cluster to change the oplog size or minimum retention period for
all members.

### Reducing Oplog Size Does Not Immediately Return Disk Space

Reducing the oplog size does not immediately reclaim that disk space.
This includes oplog size reduction due to truncation of oplog events
older than of the minimum oplog retention period.

To immediately free unused disk space after reducing the oplog size, run
`compact` against the `oplog.rs` collection in the
`local` database during a maintenance period. `compact` blocks all
operations on the database it runs against. Running `compact` against
`oplog.rs` therefore prevents oplog synchronization. For a procedure
on resizing the oplog and compacting `oplog.rs`, see
/tutorial/change-oplog-size.

### Resource Locking

`replSetResizeOplog` takes an exclusive (W) lock on the 
`oplog` and blocks other operations on the collection 
until it finishes.

For more information on locking in MongoDB, see /faq/concurrency.

## Examples

### Change the Maximum Oplog Size

Use the `db.collection.stats()` `mongosh`
method to display the current maximum oplog size, `maxSize`, in
megabytes. For example:
         

```javascript
db.getSiblingDB("local").oplog.rs.stats(1024*1024).maxSize
```

The above command returns the oplog size of this member in megabytes:

```javascript
990
```

The following command uses `replSetResizeOplog` to change the
oplog size of this member to 16384 megabytes:

```javascript
db.adminCommand({ "replSetResizeOplog": 1, size: Double(16384)})
```

To verify the new oplog size, rerun the `db.collection.stats()` method:

```javascript
db.getSiblingDB("local").oplog.rs.stats(1024*1024).maxSize
```

The above command returns:

```javascript
"maxSize": Long("16834")
```

**Warning:**

Reducing the size of the oplog in a node removes data from it. This
may cause replica members syncing with that node to become stale.
To resync those members, see /tutorial/resync-replica-set-member.

### Change the Minimum Oplog Retention Period

1. Connect `mongosh` to the `mongod`
   replica set member.

#. *Optional*. Use the `db.serverStatus()` command to verify
   the current minimum oplog retention value as
   `oplogTruncation.oplogMinRetentionHours`:

   ```javascript
   db.getSiblingDB("admin").serverStatus().oplogTruncation.oplogMinRetentionHours
   ```

   The command returns the currently configured minimum oplog retention
   period for the `mongod`. For example:

   ```javascript
   1.5
   ```

   If the `mongod` has no minimum oplog retention period,
   the operation returns an empty result.

#. Use the `replSetResizeOplog` command to modify the
   configured minimum oplog retention period. For example, the following
   sets the minimum oplog retention period to `2` hours:

   ```javascript
   db.adminCommand({
     "replSetResizeOplog" : 1, 
     "minRetentionHours" : 2
   })
   ```
