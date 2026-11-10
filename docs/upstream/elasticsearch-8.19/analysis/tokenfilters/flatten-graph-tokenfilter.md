<!-- Converted from analysis/tokenfilters/flatten-graph-tokenfilter.asciidoc (AsciiDoc). Includes are inlined. -->

### Flatten graph token filter

Flattens a token graph produced by a graph token filter, such
as `synonym_graph` or
`word_delimiter_graph`.

Flattening a token graph containing
multi-position tokens makes the graph
suitable for indexing. Otherwise, indexing does
not support token graphs containing multi-position tokens.

**Warning:**
Flattening graphs is a lossy process.

If possible, avoid using the `flatten_graph` filter. Instead, use graph token
filters in search analyzers only. This eliminates
the need for the `flatten_graph` filter.

The `flatten_graph` filter uses Lucene's
{lucene-analysis-docs}/core/FlattenGraphFilter.html[FlattenGraphFilter].

#### Example

To see how the `flatten_graph` filter works, you first need to produce a token
graph containing multi-position tokens.

The following analyze API request uses the `synonym_graph`
filter to add `internet phonebook` as a multi-position synonym for `domain name system` in the
text `domain name system is fragile`:

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "synonym_graph",
      "synonyms": [ "internet phonebook, domain name system" ]
    }
  ],
  "text": "domain name system is fragile"
}
```

The filter produces the following token graph with `internet phonebook` as a multi-position
token.

(Figure: images/analysis/token-graph-dns-synonym-ex2.svg)

Indexing does not support token graphs containing multi-position tokens. To make
this token graph suitable for indexing, it needs to be flattened.

To flatten the token graph, add the `flatten_graph` filter after the
`synonym_graph` filter in the previous analyze API request.

```console
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "synonym_graph",
      "synonyms": [ "internet phonebook, domain name system" ]
    },
    "flatten_graph"
  ],
  "text": "domain name system is fragile"
}
```

The filter produces the following flattened token graph, which is suitable for
indexing.

(Figure: images/analysis/token-graph-dns-synonym-flattened-ex2.svg)

#### Add to an analyzer

The following create index API request uses the
`flatten_graph` token filter to configure a new
custom analyzer.

In this analyzer, a custom `word_delimiter_graph` filter produces token graphs
containing catenated, multi-position tokens. The `flatten_graph` filter flattens
these token graphs, making them suitable for indexing.

```console
PUT /my-index-000001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_index_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "my_custom_word_delimiter_graph_filter",
            "flatten_graph"
          ]
        }
      },
      "filter": {
        "my_custom_word_delimiter_graph_filter": {
          "type": "word_delimiter_graph",
          "catenate_all": true
        }
      }
    }
  }
}
```
