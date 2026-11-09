<!-- Converted from reference/operator/aggregation/toBool.txt (reStructuredText). Includes are inlined. -->

# $toBool (expression operator)

## Definition

**`$toBool`**

Converts a value to a boolean.

`$toBool` has the following syntax:

```javascript
{
   $toBool: <expression>
}
```

The `$toBool` takes any valid expression.

The `$toBool` is a shorthand for the following
`$convert` expression:

```javascript
{ $convert: { input: <expression>, to: "bool" } }
```

**See also:**

`$convert`

## Behavior

The following table lists the input types that can be converted to a
boolean:

| Input Type | Behavior |
|---|---|
| Array | Returns true |
| Binary data | Returns true |
| Boolean | No-op. Returns the boolean value. |
| Code | Returns true |
| Date | Returns true |
| Decimal | \| Returns true if not zero \| Return false if zero |
| Double | \| Returns true if not zero \| Return false if zero |
| Integer | \| Returns true if not zero \| Return false if zero |
| JavaScript | Returns true |
| Long | \| Returns true if not zero \| Return false if zero |
| MaxKey | Returns true |
| MinKey | Returns true |
| Null | Returns null |
| Object | Returns true |
| ObjectId | Returns true |
| Regular expression | Returns true |
| String | Returns true |
| Timestamp | Returns true |

To learn more about data types in MongoDB, see bson-types.

The following table lists some conversion to boolean examples:

| Example | Results |
|---|---|
| `{$toBool: false}` | false |
| `{$toBool: 1.99999}` | true |
| `{$toBool: Decimal128("5")}` | true |
| `{$toBool: Decimal128("0")}` | false |
| `{$toBool: 100}` | true |
| `{$toBool: ISODate("2018-03-26T04:38:28.044Z")}` | true |
| `{$toBool: "false"}` | true |
| `{$toBool: ""}` | true |
| `{$toBool: null}` | null |

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple",  qty: 5, shipped: true },
   { _id: 2, item: "pie",  qty: 10, shipped: 0  },
   { _id: 3, item: "ice cream", shipped: 1 },
   { _id: 4, item: "almonds", qty: 2, shipped: "true" },
   { _id: 5, item: "pecans", shipped: "false" },  // Note: All strings convert to true
   { _id: 6, item: "nougat", shipped: ""  }       // Note: All strings convert to true
] )
```

The following aggregation operation on the `orders` collection
converts the `shipped` to a boolean value before finding the
unshipped orders:

```javascript
// Define stage to add convertedShippedFlag field with the converted shipped value
// Because all strings convert to true, include specific handling for "false" and "" 

shippedConversionStage = {
   $addFields: {
      convertedShippedFlag: { 
         $switch: { 
            branches: [
              { case: { $eq: [ "$shipped", "false" ] }, then: false } , 
              { case: { $eq: [ "$shipped", "" ] }, then: false }
            ],
            default: { $toBool: "$shipped" }
        }
      }
   }
};

// Define stage to filter documents and pass only the unshipped orders

unshippedMatchStage = {
   $match: { "convertedShippedFlag": false }
};

db.orders.aggregate( [
  shippedConversionStage,
  unshippedMatchStage
] )
```

The operation returns the following document:

```javascript
{ "_id" : 2, "item" : "pie", "qty" : 10, "shipped" : 0, "convertedShippedFlag" : false }
{ "_id" : 5, "item" : "pecans", "shipped" : "false", "convertedShippedFlag" : false }
{ "_id" : 6, "item" : "nougat", "shipped" : "", "convertedShippedFlag" : false }
```

**Note:**

If the conversion operation encounters an error, the aggregation
operation stops and throws an error. To override this behavior, use
`$convert` instead.
