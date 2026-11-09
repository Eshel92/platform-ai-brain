<!-- Converted from reference/operator/projection/elemMatch.txt (reStructuredText). Includes are inlined. -->

# $elemMatch (projection)

**See also:**

/reference/operator/query/elemMatch

## Definition

**`$elemMatch`**

The `$elemMatch` operator limits the contents of an
`<array>` field from the query results to contain only the **first**
element matching the `$elemMatch` condition.

## Usage Considerations

### Returned Element

Both the `$` operator and the `$elemMatch` operator project
the **first** matching element from an array based on a condition.

The `$` operator projects the first matching array element from each 
document in a collection based on some condition from the query statement.

The `$elemMatch` projection operator takes an explicit condition
argument.  This allows you to project based on a condition not in the query, or
if you need to project based on multiple fields in the array's embedded documents.
See array-field-limitation for an example.

### Field Order

Regardless of the ordering of the fields in the document, the 
`$elemMatch` projection of an existing field returns 
the field after the other existing field inclusions.

For example, consider a `players` collection with the following document:

```javascript
db.players.insertOne( { 
   name: "player1", 
   games: [ { game: "abc", score: 8 }, { game: "xyz", score: 5 } ], 
   joined: new Date("2020-01-01"),
   lastLogin: new Date("2020-05-01")
} )
```

The following projection returns the `games` field
after the other existing fields included in the projection even though
in the document, the field is listed before `joined` and
`lastLogin` fields:

```javascript
db.players.find( {}, { games: { $elemMatch: { score: { $gt: 5 } } }, joined: 1, lastLogin: 1 } )
```

That is, the operation returns the following document:

```javascript
{ 
   "_id" : ObjectId("5edef64a1c099fff6b033977"),
   "joined" : ISODate("2020-01-01T00:00:00Z"),
   "lastLogin" : ISODate("2020-05-01T00:00:00Z"),
   "games" : [ { "game" : "abc", "score" : 8 } ]
}
```

### Restrictions

- .. include:: /includes/extracts/views-unsupported-projection-$elemMatch.rst

- You cannot specify a `$text` query expression in an
  `$elemMatch`.

## Examples

The examples on the `$elemMatch` projection operator
assumes a collection `schools` with the following documents:

```javascript
{
 _id: 1,
 zipcode: "63109",
 students: [
              { name: "john", school: 102, age: 10 },
              { name: "jess", school: 102, age: 11 },
              { name: "jeff", school: 108, age: 15 }
           ]
}
{
 _id: 2,
 zipcode: "63110",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ]
}
{
 _id: 3,
 zipcode: "63109",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ]
}
{
 _id: 4,
 zipcode: "63109",
 students: [
              { name: "barney", school: 102, age: 7 },
              { name: "ruth", school: 102, age: 16 },
           ]
}
```

### Zipcode Search

The following `find()` operation
queries for all documents where the value of the `zipcode`
field is `63109`. The `$elemMatch` projection
returns only the **first** matching element of the `students`
array where the `school` field has a value of `102`:

```javascript
db.schools.find( { zipcode: "63109" },
                 { students: { $elemMatch: { school: 102 } } } )
```

The operation returns the following documents that have `zipcode`
equal to `63109` and projects the `students` array using
`$elemMatch`:

```javascript
{ "_id" : 1, "students" : [ { "name" : "john", "school" : 102, "age" : 10 } ] }
{ "_id" : 3 }
{ "_id" : 4, "students" : [ { "name" : "barney", "school" : 102, "age" : 7 } ] }
```

- For the document with `_id` equal to `1`, the `students`
  array contains multiple elements with the `school` field
  equal to `102`. However, the `$elemMatch`
  projection returns only the first matching element from the
  array.

- The document with `_id` equal to `3` does not contain the
  `students` field in the result since no element in its
  `students` array matched the `$elemMatch`
  condition.

### `$elemMatch` with Multiple Fields

The `$elemMatch` projection can specify criteria on multiple
fields:

The following `find()` operation
queries for all documents where the value of the `zipcode`
field is `63109`. The projection includes the **first**
matching element of the `students` array where the `school`
field has a value of `102` **and** the `age` field is greater
than `10`:

```javascript
db.schools.find( { zipcode: "63109" },
                 { students: { $elemMatch: { school: 102, age: { $gt: 10} } } } )
```

The operation returns the three documents that have `zipcode` equal to `63109`:

```javascript
{ "_id" : 1, "students" : [ { "name" : "jess", "school" : 102, "age" : 11 } ] }
{ "_id" : 3 }
{ "_id" : 4, "students" : [ { "name" : "ruth", "school" : 102, "age" : 16 } ] }
```

The document with `_id` equal to `3` does not contain the `students` field
since no array element matched the `$elemMatch` criteria.

**See also:**

`$ (projection)` operator
