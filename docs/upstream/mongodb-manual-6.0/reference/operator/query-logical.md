<!-- Converted from reference/operator/query-logical.txt (reStructuredText). Includes are inlined. -->

# Logical Query Operators

Logical operators return data based on expressions that evaluate to 
true or false.

## Compatibility

You can use logical query operators for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Operators

**Note:**

For details on a specific operator, including syntax and examples,
click on the link to the operator's reference page.

| Name | Description |
|---|---|
| `$and` | Joins query clauses with a logical `AND` returns all documents that match the conditions of both clauses. |
| `$not` | Inverts the effect of a query expression and returns documents that do *not* match the query expression. |
| `$nor` | Joins query clauses with a logical `NOR` returns all documents that fail to match both clauses. |
| `$or` | Joins query clauses with a logical `OR` returns all documents that match the conditions of either clause. |
