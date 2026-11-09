<!-- Converted from reference/operator/aggregation/anyElementTrue.txt (reStructuredText). Includes are inlined. -->

# $anyElementTrue (expression operator)

## Definition

**`$anyElementTrue`**

Evaluates an array as a set and returns `true` if any of the
elements are `true` and `false` otherwise. An empty array
returns `false`.

`$anyElementTrue` has the following syntax:

```javascript
{ $anyElementTrue: [ <expression> ] }
```

The `<expression>` itself must resolve to an array, separate from
the outer array that denotes the argument list. For more information
on expressions, see aggregation-expressions.

## Behavior

If a set contains a nested array element, `$anyElementTrue` does *not* descend
into the nested array but evaluates the array at top-level.

In addition to the `false` boolean value, `$anyElementTrue` evaluates
as `false` the following: `null`, `0`, and `undefined`
values. The `$anyElementTrue` evaluates all other values as `true`,
including non-zero numeric values and arrays.

| Example | Result |
|---|---|
| `{ $anyElementTrue: [ [ true, false ] ] }` | `true` |
| `{ $anyElementTrue: [ [ [ false ] ] ] }` | `true` |
| `{ $anyElementTrue: [ [ null, false, 0 ] ] }` | `false` |
| `{ $anyElementTrue: [ [ ] ] }` | `false` |

## Example

Create an example collection named `survey` with the following
documents:

```javascript
db.survey.insertMany( [
   { _id: 1, responses: [ true ] },
   { _id: 2, responses: [ true, false ] },
   { _id: 3, responses: [ ] },
   { _id: 4, responses: [ 1, true, "seven" ] },
   { _id: 5, responses: [ 0 ] },
   { _id: 6, responses: [ [ ] ] },
   { _id: 7, responses: [ [ 0 ] ] },
   { _id: 8, responses: [ [ false ] ] },
   { _id: 9, responses: [ null ] },
   { _id: 10, responses: [ undefined ] }
] )
```

The following operation uses the `$anyElementTrue` operator
to determine if the `responses` array contains any value that
evaluates to `true`:

```javascript
db.survey.aggregate(
   [
     { $project: { responses: 1, isAnyTrue: { $anyElementTrue: [ "$responses" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "responses" : [ true ], "isAnyTrue" : true }
{ "responses" : [ true, false ], "isAnyTrue" : true }
{ "responses" : [ ], "isAnyTrue" : false }
{ "responses" : [ 1, true, "seven" ], "isAnyTrue" : true }
{ "responses" : [ 0 ], "isAnyTrue" : false }
{ "responses" : [ [ ] ], "isAnyTrue" : true }
{ "responses" : [ [ 0 ] ], "isAnyTrue" : true }
{ "responses" : [ [ false ] ], "isAnyTrue" : true }
{ "responses" : [ null ], "isAnyTrue" : false }
{ "responses" : [ undefined ], "isAnyTrue" : false }
```
