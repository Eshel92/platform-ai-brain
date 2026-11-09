<!-- Converted from reference/operator/query/not.txt (reStructuredText). Includes are inlined. -->

# $not (query predicate operator)

## Definition

**`$not`**

`$not` performs a logical `NOT` operation on the
specified `<operator-expression>` and selects the documents that
do *not* match the `<operator-expression>`. This includes
documents that do not contain the `field`.

## Compatibility

You can use `$not` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$not` operator has the following form:

```javascript
{ field: { $not: { <operator-expression> } } }
```

Consider the following example:

```javascript
db.movies.find( { runtime: { $not: { $gt: 180 } } } )
```

The example selects all documents in the `movies` collection where:

- the `runtime` field value is less than or equal to `180` **or**
- the `runtime` field does not exist

`{ $not: { $gt: 180 } }` differs from the `$lte`
operator. `{ $lte: 180 }` returns *only* the documents where the
`runtime` field exists and its value is less than or equal to
`180`.

You must use the `$not` operator with another operator expression. For
example, to use `$not` to perform an inequality check, use this
syntax:

```javascript
{ runtime: { $not: { $eq: 120 } } }
```

The preceding query is equivalent to:

```javascript
{ runtime: { $ne: 120 } }
```

The following query is invalid because it compares a field without an
operator:

```javascript
{ runtime: { $not: 120 } }
```

## Behavior

### Arrays

When passed an array argument, the `$not` operator may yield
unexpected results. To match documents based on multiple false
conditions, use `$nor`.

### Regular Expressions

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

`$not` operator can perform logical `NOT` operation on:

- Regular expression objects (i.e. `/pattern/`)

  The following example returns movies where `runtime` is greater
  than `1000` minutes and `title` does not start with the letter
  `T`. Because `$not` also matches documents that don't contain
  the `title` field, the query returns movies even when title data
  is unavailable:

  ```javascript
  ```

  Output:

  ```javascript
  ```

- `$regex` operator expression 

  The following two queries return movies where `runtime` is
  greater than `1000` minutes and `title` does not start with
  the letter `T`. The first query passes a string to `$regex`:

  ```javascript
  ```

  Output:

  ```javascript
  ```

  The second query passes a regex literal to `$regex`:

  ```javascript
  ```

  Output:

  ```javascript
  ```

- driver language's regular expression objects

  For example, the following [PyMongo](https://pymongo.readthedocs.io/en/stable/index.html) query uses
  Python's `re.compile()` method to compile a regular expression:

  ```python
  import re
  for noMatch in db.inventory.find( { "item": { "$not": re.compile("^p.*") } } ):
      print noMatch
  ```

**See also:**

- `find()`
- `$set`
- `$gt`
- `$regex`
