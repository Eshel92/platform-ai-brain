<!-- Converted from reference/operator/query/text.txt (reStructuredText). Includes are inlined. -->

# $text (Self-Managed Deployments)

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

This page describes the `$text` operator for self-managed deployments.

## Definition

**`$text`**

`$text` performs a text query on the content of the fields
indexed with a text index. 

## Compatibility

You can use `$text` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

   
A `$text` expression has the following syntax:

```javascript
{
  $text: {
    $search: <string>,
    $language: <string>,
    $caseSensitive: <boolean>,
    $diacriticSensitive: <boolean>
  }
}
```

The `$text` operator accepts a text query document with the
following fields:

| Field | Type | Description |
|---|---|---|
| `$search` | string | A string of terms that MongoDB parses and uses to query the text index. MongoDB performs a logical `OR` query on the terms unless you specify the terms as an exact string. For more information on the field, see text-query-operator-behavior. |
| `$language` | string | .. _language-field: Optional. The language that determines the list of stop words for the query and the rules for the stemmer and tokenizer. If unspecified, MongoDB uses the default language of the index. For supported languages, see text-search-languages. If you specify a `default_language` value of `none`, the text index parses through each word in the field, including stop words, and ignores suffix stemming. |
| `$caseSensitive` | boolean | Optional. A boolean flag to enable or disable case sensitivity. Defaults to `false`. If unspecified, MongoDB defers to the case insensitivity of the text index. For more information, see text-operator-case-sensitivity. |
| `$diacriticSensitive` | boolean | Optional. A boolean flag to enable or disable diacritic sensitivity against version 3 text indexes. Defaults to `false`. If unspecified, MongoDB defers to the diacritic insensitivity of the text index. Text queries against earlier versions of the text index are inherently diacritic sensitive and cannot be diacritic insensitive. As such, the `$diacriticSensitive` option has no effect with earlier versions of the `text` index. For more information, see text-operator-diacritic-sensitivity. |

The `$text` operator, by default, does *not* return results sorted in
terms of the results' scores. For more information on sorting by the
results' scores, see the text-operator-text-score documentation.

## Behavior

### Restrictions

- A query can specify, at most, one `$text` expression.

- `$text` cannot appear in `$nor` expressions.

- `$text` cannot appear in `$elemMatch` query
  expressions or `$elemMatch` projection expressions.

- To use `$text` in an `$or` expression, all
  clauses in the `$or` array must be indexed.

- .. include:: /includes/fact-hint-text-query-restriction.rst

- You cannot specify the `$natural` sort order if the query
  includes a `$text` expression.

- .. include:: /includes/fact-special-indexes-and-text.rst

- .. include:: /includes/extracts/views-unsupported-text-search.rst

- `$text` is unsupported for creating indexes using the
  Stable API V1.

If using the `$text` operator in aggregation, the following
restrictions also apply.

- The `$match` stage that includes a `$text` must be
  the **first** stage in the pipeline.

- A `$text` operator can only occur once in the stage.

- The `$text` operator expression cannot appear in
  `$or` or `$not` expressions.

- `$text`, by default, does not return the matching documents in order
  of matching scores. To sort by descending score, use the
  `$meta` aggregation expression in the `$sort` stage.

### `$search` Field

In the `$search` field, specify a string of words that the
`$text` operator parses and uses to query the text index.

The `$text` operator treats most punctuation
in the string as delimiters, except a hyphen-minus (`-`) that negates term or
an escaped double quotes `\"` that specifies an exact string.

**Note:**

The `$search` field for the `$text` expression is different than
the $search aggregation stage provided by Atlas
Search. The `$search` aggregation stage performs a
full-text search on specified fields and is only available on MongoDB
Atlas.

#### Exact Strings

To match on an exact multi-word string, as opposed to individual terms, enclose
the string in escaped double quotes (`\"`), as in:

```javascript
"\"ssl certificate\""
```

If the `$search` string of a `$text` operation includes a multi-word string
and individual terms, `$text` only matches the documents that include the
multi-word string.

For example, the following `$search` string returns documents that include the
exact string `"ssl certificate"`:

```javascript
"\"ssl certificate\" authority key"
```

#### Negations

Prefixing a word with a hyphen-minus (`-`) negates a word:

- The negated word excludes documents that contain the
  negated word from the result set.

- When passed a string that only contains negated words, `$text` does
  not match any documents.

- A hyphenated word, such as `pre-market`, is not a negation. If used
  in a hyphenated word, the `$text` operator treats the hyphen-minus
  (`-`) as a delimiter. To negate the word `market` in this
  instance, include a space between `pre` and `-market`, i.e.,
  `pre -market`.

The `$text` operator adds all negations to the operation with the
logical `AND` operator.

### Match Operation

#### Stop Words

The `$text` operator ignores language-specific stop words, such
as `the` and `and` in English.

#### Stemmed Words

When you use case insensitivity and diacritic insensitivity, the
`$text` operator matches on the complete *stemmed* word. If a document
field contains the word `blueberry`, a `$text` operation with a
`$search` term of `blue` does not match. However, `blueberry` or
`blueberries` match.

##### Case Sensitivity and Stemmed Words

When you use case sensitivity
(`$caseSensitive: true`), if the suffix stem contains uppercase
letters, the `$text` operator matches on the exact word.

##### Diacritic Sensitivity and Stemmed Words

When you use diacritic sensitivity (`$diacriticSensitive: true`),
if the suffix stem contains the diacritic mark or marks, the `$text`
operator matches on the exact word.

### Case Insensitivity

The `$text` operator defaults to the case insensitivity of the
text index:

- The version 3 text index is
  case insensitive for Latin characters with or without diacritics and
  characters from non-Latin alphabets, such as the Cyrillic alphabet.
  See text index for details.

- Earlier versions of the `text` index are case insensitive for Latin
  characters without diacritic marks; i.e. for `[A-z]`.

#### `$caseSensitive` Option

To support case sensitivity where the `text` index is case
insensitive, specify `$caseSensitive: true`.

#### Case Sensitivity Process

If `$caseSensitive: true` and the `text` index is case insensitive,
the `$text` operator:

- First queries the `text` index for case insensitive and diacritic
  matches.

- Then, to return just the documents that match the case of the
  specified terms, the `$text` operation includes an additional stage to
  filter out the documents that do not match the specified case.

If `$caseSensitive: true` and if the suffix stem contains uppercase
letters, the `$text` operator matches on the exact word.

Specifying `$caseSensitive: true` may impact performance.

**See also:**

match-operation-stemmed-words

### Diacritic Insensitivity

The `$text` operator defaults to the diacritic insensitivity of
the text index:

- The version 3 text index is
  diacritic insensitive. That is, the index does not distinguish
  between characters that contain diacritical marks and their
  non-marked counterpart, such as `é`, `ê`, and `e`.

- Earlier versions of the `text` index are diacritic sensitive.

#### `$diacriticSensitive` Option

To support diacritic sensitivity with the `text` index, specify
`$diacriticSensitive: true`.

Text queries against earlier versions of the `text` index are
inherently diacritic sensitive and cannot be diacritic insensitive.  As
such, the `$diacriticSensitive` option for the `$text`
operator has no effect with earlier versions of the `text` index.

#### Diacritic Sensitivity Process

To use diacritic sensitivity (`$diacriticSensitive: true`) with a
version 3 `text` index, the `$text` operator:

- First queries the `text` index, which is diacritic insensitive.

- Then, to return just the documents that match the diacritic marked
  characters of the specified terms, the `$text` operation includes an
  additional stage to filter out the documents that do not match.

Specifying `$diacriticSensitive: true` may impact performance.

If you use `$diacriticSensitive: true` with an earlier version of the
`text` index, the `$text` operator queries the `text` index, which
is diacritic sensitive.

If `$diacriticSensitive: true` and if the suffix stem contains the
diacritic mark or marks, the `$text` operator matches on the exact
word.

**See also:**

match-operation-stemmed-words

### Text Score

The `$text` operator assigns a score to each result document. The
score represents the relevance of a document to a given query. The score
can be part of a `sort()` method specification as well as part of the
projection expression. The `{ $meta: "textScore" }` expression
provides information on the processing of the `$text` operation. See
`$meta` projection operator for details on accessing the score for projection or sort.

## Examples

The following examples assume a collection `articles` that has a
version 3 text index on the field `subject`:

```javascript
db.articles.createIndex( { subject: "text" } )
```

Populate the collection with the following documents:

```javascript
db.articles.insertMany( [
     { _id: 1, subject: "coffee", author: "xyz", views: 50 },
     { _id: 2, subject: "Coffee Shopping", author: "efg", views: 5 },
     { _id: 3, subject: "Baking a cake", author: "abc", views: 90  },
     { _id: 4, subject: "baking", author: "xyz", views: 100 },
     { _id: 5, subject: "Café Con Leche", author: "abc", views: 200 },
     { _id: 6, subject: "Сырники", author: "jkl", views: 80 },
     { _id: 7, subject: "coffee and cream", author: "efg", views: 10 },
     { _id: 8, subject: "Cafe con Leche", author: "xyz", views: 10 }
] )
```

### `$text` with a Single Word

The following example specifies a `$search` string of `coffee`:

```javascript
db.articles.find( { $text: { $search: "coffee" } } )
```

This operation returns the documents that contain the term `coffee` in the
indexed `subject` field, or more precisely, the stemmed version of
the word:

```javascript
{ _id: 1, subject: 'coffee', author: 'xyz', views: 50 },
{ _id: 7, subject: 'coffee and cream', author: 'efg', views: 10 },
{ _id: 2, subject: 'Coffee Shopping', author: 'efg', views: 5 }
```

**See also:**

- text-operator-case-sensitivity
- match-operation-stemmed-words

### Match Any of the `$search` Terms

If the `$search` string is a space-delimited string, `$text`
performs a logical `OR` operation on each term and returns documents
that contain any of the terms.

The following example specifies a `$search` string of three terms
delimited by space, `"bake coffee cake"`:

```javascript
db.articles.find( { $text: { $search: "bake coffee cake" } } )
```

This operation returns documents that contain either `bake` **or**
`coffee` **or** `cake` in the indexed `subject` field, or more
precisely, the stemmed version of these words:

```javascript
{ "_id" : 2, "subject" : "Coffee Shopping", "author" : "efg", "views" : 5 }
{ "_id" : 7, "subject" : "coffee and cream", "author" : "efg", "views" : 10 }
{ "_id" : 1, "subject" : "coffee", "author" : "xyz", "views" : 50 }
{ "_id" : 3, "subject" : "Baking a cake", "author" : "abc", "views" : 90 }
{ "_id" : 4, "subject" : "baking", "author" : "xyz", "views" : 100 }
```

**See also:**

- text-operator-case-sensitivity
- match-operation-stemmed-words

### `$text` with an Exact String

To match an exact multi-word string as a single term, escape the quotes.

The following example matches the exact string `coffee shop`:

```javascript
db.articles.find( { $text: { $search: "\"coffee shop\"" } } )
```

This operation returns documents that contain the string `coffee shop`:

```javascript
{ "_id" : 2, "subject" : "Coffee Shopping", "author" : "efg", "views" : 5 }
```

The following example matches the strings `coffee shop` and ``Cafe
con Leche``. This is a logical OR of the two strings.

```javascript
db.articles.find( { $text: { $search: "\'coffee shop\' \'Cafe con Leche\'" } } )
```

   
This operation returns documents that contain both the strings, including
documents that contain terms from both the strings: 

```javascript
[
  { _id: 8, subject: 'Cafe con Leche', author: 'xyz', views: 10 },
  { _id: 5, subject: 'Café Con Leche', author: 'abc', views: 200 },
  { _id: 1, subject: 'coffee', author: 'xyz', views: 50 },
  { _id: 7, subject: 'coffee and cream', author: 'efg', views: 10 },
  { _id: 2, subject: 'Coffee Shopping', author: 'efg', views: 5 }
]
```

**See also:**

text-operator-exact-string

### Exclude Documents That Contain a Term

A *negated* term is a term that is prefixed by a minus sign `-`. If
you negate a term, the `$text` operator excludes the documents that
contain those terms from the results.

The following example matches documents that contain the word `coffee`
but do **not** contain the term `shop`, or more precisely the stemmed
version of the words:

```javascript
db.articles.find( { $text: { $search: "coffee -shop" } } )
```

The operation returns the following documents:

```javascript
{ "_id" : 7, "subject" : "coffee and cream", "author" : "efg", "views" : 10 }
{ "_id" : 1, "subject" : "coffee", "author" : "xyz", "views" : 50 }
```

**See also:**

- text-operator-term-negation
- match-operation-stemmed-words

### Query a Different Language

Use the optional `$language` field in the `$text` expression
to specify a language that determines the list of stop words and the
rules for the stemmer and tokenizer for the `$search` string.

If you specify a `default_language` value of `none`, the text index
parses through each word in the field, including stop words, and ignores
suffix stemming.

The following example specifies `es`, i.e. Spanish, as the language
that determines the tokenization, stemming, and stop words:

```javascript
db.articles.find(
   { $text: { $search: "leche", $language: "es" } }
)
```

The example returns the following documents:

```javascript
{ "_id" : 5, "subject" : "Café Con Leche", "author" : "abc", "views" : 200 }
{ "_id" : 8, "subject" : "Cafe con Leche", "author" : "xyz", "views" : 10 }
```

The `$text` expression can also accept the language by name,
`spanish`. See text-search-languages for the supported
languages.

**See also:**

text-operator-case-sensitivity

### Case and Diacritic Insensitivity

The `$text` operator defers to the case and diacritic
insensitivity of the `text` index. The version 3 `text` index is
diacritic insensitive and expands its case insensitivity to include the
Cyrillic alphabet as well as characters with diacritics. For details,
see text Index Case Insensitivity and text Index Diacritic
Insensitivity.

The following example performs a case and diacritic insensitive text
query for the terms `сы́рники` or `CAFÉS`:

```javascript
db.articles.find( { $text: { $search: "сы́рники CAFÉS" } } )
```

Using the version 3 `text` index, the operation matches the following
documents.

```javascript
{ "_id" : 6, "subject" : "Сырники", "author" : "jkl", "views" : 80 }
{ "_id" : 5, "subject" : "Café Con Leche", "author" : "abc", "views" : 200 }
{ "_id" : 8, "subject" : "Cafe con Leche", "author" : "xyz", "views" : 10 }
```

With previous versions of the `text` index, the query would not
match any document.

**See also:**

- text-operator-case-sensitivity
- text-operator-diacritic-sensitivity
- match-operation-stemmed-words
- /core/index-text

### Case Sensitivity

To enable case sensitivity, specify `$caseSensitive: true`. Specifying
`$caseSensitive: true` may impact performance.

#### Case Sensitivity with a Term

The following example performs a case sensitive query for the term
`Coffee`:

```javascript
db.articles.find( { $text: { $search: "Coffee", $caseSensitive: true } } )
```

The operation matches just the following document:

```json
{ "_id" : 2, "subject" : "Coffee Shopping", "author" : "efg", "views" : 5 }
```

**See also:**

- text-operator-case-sensitivity
- case-sensitivity-and-stemming

#### Case Sensitivity with an Exact String

The following example performs a case sensitive query for the exact multi-word
string `Café Con Leche`:

```javascript
db.articles.find( {
   $text: { $search: "\"Café Con Leche\"", $caseSensitive: true }
} )
```

The operation matches just the following document:

```json
{ "_id" : 5, "subject" : "Café Con Leche", "author" : "abc", "views" : 200 }
```

**See also:**

- case-sensitivity-and-stemming
- text-operator-case-sensitivity

#### Case Sensitivity with Negated Term

A *negated* term is a term that is prefixed by a minus sign `-`. If
you negate a term, the `$text` operator will exclude the
documents that contain those terms from the results. You can also
specify case sensitivity for negated terms.

The following example performs a case sensitive query for documents
that contain the word `Coffee` but do **not** contain the lower-case
term `shop`, or more precisely the stemmed version of the words:

```javascript
db.articles.find( { $text: { $search: "Coffee -shop", $caseSensitive: true } } )
```

The operation matches the following document:

```json
{ "_id" : 2, "subject" : "Coffee Shopping", "author" : "efg" }
```

**See also:**

- case-sensitivity-and-stemming
- text-operator-term-negation

### Diacritic Sensitivity

To enable diacritic sensitivity with a version 3 text index, specify `$diacriticSensitive: true`.
Specifying `$diacriticSensitive: true` may impact performance.

#### Diacritic Sensitivity with a Term

The following example performs a diacritic sensitive text query on the
term `CAFÉ`, or more precisely the stemmed version of the word:

```javascript
db.articles.find( { $text: { $search: "CAFÉ", $diacriticSensitive: true } } )
```

The operation only matches the following document:

```javascript
{ "_id" : 5, "subject" : "Café Con Leche", "author" : "abc" }
```

**See also:**

- diacritic-sensitivity-and-stemming
- text-operator-diacritic-sensitivity
- text-operator-case-sensitivity

#### Diacritic Sensitivity with Negated Term

The `$diacriticSensitive` option applies also to negated terms. A
negated term is a term that is prefixed by a minus sign `-`. If you
negate a term, the `$text` operator will exclude the documents that
contain those terms from the results.

The following example performs a diacritic sensitive text query for
documents that contain the term `leches` but not the term `cafés`,
or more precisely the stemmed version of the words:

```javascript
db.articles.find(
  { $text: { $search: "leches -cafés", $diacriticSensitive: true } }
)
```

The operation matches the following document:

```javascript
{ "_id" : 8, "subject" : "Cafe con Leche", "author" : "xyz" }
```

**See also:**

- diacritic-sensitivity-and-stemming
- text-operator-diacritic-sensitivity
- text-operator-case-sensitivity

### Relevance Score Examples

#### Return the Relevance Score

The following example performs a text query for the term `cake` and
uses the `$meta` operator in the projection document to
append the relevance score to each matching document:

```javascript
db.articles.find(
   { $text: { $search: "cake" } },
   { score: { $meta: "textScore" } }
)
```

The returned document includes an *additional* field `score` that
contains the document's relevance score:

```javascript
{ "_id" : 3, "subject" : "Baking a cake", "author" : "abc", "views" : 90, "score" : 0.75 }
```

**See also:**

`$meta`

#### Sort by Relevance Score

- You can specify the `{ $meta: "textScore" }` 
  expression in the `sort()` without also specifying the 
  expression in the projection. For example:

  ```javascript
  db.articles.find( 
     { $text: { $search: "cake" } } 
  ).sort( { score: { $meta: "textScore" } } )
  ```

  As a result, you can sort the resulting documents by their
  relevance without projecting the `textScore`.

- If you include the `{ $meta: "textScore" }` expression 
  in both the projection and 
  `sort()`, the projection and sort documents can have 
  different field names for the expression.

  | For example, in the following operation, the projection uses a
   field named  `score` for the expression and the
   `sort()` uses the field named `ignoredName`.

  ```javascript
  db.articles.find(
     { $text: { $search: "cake" } } , 
     { score: { $meta: "textScore" } }
  ).sort( { ignoredName: { $meta: "textScore" } } )
  ```

**See also:**

`$meta`

#### Return Top 2 Matching Documents

Use the `limit()` method in conjunction with a
`sort()` to return the top `n` matching documents.

The following example queries for the term `coffee` and sorts the
results by the descending score, limiting the results to the top two
matching documents:

```javascript
db.articles.find(
   { $text: { $search: "coffee" } },
   { score: { $meta: "textScore" } }
).sort( { score: { $meta: "textScore" } } ).limit(2)
```

**See also:**

`$meta`

#### $text with Additional Query and Sort Expressions

The following example matches documents where the `author` equals
`"xyz"` and the indexed field `subject` contains the terms
`coffee` or `bake`. The operation also specifies a sort order of
ascending `date`, then descending relevance score:

```javascript
db.articles.find(
   { author: "xyz", $text: { $search: "coffee bake" } },
   { score: { $meta: "textScore" } } 
).sort( { date: 1, score: { $meta: "textScore" } } )
```

**See also:**

/tutorial/text-search-in-aggregation
