<!-- Converted from reference/mql/query-predicates.txt (reStructuredText). Includes are inlined. -->

# Query Predicates

Query predicates are expressions that indicate whether a document
matches a specified query. For example, ``{ name: {
$eq: "Alice" } }`` is a query predicate that returns documents where the
value of the `"name"` field is the string `"Alice"`.

Use the following types of operators in query predicates:

| Operator Type | Description |
|---|---|
| query-selectors-arrays | Return data based on array conditions. |
| query-selectors-bitwise | Return data based on bit position conditions. |
| query-selectors-comparison | Return data based on value comparisons such as less than and greater than. |
| query-selectors-data-type | Return data based on field existence or data types. |
| query-selectors-misc | Perform specialized functions in query predicates. |
| query-selectors-logical | Return data based on boolean logic (and, or, and nor). |
| query-selectors-geospatial | Return data based on geospatial query predicates, such as containment within a region on the surface of the Earth. |

## Alphabetical List of Operators

| Name | Description |
|---|---|
| `$all` | Matches arrays that contain all elements specified in the query. |
| `$and` | .. include:: /includes/query-predicates/and-desc.rst |
| `$bitsAllClear` | Matches numeric or binary values in which a set of bit positions *all* have a value of `0`. |
| `$bitsAllSet` | Matches numeric or binary values in which a set of bit positions *all* have a value of `1`. |
| `$bitsAnyClear` | Matches numeric or binary values in which *any* bit from a set of bit positions has a value of `0`. |
| `$bitsAnySet` | Matches numeric or binary values in which *any* bit from a set of bit positions has a value of `1`. |
| `$elemMatch` | .. include:: /includes/query-predicates/elemMatch-desc.rst |
| `$eq` | Matches values that are equal to a specified value. |
| `$exists` | Matches documents that have the specified field. |
| `$expr` | .. include:: /includes/query-predicates/expr-desc.rst |
| `$geoIntersects` | Selects geometries that intersect with a GeoJSON geometry. Requires a 2dsphere index. |
| `$geoWithin` | Selects geometries within a bounding GeoJSON geometry. Requires a 2dsphere or 2d index. |
| `$gt` | Matches values that are greater than a specified value. |
| `$gte` | Matches values that are greater than or equal to a specified value. |
| `$jsonSchema` | .. include:: /includes/query-predicates/jsonSchema-desc.rst |
| `$in` | Matches any of the values specified in an array. |
| `$lt` | Matches values that are less than a specified value. |
| `$lte` | Matches values that are less than or equal to a specified value. |
| `$mod` | Matches documents based on the result of a modulo operation on a field value. |
| `$ne` | Matches all values that are not equal to a specified value. |
| `$near` | Returns geospatial objects in proximity to a point. Requires a `2dsphere` or `2d` index. |
| `$nearSphere` | Returns geospatial objects in proximity to a point on a sphere. Requires a `2dsphere` or `2d` index. |
| `$nin` | .. include:: /includes/query-predicates/nin-desc.rst |
| `$nor` | .. include:: /includes/query-predicates/nor-desc.rst |
| `$not` | Inverts the effect of a query predicate and returns documents that do *not* match the query predicate. |
| `$or` | .. include:: /includes/query-predicates/or-desc.rst |
| `$regex` | Matches documents where values match a specified regular expression. |
| `$size` | .. include:: /includes/query-predicates/size-desc.rst |
| `$type` | Matches documents if a field is of the specified type. |
| `$where` | Matches documents that satisfy a JavaScript expression. |
