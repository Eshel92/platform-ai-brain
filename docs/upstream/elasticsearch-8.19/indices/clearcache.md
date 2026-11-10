<!-- Converted from indices/clearcache.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear cache API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Clears the caches of one or more indices. For data streams, the API clears the
caches of the stream's backing indices.

```console
POST /my-index-000001/_cache/clear
```

#### Request

`POST /<target>/_cache/clear`

`POST /_cache/clear`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target data stream, index,
or alias.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

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

`fielddata`::
(Optional, Boolean)
If `true`,
clears the fields cache.

Use the `fields` parameter
to clear the cache of specific fields only.

`fields`::
(Optional, string)
Comma-separated list of field names
used to limit the `fielddata` parameter.

Defaults to all fields.

**Note:** This parameter does *not* support objects
or field aliases.

`index`::
(Optional, string)
Comma-separated list of index names
used to limit the request.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`query`::
(Optional, Boolean)
If `true`,
clears the query cache.

`request`::
(Optional, Boolean)
If `true`,
clears the request cache.

#### Examples

##### Clear a specific cache

By default,
the clear cache API clears all caches.
You can clear only specific caches
by setting the following query parameters to `true`:

* `fielddata`
* `query`
* `request`

```console
POST /my-index-000001/_cache/clear?fielddata=true  <1>
POST /my-index-000001/_cache/clear?query=true      <2>
POST /my-index-000001/_cache/clear?request=true    <3>
```

<1> Clears only the fields cache
<2> Clears only the query cache
<3> Clears only the request cache

##### Clear the cache of specific fields

To only clear the cache of specific fields,
use the `fields` query parameter.

```console
POST /my-index-000001/_cache/clear?fields=foo,bar   <1>
```

<1> Clear the cache for the `foo` and `bar` field

##### Clear caches for several data streams and indices

```console
POST /my-index-000001,my-index-000002/_cache/clear
```

##### Clear caches for all data streams and indices

```console
POST /_cache/clear
```
