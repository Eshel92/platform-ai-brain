<!-- Converted from reference/operator/aggregation/asin.txt (reStructuredText). Includes are inlined. -->

# $asin (expression operator)

**`$asin`**

Returns the inverse sine (arc sine) of a value.

`$asin` has the following syntax:

```javascript
{ $asin: <expression> }
```

`$asin` takes any valid expression that resolves to a number between `-1`
and `1`, e.g. `-1 <= value <= 1`.

`$asin` returns values in radians. Use
`$radiansToDegrees` operator to convert the output value
from radians to degrees.

By default `$asin` returns values as a `double`. 
`$asin` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

If the argument resolves to a value of `null` or refers to a field
that is missing, `$asin` returns `null`. If the
argument resolves to `NaN`, `$asin` returns `NaN`.
If the argument resolves to a value outside the bounds of 
`[-1, 1]` inclusive, `$asin` throws an error.

* - Example
  - Results

* - `{ $asin: NaN }`
  - `NaN`

* - `{ $asin: null }`
  - `null`

* - `{ $asin : Infinity}` 

    *or* 

    `{ $asin : -Infinity }`
  - Throws an error message resembling the following formatted 
    output:

    ```bash
    "errmsg" : 
      "Failed to optimize pipeline :: caused by :: cannot 
      apply $asin to -inf, value must in [-1,1]"
    ```

## Example

tabs:

  - id: degrees
    name: Inverse Sine of Value in Degrees
    content: |

      The `trigonometry` collection contains a document that
      stores three sides of a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : Decimal128("3"),
        "side_b" : Decimal128("4"),
        "hypotenuse" : Decimal128("5")
      }
      ```

      The following aggregation operation uses the
      `$asin` expression to calculate the angle opposite
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $radiansToDegrees : {
                $asin : {
                  $divide : [ "$side_a", "$hypotenuse" ]
                }
              }
            }
          }
        }
      ])
      ```

      The `$radiansToDegrees` expression converts the
      radian value returned by `$asin` to the equivalent
      value in degrees.

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : Decimal128("3"),
        "side_b" : Decimal128("4"),
        "hypotenuse" : Decimal128("5"),
        "angle_a" : Decimal128("36.86989764584402129685561255909341")
      }
      ```

      Since `side_a` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$asin` is a 128-bit decimal. 

  - id: radians
    name: Inverse Sine of Value in Radians
    content: |

      The `trigonometry` collection contains a document that
      stores three sides of a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : Decimal128("3"),
        "side_b" : Decimal128("4"),
        "hypotenuse" : Decimal128("5")
      }
      ```

      The following aggregation operation uses the
      `$asin` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $asin : {
                $divide : [ "$side_a", "$hypotenuse" ]
              }
            }
          }
        }
      ])
      ```

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : Decimal128("3"),
        "side_b" : Decimal128("4"),
        "hypotenuse" : Decimal128("5"),
        "angle_a" : Decimal128("0.6435011087932843868028092287173226")
      }
      ```

      Since `side_a` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$asin` is a 128-bit decimal.
