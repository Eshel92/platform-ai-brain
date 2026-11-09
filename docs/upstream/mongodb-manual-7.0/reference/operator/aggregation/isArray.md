<!-- Converted from reference/operator/aggregation/isArray.txt (reStructuredText). Includes are inlined. -->

# $isArray (expression operator)

## Definition

**`$isArray`**

Determines if the operand is an array. Returns a boolean.

`$isArray` has the following syntax:

```javascript
{ $isArray: [ <expression> ] }
```

## Behavior

The `<expression>` can be any valid expression. For more information on expressions, see
aggregation-expressions.

| Example | Results | Notes |
|---|---|---|
| `{ $isArray: "hello" }` | `false` | `"hello"` is a string, passed as a string. |
| `{ $isArray: [ "hello" ] }` | `false` | `"hello"` is a string, passed as part of an argument array. |
| `{ $isArray: [ [ "hello" ] ] }` | `true` | `[ "hello" ]` is an array, passed as part of an argument array. |

**Note:**

Aggregation expressions accept a variable number of arguments. These
arguments are normally passed as an array. However, when the argument
is a single value, you can simplify your code by passing the argument
directly without wrapping it in an array. 

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

Check if the `instock` and the `ordered` fields are arrays. If both
fields are arrays, concatenate them:

```javascript
db.warehouses.aggregate( [
   { $project:
      { items: 
          { $cond:
            {
              if: { $and: [ { $isArray: "$instock" },
                            { $isArray: "$ordered" } 
                          ] },
              then: { $concatArrays: [ "$instock", "$ordered" ] },
              else: "One or more fields is not an array."
            }
          }
      }
   }
] )
```

```javascript
{ _id : 1, items : [ "chocolate", "butter", "apples" ] }
{ _id : 2, items : "One or more fields is not an array." }
{ _id : 3, items : [ "pears", "pecans", "cherries" ] }
{ _id : 4, items : [ "ice cream" ] }
```

**See also:**

- `$cond`
- `$concatArrays`
