<!-- Converted from tutorial/text-search-in-aggregation.txt (reStructuredText). Includes are inlined. -->

# $text in the Aggregation Pipeline on Self-Managed Deployments

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

In the aggregation pipeline, text search is available via the use of
the `$text` query operator in the `$match` stage.

## Restrictions

For general `$text` operator restrictions, see operator
restrictions.

In addition, text search in the aggregation pipeline has the following
restrictions:

- The `$match` stage that includes a `$text` must be
  the **first** stage in the pipeline.

- A `$text` operator can only occur once in the stage.

- The `$text` operator expression cannot appear in
  `$or` or `$not` expressions.

- `$text`, by default, does not return the matching documents in order
  of matching scores. To sort by descending score, use the
  `$meta` aggregation expression in the `$sort` stage.

## Text Score

The `$text` operator assigns a score to each result document. The
score represents the relevance of a document to a given query. The score
can be part of a `$sort` pipeline specification as well as part of the
projection expression. The `{ $meta: "textScore" }` expression
provides information on the processing of the `$text` operation. See
`$meta` for details on accessing the score for projection or sort.

The metadata is only available after the `$match` stage that
includes the `$text` operation.

## Examples

The following examples assume a collection `articles` that has a text
index on the field `subject`:

```javascript
db.articles.createIndex( { subject: "text" } )
```

### Calculate the Total Views for Articles that Contains a Word

The following aggregation searches for the term `cake` in the
`$match` stage and calculates the total `views` for the
matching documents in the `$group` stage.

```javascript
db.articles.aggregate(
   [
     { $match: { $text: { $search: "cake" } } },
     { $group: { _id: null, views: { $sum: "$views" } } }
   ]
)
```

### Return Results Sorted by Text Search Score

To sort by the text search score, include a `{$meta:
"textScore"}` expression in the `$sort` stage. The
following example matches on *either* the term `cake` or `tea`,
sorts by the `textScore` in descending order, and returns only the
`title` field in the results set.

```javascript
db.articles.aggregate(
   [
     { $match: { $text: { $search: "cake tea" } } },
     { $sort: { score: { $meta: "textScore" } } },
     { $project: { title: 1, _id: 0 } }
   ]
)
```

The specified metadata determines the sort order. For example, the
`"textScore"` metadata sorts in descending order. See
`$meta` for more information on metadata as well as an
example of overriding the default sort order of the metadata.

### Match on Text Score

The `"textScore"` metadata is available for projections, sorts, and
conditions subsequent the `$match` stage that includes the
`$text` operation.

The following example matches on *either* the term `cake` or `tea`,
projects the `title` and the `score` fields, and then returns only
those documents with a `score` greater than `1.0`.

```javascript
db.articles.aggregate(
   [
     { $match: { $text: { $search: "cake tea" } } },
     { $project: { title: 1, _id: 0, score: { $meta: "textScore" } } },
     { $match: { score: { $gt: 1.0 } } }
   ]
)
```

### Specify a Language for Text Search

The following aggregation searches in spanish for documents that
contain the term `saber` but not the term `claro` in the
`$match` stage and calculates the total `views` for the
matching documents in the `$group` stage.

```javascript
db.articles.aggregate(
   [
     { $match: { $text: { $search: "saber -claro", $language: "es" } } },
     { $group: { _id: null, views: { $sum: "$views" } } }
   ]
)
```

## `$search` Stage in Atlas Search

For data hosted on MongoDB Atlas, Atlas Search
provides the $search
aggregation stage to perform full-text search on your collections.
