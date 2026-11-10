<!-- Converted from mapping/types/match-only-text.asciidoc (AsciiDoc). Includes are inlined. -->

### Match-only text field type

A variant of `text` that trades scoring and efficiency of
positional queries for space efficiency. This field effectively stores data the
same way as a `text` field that only indexes documents (`index_options: docs`)
and disables norms (`norms: false`). Term queries perform as fast if not faster
as on `text` fields, however queries that need positions such as the
`match_phrase` query perform slower as they
need to look at the `_source` document to verify whether a phrase matches. All
queries return constant scores that are equal to 1.0.

Analysis is not configurable: text is always analyzed with the
default analyzer
(`standard` by default).

span queries are not supported with this field, use
interval queries instead, or the
`text` field type if you absolutely need span queries.

Other than that, `match_only_text` supports the same queries as `text`. And
like `text`, it does not support sorting and has only limited support for aggregations.

```console
PUT logs
{
  "mappings": {
    "properties": {
      "@timestamp": {
        "type": "date"
      },
      "message": {
        "type": "match_only_text"
      }
    }
  }
}
```

#### Parameters for match-only text fields

The following mapping parameters are accepted:

`fields`::

    Multi-fields allow the same string value to be indexed in multiple ways for
    different purposes, such as one field for search and a multi-field for
    sorting and aggregations, or the same string value analyzed by different
    analyzers.

`meta`::

    Metadata about the field.
