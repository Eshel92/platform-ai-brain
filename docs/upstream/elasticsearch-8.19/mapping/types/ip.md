<!-- Converted from mapping/types/ip.asciidoc (AsciiDoc). Includes are inlined. -->

### IP field type

An `ip` field can index/store either [IPv4](https://en.wikipedia.org/wiki/IPv4) or
[IPv6](https://en.wikipedia.org/wiki/IPv6) addresses.

```console
PUT my-index-000001
{
  "mappings": {
    "properties": {
      "ip_addr": {
        "type": "ip"
      }
    }
  }
}

PUT my-index-000001/_doc/1
{
  "ip_addr": "192.168.1.1"
}

GET my-index-000001/_search
{
  "query": {
    "term": {
      "ip_addr": "192.168.0.0/16"
    }
  }
}
```

**Note:** You can also store ip ranges in a single field using an ip_range data type.

#### Parameters for `ip` fields

The following parameters are accepted by `ip` fields:

`doc_values`::

    Should the field be stored on disk in a column-stride fashion, so that it
    can later be used for sorting, aggregations, or scripting? Accepts `true`
    (default) or `false`.

`ignore_malformed`::

    If `true`, malformed IP addresses are ignored. If `false` (default), malformed
    IP addresses throw an exception and reject the whole document. Note that this
    cannot be set if the `script` parameter is used.

`index`::

    Should the field be quickly searchable? Accepts `true` (default) and
    `false`. Fields that only have `doc_values`
    enabled can still be queried using term or range-based queries,
    albeit slower.

`null_value`::

    Accepts an IPv4 or IPv6 value which is substituted for any explicit `null` values.
    Defaults to `null`, which means the field is treated as missing. Note that
    this cannot be set if the `script` parameter is used.

`on_script_error`::

    Defines what to do if the script defined by the `script` parameter
    throws an error at indexing time. Accepts `reject` (default), which
    will cause the entire document to be rejected, and `ignore`, which
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
    runtime equivalent, and should emit strings
    containing IPv4 or IPv6 formatted addresses.

`store`::

    Whether the field value should be stored and retrievable separately from
    the `_source` field. Accepts `true` or `false`
    (default).

`time_series_dimension`::
    (Optional, Boolean)
Marks the field as a time series dimension. Defaults
to `false`.

The
`index.mapping.dimension_fields.limit`
index setting limits the number of dimensions in an index.

Dimension fields have the following constraints:

* The `doc_values` and `index` mapping parameters must be `true`.

#### Querying `ip` fields

The most common way to query ip addresses is to use the
[CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation)
notation: `[ip_address]/[prefix_length]`. For instance:

```console
GET my-index-000001/_search
{
  "query": {
    "term": {
      "ip_addr": "192.168.0.0/16"
    }
  }
}
```

or

```console
GET my-index-000001/_search
{
  "query": {
    "term": {
      "ip_addr": "2001:db8::/48"
    }
  }
}
```

Also beware that colons are special characters to the
`query_string` query, so ipv6 addresses will
need to be escaped. The easiest way to do so is to put quotes around the
searched value:

```console
GET my-index-000001/_search
{
  "query": {
    "query_string" : {
      "query": "ip_addr:\"2001:db8::/48\""
    }
  }
}
```

#### Synthetic `_source`

Synthetic source may sort `ip` field values and remove duplicates. For example:
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
      "ip": { "type": "ip" }
    }
  }
}
PUT idx/_doc/1
{
  "ip": ["192.168.0.1", "192.168.0.1", "10.10.12.123",
         "2001:db8::1:0:0:1", "::afff:4567:890a"]
}
```

Will become:

```console-result
{
  "ip": ["::afff:4567:890a", "10.10.12.123", "192.168.0.1", "2001:db8::1:0:0:1"]
}
```

**Note:** IPv4 addresses are sorted as though they were IPv6 addresses prefixed by
      `::ffff:0:0:0/96` as specified by
      [rfc6144](https://datatracker.ietf.org/doc/html/rfc6144).
