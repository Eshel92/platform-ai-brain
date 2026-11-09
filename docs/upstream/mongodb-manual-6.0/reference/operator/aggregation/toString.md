<!-- Converted from reference/operator/aggregation/toString.txt (reStructuredText). Includes are inlined. -->

# $toString (aggregation)

## Definition

**`$toString`**

Converts a value to a string. If the value cannot be converted
to a string, `$toString` errors. If the value is null or
missing, `$toString` returns null.

`$toString` has the following syntax:

```javascript
{
   $toString: <expression>
}
```

The `$toString` takes any valid expression.

The `$toString` is a shorthand for the following
`$convert` expression:

```javascript
{ $convert: { input: <expression>, to: "string" } }
```

**See also:**

- `$convert`
- `$dateToString`

## Behavior

The following table lists the input types that can be converted to a
string:

| Input Type | Behavior |
|---|---|
| Boolean | Returns the boolean value as a string. |
| Double | Returns the double value as a string. |
| Decimal | Returns the decimal value as a string. |
| Integer | Returns the integer value as a string. |
| Long | Returns the long value as a string. |
| ObjectId | Returns the ObjectId value as a hexadecimal string.. |
| String | No-op. Returns the string value. |
| Date | Returns the date as a string. |

The following table lists some conversion to string examples:

| Example | Results |
|---|---|
| `{$toString: true}` | "true" |
| `{$toString: false}` | "false" |
| `{$toString: 2.5}` | "2.5" |
| `{$toString: NumberInt(2)}` | "2" |
| `{$toString:  NumberLong(1000)}` | "1000" |
| `{$toString: ObjectId("5ab9c3da31c2ab715d421285")}` | "5ab9c3da31c2ab715d421285" |
| `{$toString:  ISODate("2018-03-27T16:58:51.538Z")}` | "2018-03-27T16:58:51.538Z" |

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple",  qty: 5, zipcode: 93445 },
   { _id: 2, item: "almonds", qty: 2, zipcode: "12345-0030" },
   { _id: 3, item: "peaches",  qty: 5, zipcode: 12345 },
] )
```

The following aggregation operation on the `orders` collection
converts the `zipcode` to string before sorting by the string value:

```javascript
// Define stage to add convertedZipCode field with the converted zipcode value

zipConversionStage = {
   $addFields: {
      convertedZipCode: { $toString: "$zipcode" }
   }
};

// Define stage to sort documents by the converted zipcode

sortStage = {
   $sort: { "convertedZipCode": 1 }
};

db.orders.aggregate( [
  zipConversionStage,
  sortStage
] )
```

The operation returns the following documents:

```javascript
{
  _id: 3,
  item: 'peaches',
  qty: 5,
  zipcode: 12345,
  convertedZipCode: '12345'
},
{
  _id: 2,
  item: 'almonds',
  qty: 2,
  zipcode: '12345-0030',
  convertedZipCode: '12345-0030'
},
{
  _id: 1,
  item: 'apple',
  qty: 5,
  zipcode: 93445,
  convertedZipCode: '93445'
}
```

**Note:**

If the conversion operation encounters an error, the aggregation
operation stops and throws an error. To override this behavior, use
`$convert` instead.
