<!-- Converted from reference/expression/mergeObjects.txt (reStructuredText). Includes are inlined. -->

# $mergeObjects (expression)

## Definition

**`$mergeObjects`**

Merges an array of documents into a single document.

**Note:** Disambiguation

This page describes `$mergeObjects` when used as an
**expression**, which merges an array of documents.

You can also use the `$mergeObjects (accumulator)`, which returns a merged document across a group of
input documents.

## Syntax

When used as an expression, `$mergeObjects` has this syntax:

```none
{ $mergeObjects: <expression> }
```

The `<expression>` operand can be either:

- A single expression that evaluates to an array of documents to merge.
  For example, `$blogPosts` where the document field `blogPosts`
  contains an array of documents.

- An array of expressions, each of which evaluates to a document. For
  example, `[ "$doc1", "$doc2", "$doc3" ]` where each document field
  contains a single document.

## Behavior

`$mergeObjects` ignores `null` input values. If all input
values are `null`, `$mergeObjects` returns an empty document
`{ }`.

`$mergeObjects` overwrites field values as it merges documents. If
multiple input documents contain the same field name, the output
contains the value from the *last* input document that contains the
conflicting field.

| Example | Results |
|---|---|
| .. code-block:: json :copyable: false { $mergeObjects: [ { a: 1 }, null ] } | .. code-block:: json :copyable: false { a: 1 } |
| .. code-block:: json :copyable: false { $mergeObjects: [ null, null ] } | .. code-block:: json :copyable: false { } |
| .. code-block:: json :copyable: false { $mergeObjects: [ { a: 1 }, { a: 2, b: 2 }, { a: 3, c: 3 } ] } | .. code-block:: json :copyable: false { a: 3, b: 2, c: 3 } |
| .. code-block:: json :copyable: false { $mergeObjects: [ { a: 1 }, { a: 2, b: 2 }, { a: 3, b: null, c: 3 } ] } | .. code-block:: json :copyable: false { a: 3, b: null, c: 3 } |

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following pipeline uses `$mergeObjects` in
`$replaceWith` to merge each movie's `imdb` and
`tomatoes.critic` sub-documents into a single `ratings` document.
Both sub-documents contain a `rating` field, so `$mergeObjects`
overwrites the `imdb` rating with the `tomatoes.critic` rating.
Unique fields from each sub-document are preserved in the result.

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$match` filters to Action movies from 2010 with an
  existing `imdb.rating` and `tomatoes.critic.rating`.
- `$sort` sorts documents alphabetically by `title`.
- `$limit` restricts the output to 5 documents to improve
  readability.
- `$replaceWith` uses `$mergeObjects` to merge
  `$imdb` and `$tomatoes.critic` into a `ratings` field.

  - Because both sub-documents contain a `rating` field,
    `$mergeObjects` uses the value from `tomatoes.critic` (the last
    argument).
  
  - The unique fields `votes` and `id` from `imdb`, and
    `numReviews` and `meter` from `tomatoes.critic`, are all
    preserved.
