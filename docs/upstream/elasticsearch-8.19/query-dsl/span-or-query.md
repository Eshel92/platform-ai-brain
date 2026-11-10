<!-- Converted from query-dsl/span-or-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Span or query

Matches the union of its span clauses. Here is an example:

```console
GET /_search
{
  "query": {
    "span_or" : {
      "clauses" : [
        { "span_term" : { "field" : "value1" } },
        { "span_term" : { "field" : "value2" } },
        { "span_term" : { "field" : "value3" } }
      ]
    }
  }
}
```

The `clauses` element is a list of one or more other span type queries.
