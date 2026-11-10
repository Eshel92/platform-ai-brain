<!-- Converted from mapping/fields/synthetic-source.asciidoc (AsciiDoc). Includes are inlined. -->

#### Synthetic `_source`

**Note:** This feature requires a [subscription](https://www.elastic.co/subscriptions).

Though very handy to have around, the source field takes up a significant amount
of space on disk. Instead of storing source documents on disk exactly as you
send them, Elasticsearch can reconstruct source content on the fly upon retrieval.
To enable this feature, use the value `synthetic` for the index setting `index.mapping.source.mode`:

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
  }
}
```

While this on-the-fly reconstruction is _generally_ slower than saving the source
documents verbatim and loading them at query time, it saves a lot of storage
space. Additional latency can be avoided by not loading `_source` field in queries when it is not needed.

##### Supported fields

Synthetic `_source` is supported by all field types. Depending on implementation details, field types have different
properties when used with synthetic `_source`.

Most field types construct synthetic `_source` using existing data, most
commonly `doc_values` and stored fields. For these field types, no additional space
is needed to store the contents of `_source` field. Due to the storage layout of `doc_values`, the
generated `_source` field undergoes modifications compared to the original document.

For all other field types, the original value of the field is stored as is, in the same way as the `_source` field in
non-synthetic mode. In this case there are no modifications and field data in `_source` is the same as in the original
document. Similarly, malformed values of fields that use `ignore_malformed` or
`ignore_above` need to be stored as is. This approach is less storage efficient since data needed for
`_source` reconstruction is stored in addition to other data required to index the field (like `doc_values`).

##### Synthetic `_source` restrictions

Some field types have additional restrictions. These restrictions are documented in the **synthetic `_source`** section
of the field type's documentation.

Synthetic source is not supported in source-only snapshot repositories. To store indexes that use synthetic `_source`, choose a different repository type.

##### Synthetic `_source` modifications

When synthetic `_source` is enabled, retrieved documents undergo some
modifications compared to the original JSON.

###### Arrays moved to leaf fields

Synthetic `_source` arrays are moved to leaves. For example:

```console
PUT idx/_doc/1
{
  "foo": [
    {
      "bar": 1
    },
    {
      "bar": 2
    }
  ]
}
```

Will become:

```console-result
{
  "foo": {
    "bar": [1, 2]
  }
}
```

This can cause some arrays to vanish:

```console
PUT idx/_doc/1
{
  "foo": [
    {
      "bar": 1
    },
    {
      "baz": 2
    }
  ]
}
```

Will become:

```console-result
{
  "foo": {
    "bar": 1,
    "baz": 2
  }
}
```

###### Fields named as they are mapped

Synthetic source names fields as they are named in the mapping. When used
with dynamic mapping, fields with dots (`.`) in their names are, by
default, interpreted as multiple objects, while dots in field names are
preserved within objects that have subobjects disabled. For example:

```console
PUT idx/_doc/1
{
  "foo.bar.baz": 1
}
```

Will become:

```console-result
{
  "foo": {
    "bar": {
      "baz": 1
    }
  }
}
```

This impacts how source contents can be referenced in scripts. For instance, referencing
a script in its original source form will return null:

```js
"script": { "source": """  emit(params._source['foo.bar.baz'])  """ }
```

Instead, source references need to be in line with the mapping structure:

```js
"script": { "source": """  emit(params._source['foo']['bar']['baz'])  """ }
```

or simply

```js
"script": { "source": """  emit(params._source.foo.bar.baz)  """ }
```

The following field APIs are preferable as, in addition to being agnostic to the
mapping structure, they make use of docvalues if available and fall back to synthetic source only when needed. This
reduces source synthesizing, a slow and costly operation.

```js
"script": { "source": """  emit(field('foo.bar.baz').get(null))   """ }
"script": { "source": """  emit($('foo.bar.baz', null))   """ }
```

###### Alphabetical sorting

Synthetic `_source` fields are sorted alphabetically. The
[JSON RFC](https://www.rfc-editor.org/rfc/rfc7159.html) defines objects as
"an unordered collection of zero or more name/value pairs" so applications
shouldn't care but without synthetic `_source` the original ordering is
preserved and some applications may, counter to the spec, do something with
that ordering.

###### Representation of ranges

Range field values (e.g. `long_range`) are always represented as inclusive on both sides with bounds adjusted
accordingly. See examples.

###### Reduced precision of `geo_point` values

Values of `geo_point` fields are represented in synthetic `_source` with reduced precision. See
examples.

###### Minimizing source modifications

It is possible to avoid synthetic source modifications for a particular object or field, at extra storage cost.
This is controlled through param `synthetic_source_keep` with the following option:

 - `none`: synthetic source diverges from the original source as described above (default).
 - `arrays`: arrays of the corresponding field or object preserve the original element ordering and duplicate elements.
The synthetic source fragment for such arrays is not guaranteed to match the original source exactly, e.g. array
`[1, 2, [5], [[4, [3]]], 5]` may appear as-is or in an equivalent format like `[1, 2, 5, 4, 3, 5]`. The exact format
may change in the future, in an effort to reduce the storage overhead of this option.
- `all`: the source for both singleton instances and arrays of the corresponding field or object gets recorded. When
applied to objects, the source of all sub-objects and sub-fields gets captured. Furthermore, the original source of
arrays gets captured and appears in synthetic source with no modifications.

For instance:

```console
PUT idx_keep
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
      "path": {
        "type": "object",
        "synthetic_source_keep": "all"
      },
      "ids": {
        "type": "integer",
        "synthetic_source_keep": "arrays"
      }
    }
  }
}
```

```console
PUT idx_keep/_doc/1
{
  "path": {
    "to": [
      { "foo": [3, 2, 1] },
      { "foo": [30, 20, 10] }
    ],
    "bar": "baz"
  },
  "ids": [ 200, 100, 300, 100 ]
}
```

returns the original source, with no array deduplication and sorting:

```console-result
{
  "path": {
    "to": [
      { "foo": [3, 2, 1] },
      { "foo": [30, 20, 10] }
    ],
    "bar": "baz"
  },
  "ids": [ 200, 100, 300, 100 ]
}
```

The option for capturing the source of arrays can be applied at index level, by setting
`index.mapping.synthetic_source_keep` to `arrays`. This applies to all objects and fields in the index, except for
the ones with explicit overrides of `synthetic_source_keep` set to `none`. In this case, the storage overhead grows
with the number and sizes of arrays present in source of each document, naturally.

##### Field types that support synthetic source with no storage overhead

The following field types support synthetic source using data from `doc_values` or
stored fields, and require no additional storage space to construct the `_source` field.

**Note:** If you enable the `ignore_malformed` or `ignore_above` settings, then
additional storage is required to store ignored field values for these types.

** `aggregate_metric_double`
** {plugins}/mapper-annotated-text-usage.html#annotated-text-synthetic-source[`annotated-text`]
** `binary`
** `boolean`
** `byte`
** `date`
** `date_nanos`
** `dense_vector`
** `double`
** `flattened`
** `float`
** `geo_point`
** `half_float`
** `histogram`
** `integer`
** `ip`
** `keyword`
** `long`
** `range` types
** `scaled_float`
** `short`
** `text`
** `version`
** `wildcard`
