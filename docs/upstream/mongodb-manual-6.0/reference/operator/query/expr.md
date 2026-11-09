<!-- Converted from reference/operator/query/expr.txt (reStructuredText). Includes are inlined. -->

# $expr

## Definition

**Changed in version:** 5.0

**`$expr`**

Allows the use of aggregation expressions within the query language.

## Compatibility

You can use `$expr` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`$expr` has the following syntax:

```javascript
{ $expr: { <expression> } }
```

The arguments can be any valid aggregation expression. For more information, see
aggregation-expressions.

## Behavior

`$expr` can build query expressions that compare fields from the
same document in a `$match` stage.

If the `$match` stage is part of a `$lookup` stage,
`$expr` can compare fields using `let` variables. See
lookup-multiple-joins for an example. 

The `$eq`, `$lt`, `$lte`,
`$gt`, and `$gte` comparison operators placed in
an `$expr` operator can use an index on the `from` collection
referenced in a `$lookup` stage. Limitations:

- Indexes can only be used for comparisons between fields and constants, so the
  `let` operand must resolve to a constant.

  For example, a comparison between `$a` and a constant 
  value can use an index, but a comparison between `$a` and `$b` 
  cannot.

- Indexes are not used for comparisons where the `let` operand resolves to an
  empty or missing value.

- Multikey indexes are not used.

## Examples

### Compare Two Fields from A Single Document

Consider a `monthlyBudget` collection with the following documents:

```javascript
db.monthlyBudget.insertMany( [
   { _id : 1, category : "food", budget : 400, spent : 450 },
   { _id : 2, category : "drinks", budget : 100, spent : 150 },
   { _id : 3, category : "clothes", budget : 100, spent : 50 },
   { _id : 4, category : "misc", budget : 500, spent : 300 },
   { _id : 5, category : "travel", budget : 200, spent : 650 }
] )
```

The following operation uses `$expr` to find documents 
where the `spent` amount exceeds the `budget`:

```javascript
db.monthlyBudget.find( { $expr: { $gt: [ $spent , $budget ] } } )
```

The operation returns the following results:

```javascript
{ _id : 1, category : "food", budget : 400, spent : 450 }
{ _id : 2, category : "drinks", budget : 100, spent : 150 }
{ _id : 5, category : "travel", budget : 200, spent : 650 }
```

### Using `$expr` With Conditional Statements

Some queries require the ability to execute conditional logic when 
defining a query filter. The aggregation pipeline provides the
`$cond` operator to express conditional statements. By using
`$expr` with the `$cond` operator, you can
specify a conditional filter for your query statement.

Create a sample `supplies` collection with the following documents:

```javascript
db.supplies.insertMany( [
   { _id : 1, item : "binder", qty : NumberInt("100"), price : NumberDecimal("12") },
   { _id : 2, item : "notebook", qty : NumberInt("200"), price : NumberDecimal("8") },
   { _id : 3, item : "pencil", qty : NumberInt("50"), price : NumberDecimal("6") },
   { _id : 4, item : "eraser", qty : NumberInt("150"), price : NumberDecimal("3") },
   { _id : 5, item : "legal pad", qty : NumberInt("42"), price : NumberDecimal("10") }
] )
```

Assume that for an upcoming sale next month, you want to discount the
prices such that:

- If `qty` is greater than or equal to 100, the discounted price will
  be 0.5 of the `price`.

- If `qty` is less than 100, the discounted price is 0.75 of the
  `price`.

Before applying the discounts, you would like to know which items in the
`supplies` collection have a discounted price of less than `5`.

The following example uses `$expr` with `$cond` to
calculate the discounted price based on the `qty` and 
`$lt` to return documents whose calculated discount price
is less than `NumberDecimal("5")`:

```javascript
// Aggregation expression to calculate discounted price 

let discountedPrice = { 
   $cond: { 
      if: { $gte: ["$qty", 100] }, 
      then: { $multiply: ["$price", NumberDecimal("0.50")] }, 
      else: { $multiply: ["$price", NumberDecimal("0.75")] } 
   } 
};

// Query the supplies collection using the aggregation expression

db.supplies.find( { $expr: { $lt:[ discountedPrice,  NumberDecimal("5") ] } });
```

The following table shows the discounted price for each document and
whether discounted price is less than `NumberDecimal("5")` (i.e.
whether the document meets the query condition).

| Document | Discounted Price | < NumberDecimal("5") |
|---|---|---|
| {"_id": 1, "item": "binder", "qty": 100, "price": NumberDecimal("12") } | NumberDecimal("6.00") | `false` |
| {"_id": 2, "item": "noteboook", "qty": 200, "price": NumberDecimal("8") } | NumberDecimal("4.00") | `true` |
| {"_id": 3, "item": "pencil", "qty": 50, "price": NumberDecimal("6") } | NumberDecimal("4.50") | `true` |
| {"_id": 4, "item": "eraser", "qty": 150, "price": NumberDecimal("3") } | NumberDecimal("1.50") | `true` |
| {"_id": 5, "item": "legal pad", "qty": 42, "price": NumberDecimal("10") } | NumberDecimal("7.50") | `false` |

The `db.collection.find()` operation returns the documents whose
calculated discount price is less than `NumberDecimal("5")`:

```javascript
{ _id : 2, item : "notebook", qty : 200 , price : NumberDecimal("8") }
{ _id : 3, item : "pencil", qty : 50 , price : NumberDecimal("6") }
{ _id : 4, item : "eraser", qty : 150 , price : NumberDecimal("3") }
```

Even though `$cond` calculates an effective discounted
price, that price is not reflected in the returned documents. Instead,
the returned documents represent the matching documents in their
original state. The find operation did not return the `binder`
or `legal pad` documents, as their discounted price was greater than
`5`.
