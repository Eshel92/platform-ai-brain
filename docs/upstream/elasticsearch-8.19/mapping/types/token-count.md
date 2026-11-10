<!-- Converted from mapping/types/token-count.asciidoc (AsciiDoc). Includes are inlined. -->

### Token count field type

A field of type `token_count` is really an `integer` field which
accepts string values, analyzes them, then indexes the number of tokens in the
string.

For instance:

```console
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "name": { <1>
        "type": "text",
        "fields": {
          "length": { <2>
            "type":     "token_count",
            "analyzer": "standard"
          }
        }
      }
    }
  }
}

PUT my-index-000001/_doc/1
{ "name": "John Smith" }

PUT my-index-000001/_doc/2
{ "name": "Rachel Alice Williams" }

GET my-index-000001/_search
{
  "query": {
    "term": {
      "name.length": 3 <3>
    }
  }
}
```

<1> The `name` field is a `text` field which uses the default
`standard` analyzer.
<2> The `name.length` field is a `token_count` multi-field which will index the number of tokens in the `name` field.
<3> This query matches only the document containing `Rachel Alice Williams`, as it contains three tokens.

#### Parameters for `token_count` fields

The following parameters are accepted by `token_count` fields:

`analyzer`::

    The analyzer which should be used to analyze the string
    value. Required. For best performance, use an analyzer without token
    filters.

`enable_position_increments`::

Indicates if position increments should be counted.
Set to `false` if you don't want to count tokens removed by analyzer filters (like `stop`).
Defaults to `true`.

`doc_values`::

    Should the field be stored on disk in a column-stride fashion, so that it
    can later be used for sorting, aggregations, or scripting? Accepts `true`
    (default) or `false`.

`index`::

    Should the field be searchable? Accepts `true` (default) and `false`.

`null_value`::

    Accepts a numeric value of the same `type` as the field which is
    substituted for any explicit `null` values. Defaults to `null`, which
    means the field is treated as missing.

`store`::

    Whether the field value should be stored and retrievable separately from
    the `_source` field. Accepts `true` or `false`
    (default).

##### Synthetic `_source`

`token_count` fields support synthetic `_source` in their
default configuration.
