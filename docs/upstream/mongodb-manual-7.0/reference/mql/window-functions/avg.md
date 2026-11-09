<!-- Converted from reference/mql/window-functions/avg.txt (reStructuredText). Includes are inlined. -->

# $avg (window function)

## Definition

**`$avg`**

Returns the average of values from a particular window.

**Note:** Disambiguation

This page describes `$avg` when used as an **window function**.

You can also use `$avg` in these other contexts:

- `$avg (accumulator)`, which returns a single
  aggregated value based on a variable number of input documents.

- `$avg (expression)`, which
  returns the average of numeric elements in an array.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $avg: <expression>
         }
      }
   }
}
```

## Behavior

### Result Type

The default return type is a double. If at least one input value is a
decimal, then the return type is a decimal.

### Non-numeric or Missing Values

`$avg` ignores non-numeric values, including missing values. If all
input values are non-numeric, `$avg` returns `null`.

## Example

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

This example uses the `$avg` window function to output the moving
average for the cake sales `quantity` for each `state`. For each
state, add a field to each document that contains the averaged quantity
of the order and all previous orders.

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            averageQuantityForState: {
               $avg: "$quantity",
               window: {
                  documents: [ "unbounded", "current" ]
               }         
            }
         }
      }
   }
] )
```

The moving average `quantity` for `CA` and `WA` is shown in the
`averageQuantityForState` field:

```javascript
[
   {
      _id: 4,
      type: 'strawberry',
      orderDate: ISODate('2019-05-18T16:09:01.000Z'),
      state: 'CA',
      price: 41,
      quantity: 162,
      averageQuantityForState: 162
   },
   {
      _id: 0,
      type: 'chocolate',
      orderDate: ISODate('2020-05-18T14:10:30.000Z'),
      state: 'CA',
      price: 13,
      quantity: 120,
      averageQuantityForState: 141
   },
   {
      _id: 2,
      type: 'vanilla',
      orderDate: ISODate('2021-01-11T06:31:15.000Z'),
      state: 'CA',
      price: 12,
      quantity: 145,
      averageQuantityForState: 142.33333333333334
   },
   {
      _id: 5,
      type: 'strawberry',
      orderDate: ISODate('2019-01-08T06:12:03.000Z'),
      state: 'WA',
      price: 43,
      quantity: 134,
      averageQuantityForState: 134
   },
   {
      _id: 3,
      type: 'vanilla',
      orderDate: ISODate('2020-02-08T13:13:23.000Z'),
      state: 'WA',
      price: 13,
      quantity: 104,
      averageQuantityForState: 119
   },
   {
      _id: 1,
      type: 'chocolate',
      orderDate: ISODate('2021-03-20T11:30:05.000Z'),
      state: 'WA',
      price: 14,
      quantity: 140,
      averageQuantityForState: 126
   }
]
```

In the preceding example:

- `partitionBy: "$state"` partitions the documents in the collection by
  `state`. There are partitions for `CA` and `WA`.

- `sortBy: { orderDate: 1 }` sorts the documents in each partition by
  `orderDate` in ascending order (`1`), so the earliest
  `orderDate` is first.

- `output` sets the `averageQuantityForState` field to the moving
  average `quantity` for the documents in a documents window.

  The window contains documents between
  an `unbounded` lower limit and the `current` document in the
  output. This means `$avg` returns the moving average of `quantity`
  for the documents between the beginning of the partition and the
  current document (inclusive).
