<!-- Converted from reference/operator/query-comparison.txt (reStructuredText). Includes are inlined. -->

# Comparison Query Operators

Comparison operators return data based on value comparisons.

**Note:**

For details on a specific operator, including syntax and examples,
click on the link to the operator's reference page.

For comparison of different BSON type values, see the specified
BSON comparison order.

| Name | Description |
|---|---|
| `$eq` | Matches values that are equal to a specified value. |
| `$gt` | Matches values that are greater than a specified value. |
| `$gte` | Matches values that are greater than or equal to a specified value. |
| `$in` | Matches any of the values specified in an array. |
| `$lt` | Matches values that are less than a specified value. |
| `$lte` | Matches values that are less than or equal to a specified value. |
| `$ne` | Matches all values that are not equal to a specified value. |
| `$nin` | Matches none of the values specified in an array. |

## Compatibility

You can use comparison operators for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
