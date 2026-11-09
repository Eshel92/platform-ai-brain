<!-- Converted from reference/mql/update.txt (reStructuredText). Includes are inlined. -->

# Update Operators

The following operators are available for use in update operations such
as `db.collection.updateMany()` and
`db.collection.findAndModify()`.

## Syntax

Specify update operators in the following form:

```javascript
{
   <operator1>: { <field1>: <value1>, ... },
   <operator2>: { <field2>: <value2>, ... },
   ...
}
```

## Behavior

Update operators process document fields with string-based names in
lexicographic order. Fields with numeric names are processed in numeric
order.

Consider this example `$set` command:

```javascript
{ $set: { "a.2": <new value>, "a.10": <new value>, } }
```

`"a.2"` is processed before `"a.10"` because `2` comes before
`10` in numeric order.

## Array Update Modifiers

The following modifiers change how the `$push` and
`$addToSet` operators update arrays:

| Name | Description |
|---|---|
| `$each` | Modifies the `$push` and `$addToSet` operators to append multiple items for array updates. |
| `$position` | Modifies the `$push` operator to specify the position in the array to add elements. |
| `$slice` | Modifies the `$push` operator to limit the size of updated arrays. |
| `$sort` | Modifies the `$push` operator to reorder documents stored in an array. |

## Array Update Operators

The following operators modify the contents of an array:

| Name | Description |
|---|---|
| `$addToSet` | Adds elements to an array only if they do not already exist in the set. |
| `$pop` | Removes the first or last item of an array. |
| `$pull` | Removes all array elements that match a specified query. |
| `$pullAll` | Removes all matching values from an array. |
| `$push` | Adds an item to an array. |

## Bitwise Update Operators

The following operator performs a bitwise update of an integer value:

| Name | Description |
|---|---|
| `$bit` | Performs bitwise `AND`, `OR`, and `XOR` updates of integer values. |

## Field Update Operators

The following operators modify fields in a document:

| Name | Description |
|---|---|
| `$currentDate` | Sets the value of a field to current date, either as a Date or a Timestamp. |
| `$inc` | Increments the value of the field by the specified amount. |
| `$min` | Only updates the field if the specified value is less than the existing field value. |
| `$max` | Only updates the field if the specified value is greater than the existing field value. |
| `$mul` | Multiplies the value of the field by the specified amount. |
| `$rename` | Renames a field. |
| `$set` | Sets the value of a field in a document. |
| `$setOnInsert` | Sets the value of a field if an update results in an insert of a document. Has no effect on update operations that modify existing documents. |
| `$unset` | Removes the specified field from a document. |

## Positional Update Operators

The following operators act as placeholders to identify which array
elements to update:

| Name | Description |
|---|---|
| `$` | Acts as a placeholder to update the first element that matches the query condition. |
| `$[]` | Acts as a placeholder to update all elements in an array for the documents that match the query condition. |
| `$[<identifier>]` | Acts as a placeholder to update all elements that match the `arrayFilters` condition for the documents that match the query condition. |

## Updates with Aggregation Pipeline

To create expressive update statements, such as conditional updates
based on current field values or single-field updates that use the value
of another field, you can perform updates with an aggregation pipeline.

For syntax and examples, see updates-agg-pipeline.
