<!-- Converted from reference/operator/aggregation/split.txt (reStructuredText). Includes are inlined. -->

# $split  (expression operator)

## Definition

**`$split`**

Divides a string into an array of substrings based on a delimiter.
`$split` removes the delimiter and returns the resulting substrings
as elements of an array. If the delimiter is not found in the string,
`$split` returns the original string as the only element of an array.

`$split` has the following operator expression syntax:

```javascript
{ $split: [ <string expression>, <delimiter> ] }
```

| Field | Type | Description |
|---|---|---|
| `string expression` | string | The string to be split. `string expression` can be any valid expression as long as it resolves to a string. For more information on expressions, see aggregation-expressions. |
| `delimiter` | string | The delimiter to use when splitting the string expression. `delimiter` can be any valid expression as long as it resolves to a string. |

          
          
   

## Behavior

The `$split` operator returns an array.
The `<string expression>` and `<delimiter>` inputs must both be
strings. Otherwise, the operation fails with an error.

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { $split: [ "June-15-2013", "-" ] } | .. code-block:: javascript :copyable: false [ "June", "15", "2013" ] |
| .. code-block:: javascript :copyable: false { $split: [ "banana split", "a" ] } | .. code-block:: javascript :copyable: false [ "b", "n", "n", " split" ] |
| .. code-block:: javascript :copyable: false { $split: [ "Hello World", " " ] } | .. code-block:: javascript :copyable: false [ "Hello", "World" ] |
| .. code-block:: javascript :copyable: false { $split: [ "astronomical", "astro" ] } | .. code-block:: javascript :copyable: false [ "", "nomical" ] |
| .. code-block:: javascript :copyable: false { $split: [ "pea green boat", "owl" ] } | .. code-block:: javascript :copyable: false [ "pea green boat" ] |
| `{ $split: [ "headphone jack", 7 ] }` | Errors with message: `"$split requires an expression that evaluates to a string as a second argument, found: double"` |
| `{ $split: [ "headphone jack", /jack/ ] }` | Errors with message: `"$split requires an expression that evaluates to a string as a second argument, found: regex"` |

## Example

A collection named `deliveries` contains the following documents:

```javascript
db.deliveries.insertMany( [
   { _id: 1, city: "Berkeley, CA", qty: 648 },
   { _id: 2, city: "Bend, OR", qty: 491 },
   { _id: 3, city: "Kensington, CA", qty: 233 },
   { _id: 4, city: "Eugene, OR", qty: 842 },
   { _id: 5, city: "Reno, NV", qty: 655 },
   { _id: 6, city: "Portland, OR", qty: 408 },
   { _id: 7, city: "Sacramento, CA", qty: 574 }
] )
```

The goal of following aggregation operation is to find the total
quantity of deliveries for each state and sort the list in
descending order. It has five pipeline stages:

- The `$project` stage produces documents with two fields,
  `qty` (integer) and `city_state` (array). The `$split`
  operator creates an array of strings by splitting the `city`
  field, using a comma followed by a space (`", "`) as a delimiter.

- The `$unwind` stage creates a separate record for each
  element in the `city_state` field.

- The `$match` stage uses a regular expression to filter out
  the city documents, leaving only those containing a state.

- The `$group` stage groups all the states together and sums the
  `qty` field.

- The `$sort` stage sorts the results by `total_qty` in
  descending order.

```javascript
db.deliveries.aggregate( [
  { $project: { city_state: { $split: ["$city", ", "] }, qty: 1 } },
  { $unwind: "$city_state" },
  { $match: { city_state: /[A-Z]{2}/ } },
  { $group: { _id: { state: "$city_state" }, total_qty: { $sum: "$qty" } } },
  { $sort: { total_qty: -1 } }
] )
```

The operation returns the following results:

```javascript
[
   { _id: { state: "OR" }, total_qty: 1741 },
   { _id: { state: "CA" }, total_qty: 1455 },
   { _id: { state: "NV" }, total_qty: 655 }
]
```
