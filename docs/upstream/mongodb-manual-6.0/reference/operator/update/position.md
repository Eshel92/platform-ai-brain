<!-- Converted from reference/operator/update/position.txt (reStructuredText). Includes are inlined. -->

# $position

## Definition

**`$position`**

The `$position` modifier specifies the location in the
array at which the `$push` operator inserts elements.
Without the `$position` modifier, the `$push`
operator inserts elements to the end of the array. See $push
modifiers for more information.

To use the `$position` modifier, it **must** appear with the
`$each` modifier.

```javascript
{
  $push: {
    <field>: {
       $each: [ <value1>, <value2>, ... ],
       $position: <num>
    }
  }
}
```

`<num>` indicates the position in the array, based on a zero-based 
array index (position):

- A non-negative number corresponds to the position in the array,
  starting from the beginning of the array. If the value of
  `<num>` is greater or equal to the length of the array, the
  `$position` modifier has no effect and `$push`
  adds elements to the end of the array.

- A negative number corresponds to the position in the array,
  counting from (but not including) the last element of the array.
  For example, `-1` indicates the position just before the last
  element in the array. If you specify multiple elements in the
  `$each` array, the last added element is in the specified
  position from the end. If the absolute value of `<num>` is
  greater than or equal to the length of the array, the `$push`
  adds elements to the beginning of the array.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

## Examples

### Add Elements at the Start of the Array

Create the `students` collection:

```javascript
db.students.insertOne( { "_id" : 1, "scores" : [ 100 ] } )
```

The following operation updates the `scores` field to add the
elements `50`, `60` and `70` to the beginning of the array:

```javascript
db.students.updateOne(
   { _id: 1 },
   {
     $push: {
        scores: {
           $each: [ 50, 60, 70 ],
           $position: 0
        }
     }
   }
)
```

The operation results in the following updated document:

```javascript
{ "_id" : 1, "scores" : [  50,  60,  70,  100 ] }
```

### Add Elements to the Middle of the Array

Add a document to the `students` collection:

```javascript
db.students.insertOne( { "_id" : 2, "scores" : [  50,  60,  70,  100 ] } )
```

The following operation updates the `scores` field to add the
elements `20` and `30` at the array index (position) of `2`:

```javascript
db.students.updateOne(
   { _id: 2 },
   {
     $push: {
        scores: {
           $each: [ 20, 30 ],
           $position: 2
        }
     }
   }
)
```

The operation results in the following updated document:

```javascript
{ "_id" : 2, "scores" : [  50,  60,  20,  30,  70,  100 ] }
```

### Use a Negative Array Index (Position) to Add Elements to the Array

`$position` can accept a negative array index (position) value 
to indicate the position starting from the end, counting from (but not 
including) the last element of the array. For example, `-1` indicates 
the position just before the last element in the array.

Add the following document to the `students` collection:

```javascript
db.students.insertOne(
   { "_id" : 3, "scores" : [  50,  60,  20,  30,  70,  100 ] }
)
```

The following operation specifies `-2` for the `$position` to
add `90` at the position two places before the last element, and then
`80` at the position two places before the last element.

**Important:**

With a negative array index (position), if you specify multiple 
elements in the `$each` array, the last added element is in 
the specified position from the end.

```javascript
db.students.updateOne(
   { _id: 3 },
   {
     $push: {
        scores: {
           $each: [ 90, 80 ],
           $position: -2
        }
     }
   }
)
```

The operation results in the following updated document:

```javascript
{ "_id" : 3, "scores" : [ 50, 60, 20, 30, 90, 80, 70, 100 ] }
```
