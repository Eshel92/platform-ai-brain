<!-- Converted from reference/operator/aggregation/mergeObjects.txt (reStructuredText). Includes are inlined. -->

# $mergeObjects (accumulator operator)

## Definition

**`$mergeObjects`**

Returns a document created by combining the input documents
for each group.

The `$mergeObjects` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$mergeObjects` when used as an
**accumulator**. Accumulators return an aggregated value
across a group of input documents.

You can also use the `$mergeObjects (expression)`, which merges an array of documents into a single
document.

## Syntax

```none
{ $mergeObjects: <expression> }
```

The `<expression>` can be any valid expression that evaluates to a document.

## Behavior

`$mergeObjects` ignores `null` input values. If all input
values are `null`, `$mergeObjects` returns an empty document
`{ }`.

`$mergeObjects` overwrites field values as it merges documents. If
multiple input documents contain the same field name, the output
contains the value from the *last* input document that contains the
conflicting field.

## Example

Create a `movieReviews` collection:

```javascript
db.movieReviews.insertMany( [
   {
      title: "Galactic Odyssey",
      source: "filmCritic",
      data: { rating: 8.1, votes: 1482903 }
   },
   {
      title: "Galactic Odyssey",
      source: "viewerVault",
      data: { tomatometer: 79, audienceScore: 85 }
   },
   {
      title: "Neon Horizon",
      source: "filmCritic",
      data: { rating: 7.4, votes: 983201 }
   },
   {
      title: "Neon Horizon",
      source: "viewerVault",
      data: { tomatometer: 68, audienceScore: 74 }
   },
   {
      title: "The Last Protocol",
      source: "filmCritic",
      data: { rating: 8.7, votes: 2104567 }
   },
   {
      title: "The Last Protocol",
      source: "viewerVault",
      data: { tomatometer: 91, audienceScore: 88 }
   }
] )
```

Each movie has two documents:

- One from filmCritic with `rating` and `votes` fields.
- One from viewerVault with `tomatometer` and `audienceScore`
  fields.

Because the two source documents have different field names,
`$mergeObjects` can combine them into a complete profile that includes
all four fields.

The following pipeline uses `$mergeObjects` in a
`$group` stage to combine the review data from each
source into a single document for each movie:

```javascript
```

Output:

```javascript
```

In the preceding pipeline:

- `$group` groups documents by `title` and uses
  `$mergeObjects` to merge the `data` sub-documents from
  each source. Because the FilmCritic and ViewerVault documents
  contain different field names, the merged result includes
  all fields from both sources.
- `$sort` sorts the results alphabetically by title.
