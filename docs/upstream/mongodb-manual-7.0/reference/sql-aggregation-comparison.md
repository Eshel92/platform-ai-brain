<!-- Converted from reference/sql-aggregation-comparison.txt (reStructuredText). Includes are inlined. -->

# SQL to Aggregation Mapping Chart

The aggregation pipeline maps to many
common SQL aggregation operations.

The following table compares common SQL aggregation terms, functions,
and concepts with their corresponding MongoDB
aggregation operators:

| SQL Terms, Functions, and Concepts | MongoDB Aggregation Operators |
|---|---|
| WHERE | `$match` |
| GROUP BY | `$group` |
| HAVING | `$match` |
| SELECT | `$project` |
| ORDER BY | `$sort` |
| LIMIT | `$limit` |
| SUM() | `$sum` |
| COUNT() | \| `$sum` \| `$sortByCount` |
| join | `$lookup` |
| SELECT INTO NEW_TABLE | `$out` |
| MERGE INTO TABLE | `$merge` |
| UNION ALL | `$unionWith` |

For a list of all aggregation pipeline and expression operators, see:

- aggregation-pipeline-operator-reference

- aggregation-pipeline-operators

**See also:**

/reference/sql-comparison

## Examples

The following table presents a quick reference of SQL aggregation
statements and the corresponding MongoDB statements. The examples in
the table assume the following conditions:

- The SQL examples assume *two* tables, `orders` and
  `order_lineitem` that join by the `order_lineitem.order_id` and
  the `orders.id` columns.

- The MongoDB examples assume *one* collection `orders` that contain
  documents of the following prototype:

  ```javascript
  {
    cust_id: "abc123",
    ord_date: ISODate("2012-11-02T17:04:11.102Z"),
    status: 'A',
    price: 50,
    items: [ { sku: "xxx", qty: 25, price: 1 },
             { sku: "yyy", qty: 25, price: 1 } ]
  }
  ```

| SQL Example | MongoDB Example | Description |
|---|---|---|
| .. code-block:: sql :copyable: false SELECT COUNT(*) AS count FROM orders | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: null, count: { $sum: 1 } } } ] ) | Count all records from `orders` |
| .. code-block:: sql :copyable: false SELECT SUM(price) AS total FROM orders | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: null, total: { $sum: "$price" } } } ] ) | Sum the `price` field from `orders` |
| .. code-block:: sql :copyable: false SELECT cust_id, SUM(price) AS total FROM orders GROUP BY cust_id | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: "$cust_id", total: { $sum: "$price" } } } ] ) | For each unique `cust_id`, sum the `price` field. |
| .. code-block:: sql :copyable: false SELECT cust_id, SUM(price) AS total FROM orders GROUP BY cust_id ORDER BY total | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: "$cust_id", total: { $sum: "$price" } } }, { $sort: { total: 1 } } ] ) | For each unique `cust_id`, sum the `price` field, results sorted by sum. |
| .. code-block:: sql :copyable: false SELECT cust_id, ord_date, SUM(price) AS total FROM orders GROUP BY cust_id, ord_date | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: { cust_id: "$cust_id", ord_date: { $dateToString: { format: "%Y-%m-%d", date: "$ord_date" }} }, total: { $sum: "$price" } } } ] ) | For each unique `cust_id`, `ord_date` grouping, sum the `price` field. Excludes the time portion of the date. |
| .. code-block:: sql :copyable: false SELECT cust_id, count(*) FROM orders GROUP BY cust_id HAVING count(*) > 1 | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: "$cust_id", count: { $sum: 1 } } }, { $match: { count: { $gt: 1 } } } ] ) | For `cust_id` with multiple records, return the `cust_id` and the corresponding record count. |
| .. code-block:: sql :copyable: false SELECT cust_id, ord_date, SUM(price) AS total FROM orders GROUP BY cust_id, ord_date HAVING total > 250 | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: { cust_id: "$cust_id", ord_date: { $dateToString: { format: "%Y-%m-%d", date: "$ord_date" }} }, total: { $sum: "$price" } } }, { $match: { total: { $gt: 250 } } } ] ) | For each unique `cust_id`, `ord_date` grouping, sum the `price` field and return only where the sum is greater than 250. Excludes the time portion of the date. |
| .. code-block:: sql :copyable: false SELECT cust_id, SUM(price) as total FROM orders WHERE status = 'A' GROUP BY cust_id | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $match: { status: 'A' } }, { $group: { _id: "$cust_id", total: { $sum: "$price" } } } ] ) | For each unique `cust_id` with status `A`, sum the `price` field. |
| .. code-block:: sql :copyable: false SELECT cust_id, SUM(price) as total FROM orders WHERE status = 'A' GROUP BY cust_id HAVING total > 250 | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $match: { status: 'A' } }, { $group: { _id: "$cust_id", total: { $sum: "$price" } } }, { $match: { total: { $gt: 250 } } } ] ) | For each unique `cust_id` with status `A`, sum the `price` field and return only where the sum is greater than 250. |
| .. code-block:: sql :copyable: false SELECT cust_id, SUM(li.qty) as qty FROM orders o, order_lineitem li WHERE li.order_id = o.id GROUP BY cust_id | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $unwind: "$items" }, { $group: { _id: "$cust_id", qty: { $sum: "$items.qty" } } } ] ) | For each unique `cust_id`, sum the corresponding line item `qty` fields associated with the orders. |
| .. code-block:: sql :copyable: false SELECT COUNT(*) FROM (SELECT cust_id, ord_date FROM orders GROUP BY cust_id, ord_date) as DerivedTable | .. code-block:: javascript :copyable: false db.orders.aggregate( [ { $group: { _id: { cust_id: "$cust_id", ord_date: { $dateToString: { format: "%Y-%m-%d", date: "$ord_date" }} } } }, { $group: { _id: null, count: { $sum: 1 } } } ] ) | Count the number of distinct `cust_id`, `ord_date` groupings. Excludes the time portion of the date. |

**See also:**

- /reference/sql-comparison

- `db.collection.aggregate()`

- aggregation-pipeline-operator-reference
