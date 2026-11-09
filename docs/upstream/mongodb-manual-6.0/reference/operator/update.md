<!-- Converted from reference/operator/update.txt (reStructuredText). Includes are inlined. -->

# Update Operators

The following modifiers are available for use in update operations,
for example, in `db.collection.updateMany()` and
`db.collection.findAndModify()`.

## Compatibility

You can use update operators for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

Specify the operator expression in a document of the form:

```javascript
{
   <operator1>: { <field1>: <value1>, ... },
   <operator2>: { <field2>: <value2>, ... },
   ...
}
```

**Note:**

For details on a specific operator, including syntax and examples,
click on the link to the operator's reference page.

## Update Operators

### Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. 

Consider this example `$set` command:

```javascript
{ $set: { "a.2": <new value>, "a.10": <new value>, } }
```

In MongoDB 5.0 and later, `"a.2"` is processed before `"a.10"` 
because `2` comes before `10` in numeric order. 

### Fields

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

### Array

#### Operators

| Name | Description |
|---|---|
| `$` | Acts as a placeholder to update the first element that matches the query condition. |
| `$[]` | Acts as a placeholder to update all elements in an array for the documents that match the query condition. |
| `$[<identifier>]` | Acts as a placeholder to update all elements that match the `arrayFilters` condition for the documents that match the query condition. |
| `$addToSet` | Adds elements to an array only if they do not already exist in the set. |
| `$pop` | Removes the first or last item of an array. |
| `$pull` | Removes all array elements that match a specified query. |
| `$push` | Adds an item to an array. |
| `$pullAll` | Removes all matching values from an array. |

#### Modifiers

| Name | Description |
|---|---|
| `$each` | Modifies the `$push` and `$addToSet` operators to append multiple items for array updates. |
| `$position` | Modifies the `$push` operator to specify the position in the array to add elements. |
| `$slice` | Modifies the `$push` operator to limit the size of updated arrays. |
| `$sort` | Modifies the `$push` operator to reorder documents stored in an array. |

### Bitwise

| Name | Description |
|---|---|
| `$bit` | Performs bitwise `AND`, `OR`, and `XOR` updates of integer values. |
