<!-- Converted from reference/mql/query-predicates/comparison.txt (reStructuredText). Includes are inlined. -->

# Comparison Query Predicate Operators

Comparison operators filter data with value comparisons such as less
than and greater than.

Inequality comparison operators (`$gt`, `$gte`,
`$lt`, and `$lte`) use type bracketing, which means a comparison on a given BSON type
matches only values of that type. Negations (`$ne` and
`$nin`) don't use type bracketing, so they match values of any
type.

Unlike the query predicates, the inequality comparison expressions (`$gt`,
`$gte`, `$lt`, and `$lte`) don't
use type bracketing. Instead, they compare values of different BSON
types using the specified BSON comparison order.

| Operator | Description |
|---|---|
| `$eq` | Matches values equal to a specified value. |
| `$gt` | Matches values greater than a specified value. |
| `$gte` | Matches values greater than or equal to a specified value. |
| `$in` | Matches any values specified in an array. |
| `$lt` | Matches values less than a specified value. |
| `$lte` | Matches values less than or equal to a specified value. |
| `$ne` | Matches all values not equal to a specified value. |
| `$nin` | .. include:: /includes/query-predicates/nin-desc.rst |
