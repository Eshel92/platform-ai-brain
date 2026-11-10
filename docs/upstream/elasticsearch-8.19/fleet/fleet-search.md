<!-- Converted from fleet/fleet-search.asciidoc (AsciiDoc). Includes are inlined. -->

### Fleet search API

**New API reference**
For the most up-to-date API details, refer to [Fleet APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-fleet).

The purpose of the fleet search api is to provide a search api where the search
will only be executed after provided checkpoint has been processed and is visible
for searches inside of Elasticsearch.

**Note:** The fleet search API is designed for indirect use through fleet server. Direct use is
not supported. Elastic reserves the right to change or remove this feature in future releases
without prior notice.

## Wait for checkpoint functionality

The fleet search API supports the optional parameter `wait_for_checkpoints`. This parameter
is a list of sequence number checkpoints. When this parameter is present, the search will
only be executed on local shards after the all operations up to and including the provided
sequence number checkpoint are visible for search. Indexed operations become visible after a
refresh. The checkpoints are indexed by shard.

If a timeout occurs before the checkpoint has been refreshed into Elasticsearch,
the search request will timeout.

The fleet search API only supports searches against a single target. If an index alias
is supplied as the search target, it must resolve to a single concrete index.

## Allow partial results

By default, the Elasticsearch search api will allow partial search results.
With this fleet API, it is common to configure this to be `false` or to check in the response
to ensure each shard search was successful. If these precautions are not taken, it is
possible for search results to be successfully returned even if one or more shards
timed out.

#### Request

`GET /<target>/_fleet/_fleet_search`

#### Path parameters

`<target>`::
(Required, string)
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
