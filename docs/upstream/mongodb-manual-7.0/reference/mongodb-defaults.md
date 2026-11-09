<!-- Converted from reference/mongodb-defaults.txt (reStructuredText). Includes are inlined. -->

# Default MongoDB Read Concerns/Write Concerns

## Read Concern

(Figure: /images/read-write-concern-inheritance.bakedsvg.svg)

### Default Read Concern

The default read concern is as
follows:

* - Operations
  - Default Read Concern

* - Reads against primary

  - `"local"`

    - This read concern can return data that may be rolled
      back.

    - This read concern does not guarantee causal
      consistency.

* - | Reads against secondaries.

  - `"local"`

    - This read concern can return data that may be rolled
      back.

    - This read concern does not guarantee causal
      consistency.

### Specify Read Concern: MongoDB Drivers

**override-concern:**

The following information applies to operations that are run
outside transactions. For read concern
information related to operations that are run inside
transactions, click the `Operations in Transactions` tab.

Using the `MongoDB drivers`, you can override the default 
read concern and set read concern for operations 
at the following levels:

| Level | Description |
|---|---|
| Client level | Applies to operations unless a finer-grained read concern for an operation is set at the database/collection/operation level. |
| Database level | Applies to operations on the database's collections (i.e. overrides the client read concern) unless a read concern has been set at the collection level or the operation level. Does not apply to operations inside transactions. |
| Collection level | Applies for read operations on the collection (i.e. overrides the database/client read concern) unless a read concern has been set at the operation level. Does not apply to operations inside transactions. |
| Operation level | Applies for the specific read operation (i.e. overrides the database/client/collection read concern). The ability to set read concern at the operation depends on the driver. Refer to your `driver's documentation`. Does not apply to operations inside transactions. |

**override-concern-txn:**

The following information applies to operations that are run
inside transactions. For read concern
information related to operations that are run outside
transactions, click the `Operations outside Transactions` tab.

Using the `MongoDB drivers`,you can override the default read concern and set read concern **for transactions**
at the following levels:

| Level | Description |
|---|---|
| Client level | Applies to transactions unless a finer-grained read concern is set at the session/transaction level. All operations within a transaction use the transaction read concern: Any read concern set at the operation, collection, or database level is ignored inside the transaction. |
| Session level | Applies to transactions started in the session (i.e. overrides the client read concern) unless a finer-grained read concern level is set at a specific transaction level. All operations within a transaction use the transaction read concern: Any read concern set at the operation, collection, or database level is ignored inside the transaction. See transactions-read-concern for more information. |
| Transaction level | Applies to the specific transaction (i.e. overrides the client/session read concern). All operations within a transaction use the transaction read concern: Any read concern set at the operation, collection, or database level is ignored inside the transaction. See transactions-read-concern for more information. |

### Additional Information

For more information on the available read concerns, see
/reference/read-concern.

## Write Concern

(Figure: /images/read-write-concern-inheritance.bakedsvg.svg)

### Default Write Concern

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

### Specify Write Concern: MongoDB Drivers

**override-concern:**

The following information applies to operations that are run
outside transactions. For read concern
information related to operations that are run inside
transactions, click the `Operations in Transactions` tab.

Using the `MongoDB drivers`, you can override the default 
write concern and set write concern for 
operations at the following levels:

| Level | Description |
|---|---|
| Client level | Applies to operations unless a finer-grained write concern for an operation is set at the operation/database/collection. |
| Database level | Applies to write operations on the database's collections (i.e. overrides the client write concern) unless a write concern has been set at the collection level or the operation level. Does not apply to operations inside transactions. |
| Collection level | Applies to write operations on the collection (i.e. overrides the database and client write concern) unless a write concern has been set at the operation level. Does not apply to operations inside transactions. |
| Operation level | Applies to the specific write operation. The ability to set write concern at the operation depends on the driver. Refer to your `driver's documentation`. Does not apply to operations inside transactions. |

**override-concern-txn:**

The following information applies to operations that are run
inside transactions. For read concern
information related to operations that are run outside
transactions, click the `Operations outside Transactions` tab.

Using the `MongoDB drivers`, you can override the default write concern and set write concern for **for
transactions** at the following levels:

| Level | Description |
|---|---|
| Client level | Applies to transactions unless a finer-grained write concern for transactions are set at the session/transaction level. Transaction write concern applies to the commit operation and the operations inside the transaction. All operations within a transaction use the transaction write concern: Any write concern set at the operation, collection, or database level is ignored inside the transaction. |
| Session level | Applies for transactions started in the session unless the write concern level is set at a specific transaction level. Transaction write concern applies to the commit operation and the operations inside the transaction. All operations within a transaction use the transaction write concern: Any write concern set at the operation, collection, or database level is ignored inside the transaction. |
| Transaction level | Applies to the specific transaction. Transaction write concern applies to the commit operation and the operations inside the transaction. All operations within a transaction use the transaction write concern: Any write concern set at the operation, collection, or database level is ignored inside the transaction. |

See transactions-write-concern for more information. 

### Additional Information

For more information on the available write concerns, see
/reference/write-concern.

## Causal Consistency Guarantees

With causally consistent client sessions, the
client sessions only guarantee causal consistency if:

- the associated read operations use `"majority"` read
  concern, and 

- the associated write operations use `"majority"`
  write concern.
