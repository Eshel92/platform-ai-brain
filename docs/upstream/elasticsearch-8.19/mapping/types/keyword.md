<!-- Converted from mapping/types/keyword.asciidoc (AsciiDoc). Includes are inlined. -->

### Keyword type family

The keyword family includes the following field types:

* `keyword`, which is used for structured content such as IDs, email
addresses, hostnames, status codes, zip codes, or tags.
* `constant_keyword` for keyword fields that always contain
the same value.
* `wildcard` for unstructured machine-generated content.
The `wildcard` type is optimized for fields with large values or high
cardinality.

Keyword fields are often used in sorting,
aggregations, and <<term-level-queries,term-level
queries>>, such as `term`.

**Tip:** Avoid using keyword fields for full-text search. Use the `text`
field type instead.

### Keyword field type

Below is an example of a mapping for a basic `keyword` field:

```console
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "tags": {
        "type":  "keyword"
      }
    }
  }
}
```

**Mapping numeric identifiers**

**Tip:**
Not all numeric data should be mapped as a numeric field data type.
Elasticsearch optimizes numeric fields, such as `integer` or `long`, for
`range` queries. However, `keyword` fields
are better for `term` and other
term-level queries.

Identifiers, such as an ISBN or a product ID, are rarely used in `range`
queries. However, they are often retrieved using term-level queries.

Consider mapping a numeric identifier as a `keyword` if:

* You don't plan to search for the identifier data using
  `range` queries.
* Fast retrieval is important. `term` query searches on `keyword` fields are
  often faster than `term` searches on numeric fields.

If you're unsure which to use, you can use a multi-field to map
the data as both a `keyword` _and_ a numeric data type.

#### Parameters for basic keyword fields

The following parameters are accepted by `keyword` fields:

`doc_values`::

    Should the field be stored on disk in a column-stride fashion, so that it
    can later be used for sorting, aggregations, or scripting? Accepts `true`
    (default) or `false`.

`eager_global_ordinals`::

    Should global ordinals be loaded eagerly on refresh? Accepts `true` or `false`
    (default). Enabling this is a good idea on fields that are frequently used for
    terms aggregations.

`fields`::

    Multi-fields allow the same string value to be indexed in multiple ways for
    different purposes, such as one field for search and a multi-field for
    sorting and aggregations.

`ignore_above`::

    Do not index any string longer than this value. Defaults to `2147483647`
    in standard indices so that all values would be accepted, and `8191` in logsdb
    indices to protect against Lucene's term byte-length limit of `32766`. Please
    however note that default dynamic mapping rules create a sub `keyword` field
    that overrides this default by setting `ignore_above: 256`.

`index`::

    Should the field be quickly searchable? Accepts `true` (default) and
     `false`. `keyword` fields that only have `doc_values`
     enabled can still be queried, albeit slower.

`index_options`::

    What information should be stored in the index, for scoring purposes.
    Defaults to `docs` but can also be set to `freqs` to take term frequency into account
    when computing scores.

`meta`::

    Metadata about the field.

`norms`::

    Whether field-length should be taken into account when scoring queries.
    Accepts `true` or `false` (default).

`null_value`::

    Accepts a string value which is substituted for any explicit `null`
    values. Defaults to `null`, which means the field is treated as missing.
    Note that this cannot be set if the `script` value is used.

`on_script_error`::

    Defines what to do if the script defined by the `script` parameter
    throws an error at indexing time. Accepts `fail` (default), which
    will cause the entire document to be rejected, and `continue`, which
    will register the field in the document's
    `_ignored` metadata field and continue
    indexing. This parameter can only be set if the `script` field is
    also set.

`script`::

    If this parameter is set, then the field will index values generated
    by this script, rather than reading the values directly from the
    source. If a value is set for this field on the input document, then
    the document will be rejected with an error.
    Scripts are in the same format as their
    runtime equivalent. Values emitted by the
    script are normalized as usual, and will be ignored if they are longer
    that the value set on `ignore_above`.

`store`::

    Whether the field value should be stored and retrievable separately from
    the `_source` field. Accepts `true` or `false`
    (default).

`similarity`::

    Which scoring algorithm or _similarity_ should be used. Defaults
    to `BM25`.

`normalizer`::

    How to pre-process the keyword prior to indexing. Defaults to `null`,
    meaning the keyword is kept as-is.

`split_queries_on_whitespace`::

    Whether full text queries should split the input on whitespace
    when building a query for this field.
    Accepts `true` or `false` (default).

`time_series_dimension`::
    (Optional, Boolean)
Marks the field as a time series dimension. Defaults
to `false`.

The
`index.mapping.dimension_fields.limit`
index setting limits the number of dimensions in an index.

Dimension fields have the following constraints:

* The `doc_values` and `index` mapping parameters must be `true`.
* Dimension values are used to identify a document’s time series. If dimension values are altered in any way during indexing, the document will be stored as belonging to different from intended time series. As a result there are additional constraints:
** The field cannot use a `normalizer`.

#### Synthetic `_source`

Synthetic source may sort `keyword` fields and remove duplicates.
For example:
```console
PUT idx
{
  "settings": {
    "index": {
      "mapping": {
        "source": {
          "mode": "synthetic"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "kwd": { "type": "keyword" }
    }
  }
}
PUT idx/_doc/1
{
  "kwd": ["foo", "foo", "bar", "baz"]
}
```

Will become:

```console-result
{
  "kwd": ["bar", "baz", "foo"]
}
```

If a `keyword` field sets `store` to `true` then order and duplicates
are preserved. For example:
```console
PUT idx
{
  "settings": {
    "index": {
      "mapping": {
        "source": {
          "mode": "synthetic"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "kwd": { "type": "keyword", "store": true }
    }
  }
}
PUT idx/_doc/1
{
  "kwd": ["foo", "foo", "bar", "baz"]
}
```

Will become:

```console-result
{
  "kwd": ["foo", "foo", "bar", "baz"]
}
```

Values longer than `ignore_above` are preserved but sorted to the end.
For example:
```console
PUT idx
{
  "settings": {
    "index": {
      "mapping": {
        "source": {
          "mode": "synthetic"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "kwd": { "type": "keyword", "ignore_above": 3 }
    }
  }
}
PUT idx/_doc/1
{
  "kwd": ["foo", "foo", "bang", "bar", "baz"]
}
```

Will become:

```console-result
{
  "kwd": ["bar", "baz", "foo", "bang"]
}
```

If `null_value` is configured, `null` values are replaced with the `null_value` in synthetic source.
For example:
```console
PUT idx
{
  "settings": {
    "index": {
      "mapping": {
        "source": {
          "mode": "synthetic"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "kwd": { "type": "keyword", "null_value": "NA" }
    }
  }
}
PUT idx/_doc/1
{
  "kwd": ["foo", null, "bar"]
}
```

Will become:

```console-result
{
  "kwd": ["NA", "bar", "foo"]
}
```

(See `mapping/types/constant-keyword.md`)
(See `mapping/types/wildcard.md`)
