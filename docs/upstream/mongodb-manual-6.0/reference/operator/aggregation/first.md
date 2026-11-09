<!-- Converted from reference/operator/aggregation/first.txt (reStructuredText). Includes are inlined. -->

# $first (aggregation accumulator)

## Definition

**`$first`**

   

**Changed in version:** 5.0

Returns the value that results from applying an expression to the first document in a group of
documents. Only meaningful when documents are in a defined order.

`$first` is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`
- `$setWindowFields` (Available starting in MongoDB 5.0)

**Note:** Disambiguation

This page describes the `$first` aggregation accumulator. For
the `$first` array operator, see `$first
(array operator)`.

## Syntax

`$first` syntax:

```javascript
{ $first: <expression> }
```

For more information on expressions, see aggregation-expressions.

## Behavior

To define the document order for `$first` with the:

- `$group` stage, add a `$sort` stage before the
  `$group` stage.

- `$setWindowFields` stage, set the sortBy field.

**Note:**

Although the `$sort` stage passes ordered documents as
input to the `$group` and `$setWindowFields`
stages, those stages are not guaranteed to maintain the sort order in
their own output.

When used with `$setWindowFields`, `$first` returns `null`
for empty windows. An example empty
window is a `{ documents: [ -1, -1 ] }` documents window on the first document of a
partition.

### Missing Values

The documents in a group may be missing fields or may have fields with
missing values.

- If there are no documents from the prior pipeline stage, the 
  `$group` stage returns nothing.
- If the field that the `$first` accumulator is processing is
  missing, `$first` returns `null`.
  
See the missing data example.

## Examples

### Use in `$group` Stage

Create the `sales` collection:

```javascript
db.sales.insertMany( [
   { "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : ISODate("2014-01-01T08:00:00Z") },
   { "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : ISODate("2014-02-03T09:00:00Z") },
   { "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : ISODate("2014-02-03T09:05:00Z") },
   { "_id" : 4, "item" : "abc", "price" : 10, "quantity" : 10, "date" : ISODate("2014-02-15T08:00:00Z") },
   { "_id" : 5, "item" : "xyz", "price" : 5, "quantity" : 10, "date" : ISODate("2014-02-15T09:05:00Z") },
   { "_id" : 6, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : ISODate("2014-02-15T12:05:10Z") },
   { "_id" : 7, "item" : "xyz", "price" : 5, "quantity" : 10, "date" : ISODate("2014-02-15T14:12:12Z") }
] )
```

Grouping the documents by the `item` field, the following operation
uses the `$first` accumulator to compute the first sales date for
each item:

```javascript
db.sales.aggregate(
   [
     { $sort: { item: 1, date: 1 } },
     {
       $group:
         {
           _id: "$item",
           firstSale: { $first: "$date" }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
[
   { _id: 'jkl', firstSale: ISODate("2014-02-03T09:00:00.000Z") },
   { _id: 'xyz', firstSale: ISODate("2014-02-03T09:05:00.000Z") },
   { _id: 'abc', firstSale: ISODate("2014-01-01T08:00:00.000Z") }
]
```

### Missing Data

Some documents in the `badData` collection are missing fields, other
documents are missing values. 

Create the `badData` collection:

```javascript
db.badData.insertMany( [
   { "_id": 1, "price": 6, "quantity": 6 },
   { "_id": 2, "item": "album", "price": 5 , "quantity": 5  },
   { "_id": 7, "item": "tape", "price": 6, "quantity": 6 },
   { "_id": 8, "price": 5, "quantity": 5  },
   { "_id": 9, "item": "album", "price": 3, "quantity": '' },
   { "_id": 10, "item": "tape", "price": 3, "quantity":  4 },
   { "_id": 12, "item": "cd", "price": 7  }
] )
```

Query the `badData` collection, grouping the output on the `item`
field:

```javascript
db.badData.aggregate( [
   { $sort: { item: 1, price: 1 } },
   { $group: 
      { 
         _id: "$item",
         inStock: { $first: "$quantity" }
      }
   }
] )
```

The `$sort` stage orders the documents and passes them to the
`$group` stage.

```javascript
[
  { _id: null, inStock: 5 },
  { _id: 'album', inStock: '' },
  { _id: 'cd', inStock: null },
  { _id: 'tape', inStock: 4 }
]
```

`$first` selects the first document from each output group:

- The `_id: null` group is included.
- When the accumulator field, `$quantity` in this example, is 
  missing, `$first` returns `null`.

### Use in `$setWindowFields` Stage

**New in version:** 5.0

Create a `cakeSales` collection that contains cake sales in the states
of California (`CA`) and Washington (`WA`):

```javascript
db.cakeSales.insertMany( [
   { _id: 0, type: "chocolate", orderDate: new Date("2020-05-18T14:10:30Z"),
     state: "CA", price: 13, quantity: 120 },
   { _id: 1, type: "chocolate", orderDate: new Date("2021-03-20T11:30:05Z"),
     state: "WA", price: 14, quantity: 140 },
   { _id: 2, type: "vanilla", orderDate: new Date("2021-01-11T06:31:15Z"),
     state: "CA", price: 12, quantity: 145 },
   { _id: 3, type: "vanilla", orderDate: new Date("2020-02-08T13:13:23Z"),
     state: "WA", price: 13, quantity: 104 },
   { _id: 4, type: "strawberry", orderDate: new Date("2019-05-18T16:09:01Z"),
     state: "CA", price: 41, quantity: 162 },
   { _id: 5, type: "strawberry", orderDate: new Date("2019-01-08T06:12:03Z"),
     state: "WA", price: 43, quantity: 134 }
] )
```

This example uses `$first` in the `$setWindowFields`
stage to output the first cake sales order `type` for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            firstOrderTypeForState: {
               $first: "$type",
               window: {
                  documents: [ "unbounded", "current" ]
               }         
            }
         }
      }
   }
] )
```

In the example:

- `partitionBy: "$state"` partitions the documents in the collection by
  `state`. There are partitions for `CA` and `WA`.

- `sortBy: { orderDate: 1 }` sorts the documents in each partition by
  `orderDate` in ascending order (`1`), so the earliest
  `orderDate` is first.

- `output` sets the `firstOrderTypeForState` field to the first
  order `type` from the documents
  window.
  
  The window contains documents between
  an `unbounded` lower limit and the `current` document in the
  output. This means `$first` returns the first order `type`
  for the documents between the beginning of the partition and the
  current document.

In this output, the first order `type` value for `CA` and `WA` is
shown in the `firstOrderTypeForState` field:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "firstOrderTypeForState" : "strawberry" }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "firstOrderTypeForState" : "strawberry" }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "firstOrderTypeForState" : "strawberry" }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "firstOrderTypeForState" : "strawberry" }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "firstOrderTypeForState" : "strawberry" }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "firstOrderTypeForState" : "strawberry" }
```
