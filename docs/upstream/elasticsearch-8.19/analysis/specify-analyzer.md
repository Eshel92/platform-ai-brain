<!-- Converted from analysis/specify-analyzer.asciidoc (AsciiDoc). Includes are inlined. -->

### Specify an analyzer

Elasticsearch offers a variety of ways to specify built-in or custom analyzers:

* By `text` field, index, or query
* For index or search time

**Keep it simple**

**Tip:**
The flexibility to specify analyzers at different levels and for different times
is great... _but only when it's needed_.

In most cases, a simple approach works best: Specify an analyzer for each
`text` field, as outlined in specify-index-field-analyzer.

This approach works well with Elasticsearch's default behavior, letting you use the same
analyzer for indexing and search. It also lets you quickly see which analyzer
applies to which field using the get mapping API.

If you don't typically create mappings for your indices, you can use
index templates to achieve a similar effect.

#### How Elasticsearch determines the index analyzer

Elasticsearch determines which index analyzer to use by checking the following parameters
in order:

. The `analyzer` mapping parameter for the field.
  See specify-index-field-analyzer.
. The `analysis.analyzer.default` index setting.
  See specify-index-time-default-analyzer.

If none of these parameters are specified, the
`standard` analyzer is used.

#### Specify the analyzer for a field

When mapping an index, you can use the `analyzer` mapping parameter
to specify an analyzer for each `text` field.

The following create index API request sets the
`whitespace` analyzer as the analyzer for the `title` field.

```console
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "whitespace"
      }
    }
  }
}
```

#### Specify the default analyzer for an index

In addition to a field-level analyzer, you can set a fallback analyzer for
using the `analysis.analyzer.default` setting.

The following create index API request sets the
`simple` analyzer as the fallback analyzer for `my-index-000001`.

```console
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "simple"
        }
      }
    }
  }
}
```

#### How Elasticsearch determines the search analyzer

**Warning:**
In most cases, specifying a different search analyzer is unnecessary. Doing so
could negatively impact relevancy and result in unexpected search results.

If you choose to specify a separate search analyzer, we recommend you thoroughly
test your analysis configuration before deploying in
production.

At search time, Elasticsearch determines which analyzer to use by checking the following
parameters in order:

. The `analyzer` parameter in the search query.
  See specify-search-query-analyzer.
. The `search_analyzer` mapping parameter for the field.
  See specify-search-field-analyzer.
. The `analysis.analyzer.default_search` index setting.
  See specify-search-default-analyzer.
. The `analyzer` mapping parameter for the field.
  See specify-index-field-analyzer.

If none of these parameters are specified, the
`standard` analyzer is used.

#### Specify the search analyzer for a query

When writing a full-text query, you can use the `analyzer`
parameter to specify a search analyzer. If provided, this overrides any other
search analyzers.

The following search API request sets the `stop` analyzer as
the search analyzer for a `match` query.

```console
GET my-index-000001/_search
{
  "query": {
    "match": {
      "message": {
        "query": "Quick foxes",
        "analyzer": "stop"
      }
    }
  }
}
```

#### Specify the search analyzer for a field

When mapping an index, you can use the `search_analyzer` mapping
parameter to specify a search analyzer for each `text` field.

If a search analyzer is provided, the index analyzer must also be specified
using the `analyzer` parameter.

The following create index API request sets the
`simple` analyzer as the search analyzer for the `title` field.

```console
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "whitespace",
        "search_analyzer": "simple"
      }
    }
  }
}
```

#### Specify the default search analyzer for an index

When creating an index, you can set a default search
analyzer using the `analysis.analyzer.default_search` setting.

If a search analyzer is provided, a default index analyzer must also be
specified using the `analysis.analyzer.default` setting.

The following  create index API request sets the
`whitespace` analyzer as the default search analyzer for the `my-index-000001` index.

```console
PUT my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "default": {
          "type": "simple"
        },
        "default_search": {
          "type": "whitespace"
        }
      }
    }
  }
}
```
