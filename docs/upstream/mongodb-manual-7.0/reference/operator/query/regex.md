<!-- Converted from reference/operator/query/regex.txt (reStructuredText). Includes are inlined. -->

# $regex (query predicate operator)

**Note:**

This page describes regular expression search capabilities for
self-managed (non-Atlas) deployments. For data hosted on MongoDB
Atlas, MongoDB offers an improved full-text search solution,
Atlas Search, which has its own `$regex`
operator. To learn more, see $regex
in the Atlas Search documentation.

## Definition

**`$regex`**

Provides regular expression capabilities for pattern matching
*strings* in queries.

## Compatibility

You can use `$regex` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

Use one of the following syntax variations:

```javascript
{ <field>: { $regex: /pattern/, $options: '<options>' } }
{ "<field>": { "$regex": "pattern", "$options": "<options>" } }
{ <field>: { $regex: /pattern/<options> } }
```

**Note:**

To use `$regex` with `mongodump`, enclose the query 
document in single quotes ('{ ... }') to ensure it doesn't interact 
with the shell.

The query document must be in Extended JSON v2 format (either relaxed or canonical/strict mode), 
which includes enclosing the field names and operators in quotes. For 
example:

```sh
mongodump -d=sample_mflix -c=movies  -q='{"year": {"$regex": "20"}}'
```

You can also use regular expression objects (`/pattern/`) to specify
regular expressions:

```javascript
{ <field>: /pattern/<options> }
```

For restrictions on syntax use, see syntax-restrictions.

**`$options`**

The following `<options>` are available for regular expressions:

| Option | Description |
|---|---|
| `i` | Case insensitivity to match upper and lower cases. For an example, see regex-case-insensitive. |
| `m` | For patterns that include anchors (`^` for the start, `$` for the end), match at the beginning or end of each line for strings with multiline values. Without this option, these anchors match at beginning or end of the string. For an example, see regex-multiline-match. If the pattern has no anchors or if the string value has no newline characters (for example,  `\n`), the `m` option has no effect. |
| `x` | "Extended" capability to ignore all white space characters in the `$regex` pattern unless escaped or included in a character class. Additionally, it ignores characters in-between and including an un-escaped hash/pound (`#`) character and the next new line, so that you may include comments in complicated patterns. This only applies to data characters; white space characters may never appear within special character sequences in a pattern. The `x` option does not affect the handling of the VT character (code 11). |
| `s` | Allows the dot character (`.`) to match all characters *including* newline characters. For an example, see regex-dot-new-line. |
| `u` | Unicode option, which is accepted but redundant. UTF is enabled by default for `$regex`. |

**Note:**

`$regex` doesn't support the global search modifier `g`.

## Behavior

### $regex vs. /pattern/ Syntax

#### `$in` Expressions

To include a regular expression in an `$in` query predicate operator,
you can only use JavaScript regular expression objects (`/pattern/` ).

For example:

```javascript
{ name: { $in: [ /^acme/i, /^ack/ ] } }
```

You *cannot* use `$regex` operator expressions inside an
`$in` operator.

#### Implicit `AND` Conditions for the Field

To include a regular expression in a comma-separated list of query
conditions for the field, use the `$regex` operator. For example:

```javascript
{ name: { $regex: /acme.*corp/i, $nin: [ 'acmeblahcorp' ] } }
{ name: { $regex: /acme.*corp/, $options: 'i', $nin: [ 'acmeblahcorp' ] } }
{ name: { $regex: 'acme.*corp', $options: 'i', $nin: [ 'acmeblahcorp' ] } }
```

#### `x` and `s` Options

To use either the `x` option or `s` options, you must use the
`$regex` operator expression *with* the `$options`
operator. For example, to specify the `i` and the `s` options, you
must use `$options` for both:

```javascript
{ name: { $regex: /acme.*corp/, $options: "si" } }
{ name: { $regex: 'acme.*corp', $options: "si" } }
```

#### PCRE Versus JavaScript

To use PCRE (Perl Compatible Regular Expressions)-supported features in a regular expression that
aren't supported in JavaScript, use the `$regex` operator and
specify the pattern as a string.

To match case-insensitive strings:

- `"(?i)"` begins a case-insensitive match.
- `"(?-i)"` ends a case-insensitive match.

For example, the regular expression `"(?i)a(?-i)cme"` matches strings
that:

- Begin with `"a"` or `"A"`. This is a case-insensitive match.
- End with `"cme"`. This is a case-sensitive match.

These strings match the example regular expression:

- `"acme"`
- `"Acme"`

The following example uses the `$regex` operator to find `name`
field strings that match the regular expression `"(?i)a(?-i)cme"`:

```javascript
{ name: { $regex: "(?i)a(?-i)cme" } }
```

Starting in version 6.1, MongoDB uses the PCRE2 (Perl Compatible Regular Expressions) library to
implement regular expression pattern matching. To learn more about
PCRE2, see the [PCRE Documentation](https://www.pcre.org/current/doc/html/).

#### `$regex` and `$not`

The `$not` operator can perform a logical `NOT`
operation on both:

- Regular expression objects (`/pattern/`)

  For example:

  ```javascript
  db.inventory.find( { item: { $not: /^p.*/ } } )
  ```

- `$regex` operator expressions 

  For example:

  ```javascript
  db.inventory.find( { item: { $not: { $regex: "^p.*" } } } )
  db.inventory.find( { item: { $not: { $regex: /^p.*/ } } } )
  ```

### Index Use

Index use and performance for `$regex` queries depends on
whether the query is case-sensitive or case-insensitive.

#### Case-Sensitive Queries

For case sensitive regular expression queries, if an index exists for
the field, then MongoDB matches the regular expression for the values in
the index. This can be faster than a collection scan.

Further optimization can occur if the regular expression is a "prefix
expression", which means that all potential matches start with the same
string. This allows MongoDB to construct a "range" from that prefix and
only match values from the index within the specified range.

A regular expression is a "prefix expression" if it starts with a caret
(`^`) or a left anchor (`\A`), followed by a string of simple
symbols. For example, the regex `/^abc.*/` is optimized to
match only the values from the index that start with `abc`.

Additionally, although `/^a/`, `/^a.*/`, and `/^a.*$/` match
equivalent strings, they have different performance characteristics.
All of these expressions use an index if an appropriate index
exists. However, `/^a.*/`, and `/^a.*$/` are slower. `/^a/`
can stop scanning after matching the prefix.

#### Case-Insensitive Queries

Case-insensitive indexes do not improve performance for
`$regex` queries, as the `$regex` operator is not collation-aware 
and therefore cannot take advantage of such indexes.

## Examples

The examples in this section use the following `products` collection:

```javascript
db.products.insertMany( [
   { _id: 100, sku: "abc123", description: "Single line description." },
   { _id: 101, sku: "abc789", description: "First line\nSecond line" },
   { _id: 102, sku: "xyz456", description: "Many spaces before     line" },
   { _id: 103, sku: "xyz789", description: "Multiple\nline description" },
   { _id: 104, sku: "Abc789", description: "SKU starts with A" }
] )
```

### Perform a `LIKE` Match

The following example matches all documents where the `sku` field is
like `"%789"`:

```javascript
db.products.find( { sku: { $regex: /789$/ } } )
```

The example is similar to the following SQL LIKE statement:

```SQL
SELECT * FROM products
WHERE sku like "%789";
```

Example output:

```javascript
[
   { _id: 101, sku: 'abc789', description: 'First line\nSecond line' },
   { _id: 103, sku: 'xyz789', description: 'Multiple\nline description' },
   { _id: 104, sku: 'Abc789', description: 'SKU starts with A' }
]
```

### Perform Case-Insensitive Regular Expression Match

The following example uses the `i` option to perform a
case-insensitive match for `sku` values that start with `ABC`:

```javascript
db.products.find( { sku: { $regex: /^ABC/i } } )
```

Example output:

```javascript
[
   { _id: 100, sku: 'abc123', description: 'Single line description.' },
   { _id: 101, sku: 'abc789', description: 'First line\nSecond line' },
   { _id: 104, sku: 'Abc789', description: 'SKU starts with A' }
]
```

### Multiline Match for Lines Starting with Specified Pattern

The following example uses the `m` option to match lines starting
with the letter `S` for multiline strings:

```javascript
db.products.find( { description: { $regex: /^S/, $options: 'm' } } )
```

Example output:

```javascript
[
   { _id: 100, sku: 'abc123', description: 'Single line description.' },
   { _id: 101, sku: 'abc789', description: 'First line\nSecond line' },
   { _id: 104, sku: 'Abc789', description: 'SKU starts with A' }
]
```

Without the `m` option, the example output is:

```javascript
[
   { _id: 100, sku: 'abc123', description: 'Single line description.' },
   { _id: 104, sku: 'Abc789', description: 'SKU starts with A' }
]
```

If the `$regex` pattern doesn't contain an anchor, the pattern
matches against the whole string. For example:

```javascript
db.products.find( { description: { $regex: /S/ } } )
```

Example output:

```javascript
[
   { _id: 100, sku: 'abc123', description: 'Single line description.' },
   { _id: 101, sku: 'abc789', description: 'First line\nSecond line' },
   { _id: 104, sku: 'Abc789', description: 'SKU starts with A' }
]
```

### Use the `.` Dot Character to Match New Line

The following example uses the `s` option to allow the dot character
(`.`) to match all characters *including* new line, and the
`i` option to perform a case-insensitive match:

```javascript
db.products.find( { description: { $regex: /m.*line/, $options: 'si' } } )
```

Example output:

```javascript
[
   { _id: 102, sku: 'xyz456', description: 'Many spaces before     line' },
   { _id: 103, sku: 'xyz789', description: 'Multiple\nline description' }
]
```

Without the `s` option, the query returns:

```javascript
[
   { _id: 102, sku: 'xyz456', description: 'Many spaces before     line' }
]
```

### Ignore White Spaces in Pattern

The following example uses the `x` option ignore white spaces and the
comments, denoted by the `#` and ending with the `\n` in the
matching pattern:

```javascript
var pattern = "abc #category code\n123 #item number"
db.products.find( { sku: { $regex: pattern, $options: "x" } } )
```

Example output:

```javascript
[
   { _id: 100, sku: 'abc123', description: 'Single line description.' }
]
```

### Use a Regular Expression to Match Case in Strings

The following example uses the regular expression `"(?i)a(?-i)bc"` to
match `sku` field strings that contain:

- `"abc"`
- `"Abc"`

```javascript
db.products.find( { sku: { $regex: "(?i)a(?-i)bc" } } )
```

Example output:

```javascript
[
   { _id: 100, sku: 'abc123', description: 'Single line description.' },
   { _id: 101, sku: 'abc789', description: 'First line\nSecond line' },
   { _id: 104, sku: 'Abc789', description: 'SKU starts with A' }
]
```

### Extend Regex Options to Match Characters Outside of ASCII

**New in version:** 6.1

By default, some regex options (such as `/b` and `/w`) only
recognize ASCII characters. This can cause unexpected results when
performing regex matches against UTF-8 characters.

Starting in MongoDB 6.1, you can specify the `*UCP` regex option to
match UTF-8 characters.

**Important:** Performance of UCP Option

The `*UCP` option results in slower queries than those without the
option specified because `*UCP` requires a multistage table lookup
to perform the match.

For example, consider the following documents in a `songs`
collection:

```javascript
db.songs.insertMany( [
   { _id: 0, "artist" : "Blue Öyster Cult", "title": "The Reaper" },
   { _id: 1, "artist": "Blue Öyster Cult", "title": "Godzilla" },
   { _id: 2, "artist" : "Blue Oyster Cult", "title": "Take Me Away" }
] )
```

The following regex query uses the `\b` option in a regex match. The
`\b` option matches a word boundary.

```javascript
db.songs.find( { artist: { $regex: /\byster/ } } )
```

Example output:

```javascript
[
   { _id: 0, artist: 'Blue Öyster Cult', title: 'The Reaper' },
   { _id: 1, artist: 'Blue Öyster Cult', title: 'Godzilla' }
]
```

The previous results are unexpected because none of the whole words in the
returned `artist` fields begin with the matched string (`yster`).
The `Ö` character in documents `_id: 0` and `_id: 1` is ignored
when performing the match because `Ö` is a UTF-8 character.

The expected result is the query doesn't return any documents.

To allow the query to recognize UTF-8 characters, specify the `*UCP`
option before the pattern:

```javascript
db.songs.find( { artist: { $regex: "(*UCP)/\byster/" } } )
```

The previous query doesn't return any documents, which is the expected
result because none of the whole words in the `artist` fields begin with the
string `yster`.

**Tip:** Escape Characters for Regex Patterns

When specifying `*UCP` or any other regular expression option,
use the correct escape characters for your shell or
driver.
