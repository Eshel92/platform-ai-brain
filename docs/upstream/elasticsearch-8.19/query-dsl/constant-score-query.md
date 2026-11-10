<!-- Converted from query-dsl/constant-score-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Constant score query

Wraps a filter query and returns every matching
document with a relevance score equal to the `boost`
parameter value.

```console
GET /_search
{
  "query": {
    "constant_score": {
      "filter": {
        "term": { "user.id": "kimchy" }
      },
      "boost": 1.2
    }
  }
}
```

#### Top-level parameters for `constant_score`

`filter`::
(Required, query object) Filter query you wish to run.
Any returned documents must match this query.

Filter queries do not calculate relevance scores. To
speed up performance, Elasticsearch automatically caches frequently used filter queries.

`boost`::
(Optional, float) Floating point number used as the constant
relevance score for every document matching the
`filter` query. Defaults to `1.0`.
