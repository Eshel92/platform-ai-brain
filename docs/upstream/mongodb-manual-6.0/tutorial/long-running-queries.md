<!-- Converted from tutorial/long-running-queries.txt (reStructuredText). Includes are inlined. -->

# Perform Long-Running Snapshot Queries

Snapshot queries allow you to read data as it appeared at a single point
in time in the recent past.

Starting in MongoDB 5.0, you can use read concern
`"snapshot"` to query data on secondary nodes. This
feature increases the versatility and resilience of your application's
reads. You do not need to create a static copy of your data, move it out
into a separate system, and manually isolate these long-running queries
from interfering with your operational workload. Instead, you can
perform long-running queries against a live, transactional database
while reading from a consistent state of the data.

Using read concern `"snapshot"` on secondary nodes does not
impact your application's write workload. Only application reads benefit
from long-running queries being isolated to secondaries.

Use snapshot queries when you want to:

- Perform multiple related queries and ensure that each query reads data
  from the same point in time.

- Ensure that you read from a consistent state of the data from some
  point in the past.

## Comparing Local and Snapshot Read Concerns

When MongoDB performs long-running queries using the default
`"local"` read concern, the query results may contain data
from writes that occur at the same time as the query. As a result, the
query may return unexpected or inconsistent results.

To avoid this scenario, create a session and specify
read concern `"snapshot"`. With read concern
`"snapshot"`, MongoDB runs your query with snapshot
isolation, meaning that your query reads data as it appeared at a single
point in time in the recent past.

## Examples

The examples on this page show how you can use snapshot queries to:

- example-snapshot-queries-multiple

- example-snapshot-pit

### Run Related Queries From the Same Point in Time

Read concern `"snapshot"` lets you run multiple related
queries within a session and ensure that each query reads data from the
same point in time.

An animal shelter has a `pets` database that contains collections for
each type of pet. The `pets` database has these collections:

- `cats`
- `dogs`

Each document in each collection contains an `adoptable` field,
indicating whether the pet is available for adoption. For example, a
document in the `cats` collection looks like this:

```javascript
{
   "name": "Whiskers",
   "color": "white",
   "age": 10,
   "adoptable": true
}
```

You want to run a query to see the total number of pets available for
adoption across all collections. To provide a consistent view of the
data, you want to ensure that the data returned from each collection is
from a single point in time.

To accomplish this goal, use read concern `"snapshot"`
within a session:

**python:**

(Code example not available offline: /driver-examples/test_examples.py)

**c:**

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**go:**

(Code example not available offline: /driver-examples/go_examples.go)

**motor:**

(Code example not available offline: /driver-examples/test_examples_motor.py)

**php:**

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

**ruby:**

(Code example not available offline: /driver-examples/snapshot_query_examples_spec.rb)

**cpp:**

(Code example not available offline: /driver-examples/cpp-documentation-examples.cpp)

The preceding series of commands: 

- Uses `MongoClient()` to establish a connection to the MongoDB
  deployment.

- Switches to the `pets` database.

- Establishes a session. The command specifies `snapshot=True`,
  so the session uses read concern `"snapshot"`.

- Performs these actions for each collection in the `pets` database:

  - Uses `$match` to filter for documents where the
    `adoptable` field is `True`.

  - Uses `$count` to return a count of the filtered documents.

  - Increments the `adoptablePetsCount` variable with the count from
    the database.

- Prints the `adoptablePetsCount` variable.

All queries within the session read data as it appeared at the same
point in time. As a result, the final count reflects a consistent
snapshot of the data.

**Note:**

If the session lasts longer than the WiredTiger history retention
period (300 seconds, by default), the query errors with a
`SnapshotTooOld` error. To learn how to configure snapshot
retention and enable longer-running queries, see
configure-snapshot-retention.

### Read from a Consistent State of the Data from Some Point in the Past

Read concern `"snapshot"` ensures that your query reads
data as it appeared at some single point in time in the recent past.

An online shoe store has a `sales` collection that contains data for
each item sold at the store. For example, a document in the `sales`
collection looks like this:

```javascript
{
   "shoeType": "boot",
   "price": 30,
   "saleDate": ISODate("2022-02-02T06:01:17.171Z")  
}
```

Each day at midnight, a query runs to see how many pairs of shoes were
sold that day. The daily sales query looks like this:

**python:**

(Code example not available offline: /driver-examples/test_examples.py)

**c:**

(Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

**go:**

(Code example not available offline: /driver-examples/go_examples.go)

**motor:**

(Code example not available offline: /driver-examples/test_examples_motor.py)

**php:**

(Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

The preceding query:

- Uses `$match` with `$expr` to specify a filter on the
  `saleDate` field.
  
  - `$expr` allows the use of aggregation expressions (such as `NOW`) in the
    `$match` stage.

- Uses the `$gt` operator and `$dateSubtract`
  expression to return documents where the `saleDate` is
  greater than one day before the time the query is executed.

- Uses `$count` to return a count of the matching documents.
  The count is stored in the `totalDailySales` variable.

- Specifies read concern `"snapshot"` to ensure that the
  query reads from a single point in time.

The `sales` collection is quite large, and as a result this query may
take a few minutes to run. Because the store is online, sales can occur
at any time of day.

For example, consider if:

- The query begins executing at 12:00 AM.
- A customer buys three pairs of shoes at 12:02 AM.
- The query finishes executing at 12:04 AM.

If the query doesn't use read concern `"snapshot"`, sales
that occur between when the query starts and when it finishes can be
included in the query count, despite not occurring on the day the report
is for. This could result in inaccurate reports with some sales being
counted twice.

By specifying read concern `"snapshot"`, the query only
returns data that was present in the database at a point in time shortly
before the query started executing.

**Note:**

If the query takes longer than the WiredTiger history retention
period (300 seconds, by default), the query errors with a
`SnapshotTooOld` error. To learn how to configure snapshot
retention and enable longer-running queries, see
configure-snapshot-retention.

## Configure Snapshot Retention

By default, the WiredTiger storage engine retains history for 300
seconds. You can use a session with `snapshot=true` for a total of 300
seconds from the time of the first operation in the session to the last.
If you use the session for a longer period of time, the session fails
with a `SnapshotTooOld` error. Similarly, if you query data using read
concern `"snapshot"` and your query lasts longer than 300
seconds, the query fails.

If your query or session run for longer than 300 seconds, consider
increasing the snapshot retention period. To increase the retention
period, modify the `minSnapshotHistoryWindowInSeconds`
parameter.

For example, this command sets the value of
`minSnapshotHistoryWindowInSeconds` to 600 seconds:

```javascript
db.adminCommand( { setParameter: 1, minSnapshotHistoryWindowInSeconds: 600 } )
```

   

**Important:**

To modify `minSnapshotHistoryWindowInSeconds` for a
MongoDB Atlas cluster, you must contact Atlas
Support.

### Disk Space and History

Increasing the value of `minSnapshotHistoryWindowInSeconds`
increases disk usage because the server must maintain the history of
older modified values within the specified time window. The amount of
disk space used depends on your workload, with higher volume workloads
requiring more disk space.
