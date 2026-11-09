<!-- Converted from reference/operator/aggregation/sortArray.txt (reStructuredText). Includes are inlined. -->

# $sortArray  (expression operator)

## Definition

**`$sortArray`**

**New in version:** 5.2

Sorts an array based on its elements. The sort order is user
specified. 

`$sortArray` has the following syntax:

```javascript
$sortArray: {
   input: <array>,
   sortBy: <sort spec>
}
```

* - Field
  - Type
  - Description

* - `input`
  - expression
  - The array to be sorted.

    The result is `null` if the expression:

    - Evaluates to missing.
    - Evaluates to `null`.
    - Evaluates to `undefined`.

    If the expression evaluates to any other non-array value, the operation 
    results in an error.

* - `sortBy`
  - document or int (`1` or `-1`)
  - A value that specifies a sort ordering. Its possible values 
    are `1`, `-1`, or a document.

    If the value of `sortBy` is a document, sort ordering refers to 
    field-direction pairs that determine how to sort the array elements, 
    such as `{ name: 1, age: -1 }` where `1` indicates ascending order 
    and `-1` indicates descending order.

    If the value of `sortBy` is `1`, MongoDB sorts the array in ascending order.
    If the value of `sortBy` is `-1`, MongoDB sorts the array in descending order.

## Behavior

The `$sortArray` expression orders the `input` array
according to the `sortBy` specification.

The `$sortArray` syntax and semantics are the same as the
behavior in a `$push` operation modified by `$sort`.

### Sort by Document Fields

If the array elements are documents, you can sort by a document field.
Specify the field name and a sort direction, ascending (`1`), or
descending (`-1` ).

```javascript
{
   input: <array-of-documents>,
   sortBy: { <document-field>: <sort-direction> }
}
```

### Sort by Value

To sort the whole array by value, or to sort by array elements that are
not documents, identify the input array and specify 1 for an ascending
sort or -1 for descending sort in the `sortBy` parameter.

```javascript
{
   input: <array-of-documents>,
   sortBy: <sort-direction>
}
```

### Considerations

- There is no implicit array traversal on the sort key.
- Positional operators are not supported. A field name like "values.1"
  denotes a sub-field called "1" in the `values` array. It does not
  refer to the item at index 1 in the `values` array.
- When a whole array is sorted, the sort is lexicographic. The
  aggregation `$sort` stage, behaves differently. See
  `$sort` for more details.
- When an array is sorted by a field, any documents or scalars that do
  not have the specified field are sorted equally. The resulting sort
  order is undefined.
- `null` values and missing values sort equally.

### Sort Stability

The stability of the sort is not specified. Users should not rely on
`$sortArray` to use a particular sorting algorithm.

## Examples

The examples in this section use a `team` array in an `engineers` collection. 

```javascript
db.engineers.insertOne(
   {
      team:
         [
            {
               name: "pat",
               age: 30,
               address: { street: "12 Baker St", city: "London" }
            },
            {
               name: "dallas",
               age: 36,
               address: { street: "12 Cowper St", city: "Palo Alto" }
            },
            {
              name: "charlie",
              age: 42,
              address: { street: "12 French St", city: "New Brunswick" }
            }
         ]
   }
)
```

The `team` array has three elements. Each element of `team` has
nested sub-elements: `name`, `age`, and `address`. The following
examples show how to sort the `team` array using these sub-elements. 

### Sort on a Field

The following operation sorts on the `name` field within the `team` array:

```javascript
db.engineers.aggregate( [
   { $project: 
      {
         _id: 0,
         result:
            {
               $sortArray: { input: "$team", sortBy: { name: 1 } }
            }
      }
   }
] )
```

The operation returns the following results:

```javascript
{
   result:
      [
         {
            name: 'charlie',
            age: 42,
            address: { street: '12 French St', city: 'New Brunswick' }
         },
         {
            name: 'dallas',
            age: 36,
            address: { street: '12 Cowper St', city: 'Palo Alto' }
         },
         {
            name: 'pat',
            age: 30,
            address: { street: '12 Baker St', city: 'London' }
         }
      ]
}
```

### Sort on a Subfield

The following operation uses dot notation to sort the array based on the
`address` subfield:

```javascript
db.engineers.aggregate( [
   { 
      $project: 
         {
        	   _id: 0,
        	   result: 
               {
                  $sortArray:
                     {
                        input: "$team",
                        sortBy: { "address.city": -1 }
                     }
               }
        	}
   }
] )
```

The sort direction is descending because the `sortBy` value is "-1".

```javascript
{
   result: [
      {
         name: 'dallas',
         age: 36,
         address: { street: '12 Cowper St', city: 'Palo Alto' }
      },
      {
         name: 'charlie',
         age: 42,
         address: { street: '12 French St', city: 'New Brunswick' }
      },
      {
         name: 'pat',
         age: 30,
         address: { street: '12 Baker St', city: 'London' }
      }
  ]
}
```

### Sort on Multiple Fields

The following operation specifies multiple index fields to do a compound sort
within the `$sortArray` operation:

```javascript
db.engineers.aggregate( [
   {
      $project:
         {
            _id: 0,
            result:
               {
                  $sortArray:
                     {
                        input: "$team",
                        sortBy: { age: -1, name: 1 }
                     }
               }
         }
    }
 ] )
```

Example output:

```javascript
{
   result: [
      {
         name: 'charlie',
         age: 42,
         address: { street: '12 French St', city: 'New Brunswick' }
      },
      {
         name: 'dallas',
         age: 36,
         address: { street: '12 Cowper St', city: 'Palo Alto' }
      },
      {
         name: 'pat',
         age: 30,
         address: { street: '12 Baker St', city: 'London' }
      }
   ]
}
```

### Sort an Array of Integers

This example specifies an input array directly. The values are all
the same type, Int32:

```javascript
db.engineers.aggregate( [
   { 
      $project: 
         {
            _id: 0,
            result: 
               { 
                  $sortArray: 
                     {
                         input: [ 1, 4, 1, 6, 12, 5 ],
                         sortBy: 1 
                     } 
               }
         }
   }
] )
```

Example output:

```javascript
[ { result: [ 1, 1, 4, 5, 6, 12 ] } ]
```

The input array has a "1" in position 0 and position 2. The ones are
grouped together in the results, but their are no guarantees regarding
how the group of ones is sorted relative to their original order. 

### Sort on Mixed Type Fields

This example specifies an input array directly. The values have
different types:

```javascript
db.engineers.aggregate( [
   { 
      $project: 
         {
            _id: 0,
            result: 
            { 
               $sortArray: 
                  {
                     input: [ 20, 4, { a: "Free" }, 6, 21, 5, "Gratis", 
                             { a: null }, { a: { sale: true, price: 19 } },
                             Decimal128( "10.23" ), { a: "On sale" } ],
                     sortBy: 1 
                  }
            }
         }
   }
] )
```

Example output:

```javascript
{ result: 
   [
      4,
      5,
      6,
      Decimal128("10.23"),
      20,
      21,
      'Gratis',
      { a: null },
      { a: 'Free' },
      { a: 'On sale' },
      { a: { sale: true, price: 19 } }
   ] 
}
```

The results are ordered. 

In contrast, after changing the `sortBy` field to sort on the one of
the document fields, `sortBy: { a: 1 }`, the sort order for the
scalar and `null` values is undefined:

```javascript
 :copyable: false

{ result: 
    [
       20,
       4,
       6,
       21,
       5,
       'Gratis',
       { a: null },
       Decimal128("10.23"),
       { a: 'Free' },
       { a: 'On sale' },
       { a: { sale: true, price: 19 } }
    ] 
 }
```
