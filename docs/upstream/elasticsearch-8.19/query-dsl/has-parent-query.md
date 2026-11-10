<!-- Converted from query-dsl/has-parent-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Has parent query

Returns child documents whose joined parent document matches a
provided query. You can create parent-child relationships between documents in
the same index using a join field mapping.

**Warning:**
Because it performs a join, the `has_parent` query is slow compared to other queries.
Its performance degrades as the number of matching parent documents increases.
Each `has_parent` query in a search can increase query time significantly.

#### Example request

##### Index setup

To use the `has_parent` query, your index must include a join
field mapping. For example:

```console
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "my-join-field": {
        "type": "join",
        "relations": {
          "parent": "child"
        }
      },
      "tag": {
        "type": "keyword"
      }
    }
  }
}

```

##### Example query

```console
GET /my-index-000001/_search
{
  "query": {
    "has_parent": {
      "parent_type": "parent",
      "query": {
        "term": {
          "tag": {
            "value": "Elasticsearch"
          }
        }
      }
    }
  }
}
```

#### Top-level parameters for `has_parent`

`parent_type`::
(Required, string) Name of the parent relationship mapped for the
join field.

`query`::
(Required, query object) Query you wish to run on parent documents of the
`parent_type` field. If a parent document matches the search, the query returns
its child documents.

`score`::
(Optional, Boolean) Indicates whether the <<query-filter-context,relevance
score>> of a matching parent document is aggregated into its child documents.
Defaults to `false`.

If `false`, Elasticsearch ignores the relevance score of the parent document. Elasticsearch also
assigns each child document a relevance score equal to the `query`'s `boost`,
which defaults to `1`.

If `true`, the relevance score of the matching parent document is aggregated
into its child documents' relevance scores.

`ignore_unmapped`::
(Optional, Boolean) Indicates whether to ignore an unmapped `parent_type` and
not return any documents instead of an error. Defaults to `false`.

If `false`, Elasticsearch returns an error if the `parent_type` is unmapped.

You can use this parameter to query multiple indices that may not contain the
`parent_type`.

#### Notes

##### Sorting

You cannot sort the results of a `has_parent` query using standard
sort options.

If you need to sort returned documents by a field in their parent documents, use
a `function_score` query and sort by `_score`. For example, the following query
sorts returned documents by the `view_count` field of their parent documents.

```console
GET /_search
{
  "query": {
    "has_parent": {
      "parent_type": "parent",
      "score": true,
      "query": {
        "function_score": {
          "script_score": {
            "script": "_score * doc['view_count'].value"
          }
        }
      }
    }
  }
}
```
