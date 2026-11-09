<!-- Converted from reference/operator/projection/slice.txt (reStructuredText). Includes are inlined. -->

# $slice (projection)

## Definition

**`$slice`**

The `$slice` projection operator specifies the number of
elements in an array to return in the query result.

**Note:** Disambiguation

The $slice projection operator can only be used within
a find command projection. To use $slice 
anywhere an expression can be used, see the `$slice` 
expression operator. 

For information on limiting the size of an array during an update
with `$push`, see the `$slice` update modifier instead.

## Syntax

The `$slice` has one of the following syntax forms:

```javascript
db.collection.find( 
   <query>, 
   { <arrayField>: { $slice: <number> } } 
);
```

or

```javascript
db.collection.find( 
   <query>, 
   { <arrayField>: { $slice: [ <number>, <number> ] } } 
);
```

* - Value
  - Description

* - `$slice: <number>`

  - Specifies the number of elements to return in the
    `<arrayField>`. For `<number>`:

    - Specify a positive number `n` to return the first `n`
      elements.

    - Specify a negative number `n` to return the last `n`
      elements.

    If the `<number>` is greater than the number of array
    elements, the query returns all array elements.

* - `$slice: [ <number to skip>, <number to return> ]`

  - Specifies the number of elements to return in the
    `<arrayField>` after skipping the specified number of elements
    starting from the first element. You must specify both elements.

    For the `<number to skip>`:

    - Specify a positive number `n` to skip `n` elements from
      the start of the array; i.e. 0th index position. Based on a
      zero-based array index, `1` indicates the starting position
      of the 2nd element, etc. If `n` is greater than the number
      of array elements, the query returns an empty array for the
      `<arrayField>`.

    - Specify a negative number `n` to skip backward `n`
      elements from the start of the array; i.e. 0th index position
      Based on a zero-based array index (i.e. the first element is
      at index 0), `-1` indicates the starting position of the
      last element, etc. If the absolute value of the negative
      number is greater than the number of array elements, the
      starting position is the start of the array.

    For the `<number to return>`, you must specify a 
    *positive* number `n` to return the next `n` elements,
    starting after skipping the specified number.

## Behavior

### `$slice` of Embedded Array

The `$slice` projection of an array in an nested document no 
longer returns the other fields in the nested document when the projection 
is part of an inclusion projection. 

For example, consider a collection `inventory` with documents that
contain a `size` field:

```javascript
{ item: "socks", qty: 100, details: { colors: [ "blue", "red" ], sizes: [ "S", "M", "L"] } }
```

The following operation projects the `_id` field (by default), the 
`qty` field, and the `details` field with just the specified slice 
of the `colors` array:

```javascript
db.inventory.find( { }, { qty: 1, "details.colors": { $slice: 1 } } )
```

That is, the operation returns the following document:

```javascript
{ "_id" : ObjectId("5ee92a6ec644acb6d13eedb1"), "qty" : 100, "details" : { "colors" : [ "blue" ] } }
```

If the `$slice` projection is part of an exclusion
projection, the operation continues to return the other fields in
the nested document. That is, the following projection is an
exclusion projection. The projection excludes the `_id` field and
the elements in the `colors` array that fall outside the specified
slice and returns all other fields.

```javascript
db.inventory.find( { }, { _id: 0, "details.colors": { $slice: 1 } } )
```

```javascript
{ "item" : "socks", "qty" : 100, "details" : { "colors" : [ "blue" ], "sizes" : [ "S", "M", "L" ] } }
```

The `$slice` projection by itself is considered an exclusion.

In previous versions, the `$slice` projection also
include the other fields in the nested document regardless of
whether the projection is an inclusion or an exclusion.

### View Restriction

`db.collection.find()` operations on views do not support `$slice` projection operator.

### `$` Positional Operator and `$slice` Restriction

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

### Path Collision: `$slice` of an Array and Embedded Fields

`find` and `findAndModify` projection cannot contain both a `$slice` of an 
array and a field embedded in the array. 

For example, consider a collection `inventory` that contains an array
field `instock`:

```javascript
{ ..., instock: [ { warehouse: "A", qty: 35 }, { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ], ... }
```

The following operation fails with a ``Path
collision`` error:

```javascript
db.inventory.find( {}, { "instock": { $slice: 1 }, "instock.warehouse": 0 } ) 
```

In previous versions, the projection applies both projections and
returns the first element (`$slice: 1`) in the `instock` array
but suppresses the `warehouse` field in the projected element.
Starting in MongoDB 4.4, to achieve the same result, use the
`db.collection.aggregate()` method with two separate
`$project` stages.

**See also:**

find-projection

## Examples

Create an example collection `posts` with the following documents:

```javascript
db.posts.insertMany([
   {
     _id: 1, 
     title: "Bagels are not croissants.", 
     comments: [ { comment: "0. true" }, { comment: "1. croissants aren't bagels."} ]
   },
   {
     _id: 2, 
     title: "Coffee please.", 
     comments: [ { comment: "0. fooey" }, { comment: "1. tea please" }, { comment: "2. iced coffee" }, { comment: "3. cappuccino" }, { comment: "4. whatever" } ]
   }
])
```

### Return an Array with Its First 3 Elements

The following operation uses the `$slice` projection
operator on the `comments` array to return the array with its first
three elements. If the array has less than three elements, all elements
in the array are returned.

```javascript
db.posts.find( {}, { comments: { $slice: 3 } } )
```

The operation returns the following documents:

```javascript
{
   "_id" : 1, 
   "title" : "Bagels are not croissants.", 
   "comments" : [ { "comment" : "0. true" }, { "comment" : "1. croissants aren't bagels." } ] 
}
{ 
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "0. fooey" }, { "comment" : "1. tea please" }, { "comment" : "2. iced coffee" } ]
}
```

### Return an Array with Its Last 3 Elements

The following operation uses the `$slice` projection
operator on the `comments` array to return the array with its last
three elements. If the array has less than three elements, all elements
in the array are returned.

```javascript
db.posts.find( {}, { comments: { $slice: -3 } } )
```

The operation returns the following documents:

```javascript
{ 
   "_id" : 1, 
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "0. true" }, { "comment" : "1. croissants aren't bagels." } ]
}
{ 
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "2. iced coffee" }, { "comment" : "3. cappuccino" }, { "comment" : "4. whatever" } ]
}
```

### Return an Array with 3 Elements After Skipping the First Element

The following operation uses the `$slice` projection
operator on the `comments` array to:

- Skip the first element such that the second element is the starting
  point.

- Then, return three elements from the starting point.

If the array has less than three
elements after the skip, all remaining elements are returned.

```javascript
db.posts.find( {}, { comments: { $slice: [ 1, 3 ] } } )
```

The operation returns the following documents:

```javascript
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "1. croissants aren't bagels." } ]
}

{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "1. tea please" }, { "comment" : "2. iced coffee" }, { "comment" : "3. cappuccino" } ]
}
```

### Return an Array with 3 Elements After Skipping the Last Element

The following operation uses the `$slice` projection
operator on the `comments` array to

- Skip backwards from the first element such that the last element is
  the starting point.

- Then, return three elements from the starting point.

If the array has less than three elements after the skip, all remaining
elements in the array are returned.

```javascript
db.posts.find( {}, { comments: { $slice: [ -1, 3 ] } } )
```

The operation returns the following documents:

```javascript
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "1. croissants aren't bagels." } ]
}
{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "4. whatever" } ]
}
```
