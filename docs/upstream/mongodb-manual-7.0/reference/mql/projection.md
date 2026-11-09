<!-- Converted from reference/mql/projection.txt (reStructuredText). Includes are inlined. -->

# Find Command Projection Operators

The following linked pages describe specialized operators available only
in find command projections. You can also use non-specialized
expressions in find command projections.

| Name | Description |
|---|---|
| `$` | Projects the first array element that matches the query condition. |
| `$elemMatch` | Projects the first array element that matches the specified `$elemMatch` condition. |
| `$meta` | Projects the available per-document metadata. |
| `$slice` | Limits the number of elements projected from an array. Supports skip and limit slices. |

     

**Note:** View Support

`find()` operations on views do not support
any of the preceding projection operators.
