<!-- Converted from reference/operator/aggregation/convert.txt (reStructuredText). Includes are inlined. -->

# $convert (aggregation)

## Definition

**`$convert`**

Converts a value to a specified type.

## Compatibility

You can use `$convert` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`$convert` has the following syntax:

```javascript
{
 $convert:
     {
        input: <expression>,
        to: <type expression>,
        onError: <expression>,  // Optional.
        onNull: <expression>    // Optional.
      }
}
```

The `$convert` takes a document with the following fields:

* - Field
  - Description

* - `input`
  - The argument can be any valid expression. For more information on
    expressions, see aggregation-expressions.

* - `to`
  - The argument can be any valid expression that resolves to one of the following
    numeric or string identifiers:

    | String Identifier | Numeric Identifier | Notes |
    |---|---|---|
    | "double" | 1 | For more information on the conversion to double, see convert-to-double. |
    | "string" | 2 | For more information on the conversion to string, see convert-to-string. |
    | "objectId" | 7 | For more information on the conversion to objectId, see convert-to-objectId. |
    | "bool" | 8 | For more information on the conversion to boolean, see convert-to-bool. |
    | "date" | 9 | For more information on the conversion to date, see convert-to-date. |
    | "int" | 16 | For more information on the conversion to integer, see convert-to-int. |
    | "long" | 18 | For more information on the conversion to long, see convert-to-long. |
    | "decimal" | 19 | For more information on the conversion to decimal, see convert-to-decimal. |

* - `onError`
  - Optional. The value to return on encountering an error during
    conversion, including unsupported type conversions. The
    arguments can be any valid expression.

    If unspecified, the operation throws an error upon
    encountering an error and stops.

* - `onNull`
  - Optional. The value to return if the `input` is null or
    missing. The arguments can be any valid expression.

    If unspecified, `$convert` returns null if the
    `input` is null or missing.

In addition to `$convert`, MongoDB provides the
following aggregation operators as shorthand when the default
"onError" and "onNull" behavior is acceptable:

- `$toBool`
- `$toDate`
- `$toDecimal`
- `$toDouble`
- `$toInt`
- `$toLong`
- `$toObjectId`
- `$toString`

## Behavior

### Converting to a Boolean

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
| Null | Returns the value specified for the `onNull` option. By default, returns null. |
| Object | Returns true |
| ObjectId | Returns true |
| Regular expression | Returns true |
| String | Returns true |
| Timestamp | Returns true |

To learn more about data types in MongoDB, see bson-types.

The following table lists some conversion to boolean examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: true, to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: false, to: "bool" } | false |
| .. code-block:: javascript :copyable: false { input: 1.99999, to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: Decimal128( "5" ), to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: Decimal128( "0" ), to: "bool" } | false |
| .. code-block:: javascript :copyable: false { input: 100, to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: ISODate( "2018-03-26T04:38:28.044Z" ), to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: "hello", to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: "false", to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: "", to: "bool" } | true |
| .. code-block:: javascript :copyable: false { input: null, to: "bool" } | null |

**See also:**

`$toBool`

### Converting to an Integer

The following table lists the input types that can be converted to an
integer:

| Input Type | Behavior |
|---|---|
| Boolean | \| Returns `0` for  `false`. \| Returns `1` for `true`. |
| Double | Returns truncated value. The truncated double value must fall within the minimum and maximum value for an integer. You cannot convert a double value whose truncated value is less than the minimum integer value or is greater than the maximum integer value. |
| Decimal | Returns truncated value. The truncated decimal value must fall within the minimum and maximum value for an integer. You cannot convert a decimal value whose truncated value is less than the minimum integer value or is greater than the maximum integer value. |
| Integer | No-op. Returns the integer value. |
| Long | Returns the long value as an integer. The long value must fall within the minimum and maximum value for an integer. You cannot convert a long value that is less than the minimum integer value or is greater than the maximum integer value. |
| String | Returns the numerical value of the string as an integer. The string value must be a base`10` integer (e.g. `"-5"`, `"123456"`) and fall within the minimum and maximum value for an integer. You cannot convert a string value of a float or decimal or non-base`10` number (e.g. `"-5.0"`, `"0x6400"`) or a value that falls outside the minimum and maximum value for an integer. |

The following table lists some conversion to integer examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: true, to: "int" } | 1 |
| .. code-block:: javascript :copyable: false { input: false, to: "int" } | 0 |
| .. code-block:: javascript :copyable: false { input: 1.99999, to: "int" } | 1 |
| .. code-block:: javascript :copyable: false { input: Decimal128( "5.5000" ), to: "int" } | 5 |
| .. code-block:: javascript :copyable: false { input: Decimal128( "9223372036000.000" ), to: "int" } | Error |
| .. code-block:: javascript :copyable: false { input: Long( "5000" ), to: "int" } | 5000 |
| .. code-block:: javascript :copyable: false { input: Long( "922337203600" ), to: "int" } | Error |
| .. code-block:: javascript :copyable: false { input: "-2", to: "int" } | -2 |
| .. code-block:: javascript :copyable: false { input: "2.5", to: "int" } | Error |
| .. code-block:: javascript :copyable: false { input: null, to: "int" } | null |

**See also:**

`$toInt` operator.

### Converting to a Decimal

The following table lists the input types that can be converted to a
decimal:

| Input Type | Behavior |
|---|---|
| Boolean | \| Returns `Decimal128( "0" )` for  `false`. \| Returns `Decimal128( "1" )` for `true`. |
| Double | Returns double value as a decimal. |
| Decimal | No-op. Returns the decimal. |
| Integer | Returns the int value as a decimal. |
| Long | Returns the long value as a decimal. |
| String | Returns the numerical value of the string as a decimal. The string value must be of a base`10` numeric value (e.g. `"-5.5"`, `"123456"`). You cannot convert a string value of a non-base`10` number (e.g. `"0x6400"`) |
| Date | Returns the number of milliseconds since the epoch that corresponds to the date value. |

The following table lists some conversion to decimal examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: true, to: "decimal" } | Decimal128("1") |
| .. code-block:: javascript :copyable: false { input: false, to: "decimal" } | Decimal128("0") |
| .. code-block:: javascript :copyable: false { input: 2.5, to: "decimal" } | Decimal128( "2.50000000000000" ) |
| .. code-block:: javascript :copyable: false { input: Int32( 5 ), to: "decimal" } | Decimal128("5") |
| .. code-block:: javascript :copyable: false { input: Long( 10000 ), to: "decimal" } | Decimal128("10000") |
| .. code-block:: javascript :copyable: false { input: "-5.5", to: "decimal" } | Decimal128("-5.5") |
| .. code-block:: javascript :copyable: false { input: ISODate( "2018-03-26T04:38:28.044Z" ), to: "decimal" } | Decimal128("1522039108044") |

**See also:**

`$toDecimal`

### Converting to a Double

The following table lists the input types that can be converted to a
double:

| Input Type | Behavior |
|---|---|
| Boolean | \| Returns NumberDouble(0) for  `false`. \| Returns NumberDouble(1) for `true`. |
| Double | No-op. Returns the double. |
| Decimal | Returns the decimal value as a double. The decimal value must fall within the minimum and maximum value for a double. You cannot convert a decimal value whose value is less than the minimum double value or is greater than the maximum double value. |
| Integer | Returns the int value as a double. |
| Long | Returns the long value as a double. |
| String | Returns the numerical value of the string as a double. The string value must be of a base`10` numeric value (e.g. `"-5.5"`, `"123456"`) and fall within the minimum and maximum value for a double. You cannot convert a string value of a non-base`10` number (e.g. `"0x6400"`) or a value that falls outside the minimum and maximum value for a double. |
| Date | Returns the number of milliseconds since the epoch that corresponds to the date value. |

The following table lists some conversion to double examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: true, to: "double" } | 1 |
| .. code-block:: javascript :copyable: false { input: false, to: "double" } | 0 |
| .. code-block:: javascript :copyable: false { input: 2.5, to: "double" } | 2.5 |
| .. code-block:: javascript :copyable: false { input: Int32( 5 ), to: "double" } | 5 |
| .. code-block:: javascript :copyable: false { input: Long( "10000" ), to: "double" } | 10000 |
| .. code-block:: javascript :copyable: false { input: "-5.5", to: "double" } | -5.5 |
| .. code-block:: javascript :copyable: false { input: "5e10", to: "double" } | 50000000000 |
| .. code-block:: javascript :copyable: false { input: ISODate( "2018-03-26T04:38:28.044Z" ), to: "double" } | 1522039108044 |

**See also:**

`$toDouble`

### Converting to a Long

The following table lists the input types that can be converted to a
long:

| Input Type | Behavior |
|---|---|
| Boolean | \| Returns `0` for  `false`. \| Returns `1` for `true`. |
| Double | Returns truncated value. The truncated double value must fall within the minimum and maximum value for a long. You cannot convert a double value whose truncated value is less than the minimum long value or is greater than the maximum long value. |
| Decimal | Returns truncated value. The truncated decimal value must fall within the minimum and maximum value for a long. You cannot convert a decimal value whose truncated value is less than the minimum long value or is greater than the maximum long value. |
| Integer | Returns the int value as a long. |
| Long | No-op. Returns the long value. |
| String | Returns the numerical value of the string. The string value must be of a base`10` long (e.g. `"-5"`, `"123456"`) and fall within the minimum and maximum value for a long. You cannot convert a string value of a float or decimal or non-base`10` number (e.g. `"-5.0"`, `"0x6400"`) or a value that falls outside the minimum and maximum value for a long. |
| Date | Converts the Date into the number of milliseconds since the epoch. |

The following table lists some conversion to long examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: true, to: "long" } | Long("1") |
| .. code-block:: javascript :copyable: false { input: false, to: "long"  } | Long("0") |
| .. code-block:: javascript :copyable: false { input: 2.5, to: "long"  } | Long("2") |
| .. code-block:: javascript :copyable: false { input: Decimal128( "5.5000" ), to: "long" } | Long("5") |
| .. code-block:: javascript :copyable: false { input: Decimal128( "9223372036854775808.0" ), to: "long" } | Error |
| .. code-block:: javascript :copyable: false { input: Int32( 8 ), to: "long" } | Long("8") |
| .. code-block:: javascript :copyable: false { input: ISODate( "2018-03-26T04:38:28.044Z" ), to: "long" } | Long("1522039108044") |
| .. code-block:: javascript :copyable: false { input: "-2", to: "long" } | Long("-2") |
| .. code-block:: javascript :copyable: false { input: "2.5", to: "long" } | Error |
| .. code-block:: javascript :copyable: false { input: null, to: "long" } | null |

**See also:**

`$toLong`

### Converting to a Date

The following table lists the input types that can be converted to a
date:

* - Input Type
  - Behavior

* - Double
  - Returns a date that corresponds to the number of milliseconds
    represented by the truncated double value.

    Positive number corresponds to the number of milliseconds since
    Jan 1, 1970.

    Negative number corresponds to the number of milliseconds before
    Jan 1, 1970.

* - Decimal
  - Returns a date that corresponds to the number of milliseconds
    represented by the truncated decimal value.

    Positive number corresponds to the number of milliseconds since
    Jan 1, 1970.

    Negative number corresponds to the number of milliseconds before
    Jan 1, 1970.

* - Long
  - Returns a date that corresponds to the number of milliseconds
    represented by the long value.

    Positive number corresponds to the number of milliseconds since
    Jan 1, 1970.

    Negative number corresponds to the number of milliseconds before
    Jan 1, 1970.

* - String
  - Returns a date that corresponds to the date string.

    The string must be a valid date string, such as:

    - "2018-03-03"
    - "2018-03-03T12:00:00Z"
    - "2018-03-03T12:00:00+0500"

* - ObjectId
  - Returns a date that corresponds to the timestamp of the
    ObjectId.

* - Timestamp
  - Returns a date that corresponds to the timestamp. 

The following table lists some conversion to date examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: 120000000000.5, to: "date" } | ISODate("1973-10-20T21:20:00.000Z") |
| .. code-block:: javascript :copyable: false { input: Decimal128( "1253372036000.50" ), to: "date" } | ISODate("2009-09-19T14:53:56.000Z") |
| .. code-block:: javascript :copyable: false { input: Long( "1100000000000" ), to: "date } | ISODate("2004-11-09T11:33:20.000Z") |
| .. code-block:: javascript :copyable: false { input:  Long( "-1100000000000" ), to: "date" } | ISODate("1935-02-22T12:26:40.000Z") |
| .. code-block:: javascript :copyable: false { input: ObjectId( "5ab9c3da31c2ab715d421285" ), to: "date" } | ISODate("2018-03-27T04:08:58.000Z") |
| .. code-block:: javascript :copyable: false { input:  "2018-03-03", to: "date" } | ISODate("2018-03-03T00:00:00.000Z") |
| .. code-block:: javascript :copyable: false { input: "2018-03-20 11:00:06 +0500", to: "date" } | ISODate("2018-03-20T06:00:06.000Z") |
| .. code-block:: javascript :copyable: false { input: "Friday", to: "date" } | Error |
| .. code-block:: javascript :copyable: false { input: Timestamp( { t: 1637688118, i: 1 } ), to: "date" } | ISODate("2021-11-23T17:21:58.000Z") |

**See also:**

- `$toDate` operator
- `$dateFromString`

### Converting to an ObjectId

The following table lists the input types that can be converted to an
ObjectId:

| Input Type | Behavior |
|---|---|
| String | Returns an ObjectId for the hexadecimal string of length 24. You cannot convert a string value that is not a hexadecimal string of length 24. |

The following table lists some conversion to date examples:

| Example | Results |
|---|---|
| .. code-block:: javascript :copyable: false { input: "5ab9cbfa31c2ab715d42129e", to: "objectId" } | ObjectId("5ab9cbfa31c2ab715d42129e") |
| .. code-block:: javascript :copyable: false { input: "5ab9cbfa31c2ab715d42129", to: "objectId" } | Error |

**See also:**

`$toObjectId` operator.

### Converting to a String

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
| .. code-block:: javascript :copyable: false { input: true, to: "string" } | "true" |
| .. code-block:: javascript :copyable: false { input: false, to: "string" } | "false" |
| .. code-block:: javascript :copyable: false { input: 2.5, to: "string" } | "2.5" |
| .. code-block:: javascript :copyable: false { input: Int32( 2 ), to: "string" } | "2" |
| .. code-block:: javascript :copyable: false { input:  Long( 1000 ), to: "string" } | "1000" |
| .. code-block:: javascript :copyable: false { input: ObjectId( "5ab9c3da31c2ab715d421285" ), to: "string" } | "5ab9c3da31c2ab715d421285" |
| .. code-block:: javascript :copyable: false { input:  ISODate( "2018-03-27T16:58:51.538Z" ), to: "string" } | "2018-03-27T16:58:51.538Z" |

**See also:**

- `$toString` operator
- `$dateToString`

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple", qty: 5, price: 10 },
   { _id: 2, item: "pie", qty: 10, price: Decimal128("20.0") },
   { _id: 3, item: "ice cream", qty: 2, price: "4.99" },
   { _id: 4, item: "almonds" },
   { _id: 5, item: "bananas", qty: 5000000000, price: Decimal128("1.25") }
] )
```

The following aggregation operation on the `orders` collection
converts the `price` to a decimal:

```javascript
// Define stage to add convertedPrice and convertedQty fields with
//    the converted price and qty values.
// If price or qty values are missing, the conversion returns a
//    value of decimal value or int value of 0.
// If price or qty values cannot be converted, the conversion returns
//    a string

priceQtyConversionStage = { 
   $addFields: { 
      convertedPrice: { $convert:
         {
            input: "$price",
            to: "decimal",
            onError: "Error",
            onNull: Decimal128("0")
         } },
      convertedQty: { $convert:
         { 
            input: "$qty",
            to: "int", 
            onError:{ $concat:
               [
                  "Could not convert ",
                  { $toString:"$qty" },
                  " to type integer."
               ]
            },
         onNull: Int32("0") 
      } },
   }
};

totalPriceCalculationStage = { 
   $project: { totalPrice: {
     $switch: {
        branches: [
          { case:
             { $eq: [ { $type: "$convertedPrice" }, "string" ] },
             then: "NaN"
          },
          { case:
             { $eq: [ { $type: "$convertedQty" }, "string" ] },
             then: "NaN"
          },
        ],
        default: { $multiply: [ "$convertedPrice", "$convertedQty" ] }
     }
} } };

db.orders.aggregate( [
   priceQtyConversionStage,
   totalPriceCalculationStage
])
```

The operation returns the following documents:

```javascript
 :copyable: false

{ _id: 1, totalPrice: Decimal128("50") },
{ _id: 2, totalPrice: Decimal128("200.0") },
{ _id: 3, totalPrice: Decimal128("9.98") },
{ _id: 4, totalPrice: Decimal128("0") },
{ _id: 5, totalPrice: 'NaN' }
```

**Note:**

These examples use `mongosh`. The default types are
different in the legacy `mongo` shell.
