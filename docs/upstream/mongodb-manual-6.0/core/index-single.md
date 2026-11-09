<!-- Converted from core/index-single.txt (reStructuredText). Includes are inlined. -->

# Single Field Indexes

MongoDB provides complete support for indexes on any field in a
collection of documents. By default, all
collections have an index on the _id field, and
applications and users may add additional indexes to support important
queries and operations.

This document describes ascending/descending indexes on a single field.

(Figure: /images/index-ascending.bakedsvg.svg)

## Compatibility

You can use single field indexes for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).
To learn more about managing indexes for deployments hosted in MongoDB
Atlas, see Create, View, Drop, and Hide Indexes.

## Create an Ascending Index on a Single Field

Consider a collection `schools` that contains the following sample document:

```javascript
db.schools.insertOne(
   {
      "_id": ObjectId("570c04a4ad233577f97dc459"),
      "studentsEnrolled": 1034,
      "location": { state: "NY", city: "New York" }
   }
)
```

The following operation creates an ascending index on the `studentsEnrolled`
field of the `schools` collection:

```javascript
db.schools.createIndex( { studentsEnrolled: 1 } )
```

The created index supports queries that select on the field
`studentsEnrolled`, such as the following:

```javascript
db.schools.find( { studentsEnrolled: 1034 } )
db.schools.find( { studentsEnrolled: { $gt: 500 } } )
```

## Create an Index on an Embedded Field

You can create indexes on fields within embedded documents, just as you
can index top-level fields in documents. Indexes on embedded fields
differ from indexes on embedded documents,
which include the full content up to the maximum index size
of the embedded document in the index. Instead, indexes on
embedded fields allow you to use a "dot notation," to introspect into
embedded documents.

Consider a collection named `records` that holds documents that
resemble the following sample document:

```javascript
{
  "_id": ObjectId("570c04a4ad233577f97dc459"),
  "studentsEnrolled": 1034,
  "location": { state: "NY", city: "New York" }
}
```

The following operation creates an index on the `location.state`
field:

```javascript
db.schools.createIndex( { "location.state": 1 } )
```

The created index will support queries that select on the field
`location.state`, such as the following:

```javascript
db.schools.find( { "location.state": "CA" } )
db.schools.find( { "location.city": "Albany", "location.state": "NY" } )
```

## Create an Index on Embedded Document

You can also create indexes on embedded document as a whole.

When you create an index on an embedded document, only queries that
specify the entire embedded document use the index. Queries on a
specific field within the document do not use the index.

Consider a collection named `schools` that holds documents that
resemble the following sample document:

```javascript
{
  "_id": ObjectId("570c04a4ad233577f97dc459"),
  "studentsEnrolled": 1034,
  "location": { state: "NY", city: "New York" }
}
```

The `location` field is an embedded document, containing the embedded fields
`city` and `state`. The following command creates an index on the `location`
field as a whole:

```javascript
db.schools.createIndex( { location: 1 } )
```

The following query can use the index on the `location` field:

```javascript
db.schools.find( { location: { city: "New York", state: "NY" } } )
```

**Note:** Although the query can use the index, the result set does not

include the sample document above. When performing equality matches on
embedded documents, field order matters and the embedded documents
must match exactly. See query-embedded-documents for more
information regarding querying on embedded documents.

## Additional Considerations

During index builds, applications may encounter reduced performance or
limited read/write access to the collection being indexed.

For more information on the index build process, see
index-operations, especially the
index-operations-replicated-build section.

Some drivers use `NumberLong(1)` instead of `1` to specify the index
order. The resulting indexes are the same.
