<!-- Converted from core/text-search-operators.txt (reStructuredText). Includes are inlined. -->

# Text Search Operators (Self-Managed Deployments)

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

## Query Framework

Use the `$text` query operator to perform text searches on a
collection with a text index.

`$text` tokenizes the search string using whitespace and most
punctuation as delimiters, and perform a logical `OR` of all such
tokens in the search string.

For example, you could use the following query to find all stores
containing any terms from the list "coffee", "shop", and "java" in 
the `stores` collection:

```javascript
db.stores.find( { $text: { $search: "java coffee shop" } } )
```

Use the `$meta` query operator to obtain and sort by the
relevance score of each matching document. For example, to order a
list of coffee shops in order of relevance, run the following:

```javascript
db.stores.find(
   { $text: { $search: "coffee shop cake" } },
   { score: { $meta: "textScore" } }
).sort( { score: { $meta: "textScore" } } )
```

For more information on the `$text` and `$meta`
operators, including restrictions and behavior, see:

- `$text Reference Page`

- $text Query Examples

- `$meta` projection operator

## Aggregation Pipeline

When working with aggregation pipelines, use
`$match` with a `$text` expression to execute a text
search query. To sort the results in order of relevance score, use the
`$meta` *aggregation operator* in the `$sort`
stage [#meta-aggregation]_.

For more information and examples of `$text` in
aggregation pipelines, see
/tutorial/text-search-in-aggregation.

For data hosted on MongoDB Atlas, Atlas Search
provides the $search
aggregation stage to perform full-text search on your collections.
