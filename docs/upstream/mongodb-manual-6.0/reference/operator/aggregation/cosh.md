<!-- Converted from reference/operator/aggregation/cosh.txt (reStructuredText). Includes are inlined. -->

# $cosh (aggregation)

**`$cosh`**

Returns the hyperbolic cosine of a value that is measured in radians.

`$cosh` has the following syntax:

```javascript
{ $cosh: <expression> }
```

`$cosh` takes any valid expression that resolves to a number, measured in
radians. If the expression returns a value in degrees, use the
`$degreesToRadians` operator to convert the value to
radians.

By default `$cosh` returns values as a `double`.
`$cosh` can also return values as a 128-bit decimal if the `<expression>` resolves to a 128-bit
decimal value. 

For more information on expressions, see 
aggregation-expressions.

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the input argument resolves to a value of `null` or refers to a
field that is missing, `$cosh` returns `null`. If the
argument resolves to `NaN`, `$cosh` returns `NaN`. If
the argument resolves to negative or positive `Infinity`,
`$cosh` returns positive `Infinity`.

| Example | Results |
|---|---|
| `{ $cosh: NaN }` | `NaN` |
| `{ $cosh: null }` | `null` |
| `{ $cosh: -Infinity }` | `Infinity` |
| `{ $cosh: Infinity }` | `Infinity` |

## Example

tabs:

  - id: degrees
    name: Hyperbolic Cosine in Degrees
    content: |

      The following `trigonometry` collection contains a document
      that stores an `angle` value measured in degrees:

      ```javascript
      db.trigonometry.insertOne(
         {
            "_id" : ObjectId( "5c50782193f833234ba90d85" ),
            "angle" : NumberDecimal( "53.1301023541559787031443874490659" )
         }
      )
      ```

      The following aggregation operation uses the
      `$cosh` expression to calculate the hyperbolic
      cosine of `angle` and adds it to the input document using the
      `$addFields` pipeline stage:

      ```javascript
      db.trigonometry.aggregate( [
         {
            $addFields : {
               "cosh_output" : { $cosh : { $degreesToRadians : "$angle" } }
            }
         }
      ] )
      ```

      The `$degreesToRadians` expression converts the
      `angle` in degrees to radians.

      Example output:

      ```javascript
      {
         "_id" : ObjectId("5c50782193f833234ba90d85"),
         "angle" : NumberDecimal("53.1301023541559787031443874490659"),
         "cosh_output" : NumberDecimal("1.461642741099671277595921778079396")
      }
      ```

      Because `angle` is stored as a 128-bit decimal, the `$cosh` output is also a
      128-bit decimal.

  - id: radians
    name: Hyperbolic Cosine in Radians
    content: |

      The following `trigonometry` collection contains a document
      that stores an `angle` value measured in radians:

      ```javascript
      db.trigonometry.insertOne(
         {
            "_id" : ObjectId( "5c50782193f833234ba90d15" ),
            "angle" : NumberDecimal( "1.6301023541559787031443874490659" )
         }
      )
      ```

      The following aggregation operation uses the
      `$cosh` expression to calculate the hyperbolic
      cosine of `angle` and adds it to the input document using
      the `$addFields` pipeline stage:

      ```javascript
      db.trigonometry.aggregate( [
         {
            $addFields : {
               "cosh_output" : { $cosh : "$angle" }
            }
         }
      ] )
      ```

      Example output:

      ```javascript
      {
         "_id" : ObjectId("5c50782193f833234ba90d15"),
         "angle" : NumberDecimal("1.6301023541559787031443874490659"),
         "cosh_output" : NumberDecimal("2.650153334504361016712328539738000")
      }
      ```

      Because `angle` is stored as a 128-bit decimal, the `$cosh` output is also
      a 128-bit decimal.
