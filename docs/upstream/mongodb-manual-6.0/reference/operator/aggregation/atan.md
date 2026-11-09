<!-- Converted from reference/operator/aggregation/atan.txt (reStructuredText). Includes are inlined. -->

# $atan (aggregation)

**`$atan`**

Returns the inverse tangent (arc tangent) of a value.

`$atan` has the following syntax:

```javascript
{ $atan: <expression> }
```

`$atan` takes any valid expression that resolves to a number.

`$atan` returns values in radians. Use
`$radiansToDegrees` operator to convert the output value
from radians to degrees.

By default `$atan` returns values as a `double`. 
`$atan` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null` and `NaN`

If the argument resolves to a value of `null` or refers to a field
that is missing, `$atan` returns `null`. If the
argument resolves to `NaN`, `$tan` returns `NaN`.

| Example | Results |
|---|---|
| `{ $atan: NaN }` | `NaN` |
| `{ $atan: null }` | `null` |

## Example

tabs:

  - id: degrees
    name: Inverse Tangent of Value in Degrees
    content: |

      The `trigonometry` collection contains a document that
      stores three sides of a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : NumberDecimal("3"),
        "side_b" : NumberDecimal("4"),
        "hypotenuse" : NumberDecimal("5")
      }
      ```

      The following aggregation operation uses the
      `$atan` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $radiansToDegrees : {
                $atan : {
                  $divide : [ "$side_b", "$side_a" ]
                }
              }
            }
          }
        }
      ])
      ```

      The `$radiansToDegrees` expression converts the
      radian value returned by `$atan` to the equivalent
      value in degrees.

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : NumberDecimal("3"),
        "side_b" : NumberDecimal("4"),
        "hypotenuse" : NumberDecimal("5"),
        "angle_a" : NumberDecimal("53.13010235415597870314438744090658")
      }
      ```

      Since `side_b` and `side_a` are stored as 
      128-bit decimals, the output of 
      `$atan` is a 128-bit decimal. 

  - id: radians
    name: Inverse Tangent of Value in Radians
    content: |

      The `trigonometry` collection contains a document that
      stores three sides of a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : NumberDecimal("3"),
        "side_b" : NumberDecimal("4"),
        "hypotenuse" : NumberDecimal("5")
      }
      ```

      The following aggregation operation uses the
      `$atan` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $atan : {
                $divide : [ "$side_b", "$side_a" ]
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
        "side_a" : NumberDecimal("3"),
        "side_b" : NumberDecimal("4"),
        "hypotenuse" : NumberDecimal("5"),
        "angle_a" : NumberDecimal("0.9272952180016122324285124629224287")
      }
      ```

      Since `side_b` and `side_a` are stored as 
      128-bit decimals, the output of 
      `$atan` is a 128-bit decimal.
