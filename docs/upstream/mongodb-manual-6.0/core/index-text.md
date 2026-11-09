<!-- Converted from core/index-text.txt (reStructuredText). Includes are inlined. -->

# Text Indexes on Self-Managed Deployments

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

## Overview

To run text search queries on self-managed deployments, you must have a
text index on your collection. MongoDB
provides text indexes to support text search queries on string content.
Text indexes can include any field whose value is a string or an array
of string elements. A collection can only have **one** text search
index, but that index can cover multiple fields.

## Compatibility

You can use text indexes for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).
To learn more about managing indexes for deployments hosted in MongoDB
Atlas, see Create, View, Drop, and Hide Indexes.

## Versions

The text index is available in three versions.  By default, MongoDB uses
version 3 with new text indexes.

To override the default and use an older version, use the `textIndexVersion` 
option when you create the index.

## Create Text Index

**Important:**

A collection can have at most **one** `text` index.

Atlas Search (available in [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)) supports
multiple full-text search indexes on a single collection. To learn more,
see the Atlas Search documentation.

To create a `text` index, use the
`db.collection.createIndex()` method. To index a field that
contains a string or an array of string elements, include the field and
specify the string literal `"text"` in the index document, as in the
following example:

```javascript
db.reviews.createIndex( { comments: "text" } )
```

You can index multiple fields for the `text` index. The following
example creates a `text` index on the fields `subject` and
`comments`:

```javascript
db.reviews.createIndex(
   {
     subject: "text",
     comments: "text"
   }
 )
```

A compound index can include `text`
index keys in combination with ascending/descending index keys. For
more information, see text-index-compound.

In order to drop a `text` index, use the index name. See
drop-text-index for more information.

### Specify Weights

For a `text` index, the *weight* of an indexed field denotes the
significance of the field relative to the other indexed fields in terms
of the text search score.

For each indexed field in the document, MongoDB multiplies the number
of matches by the weight and sums the results. Using this sum, MongoDB
then calculates the score for the document. See `$meta`
operator for details on returning and sorting by text scores.

The default weight is 1 for the indexed fields. To adjust the weights
for the indexed fields, include the `weights` option in the
`db.collection.createIndex()` method.

For more information using weights to control the results of a text
search, see /tutorial/control-results-of-text-search.

### Wildcard Text Indexes

**Note:**

Wildcard Text Indexes are distinct from wildcard-index-core. 
Wildcard indexes cannot support queries using the `$text` 
operator. 

While Wildcard Text Indexes and wildcard-index-core share the
wildcard `$**` field pattern, they are distinct index types. Only 
Wildcard Text Indexes support the `$text` operator. 

When creating a `text` index on multiple fields, you can also use the
wildcard specifier (`$**`). With a wildcard text index, MongoDB
indexes every field that contains string data for each document in the
collection. The following example creates a text index using the
wildcard specifier:

```javascript
db.collection.createIndex( { "$**": "text" } )
```

This index allows for text search on all fields with string content.
Such an index can be useful with highly unstructured data if it is
unclear which fields to include in the text index or for ad-hoc
querying.

Wildcard text indexes are `text` indexes on multiple fields. As such,
you can assign weights to specific fields during index creation to
control the ranking of the results. For more information using weights
to control the results of a text search, see
/tutorial/control-results-of-text-search.

Wildcard text indexes, as with all text indexes, can be part of a
compound indexes. For example, the following creates a compound index
on the field `a` as well as the wildcard specifier:

```javascript
db.collection.createIndex( { a: 1, "$**": "text" } )
```

As with all compound text indexes, since
the `a` precedes the text index key, in order to perform a
`$text` search with this index, the query predicate must include
an equality match conditions `a`. For information on compound text
indexes, see Compound Text Indexes.

## Case Insensitivity

The version 3 `text` index supports the common `C`, simple `S`,
and for Turkish languages, the special `T` case foldings as specified
in [Unicode 8.0 Character Database Case Folding](http://www.unicode.org/Public/8.0.0/ucd/CaseFolding.txt).

The case foldings expands the case insensitivity of the `text`
index to include characters with diacritics, such as `é` and
`É`, and characters from non-Latin alphabets, such as "И" and "и"
in the Cyrillic alphabet.

Version 3 of the `text` index is also diacritic insensitive. As such, the index also does not
distinguish between `é`, `É`, `e`, and `E`.

Previous versions of the `text` index are case insensitive for
`[A-z]` only; i.e. case insensitive for non-diacritics Latin
characters only . For all other characters, earlier versions of the
text index treat them as distinct.

## Diacritic Insensitivity

With version 3, `text` index is diacritic insensitive. That is, the
index does not distinguish between characters that contain diacritical
marks and their non-marked counterpart, such as `é`, `ê`, and
`e`. More specifically, the `text` index strips the characters
categorized as diacritics in [Unicode 8.0 Character Database Prop List](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt).

Version 3 of the `text` index is also case insensitive to characters with diacritics. As
such, the index also does not distinguish between `é`, `É`, `e`,
and `E`.

Previous versions of the `text` index treat characters with
diacritics as distinct.

## Tokenization Delimiters

For tokenization, version 3 `text` index uses the delimiters
categorized under `Dash`, `Hyphen`, `Pattern_Syntax`,
`Quotation_Mark`, `Terminal_Punctuation`, and `White_Space` in
[Unicode 8.0 Character Database Prop List](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt).

For example, if given a string ``"Il a dit qu'il «était le meilleur
joueur du monde»"`, the `text` index treats `«`, `»``, and spaces
as delimiters.

Previous versions of the index treat `«` as part of the term
`"«était"` and `»` as part of the term `"monde»"`.

## Index Entries

`text` index tokenizes and stems the terms in the indexed fields for
the index entries. `text` index stores one index entry for each
unique stemmed term in each indexed field for each document in the
collection. The index uses simple language-specific suffix stemming.

## Supported Languages and Stop Words

MongoDB supports text search for various languages. `text` indexes
drop language-specific stop words (e.g. in English, `the`, `an`,
`a`, `and`, etc.) and use simple language-specific suffix stemming.
For a list of the supported languages, see text-search-languages.

If you specify a `default_language` value of `none`, the text index
parses through each word in the field, including stop words, and ignores
suffix stemming.

To specify a language for the `text` index, see
/tutorial/specify-language-for-text-index.

## `sparse` Property

`text` indexes are always sparse and ignore the
sparse option. If a document lacks a `text` index field (or
the field is `null` or an empty array), MongoDB does not add an entry
for the document to the `text` index. For inserts, MongoDB inserts
the document but does not add to the `text` index.

For a compound index that includes a `text` index key along with keys
of other types, only the `text` index field determines whether the
index references a document. The other keys do not determine whether
the index references the documents or not.

## Restrictions

### One Text Index Per Collection

A collection can have at most **one** `text` index.

Atlas Search (available in [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)) supports
multiple full-text search indexes on a single collection. To learn more,
see the Atlas Search documentation.

### Text Search and Hints

If a query includes a `$text` expression, you cannot use
`hint()` to specify which index to use for the query.

## Text Search and Phrases

If the `$search` string of a `$text` operation includes a multi-word string
and individual terms, `$text` only matches the documents that include the
multi-word string.

### Text Index and Sort

Sort operations cannot obtain sort order from a `text` index, even
from a compound text index; i.e. sort
operations cannot use the ordering in the text index.

### Compound Index

A compound index can include a `text`
index key in combination with ascending/descending index keys. However,
these compound indexes have the following restrictions:

- A compound `text` index cannot include any other special index
  types, such as multi-key or
  geospatial index fields.

- If the compound text index includes keys **preceding** the text index
  key, to use `$text`, the query predicate must
  include **equality match conditions** on the preceding keys.

- When creating a compound `text` index, all `text` index keys must
  be listed adjacently in the index specification document.

See also text-index-and-sort for additional limitations.

For an example of a compound text index, see
/tutorial/limit-number-of-items-scanned-for-text-search.

### Drop a Text Index

To drop a `text` index, pass the *name* of the index to the
`db.collection.dropIndex()` method. To get the name of the
index, run the `db.collection.getIndexes()` method.

For information on the default naming scheme for `text` indexes as
well as overriding the default name, see
/tutorial/avoid-text-index-name-limit.

### Collation Option

`text` indexes only support simple binary comparison and do not
support collation.

To create a `text` index on a a collection that has a non-simple
collation, you must explicitly specify ``{collation: {locale: "simple"}
}`` when creating the index.

## Storage Requirements and Performance Costs

`text` indexes have the following storage requirements and
performance costs:

- `text` indexes can be large. They contain one index entry for each
  unique post-stemmed word in each indexed field for each document
  inserted.

- Building a `text` index is very similar to building a large
  multi-key index and will take longer than building a simple ordered
  (scalar) index on the same data.

- When building a large `text` index on an existing collection,
  ensure that you have a sufficiently high limit on open file
  descriptors. See the recommended settings.

- `text` indexes will impact insertion throughput because MongoDB
  must add an index entry for each unique post-stemmed word in each
  indexed field of each new source document.

- Additionally, `text` indexes do not store phrases or information
  about the proximity of words in the documents. As a result, phrase
  queries will run much more effectively when the entire collection
  fits in RAM.

## Text Search Support

The `text` index supports `$text` query operations. For
examples of text search, see the `$text reference page`.
For examples of `$text` operations in aggregation pipelines, see
/tutorial/text-search-in-aggregation.
