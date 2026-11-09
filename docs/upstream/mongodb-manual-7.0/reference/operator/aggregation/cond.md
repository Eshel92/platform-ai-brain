<!-- Converted from reference/operator/aggregation/cond.txt (reStructuredText). Includes are inlined. -->

# $cond (expression operator)

## Definition

**`$cond`**

Evaluates a boolean expression to return one of the two specified
return expressions.

## Compatibility

You can use `$cond` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$cond` expression has one of two syntaxes:

```javascript
{ $cond: { if: <boolean-expression>, then: <true-case>, else: <false-case> } }
```

Or:

```javascript
{ $cond: [ <boolean-expression>, <true-case>, <false-case> ] }
```

`$cond` requires all three arguments (`if-then-else`)
for either syntax.

If the `<boolean-expression>` evaluates to `true`, then
`$cond` evaluates and returns the value of the
`<true-case>` expression. Otherwise, `$cond` evaluates
and returns the value of the `<false-case>` expression.

The arguments can be any valid expression.

**See also:**

`$switch`

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following aggregation operation uses the `$cond` expression to
assign a rental price to each movie. The operation prices movies with an
`imdb.rating` greater than or equal to `9` at `5.99`. The operation prices
all other movies at `3.99`:

```javascript
```

Output:

```javascript
```

The following operation uses the array syntax of the
`$cond` expression and returns the same results:

```javascript
db.movies.aggregate( [
   { $match: { runtime: { $gt: 1000 } } },
   {
      $project:
        {
          title: 1,
          rentalPrice:
            {
              $cond: [
                 { $gte: [ "$imdb.rating", 9 ] },
                 5.99,
                 3.99
              ]
            }
        }
   }
] )
```
