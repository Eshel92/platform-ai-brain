<!-- Converted from core/transactions-in-applications.txt (reStructuredText). Includes are inlined. -->

# Drivers API

## Callback API vs Core API

The txn-callback-api:

- Starts a transaction, executes the specified operations, and commits
  (or aborts on error).

- Automatically incorporates error handling logic for
  transient-transaction-error and
  unknown-transaction-commit-result.

The txn-core-api:

- Requires explicit call to start the transaction and commit the
  transaction.

- Does not incorporate error handling logic for
  transient-transaction-error and
  unknown-transaction-commit-result, and instead provides the
  flexibility to incorporate custom error handling for these errors.

## Callback API

The callback API incorporates logic:

- To retry the transaction as a whole if the transaction encounters a
  transient-transaction-error error.

- To retry the commit operation if the commit encounters an
  unknown-transaction-commit-result error.

Starting in MongoDB 6.0.5, the server does not retry the transaction if
it receives a transactionTooLargeForCache-error error.

### Example

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

tabs:

   - id: python
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         (Code example not available offline: /driver-examples/test_examples.py)

   - id: java-sync
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         ```java
         /*
         For a replica set, include the replica set name and a seedlist of the members in the URI string; e.g.
         String uri = "mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017/admin?replicaSet=myRepl";
         For a sharded cluster, connect to the mongos instances; e.g.
         String uri = "mongodb://mongos0.example.com:27017,mongos1.example.com:27017:27017/admin";
         */

         final MongoClient client = MongoClients.create(uri);

         /*
            Create collections.
         */

         client.getDatabase("mydb1").getCollection("foo")
               .withWriteConcern(WriteConcern.MAJORITY).insertOne( new Document("abc", 0));
         client.getDatabase("mydb2").getCollection("bar")
               .withWriteConcern(WriteConcern.MAJORITY).insertOne( new Document("xyz", 0));

         /* Step 1: Start a client session. */

         final ClientSession clientSession = client.startSession();

         /* Step 2: Optional. Define options to use for the transaction. */

         TransactionOptions txnOptions = TransactionOptions.builder()
               .readPreference(ReadPreference.primary())
               .readConcern(ReadConcern.LOCAL)
               .writeConcern(WriteConcern.MAJORITY)
               .build();

         /* Step 3: Define the sequence of operations to perform inside the transactions. */

         TransactionBody txnBody = new TransactionBody<String>() {
            public String execute() {
               MongoCollection<Document> coll1 = client.getDatabase("mydb1").getCollection("foo");
               MongoCollection<Document> coll2 = client.getDatabase("mydb2").getCollection("bar");

               /*
                  Important:: You must pass the session to the operations..
                  */

               coll1.insertOne(clientSession, new Document("abc", 1));
               coll2.insertOne(clientSession, new Document("xyz", 999));

               return "Inserted into collections in different databases";
            }
         };
         try {
            /* 
               Step 4: Use .withTransaction() to start a transaction, 
               execute the callback, and commit (or abort on error).
            */

            clientSession.withTransaction(txnBody, txnOptions);
         } catch (RuntimeException e) {
            // some error handling
         } finally {
            clientSession.close();
         }
         ```

   - id: nodejs
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         (Code example not available offline: /driver-examples/node_transactions.js)

   - id: php
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

   - id: csharp
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         (Code example not available offline: /driver-examples/withTxnExample1.cs)

   - id: c
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

   - id: cpp
     content: |

         **Important:**

         - Use the MongoDB driver for your MongoDB version.

         - When using drivers, each operation in the transaction must pass
           the session to each operation.

         - Operations in a transaction use transaction-level read
           concern, transaction-level
           write concern, and
           transaction-level read preference.

         - You can create collections in transactions implicitly or 
           explicitly. See transactions-create-collections-indexes.

         The example uses the new callback API for working with
         transactions, which starts a transaction, executes the
         specified operations, and commits (or aborts on error). The
         new callback API incorporates retry logic for
         transient-transaction-error or
         unknown-transaction-commit-result commit errors.

         (Code example not available offline: /driver-examples/cpp-with-transaction.cpp)

   - id: motor
     content: |

      **Important:**

      - Use the MongoDB driver for your MongoDB version.

      - When using drivers, each operation in the transaction must pass
        the session to each operation.

      - Operations in a transaction use transaction-level read
        concern, transaction-level
        write concern, and
        transaction-level read preference.

      - You can create collections in transactions implicitly or 
        explicitly. See transactions-create-collections-indexes.

      The example uses the new callback API for working with
      transactions, which starts a transaction, executes the
      specified operations, and commits (or aborts on error). The
      new callback API incorporates retry logic for
      transient-transaction-error or
      unknown-transaction-commit-result commit errors.

      (Code example not available offline: /driver-examples/test_examples_motor.py)

   - id: ruby
     content: |

      **Important:**

      - Use the MongoDB driver for your MongoDB version.

      - When using drivers, each operation in the transaction must pass
        the session to each operation.

      - Operations in a transaction use transaction-level read
        concern, transaction-level
        write concern, and
        transaction-level read preference.

      - You can create collections in transactions implicitly or 
        explicitly. See transactions-create-collections-indexes.

      The example uses the new callback API for working with
      transactions, which starts a transaction, executes the
      specified operations, and commits (or aborts on error). The
      new callback API incorporates retry logic for
      transient-transaction-error or
      unknown-transaction-commit-result commit errors.

      (Code example not available offline: /driver-examples/with_transactions_examples_spec.rb)

   - id: go
     content: |

      The example uses the new callback API for working with
      transactions, which starts a transaction, executes the
      specified operations, and commits (or aborts on error). The
      new callback API incorporates retry logic for
      transient-transaction-error or
      unknown-transaction-commit-result commit errors.

      **Important:**

      - Use the MongoDB driver for your MongoDB version.

      - When using drivers, each operation in the transaction must pass
        the session to each operation.

      - Operations in a transaction use transaction-level read
        concern, transaction-level
        write concern, and
        transaction-level read preference.

      - You can create collections in transactions implicitly or 
        explicitly. See transactions-create-collections-indexes.

      (Code example not available offline: /driver-examples/go_examples.go)

   - id: perl
     content: |

         **Note:**

         For the Perl driver, see the txn-core-api usage example instead.

   - id: scala
     content: |

         **Note:**

         For the Scala driver, see the txn-core-api usage example instead.

## Core API

The core transaction API does not incorporate retry logic for errors
labeled:

- transient-transaction-error. If an operation in a transaction
  returns an error labeled transient-transaction-error, the
  transaction as a whole can be retried.
   
  To handle transient-transaction-error, applications should
  explicitly incorporate retry logic for the error.

- unknown-transaction-commit-result. If the commit returns an
  error labeled unknown-transaction-commit-result, the commit
  can be retried. 

  To handle unknown-transaction-commit-result,
  applications should explicitly incorporate retry logic for the error.

### Example

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

The following example incorporates logic to retry the transaction for
transient errors and retry the commit for unknown commit error:

tabs:

  - id: python
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      (Code example not available offline: /driver-examples/test_examples.py)

  - id: java-sync
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      ```java
      void runTransactionWithRetry(Runnable transactional) {
          while (true) {
              try {
                  transactional.run();
                  break;
              } catch (MongoException e) {
                  System.out.println("Transaction aborted. Caught exception during transaction.");

                  if (e.hasErrorLabel(MongoException.TRANSIENT_TRANSACTION_ERROR_LABEL)) {
                      System.out.println("TransientTransactionError, aborting transaction and retrying ...");
                      continue;
                  } else {
                      throw e;
                  }
              }
          }
      }

      void commitWithRetry(ClientSession clientSession) {
          while (true) {
              try {
                  clientSession.commitTransaction();
                  System.out.println("Transaction committed");
                  break;
              } catch (MongoException e) {
                  // can retry commit
                  if (e.hasErrorLabel(MongoException.UNKNOWN_TRANSACTION_COMMIT_RESULT_LABEL)) {
                      System.out.println("UnknownTransactionCommitResult, retrying commit operation ...");
                      continue;
                  } else {
                      System.out.println("Exception during commit ...");
                      throw e;
                  }
              }
          }
      }

      void updateEmployeeInfo() {

          MongoCollection<Document> employeesCollection = client.getDatabase("hr").getCollection("employees");
          MongoCollection<Document> eventsCollection = client.getDatabase("reporting").getCollection("events");

          TransactionOptions txnOptions = TransactionOptions.builder()
                  .readPreference(ReadPreference.primary())
                  .readConcern(ReadConcern.MAJORITY)
                  .writeConcern(WriteConcern.MAJORITY)
                  .build();

          try (ClientSession clientSession = client.startSession()) {
              clientSession.startTransaction(txnOptions);

              employeesCollection.updateOne(clientSession,
                      Filters.eq("employee", 3),
                      Updates.set("status", "Inactive"));
              eventsCollection.insertOne(clientSession,
                      new Document("employee", 3).append("status", new Document("new", "Inactive").append("old", "Active")));

              commitWithRetry(clientSession);
          }
      }

      void updateEmployeeInfoWithRetry() {
          runTransactionWithRetry(this::updateEmployeeInfo);
      }
      ```

  - id: nodejs
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      (Code example not available offline: /driver-examples/node_transactions.js)

  - id: perl
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      (Code example not available offline: /driver-examples/perl-transactions-examples.t)

  - id: scala
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      (Code example not available offline: /driver-examples/DocumentationTransactionsExampleSpec.scala)

  - id: ruby
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      (Code example not available offline: /driver-examples/transactions_examples_spec.rb)

  - id: php
    content: |

      **Important:**

      To associate read and write operations with a transaction, you **must**
      pass the session to each operation in the transaction.

      (Code example not available offline: /driver-examples/DocumentationExamplesTest.php)

  - id: csharp
    content: |

      (Code example not available offline: /driver-examples/TransactionsRetryExample3.cs)

  - id: c
    content: |

      (Code example not available offline: /driver-examples/test-mongoc-sample-commands.c)

  - id: cpp
    content: |

      (Code example not available offline: /driver-examples/cpp-transactions.cpp)

  - id: go
    content: |

      (Code example not available offline: /driver-examples/go_examples.go)

  - id: motor
    content: |

       **Note:**

       For Motor, see the txn-callback-api instead.

## Driver Versions

- [C 1.15.0](http://mongoc.org/libmongoc/)

- [C# 2.9.0](https://mongodb.github.io/mongo-csharp-driver/)

- [Go 1.1](https://godoc.org/go.mongodb.org/mongo-driver/mongo)

- [Java 3.11.0](https://mongodb.github.io/mongo-java-driver/)

- [Node 3.3.0](https://mongodb.github.io/node-mongodb-native/)

- [Perl 2.2.0](https://metacpan.org/author/MONGODB)

- [Python](https://pymongo.readthedocs.io/en/stable/index.html)

- `Ruby 2.10.0`

- [Scala 2.7.0](https://mongodb.github.io/mongo-scala-driver/)

## Transaction Error Handling

Regardless of the database system, whether MongoDB or relational
databases, applications should take measures to handle errors during
transaction commits and incorporate retry logic for transactions.

### `TransientTransactionError`

The *individual* write operations inside the transaction are not
retryable, regardless of the value of `retryWrites`. If an
operation encounters an error [associated with the label](https://github.com/mongodb/specifications/blob/master/source/transactions/transactions.rst#error-labels) 
`"TransientTransactionError"`, such as when the primary steps down,
the transaction as a whole can be retried.

- The callback API incorporates retry logic for
  `"TransientTransactionError"`.

- The core transaction API does not incorporate retry logic
  for `"TransientTransactionError"`. To handle
  `"TransientTransactionError"`, applications should explicitly
  incorporate retry logic for the error. To view an example that incorporates 
  retry logic for transient errors, see Core API Example.

### `UnknownTransactionCommitResult`

Commit operations are retryable write operations. If 
the commit operation encounters an error, MongoDB drivers retry the commit 
regardless of the value of `retryWrites`.

If the commit operation encounters an error labeled
`"UnknownTransactionCommitResult"`, the commit can be retried.

- The callback API incorporates retry logic for
  `"UnknownTransactionCommitResult"`.

- The core transaction API does not incorporate retry logic for
  `"UnknownTransactionCommitResult"`. To handle
  `"UnknownTransactionCommitResult"`, applications should explicitly
  incorporate retry logic for the error. To view an example that incorporates 
  retry logic for unknown commit errors, see Core API Example.

### `TransactionTooLargeForCache`

**New in version:** 6.0.5

Starting in MongoDB 6.0.5, the server does not retry the transaction if
it receives a `TransactionTooLargeForCache` error. This error means
the cache is too small and a retry is likely to fail.

The default value for the
`transactionTooLargeForCacheThreshold` threshold is `0.75`.
The server returns `TransactionTooLargeForCache` instead of retrying
the transaction when the transaction uses more than 75% of the cache.

In earlier versions of MongoDB, the server returns
`TemporarilyUnavailable` or `WriteConflict` instead of
`TransactionTooLargeForCache`.

Use the `setParameter` command to modify the error threshold. 

## Additional Information

### `mongosh` Example

The following `mongosh` methods are available for
transactions:

- `Session.startTransaction()`

- `Session.commitTransaction()`

- `Session.abortTransaction()`

**Note:**

The `mongosh` example omits retry logic
and robust error handling for simplicity's sake. For a
more practical example of incorporating transactions in
applications, see transactions-retry instead.

```javascript
// Create collections:
db.getSiblingDB("mydb1").foo.insertOne(
    {abc: 0},
    { writeConcern: { w: "majority", wtimeout: 2000 } }
)
db.getSiblingDB("mydb2").bar.insertOne(
   {xyz: 0},
   { writeConcern: { w: "majority", wtimeout: 2000 } }
)

// Start a session.
session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );

coll1 = session.getDatabase("mydb1").foo;
coll2 = session.getDatabase("mydb2").bar;

// Start a transaction
session.startTransaction( { readConcern: { level: "local" }, writeConcern: { w: "majority" } } );

// Operations inside the transaction
try {
   coll1.insertOne( { abc: 1 } );
   coll2.insertOne( { xyz: 999 } );
} catch (error) {
   // Abort transaction on error
   session.abortTransaction();
   throw error;
}

// Commit the transaction using write concern set at transaction start
session.commitTransaction();

session.endSession();
```
