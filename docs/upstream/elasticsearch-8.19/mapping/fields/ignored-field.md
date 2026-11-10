<!-- Converted from mapping/fields/ignored-field.asciidoc (AsciiDoc). Includes are inlined. -->

### `_ignored` field

The `_ignored` field indexes and stores the names of every field in a document
that has been ignored when the document was indexed. This can, for example,
be the case when the field was malformed and `ignore_malformed`
was turned on, when a `keyword` field's value exceeds its optional
`ignore_above` setting, or when
`index.mapping.total_fields.limit` has been reached and
`index.mapping.total_fields.ignore_dynamic_beyond_limit`
is set to `true`.

This field is searchable with `term`,
`terms` and `exists`
queries, and is returned as part of the search hits.

For instance the below query matches all documents that have one or more fields
that got ignored:

```console
GET _search
{
  "query": {
    "exists": {
      "field": "_ignored"
    }
  }
}
```

Similarly, the below query finds all documents whose `@timestamp` field was
ignored at index time:

```console
GET _search
{
  "query": {
    "term": {
      "_ignored": "@timestamp"
    }
  }
}
```

Since 8.15.0, the `_ignored` field supports aggregations as well.
For example, the below query finds all fields that got ignored:

```console
GET _search
{
  "aggs": {
    "ignored_fields": {
      "terms": {
         "field": "_ignored"
      }
    }
  }
}
```
