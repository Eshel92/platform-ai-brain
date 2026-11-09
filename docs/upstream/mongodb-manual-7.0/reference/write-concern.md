<!-- Converted from reference/write-concern.txt (reStructuredText). Includes are inlined. -->

# Write Concern

Write concern describes the level of acknowledgment requested from
MongoDB for write operations to a standalone `mongod`,
replica sets, or sharded clusters. In sharded clusters, `mongos`
instances pass the write concern to the shards.

**Note:**

For multi-document transactions, you set
the write concern at the transaction level, not at the individual
operation level. Do not explicitly set the write concern for
individual write operations in a transaction.

Replica sets and sharded clusters support a global default write
concern. Operations without an explicit write concern inherit the
global default. The default global write concern is majority. See
`setDefaultRWConcern` for more information.

To learn more about setting the write concern for deployments
hosted in MongoDB Atlas, see 
Build a Resilient Application with MongoDB Atlas

## Write Concern Specification

Write concern can include the following fields:

```javascript
{ w: <value>, j: <boolean>, wtimeout: <number> }
```

- w: Requests acknowledgment that the write operation
  has propagated to a specified number of `mongod`
  instances or to `mongod` instances with specified tags.

- j: Requests acknowledgment that the write operation
  has been written to the on-disk journal.

- wtimeout: Specifies a time limit to prevent
  write operations from blocking indefinitely.

### `w` Option

The `w` option requests acknowledgment that the write operation has
propagated to a specified number of `mongod` instances or
to `mongod` instances with specified tags. If the write
concern is missing the `w` field, MongoDB sets the `w` option to the
default write concern. 

**Note:**

If you use the `setDefaultRWConcern` to set the default
write concern, you must specify a `w` field value. 

The `w` option supports the following `w: <value>` write concerns:

* - Value
  - Description

* - .. writeconcern:: "majority"

  - Requests acknowledgment that write operations have been durably committed 
    to the calculated majority of
    the data-bearing voting members (i.e. primary and secondaries
    with `members[n].votes` greater than `0`).
    `{ w: "majority" }` is the default write concern for *most* MongoDB
    deployments. See wc-default-behavior.

    For example, consider a replica set with 3 voting members,
    Primary-Secondary-Secondary (P-S-S). For this replica set, the
    calculated majority is 2, and
    the write must propagate to the oplogs of the primary and one
    secondary to acknowledge the write concern to the client.

    Hidden,
    delayed,
    and priority 0
    members with `members[n].votes` greater than `0`
    can acknowledge `"majority"` write operations.

    Delayed secondaries can return write acknowledgment no earlier
    than the configured `secondaryDelaySecs`. 

    After the write operation returns with a `w:
    "majority"` acknowledgment to the client, the
    client can read the result of that write with a
    `"majority"` readConcern.

    If you specify a `"majority"` write concern for writes and the 
    operation does not replicate to the  calculated majority
    of replica set members before it returns a response, then the data eventually 
    replicates or rolls back. See wc-wtimeout.

    See wc-ack-behavior for when `mongod` instances
    acknowledge the write.

* - .. writeconcern:: <number>

  - Requests acknowledgment that the write operation has propagated
    to the specified number of `mongod` instances. For
    example:

    `w: 1`
      Requests acknowledgment that the write operation has
      propagated to the standalone `mongod` or the
      primary in a replica set. Data can be
      rolled back if the primary steps down
      before the write operations replicate to any of the
      secondaries.

      WARNING: If write operations use
      `{ w: 1 } <` write concern, the
      rollback directory may exclude writes submitted after an
      oplog hole if the primary restarts before the write
      operation completes.

    `w: 0`
      Requests no acknowledgment of the write operation. However,
      `w: 0` may return information about socket exceptions and
      networking errors to the application. Data can be
      rolled back if the primary steps down
      before the write operations replicate to any of the
      secondaries.

      If you specify `w: 0` but include j: true,
      j: true prevails to request acknowledgment from
      the standalone `mongod` or the primary of a
      replica set.

    `w` greater than 1 requires acknowledgment from the primary
    and as many data-bearing secondaries as needed to meet the
    specified write concern. Secondaries do not need to be voting
    members to meet the write concern threshold.

    For example, consider a 3-member replica set with a primary and
    2 secondaries. Specifying `w: 2` requires acknowledgment from
    the primary and one secondary. Specifying `w: 3` requires
    acknowledgment from the primary and both secondaries.

    Hidden,
    delayed,
    and priority 0
    members can acknowledge 
    `w: <number> <` write operations.

    Delayed secondaries can return write acknowledgment no earlier
    than the configured `secondaryDelaySecs`. 

    See wc-ack-behavior for when `mongod` instances
    acknowledge the write.

* - .. writeconcern:: <custom write concern name>

  - Requests acknowledgment that the write operations have
    propagated to `tagged` members that
    satisfy the custom write concern defined in
    `settings.getLastErrorModes`. For an example, see
    configure-custom-write-concern.

    Data can be rolled back if the custom
    write concern only requires acknowledgment from the primary and
    the primary steps down before the write operations replicate to
    any of the secondaries.

    See wc-ack-behavior for when `mongod`
    instances acknowledge the write.

**See also:**

- default-mongodb-read-write-concerns
- replica-set-protocol-version

### `j` Option

The `j` option requests acknowledgment from MongoDB that
the write operation has been written to the on-disk journal.

|  |  |
|---|---|
| .. writeconcern:: j | If `j: true`, requests acknowledgment that the `mongod` instances, as specified in the w: <value>, have written to the on-disk journal. `j: true` alone does not guarantee that the write will not roll back due to replica set primary failover. With `j: true`, MongoDB returns only after the requested number of members, including the primary, have written to the journal. Previously `j: true` write concern in a replica set only requires the primary to write to the journal, regardless of the w: <value> write concern. |

**Note:**

- Specifying a write concern that includes `j: true` to a
  `mongod` instance running without journaling produces
  an error.

- If journaling is enabled, `w:
  "majority"` may imply `j: true`. The
  `writeConcernMajorityJournalDefault` replica set
  configuration setting determines the behavior. See
  wc-ack-behavior for details.

- A write concern that includes or implies `j: true` causes an
  immediate journal synchronization. See journal-process.

### `wtimeout`

This option specifies a time limit, in milliseconds, for a write
operation to propagate to enough members to achieve the write concern
after the operation succeeds on the primary. `wtimeout` does not
apply if `w` is less than or equal to `1`. If the write operation
does not achieve the write concern within this time limit, MongoDB
returns a write concern error.

`wtimeout` causes write operations to return with a write concern error
after the specified limit, even if the required write concern will
eventually succeed. When these write operations return,
MongoDB **does not** undo successful data modifications performed
before the write concern exceeded the `wtimeout` time limit.

If you do not specify the `wtimeout` option and the level of write
concern is unachievable, the write operation will block indefinitely.
Specifying a `wtimeout` value of `0` is equivalent to a write
concern without the `wtimeout` option.

**Note:**

To set a time limit on the primary write operation, use the
`maxTimeMS()` method. 

## Implicit Default Write Concern

The implicit default write concern is
`w: majority`. `w: majority`
ensures write durability by requiring replica sets to wait for on-disk journaling
by default, controlled by `writeConcernMajorityJournalDefault`.
However, there is an edge case for replica set deployments containing
arbiters:

- The voting majority of a replica set is 1 plus half the number of
  voting members, rounded down. If the number of data-bearing voting
  members is not greater than the voting majority, the default write
  concern is `{ w: 1 }`.

- In all other scenarios, the default write concern is ``{ w:
  "majority" }``.

Specifically, MongoDB uses the following formula to determine the
default write concern:

```none
if [ (#arbiters > 0) AND (#non-arbiters <= majority(#voting-nodes)) ]
    defaultWriteConcern = { w: 1 }
else
    defaultWriteConcern = { w: "majority" }
```

For example, consider the following deployments and their respective
default write concerns:

| Non-Arbiters | Arbiters | Voting Nodes | Majority of Voting Nodes | Implicit Default Write Concern |
|---|---|---|---|---|
| 2 | 1 | 3 | 2 | `{ w: 1 }` |
| 4 | 1 | 5 | 3 | `{ w: "majority" }` |

- In the first example:

  - There are 2 non-arbiters and 1 arbiter for a total of 3 voting
    nodes.

  - The majority of voting nodes (1 plus half of 3, rounded
    down) is 2.

  - The number of non-arbiters (2) is equal to
    the majority of voting nodes (2), resulting in an implicit write
    concern of `{ w: 1 }`.

- In the second example:

  - There are 4 non-arbiters and 1 arbiter for a total of 5
    voting nodes.

  - The majority of voting nodes (1 plus half of 5, rounded
    down) is 3.

  - The number of non-arbiters (4) is greater than the majority
    of voting nodes (3), resulting in an implicit write concern of
    `{ w: "majority" }`.

On a sharded cluster, DDL (Data Definition Language) operations run with write concern `"majority"`. If
you specify a different write concern, the operation overrides the
provided write concern with `"majority"`.

## Acknowledgment Behavior

The w option and the j option determine
when `mongod` instances acknowledge write operations. 

### Standalone

A standalone `mongod` acknowledges a write operation after
applying the write in memory or after writing to the on-disk journal.
The following table lists the acknowledgment behavior for a standalone
with the relevant write concerns:

|  | `j` is unspecified | `j:true` | `j:false` |
|---|---|---|---|
| `w: 1` | In memory | On-disk journal | In memory |
| `w: "majority"` | On-disk journal *if running with journaling* | On-disk journal | In memory |

**Note:**

With `writeConcernMajorityJournalDefault` set to `false`,
MongoDB does not wait for `w: "majority"`
writes to be written to the on-disk journal before acknowledging the
writes. As such, `"majority"` write operations could
possibly roll back in the event of a transient loss (e.g. crash and
restart) of a majority of nodes in a given replica set.

### Replica Sets

The w value determines the number of replica set members
that must acknowledge the write before returning success. For each
eligible member, the j option determines whether the
member acknowledges writes after applying the write in memory or after
writing to the on-disk journal.

`w: "majority"`
  Any data-bearing voting member of the replica set can contribute
  to write acknowledgment of `"majority"` write 
  operations.

  The following table lists when the member can acknowledge
  the write based on the j value:

  * - `j` is unspecified
    - Acknowledgment depends on the value of
      `writeConcernMajorityJournalDefault`:

      - If `true`, acknowledgment requires MongoDB to make writes
        durable by syncing them to on-disk journal, equivalent to
        `j: true`.

        `writeConcernMajorityJournalDefault` defaults to
        `true`

      - If `false`, acknowledgment requires writing operation in
        memory, equivalent to `j: false`.

  * - `j: true`
    - Acknowledgment requires MongoDB to make writes durable by 
      syncing them to on-disk journal.

  * - `j: false`
    - Acknowledgment requires writing operation in memory.

      Typically, if `j: false` is set, writing the operation to the
      on-disk journal isn't required. However, if
      `writeConcernMajorityJournalDefault: true` is set, writing
      the operation to the journal is required even if `j: false`
      is set.

      If `j: false` and ``writeConcernMajorityJournalDefault:
      true`` are set, the write operations are written to the journal
      asynchronously.

      - Writes that have `w: majority` set aren't acknowledged as
        complete until the journal is flushed to disk.

      - `w: majority` writes wait for the `"majority"`
        read snapshot to complete, regardless of the `j` setting.
        This is because if ``writeConcernMajorityJournalDefault:
        true`` is set, the majority read snapshot is based on the
        majority of journaled writes.

      - After the write operation returns with a `w: majority`
        acknowledgment to the client application, the application can
        read the result of the write if the `majority` read
        concern is set.

  For behavior details, see wc-majority-behavior.

`w: <number>`
  Any data-bearing member of the replica set can contribute
  to write acknowledgment of w: <number> write
  operations.
       
  The following table lists when the member can acknowledge
  the write based on the j value:

  |  |  |
  |---|---|
  | `j` is unspecified | Acknowledgment requires writing operation in memory, equivalent to `j: false`. |
  | `j: true` | Acknowledgment requires MongoDB to make writes durable by syncing them to on-disk journal. |
  | `j: false` | Acknowledgment requires writing operation in memory. |

**Note:**

Hidden,
delayed,
and priority 0
members can acknowledge 
`w: <number> <` write operations.

Delayed secondaries can return write acknowledgment no earlier
than the configured `secondaryDelaySecs`. 

## Additional Information

### Read and Write Concern Recommendations

To read your own writes on the primary, use the
`"majority"` read concern and the `{ w: "majority" }`
write concern. During an election, a read routed to the
former primary can return a snapshot that does not include
a majority-acknowledged write accepted by the new primary.

If you use a `{ w: n }` write concern where `n` is greater than
the calculated majority of the
cluster's nodes and the cluster uses the default settings, enable the
write concern "j" option to acknowledge the write to the
journal. The `"majority"` read concern only allows you to read
updates that are durable on a majority of nodes in the replica
set.

**Note:**

If you perform writes with a `{ w: n }` write concern and `n` is
greater than the calculated majority, without journaling and with
the default cluster settings, you may receive a write acknowledgement
before the write is durable on a majority of nodes.

### Causally Consistent Sessions and Write Concerns

Causally consistent client sessions guarantee causal
consistency only if:

- the associated read operations use `"majority"` read
  concern, and 

- the associated write operations use `"majority"`
  write concern.

For details, see causal-consistency.

### `w: "majority"` Behavior

- .. include:: /includes/extracts/no-journaling-rollback.rst

- Hidden,
  delayed,
  and priority 0
  members with `members[n].votes` greater than `0`
  can acknowledge `"majority"` write operations.

  - Delayed secondaries can return write acknowledgment no earlier
    than the configured `secondaryDelaySecs`. 

- Starting in MongoDB 5.0, replica set members in the
  `STARTUP2` state do not participate in write majorities.

### Write Concern not Supported on `local` Database

The local database does not
support write concerns. MongoDB silently ignores any configured write
concern for operations on collections in the local database.

### Calculating Majority for Write Concern

**Tip:**

The `rs.status()` returns the 
`writeMajorityCount` field which contains
the calculated majority number.

The majority for write concern `"majority"` is calculated
as the smaller of the following values:

- the majority of *all* voting members, including arbiters

- the number of all **data-bearing** voting members

**Warning:**

If the calculated majority equals the number of all
**data-bearing** voting members, such as in a 3-member
Primary-Secondary-Arbiter deployment, write concern
`"majority"` may time out or never be acknowledged if
a data-bearing voting member is down or unreachable. If possible,
use a data-bearing voting member instead of an arbiter.

For example, consider:

- A replica set with 3 voting members, Primary-Secondary-Secondary
  (P-S-S):

  - The majority of all voting members is 2.

  - The number of all data-bearing voting members is 3.

  | The calculated majority is 2, the minimum of 2 and 3. The write
    must propagate to the primary and one of the secondaries to
    acknowledge the write concern `"majority"` to the
    client.

- A replica set with 3 voting members, Primary-Secondary-Arbiter
  (P-S-A):

  - The majority of all voting members is 2.

  - The number of all data-bearing voting members is 2.

  | The calculated majority is 2, the minimum of 2 and 2. Since the
    write can only be applied to data-bearing members, the write must
    propagate to the primary and the secondary to acknowledge write
    concern `"majority"` to the client.

  **Tip:**

  Avoid using `"majority"` write concern with P-S-A
  or other topologies that require all data-bearing voting members
  to be available to acknowledge writes. For the durability
  guarantees of a `"majority"` write concern, deploy a
  topology that does not require all data-bearing voting members to
  be available, such as P-S-S.

**Warning:**

Avoid deploying more than one arbiter in a replica
set. See rollbacks-multi-arbiters.

To add an arbiter to an existing replica set:

- Typically, if there are two or fewer data-bearing members in the
  replica set, you might need to first set the cluster wide write
  concern for the replica set.

- See cluster wide write concern for more information on why you
  might need to set the cluster wide write concern.

You do not need to change the cluster wide write concern before starting
a new replica set with an arbiter.

**See also:**

Default write concern formula

### Write Concern Provenance

MongoDB tracks write concern `provenance`, which indicates the source of a 
particular write concern. You may see `provenance` shown in the
`getLastError` metrics, write
concern error objects, and MongoDB logs.

The following table shows the possible write concern `provenance`
values and their significance:

| Provenance | Description |
|---|---|
| `clientSupplied` | The write concern was specified in the application. |
| `customDefault` | The write concern originated from a custom defined default value. See `setDefaultRWConcern`. |
| `getLastErrorDefaults` | The write concern originated from the replica set's `settings.getLastErrorDefaults` field. |
| `implicitDefault` | The write concern originated from the server in absence of all other write concern specifications. |

### Write Concern Contrasted with Commit Quorum

There are important differences between commit quorums and write concerns:

- Index builds use **commit quorums**.
- Write operations use **write concerns**. 

Each data-bearing node in a cluster is a voting member.

The **commit quorum** specifies how many data-bearing voting members, or
which voting members, including the primary, must be prepared to commit
a simultaneous index build
before the primary will execute the commit.

The **write concern** is the level of acknowledgment that the write has
propagated to the specified number of instances.

The **commit quorum** specifies how many nodes must be *ready* to finish
the index build before the primary commits the index build. In contrast,
when the primary has committed the index build, the **write concern**
specifies how many nodes must *finish* the index build before the
command returns.
