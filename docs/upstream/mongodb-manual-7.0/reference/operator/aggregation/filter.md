<!-- Converted from reference/operator/aggregation/filter.txt (reStructuredText). Includes are inlined. -->

# $filter (expression operator)

## Definition

**`$filter`**

Selects a subset of an array to return based on the specified
condition. Returns an array with only those elements that match the
condition. The returned elements are in the original order.

## Compatibility

You can use `$filter` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`$filter` has the following syntax:

```javascript
{ 
    $filter: 
      { 
         input: <array>, 
         as: <string>,  
         cond: <expression>,
         limit: <number expression> 
      } 
}
```

| Field | Specification |
|---|---|
| `input` | An expression that resolves to an array. If `input` resolves to `null` or refers to a missing field, `$filter` returns `null`. If `input` resolves to a non-array, non-null value, the pipeline errors. |
| `as` | Optional. A name for the variable that represents each individual element of the `input` array. If no name is specified, the variable name defaults to `this`. |
| `cond` | An expression that resolves to a boolean value used to determine if an element should be included in the output array. The expression references each element of the `input` array individually with the variable name specified in `as`. |
| `limit` | Optional. A number expression that restricts the number of matching array elements that `$filter` returns. You cannot specify a limit less than `1`. The matching array elements are returned in the order they appear in the input array. If the specified `limit` is greater than the number of matching array elements, `$filter` returns all matching array elements. If the limit is `null`, `$filter` returns all matching array elements. |

For more information on expressions, see
aggregation-expressions.

## Behavior

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { $filter: { input: [ 1, "a", 2, null, 3.1, Long(4), "5" ], as: "num", cond: { $isNumber: "$$num" } } } | `[ 1, 2, 3.1, Long(4) ]` |
| .. code-block:: javascript :copyable: false :emphasize-lines: 6 { $filter: { input: [ 1, "a", 2, null, 3.1, Long(4), "5" ], as: "num", cond: { $isNumber: "$$num" }, limit: 2 } } | `[ 1, 2 ]` |
| .. code-block:: javascript :copyable: false :emphasize-lines: 6 { $filter: { input: [ 1, "a", 2, null, 3.1, Long(4), "5" ], as: "num", cond: { $isNumber: "$$num" }, limit: { $add: [ 0, 1 ] } } } | `[ 1 ]` |

## Examples

The following examples use a `sales` collection with these documents:

```javascript
db.sales.insertMany( [
   {
      _id: 0,
      items: [
         { item_id: 43, quantity: 2, price: 10, name: "pen" },
         { item_id: 2, quantity: 1, price: 240, name: "briefcase" }
      ]
   },
   {
      _id: 1,
      items: [
         { item_id: 23, quantity: 3, price: 110, name: "notebook" },
         { item_id: 103, quantity: 4, price: 5, name: "pen" },
         { item_id: 38, quantity: 1, price: 300, name: "printer" }
      ]
   },
   {
      _id: 2,
      items: [
         { item_id: 4, quantity: 1, price: 23, name: "paper" }
      ]
   }
] )
```

### Filter Based on Number Comparison

The following example filters the `items` array to only include
documents that have a `price` greater than or equal to `100`:

```javascript
db.sales.aggregate( [
   {
      $project: {
         items: {
            $filter: {
               input: "$items", 
               as: "item", 
               cond: { $gte: [ "$$item.price", 100 ] } 
            }
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: 0,
      items: [ { item_id: 2, quantity: 1, price: 240, name: 'briefcase' } ]
   },
   {
      _id: 1,
      items: [
         { item_id: 23, quantity: 3, price: 110, name: 'notebook' },
         { item_id: 38, quantity: 1, price: 300, name: 'printer' }
      ]
   },
   { _id: 2, items: [] }
]
```

### Use the limit Field

The example uses the `limit` field to specify the number of matching
elements returned in each `items` array. 

```javascript
db.sales.aggregate( [
   {
      $project: {
         items: {
            $filter: {
               input: "$items",
               as: "item", 
               cond: { $gte: [ "$$item.price", 100 ] }, 
               limit: 1 
            }
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: 0,
      items: [ { item_id: 2, quantity: 1, price: 240, name: 'briefcase' } ]
   },
   {
      _id: 1,
      items: [ { item_id: 23, quantity: 3, price: 110, name: 'notebook' } ]
   },
   { _id: 2, items: [] }
]
```

### limit Greater than Possible Matches

The example uses a `limit` field value that is larger than the
possible number of matching elements that can be returned. In this case,
`limit` does not affect the query results and returns all documents
matching the `$gte` filter criteria.

```javascript
db.sales.aggregate( [
   {
      $project: {
         items: {
            $filter: {
               input: "$items",
               as: "item", 
               cond: { $gte: [ "$$item.price", 100] },
               limit: 5
            }
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: 0,
      items: [ { item_id: 2, quantity: 1, price: 240, name: 'briefcase' } ]
   },
   {
      _id: 1,
      items: [
         { item_id: 23, quantity: 3, price: 110, name: 'notebook' },
         { item_id: 38, quantity: 1, price: 300, name: 'printer' }
      ]
   },
   { _id: 2, items: [] }
]
```

### Filter Based on String Equality Match

The following aggregation filters for `items` that have a `name`
value of `pen`.

```javascript
db.sales.aggregate( [
   {
      $project: {
         items: {
            $filter: {
               input: "$items",
               as: "item",
               cond: { $eq: [ "$$item.name", "pen"] }
            }
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: 0,
      items: [ { item_id: 43, quantity: 2, price: 10, name: 'pen' } ]
   },
   {
      _id: 1,
      items: [ { item_id: 103, quantity: 4, price: 5, name: 'pen' } ]
   },
   { _id: 2, items: [] }
]
```

### Filter Based on Regular Expression Match

The following aggregation uses `$regexMatch` to filter for
`items` that have a `name` value that starts with `p`:

```javascript
db.sales.aggregate( [
   {
      $project: {
         items: {
            $filter: {
               input: "$items",
               as: "item",
               cond: {
                  $regexMatch: { input: "$$item.name", regex: /^p/ }
               } 
            }
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: 0,
      items: [ { item_id: 43, quantity: 2, price: 10, name: 'pen' } ]
   },
   {
      _id: 1,
      items: [
         { item_id: 103, quantity: 4, price: 5, name: 'pen' },
         { item_id: 38, quantity: 1, price: 300, name: 'printer' }
      ]
   },
   {
      _id: 2,
      items: [ { item_id: 4, quantity: 1, price: 23, name: 'paper' } ]
   }
]
```
