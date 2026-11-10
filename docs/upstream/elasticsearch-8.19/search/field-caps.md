<!-- Converted from search/field-caps.asciidoc (AsciiDoc). Includes are inlined. -->

### Field capabilities API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Allows you to retrieve the capabilities of fields among multiple indices.
For data streams, the API returns field capabilities among the stream's backing
indices.

```console
GET /_field_caps?fields=rating
```

#### Request

`GET /_field_caps?fields=<fields>`

`POST /_field_caps?fields=<fields>`

`GET /<target>/_field_caps?fields=<fields>`

`POST /<target>/_field_caps?fields=<fields>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata`, `read`, or `manage` <<privileges-list-indices,index
privilege>> for the target data stream, index, or alias.

#### Description

The field capabilities API returns the information about the capabilities of
fields among multiple indices.

The field capabilities API returns runtime fields like any
other field. For example, a runtime field with a type of
`keyword` is returned as any other field that belongs to the `keyword` family.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`fields`::
(Required, string)
Comma-separated list of fields to retrieve capabilities for. Wildcard (`*`)
expressions are supported.

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`include_unmapped`::
  (Optional, Boolean) If `true`, unmapped fields that are mapped in one index but not in another are included in the response. Fields that don't have any mapping are never included.
  Defaults to `false`.

`include_empty_fields`::
  (Optional, Boolean) If `false`, fields that never had a value in any shards are not included in the response. Fields that are not empty are always included. This flag does not consider deletions and updates.  If a field was non-empty and all the documents containing that field were deleted or the field was removed by updates,  it will still be returned even if the flag is `false`.
  Defaults to `true`.

`filters`::
(Optional, string) Comma-separated list of filters to apply to the response.
**Valid values for `filters`**
`+metadata`::
Only include metadata fields
`-metadata`::
Exclude metadata fields
`-parent`::
Exclude parent fields
`-nested`::
Exclude nested fields
`-multifield`::
Exclude multifields

`types`::
(Optional, string) Comma-separated list of field types to include. Any fields that
do not match one of these types will be excluded from the results.  Defaults to empty,
meaning that all field types are returned.  See here for
more information about field types in field capabilities requests and responses.

#### Request body

`index_filter`::
(Optional,  query object Allows to filter indices if the provided
query rewrites to `match_none` on every shard.

`runtime_mappings`::
(Optional, object)
Defines ad-hoc runtime fields in the request similar
to the way it is done in search requests. These fields
exist only as part of the query and take precedence over fields defined with the
same name in the index mappings.

#### Response body

The types used in the response describe _families_ of field types.
Normally a type family is the same as the field type declared in the mapping,
but to simplify matters certain field types that behave identically are
described using a type family. For example, `keyword`, `constant_keyword` and `wildcard`
field types are all described as the `keyword` type family.

`metadata_field`::
  Whether this field is registered as a metadata field.

`searchable`::
  Whether this field is indexed for search on all indices.

`aggregatable`::
  Whether this field can be aggregated on all indices.

`time_series_dimension`::
  Whether this field is used as a time series dimension on all indices.
  For non-time-series indices this field is not present.

`time_series_metric`::
  Contains the metric type if the field is used as a time series metric on all indices, absent if the field is
  not used as a metric. For non-time-series indices this field is not included.

`indices`::
  The list of indices where this field has the same type family, or null if all indices
  have the same type family for the field.

`non_searchable_indices`::
  The list of indices where this field is not searchable, or null if all indices
  have the same definition for the field.

`non_aggregatable_indices`::
  The list of indices where this field is not aggregatable, or null if all
  indices have the same definition for the field.

`non_dimension_indices`::
  experimental:[]
  If this list is present in the response, some indices have the field marked as a dimension and other indices, the
  ones in this list, do not.

`metric_conflicts_indices`::
  experimental:[]
  The list of indices where this field is present, if these indices don't have the same `time_series_metric` value for
  this field.

`meta`::
  Merged metadata across all indices as a map of string keys to arrays of values.
  A value length of 1 indicates that all indices had the same value for this key,
  while a length of 2 or more indicates that not all indices had the same value
  for this key.

#### Examples

The request can be restricted to specific data streams and indices:

```console
GET my-index-000001/_field_caps?fields=rating
```

The next example API call requests information about the `rating` and the
`title` fields:

```console
GET _field_caps?fields=rating,title
```

The API returns the following response:

```console-result
{
  "indices": [ "index1", "index2", "index3", "index4", "index5" ],
  "fields": {
    "rating": {                                   <1>
      "long": {
        "metadata_field": false,
        "searchable": true,
        "aggregatable": false,
        "indices": [ "index1", "index2" ],
        "non_aggregatable_indices": [ "index1" ]  <2>
      },
      "keyword": {
        "metadata_field": false,
        "searchable": false,
        "aggregatable": true,
        "indices": [ "index3", "index4" ],
        "non_searchable_indices": [ "index4" ]    <3>
      }
    },
    "title": {                                    <4>
      "text": {
        "metadata_field": false,
        "searchable": true,
        "aggregatable": false
      }
    }
  }
}
```

<1> The field `rating` is defined as a long in `index1` and `index2`
and as a `keyword` in `index3` and `index4`.
<2> The field `rating` is not aggregatable in `index1`.
<3> The field `rating` is not searchable in `index4`.
<4> The field `title` is defined as `text` in all indices.

By default unmapped fields are ignored. You can include them in the response by
adding a parameter called `include_unmapped` in the request:

```console
GET _field_caps?fields=rating,title&include_unmapped
```

In which case the response will contain an entry for each field that is present
in some indices but not all:

```console-result
{
  "indices": [ "index1", "index2", "index3" ],
  "fields": {
    "rating": {
      "long": {
        "metadata_field": false,
        "searchable": true,
        "aggregatable": false,
        "indices": [ "index1", "index2" ],
        "non_aggregatable_indices": [ "index1" ]
      },
      "keyword": {
        "metadata_field": false,
        "searchable": false,
        "aggregatable": true,
        "indices": [ "index3", "index4" ],
        "non_searchable_indices": [ "index4" ]
      },
      "unmapped": {                               <1>
        "metadata_field": false,
        "indices": [ "index5" ],
        "searchable": false,
        "aggregatable": false
      }
    },
    "title": {
      "text": {
        "metadata_field": false,
        "indices": [ "index1", "index2", "index3", "index4" ],
        "searchable": true,
        "aggregatable": false
      },
      "unmapped": {                               <2>
        "metadata_field": false,
        "indices": [ "index5" ],
        "searchable": false,
        "aggregatable": false
      }
    }
  }
}
```

<1> The `rating` field is unmapped` in `index5`.
<2> The `title` field is unmapped` in `index5`.

It is also possible to filter indices with a query:

```console
POST my-index-*/_field_caps?fields=rating
{
  "index_filter": {
    "range": {
      "@timestamp": {
        "gte": "2018"
      }
    }
  }
}
```

In which case indices that rewrite the provided filter to `match_none` on every shard
will be filtered from the response.

**Important:**
The filtering is done on a best-effort basis, it uses index statistics and mappings
to rewrite queries to `match_none` instead of fully executing the request.
For instance a `range` query over a `date` field can rewrite to `match_none`
if all documents within a shard (including deleted documents) are outside
of the provided range.
However, not all queries can rewrite to `match_none` so this API may return
an index even if the provided filter matches no document.
