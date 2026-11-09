<!-- Converted from reference/command/geoSearch.txt (reStructuredText). Includes are inlined. -->

# geoSearch

**`geoSearch`**

**Important:** Removed in MongoDB 5.0

MongoDB 5.0 removes the deprecated geoHaystack index and `geoSearch` command. Use a
2d index with `$geoNear` or one of the
supported geospatial query operators
instead.

Upgrading your MongoDB instance to 5.0 and setting
featureCompatibilityVersion to `5.0` will delete any
pre-existing geoHaystack indexes.

The `geoSearch` command provides an interface to
MongoDB's haystack index functionality. These indexes are
useful for returning results based on location coordinates *after*
collecting results based on some other query (i.e. a "haystack.")

The `geoSearch` command accepts a document that
contains the following fields.

* - Field

  - Type

  - Description

* - `geoSearch`

  - string

  - The collection to query.

* - `search`

  - document

  - Query to filter documents.

* - `near`

  - array

  - Coordinates of a point.

* - `maxDistance`

  - number

  - Optional. Maximum distance from the specified point.

* - `limit`

  - number

  - Optional. Maximum number of documents to return.

* - `readConcern`

  - document

  - Optional. Specifies the read concern.

    The `readConcern` option has the following syntax: 
    `readConcern: { level: <value> }`

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

    For more information on the read concern levels, see
    read-concern-levels.

* - `comment`

  - any

  - .. include:: /includes/extracts/comment-content.rst

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Limit

Unless specified otherwise, the `geoSearch` command
limits results to 50 documents.

### Sharded Clusters

`geoSearch` is not supported for sharded clusters.

### Transactions

`geoSearch` can be used inside distributed transactions.

**Important:**

In most cases, a distributed transaction incurs a greater
performance cost over single document writes, and the
availability of distributed transactions should not be a
replacement for effective schema design. For many scenarios, the
denormalized data model (embedded documents and arrays) will continue to be optimal for your
data and use cases. That is, for many scenarios, modeling your data
appropriately will minimize the need for distributed
transactions. 

For additional transactions usage considerations
(such as runtime limit and oplog size limit), see also
/core/transactions-production-consideration.

## Examples

Consider the following example:

```javascript
db.runCommand({
   geoSearch : "places", 
   near: [ -73.9667, 40.78 ],
   maxDistance : 6,
   search : { type : "restaurant" },
   limit : 30
})
```

The above command returns all documents with a `type` of
`restaurant` having a maximum distance of 6 units from the
coordinates `[ -73.9667, 40.78 ]` in the collection `places` up to a
maximum of 30 results.

### Override Default Read Concern

To override the default read concern level of `"local"`,
use the `readConcern` option.

The following operation on a replica set specifies a
/reference/read-concern of `"majority"` to read the
most recent copy of the data confirmed as having been written to a
majority of the nodes.

**Note:**

Regardless of the read concern level, the most recent data on a
node may not reflect the most recent version of the data in the system.

```javascript
db.runCommand(
   {
      geoSearch: "places",
      near: [ -73.9667, 40.78 ],
      search : { type : "restaurant" },
      readConcern: { level: "majority" }
    }
)
```

To ensure that a single thread can read its own writes, use
`"majority"` read concern and `"majority"`
write concern against the primary of the replica set.
