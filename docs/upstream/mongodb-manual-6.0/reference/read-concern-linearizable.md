<!-- Converted from reference/read-concern-linearizable.txt (reStructuredText). Includes are inlined. -->

# Read Concern `"linearizable"`

**`"linearizable"`**

The query returns data that reflects all successful
majority-acknowledged writes that completed prior to the start of the
read operation. The query may wait for concurrently executing writes to
propagate to a majority of replica set members before returning results.

If a majority of your replica set members crash and restart after the
read operation, documents returned by the read operation are durable if
`writeConcernMajorityJournalDefault` is set to the default
state of `true`.

With `writeConcernMajorityJournalDefault` set to `false`,
MongoDB does not wait for `w: "majority"`
writes to be written to the on-disk journal before acknowledging the
writes. As such, `"majority"` write operations could
possibly roll back in the event of a transient loss (e.g. crash and
restart) of a majority of nodes in a given replica set.

You can specify linearizable read concern for read operations on
the `primary` only.

**Tip:**

Always use `maxTimeMS` with linearizable read concern in case a
majority of data bearing members are unavailable. `maxTimeMS`
ensures that the operation does not block indefinitely and instead
ensures that the operation returns an error if the read concern
cannot be fulfilled.

## Requirements

Linearizable read concern guarantees only apply if read operations
specify a query filter that uniquely identifies a single document.
Additionally if none of the following criteria are met, linearizable
read concern might not read from a consistent snapshot, resulting in a
document matching the filter not being returned:

- The query uses an immutable field as the search key of the query. For
  example, searching on the `_id` field or using `$natural`.

- No concurrent updates mutate the search key of the query.

- The search key has a unique index and the
  query uses that index.

If any of the preceding criteria are met, the query reads from a
consistent snapshot to return the single matching document.

## Causally Consistent Sessions

Read concern `"linearizable"` is unavailable for use with
causally consistent sessions.

## Aggregation Restriction

You cannot use the `$out` or the `$merge` stage
in conjunction with read concern `"linearizable"`. That
is, if you specify `"linearizable"` read concern for
`db.collection.aggregate()`, you cannot include either
stages in the pipeline.

## Real Time Order

Combined with `"majority"` write concern,
`"linearizable"` read concern enables multiple threads to
perform reads and writes on a single document as if a single thread
performed these operations in real time; that is, the corresponding
schedule for these reads and writes is considered linearizable.

## Read Your Own Writes

You can use causally consistent sessions to read your own 
writes, if the writes request acknowledgment.

## Performance Comparisons

Unlike `"majority"`, `"linearizable"` read
concern confirms with secondary members that the read operation is
reading from a primary that is capable of confirming writes with
`{ w: "majority" }` write concern.
[#edge-cases-2-primaries]_ As such, reads with linearizable read
concern may be significantly slower than reads with
`"majority"` or `"local"` read concerns.

Always use `maxTimeMS` with linearizable read concern in case a
majority of data bearing members are unavailable. `maxTimeMS` ensures
that the operation does not block indefinitely and instead ensures that
the operation returns an error if the read concern cannot be fulfilled.

For example:

```javascript
db.restaurants.find( { _id: 5 } ).readConcern("linearizable").maxTimeMS(10000)

db.runCommand( {
     find: "restaurants",
     filter: { _id: 5 },
     readConcern: { level: "linearizable" },
     maxTimeMS: 10000
} )
```
