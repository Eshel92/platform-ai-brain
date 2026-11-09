<!-- Converted from reference/operator/aggregation/sinh.txt (reStructuredText). Includes are inlined. -->

# $sinh  (expression operator)

**`$sinh`**

Returns the hyperbolic sine of a value that is measured in radians.

`$sinh` has the following syntax:

```javascript
{ $sinh: <expression> }
```

`$sinh` takes any valid expression that resolves to a number, measured in
radians. If the expression returns a value in degrees, use the
`$degreesToRadians` operator to convert the value to
radians.

By default `$sinh` returns values as a `double`.
`$sinh` can also return values as a 128-bit decimal if the `<expression>` resolves to a 128-bit
decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the input argument resolves to a value of `null` or refers to a
field that is missing, `$sinh` returns `null`. If the
argument resolves to `NaN`, `$sinh` returns `NaN`. If
the argument resolves to negative or positive `Infinity`,
`$sinh` returns negative or positive `Infinity`
respectively.

| Example | Results |
|---|---|
| `{ $sinh: NaN }` | `NaN` |
| `{ $sinh: null }` | `null` |
| `{ $sinh: -Infinity }` | `-Infinity` |
| `{ $sinh: Infinity }` | `Infinity` |

## Example

tabs:

  - id: degrees
    name: Hyperbolic Sine of Value in Degrees
    content: |

      The following `trigonometry` collection contains a document
      that stores an `angle` value measured in degrees:

      ```javascript
      db.trigonometry.insertOne(
         {
            "_id" : ObjectId( "5c50782193f833234ba90d25" ),
            "angle" : Decimal128( "53.1301023541559787031443874490659" )
         }
      )
      ```

      The following aggregation operation uses the
      `$sinh` expression to calculate the hyperbolic sine
      of `angle` and adds it to the input document using the
      `$addFields` pipeline stage:

      ```javascript
      db.trigonometry.aggregate( [
         {
            $addFields : {
               "sinh_output" : { $sinh : { $degreesToRadians : "$angle" } }
            }
         }
      ] )
      ```

      The `$degreesToRadians` expression converts the
      `angle` in degrees to radians.

      Example output:

      ```javascript
      {
         "_id" : ObjectId("5c50782193f833234ba90d25"),
         "angle" : Decimal128("53.1301023541559787031443874490659"),
         "sinh_output" : Decimal128("1.066020404405732132503284522731829")
      }
      ```

      Because `angle` is stored as a 128-bit decimal, the `$sinh` output is also a
      128-bit decimal.

  - id: radians
    name: Hyperbolic Sine of Value in Radians
    content: |

      The following `trigonometry` collection contains a document
      that stores an `angle` value measured in radians:

      ```javascript
      db.trigonometry.insertOne(
         {
            "_id" : ObjectId( "5c50782193f833234ba90d35" ),
            "angle" : Decimal128( "1.6301023541559787031443874490659" )
         }
      )
      ```

      The following aggregation operation uses the
      `$sinh` expression to calculate the hyperbolic sine
      of `angle` and adds it to the input document using the
      `$addFields` pipeline stage:

      ```javascript
      db.trigonometry.aggregate( [
         {
            $addFields : {
               "sinh_output" : { $sinh : "$angle" }
            }
         }
      ] )
      ```

      Example output:

      ```javascript
      {
         "_id" : ObjectId("5c50782193f833234ba90d35"),
         "angle" : Decimal128("1.6301023541559787031443874490659"),
         "sinh_output" : Decimal128("2.454243813557362033961729701069671")
      }
      ```

      Because `angle` is stored as a 128-bit decimal, the `$sinh` output is also
      a 128-bit decimal.
