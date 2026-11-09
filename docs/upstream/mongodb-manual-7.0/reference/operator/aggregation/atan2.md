<!-- Converted from reference/operator/aggregation/atan2.txt (reStructuredText). Includes are inlined. -->

# $atan2 (expression operator)

**`$atan2`**

Returns the inverse tangent (arc tangent) of `y / x`,
where `y` and `x` are the first and second values passed to the
expression respectively.

`$atan2` has the following syntax:

```javascript
{ $atan2: [ <expression 1>, <expression 2> ] }
```

`$atan2` takes any valid expression that resolves to a number.

`$atan2` returns values in radians. Use
`$radiansToDegrees` operator to convert the output value
from radians to degrees.

By default `$atan2` returns values as a `double`. 
`$atan2` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null` and `NaN`

If either argument given to `$atan2` is `null`, the expression returns
`null`.  If either argument is `NaN`, the expression returns `NaN`.
If one argument is `null` and the other is `NaN`, the expression returns
`null`.

| Example | Results |
|---|---|
| `{ $atan2: [ NaN, <value> ] }` | `NaN` |
| `{ $atan2: [ <value>, NaN ] }` | `NaN` |
| `{ $atan2: [ null, <value> ] }` | `null` |
| `{ $atan2: [ <value>, null ] }` | `null` |
| `{ $atan2: [ NaN, null ] }` | `null` |
| `{ $atan2: [ null, NaN ] }` | `null` |

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
        "side_a" : Decimal128("3"),
        "side_b" : Decimal128("4"),
        "hypotenuse" : Decimal128("5")
      }
      ```

      The following aggregation operation uses the
      `$atan2` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $radiansToDegrees : {
                $atan2 : [ "$side_b", "$side_a" ]
              }
            }
          }
        }
      ])
      ```

      The `$radiansToDegrees` expression converts the
      radian value returned by `$atan2` to the equivalent
      value in degrees.

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "side_a" : Decimal128("3"),
        "side_b" : Decimal128("4"),
        "hypotenuse" : Decimal128("5"),
        "angle_a" : Decimal128("53.13010235415597870314438744090658")
      }
      ```

      Since `side_b` and `side_a` are stored as 
      128-bit decimals, the output of 
      `$atan2` is a 128-bit decimal. 

  - id: radians
    name: Inverse Tangent of Value in Radians
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
      `$atan2` expression to calculate the angle adjacent
      to `side_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "angle_a" : {
              $atan2 : [ "$side_b", "$side_a" ]
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
        "angle_a" : Decimal128("0.9272952180016122324285124629224287")
      }
      ```

      Since `side_b` and `side_a` are stored as 
      128-bit decimals, the output of 
      `$atan2` is a 128-bit decimal.
