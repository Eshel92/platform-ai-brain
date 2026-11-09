<!-- Converted from reference/mql/expressions.txt (reStructuredText). Includes are inlined. -->

# Expressions

Expressions are MQL (MongoDB Query Language) components that
evaluate to a value without modifying their inputs. You can use them
in the following contexts:

- Some aggregation pipeline stages, such as `$project`,
  `$addFields`, and `$group`
  
- Query predicates that use `$expr`

- Find command projections

In the MongoDB Query Language, you can build expressions from the
following components:

| Component | Example |
|---|---|
| Constants | `3` |
| Operators | `$add` |
| Field path expressions | `"$<path.to.field>"` |

For example, `{ $add: [ 3, "$inventory.total" ] }` is an expression
that consists of the `$add` operator and two operands:

- The constant `3`
- The field path expression
  `"$inventory.total"`

The expression returns the result of adding 3 to the value at path
`inventory.total` of the input document.

Expression operators take an array of arguments and have the following
form:

```javascript
{ <operator>: [ <argument1>, <argument2> ... ] }
```

If an operator accepts a single argument, you can omit the outer
array:

```javascript
{ <operator>: <argument> }
```

## Arithmetic Operators

Arithmetic expressions perform mathematic operations on numbers. Some
arithmetic expressions can also support date arithmetic.

| Name | Description |
|---|---|
| `$abs` | Returns the absolute value of a number. |
| `$add` | Adds numbers to return the sum, or adds numbers and a date to return a new date. If adding numbers and a date, treats the numbers as milliseconds. Accepts any number of argument expressions, but at most, one expression can evaluate to a date. |
| `$ceil` | Returns the smallest integer greater than or equal to the specified number. |
| `$divide` | Returns the result of dividing the first number by the second. Accepts two argument expressions. |
| `$exp` | Raises *e* to the specified exponent. |
| `$floor` | Returns the largest integer less than or equal to the specified number. |
| `$ln` | Calculates the natural log of a number. |
| `$log` | Calculates the log of a number in the specified base. |
| `$log10` | Calculates the log base 10 of a number. |
| `$mod` | Returns the remainder of the first number divided by the second. Accepts two argument expressions. |
| `$multiply` | Multiplies numbers to return the product. Accepts any number of argument expressions. |
| `$pow` | Raises a number to the specified exponent. |
| `$round` | Rounds a number to to a whole integer *or* to a specified decimal place. |
| `$sqrt` | Calculates the square root. |
| `$subtract` | Returns the result of subtracting the second value from the first. If the two values are numbers, return the difference. If the two values are dates, return the difference in milliseconds. If the two values are a date and a number in milliseconds, return the resulting date. Accepts two argument expressions. If the two values are a date and a number, specify the date argument first as it is not meaningful to subtract a date from a number. |
| `$trunc` | Truncates a number to a whole integer *or* to a specified decimal place. |

## Array Operators

| Name | Description |
|---|---|
| `$arrayElemAt` | Returns the element at the specified array index. |
| `$arrayToObject` | Converts an array of key value pairs to a document. |
| `$concatArrays` | Concatenates arrays to return the concatenated array. |
| `$filter` | Selects a subset of the array to return an array with only the elements that match the filter condition. |
| `$first` | Returns the first element of an array. Distinct from the `$first` accumulator. |
| `$firstN` | Returns a specified number of elements from the beginning of an array. Distinct from the `$firstN` accumulator. |
| `$in` | Returns a boolean indicating whether a specified value is in an array. |
| `$indexOfArray` | Searches an array for an occurrence of a specified value and returns the array index of the first occurrence. Array indexes start at zero. |
| `$isArray` | Determines if the operand is an array. Returns a boolean. |
| `$last` | Returns the last element of an array. Distinct from `$last` accumulator. |
| `$lastN` | Returns a specified number of elements from the end of an array. Distinct from the `$lastN` accumulator. |
| `$map` | Applies a subexpression to each element of an array and returns the array of resulting values in order. Accepts named parameters. |
| `$maxN` | Returns the `n` largest values in an array. Distinct from the `$maxN` accumulator. |
| `$minN` | Returns the `n` smallest values in an array. Distinct from the `$minN` accumulator. |
| `$objectToArray` | Converts a document to an array of documents representing key-value pairs. |
| `$range` | Outputs an array containing a sequence of integers according to user-defined inputs. |
| `$reduce` | Applies an expression to each element in an array and combines them into a single value. |
| `$reverseArray` | Returns an array with the elements in reverse order. |
| `$size` | Returns the number of elements in the array. Accepts a single expression as argument. |
| `$slice` | Returns a subset of an array. |
| `$sortArray` | Sorts the elements of an array. |
| `$zip` | Merge two arrays together. |

## Bitwise Operators

* - Name
  - Description

* - `$bitAnd`
  - Returns the result of a bitwise `and` operation on an array of 
    `int` or `long` values. 

    **New in version:** 6.3

* - `$bitNot`
  - Returns the result of a bitwise `not` operation on a single argument 
    or an array that contains a single `int` or `long` value. 

    **New in version:** 6.3

* - `$bitOr`
  - Returns the result of a bitwise `or` operation on an array of 
    `int` or `long` values. 

    **New in version:** 6.3

* - `$bitXor`
  - Returns the result of a bitwise `xor` (exclusive or) operation on an 
    array of `int` and `long` values.

    **New in version:** 6.3

## Boolean Operators

Boolean expressions evaluate their argument expressions as booleans and
return a boolean as the result.

In addition to the `false` boolean value, Boolean expression evaluates
as `false` the following: `null`, `0`, and `undefined`
values. The Boolean expression evaluates all other values as `true`,
including non-zero numeric values and arrays.

| Name | Description |
|---|---|
| `$and` | Returns `true` only when *all* its expressions evaluate to `true`. Accepts any number of argument expressions. |
| `$not` | Returns the boolean value that is the opposite of its argument expression. Accepts a single argument expression. |
| `$or` | Returns `true` when *any* of its expressions evaluates to `true`. Accepts any number of argument expressions. |

## Comparison Operators

Comparison expressions return a boolean except for `$cmp`
which returns a number.

The comparison expressions take two argument expressions and compare
both value and type, using the specified BSON comparison order for values of different types. Unlike the
inequality query predicates, the
comparison expressions do not use type bracketing.

| Name | Description |
|---|---|
| `$cmp` | Returns `0` if the two values are equivalent, `1` if the first value is greater than the second, and `-1` if the first value is less than the second. |
| `$eq` | Returns `true` if the values are equivalent. |
| `$gt` | Returns `true` if the first value is greater than the second. |
| `$gte` | Returns `true` if the first value is greater than or equal to the second. |
| `$lt` | Returns `true` if the first value is less than the second. |
| `$lte` | Returns `true` if the first value is less than or equal to the second. |
| `$ne` | Returns `true` if the values are *not* equivalent. |

## Conditional Operators

| Name | Description |
|---|---|
| `$cond` | A ternary operator that evaluates one expression, and depending on the result, returns the value of one of the other two expressions. Accepts either three expressions in an ordered list or three named parameters. |
| `$ifNull` | Returns either the non-null result of the first expression or the result of the second expression if the first expression results in a null result. Null result encompasses instances of undefined values or missing fields. Accepts two expressions as arguments. The result of the second expression can be null. |
| `$switch` | Evaluates a series of case expressions. When it finds an expression which evaluates to `true`, `$switch` executes a specified expression and breaks out of the control flow. |

## Custom Aggregation Operators

| Name | Description |
|---|---|
| `$accumulator` | Defines a custom accumulator function. |
| `$function` | Defines a custom function. |

## Data Size Operators

The following operators return the size of a data element:

| Name | Description |
|---|---|
| `$binarySize` | Returns the size of a given string or binary data value's content in bytes. |
| `$bsonSize` | Returns the size in bytes of a given document (i.e. bsontype `Object`) when encoded as BSON. |

## Date Operators

The following operators returns date objects or components of a date
object:

| Name | Description |
|---|---|
| `$dateAdd` | Adds a number of time units to a date object. |
| `$dateDiff` | Returns the difference between two dates. |
| `$dateFromParts` | Constructs a BSON Date object given the date's constituent parts. |
| `$dateFromString` | Converts a date/time string to a date object. |
| `$dateSubtract` | Subtracts a number of time units from a date object. |
| `$dateToParts` | Returns a document containing the constituent parts of a date. |
| `$dateToString` | Returns the date as a formatted string. |
| `$dateTrunc` | Truncates a date. |
| `$dayOfMonth` | Returns the day of the month for a date as a number between 1 and 31. |
| `$dayOfWeek` | Returns the day of the week for a date as a number between 1 (Sunday) and 7 (Saturday). |
| `$dayOfYear` | Returns the day of the year for a date as a number between 1 and 366 (leap year). |
| `$hour` | Returns the hour for a date as a number between 0 and 23. |
| `$isoDayOfWeek` | Returns the weekday number in ISO 8601 format, ranging from `1` (for Monday) to `7` (for Sunday). |
| `$isoWeek` | Returns the week number in ISO 8601 format, ranging from `1` to `53`. Week numbers start at `1` with the week (Monday through Sunday) that contains the year's first Thursday. |
| `$isoWeekYear` | Returns the year number in ISO 8601 format. The year starts with the Monday of week 1 (ISO 8601) and ends with the Sunday of the last week (ISO 8601). |
| `$millisecond` | Returns the milliseconds of a date as a number between 0 and 999. |
| `$minute` | Returns the minute for a date as a number between 0 and 59. |
| `$month` | Returns the month for a date as a number between 1 (January) and 12 (December). |
| `$second` | Returns the seconds for a date as a number between 0 and 60 (leap seconds). |
| `$toDate` | Converts value to a Date. |
| `$week` | Returns the week number for a date as a number between 0 (the partial week that precedes the first Sunday of the year) and 53 (leap year). |
| `$year` | Returns the year for a date as a number (e.g. 2014). |

The following arithmetic operators can take date operands:

| Name | Description |
|---|---|
| `$add` | Adds numbers and a date to return a new date. If adding numbers and a date, treats the numbers as milliseconds. Accepts any number of argument expressions, but at most, one expression can evaluate to a date. |
| `$subtract` | Returns the result of subtracting the second value from the first. If the two values are dates, return the difference in milliseconds. If the two values are a date and a number in milliseconds, return the resulting date. Accepts two argument expressions. If the two values are a date and a number, specify the date argument first as it is not meaningful to subtract a date from a number. |

## Expressions Associated with Accumulators

* - Name
  - Description

* - `$avg`
  - Returns the average of numeric array elements.

* - `$max`
  - Returns the maximum value from an array.

* - `$median`
  - Returns the median (50th percentile) of an array of
    numeric values.

    **New in version:** 7.0

* - `$min`
  - Returns the minimum value from an array.

* - `$percentile`
  - Returns one or more percentile values computed over an
    array of numbers.

    **New in version:** 7.0

* - `$stdDevPop`
  - Returns the population standard deviation of numeric
    values in an array.

## Literal Expression Operators

| Name | Description |
|---|---|
| `$literal` | Return a value without parsing. Use for values that the aggregation pipeline may interpret as an expression. For example, use a `$literal` expression to a string that starts with a  dollar sign (`$`) to avoid parsing as a field path. |

## Miscellaneous Operators

| Name | Description |
|---|---|
| `$getField` | Returns the value of a specified field from a document. You can use `$getField` to retrieve the value of fields with names that contain periods (`.`) or start with dollar signs (`$`). |
| `$rand` | Returns a random float between 0 and 1 |
| `$sampleRate` | Randomly select documents at a given rate. Although the exact number of documents selected varies on each run, the quantity chosen approximates the sample rate expressed as a percentage of the total number of documents. |
| `$toHashedIndexKey` | Computes and returns the hash of the input expression using the same hash function that MongoDB uses to create a hashed index. |

## Object Operators

* - Name
  - Description

* - `$mergeObjects`

  - Combines multiple documents into a single document.

* - `$objectToArray`

  - Converts a document to an array of documents representing
    key-value pairs.

* - `$setField`

  - Adds, updates, or removes a specified field in a document. You
    can use `$setField` to add, update,
    or remove fields with names that contain periods (`.`) or 
    start with dollar signs (`$`).

    **New in version:** 5.0

## Set Operators

Set expressions performs set operation on arrays, treating arrays as
sets. Set expressions ignores the duplicate entries in each input array
and the order of the elements.

If the set operation returns a set, the operation filters out
duplicates in the result to output an array that contains only unique
entries. The order of the elements in the output array is unspecified.

If a set contains a nested array element, the set expression does *not* descend
into the nested array but evaluates the array at top-level.

| Name | Description |
|---|---|
| `$allElementsTrue` | Returns `true` if *no* element of a set evaluates to `false`, otherwise, returns `false`. Accepts a single argument expression. |
| `$anyElementTrue` | Returns `true` if *any* elements of a set evaluate to `true`; otherwise, returns `false`. Accepts a single argument expression. |
| `$setDifference` | Returns a set with elements that appear in the first set but not in the second set; i.e. performs a [relative complement](http://en.wikipedia.org/wiki/Complement_(set_theory)) of the second set relative to the first. Accepts exactly two argument expressions. |
| `$setEquals` | Returns `true` if the input sets have the same distinct elements. Accepts two or more argument expressions. |
| `$setIntersection` | Returns a set with elements that appear in *all* of the input sets. Accepts any number of argument expressions. |
| `$setIsSubset` | Returns `true` if all elements of the first set appear in the second set, including when the first set equals the second set; i.e. not a [strict subset](http://en.wikipedia.org/wiki/Subset). Accepts exactly two argument expressions. |
| `$setUnion` | Returns a set with elements that appear in *any* of the input sets. |

## String Operators

   `$concat`, only have

String expressions, with the exception of a well-defined behavior for strings of ASCII characters.

`$concat` behavior is well-defined regardless of
the characters used.

| Name | Description |
|---|---|
| `$concat` | Concatenates any number of strings. |
| `$dateFromString` | Converts a date/time string to a date object. |
| `$dateToString` | Returns the date as a formatted string. |
| `$indexOfBytes` | Searches a string for an occurrence of a substring and returns the UTF-8 byte index of the first occurrence. If the substring is not found, returns `-1`. |
| `$indexOfCP` | Searches a string for an occurrence of a substring and returns the UTF-8 code point index of the first occurrence. If the substring is not found, returns `-1` |
| `$ltrim` | Removes whitespace or the specified characters from the beginning of a string. |
| `$regexFind` | Applies a regular expression (regex) to a string and returns information on the *first* matched substring. |
| `$regexFindAll` | Applies a regular expression (regex) to a string and returns information on the all matched substrings. |
| `$regexMatch` | Applies a regular expression (regex) to a string and returns a boolean that indicates if a match is found or not. |
| `$replaceOne` | Replaces the first instance of a matched string in a given input. |
| `$replaceAll` | Replaces all instances of a matched string in a given input. |
| `$rtrim` | Removes whitespace or the specified characters from the end of a string. |
| `$split` | Splits a string into substrings based on a delimiter. Returns an array of substrings. If the delimiter is not found within the string, returns an array containing the original string. |
| `$strLenBytes` | Returns the number of UTF-8 encoded bytes in a string. |
| `$strLenCP` | Returns the number of UTF-8 [code points](http://www.unicode.org/glossary/#code_point) in a string. |
| `$strcasecmp` | Performs case-insensitive string comparison and returns: `0` if two strings are equivalent, `1` if the first string is greater than the second, and `-1` if the first string is less than the second. |
| `$substr` | Deprecated. Use `$substrBytes` or `$substrCP`. |
| `$substrBytes` | Returns the substring of a string. Starts with the character at the specified UTF-8 byte index (zero-based) in the string and continues for the specified number of bytes. |
| `$substrCP` | Returns the substring of a string. Starts with the character at the specified UTF-8 [code point (CP)](http://www.unicode.org/glossary/#code_point) index (zero-based) in the string and continues for the number of code points specified. |
| `$toLower` | Converts a string to lowercase. Accepts a single argument expression. |
| `$toString` | Converts value to a string. |
| `$trim` | Removes whitespace or the specified characters from the beginning and end of a string. |
| `$toUpper` | Converts a string to uppercase. Accepts a single argument expression. |

## Text Operators

| Name | Description |
|---|---|
| `$meta` | Access available per-document metadata related to the aggregation operation. |

## Timestamp Operators

Timestamp expression operators return values from a timestamp.

* - Name
  - Description

* - `$tsIncrement`

  - .. include:: /includes/tsIncrement-introduction.rst

    **New in version:** 5.1

* - `$tsSecond`

  - .. include:: /includes/tsSecond-introduction.rst

    **New in version:** 5.1

## Trigonometry Operators

Trigonometry expressions perform trigonometric operations on numbers.
Values that represent angles are always input or output in  radians. Use
`$degreesToRadians` and `$radiansToDegrees` to
convert between degree and radian measurements.

| Name | Description |
|---|---|
| `$sin` | Returns the sine of a value that is measured in radians. |
| `$cos` | Returns the cosine of a value that is measured in radians. |
| `$tan` | Returns the tangent of a value that is measured in radians. |
| `$asin` | Returns the inverse sin (arc sine) of a value in radians. |
| `$acos` | Returns the inverse cosine (arc cosine) of a value in radians. |
| `$atan` | Returns the inverse tangent (arc tangent) of a value in radians. |
| `$atan2` | Returns the inverse tangent (arc tangent) of `y / x` in radians, where `y` and `x` are the first and second values passed to the expression respectively. |
| `$asinh` | Returns the inverse hyperbolic sine (hyperbolic arc sine) of a value in radians. |
| `$acosh` | Returns the inverse hyperbolic cosine (hyperbolic arc cosine) of a value in radians. |
| `$atanh` | Returns the inverse hyperbolic tangent (hyperbolic arc tangent) of a value in radians. |
| `$sinh` | Returns the hyperbolic sine of a value that is measured in radians. |
| `$cosh` | Returns the hyperbolic cosine of a value that is measured in radians. |
| `$tanh` | Returns the hyperbolic tangent of a value that is measured in radians. |
| `$degreesToRadians` | Converts a value from degrees to radians. |
| `$radiansToDegrees` | Converts a value from radians to degrees. |

## Type Operators

| Name | Description |
|---|---|
| `$convert` | Converts a value to a specified type. |
| `$isNumber` | Returns boolean `true` if the specified expression evaluates to an `integer`, `decimal`, `double`, or `long`. Returns boolean `false` if the expression evaluates to any other BSON type, `null`, or a missing field. |
| `$toBool` | Converts value to a boolean. |
| `$toDate` | Converts value to a Date. |
| `$toDecimal` | Converts value to a Decimal128. |
| `$toDouble` | Converts value to a double. |
| `$toInt` | Converts value to an integer. |
| `$toLong` | Converts value to a long. |
| `$toObjectId` | Converts value to an ObjectId. |
| `$toString` | Converts value to a string. |
| `$type` | Return the BSON data type of the field. |

## Variable Operators

| Name | Description |
|---|---|
| `$let` | Defines variables for use within the scope of a subexpression and returns the result of the subexpression. Accepts named parameters. Accepts any number of argument expressions. |

For operators used in the `$setWindowFields` stage, see
window-functions-ref.
