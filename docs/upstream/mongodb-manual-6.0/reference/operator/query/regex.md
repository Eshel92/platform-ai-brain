<!-- Converted from reference/operator/query/regex.txt (reStructuredText). Includes are inlined. -->

# $regex

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
*strings* in queries. MongoDB uses Perl compatible regular
expressions (i.e. "PCRE" ) version 8.42 with UTF-8 support.

## Compatibility

You can use `$regex` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

To use `$regex`, use one of the following syntaxes:

```javascript
{ <field>: { $regex: /pattern/, $options: '<options>' } }
{ "<field>": { "$regex": "pattern", "$options": "<options>" } }
{ <field>: { $regex: /pattern/<options> } }
```

**Note:**

To use `$regex` with `mongodump`, you must enclose the query 
document in single quotes ('{ ... }') to ensure that it does not interact 
with your shell environment. 

The query document must be in Extended JSON v2 format (either relaxed or canonical/strict mode), 
which includes enclosing the field names and operators in quotes. For 
example:

```sh
mongodump -d=sample_mflix -c=movies  -q='{"year": {"$regex": "20"}}'
```

In MongoDB, you can also use regular expression objects (i.e.
`/pattern/`) to specify regular expressions:

```javascript
{ <field>: /pattern/<options> }
```

For restrictions on particular syntax use, see
syntax-restrictions.

**`$options`**

The following `<options>` are available for use with regular
expression.

| Option | Description |
|---|---|
| `i` | Case insensitivity to match upper and lower cases. For an example, see regex-case-insensitive. |
| `m` | For patterns that include anchors (i.e. `^` for the start, `$` for the end), match at the beginning or end of each line for strings with multiline values. Without this option, these anchors match at beginning or end of the string. For an example, see regex-multiline-match. If the pattern contains no anchors or if the string value has no newline characters (e.g. `\n`), the `m` option has no effect. |
| `x` | "Extended" capability to ignore all white space characters in the `$regex` pattern unless escaped or included in a character class. Additionally, it ignores characters in-between and including an un-escaped hash/pound (`#`) character and the next new line, so that you may include comments in complicated patterns. This only applies to data characters; white space characters may never appear within special character sequences in a pattern. The `x` option does not affect the handling of the VT character (i.e. code 11). |
| `s` | Allows the dot character (i.e. `.`) to match all characters *including* newline characters. For an example, see regex-dot-new-line. |
| `u` | Supports Unicode. This flag is accepted, but is redundant. UTF is set by default in the `$regex` operator, making the `u` option unnecessary. |

**Note:**

The `$regex` operator *does not* support the global search modifier `g`.

## Behavior

### $regex vs. /pattern/ Syntax

#### `$in` Expressions

To include a regular expression in an `$in` query expression, you can
only use JavaScript regular expression objects (i.e. `/pattern/`
). For example:

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

#### PCRE vs JavaScript

To use PCRE supported features in a regular expression that aren't
supported in JavaScript, you must use the `$regex` operator and
specify the regular expression as a string.

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

#### `$regex` and `$not`

The `$not` operator can perform logical `NOT`
operation on both:

- Regular expression objects (i.e. `/pattern/`)

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

In 4.0.6 and earlier, you could use `$not` operator with regular
expression objects (i.e. `/pattern/`) but not with `$regex`
operator expressions.

### Index Use

Index use and performance for `$regex` queries varies depending on
whether the query is case-sensitive or case-insensitive.

#### Case-Sensitive Queries

For case sensitive regular expression queries, if an index exists
for the field, then MongoDB matches the regular expression against the
values in the index, which can be faster than a collection scan.

Further optimization can occur if the regular expression is a "prefix
expression", which means that all potential matches start with the same
string. This allows MongoDB to construct a "range" from that prefix and
only match against those values from the index that fall within that
range.

A regular expression is a "prefix expression" if it starts with a caret
(`^`) or a left anchor (`\A`), followed by a string of simple
symbols. For example, the regex `/^abc.*/` will be optimized by
matching only against the values from the index that start with `abc`.

Additionally, while `/^a/`, `/^a.*/`, and `/^a.*$/` match
equivalent strings, they have different performance characteristics.
All of these expressions use an index if an appropriate index
exists; however, `/^a.*/`, and `/^a.*$/` are slower. `/^a/`
can stop scanning after matching the prefix.

#### Case-Insensitive Queries

Case-insensitive indexes typically do not improve performance for
`$regex` queries. The `$regex` implementation is not
collation-aware and cannot utilize case-insensitive indexes efficiently.

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

The example is analogous to the following SQL LIKE statement:

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

The following example uses the `i` option perform a
*case-insensitive* match for documents with `sku` value that starts
with `ABC`.

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

If the `$regex` pattern does not contain an anchor, the pattern
matches against the string as a whole, as in the following example:

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

The following example uses the `s` option to allow the  dot
character (i.e. `.`) to match all characters *including* new line as well as the
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

*Without* the `s` option, the example output is:

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
