<!-- Converted from reference/operator/projection/elemMatch.txt (reStructuredText). Includes are inlined. -->

# $elemMatch (projection operator)

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

- You cannot specify a `$text` query operator in an
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
},
{
 _id: 2,
 zipcode: "63110",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ],
 athletics: [ "swimming", "basketball", "football" ]
},
{
 _id: 3,
 zipcode: "63109",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ],
 athletics: [ "baseball", "basketball", "soccer" ]
},
{
 _id: 4,
 zipcode: "63109",
 students: [
              { name: "barney", school: 102, age: 7 },
              { name: "ruth", school: 102, age: 16 },
           ]
}
```

You can model these documents by using the following C# classes:

```csharp
public class School
{
    public string Id { get; set; }

    [BsonElement("zipcode")]
    public string ZipCode { get; set; }

    public Student[] Students { get; set; }

    public string[] Athletics { get; set; }
}
```

```csharp
public class Student
{
    public string Id { get; set; }

    public string Name { get; set; }

    public int School {  get; set; }

    public int Age {  get; set; }
}
```

### Zipcode Search

The following `find()` operation
queries for all documents where the value of the `zipcode`
field is `"63109"`. The `$elemMatch` projection
returns only the **first** matching element of the `students`
array where the `school` field has a value of `102`:

```javascript
db.schools.find( { zipcode: "63109" },
                { students: { $elemMatch: { school: 102 } } } )
```

To perform an `$elemMatch` projection when using the .NET/C# driver, call the
`ElemMatch()` method on the projection builder. Pass the name of the array field
to project and the filter to apply to the array elements.

The following code example finds all documents in which the value of the `Zipcode`  
field is `"63109"`. For each matching document, the projection returns the
following fields:  

- `Id` 
- The first element of the `Students` array in which the value of the nested
  `School` field has the value `102`

```csharp
var results = schoolsCollection
    .Find(s => s.ZipCode == "63109")
    .Project(Builders<School>.Projection.ElemMatch(
        field: school => school.Students,
        filter: student => student.School == 102
   )
).ToList();
```

The operation returns the following documents that have a `zipcode` value of
`"63109"` and projects the `students` array using
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
fields.

The following `find()` operation
queries for all documents where the value of the `zipcode`
field is `"63109"`. The projection includes the **first**
matching element of the `students` array where the `school`
field has a value of `102` **and** the `age` field is greater
than `10`:

```javascript
db.schools.find( { zipcode: "63109" },
                { students: { $elemMatch: { school: 102, age: { $gt: 10} } } } )
```

The following code example finds all documents in which the value of the `Zipcode`  
field is `"63109"`. For each matching document, the projection returns the following fields:  

- `Id` 
- The first element of the `Students` array in which the value of the nested
  `School` field has the value `102` and the `Age` field has a value greater than
  `10`

```csharp
var results = schoolsCollection
    .Find(s => s.ZipCode == "63109")
    .Project(Builders<School>.Projection.ElemMatch(
            field: school => school.Students,
            filter: student => (student.School == 102) && (student.Age > 10) 
        )
    ).ToList();
```

The operation returns the three documents that have a `zipcode` value of `"63109"`:

```javascript
{ "_id" : 1, "students" : [ { "name" : "jess", "school" : 102, "age" : 11 } ] }
{ "_id" : 3 }
{ "_id" : 4, "students" : [ { "name" : "ruth", "school" : 102, "age" : 16 } ] }
```

The document with `_id` equal to `3` does not contain the `students` field
since no array element matched the `$elemMatch` criteria.

The argument to `$elemMatch` matches elements of the array that
`$elemMatch` is projecting. If you specify an equality with a field
name to `$elemMatch`, it attempts to match objects within the array.
For example, `$elemMatch` attempts to match objects, instead of scalar
values, within the array for the following in the projection:

```javascript
db.schools.find( { zipcode: "63109" },
                { athletics: { $elemMatch: { athletics: "basketball" } } })
```

```csharp
var results = schoolsCollection
    .Find(s => s.ZipCode == "63109")
    .Project(Builders<School>.Projection.ElemMatch(
            "athletics",
            Builders<School>.Filter.Eq("athletics", "basketball"))
    ).ToList();
```

The preceding examples return the documents that have a `zipcode` value of
`"63109"`, but these documents include only the `_id` field because the projection
operation found no matching elements.

To match scalar values, use the equality operator along with the scalar
value that you want to match (`{$eq: <scalar value>}`). For example,
the following `find()` operation queries for all
documents where the value of the `zipcode` field is `"63109"`. The
projection includes the matching element of the `athletics` array
where the value is `basketball`:

```javascript
db.schools.find( { zipcode: "63109" },
                { athletics: { $elemMatch: { $eq: "basketball" } } })
```

To perform an `$elemMatch` operation against scalar values in an array when using
the .NET/C# driver, call the `ElemMatch()` method
on the projection builder. Pass the name of the array field to project and an
equality filter for the field `"$eq"` and the value you want to compare against.

```csharp
var results = schoolsCollection
    .Find(s => s.ZipCode == "63109")
    .Project(Builders<School>.Projection.ElemMatch(
            "athletics",
            Builders<School>.Filter.Eq("athletics", "basketball"))
    ).ToList();
```

The operation returns the three documents that have `zipcode` value of
`"63109"`. The returned documents include the `_id` field and matching
elements of the `athletics` array, if any.

```javascript
[
   { _id: 1 },
   { _id: 3, athletics: [ 'basketball' ] },
   { _id: 4 }
]
```

The document with `_id` equal to `3` is the only document that
matched the `$elemMatch` criteria.

**See also:**

`$ (projection)` operator
