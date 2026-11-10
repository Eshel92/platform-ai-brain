<!-- Converted from searchable-snapshots/apis/clear-cache.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear cache API

**New API reference**
For the most up-to-date API details, refer to [Searchable snapshots APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-searchable_snapshots).

experimental::[]

Clears indices and data streams from the shared cache for
partially mounted indices.

#### Request

`POST /_searchable_snapshots/cache/clear`

`POST /<target>/_searchable_snapshots/cache/clear`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API. You must also
have the `manage` index privileges for the target
data stream, index, or alias.

#### Path parameters

`<target>`::
(Optional, string)
Comma-separated list of data streams, indices, and aliases to clear from the
cache. Supports wildcards (`*`). To clear the entire cache, omit this parameter.

#### Examples

Clears the cache of the index `my-index`:

```console
POST /my-index/_searchable_snapshots/cache/clear
```
