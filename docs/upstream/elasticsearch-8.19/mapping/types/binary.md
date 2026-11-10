<!-- Converted from mapping/types/binary.asciidoc (AsciiDoc). Includes are inlined. -->

### Binary field type

The `binary` type accepts a binary value as a
[Base64](https://en.wikipedia.org/wiki/Base64) encoded string. The field is not
stored by default and is not searchable:

```console
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      },
      "blob": {
        "type": "binary"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "name": "Some binary blob",
  "blob": "U29tZSBiaW5hcnkgYmxvYg==" <1>
}
```

<1> The Base64 encoded binary value must not have embedded newlines `\n`.

#### Parameters for `binary` fields

The following parameters are accepted by `binary` fields:

`doc_values`::

    Should the field be stored on disk in a column-stride fashion, so that it
    can later be used for sorting, aggregations, or scripting? Accepts `true`
    or `false` (default). This parameter will be automatically set to `true` for TSDB indices
(indices that have `index.mode` set to `time_series`).

`store`::

    Whether the field value should be stored and retrievable separately from
    the `_source` field. Accepts `true` or `false`
    (default).

#### Synthetic `_source`

Synthetic source may sort `binary` values in order of their byte representation. For example:
```console
PUT idx
{
  "mappings": {
    "_source": { "mode": "synthetic" },
    "properties": {
      "binary": { "type": "binary", "doc_values": true }
    }
  }
}
PUT idx/_doc/1
{
  "binary": ["IAA=", "EAA="]
}
```

Will become:
```console-result
{
  "binary": ["EAA=", "IAA="]
}
```
