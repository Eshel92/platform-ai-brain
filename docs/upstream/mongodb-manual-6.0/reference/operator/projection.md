<!-- Converted from reference/operator/projection.txt (reStructuredText). Includes are inlined. -->

# Projection Operators

Projection operators specify the fields returned by an operation. 

**Note:**

`find()` operations on views do not support
the following projection
operators:

- `$`
- `$elemMatch`
- `$slice`
- `$meta`

**Note:**

For details on a specific operator, including syntax and examples,
click on the link to the operator's reference page.

| Name | Description |
|---|---|
| `$` | Projects the first element in an array that matches the query condition. |
| `$elemMatch` | Projects the first element in an array that matches the specified `$elemMatch` condition. |
| `$meta` | Projects the available per-document metadata. |
| `$slice` | Limits the number of elements projected from an array. Supports skip and limit slices. |
