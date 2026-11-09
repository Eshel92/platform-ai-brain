<!-- Converted from reference/operator/update-field.txt (reStructuredText). Includes are inlined. -->

# Field Update Operators

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

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
