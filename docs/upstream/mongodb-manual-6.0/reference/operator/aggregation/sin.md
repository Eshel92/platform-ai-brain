<!-- Converted from reference/operator/aggregation/sin.txt (reStructuredText). Includes are inlined. -->

# $sin (aggregation)

## Definition

**`$sin`**

Returns the sine of a value that is measured in radians.

`$sin` has the following syntax:

```javascript
{ $sin: <expression> }
```

`$sin` takes any valid expression that resolves to a number. If the
expression returns a value in degrees, use the
`$degreesToRadians` operator to convert the
result to radians.

By default `$sin` returns values as a `double`. 
`$sin` can also return values as a
128-bit decimal
as long as the `<expression>` resolves to a 128-bit decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the argument resolves to a value of `null` or refers to a field
that is missing, `$sin` returns `null`. If the
argument resolves to `NaN`, `$sin` returns `NaN`.
If the argument resolves to negative or positive infinity, 
`$sin` throws an error.

* - Example
  - Results

* - `{ $sin: NaN }`
  - `NaN`

* - `{ $sin: null }`
  - `null`

* - `{ $sin : Infinity}` 

    *or* 

    `{ $sin : -Infinity }`
  - Throws an error message resembling the following formatted 
    output:

    ```bash
    "errmsg" : 
      "Failed to optimize pipeline :: caused by :: cannot 
      apply $sin to -inf, value must in (-inf,inf)"
    ```

## Example

tabs:

  - id: degrees
    name: Sine of Value in Degrees
    content: |

      The `trigonometry` collection contains a document that
      stores the hypotenuse and one angle in a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "angle_a" : NumberDecimal("53.13010235415597870314438744090659"),
        "hypotenuse" : NumberDecimal("5")
      }
      ```

      The following aggregation operation uses the
      `$sin` expression to calculate the side opposite
      to `angle_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        {
          $addFields : {
            "side_b" : {
              $multiply : [
                { $sin : {$degreesToRadians : "$angle_a"} },
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
        "angle_a" : NumberDecimal("53.13010235415597870314438744090659"),
        "side_b" : NumberDecimal("4.000000000000000000000000000000000"),
        "hypotenuse" : NumberDecimal("5"),
      }
      ```

      Since `angle_a` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$sin` is a 128-bit decimal. 

  - id: radians
    name: Sine of Value in Radians
    content: |

      The `trigonometry` collection contains a document that
      stores the hypotenuse and one angle in a right-angle triangle:

      ```bash
      {
        "_id" : ObjectId("5c50782193f833234ba90d85"),
        "angle_a" : NumberDecimal("0.9272952180016122324285124629224288"),
        "hypotenuse" : NumberDecimal("5")
      }
      ```

      The following aggregation operation uses the
      `$sin` expression to calculate the side opposite
      to `angle_a` and add it to the input document using the 
      `$addFields` pipeline stage. 

      ```bash
      db.trigonometry.aggregate([
        {
          $addFields : {
            "side_b" : {
              $multiply : [
                { $sin : "$angle_a" },
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
        "angle_a" : NumberDecimal("0.9272952180016122324285124629224288"),
        "side_b" : NumberDecimal("4.000000000000000000000000000000000"),
        "hypotenuse" : NumberDecimal("5"),
      }
      ```

      Since `angle_a` and `hypotenuse` are stored as 
      128-bit decimals, the output of 
      `$sin` is a 128-bit decimal.
