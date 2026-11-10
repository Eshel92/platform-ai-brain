<!-- Converted from sql/functions/math.asciidoc (AsciiDoc). Includes are inlined. -->

### Mathematical Functions

All math and trigonometric functions require their input (where applicable)
to be numeric.

### Generic

#### `ABS`

**Synopsis:**
```sql
ABS(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: numeric

*Description*: Returns the [absolute value](https://en.wikipedia.org/wiki/Absolute_value) of `numeric_exp`. The return type is the same as the input type.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[abs]
```

#### `CBRT`

**Synopsis:**
```sql
CBRT(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [cube root](https://en.wikipedia.org/wiki/Cube_root) of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineCbrtWithNegativeValue]
```

#### `CEIL/CEILING`

**Synopsis:**
```sql
CEIL(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: integer or long numeric value

*Description*: Returns the smallest integer greater than or equal to `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineCeiling]
```

#### `E`

**Synopsis:**
```sql
E()
```

*Input*: _none_

*Output*: `2.718281828459045`

*Description*: Returns [Euler's number](https://en.wikipedia.org/wiki/E_%28mathematical_constant%29).

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathEulersNumber]
```

#### `EXP`

**Synopsis:**
```sql
EXP(numeric_exp) <1>
```

*Input*:

<1> float numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns [Euler's number at the power](https://en.wikipedia.org/wiki/Exponential_function) of `numeric_exp` e^numeric_exp^.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathExpInline]
```

#### `EXPM1`

**Synopsis:**
```sql
EXPM1(numeric_exp) <1>
```

*Input*:

<1> float numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns [Euler's number at the power](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#expm1-double-) of `numeric_exp` minus 1 (e^numeric_exp^ - 1).

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathExpm1Inline]
```

#### `FLOOR`

**Synopsis:**
```sql
FLOOR(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: integer or long numeric value

*Description*: Returns the largest integer less than or equal to `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineFloor]
```

#### `LOG`

**Synopsis:**
```sql
LOG(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm) of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineLog]
```

#### `LOG10`

**Synopsis:**
```sql
LOG10(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [base 10 logarithm](https://en.wikipedia.org/wiki/Common_logarithm) of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineLog10]
```

#### `PI`

**Synopsis:**
```sql
PI()
```

*Input*: _none_

*Output*: `3.141592653589793`

*Description*: Returns [PI number](https://en.wikipedia.org/wiki/Pi).

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathPINumber]
```

#### `POWER`

**Synopsis:**
```sql
POWER(
    numeric_exp, <1>
    integer_exp) <2>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.
<2> integer expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the value of `numeric_exp` to the power of `integer_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlinePowerPositive]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlinePowerNegative]
```

#### `RANDOM/RAND`

**Synopsis:**
```sql
RANDOM(seed) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns a random double using the given seed.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathRandom]
```

#### `ROUND`

**Synopsis:**
```sql
ROUND(
    numeric_exp      <1>
    [, integer_exp]) <2>
```
*Input*:

<1> numeric expression. If `null`, the function returns `null`.
<2> integer expression; optional. If `null`, the function returns `null`.

*Output*: numeric 

*Description*: Returns `numeric_exp` rounded to `integer_exp` places right of the decimal point. If `integer_exp` is negative,
`numeric_exp` is rounded to |`integer_exp`| places to the left of the decimal point. If `integer_exp` is omitted,
the function will perform as if `integer_exp` would be 0. The returned numeric data type is the same as the data type 
of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathRoundWithPositiveParameter]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathRoundWithNegativeParameter]
```

#### `SIGN/SIGNUM`

**Synopsis:**
```sql
SIGN(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: [-1, 0, 1]

*Description*: Returns an indicator of the sign of `numeric_exp`. If `numeric_exp` is less than zero, –1 is returned. If `numeric_exp` equals zero, 0 is returned. If `numeric_exp` is greater than zero, 1 is returned.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineSign]
```

#### `SQRT`

**Synopsis:**
```sql
SQRT(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns [square root](https://en.wikipedia.org/wiki/Square_root) of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineSqrt]
```

#### `TRUNCATE/TRUNC`

**Synopsis:**
```sql
TRUNCATE(
    numeric_exp      <1>
    [, integer_exp]) <2>
```
*Input*:

<1> numeric expression. If `null`, the function returns `null`.
<2> integer expression; optional. If `null`, the function returns `null`.

*Output*: numeric 

*Description*: Returns `numeric_exp` truncated to `integer_exp` places right of the decimal point. If `integer_exp` is negative,
`numeric_exp` is truncated to |`integer_exp`| places to the left of the decimal point. If `integer_exp` is omitted,
the function will perform as if `integer_exp` would be 0. The returned numeric data type is the same as the data type 
of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathTruncateWithPositiveParameter]
```

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathTruncateWithNegativeParameter]
```

### Trigonometric

#### `ACOS`

**Synopsis:**
```sql
ACOS(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [arccosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of `numeric_exp` as an angle, expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineAcos]
```

#### `ASIN`

**Synopsis:**
```sql
ASIN(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [arcsine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of `numeric_exp` as an angle, expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineAsin]
```

#### `ATAN`

**Synopsis:**
```sql
ATAN(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [arctangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of `numeric_exp` as an angle, expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineAtan]
```

#### `ATAN2`

**Synopsis:**
```sql
ATAN2(
    ordinate, <1>
    abscisa)  <2>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.
<2> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [arctangent of the `ordinate` and `abscisa` coordinates](https://en.wikipedia.org/wiki/Atan2) specified as an angle, expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineAtan2]
```

#### `COS`

**Synopsis:**
```sql
COS(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#cosine) of `numeric_exp`, where `numeric_exp` is an angle expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineCosine]
```

#### `COSH`

**Synopsis:**
```sql
COSH(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_function) of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineCosh]
```

#### `COT`

**Synopsis:**
```sql
COT(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [cotangent](https://en.wikipedia.org/wiki/Trigonometric_functions#Cosecant,_secant,_and_cotangent) of `numeric_exp`, where `numeric_exp` is an angle expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineCotangent]
```

#### `DEGREES`

**Synopsis:**
```sql
DEGREES(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Convert from [radians](https://en.wikipedia.org/wiki/Radian)
to [degrees](https://en.wikipedia.org/wiki/Degree_(angle)).

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineDegrees]
```

#### `RADIANS`

**Synopsis:**
```sql
RADIANS(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Convert from [degrees](https://en.wikipedia.org/wiki/Degree_(angle))
to [radians](https://en.wikipedia.org/wiki/Radian).

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineRadians]
```

#### `SIN`

**Synopsis:**
```sql
SIN(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [sine](https://en.wikipedia.org/wiki/Trigonometric_functions#sine) of `numeric_exp`, where `numeric_exp` is an angle expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineSine]
```

#### `SINH`

**Synopsis:**
```sql
SINH(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_function) of `numeric_exp`.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineSinh]
```

#### `TAN`

**Synopsis:**
```sql
TAN(numeric_exp) <1>
```

*Input*:

<1> numeric expression. If `null`, the function returns `null`.

*Output*: double numeric value

*Description*: Returns the [tangent](https://en.wikipedia.org/wiki/Trigonometric_functions#tangent) of `numeric_exp`, where `numeric_exp` is an angle expressed in radians.

```
include-tagged::{sql-specs}/docs/docs.csv-spec[mathInlineTanget]
```
