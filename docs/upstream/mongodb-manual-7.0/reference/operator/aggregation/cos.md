<!-- Converted from reference/operator/aggregation/cos.txt (reStructuredText). Includes are inlined. -->

# $cos (expression operator)

## Definition

**`$cos`**

Returns the cosine of a value that is measured in radians.

`$cos` has the following syntax:

```javascript
{ $cos: <expression> }
```

`$cos` takes any valid expression that resolves to a number. If the
expression returns a value in degrees, use the
`$degreesToRadians` operator to convert the
result to radians.

By default `$cos` returns values as a `double`. 
`$cos` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the argument resolves to a value of `null` or refers to a field
that is missing, `$cos` returns `null`. If the
argument resolves to `NaN`, `$cos` returns `NaN`.
If the argument resolves to negative or positive infinity, 
`$cos` throws an error.

* - Example
  - Results

* - `{ $cos: NaN }`
  - `NaN`

* - `{ $cos: null }`
  - `null`

* - `{ $cos : Infinity}` 

    *or* 

    `{ $cos : -Infinity }`

  - Throws an error message resembling the following formatted 
    output:

    ```bash
    "errmsg" : 
      "Failed to optimize pipeline :: caused by :: cannot 
      apply $cos to -inf, value must in (-inf,inf)"
    ```

## Example

tabs:

  - id: degrees
    name: Cosine of Value in Degrees
    content: |

      The `trigonometry` collection contains a document that
      stores the hypotenuse and one angle in a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "angle_a" : Decimal128("53.13010235415597870314438744090659"),
        "hypotenuse" : Decimal128("5")
      }
      ```

      The following aggregation operation uses the
      `$cos` expression to calculate the side adjacent
      to `angle_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        {
          $addFields : {
            "side_a" : {
              $multiply : [
                { $cos : {$degreesToRadians : "$angle_a"} },
                "$hypotenuse"
              ]
            }
          }
        }
      ])
      ```

      The `$degreesToRadians` expression converts the 
      degree value of `angle_a` to the equivalent value in radians.

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "angle_a" : Decimal128("53.13010235415597870314438744090659"),
        "side_a" : Decimal128("2.999999999999999999999999999999999"),
        "hypotenuse" : Decimal128("5"),
      }
      ```

      Since `angle_a` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$cos` is a 128-bit decimal. 

  - id: radians
    name: Cosine of Value in Radians
    content: |

      The `trigonometry` collection contains a document that
      stores the hypotenuse and one angle in a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "angle_a" : Decimal128("0.9272952180016122324285124629224288"),
        "hypotenuse" : Decimal128("5")
      }
      ```

      The following aggregation operation uses the
      `$cos` expression to calculate the side adjacent
      to `angle_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        {
          $addFields : {
            "side_b" : {
              $multiply : [
                { $cos : "$angle_a" },
                "$hypotenuse"
              ]
            }
          }
        }
      ])
      ```

      The command returns the following output:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "angle_a" : Decimal128("0.9272952180016122324285124629224288"),
        "side_b" : Decimal128("3.000000000000000000000000000000000"),
        "hypotenuse" : Decimal128("5"),
      }
      ```

      Since `angle_a` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$cos` is a 128-bit decimal.
