<!-- Converted from reference/operator/query/nor.txt (reStructuredText). Includes are inlined. -->

# $nor

## Definition

**`$nor`**

`$nor` performs a logical `NOR` operation on an array
of one or more query expression and selects the documents that **fail**
all the query expressions in the array. The `$nor` has
the following syntax:

```javascript
{ $nor: [ { <expression1> }, { <expression2> }, ...  { <expressionN> } ] }
```

## Examples

### `$nor` Query with Two Expressions

Consider the following query which uses only the `$nor` operator:

```javascript
db.inventory.find( { $nor: [ { price: 1.99 }, { sale: true } ]  } )
```

This query will return all documents that:

- contain the `price` field whose value is *not* equal to `1.99`
  and contain the `sale` field whose value *is not* equal to
  `true` **or**

- contain the `price` field whose value is *not* equal to `1.99`
  *but* do *not* contain the `sale` field **or**

- do *not* contain the `price` field *but* contain the `sale`
  field whose value *is not* equal to `true` **or**
- do *not* contain the `price` field *and* do *not* contain the
  `sale` field

### `$nor` and Additional Comparisons

Consider the following query:

```javascript
db.inventory.find( { $nor: [ { price: 1.99 }, { qty: { $lt: 20 } }, { sale: true } ] } )
```

This query will select all documents in the `inventory` collection
where:

- the `price` field value does *not* equal `1.99` **and**
- the `qty` field value is *not* less than `20` **and**
- the `sale` field value is *not* equal to `true`

including those documents that do not contain these field(s).

The exception in returning documents that do not contain the field
in the `$nor` expression is when the `$nor` operator is
used with the `$exists` operator.

### `$nor` and `$exists`

Compare that with the following query which uses the
`$nor` operator with the `$exists` operator:

```javascript
db.inventory.find( { $nor: [ { price: 1.99 }, { price: { $exists: false } },
                             { sale: true }, { sale: { $exists: false } } ] } )
```

This query will return all documents that:

- contain the `price` field whose value is *not* equal to `1.99`
  and contain the `sale` field whose value *is not* equal to
  `true`

**See also:**

- `find()`
- `$or`
- `$set`
- `$exists`
