<!-- Converted from reference/operator/aggregation/acosh.txt (reStructuredText). Includes are inlined. -->

# $acosh (expression operator)

**`$acosh`**

Returns the inverse hyperbolic cosine (hyperbolic arc cosine) of
a value.

`$acosh` has the following syntax:

```javascript
{ $acosh: <expression> }
```

`$acosh` takes any valid expression that resolves to a number  between `1` 
and `+Infinity`, e.g. `1 <= value <= +Infinity`.

`$acosh` returns values in radians. Use
`$radiansToDegrees` operator to convert the output value
from radians to degrees.

By default `$acosh` returns values as a `double`. 
`$acosh` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the argument resolves to a value of `null` or refers to a field
that is missing, `$acosh` returns `null`. If the argument
resolves to `NaN`, `$acosh` returns `NaN`. If the
argument resolves to negative infinity,  `$acosh` throws an
error. If the argument resolves to `Infinity`, `$acosh`
returns `Infinity`.  If the argument resolves to a value outside the
bounds of  `[-1, Infinity]` inclusive, `$acosh` throws an error.

* - Example
  - Results

* - `{ $acosh: NaN }`
  - `NaN`

* - `{ $acosh: null }`
  - `null`

* - `{ $acosh : Infinity}`
  - `Infinity`

* - `{ $acosh : 0 }`

  - Throws an error message resembling the following formatted 
    output:

    ```bash
    "errmsg" : 
      "Failed to optimize pipeline :: caused by :: cannot 
      apply $acosh to -inf, value must in (1,inf)"
    ```

## Example

tabs:

  - id: degrees
    name: Inverse Hyperbolic Cosine in Degrees
    content: |

      The `trigonometry` collection contains a document that
      stores a value along the `x` axis of a 2-D graph:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "x-coordinate" : Decimal128("3")
      }
      ```

      The following aggregation operation uses the
      `$acosh` expression to calculate inverse hyperbolic
      cosine of `x-coordinate` and add it to the input document using 
      the `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "y-coordinate" : {
              $radiansToDegrees : { $acosh : "$x-coordinate" }
            }
          }
        }
      ])
      ```

      The `$radiansToDegrees` expression converts the
      radian value returned by `$acosh` to the equivalent
      value in degrees.

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "x-coordinate" : Decimal128("3"),
        "y-coordinate" : Decimal128("100.9979734210524228844295260083432")
      }
      ```

      Since `x-coordinate` is stored as a
      128-bit decimal, the output of 
      `$acosh` is a 128-bit decimal. 

  - id: radians
    name: Inverse Hyperbolic Cosine in Radians
    content: |

      The `trigonometry` collection contains a document that
      stores a value along the `x` axis of a 2-D graph:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "x-coordinate" : Decimal128("3")
      }
      ```

      The following aggregation operation uses the
      `$acosh` expression to calculate inverse hyperbolic
      cosine of `x-coordinate` and add it to the input document using 
      the `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        { 
          $addFields : {
            "y-coordinate" : {
              $acosh : "$x-coordinate"
            }
          }
        }
      ])
      ```

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "x-coordinate" : Decimal128("3"),
        "y-coordinate" : Decimal128("1.762747174039086050465218649959585")
      }
      ```

      Since `x-coordinate` is stored as a
      128-bit decimal, the output of 
      `$acosh` is a 128-bit decimal.
