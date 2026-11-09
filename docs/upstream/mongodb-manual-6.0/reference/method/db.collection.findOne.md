<!-- Converted from reference/method/db.collection.findOne.txt (reStructuredText). Includes are inlined. -->

# db.collection.findOne()

(Include not available offline: includes/wayfinding/mongosh-method-findOne.rst)

## Definition

**`db.collection.findOne(query, projection, options)`**

Returns one document that satisfies the specified query criteria on
the collection or view. 

The returned document may vary depending on the number of documents 
that match the query criteria, and the 
query plan used:

| Number of matching documents | Query plan | Result |
|---|---|---|
| 0 | Any | The method returns `null` |
| 1 | Any | The method returns the document that satisfies the specified query criteria. |
| 2 or more | Collection Scan | The method returns the first document according to the natural order. In capped collections, natural order is the same as insertion order. |
| 2 or more | Index Scan | The method returns the first document retrieved from the index. |

**Important:**

If the query plan changes to use a different index, the method 
may return a different document. If your use case requires that 
a particular record is chosen consistently, you must use the 
`options` document to specify a sort. For details on using 
`findOne()` with an `options` document, see the 
example.

If you specify a `projection` parameter, 
`findOne()` returns a document that only 
contains the `projection` fields. The `_id` field is always 
included unless you explicitly exclude it.

**Note:**

Although similar to the `find()` method,
the `findOne()` method returns a document
rather than a cursor.

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

## Syntax

The `findOne()` method has the following
form:

```javascript
db.collection.findOne( <query>, <projection>, <options> )
```

The `findOne()` method takes the following
parameters:

| Parameter | Type | Description |
|---|---|---|
| `query` | document | Optional. Specifies query selection criteria using query operators. |
| `projection` | document | Optional. Specifies the fields to return using projection operators. Omit this parameter to return all fields in the matching document. For details, see findOne-projection. |
| `options` | document | .. include:: /includes/find-options-description.rst |

## Behavior

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `db.collection.findOne()`
disconnects before the operation completes, MongoDB marks `db.collection.findOne()` 
for termination using `killOp`.

### Projection

**Important:** Language Consistency

As part of making `find` and
`findAndModify` projection consistent with
aggregation's `$project` stage:

- The `find` and
  `findAndModify` projection can accept
  aggregation expressions and syntax.

- MongoDB enforces additional restrictions with regards to
  projections. See `Projection Restrictions` for details.

The `projection` parameter determines which fields are returned in
the matching documents. The `projection` parameter takes a document
of the following form:

```javascript
{ field1: <value>, field2: <value> ... }
```

* - Projection
  - Description

* - `<field>: <1 or true>`

  - Specifies the inclusion of a field. If you specify a non-zero 
    integer for the projection value, the operation treats the 
    value as `true`.

* - `<field>: <0 or false>`

  - Specifies the exclusion of a field.

* - `"<field>.$": <1 or true>`

  - Uses the `$` array projection operator to return 
    the first element that matches the query condition on the
    array field. If you specify a non-zero integer for the 
    projection value, the operation treats the value as `true`. 

    Not available for views.

* - `<field>: <array projection>`

  - Uses the array projection operators (`$elemMatch`,
    `$slice`) to specify the array elements to
    include. 

    Not available for views.

* - `<field>: <$meta expression>`

  - Uses the `$meta` operator expression to specify 
    the inclusion of available `per-document metadata`. 

    Not available for views.

* - `<field>: <aggregation expression>`

  - Specifies the value of the projected field.

    With the use of aggregation expressions and syntax, including the use of literals and 
    aggregation variables, you can project new fields or project existing 
    fields with new values.

    - If you specify a non-numeric, non-boolean literal (such as a
      literal string or an array or an operator expression) for
      the projection value, the field is projected with the new
      value, for example:

      - `{ field: [ 1, 2, 3, "$someExistingField" ] }`
      - `{ field: "New String Value" }`
      - `{ field: { status: "Active", total: { $sum: "$existingArray" } } }`

    - To project a literal value for a field, use the
      `$literal` aggregation expression; for example:

      - `{ field: { $literal: 5 } }`
      - `{ field: { $literal: true } }`
      - `{ field: { $literal: { fieldWithValue0: 0, fieldWithValue1: 1 } } }` 

#### Embedded Field Specification

For fields in an embedded documents, you can specify the field using
either:

- dot notation, for example `"field.nestedfield": <value>`

- nested form, for example `{ field: { nestedfield: <value> } }`

#### `_id` Field Projection

The `_id` field is included in the returned documents by default unless
you explicitly specify `_id: 0` in the projection to suppress the field.

#### Inclusion or Exclusion

A `projection` *cannot* contain *both* include and exclude
specifications, with the exception of the `_id` field:

- In projections that *explicitly include* fields, the `_id` field is
  the only field that you can *explicitly exclude*.

- In projections that *explicitly excludes* fields, the `_id` field
  is the only field that you can *explicitly include*; however, the
  `_id` field is included by default.

For more information on projection, see also:

- find-projection

- read-operations-projection

## Examples

### With Empty Query Specification

The following operation returns a single document from
the bios collection:

```javascript
db.bios.findOne()
```

### With a Query Specification

The following operation returns the first matching document from the
bios collection where either
the field `first` in the embedded document `name` starts with the letter
`G` **or** where the field `birth` is less than ``new
Date('01/01/1945')``:

```javascript
db.bios.findOne(
   {
     $or: [
            { 'name.first' : /^G/ },
            { birth: { $lt: new Date('01/01/1945') } }
          ]
   }
)
```

### With a Projection

The `projection` parameter specifies which fields to return. The
parameter contains either include or exclude specifications, not both,
unless the exclude is for the `_id` field.

#### Specify the Fields to Return

The following operation finds a document in the bios collection and returns only the `name`,
`contribs` and `_id` fields:

```javascript
db.bios.findOne(
    { },
    { name: 1, contribs: 1 }
)
```

#### Return All but the Excluded Fields

The following operation returns a document in the bios collection where the `contribs` field
contains the element `OOP` and returns all fields *except* the `_id`
field, the `first` field in the `name` embedded document, and the
`birth` field:

```javascript
db.bios.findOne(
   { contribs: 'OOP' },
   { _id: 0, 'name.first': 0, birth: 0 }
)
```

### With an Option

The following operation uses the `sort` option to return the first 
matching document from the *sorted* `bios` collection. In this example, 
the collection is sorted by `birth` in ascending order.

```javascript
db.bios.findOne(
   { },
   { },
   { sort: { birth: 1 } }
)
```

### The `findOne` Result Document

You cannot apply cursor methods to the result of
`findOne()` because a single document is
returned. You have access to the document directly:

```javascript
var myDocument = db.bios.findOne();

if (myDocument) {
   var myName = myDocument.name;

   print (tojson(myName));
}
```

### Use Variables in `let` Option

You can specify query options to modify query behavior and indicate how
results are returned.

For example, to define variables that you can access elsewhere in the
`findOne` method, use the `let` option. To filter results using a
variable, you must access the variable within the `$expr`
operator.

Create a collection `cakeFlavors`:

```javascript
db.cakeFlavors.insertMany( [
   { _id: 1, flavor: "chocolate" },
   { _id: 2, flavor: "strawberry" },
   { _id: 3, flavor: "cherry" }
] )
```

The following example defines a `targetFlavor` variable in `let` and
uses the variable to retrieve the chocolate cake flavor:

```javascript
db.cakeFlavors.findOne(
   { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   { _id: 0 },
   { let : { targetFlavor: "chocolate" }
} )
```

Output:

```javascript
{ flavor: 'chocolate' }
```

To see all available query options, see :node-api-4.0:`FindOptions
</interfaces/findoptions.html>`.
