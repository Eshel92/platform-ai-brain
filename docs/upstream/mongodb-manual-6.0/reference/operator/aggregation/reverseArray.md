<!-- Converted from reference/operator/aggregation/reverseArray.txt (reStructuredText). Includes are inlined. -->

# $reverseArray (aggregation)

   

## Definition

**`$reverseArray`**

Accepts an array expression as an argument and returns an array with the
elements in reverse order.

`$reverseArray` has the following operator
expression syntax:

```javascript
{ $reverseArray: <array expression> }
```

The argument can be any valid expression as long as it resolves to an array.

## Behavior

If  the argument resolves to a value of `null` or refers to a
missing field, `$reverseArray` returns `null`. 

If the argument does not resolve to an array or `null` nor refers
to a missing field, `$reverseArray` returns an error.

`$reverseArray` returns an empty array when the argument is an empty array.

If the argument contains subarrays, `$reverseArray` only operates on the top level array elements and will not reverse the contents of subarrays.

| Example [#literal]_ | Results |
|---|---|
| .. code-block:: javascript :copyable: false { $reverseArray: { $literal: [ 1, 2, 3 ] } } | `[ 3, 2, 1 ]` |
| .. code-block:: javascript :copyable: false { $reverseArray: { $slice:  [ [ "foo", "bar", "baz", "qux" ], 1, 2 ] } } } | `[ "baz", "bar" ]` |
| .. code-block:: javascript :copyable: false { $reverseArray: null } | `null` |
| .. code-block:: javascript :copyable: false { $reverseArray: { $literal: [ ] } } | `[ ]` |
| .. code-block:: javascript :copyable: false { $reverseArray: { $literal: [ [ 1, 2, 3 ], [ 4, 5, 6 ] ] } } | `[ [ 4, 5, 6 ], [ 1, 2, 3 ] ]` |

## Example

A collection named `users` contains the following documents:

```javascript
{ "_id" : 1, "name" : "dave123", "favorites" : [ "chocolate", "cake", "butter", "apples" ] }
{ "_id" : 2, "name" : "li", "favorites" : [ "apples", "pudding", "pie" ] }
{ "_id" : 3, "name" : "ahn", "favorites" : [ ] }
{ "_id" : 4, "name" : "ty" }
```

The following example returns an array containing the elements of
the `favorites` array in reverse order:

```javascript
db.users.aggregate([
   {
     $project:
      {
         name: 1,
         reverseFavorites: { $reverseArray: "$favorites" }
      }
   }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "name" : "dave123", "reverseFavorites" : [ "apples", "butter", "cake", "chocolate" ] }
{ "_id" : 2, "name" : "li", "reverseFavorites" : [ "pie", "pudding", "apples" ] }
{ "_id" : 3, "name" : "ahn", "reverseFavorites" : [ ] }
{ "_id" : 4, "name" : "ty", "reverseFavorites" : null }
```
