<!-- Converted from reference/operator/aggregation/last.txt (reStructuredText). Includes are inlined. -->

# $last (aggregation accumulator)

## Definition

**`$last`**

**Changed in version:** 5.0

Returns the value that results from applying an expression to the last document in a group of documents.
Only meaningful when documents are in a defined order.

`$last` is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`
- `$setWindowFields` (Available starting in MongoDB 5.0)

**Note:** Disambiguation

This page describes the `$last` aggregation accumulator. For
the `$last` array operator, see `$last (array
operator)`.

## Syntax

`$last` syntax:

```javascript
{ $last: <expression> }
```

For more information on expressions, see aggregation-expressions.

## Behavior

To define the document order for `$last` with the:

- `$group` stage, add a `$sort` stage before the
  `$group` stage.

- `$setWindowFields` stage, set the sortBy field.

**Note:**

Although the `$sort` stage passes ordered documents as
input to the `$group` and `$setWindowFields`
stages, those stages are not guaranteed to maintain the sort order in
their own output.

When used with `$setWindowFields`, `$last` returns `null`
for empty windows. An example empty
window is a `{ documents: [ -1, -1 ] }` documents window on the first document of a
partition.

## Examples

### Use in `$group` Stage

Consider a `sales` collection with the following documents:

```javascript
{ "_id" : 1, "item" : "abc", "date" : ISODate("2014-01-01T08:00:00Z"), "price" : 10, "quantity" : 2 }
{ "_id" : 2, "item" : "jkl", "date" : ISODate("2014-02-03T09:00:00Z"), "price" : 20, "quantity" : 1 }
{ "_id" : 3, "item" : "xyz", "date" : ISODate("2014-02-03T09:05:00Z"), "price" : 5, "quantity" : 5 }
{ "_id" : 4, "item" : "abc", "date" : ISODate("2014-02-15T08:00:00Z"), "price" : 10, "quantity" : 10 }
{ "_id" : 5, "item" : "xyz", "date" : ISODate("2014-02-15T09:05:00Z"), "price" : 5, "quantity" : 10 }
{ "_id" : 6, "item" : "xyz", "date" : ISODate("2014-02-15T12:05:10Z"), "price" : 5, "quantity" : 5 }
{ "_id" : 7, "item" : "xyz", "date" : ISODate("2014-02-15T14:12:12Z"), "price" : 5, "quantity" : 10 }
```

The following operation first sorts the documents by `item` and
`date`, and then in the following `$group` stage, groups
the now sorted documents by the `item` field and uses the
`$last` accumulator to compute the last sales date for each item:

```javascript
db.sales.aggregate(
   [
     { $sort: { item: 1, date: 1 } },
     {
       $group:
         {
           _id: "$item",
           lastSalesDate: { $last: "$date" }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : "xyz", "lastSalesDate" : ISODate("2014-02-15T14:12:12Z") }
{ "_id" : "jkl", "lastSalesDate" : ISODate("2014-02-03T09:00:00Z") }
{ "_id" : "abc", "lastSalesDate" : ISODate("2014-02-15T08:00:00Z") }
```

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

This example uses `$last` in the `$setWindowFields`
stage to output the last cake sales order `type` for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            lastOrderTypeForState: {
               $last: "$type",
               window: {
                  documents: [ "current", "unbounded" ]
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

- `output` sets the `lastOrderTypeForState` field to the last
  order `type` from the documents
  window.
  
  The window contains documents between
  the `current` lower limit, which is the current document in the
  output, and the `unbounded` upper limit. This means `$last`
  returns the last order `type` for the documents between the
  current document and the end of the partition.

In this output, the last order `type` value for `CA` and `WA` is
shown in the `lastOrderTypeForState` field:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "lastOrderTypeForState" : "vanilla" }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "lastOrderTypeForState" : "vanilla" }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "lastOrderTypeForState" : "vanilla" }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "lastOrderTypeForState" : "chocolate" }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "lastOrderTypeForState" : "chocolate" }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "lastOrderTypeForState" : "chocolate" }
```
