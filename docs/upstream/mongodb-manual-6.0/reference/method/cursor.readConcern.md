<!-- Converted from reference/method/cursor.readConcern.txt (reStructuredText). Includes are inlined. -->

# cursor.readConcern()

## Definition

**`cursor.readConcern(level)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Specify a read concern for the `db.collection.find()`
method.

The `readConcern()` method has the following form:

```javascript
db.collection.find().readConcern(<level>)
```

The `readConcern()` method has the following
parameter:

* - Parameter

  - Type

  - Description

* - `level`

  - string

  - Read concern level.

    Possible read concern levels are:

    - `"local"`. This is the default read concern level for
      read operations against the primary and secondaries.

    - `"available"`. Available for read operations against
      the primary and secondaries. `"available"` behaves the 
      same as `"local"` against the primary and non-sharded
      secondaries. The query returns the instance's most recent data.

    - `"majority"`. Available for replica sets that use
      WiredTiger storage engine.

    - `"linearizable"`. Available for read operations on the
      `primary` only.

    - `"snapshot"`. Available for multi-document
      transactions, and starting in MongoDB 5.0, certain
      read operations outside of multi-document transactions.

    For more formation on the read concern levels, see
    read-concern-levels.

          
          

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Considerations

### Read Your Own Writes

You can use causally consistent sessions to read your own 
writes, if the writes request acknowledgment.

### Linearizable Read Concern Performance

When specifying `linearizable read concern`, always use `maxTimeMS()` in case
a majority of data bearing members are unavailable.

```javascript
db.restaurants.find( { _id: 5 } ).readConcern("linearizable").maxTimeMS(10000)
```

**See also:**

/reference/read-concern
