<!-- Converted from reference/operator/query/text.txt (reStructuredText). Includes are inlined. -->

# $text (query predicate operator)

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

This page describes the `$text` operator for self-managed deployments.

## Definition

**`$text`**

`$text` performs a text query on fields indexed with a
text index. 

## Compatibility

You can use `$text` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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

The `$text` operator accepts these fields:

| Field | Type | Description |
|---|---|---|
| `$search` | string | A string of terms that MongoDB parses and uses to query the text index. MongoDB performs a logical `OR` query on the terms unless you specify an exact string. See text-query-operator-behavior for details. |
| `$language` | string | .. _language-field: Optional. The language that determines the stop words, stemmer, and tokenizer rules. Defaults to the index language. For supported languages, see text-search-languages. If you specify a `default_language` value of `none`, the text index parses through each word in the field, including stop words, and ignores suffix stemming. |
| `$caseSensitive` | boolean | Optional. Enables case sensitivity. Defaults to `false`. See text-operator-case-sensitivity. |
| `$diacriticSensitive` | boolean | Optional. Enables diacritic sensitivity for version 3 text indexes. Defaults to `false`. Earlier text index versions are always diacritic sensitive. See text-operator-diacritic-sensitivity. |

By default, `$text` does not sort results by score. See
text-operator-text-score for details on score sorting.

## Behavior

### Restrictions

- A query can specify only one `$text` expression.

- `$text` cannot appear in `$nor` expressions.

- `$text` cannot appear in `$elemMatch` query or
  projection expressions.

- All `$or` clauses must be indexed to use `$text`.

- .. include:: /includes/fact-hint-text-query-restriction.rst

- Queries with `$text` cannot use `$natural` sort.

- .. include:: /includes/fact-special-indexes-and-text.rst

- .. include:: /includes/extracts/views-unsupported-text-search.rst

- Stable API V1 does not support `$text`
  for index creation.

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

In the `$search` field, specify the words that MongoDB uses to
query the text index.

**Note:**

The `$search` field differs from the MongoDB Atlas $search
aggregation stage.
The `$search` stage provides full-text search and is
available only on MongoDB Atlas.

#### Exact Strings

To match an exact multi-word string instead of individual terms,
enclose the string in escaped double quotes (`\"`): as in:

```javascript
"\"ssl certificate\""
```

If the `$search` string of a `$text` operation includes a multi-word string
and individual terms, `$text` only matches the documents that include the
multi-word string.

For example, this `$search` string returns documents with the
exact string `"ssl certificate"`:

```javascript
"\"ssl certificate\" authority key"
```

#### Negations

Prefix a word with a hyphen-minus (`-`) to negate it:

- Negated words exclude documents that contain the negated word
  from the result set.

- A string with only negated words matches no documents.

- Hyphenated words like `pre-market` are not negations.
  MongoDB treats the hyphen as a delimiter. To negate
  `market`, use `pre -market`.

MongoDB applies all negations to the operation with logical `AND`.

### Match Operation

#### Stop Words

MongoDB ignores language-specific stop words such as `the` and
`and` in English.

#### Stemmed Words

With case and diacritic insensitivity, `$text` matches the
complete *stemmed* word. If a document field contains
`blueberry`, a `$search` term of `blue` does not match.
However, `blueberry` or `blueberries` do match.

##### Case Sensitivity and Stemmed Words

With case sensitivity enabled (`$caseSensitive: true`), if the suffix stem 
contains uppercase letters, `$text` matches the exact word.

##### Diacritic Sensitivity and Stemmed Words

With diacritic sensitivity enabled
(`$diacriticSensitive: true`), if the suffix stem contains
diacritic marks, `$text` matches the exact word.

### Case Insensitivity

`$text` defaults to the case insensitivity of the text index:

- The version 3 text index is
  case insensitive for Latin characters with or without diacritics
  and non-Latin alphabets like Cyrillic.

- Earlier versions are case insensitive for Latin characters
  without diacritics (`[A-z]`).

#### Enabling Case Sensitivity

Specify `$caseSensitive: true` to enable case sensitivity when
the text index is case insensitive.

#### Case Sensitivity Process

When `$caseSensitive: true` and the text index is case
insensitive, `$text`:

- Queries the text index for case-insensitive and
  diacritic-insensitive matches.

- Filters results to return only documents matching the specified
  case.

When `$caseSensitive: true` and the suffix stem contains
uppercase letters, `$text` matches the exact word.

Enabling `$caseSensitive: true` may reduce performance.

### Diacritic Insensitivity

`$text` defaults to the diacritic insensitivity of the
text index:

- Version 3 text index is diacritic insensitive.
  The index does not distinguish between characters with diacritic
  marks and their non-marked counterparts (`é`, `ê`, `e`).

- Earlier versions are diacritic sensitive.

#### Enabling Diacritic Sensitivity

Specify `$diacriticSensitive: true` to enable diacritic
sensitivity with version 3 text indexes.

Earlier text index versions are always diacritic sensitive, so
`$diacriticSensitive` has no effect.

#### Diacritic Sensitivity Process

With version 3 text indexes and `$diacriticSensitive: true`,
`$text`:

- Queries the diacritic-insensitive text index.

- Filters results to return only documents matching the diacritic
  marks in the specified terms.

Enabling `$diacriticSensitive: true` may reduce performance.

With earlier text index versions, `$diacriticSensitive: true`
queries the already diacritic-sensitive text index.

When `$diacriticSensitive: true` and the suffix stem contains
diacritic marks, `$text` matches the exact word.

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

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The examples assume a version 3 text
index on the `title` and `fullplot` fields:

```javascript
db.movies.createIndex( { title: "text", fullplot: "text" } )
```

### Search for a Single Word

This example specifies `baseball` in the `$search` string. The
query returns documents containing the stemmed version of
`baseball` in the indexed `title` or `fullplot` fields:

```javascript
```

Output:

```javascript
```

### Match Any Search Term

A space-delimited `$search` string performs a logical `OR` on
each term. MongoDB returns documents containing any of the terms.

This example specifies two space-delimited terms. The query returns
documents containing the stemmed versions of `baseball` **or**
`colorado` in the indexed `title` or `fullplot` fields:

```javascript
```

Output:

```javascript
```

### Search for an Exact String

Escape the quotes to match an exact multi-word string.

This example matches the exact phrase `ken burns`:

```javascript
```

Output:

```javascript
```

This example performs a logical OR of two exact strings:

```javascript
```

Output:

```javascript
```

### Exclude Documents That Contain a Term

Prefix a term with `-` to exclude documents containing that term.

This example matches documents containing `baseball` or
`colorado` but not `sport` (stemmed versions):

```javascript
```

Output:

```javascript
```

### Relevance Score Examples

#### Return the Relevance Score

This example queries for `baseball` and uses
`$meta` to append the relevance score to each
matching document. The returned document includes a `score`
field with the relevance score:

```javascript
```

Output:

```javascript
```

#### Return Top 2 Matching Documents

Use `limit()` with `sort()` to
return the top matching documents.

This example queries for `baseball` **or** `colorado`, sorts by
descending score, and limits results to the top two documents:

```javascript
```

Output:

```javascript
```

#### Combine $text with Other Query and Sort Operations

This example matches documents where `runtime` is greater
than `1000` and the indexed fields contain `baseball` or
`colorado`. It sorts by ascending `year`, then descending
relevance score:

```javascript
```

Output:

```javascript
```

### Query a Different Language

The rest of the examples on this page use an `articles` collection with a
version 3 text index on `subject`:

```javascript
db.articles.createIndex( { subject: "text" } )
```

The collection contains the following documents:

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

Use `$language` to specify the language that determines stop
words, stemmer, and tokenizer rules for the `$search` string.

If you specify a `default_language` value of `none`, the text index
parses through each word in the field, including stop words, and ignores
suffix stemming.

This example specifies `es` (Spanish) as the language:

```javascript
```

Output:

```javascript
```

You can also specify languages by name, such as `spanish`. See
text-search-languages for supported languages.

### Sort by Relevance Score

You can specify the `{ $meta: "textScore" }`
expression in the `sort()` without also specifying
the expression in the projection. For example:

```javascript
db.articles.find(
   { $text: { $search: "cake" } }
).sort( { score: { $meta: "textScore" } } )
```

As a result, you can sort the resulting documents by their relevance
without projecting the `textScore`.

If you include the `{ $meta: "textScore" }`
expression in both the projection and
`sort()`, the projection and sort documents can have
different field names for the expression. For example, in the
following operation, the projection uses a field named `score` for
the expression and the `sort()` uses the field named
`ignoredName`:

```javascript
db.articles.find(
   { $text: { $search: "cake" } },
   { score: { $meta: "textScore" } }
).sort( { ignoredName: { $meta: "textScore" } } )
```

### Case and Diacritic Insensitivity

`$text` defaults to the case and diacritic insensitivity of the
text index. Version 3 text indexes are diacritic insensitive and
case insensitive for Latin characters with diacritics and non-Latin
alphabets like Cyrillic. See text Index Case Insensitivity and text Index Diacritic
Insensitivity.

This example performs a case and diacritic insensitive query.
Using version 3 text indexes, the query matches documents
containing the stemmed versions of the search terms:

```javascript
```

Output:

```javascript
```

Earlier text index versions would not match any documents.

### Case Sensitivity

Enable case sensitivity with `$caseSensitive: true`. This may
reduce performance.

#### Case-Sensitive Term Search

This example performs a case-sensitive query for `Coffee`:

```javascript
```

Output:

```javascript
```

#### Case-Sensitive Exact String Search

This example performs a case-sensitive query for an exact
multi-word string:

```javascript
```

Output:

```javascript
```

#### Case-Sensitive Negated Term Search

You can use case sensitivity with negated terms (terms prefixed
with `-`).

This example performs a case-sensitive query for documents
containing `Coffee` but not `shop` (stemmed versions):

```javascript
```

Output:

```javascript
```

### Diacritic Sensitivity

Enable diacritic sensitivity with version 3 text indexes using `$diacriticSensitive: true`.
This may reduce performance.

#### Diacritic-Sensitive Term Search

This example performs a diacritic-sensitive query for `CAFÉ`
(stemmed version):

```javascript
```

Output:

```javascript
```

#### Diacritic-Sensitive Negated Term Search

You can use diacritic sensitivity with negated terms (terms
prefixed with `-`).

This example performs a diacritic-sensitive query for documents
containing `leches` but not `cafés` (stemmed versions):

```javascript
```

Output:

```javascript
```

**See also:**

- index-type-text
- match-operation-stemmed-words
- text-operator-exact-string
- text-operator-term-negation
- text-operator-case-sensitivity
- case-sensitivity-and-stemming
- text-operator-diacritic-sensitivity
- diacritic-sensitivity-and-stemming
- `$meta`
- text-agg
