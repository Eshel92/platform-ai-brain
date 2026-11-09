<!-- Converted from reference/operator/aggregation/getField.txt (reStructuredText). Includes are inlined. -->

# $getField (expression operator)

## Definition

**`$getField`**

**New in version:** 5.0

Returns the value of a specified field from a document. If you
don't specify an object, `$getField` returns the value of
the field from `$$CURRENT`.

You can use `$getField` to retrieve the value of fields
with names that contain periods (`.`) or start with dollar signs
(`$`).

Do not rely on root-level dollar-prefixed field names that collide
with reserved internal metadata field names, as those fields may be
dropped or inaccessible in some query-processing contexts. For
restrictions and guidance on field names that contain dollar signs
(`$`) or periods (`.`), see
crud-concepts-dot-dollar-considerations.

**Tip:**

Use `$setField` to add or update fields with names
that contain dollar signs (`$`) or periods (`.`).

## Syntax

`$getField` has the following syntax:

```javascript
{ 
  $getField: {
    field: <String>,
    input: <Object> 
  }
}
```

| Field | Type | Description |
|---|---|---|
| `field` | String | Field in the `input` object for which you want to return a value. `field` can be any valid expression that resolves to a string constant. If `field` begins with a dollar sign (`$`), place the field name inside of a `$literal` expression to return its value. |
| `input` | Object | *Default*: `$$CURRENT` A valid expression that contains the `field` for which you want to return a value. `input` must resolve to an object, `missing`, `null`, or `undefined`. If omitted, defaults to the document currently being processed in the pipeline (`$$CURRENT`). |

`$getField` has the following shorthand syntax for
retrieving field values from `$$CURRENT`:

```javascript
{ 
  $getField: <String>
}
```

For this syntax, the argument is equivalent to the value of `field`
described above.

## Behavior

- If `field` resolves to anything other than a string constant,
  `$getField` returns an error.

- If the `field` that you specify is not present in the `input` 
  object, or in `$$CURRENT` if you don't specify an
  `input` object, `$getField` returns `missing`. 

- If `input` evaluates to `missing`, `undefined`, or `null`,
  `$getField` returns `null`.

- If `input` evaluates to anything other than an object, `missing`, 
  `undefined`, or `null`, `$getField` returns an error.

- `$getField` doesn't implicitly traverse objects or arrays.
  For example, `$getField` evaluates a `field` value of
  `a.b.c` as a top-level field `a.b.c` instead of a nested field 
  `{ a: { b: { c: } } }`.

 

## Examples

### Query Fields that Contain Periods (`.`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "sweatshirt", "price.usd": 45.99, qty: 300 },
   { _id: 2, item: "winter coat", "price.usd": 499.99, qty: 200 },
   { _id: 3, item: "sun dress", "price.usd": 199.99, qty: 250 },
   { _id: 4, item: "leather boots", "price.usd": 249.99, qty: 300 },
   { _id: 5, item: "bow tie", "price.usd": 9.99, qty: 180 }
] )
```

The following operation uses the `$getField` and
`$gt` operators to find which products have a `price.usd`
greater than `200`:

```javascript
db.inventory.aggregate( [
  {
    $match: 
      { $expr: 
        { $gt: [ { $getField: "price.usd" }, 200 ] }
      }
   }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 2, item: 'winter coat', qty: 200, 'price.usd': 499.99 },
  { _id: 4, item: 'leather boots', qty: 300, 'price.usd': 249.99 }
]
```

### Query Fields that Start with a Dollar Sign (`$`)

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "sweatshirt", "$price": 45.99, qty: 300 },
   { _id: 2, item: "winter coat", "$price": 499.99, qty: 200 },
   { _id: 3, item: "sun dress", "$price": 199.99, qty: 250 },
   { _id: 4, item: "leather boots", "$price": 249.99, qty: 300 },
   { _id: 5, item: "bow tie", "$price": 9.99, qty: 180 }
] )
```

The following operation uses the `$getField`,
`$gt`, and `$literal` operators to find which 
products have a `$price` greater than `200`:

```javascript
db.inventory.aggregate( [
  {
    $match: 
      { $expr: 
        { $gt: [ { $getField: {$literal: "$price" } }, 200 ] }
      }
   }
] )
```

The operation returns the following results:

```javascript
[
  { _id: 2, item: 'winter coat', qty: 200, '$price': 499.99 },
  { _id: 4, item: 'leather boots', qty: 300, '$price': 249.99 }
]
```

### Query a Field in a Sub-document

Create an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "sweatshirt",  "price.usd": 45.99,
     quantity: { "$large": 50, "$medium": 50, "$small": 25 }
   }, 
   { _id: 2, item: "winter coat", "price.usd": 499.99,
     quantity: { "$large": 35, "$medium": 35, "$small": 35 }
   },
   { _id: 3, item: "sun dress", "price.usd": 199.99,
     quantity: { "$large": 45, "$medium": 40, "$small": 5 }
   },
   { _id: 4, item: "leather boots", "price.usd": 249.99,
     quantity: { "$large": 20, "$medium": 30, "$small": 40 }
   },
   { _id: 5, item: "bow tie", "price.usd": 9.99,
     quantity: { "$large": 0, "$medium": 10, "$small": 75 }
   }
] )
```

The following operation returns documents where the number of
`$small` items is less than or equal to `20`.

```javascript
db.inventory.aggregate( [
   { $match: 
      { $expr:
         { $lte:
            [
               { $getField: 
                  { field: { $literal: "$small" },
                    input: "$quantity"
                  }
               },
               20
            ]
         }
      }
   }
] )
```

Use these operators to query the collection:

- The `$lte` operator finds values less than or equal to
  20.
- `$getField` requires explicit `field` and `input`
  parameters because the `$small` field is part of a
  sub-document.
- `$getField` uses `$literal` to evaluate
  "`$small`", because the field name has a dollar sign (`$`) in it.

Example output:

```javascript
[
  {
    _id: 3,
    item: 'sun dress',
    'price.usd': 199.99,
    quantity: { '$large': 45, '$medium': 40, '$small': 5 }
  }
]
```
