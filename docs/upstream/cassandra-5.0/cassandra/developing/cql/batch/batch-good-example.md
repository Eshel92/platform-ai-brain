<!-- Converted from modules/cassandra/pages/developing/cql/batch/batch-good-example.adoc (AsciiDoc). Includes are inlined. -->

# Good use of BATCH statement

Batch operations can be beneficial, as shown in the following examples.
The examples use the table `cyclist_expenses`:

```language-cql
CREATE TABLE IF NOT EXISTS cycling.cyclist_expenses (
```

Note that `balance` is `STATIC`.

**Note:**
If there are two different tables in the same keyspace and the two tables have the same partition key, this scenario is considered a single partition batch.
There will be a single mutation for each table.
This happens because the two tables could have different columns, even though the keyspace and partition are the same.
Batches allow a caller to bundle multiple operations into a single batch request.
All the operations are performed by the same coordinator.
The best use of a batch request is for a single partition in multiple tables in the same keyspace.
Also, batches provide a guarantee that mutations will be applied in a particular order.

## Single partition batch

* The first INSERT in the `BATCH` statement sets the `balance` to zero.
The next two statements insert an `expense_id` and change the `balance` value.
All the `INSERT` and `UPDATE` statements in this batch write to the same partition, keeping the latency of the write operation low.
+
```language-cql
BEGIN BATCH
```
+
This batching example includes conditional updates combined with using static columns.
Recall that single partition batches are not logged.
+

**Note:**
 It would be reasonable to expect that an UPDATE to the balance could be included in this BATCH statement:
+
```language-cql
UPDATE cycling.cyclist_expenses
```
+
However, it is important to understand that all the statements processed in a `BATCH` statement timestamp the records with the same value.
The operations may not perform in the order listed in the `BATCH` statement.
The UPDATE might be processed BEFORE the first INSERT that sets the balance value to zero, allowing the conditional to be met.
+
An acknowledgement of a batch statement is returned if the batch operation is successful.
+
```results
 [applied]
-----------
      True

```
+
The resulting table will only have one record so far.
+
```results
 cyclist_name | expense_id | balance | amount | description | paid
--------------+------------+---------+--------+-------------+-------
  Vera ADRIAN |          1 |       0 |   7.95 |   Breakfast | False

(1 rows)

```

* The balance can be adjusted separately with an UPDATE statement.
Now the `balance` will reflect that breakfast was unpaid.
+
```language-cql
UPDATE cycling.cyclist_expenses
```
+
```results
 cyclist_name | expense_id | balance | amount | description | paid
--------------+------------+---------+--------+-------------+-------
  Vera ADRIAN |          1 |   -7.95 |   7.95 |   Breakfast | False

(1 rows)

```

* The table `cyclist_expenses` stores records about each purchase by a cyclist and includes the running balance of all the cyclist's purchases.
Because the balance is static, all purchase records for a cyclist have the same running balance.
This `BATCH` statement inserts expenses for two more meals changes the balance to reflect that breakfast and dinner were unpaid.
+
```language-cql
BEGIN BATCH
```
+
```results
 cyclist_name | expense_id | balance | amount | description | paid
--------------+------------+---------+--------+-------------+-------
  Vera ADRIAN |          1 |  -32.95 |   7.95 |   Breakfast | False
  Vera ADRIAN |          2 |  -32.95 |  13.44 |       Lunch |  True
  Vera ADRIAN |          3 |  -32.95 |     25 |      Dinner | False

(3 rows)

```

* Finally, the cyclist pays off all outstanding bills and the `balance` of the account goes to zero.
+
```language-cql
BEGIN BATCH
```
+
```results
 cyclist_name | expense_id | balance | amount | description | paid
--------------+------------+---------+--------+-------------+------
  Vera ADRIAN |          1 |       0 |   7.95 |   Breakfast | True
  Vera ADRIAN |          2 |       0 |  13.44 |       Lunch | True
  Vera ADRIAN |          3 |       0 |     25 |      Dinner | True

(3 rows)

```
+
Because the column is static, you can provide only the partition key when updating the data.
To update a non-static column, you would also have to provide a clustering key.
Using batched conditional updates, you can maintain a running balance.
If the balance were stored in a separate table, maintaining a running balance would not be possible because a batch having conditional updates cannot span multiple partitions.

## Multiple partition logged batch

* Another example is using `BATCH` to perform a multiple partition insert that involves writing the same data to two related tables that must be synchronized.
The following example modifies multiple partitions, which in general is to be avoided, but the batch only contains two statements:
+
```language-cql
BEGIN BATCH
```
+
Another common use for this type of batch operation is updating usernames and passwords.
