<!-- Converted from reference/operator/projection/positional.txt (reStructuredText). Includes are inlined. -->

# \$  (projection operator)

## Definition

**`$`**

The positional `$` operator limits the contents of an
`<array>` to return the first element that matches the query
condition on the array.

Use `$` in the projection document of the
`find()` method or the
`findOne()` method when you only need one
particular array element in selected documents.

See the aggregation operator `$filter` to return an
array with only those elements that match the specified condition.

**Note:** Disambiguation

To specify an array element to update, see the
positional $ operator for updates.

      

## Usage Considerations

Both the `$` operator and the `$elemMatch` operator project
the **first** matching element from an array based on a condition.

The `$` operator projects the first matching array element from each 
document in a collection based on some condition from the query statement.

The `$elemMatch` projection operator takes an explicit condition
argument.  This allows you to project based on a condition not in the query, or
if you need to project based on multiple fields in the array's embedded documents.
See array-field-limitation for an example.

`db.collection.find()` operations on views do not support `$` projection operator.

## Behavior

### Syntax

To return the first array element that matches the specified query
condition on the array:

```javascript
db.collection.find( { <array>: <condition> ... },
                    { "<array>.$": 1 } )
db.collection.find( { <array.field>: <condition> ...},
                    { "<array>.$": 1 } )
```

You can use the `$` operator to limit an `<array>` field, which 
does not appear in the query document. 
In previous versions of MongoDB, the `<array>` field being limited
**must** appear in the query document.

```javascript
db.collection.find( { <someOtherArray>: <condition> ... }, 
                    { "<array>.$" : 1 } )
```

**Important:**

To ensure expected behavior, the arrays used in the query document
and the projection document must be the same length. If the arrays are
different lengths, the operation may error in certain scenarios.

### Array Field Limitations

MongoDB requires the following when dealing with projection over arrays:

- Only one positional `$` operator may appear in the projection
  document.

- Only one array field should appear in the
  query document. Additional
  array fields in the query document may lead to undefined behavior.

  For example, the following projection may lead to
  undefined behavior:

  ```javascript
  db.collection.find( { <array>: <value>, <someOtherArray>: <value2> },
                      { "<array>.$": 1 } )
  ```

- The query document should only
  contain a single condition on the array field to which it is applied.
  Multiple conditions may override each other internally and lead to
  undefined behavior.

  To specify criteria on multiple fields of documents inside that array, use the
  `$elemMatch` query operator. The following query returns the first 
  document inside a `grades` array that has a `mean` of greater than 70
  and a `grade` of greater than 90.

  ```javascript
  db.students.find( { grades: { $elemMatch: {
                                              mean: { $gt: 70 },
                                              grade: { $gt:90 }
                                            } } },
                    { "grades.$": 1 } )
  ```

  You must use the `$elemMatch` operator if you need separate conditions
  for selecting documents and for choosing fields within those documents.

### Sorts and the Positional Operator

When the `find()` method includes a
`sort()`, the `find()`
method applies the `sort()` to order the matching
documents **before** it applies the positional `$`
projection operator.

If an array field contains multiple documents with the same field
name and the `find()` method includes a
`sort()` on that repeating field, the returned
documents may not reflect the sort order because the sort was
applied to the elements of the array before the `$`
projection operator.

### Positional Operator Placement Restriction

The `$` projection operator can only appear at the end of the 
field path, for example `"field.$"` or `"fieldA.fieldB.$"`.

For example, the following operation is invalid:

```javascript
db.inventory.find( { }, { "instock.$.qty": 1 } )
```

To resolve, remove the component of the field path that follows the
`$` projection operator.

       

### Positional Operator and `$slice` Restriction

`find` and `findAndModify` projection cannot include `$slice` projection 
expression as part of a `$` projection expression. 

For example, the following operation is invalid:

```javascript
db.inventory.find( { "instock.qty": { $gt: 25 } }, { "instock.$": { $slice: 1 } } ) 
```

In previous versions, MongoDB returns the first element
(`instock.$`) in the `instock` array that matches the query
condition; i.e. the positional projection `"instock.$"` takes
precedence and the `$slice:1` is a no-op. The ``"instock.$": {
$slice: 1 }`` does not exclude any other document field.

## Examples

### Project Array Values

A collection `students` contains the following documents:

```javascript
{ "_id" : 1, "semester" : 1, "grades" : [ 70, 87, 90 ] }
{ "_id" : 2, "semester" : 1, "grades" : [ 90, 88, 92 ] }
{ "_id" : 3, "semester" : 1, "grades" : [ 85, 100, 90 ] }
{ "_id" : 4, "semester" : 2, "grades" : [ 79, 85, 80 ] }
{ "_id" : 5, "semester" : 2, "grades" : [ 88, 88, 92 ] }
{ "_id" : 6, "semester" : 2, "grades" : [ 95, 90, 96 ] }
```

In the following query, the projection `{ "grades.$": 1 }`
returns only the first element greater than or equal to `85`
for the `grades` field.

```javascript
db.students.find( { semester: 1, grades: { $gte: 85 } },
                  { "grades.$": 1 } )
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "grades" : [ 87 ] }
{ "_id" : 2, "grades" : [ 90 ] }
{ "_id" : 3, "grades" : [ 85 ] }
```

Although the array field `grades` may contain multiple elements
that are greater than or equal to `85`, the `$`
projection operator returns only the first matching element from the
array.

### Project Array Documents

A `students` collection contains the following documents
where the `grades` field is an array of documents; each document
contain the three field names `grade`, `mean`, and `std`:

```javascript
{ "_id" : 7, semester: 3, "grades" : [ { grade: 80, mean: 75, std: 8 },
                                       { grade: 85, mean: 90, std: 5 },
                                       { grade: 90, mean: 85, std: 3 } ] }

{ "_id" : 8, semester: 3, "grades" : [ { grade: 92, mean: 88, std: 8 },
                                       { grade: 78, mean: 90, std: 5 },
                                       { grade: 88, mean: 85, std: 3 } ] }
```

In the following query, the projection `{ "grades.$": 1 }`
returns only the first element with the `mean` greater
than `70` for the `grades` field:

```javascript
db.students.find(
   { "grades.mean": { $gt: 70 } },
   { "grades.$": 1 }
)
```

The operation returns the following documents:

```javascript
{ "_id" : 7, "grades" : [  {  "grade" : 80,  "mean" : 75,  "std" : 8 } ] }
{ "_id" : 8, "grades" : [  {  "grade" : 92,  "mean" : 88,  "std" : 8 } ] }
```

## Further Reading

`$elemMatch (projection)`
