<!-- Converted from core/index-wildcard.txt (reStructuredText). Includes are inlined. -->

# Wildcard Indexes

MongoDB supports creating indexes on a field or set of fields to 
support queries. Since MongoDB supports dynamic schemas, applications
can query against fields whose names cannot be known in advance or are
arbitrary. 

**New in version:** MongoDB 4.2

MongoDB 4.2 introduces wildcard indexes for supporting queries
against unknown or arbitrary fields.

Consider an application that captures user-defined data under the
`userMetadata` field and supports querying against that data:

```javascript
{ "userMetadata" : { "likes" : [ "dogs", "cats" ] } }
{ "userMetadata" : { "dislikes" : "pickles" } }
{ "userMetadata" : { "age" : 45 } }
{ "userMetadata" : "inactive" }
```

Administrators want to create indexes to support queries on any
subfield of `userMetadata`.

A wildcard index on `userMetadata`
can support single-field queries on `userMetadata`,
`userMetadata.likes`, `userMetadata.dislikes`, and
`userMetadata.age`:

```bash
db.userData.createIndex( { "userMetadata.$**" : 1 } )
```

The index can support the following queries:

```bash
db.userData.find({ "userMetadata.likes" : "dogs" })
db.userData.find({ "userMetadata.dislikes" : "pickles" })
db.userData.find({ "userMetadata.age" : { $gt : 30 } })
db.userData.find({ "userMetadata" : "inactive" })
```

A non-wildcard index on `userMetadata` can only support queries on
values of `userMetadata`.

**Important:**

Wildcard indexes are not designed to replace workload-based index
planning. For more information on creating indexes to support
queries, see create-indexes-to-support-queries. For 
complete documentation on wildcard index limitations, see 
wildcard-index-restrictions.

## Create Wildcard Index

**Important:**

The `mongod` 
featureCompatibilityVersion must be `4.2` to
create wildcard indexes. For instructions on setting the fCV, see 
set-fcv.

You can create wildcard indexes using the 
`createIndexes` database command or its shell helpers,
`createIndex()` or 
`createIndexes()`.

### Create a Wildcard Index on a Field

To index the value of a specific field:

```javascript
db.collection.createIndex( { "fieldA.$**" : 1 } )
```

With this wildcard index, MongoDB indexes all values of
`fieldA`. If the field is a nested document or array, the wildcard
index recurses into the document/array and stores the value for all 
fields in the document/array.

For example, documents in the `product_catalog` collection may contain
a  `product_attributes` field. The `product_attributes` field can
contain arbitrary nested fields, including embedded documents and
arrays:

```json
{
  "product_name" : "Spy Coat",
  "product_attributes" : {
    "material" : [ "Tweed", "Wool", "Leather" ]
    "size" : {
      "length" : 72,
      "units" : "inches"
    }
  } 
}

{
  "product_name" : "Spy Pen",
  "product_attributes" : {
     "colors" : [ "Blue", "Black" ],
     "secret_feature" : {
       "name" : "laser",
       "power" : "1000",
       "units" : "watts", 
     }
  }
}
```

The following operation creates a wildcard index on the
`product_attributes` field:

```javascript
db.products_catalog.createIndex( { "product_attributes.$**" : 1 } )
```

The wildcard index can support arbitrary single-field queries on
`product_attributes` or its embedded fields:

```bash
db.products_catalog.find( { "product_attributes.size.length" : { $gt : 60 } } )
db.products_catalog.find( { "product_attributes.material" : "Leather" } )
db.products_catalog.find( { "product_attributes.secret_feature.name" : "laser" } )
```

**Note:**

The path-specific wildcard index syntax is incompatible with the
`wildcardProjection` option. See the createIndex-method-wildcard-option for more
information.

For an example, see createIndex-method-wildcard-onepath.

### Create a Wildcard Index on All Fields

To index the value of all fields in a document
(excluding `_id`), specify `"$**"` as the index key:

```javascript
db.collection.createIndex( { "$**" : 1 } )
```

With this wildcard index, MongoDB indexes all fields for each document
in the collection. If a given field is a nested document or array, the
wildcard index recurses into the document/array and stores the value for
all fields in the document/array.

For an example, see createIndex-method-wildcard-allpaths.

**Note:**

Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it
in the `wildcardProjection` document. See createIndex-method-wildcard-option for
more information.

### Create a Wildcard Index on Multiple Specific Fields

To index the values of multiple specific fields in a document:

```javascript
db.collection.createIndex(
  { "$**" : 1 },
  { "wildcardProjection" : 
    { "fieldA" : 1, "fieldB.fieldC" : 1 }
  }
)
```

With this wildcard index, MongoDB indexes all values for the specified
fields for each document in the collection. If a given field is a nested
document or array, the wildcard index recurses into the document/array
and stores the value for all fields in the document/array. 

**Note:**

Wildcard indexes do not support mixing inclusion and exclusion
statements in the `wildcardProjection` document *except* when
explicitly including the `_id` field. For more information on
`wildcardProjection`, see the createIndex-method-wildcard-option.

For an example, see createIndex-method-wildcard-inclusion.

### Create a Wildcard Index that Excludes Multiple Specific Fields

To index the fields of all fields in a document
*excluding* specific field paths:

```javascript
db.collection.createIndex(
  { "$**" : 1 },
  { "wildcardProjection" : 
    { "fieldA" : 0, "fieldB.fieldC" : 0 }
  }
)
```

With this wildcard index, MongoDB indexes all fields for each 
document in the collection *excluding* the specified field paths. If a
given field is a nested document or array, the wildcard index recurses
into the document/array and stores the values for all fields in the
document/array.

For an example, see createIndex-method-wildcard-exclusion.

**Note:**

Wildcard indexes do not support mixing inclusion and exclusion
statements in the `wildcardProjection` document *except* when
explicitly including the `_id` field. For more information on
`wildcardProjection`, see the createIndex-method-wildcard-option.

## Considerations

- Wildcard indexes can support at most *one* field in any given query 
  predicate. For more information on wildcard index query
  support, see wildcard-index-query-sort-support.

- .. include:: /includes/extracts/wildcard-index-fcv.rst

- Wildcard indexes omit the _id field by default. To include the `_id`
  field in the wildcard index, you must explicitly include it in the
  wildcardProjection document (i.e. `{ "_id" : 1 }`).

- You can create multiple wildcard indexes in a collection.

- A wildcard index may cover the same fields as other indexes in the 
  collection.

- Wildcard indexes are /core/index-sparse and only contain 
  entries for documents that have the indexed field, even if the index 
  field contains a null value.

## Behavior

Wildcard indexes have specific behavior when indexing fields which
are an object (i.e. an embedded document) or an array:

- If the field is an object, the wildcard index descends into
  the object and indexes its contents. The wildcard index continues
  descending into any additional embedded documents it encounters.

- If the field is an array, then the wildcard index traverses the array
  and indexes each element:

  - If an element in the array is an object, the wildcard index
    descends into the object to index its contents as described above.
    
  - If the element is an array - that is, an array which is embedded
    directly within the parent array - then the wildcard index does
    *not* traverse the embedded array, but indexes the *entire* array
    as a single value.

- For all other fields, record the primitive (non-object/array) value
  into the index.

The wildcard index continues traversing any additional nested objects or
arrays until it reaches a primitive value (i.e. a field that is not an
object or array). It then indexes this primitive value, along with the
full path to that field.

For example, consider the following document:

```json
{
  "parentField" : {
    "nestedField" : "nestedValue",
    "nestedObject" : {
      "deeplyNestedField" : "deeplyNestedValue" 
    },
    "nestedArray" : [
      "nestedArrayElementOne",
      [ "nestedArrayElementTwo" ]
    ]
  }
}
```

A wildcard index which includes `parentField` records the following
entries:

- `"parentField.nestedField" : "nestedValue"`
- `"parentField.nestedObject.deeplyNestedField" : "deeplyNestedValue"`
- `"parentField.nestedArray" : "nestedArrayElementOne"`
- `"parentField.nestedArray" : ["nestedArrayElementTwo"]`

Note that the records for `parentField.nestedArray` do not include the
array position for each element. Wildcard indexes ignore array element
positions when recording the element into the index. Wildcard indexes
can still support queries that include explicit array indices. See
wildcard-query-support-explicit-array-indices for more
information.

For more information on wildcard index behavior with nested objects,
see wildcard-index-nested-objects. 

For more information on wildcard index behavior with nested arrays,
see wildcard-index-nested-arrays.

### Nested Objects

When a wildcard index encounters a nested object, it descends into
the object and indexes its contents. For example:

```json
{
  "parentField" : {
    "nestedField" : "nestedValue",
    "nestedArray" : ["nestedElement"]
    "nestedObject" : {
      "deeplyNestedField" : "deeplyNestedValue"
    }
  }
}
```

A wildcard index which includes `parentField` descends into the
object to traverse and index its contents:

- For each field which is itself an object (i.e. an embedded document),
  descend into the object to index its contents. 

- For each field which is an array, traverse the array and index 
  its contents.

- For all other fields, record the primitive (non-object/array) value
  into the index.

The wildcard index continues traversing any additional nested objects or
arrays until it reaches a primitive value (i.e. a field that is not an
object or array). It then indexes this primitive value, along with the
full path to that field.

Given the sample document, the wildcard index adds the following records
to the index:

- `"parentField.nestedField" : "nestedValue"` 
- `"parentField.nestedObject.deeplyNestedField" : "deeplyNestedValue"`
- `"parentField.nestedArray" : "nestedElement"`

For more information on wildcard index behavior with nested arrays,
see wildcard-index-nested-arrays.

### Nested Arrays

When a wildcard index encounters a nested array, it attempts to traverse
the array to index its elements. If the array is itself an element in a
parent array (i.e. an embedded array), the wildcard index instead
records the entire array as a value instead of traversing its contents.
For example:

```json
{
  "parentArray" : [
    "arrayElementOne",
    [ "embeddedArrayElement" ],
    "nestedObject" : {
      "nestedArray" : [
        "nestedArrayElementOne",
        "nestedArrayElementTwo"
      ]
    }
  ]
}
```

A wildcard index which includes `parentArray` descends into the
array to traverse and index its contents:

- For each element which is an array (i.e. an embedded array), 
  index the *entire* array as a value.

- For each element which is an object, descend into the object to 
  traverse and index its contents. 

- For all other fields, record the primitive (non-object/array) value
  into the index.

The wildcard index continues traversing any additional nested objects or
arrays until it reaches a primitive value (i.e. a field that is not an
object or array). It then indexes this primitive value, along with the
full path to that field.

Given the sample document, the wildcard index adds the following records
to the index:

- `"parentArray" : "arrayElementOne"` 
- `"parentArray" : ["embeddedArrayElement"]`
- `"parentArray.nestedObject.nestedArray" : "nestedArrayElementOne"`
- `"parentArray.nestedObject.nestedArray" : "nestedArrayElementTwo"`

Note that the records for `parentField.nestedArray` do not include the
array position for each element. Wildcard indexes ignore array element
positions when recording the element into the index. Wildcard indexes
can still support queries that include explicit array indices. See
wildcard-query-support-explicit-array-indices for more
information.

**See also:**

`Nested Depth for BSON Documents`

### Index Display

Starting in MongoDB 6.3, 6.0.5, and 5.0.16, the `wildcardProjection`
field stores the index projection in its submitted form. Earlier
versions of the server may have stored the projection in a normalized
form.

The server uses the index the same way, but you may notice a difference
in the output of the `listIndexes` and
`db.collection.getIndexes()` commands.

## Restrictions

- You cannot shard a collection using a wildcard index. Create a
  non-wildcard index on the field or fields you want to shard on.
  For more information on shard key selection, see
  sharding-shard-key.

- You cannot create a compound index.

- You cannot specify the following properties for a wildcard index:

  - TTL
  - Unique

- You cannot create the following index types using wildcard syntax:

  - 2d (Geospatial)
  - 2dsphere (Geospatial)
  - Hashed

**Important:**

Wildcard Indexes are distinct from and incompatible with
text-index-wildcard. Wildcard indexes cannot support
queries using the `$text` operator. 

For complete documentation on wildcard index creation restrictions, see 
wildcard-index-restrictions-create.

## Wildcard Index Query/Sort Support

### Covered Queries

Wildcard indexes can support a covered query 
**only if** all of the following are true:

- The query planner selects the wildcard index for satisfying the
  query predicate.

- The query predicate specifies *exactly* one field covered by the wildcard
  index.

- The projection explicitly excludes `_id` and includes *only* the query
  field.

- The specified query field is never an array.

Consider the following wildcard index on the `employees` collection:

```javascript
db.employees.createIndex( { "$**" : 1 } )
```

The following operation queries for a single field 
`lastName` and projects out all other fields from the
resulting document:

```javascript
db.employees.find(
  { "lastName" : "Doe" },
  { "_id" : 0, "lastName" : 1 }
)
```

Assuming that the specified `lastName` is never an array, MongoDB
can use the `$**` wildcard index for supporting a covered query.

### Multi-Field Query Predicates

Wildcard indexes can support at most *one* query predicate field. That 
is:

- MongoDB cannot use a non-wildcard index to satisfy one part of a 
  query predicate and a wildcard index to satisfy another.

- MongoDB cannot use one wildcard index to satisfy one part of a query 
  predicate and another wildcard index to satisfy another.

- Even if a single wildcard index could support multiple query fields, 
  MongoDB can use the wildcard index to support only one of the query 
  fields. All remaining fields are resolved without an index.

However, MongoDB may use the same wildcard index for satisfying each 
independent argument of the query `$or` or aggregation 
`$or` operators.

### Queries with Sort

MongoDB can use a wildcard index for satisfying the 
`sort()` **only if** all of the following are true:

- The query planner selects the wildcard index for satisfying the
  query predicate.

- The `sort()` specifies **only** the query predicate
  field.

- The specified field is never an array.

If the above conditions are not met, MongoDB cannot use the wildcard 
index for the sort. MongoDB does not support `sort`
operations that require a different index from that of the query
predicate. For more information, see index-intersection-sort.

Consider the following wildcard index on the `products` collection:

```javascript
db.products.createIndex( { "product_attributes.$**" : 1 } )
```

The following operation queries for a single field 
`product_attributes.price` and sorts on that same field:

```javascript
db.products.find(
  { "product_attributes.price" : { $gt : 10.00 } },
).sort(
  { "product_attributes.price" : 1 }
)
```

Assuming that the specified `price` is never an array, MongoDB
can use the `product_attributes.$**` wildcard index for satisfying 
both the `find()` and `sort()`.

### Unsupported Query Patterns

Wildcard indexes **cannot** support the following query patterns:

- Queries that check if a field does not exist

- Queries that check if a field is or is not equal to a document or an
  array

- Queries that check if a field is equal to null

For details, see wildcard-index-restrictions-query-aggregation.

### Queries with Explicit Array Indices

MongoDB wildcard indexes do not record the array position of any given
element in an array during indexing. However, MongoDB may still select
the wildcard index to answer a query which includes a field path with
one or more explicit array indices (for example,
`parentArray.0.nestedArray.0`). Due to the increasing complexity of
defining index bounds for each consecutive nested array, MongoDB does
not consider the wildcard index to answer a given field path in the
query if that path contains more than `8` explicit array indices.
MongoDB can still consider the wildcard index to answer other field
paths in the query.

For example:

```json
{
  "parentObject" : {
    "nestedArray" : [ 
       "elementOne",
       {
         "deeplyNestedArray" : [ "elementTwo" ]
       }
     ]
  }
}
```

MongoDB can select a wildcard index which includes `parentObject` to
satisfy the following queries:

- `"parentObject.nestedArray.0" : "elementOne"`
- `"parentObject.nestedArray.1.deeplyNestedArray.0" : "elementTwo"`

If a given field path in the query predicate specifies more than 8
explicit array indices, MongoDB does not consider the wildcard index for
answering that field path. MongoDB instead either selects another
eligible index to answer the query, *or* performs a collection scan.

Note that wildcard indexes themselves do not have any limits on the
depth to which they traverse a document while indexing it; the
limitation only applies to queries which explicitly specify exact array
indices. By issuing the same queries without the explicit array indices,
MongoDB may select the wildcard index to answer the query:

- `"parentObject.nestedArray" : "elementOne"`
- `"parentObject.nestedArray.deeplyNestedArray" : "elementTwo"`

**See also:**

`Nested Depth for BSON Documents`
