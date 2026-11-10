<!-- Converted from sql/functions/string.asciidoc (AsciiDoc). Includes are inlined. -->

### String Functions

Functions for performing string manipulation.

#### `ASCII`

**Synopsis:**
```sql
ASCII(string_exp) <1>
```

*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Returns the ASCII code value of the leftmost character of `string_exp` as an integer.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringAscii]
```

#### `BIT_LENGTH`

**Synopsis:**
```sql
BIT_LENGTH(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Returns the length in bits of the `string_exp` input expression.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringBitLength]
```

#### `CHAR`

**Synopsis:**
```sql
CHAR(code) <1>
```
*Input*:

<1> integer expression between `0` and `255`. If `null`, negative, or greater
than `255`, the function returns `null`.

*Output*: string

*Description*: Returns the character that has the ASCII code value specified by the numeric input.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringChar]
```

#### `CHAR_LENGTH`

**Synopsis:**
```sql
CHAR_LENGTH(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Returns the length in characters of the input, if the string expression is of a character data type; otherwise, returns the length in bytes of the string expression (the smallest integer not less than the number of bits divided by 8).

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringCharLength]
```

#### `CONCAT`

**Synopsis:**
```sql
CONCAT(
    string_exp1, <1>
    string_exp2) <2>
```
*Input*:

<1> string expression. Treats `null` as an empty string.
<2> string expression. Treats `null` as an empty string.

*Output*: string

*Description*: Returns a character string that is the result of concatenating `string_exp1` to `string_exp2`.

The resulting string cannot exceed a byte length of 1 MB.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringConcat]
```

#### `INSERT`

**Synopsis:**
```sql
INSERT(
    source,      <1>
    start,       <2>
    length,      <3>
    replacement) <4>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> integer expression. If `null`, the function returns `null`.
<3> integer expression. If `null`, the function returns `null`.
<4> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns a string where `length` characters have been deleted from `source`, beginning at `start`, and where `replacement` has been inserted into `source`, beginning at `start`.

The resulting string cannot exceed a byte length of 1 MB.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringInsert]
```

#### `LCASE`

**Synopsis:**
```sql
LCASE(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns a string equal to that in `string_exp`, with all uppercase characters converted to lowercase.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringLCase]
```

#### `LEFT`

**Synopsis:**
```sql
LEFT(
    string_exp, <1>
    count)      <2>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> integer expression. If `null`, the function returns `null`. If `0` or
negative, the function returns an empty string.

*Output*: string

*Description*: Returns the leftmost count characters of `string_exp`.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringLeft]
```

#### `LENGTH`

**Synopsis:**
```sql
LENGTH(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Returns the number of characters in `string_exp`, excluding trailing blanks.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringLength]
```

#### `LOCATE`

**Synopsis:**
```sql
LOCATE(
    pattern, <1>
    source   <2>
    [, start]<3>
)
```
*Input*:

<1> string expression.  If `null`, the function returns `null`.
<2> string expression.  If `null`, the function returns `null`.
<3> integer expression; optional. If `null`, `0`, `1`, negative, or not
specified, the search starts at the first character position.

*Output*: integer

*Description*: Returns the starting position of the first occurrence of
`pattern` within `source`. The optional `start` specifies the character position
to start the search with. If the `pattern` is not found within `source`, the
function returns `0`.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringLocateWoStart]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringLocateWithStart]
```

#### `LTRIM`

**Synopsis:**
```sql
LTRIM(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns the characters of `string_exp`, with leading blanks removed.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringLTrim]
```

#### `OCTET_LENGTH`

**Synopsis:**
```sql
OCTET_LENGTH(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Returns the length in bytes of the `string_exp` input expression.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringOctetLength]
```

#### `POSITION`

**Synopsis:**
```sql
POSITION(
    string_exp1, <1>
    string_exp2) <2>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> string expression. If `null`, the function returns `null`.

*Output*: integer

*Description*: Returns the position of the `string_exp1` in `string_exp2`. The result is an exact numeric.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringPosition]
```

#### `REPEAT`

**Synopsis:**
```sql
REPEAT(
    string_exp, <1>
    count)      <2>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> integer expression. If `0`, negative, or `null`, the function returns `null`.

*Output*: string

*Description*: Returns a character string composed of `string_exp` repeated `count` times.

The resulting string cannot exceed a byte length of 1 MB.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringRepeat]
```

#### `REPLACE`

**Synopsis:**
```sql
REPLACE(
    source,      <1>
    pattern,     <2>
    replacement) <3>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> string expression. If `null`, the function returns `null`.
<3> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Search `source` for occurrences of `pattern`, and replace with `replacement`.

The resulting string cannot exceed a byte length of 1 MB.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringReplace]
```

#### `RIGHT`

**Synopsis:**
```sql
RIGHT(
    string_exp, <1>
    count)      <2>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> integer expression. If `null`, the function returns `null`. If `0` or
negative, the function returns an empty string.

*Output*: string

*Description*: Returns the rightmost count characters of `string_exp`.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringRight]
```

#### `RTRIM`

**Synopsis:**
```sql
RTRIM(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns the characters of `string_exp` with trailing blanks removed.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringRTrim]
```

#### `SPACE`

**Synopsis:**
```sql
SPACE(count) <1>
```
*Input*:

<1> integer expression. If `null` or negative, the function returns `null`.

*Output*: string

*Description*: Returns a character string consisting of `count` spaces.

The resulting string cannot exceed a byte length of 1 MB.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringSpace]
```

#### `STARTS_WITH`

**Synopsis:**
```sql
STARTS_WITH(
    source,   <1>
    pattern)  <2>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> string expression. If `null`, the function returns `null`.

*Output*: boolean value

*Description*: Returns `true` if the source expression starts with the specified
pattern, `false` otherwise. The matching is case sensitive.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringStartsWithTrue]
```

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringStartsWithFalse]
```

#### `SUBSTRING`

**Synopsis:**
```sql
SUBSTRING(
    source, <1>
    start,  <2>
    length) <3>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.
<2> integer expression. If `null`, the function returns `null`.
<3> integer expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns a character string that is derived from `source`, beginning at the character position specified by `start` for `length` characters.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringSubString]
```

#### `TRIM`

**Synopsis:**
```sql
TRIM(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns the characters of `string_exp`, with leading and trailing blanks removed.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringTrim]
```

#### `UCASE`

**Synopsis:**
```sql
UCASE(string_exp) <1>
```
*Input*:

<1> string expression. If `null`, the function returns `null`.

*Output*: string

*Description*: Returns a string equal to that of the input, with all lowercase characters converted to uppercase.

```sql
include-tagged::{sql-specs}/docs/docs.csv-spec[stringUCase]
```
