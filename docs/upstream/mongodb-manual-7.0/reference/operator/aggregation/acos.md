<!-- Converted from reference/operator/aggregation/acos.txt (reStructuredText). Includes are inlined. -->

# $acos (expression operator)

**`$acos`**

Returns the inverse cosine (arc cosine) of a value.

`$acos` has the following syntax:

```javascript
{ $acos: <expression> }
```

`$acos` takes any valid expression that resolves to a number between `-1` 
and `1`, e.g. `-1 <= value <= 1`.

`$acos` returns values in radians. Use
`$radiansToDegrees` operator to convert the output value
from radians to degrees.

By default `$acos` returns values as a `double`. 
`$acos` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

If the argument resolves to a value of `null` or refers to a field
that is missing, `$acos` returns `null`. If the
argument resolves to `NaN`, `$acos` returns `NaN`.
If the argument resolves to a value outside the bounds of 
`[-1, 1]` inclusive, `$acos` throws an error.

* - Example
  - Results

* - `{ $acos: NaN }`
  - `NaN`

* - `{ $acos: null }`
  - `null`

* - `{ $acos : Infinity}` 

    *or* 

    `{ $acos : -Infinity }`
  - Throws an error message resembling the following formatted 
    output:

    ```bash
    "errmsg" : 
      "Failed to optimize pipeline :: caused by :: cannot 
      apply $acos to -inf, value must in [-1,1]"
    ```

## Example

tabs:

  - id: degrees
    name: Inverse Cosine of Value in Degrees
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
      `$acos` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $radiansToDegrees : {
                $acos : {
                  $divide : [ "$side_b", "$hypotenuse" ]
                }
              }
            }
          }
        }
      ])
      ```

      The `$radiansToDegrees` expression converts the
      radian value returned by `$acos` to the equivalent
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

      Since `side_b` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$acos` is a 128-bit decimal. 

  - id: radians
    name: Inverse Cosine of Value in Radians
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
      `$acos` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $acos : {
                $divide : [ "$side_b", "$hypotenuse" ]
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

      Since `side_b` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$acos` is a 128-bit decimal.
