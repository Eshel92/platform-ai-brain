<!-- Converted from reference/operator/aggregation/regexMatch.txt (reStructuredText). Includes are inlined. -->

# $regexMatch (aggregation)

## Definition

**`$regexMatch`**

Performs a regular expression (regex) pattern matching and returns:

- `true`  if a match exists.

- `false` if a match doesn't exist.

MongoDB uses Perl compatible regular expressions (i.e. "PCRE" )
version 8.41 with UTF-8 support.

## Syntax

The `$regexMatch` operator has the following syntax:

```javascript
{ $regexMatch: { input: <expression> , regex: <expression>, options: <expression> } }
```

* - Field
  - Description

* - input

  - .. _regexMatch-input:

    The string on which you wish to apply the regex pattern.
    Can be a string or any valid expression that resolves to a string.

* - regex

  - .. _regexMatch-regex:

    The regex pattern to apply. Can be any valid expression that resolves to either a string or regex
    pattern `/<pattern>/`. When using the regex `/<pattern>/`, you
    can also specify the regex options `i` and `m` (but not the
    `s` or `x` options):

    - `"pattern"`

    - `/<pattern>/`

    - `/<pattern>/<options>` 

    Alternatively, you can also specify the regex options with the
    options field. To specify the `s` or `x` options, you
    must use the options field.

    You cannot specify options in both the `regex` and the `options`
    field.

* - options

  - .. _regexMatch-options:

    *Optional*. The following `<options>` are available for use
    with regular expression.

    You cannot specify options in both the `regex` and the `options` field.

    | Option | Description |
    |---|---|
    | `i` | Case insensitivity to match both upper and lower cases. You can specify the option in the `options` field or as part of the regex field. |
    | `m` | For patterns that include anchors (i.e. `^` for the start, `$` for the end), match at the beginning or end of each line for strings with multiline values. Without this option, these anchors match at beginning or end of the string. If the pattern contains no anchors or if the string value has no newline characters (e.g. `\n`), the `m` option has no effect. |
    | `x` | "Extended" capability to ignore all white space characters in the pattern unless escaped or included in a character class. Additionally, it ignores characters in-between and including an un-escaped hash/pound (`#`) character and the next new line, so that you may include comments in complicated patterns. This only applies to data characters; white space characters may never appear within special character sequences in a pattern. The `x` option does not affect the handling of the VT character (i.e. code 11). You can specify the option only in the `options` field. |
    | `s` | Allows the dot character (i.e. `.`) to match all characters *including* newline characters. You can specify the option only in the `options` field. |

### Returns

The operator returns a boolean:

- `true` if a match exists.

- `false` if a match doesn't exist.

**See also:**

- `$regexFind`
- `$regexFindAll`

## Behavior

### $regexMatch and Collation

String matching for `$regexMatch` is always case-sensitive and
diacritic-sensitive. `$regexMatch` ignores the collation specified
for the collection, `db.collection.aggregate()`, and the index,
if used.

For example, create a collection with collation strength
`1`, meaning the collation only compares base characters and ignores
differences such as case and diacritics:

```javascript
db.createCollection( "restaurants", { collation: { locale: "fr", strength: 1 } } )
```

Insert the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The following uses the collection's collation to perform a
case-insensitive and diacritic-insensitive match:

```javascript
db.restaurants.aggregate( [ { $match: { category: "cafe" } } ] )
```

Output:

```javascript
[
   { _id: 1, category: 'café', status: 'Open' },
   { _id: 2, category: 'cafe', status: 'open' },
   { _id: 3, category: 'cafE', status: 'open' }
]
```

However, `$regexMatch` ignores collation. The following regular
expression pattern matching examples are case-sensitive and diacritic
sensitive:

```javascript
db.restaurants.aggregate( [
   {
      $addFields: { 
         resultObject: { $regexMatch: { input: "$category", regex: /cafe/ } }
      }
   }
] )

db.restaurants.aggregate( [
   {
      $addFields: {
         resultObject: { $regexMatch: { input: "$category", regex: /cafe/ } }
      }
   }
], 
   { collation: { locale: "fr", strength: 1 } } // Ignored in the $regexMatch
)
```

Both operations return the following:

```javascript
{ "_id" : 1, "category" : "café", "resultObject" : null }
{ "_id" : 2, "category" : "cafe", "resultObject" : { "match" : "cafe", "idx" : 0, "captures" : [ ] } }
{ "_id" : 3, "category" : "cafE", "resultObject" : null }
```

Because the query ignores the collation, it requires an exact match on
the `category` string (including case and accent marks), meaning only
document `_id: 2` is matched.

To perform a case-insensitive regex pattern matching, use the
regexMatch-example-i-options instead. See
regexMatch-example-i-options for an example.

## Examples

### `$regexMatch` and Its Options

To illustrate the behavior of the `$regexMatch` operator as
discussed in this example, create a sample collection `products` with
the following documents:

```javascript
db.products.insertMany([
   { _id: 1, description: "Single LINE description." },
   { _id: 2, description: "First lines\nsecond line" },
   { _id: 3, description: "Many spaces before     line" },
   { _id: 4, description: "Multiple\nline descriptions" },
   { _id: 5, description: "anchors, links and hyperlinks" },
   { _id: 6, description: "métier work vocation" }
])
```

By default, `$regexMatch` performs a case-sensitive match.
For example, the following aggregation performs a case-*sensitive*
`$regexMatch` on the `description` field. The regex
pattern `/line/` does not specify any grouping:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /line/ } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : false }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

   

The following regex pattern `/lin(e|k)/` specifies a grouping
`(e|k)` in the pattern:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /lin(e|k)/ } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : true }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

#### `i` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To perform case-*insensitive* pattern matching, include the i option as part of the regex field or in the options
field:

```javascript
// Specify i as part of the regex field
{ $regexMatch: { input: "$description", regex: /line/i } }

// Specify i in the options field
{ $regexMatch: { input: "$description", regex: /line/, options: "i" } }
{ $regexMatch: { input: "$description", regex: "line", options: "i" } }
```

For example, the following aggregation performs a case-*insensitive*
`$regexMatch` on the `description` field. The regex
pattern `/line/` does not specify any grouping:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /line/i } } } }
])
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : true }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : false }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

#### `m` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To match the specified anchors (e.g. `^`, `$`) for each line of a
multiline string, include the m option
as part of the regex field or in the
options field:

```javascript
// Specify m as part of the regex field
{ $regexMatch: { input: "$description", regex: /line/m } }

// Specify m in the options field
{ $regexMatch: { input: "$description", regex: /line/, options: "m" } }
{ $regexMatch: { input: "$description", regex: "line", options: "m" } }
```

The following example includes both the `i` and the `m` options to
match lines starting with either the letter `s` or `S` for
multiline strings:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /^s/im } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : true }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : false }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : false }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : false }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

#### `x` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To ignore all unescaped white space characters and comments (denoted by
the un-escaped hash `#` character and the next new-line character) in
the pattern, include the s option in the
options field:

```javascript
// Specify x in the options field
{ $regexMatch: { input: "$description", regex: /line/, options: "x" } }
{ $regexMatch: { input: "$description", regex: "line", options: "x" } }
```

The following example includes the `x` option to skip unescaped white
spaces and comments:

```javascript
db.products.aggregate([
   { $addFields: { returns: { $regexMatch: { input: "$description", regex: /lin(e|k) # matches line or link/, options:"x" } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returns" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "returns" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "returns" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returns" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returns" : true }
{ "_id" : 6, "description" : "métier work vocation", "returns" : false }
```

#### `s` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To allow the dot character (i.e. `.`) in the pattern to match all
characters including the new line character, include the s option in the options field:

```javascript
// Specify s in the options field
{ $regexMatch: { input: "$description", regex: /m.*line/, options: "s" } }
{ $regexMatch: { input: "$description", regex: "m.*line", options: "s" } }
```

The following example includes the `s` option to allow the dot
character (i.e. .) to match all characters including new line as well
as the `i` option to perform a case-insensitive match:

```javascript
db.products.aggregate([
   { $addFields: { returns: { $regexMatch: { input: "$description", regex:/m.*line/, options: "si"  } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returns" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "returns" : false }
{ "_id" : 3, "description" : "Many spaces before     line", "returns" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returns" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returns" : false }
{ "_id" : 6, "description" : "métier work vocation", "returns" : false }
```

### Use `$regexMatch` to Check Email Address

Create a sample collection `feedback` with the following documents:

```javascript
db.feedback.insertMany([
   { "_id" : 1, comment: "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com"  },
   { "_id" : 2, comment: "I wanted to concatenate a string" },
   { "_id" : 3, comment: "How do I convert a date to string? Contact me at either cam@mongodb.com or c.dia@mongodb.com" },
   { "_id" : 4, comment: "It's just me. I'm testing.  fred@MongoDB.com" }
])
```

   
The following aggregation uses the `$regexMatch` to check
if the `comment` field contains an email address with
`@mongodb.com` and categorize the feedback as `Employee` or
`External`.

```javascript
db.feedback.aggregate( [ 
    { $addFields: { 
       "category": { $cond: { if:  { $regexMatch: { input: "$comment", regex: /[a-z0-9_.+-]+@mongodb.com/i } },
                              then: "Employee",
                              else: "External" } }
    } },
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "comment" : "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com", "category" : "External" }
{ "_id" : 2, "comment" : "I wanted to concatenate a string", "category" : "External" }
{ "_id" : 3, "comment" : "How do I convert a date to string? Contact me at either cam@mongodb.com or c.dia@mongodb.com", "category" : "Employee" }
{ "_id" : 4, "comment" : "It's just me. I'm testing.  fred@MongoDB.com", "category" : "Employee" }
```
