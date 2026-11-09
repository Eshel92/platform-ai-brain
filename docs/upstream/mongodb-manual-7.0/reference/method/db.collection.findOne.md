<!-- Converted from reference/method/db.collection.findOne.txt (reStructuredText). Includes are inlined. -->

# db.collection.findOne() (mongosh method)

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
`findOne()` returns a document
rather than a cursor.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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

`db.collection.findOne()` has the following
form:

```javascript
db.collection.findOne( <query>, <projection>, <options> )
```

`db.collection.findOne()` takes the following
parameters:

| Parameter | Type | Description |
|---|---|---|
| `query` | document | Optional. Specifies query selection criteria using query operators. |
| `projection` | document | Optional. Specifies the fields to return using projection operators. Omit this parameter to return all fields in the matching document. For details, see findOne-projection. |
| `options` | document | .. include:: /includes/find-options-description.rst |

## Behavior

### Client Disconnection

If the client that issued `findOne()` disconnects before the operation 
completes, MongoDB marks `findOne()` for termination using 
`killOp`.

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

**Note:**

You can specify projection in two ways for `find()` 
and `findOne()`:

- Setting the `projection` parameter
- Setting the `options` parameter to `projection`

If you specify both parameters, the `projection` parameter takes precedence. To use 
`options.projection`, set the `projection` parameter to `null` or 
`undefined`.

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

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### With Empty Query Specification

The following operation returns a single document from
the `movies` collection in the `sample_mflix` database:

```javascript
db.movies.findOne()
```

### With a Query Specification

The following operation returns the first matching document from the
`movies` collection where either the `title` field starts with the
letter "T" **or** the `year` field is less than 1950:

```javascript
db.movies.findOne(
   {
      $or: [
            { title: /^T/ },
            { year: { $lt: 1950 } }
            ]
   }
)
```

### With a Projection

The `projection` parameter specifies which fields to return. The
parameter contains either include or exclude specifications, not both,
unless the exclude is for the `_id` field.

#### Specify the Fields to Return

The following operation finds a document in the `movies` collection and
returns only the `title`, `genres`, and `imdb` fields:

```javascript
db.movies.findOne(
   { },
   { title: 1, genres: 1, imdb: 1 }
)
```

#### Return All but the Excluded Fields

The following operation returns a document in the `movies` collection
where the `cast` array contains `"Al Pacino"`. The projection returns all
fields *except* the `_id` field, the `votes` field in the `imdb`
embedded document, and the `fullplot` field:

```javascript
db.movies.findOne(
   { cast: 'Al Pacino' },
   { _id: 0, 'imdb.votes': 0, fullplot: 0 }
)
```

### With an Option

The following operation uses the `sort` option to return the first 
matching document from the *sorted* `movies` collection. In this
example, the collection is sorted by `year` in ascending order.

```javascript
db.movies.findOne(
   { },
   { },
   { sort: { year: 1 } }
)
```

### The `findOne` Result Document

You cannot apply cursor methods to the result of
`findOne()` because a single document is
returned. You have access to the document directly:

```javascript
var myDocument = db.movies.findOne();

if (myDocument) {
   var myTitle = myDocument.title;
   print(myTitle);
}
```

### Use Variables in `let` Option

You can specify query options to modify query behavior and indicate how
results are returned.

For example, to define variables that you can access elsewhere in the
`findOne` method, use the `let` option. To filter results using a
variable, you must access the variable within the `$expr`
operator.

The following example defines a `targetTitle` variable in `let` and
uses the variable to retrieve the movie titled `"The Godfather"`:

 :copyable: true

```javascript
```

Output:

```javascript
```
