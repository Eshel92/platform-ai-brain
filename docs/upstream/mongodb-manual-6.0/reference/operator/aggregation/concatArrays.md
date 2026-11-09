<!-- Converted from reference/operator/aggregation/concatArrays.txt (reStructuredText). Includes are inlined. -->

# $concatArrays (aggregation)

## Definition

**`$concatArrays`**

Concatenates arrays to return the concatenated array.

`$concatArrays` has the following syntax:

```javascript
{ $concatArrays: [ <array1>, <array2>, ... ] }
```

The `<array>` expressions can be any valid expression as long as they resolve to an array. For
more information on expressions, see aggregation-expressions.

If any argument resolves to a value of `null` or refers to a field
that is missing, `$concatArrays` returns `null`.

## Behavior

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { $concatArrays: [ [ "hello", " "], [ "world" ] ] } | .. code-block:: javascript :copyable: false [ "hello", " ", "world" ] |
| .. code-block:: javascript :copyable: false { $concatArrays: [ [ "hello", " "], [ [ "world" ], "again"] ] } | .. code-block:: javascript :copyable: false [ "hello", " ", [ "world" ], "again" ] |

## Example

Create a collection named `warehouses` with the following documents:

```javascript
db.warehouses.insertMany( [
   { _id : 1, instock: [ "chocolate" ], ordered: [ "butter", "apples" ] },
   { _id : 2, instock: [ "apples", "pudding", "pie" ] },
   { _id : 3, instock: [ "pears", "pecans" ], ordered: [ "cherries" ] },
   { _id : 4, instock: [ "ice cream" ], ordered: [ ] }
] )
```

The following example concatenates the `instock` and the `ordered`
arrays:

```javascript
db.warehouses.aggregate( [
   { $project: { items: { $concatArrays: [ "$instock", "$ordered" ] } } }
] )
```

```javascript
{ _id : 1, items : [ "chocolate", "butter", "apples" ] }
{ _id : 2, items : null }
{ _id : 3, items : [ "pears", "pecans", "cherries" ] }
{ _id : 4, items : [ "ice cream" ] }
```

**See also:**

`$push`
