<!-- Converted from fleet/fleet-multi-search.asciidoc (AsciiDoc). Includes are inlined. -->

### Fleet multi search API

**New API reference**
For the most up-to-date API details, refer to [Fleet APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-fleet).

Executes several fleet searches with a single API request.

The API follows the same structure as the multi search API. However,
similar to the fleet search API, it supports the `wait_for_checkpoints` parameter.

**Note:** The fleet multi search API is designed for indirect use through fleet server. Direct use is
not supported. Elastic reserves the right to change or remove this feature in future releases
without prior notice.

#### Request

`GET /_fleet/_fleet_msearch`

`GET /<index>/_fleet/_fleet_msearch`

#### Path parameters

`<target>`::
(Optional, string)
A single target to search. If the target is an index alias, it must resolve to a single index.

#### Query parameters

`wait_for_checkpoints`::
(Optional, list) A comma separated list of checkpoints. When configured, the search API will
only be executed on a shard after the relevant checkpoint has become visible for search.
Defaults to an empty list which will cause Elasticsearch to immediately execute the search.

`allow_partial_search_results`::
(Optional, Boolean)
If `true`, returns partial results if there are shard request timeouts or
shard failures. If `false`, returns an error with
no partial results. Defaults to the configured cluster setting `search.default_allow_partial_results` which
is `true` by default.
