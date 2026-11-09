<!-- Converted from reference/operator/aggregation/regexFind.txt (reStructuredText). Includes are inlined. -->

# $regexFind (expression operator)

## Definition

**`$regexFind`**

Provides regular expression (regex) pattern matching capability in
aggregation expressions. If a match is found, returns a document
that contains information on the *first* match. If a match is not
found, returns null.

## Syntax

The `$regexFind` operator has the following syntax:

```javascript
{ $regexFind: { input: <expression> , regex: <expression>, options: <expression> } }
```

### Operator Fields

* - Field
  - Description

* - input

  - .. _regexFind-input:

    The string on which you wish to apply the regex pattern.
    Can be a string or any valid expression that resolves to a string.

* - regex

  - .. _regexFind-regex:

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

  - .. _regexFind-options:

    *Optional*. The following `<options>` are available for use
    with regular expression.

    You cannot specify options in both the `regex` and the
    `options` field.

    - `i`: Case insensitivity to match both upper and lower cases.
      You can specify the option in the `options` field or as part
      of the regex field.

    - `m`: For patterns that include anchors (that is, `^` for
      the start, `$` for the end), match at the beginning or end
      of each line for strings with multiline values. Without this
      option, these anchors match at beginning or end of the string.

      If the pattern contains no anchors or if the string value has
      no newline characters (e.g. `\n`), the `m` option has no
      effect.

    - `x`: "Extended" capability to ignore all white space
      characters in the pattern unless escaped or included in a
      character class.

      Additionally, it ignores characters in-between and including
      an un-escaped hash/pound (`#`) character and the next new
      line, so that you may include comments in complicated
      patterns. This only applies to data characters; white space
      characters may never appear within special character
      sequences in a pattern.

      The `x` option does not affect the handling of the VT
      character (code 11).

      You can specify the option only in the `options` field.

    - `s`: Allows the dot character (`.`) to match all
      characters *including* newline characters.

      You can specify the option only in the `options` field.

### Returns

If the operator does not find a match, the result of the operator is a
`null`.

If the operator finds a match, the result of the operator is a document
that contains:

- the *first* matching string in the input, 

- the [code point](http://www.unicode.org/glossary/#code_point) index
  (not byte index) of the matching string in the input, and

- An array of the strings that corresponds to the groups captured by
  the matching string. Capturing groups are specified with
  unescaped parenthesis `()` in the regex
  pattern.

```javascript
{ "match" : <string>, "idx" : <num>, "captures" : <array of strings> }
```

**See also:**

- `$regexFindAll`
- `$regexMatch`

## Behavior

### PCRE Library

Starting in version 6.1, MongoDB uses the PCRE2 (Perl Compatible Regular Expressions) library to
implement regular expression pattern matching. To learn more about
PCRE2, see the [PCRE Documentation](https://www.pcre.org/current/doc/html/).

### $regexFind and Collation

String matching for `$regexFind` is always case-sensitive and
diacritic-sensitive. `$regexFind` ignores the collation specified
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

However, `$regexFind` ignores collation. The following regular
expression pattern matching examples are case-sensitive and diacritic
sensitive:

```javascript
db.restaurants.aggregate( [
   {
      $addFields: { 
         resultObject: { $regexFind: { input: "$category", regex: /cafe/ } }
      }
   }
] )

db.restaurants.aggregate( [
   {
      $addFields: {
         resultObject: { $regexFind: { input: "$category", regex: /cafe/ } }
      }
   }
], 
   { collation: { locale: "fr", strength: 1 } } // Ignored in the $regexFind
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
regexFind-example-i-options instead. See
regexFind-example-i-options for an example.

### `captures` Output Behavior

If your regex pattern contains capture groups
and the pattern finds a match in the input, the
`captures` array in the results corresponds to the groups captured by
the matching string. Capture groups are specified with unescaped
parentheses `()` in the regex pattern. The
length of the `captures` array equals the number of capture groups in
the pattern and the order of the array matches the order in which the
capture groups appear.

Create a sample collection named `contacts` with the following
documents:

```javascript
db.contacts.insertMany([
  { "_id": 1, "fname": "Carol", "lname": "Smith", "phone": "718-555-0113" },
  { "_id": 2, "fname": "Daryl", "lname": "Doe", "phone": "212-555-8832" },
  { "_id": 3, "fname": "Polly", "lname": "Andrews", "phone": "208-555-1932" },
  { "_id": 4, "fname": "Colleen", "lname": "Duncan", "phone": "775-555-0187" },
  { "_id": 5, "fname": "Luna", "lname": "Clarke", "phone": "917-555-4414" }
])
```

The following pipeline applies the regex
pattern `/(C(ar)*)ol/` to the `fname` field:

```javascript
db.contacts.aggregate([
  {
    $project: {
      returnObject: {
        $regexFind: { input: "$fname", regex: /(C(ar)*)ol/ }
      }
    }
  }
])
```

The regex pattern finds a match with `fname`
values `Carol` and `Colleen`:

```javascript
{ "_id" : 1, "returnObject" : { "match" : "Carol", "idx" : 0, "captures" : [ "Car", "ar" ] } }
{ "_id" : 2, "returnObject" : null }
{ "_id" : 3, "returnObject" : null }
{ "_id" : 4, "returnObject" : { "match" : "Col", "idx" : 0, "captures" : [ "C", null ] } }
{ "_id" : 5, "returnObject" : null }
```

The pattern contains the capture group `(C(ar)*)` which contains the
nested group `(ar)`. The elements in the `captures` array correspond
to the two capture groups. If a matching document is not captured by a
group (e.g. `Colleen` and the group `(ar)`),
`$regexFind` replaces the group with a null placeholder.

As shown in the previous example, the `captures` array contains an
element for each capture group (using `null` for non-captures).
Consider the following example which searches for phone numbers with
New York City area codes by applying a logical `or` of capture
groups to the `phone` field. Each group represents a New York City
area code:

```javascript
db.contacts.aggregate([
  {
    $project: {
      nycContacts: {
        $regexFind: { input: "$phone", regex: /^(718).*|^(212).*|^(917).*/ }
      }
    }
  }
])
```

For documents which are matched by the regex
pattern, the `captures` array includes the matching capture group
and replaces any non-capturing groups with `null`:

```javascript
{ "_id" : 1, "nycContacts" : { "match" : "718-555-0113", "idx" : 0, "captures" : [ "718", null, null ] } }
{ "_id" : 2, "nycContacts" : { "match" : "212-555-8832", "idx" : 0, "captures" : [ null, "212", null ] } }
{ "_id" : 3, "nycContacts" : null }
{ "_id" : 4, "nycContacts" : null }
{ "_id" : 5, "nycContacts" : { "match" : "917-555-4414", "idx" : 0, "captures" : [ null, null, "917" ] } }
```

## Examples

### `$regexFind` and Its Options

To illustrate the behavior of the `$regexFind` operator as
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

By default, `$regexFind` performs a case-sensitive match.
For example, the following aggregation performs a case-*sensitive*
`$regexFind` on the `description` field. The regex
pattern `/line/` does not specify any grouping:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex: /line/ } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : null }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : { "match" : "line", "idx" : 6, "captures" : [ ] } }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : { "match" : "line", "idx" : 23, "captures" : [ ] } }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : { "match" : "line", "idx" : 9, "captures" : [ ] } }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : null }
{ "_id" : 6, "description" : "métier work vocation", "returnObject" : null }
```

The following regex pattern `/lin(e|k)/` specifies a grouping
`(e|k)` in the pattern:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex: /lin(e|k)/ } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : null }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : { "match" : "line", "idx" : 6, "captures" : [ "e" ] } }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : { "match" : "line", "idx" : 23, "captures" : [ "e" ] } }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : { "match" : "line", "idx" : 9, "captures" : [ "e" ] } }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : { "match" : "link", "idx" : 9, "captures" : [ "k" ] } }
{ "_id" : 6, "description" : "métier work vocation", "returnObject" : null }
```

In the return option, the `idx` field is the [code point](http://www.unicode.org/glossary/#code_point) index and not the byte
index. To illustrate, consider the following example that uses the
regex pattern `/tier/`:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex: /tier/ } } } }
])
```

The operation returns the following where only the last record
matches the pattern and the returned `idx` is `2` (instead of 3
if using a byte index)

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : null }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : null }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : null }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : null }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : null }
{ "_id" : 6, "description" : "métier work vocation", 
             "returnObject" : { "match" : "tier", "idx" : 2, "captures" : [ ] } }
```

#### `i` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To perform case-*insensitive* pattern matching, include the i option as part of the regex field or
in the options field:

```none
// Specify i as part of the regex field
{ $regexFind: { input: "$description", regex: /line/i } }

// Specify i in the options field
{ $regexFind: { input: "$description", regex: /line/, options: "i" } }
{ $regexFind: { input: "$description", regex: "line", options: "i" } }
```

For example, the following aggregation performs a case-*insensitive*
`$regexFind` on the `description` field. The regex
pattern `/line/` does not specify any grouping:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex: /line/i } } } }
])
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : { "match" : "LINE", "idx" : 7, "captures" : [ ] } }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : { "match" : "line", "idx" : 6, "captures" : [ ] } }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : { "match" : "line", "idx" : 23, "captures" : [ ] } }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : { "match" : "line", "idx" : 9, "captures" : [ ] } }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : null }
{ "_id" : 6, "description" : "métier work vocation", "returnObject" : null }
```

   

#### `m` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To match the specified anchors (e.g. `^`, `$`) for each line of a
multiline string, include the m option as
part of the regex field or in the
options field:

```none
// Specify m as part of the regex field
{ $regexFind: { input: "$description", regex: /line/m } }

// Specify m in the options field
{ $regexFind: { input: "$description", regex: /line/, options: "m" } }
{ $regexFind: { input: "$description", regex: "line", options: "m" } }
```

The following example includes both the `i` and the `m` options to
match lines starting with either the letter `s` or `S` for
multiline strings:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex: /^s/im } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : { "match" : "S", "idx" : 0, "captures" : [ ] } }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : { "match" : "s", "idx" : 12, "captures" : [ ] } }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : null }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : null }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : null }
{ "_id" : 6, "description" : "métier work vocation", "returnObject" : null }
```

#### `x` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To ignore all unescaped white space characters and comments (denoted by
the un-escaped hash `#` character and the next new-line character) in
the pattern, include the s option in the
options field:

```none
// Specify x in the options field
{ $regexFind: { input: "$description", regex: /line/, options: "x" } }
{ $regexFind: { input: "$description", regex: "line", options: "x" } }
```

The following example includes the `x` option to skip unescaped white
spaces and comments:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex: /lin(e|k) # matches line or link/, options:"x" } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : null }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : { "match" : "line", "idx" : 6, "captures" : [ "e" ] } }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : { "match" : "line", "idx" : 23, "captures" : [ "e" ] } }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : { "match" : "line", "idx" : 9, "captures" : [ "e" ] } }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : { "match" : "link", "idx" : 9, "captures" : [ "k" ] } }
{ "_id" : 6, "description" : "métier work vocation", "returnObject" : null }
```

#### `s` Option

**Note:**

You cannot specify options in both the `regex` and the
`options` field.

To allow the dot character (i.e. `.`) in the pattern to match all
characters including the new line character, include the s option in the options
field:

```none
// Specify s in the options field
{ $regexFind: { input: "$description", regex: /m.*line/, options: "s" } }
{ $regexFind: { input: "$description", regex: "m.*line", options: "s" } }
```

The following example includes the `s` option to allow the dot
character (i.e. .) to match all characters including new line as well
as the `i` option to perform a case-insensitive match:

```javascript
db.products.aggregate([
   { $addFields: { returnObject: { $regexFind: { input: "$description", regex:/m.*line/, options: "si"  } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returnObject" : null }
{ "_id" : 2, "description" : "First lines\nsecond line", "returnObject" : null }
{ "_id" : 3, "description" : "Many spaces before     line", "returnObject" : { "match" : "Many spaces before     line", "idx" : 0, "captures" : [ ] } }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returnObject" : { "match" : "Multiple\nline", "idx" : 0, "captures" : [ ] } }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returnObject" : null }
{ "_id" : 6, "description" : "métier work vocation", "returnObject" : null }
```

### Use `$regexFind` to Parse Email from String

Create a sample collection `feedback` with the following documents:

```javascript
db.feedback.insertMany([
   { "_id" : 1, comment: "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com"  },
   { "_id" : 2, comment: "I wanted to concatenate a string" },
   { "_id" : 3, comment: "How do I convert a date to string? cam@mongodb.com" },
   { "_id" : 4, comment: "It's just me. I'm testing.  fred@MongoDB.com" }
])
```

   
The following aggregation uses the `$regexFind` to extract
the email from the `comment` field (case insensitive).

```javascript
db.feedback.aggregate( [ 
    { $addFields: { 
       "email": { $regexFind: { input: "$comment", regex: /[a-z0-9_.+-]+@[a-z0-9_.+-]+\.[a-z0-9_.+-]+/i } }
    } },
    { $set: { email: "$email.match"} }
] )
```

First Stage
   The stage uses the `$addFields` stage to add a new field
   `email` to the document. The new field contains the result of
   performing the `$regexFind` on the `comment` field:

   ```javascript
   { "_id" : 1, "comment" : "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com", "email" : { "match" : "aunt.arc.tica@example.com", "idx" : 38, "captures" : [ ] } }
   { "_id" : 2, "comment" : "I wanted to concatenate a string", "email" : null }
   { "_id" : 3, "comment" : "I can't find how to convert a date to string. cam@mongodb.com", "email" : { "match" : "cam@mongodb.com", "idx" : 46, "captures" : [ ] } }
   { "_id" : 4, "comment" : "It's just me. I'm testing.  fred@MongoDB.com", "email" : { "match" : "fred@MongoDB.com", "idx" : 28, "captures" : [ ] } }
   ```

Second Stage
   The stage use the `$set` stage to reset the `email` to
   the current `"$email.match"` value. If the current value of `email`
   is null, the new value of `email` is set to null.

   ```javascript
   { "_id" : 1, "comment" : "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com", "email" : "aunt.arc.tica@example.com" }
   { "_id" : 2, "comment" : "I wanted to concatenate a string" }
   { "_id" : 3, "comment" : "I can't find how to convert a date to string. cam@mongodb.com", "email" : "cam@mongodb.com" }
   { "_id" : 4, "comment" : "It's just me. I'm testing.  fred@MongoDB.com", "email" : "fred@MongoDB.com" }
   ```

### Apply `$regexFind` to String Elements of an Array

Create a sample collection `contacts` with the following documents:

```javascript
db.contacts.insertMany([
   { "_id" : 1, name: "Aunt Arc Tikka", details: [ "+672-19-9999", "aunt.arc.tica@example.com" ] },
   { "_id" : 2, name: "Belle Gium",  details: [ "+32-2-111-11-11", "belle.gium@example.com" ] },
   { "_id" : 3, name: "Cam Bo Dia",  details: [ "+855-012-000-0000", "cam.bo.dia@example.com" ] },
   { "_id" : 4, name: "Fred", details: [ "+1-111-222-3333" ] }
])
```

The following aggregation uses the `$regexFind` to convert
the `details` array into an embedded document with an `email` and
`phone` fields:

```javascript
db.contacts.aggregate( [ 
   { $unwind: "$details" },
   { $addFields: { 
      "regexemail": { $regexFind: { input: "$details", regex: /^[a-z0-9_.+-]+@[a-z0-9_.+-]+\.[a-z0-9_.+-]+$/, options: "i" } }, 
      "regexphone": { $regexFind: { input: "$details", regex: /^[+]{0,1}[0-9]*\-?[0-9_\-]+$/ } } 
   } },
   { $project: { _id: 1, name: 1, details: { email: "$regexemail.match", phone: "$regexphone.match" } } },
   { $group: { _id: "$_id", name: { $first: "$name" }, details: { $mergeObjects: "$details"} } },
   { $sort: { _id: 1 } }
])
```

First Stage
   The stage `$unwinds` the array into separate
   documents:

   ```javascript
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : "+672-19-9999" }
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : "aunt.arc.tica@example.com" }
   { "_id" : 2, "name" : "Belle Gium", "details" : "+32-2-111-11-11" }
   { "_id" : 2, "name" : "Belle Gium", "details" : "belle.gium@example.com" }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : "+855-012-000-0000" }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : "cam.bo.dia@example.com" }
   { "_id" : 4, "name" : "Fred", "details" : "+1-111-222-3333" }
   ```

Second Stage
   The stage uses the `$addFields` stage to add new fields to
   the document that contains the result of the
   `$regexFind` for phone number and email:

   ```javascript
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : "+672-19-9999", "regexemail" : null, "regexphone" : { "match" : "+672-19-9999", "idx" : 0, "captures" : [ ] } }
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : "aunt.arc.tica@example.com", "regexemail" : { "match" : "aunt.arc.tica@example.com", "idx" : 0, "captures" : [ ] }, "regexphone" : null }
   { "_id" : 2, "name" : "Belle Gium", "details" : "+32-2-111-11-11", "regexemail" : null, "regexphone" : { "match" : "+32-2-111-11-11", "idx" : 0, "captures" : [ ] } }
   { "_id" : 2, "name" : "Belle Gium", "details" : "belle.gium@example.com", "regexemail" : { "match" : "belle.gium@example.com", "idx" : 0, "captures" : [ ] }, "regexphone" : null }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : "+855-012-000-0000", "regexemail" : null, "regexphone" : { "match" : "+855-012-000-0000", "idx" : 0, "captures" : [ ] } }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : "cam.bo.dia@example.com", "regexemail" : { "match" : "cam.bo.dia@example.com", "idx" : 0, "captures" : [ ] }, "regexphone" : null }
   { "_id" : 4, "name" : "Fred", "details" : "+1-111-222-3333", "regexemail" : null, "regexphone" : { "match" : "+1-111-222-3333", "idx" : 0, "captures" : [ ] } }
   ```

Third Stage
   The stage use the `$project` stage to output documents with the `_id` field, the `name` field and
   the `details` field. The `details` field is set to a
   document with `email` and `phone` fields, whose values are determined from the
   `regexemail` and `regexphone` fields, respectively.

   ```javascript
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : { "phone" : "+672-19-9999" } }
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : { "email" : "aunt.arc.tica@example.com" } }
   { "_id" : 2, "name" : "Belle Gium", "details" : { "phone" : "+32-2-111-11-11" } }
   { "_id" : 2, "name" : "Belle Gium", "details" : { "email" : "belle.gium@example.com" } }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : { "phone" : "+855-012-000-0000" } }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : { "email" : "cam.bo.dia@example.com" } }
   { "_id" : 4, "name" : "Fred", "details" : { "phone" : "+1-111-222-3333" } }
   ```

Fourth Stage
   The stage uses the `$group` stage to groups the input documents by
   their `_id` value. The stage uses the `$mergeObjects`
   expression to merge the `details` documents.

   ```javascript
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : { "phone" : "+855-012-000-0000", "email" : "cam.bo.dia@example.com" } }
   { "_id" : 4, "name" : "Fred", "details" : { "phone" : "+1-111-222-3333" } }
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : { "phone" : "+672-19-9999", "email" : "aunt.arc.tica@example.com" } }
   { "_id" : 2, "name" : "Belle Gium", "details" : { "phone" : "+32-2-111-11-11", "email" : "belle.gium@example.com" } }
   ```

Fifth Stage
   The stage uses the `$sort` stage to sort the documents by the `_id` field.

   ```javascript
   { "_id" : 1, "name" : "Aunt Arc Tikka", "details" : { "phone" : "+672-19-9999", "email" : "aunt.arc.tica@example.com" } }
   { "_id" : 2, "name" : "Belle Gium", "details" : { "phone" : "+32-2-111-11-11", "email" : "belle.gium@example.com" } }
   { "_id" : 3, "name" : "Cam Bo Dia", "details" : { "phone" : "+855-012-000-0000", "email" : "cam.bo.dia@example.com" } }
   { "_id" : 4, "name" : "Fred", "details" : { "phone" : "+1-111-222-3333" } }
   ```

### Use Captured Groupings to Parse User Name

Create a sample collection `employees` with the following documents:

```javascript
db.employees.insertMany([
   { "_id" : 1, name: "Aunt Arc Tikka", "email" : "aunt.tica@example.com" },
   { "_id" : 2, name: "Belle Gium", "email" : "belle.gium@example.com" },
   { "_id" : 3, name: "Cam Bo Dia", "email" : "cam.dia@example.com" },
   { "_id" : 4, name: "Fred"  }
])
```

The employee email has the format
`<firstname>.<lastname>@example.com`. Using the `captured` field
returned in the `$regexFind` results, you can parse out
user names for employees.

```javascript
db.employees.aggregate( [ 
    { $addFields: { 
       "username": { $regexFind: { input: "$email", regex: /^([a-z0-9_.+-]+)@[a-z0-9_.+-]+\.[a-z0-9_.+-]+$/, options: "i" } },
    } },
    { $set: { username: { $arrayElemAt:  [ "$username.captures", 0 ] } } }
] )
```

First Stage
   The stage uses the `$addFields` stage to add a new field
   `username` to the document. The new field contains the result of
   performing the `$regexFind` on the `email` field:

   ```javascript
   { "_id" : 1, "name" : "Aunt Arc Tikka", "email" : "aunt.tica@example.com", "username" : { "match" : "aunt.tica@example.com", "idx" : 0, "captures" : [ "aunt.tica" ] } }
   { "_id" : 2, "name" : "Belle Gium", "email" : "belle.gium@example.com", "username" : { "match" : "belle.gium@example.com", "idx" : 0, "captures" : [ "belle.gium" ] } }
   { "_id" : 3, "name" : "Cam Bo Dia", "email" : "cam.dia@example.com", "username" : { "match" : "cam.dia@example.com", "idx" : 0, "captures" : [ "cam.dia" ] } }
   { "_id" : 4, "name" : "Fred", "username" : null }
   ```

   
Second Stage
   The stage use the `$set` stage to reset the `username` to
   the zero-th element of the `"$username.captures"` array. If the current value of `username`
   is null, the new value of `username` is set to null.

   ```javascript
   { "_id" : 1, "name" : "Aunt Arc Tikka", "email" : "aunt.tica@example.com", "username" : "aunt.tica" }
   { "_id" : 2, "name" : "Belle Gium", "email" : "belle.gium@example.com", "username" : "belle.gium" }
   { "_id" : 3, "name" : "Cam Bo Dia", "email" : "cam.dia@example.com", "username" : "cam.dia" }
   { "_id" : 4, "name" : "Fred", "username" : null }
   ```

**See also:**

For more information on the behavior of the `captures` array and
additional examples, see
regexFind-captures-behavior.
