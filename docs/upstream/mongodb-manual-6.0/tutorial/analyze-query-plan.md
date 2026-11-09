<!-- Converted from tutorial/analyze-query-plan.txt (reStructuredText). Includes are inlined. -->

# Analyze Query Performance

The explain plan results for queries are
subject to change between MongoDB versions.

tabs:
  - id: shell
    content: |
      The
      `cursor.explain("executionStats")`
      and the `db.collection.explain("executionStats")` methods provide statistics about
      the performance of a query. These statistics can be useful in
      measuring if and how a query uses an index. See
      `db.collection.explain()` for details.

  - id: compass
    content: |
      MongoDB Compass provides an `Explain Plan` tab, which 
      displays statistics about  the performance of a query. These statistics 
      can be useful in measuring if and how a query uses an index.

## Evaluate the Performance of a Query

Consider a collection `inventory` with the following documents:

```javascript
db.inventory.insertMany ( [ 
   { _id: 1, item: "f1", type: "food", quantity: 500 },
   { _id: 2, item: "f2", type: "food", quantity: 100 },
   { _id: 3, item: "p1", type: "paper", quantity: 200 },
   { _id: 4, item: "p2", type: "paper", quantity: 150 },
   { _id: 5, item: "f3", type: "food", quantity: 300 },
   { _id: 6, item: "t1", type: "toys", quantity: 500 },
   { _id: 7, item: "a1", type: "apparel", quantity: 250 },
   { _id: 8, item: "a2", type: "apparel", quantity: 400 },
   { _id: 9, item: "t2", type: "toys", quantity: 50 },
   { _id: 10, item: "f4", type: "food", quantity: 75 }
] )
```

**shell:**

**compass:**

The documents appear in MongoDB Compass as the following:

(Figure: /images/compass-analyze-inventory-docs.png)

### Query with No Index

tabs:
  - id: shell
    content: |
      The following query retrieves documents where the
      `quantity` field has a value between `100` and `200`,
      inclusive:

      ```javascript
      db.inventory.find( { quantity: { $gte: 100, $lte: 200 } } )
      ```

      The query returns the following documents:

      ```javascript
      { "_id" : 2, "item" : "f2", "type" : "food", "quantity" : 100 }
      { "_id" : 3, "item" : "p1", "type" : "paper", "quantity" : 200 }
      { "_id" : 4, "item" : "p2", "type" : "paper", "quantity" : 150 }
      ```

      To view the query plan selected, chain the
      `cursor.explain("executionStats")`
      cursor method to the end of the `find` command:

      ```javascript
      db.inventory.find(
         { quantity: { $gte: 100, $lte: 200 } }
      ).explain("executionStats")
      ```

      `explain()` returns the following results:

      ```javascript
      {
         queryPlanner: {
               ...
               winningPlan: {
                  queryPlan: {
                     stage: 'COLLSCAN',
                     ...
                  }
               }
         },
         executionStats: {
            executionSuccess: true,
            nReturned: 3,
            executionTimeMillis: 0,
            totalKeysExamined: 0,
            totalDocsExamined: 10,
            executionStages: {
               stage: 'COLLSCAN',
               ...
            },
            ...
         },
         ...
      }
      ```

      - `queryPlanner.winningPlan.queryPlan.stage` displays
        `COLLSCAN` to indicate a collection scan.

        Collection scans indicate that the
        `mongod` had to scan the entire collection
        document by document to identify the results. This is a
        generally expensive operation and can result in slow
        queries.

      - `executionStats.nReturned` displays `3` to
        indicate that the winning query plan returns three documents.

      - `executionStats.totalKeysExamined` displays `0`
        to indicate that this is query is not using an index.

      - `executionStats.totalDocsExamined` displays `10`
        to indicate that MongoDB had to scan ten documents (i.e.
        all documents in the collection) to find the three matching
        documents.

  - id: compass
    content: |
      The following query retrieves documents where the
      `quantity` field has a value between `100` and `200`,
      inclusive:

      Copy the following filter into the Compass query bar and click
      Find:

      ```javascript
      { quantity: { $gte: 100, $lte: 200 } }
      ```

      The query returns the following documents:

      To view the query plan selected:

      1. Click the Explain Plan tab for the
         `test.inventory` collection.

      #. Click Explain.

      MongoDB Compass displays the query plan as follows:

      (Figure: /images/compass-explain-plan-no-index.png)

      **Note:**

      Because we are working with such a small dataset for the
      purposes of this tutorial, the
      Actual Query Execution Time displays
      `0` seconds, even though we are not using an index.

      In a larger dataset, the difference in query
      execution time between an indexed query versus a
      non-indexed query would be much more substantial.

      Visual Tree
      ```````````

      - The :guilabel:`Query Performance Summary` shows the
        execution stats of the query:

        - :guilabel:`Documents Returned` displays ``3`` to indicate
          that the winning query plan returns three documents.

        - :guilabel:`Index Keys Examined` displays ``0`` to
          indicate that this query is not using an index.

        - :guilabel:`Documents Examined` displays ``10`` to indicate
          that MongoDB had to scan ten documents (i.e. all documents
          in the collection) to find the three matching documents.

      - Below the :guilabel:`Query Performance Summary`, MongoDB Compass
        displays the ``COLLSCAN`` query stage to indicate that a
        collection scan was used for this query.

        Collection scans indicate that the
        :binary:`~bin.mongod` had to scan the entire collection
        document by document to identify the results. This is a
        generally expensive operation and can result in slow
        queries.

      Raw JSON
      ````````

      The explain details can also be viewed in raw JSON format by
      clicking :guilabel:`Raw JSON` below the query bar:

      (Figure: /images/compass-explain-plan-no-index-raw-json.png)

The difference between the number of matching documents and the number
of examined documents may suggest that, to improve efficiency, the
query might benefit from the use of an index.

### Query with Index

To support the query on the ``quantity`` field, add an index on the
``quantity`` field:

tabs:
  - id: shell
    content: |

      ```javascript
      db.inventory.createIndex( { quantity: 1 } )
      ```

      To view the query plan statistics, use the
      `explain("executionStats")` method:

      ```javascript
      db.inventory.find(
         { quantity: { $gte: 100, $lte: 200 } }
      ).explain("executionStats")
      ```

      The `explain()` method returns the following
      results:

      ```javascript
      {
         queryPlanner: {
               ...
               winningPlan: {
                  queryPlan: {
                     stage: 'FETCH',
                     inputStage: {
                        stage: 'IXSCAN',
                        keyPattern: {
                           quantity: 1
                        },
                        ...
                     }
                  }
               },
               rejectedPlans: [ ]
         },
         executionStats: {
               executionSuccess: true,
               nReturned: 3,
               executionTimeMillis: 0,
               totalKeysExamined: 3,
               totalDocsExamined: 3,
               executionStages: {
                  ...
               },
               ...
         },
         ...
      }
      ```

      - `queryPlanner.winningPlan.queryPlan.inputStage.stage` displays
        `IXSCAN` to indicate index use.

      - `executionStats.nReturned`
        displays `3` to indicate that the winning query plan returns 
        three documents.

      - `executionStats.totalKeysExamined` displays `3`
        to indicate that MongoDB scanned three index entries. The
        number of keys examined match the number of documents
        returned, meaning that the `mongod` only had
        to examine index keys to return the results. The
        `mongod` did not have to scan all of the
        documents, and only the three matching documents had to be
        pulled into memory. This results in a very efficient query.

      - `executionStats.totalDocsExamined` display `3`
        to indicate that MongoDB scanned three documents.

  - id: compass
    content: |
      1. Click the Indexes tab for the
         `test.inventory` collection.

      2. Click Create Index.

      3. Select `quantity` from the
         Select a field name dropdown.

      4. Select `1 (asc)` from the type dropdown.

      5. Click Create.

      **Note:**

      Leaving the index name field blank causes MongoDB Compass to
      create a default name for the index.

      You can now see your newly created index in the
      Indexes tab:

      (Figure: /images/compass-show-new-index.png)

      Return to the Explain Plan tab for the
      `inventory` collection and re-run the query from
      the previous step:

      ```javascript
      { quantity: { $gte: 100, $lte: 200 } }
      ```

      MongoDB Compass displays the query plan as follows:

      (Figure: /images/compass-explain-plan-with-index.png)

      Visual Tree
      ```````````

      - The :guilabel:`Query Performance Summary` shows the
        execution stats of the query:

        - :guilabel:`Documents Returned` displays ``3`` to indicate
          that the winning query plan returns three documents.

        - :guilabel:`Index Keys Examined` displays ``3``
          to indicate that MongoDB scanned three index entries. The
          number of keys examined match the number of documents
          returned, meaning that the :binary:`~bin.mongod` only had
          to examine index keys to return the results. The
          :binary:`~bin.mongod` did not have to scan all of the
          documents, and only the three matching documents had to be
          pulled into memory. This results in a very efficient
          query.

        - :guilabel:`Documents Examined` displays ``3`` to indicate
          that MongoDB scanned three documents.

        - On the right-hand side of the
          :guilabel:`Query Performance Summary`, MongoDB Compass shows
          that the query used the ``quantity`` index.

      - Below the :guilabel:`Query Performance Summary`, MongoDB Compass
        displays the query stages ``FETCH`` and ``IXSCAN``.
        ``IXSCAN`` indicates that the
        :binary:`~bin.mongod` used an index to satisfy the query
        before exeuting the ``FETCH`` stage and retrieving the
        documents.

      Raw JSON
      ````````

      The explain details can also be viewed in raw JSON format by
      clicking :guilabel:`Raw JSON` below the query bar:

      (Figure: /images/compass-explain-plan-with-index-raw-json.png)

Without the index, the query would scan the whole collection of ``10``
documents to return ``3`` matching documents. The query also had to
scan the entirety of each document, potentially pulling them into
memory. This results in an expensive and potentially slow query
operation.

When run with an index, the query scanned ``3`` index entries
and ``3`` documents to return ``3`` matching documents, resulting
in a very efficient query.

**shell:**

**Compare Performance of Indexes**

To manually compare the performance of a query using more
than one index, you can use the :method:`~cursor.hint()`
method in conjunction with the :method:`~cursor.explain()`
method.

Consider the following query:

```javascript
db.inventory.find( {
   quantity: {
      $gte: 100, $lte: 300
   },
   type: "food"
} )
```

The query returns the following documents:

```javascript
{ "_id" : 2, "item" : "f2", "type" : "food", "quantity" : 100 }
{ "_id" : 5, "item" : "f3", "type" : "food", "quantity" : 300 }
```

To support the query, add a compound index. With compound indexes, the order
of the fields matter.

For example, add the following two compound indexes. The
first index orders by `quantity` field first, and then the
`type` field. The second index orders by `type` first,
and then the `quantity` field.

```javascript
db.inventory.createIndex( { quantity: 1, type: 1 } )
db.inventory.createIndex( { type: 1, quantity: 1 } )
```

Evaluate the effect of the first index on the query:

```javascript
db.inventory.find(
   { quantity: { $gte: 100, $lte: 300 }, type: "food" }
).hint({ quantity: 1, type: 1 }).explain("executionStats")
```

The `explain()` method returns the following
output:

```javascript
{
   queryPlanner: {
      ...
      winningPlan: {
         queryPlan: {
            stage: 'FETCH',
            inputStage: {
               stage: 'IXSCAN',
               keyPattern: {
                  quantity: 1,
                  type: 1
               },
               ...
               }
            }
         }
      },
      rejectedPlans: [ ]
   },
   executionStats: {
      executionSuccess: true,
      nReturned: 2,
      executionTimeMillis: 0,
      totalKeysExamined: 5,
      totalDocsExamined: 2,
      executionStages: {
      ...
      }
   },
   ...
}
```

MongoDB scanned `5` index keys
(`executionStats.totalKeysExamined`) to return `2`
matching documents (`executionStats.nReturned`).

Evaluate the effect of the second index on the query:

```javascript
db.inventory.find(
   { quantity: { $gte: 100, $lte: 300 }, type: "food" }
).hint({ type: 1, quantity: 1 }).explain("executionStats")
```

The `explain()` method returns the following
output:

```javascript
{
   queryPlanner: {
      ...
      queryPlan: {
         winningPlan: {
            stage: 'FETCH',
            inputStage: {
               stage: 'IXSCAN',
               keyPattern: {
                  type: 1,
                  quantity: 1
               },
               ...
            }
         }
      },
      rejectedPlans: [ ]
   },
   executionStats: {
      executionSuccess: true,
      nReturned: 2,
      executionTimeMillis: 0,
      totalKeysExamined: 2,
      totalDocsExamined: 2,
      executionStages: {
         ...
      }
   },
   ...
}
```

MongoDB scanned `2` index keys
(`executionStats.totalKeysExamined`) to return `2`
matching documents (`executionStats.nReturned`).

The second compound index, `{ type: 1, quantity: 1 }`, is
therefore the more efficient index for supporting the example
query, as the MongoDB server only needs to scan `2`
`index keys`
to find all matching documents using this index, compared to
`5` when when using the compound index
`{ quantity: 1, type: 1 }`.

**See also:**

- /core/query-optimization
- /core/query-plans
- /tutorial/optimize-query-performance-with-indexes-and-projections
- /applications/indexes

**compass:**

**See also:**

- Query Optimization
- MongoDB Compass Documentation
- `Compass Query Plan Documentation`
