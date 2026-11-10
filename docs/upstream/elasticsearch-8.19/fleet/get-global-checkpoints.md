<!-- Converted from fleet/get-global-checkpoints.asciidoc (AsciiDoc). Includes are inlined. -->

### Get global checkpoints API

The purpose of the get global checkpoints api is to return the current global
checkpoints for an index. This API allows users to know the what sequence numbers
have been safely persisted in Elasticsearch.

## Polling on global checkpoint advance

The API has an optional polling mode enabled by the `wait_for_advance` query
parameter. In polling mode, the API will only return after the global checkpoints
advance past the provided `checkpoints`. By default, `checkpoints` is an empty
array, which will lead to the API returning immediately.

If a timeout occurs before the global checkpoints advance past the provided
`checkpoints`, Elasticsearch will return the current global checkpoints and a
boolean indicating that the request timed out.

Currently the `wait_for_advance` parameter is only supported for one shard indices.

## Polling on index ready

By default in polling mode, an exception will be returned if the index does not
exist or all the primary shards are not active. In polling mode, the
`wait_for_index` parameter can be used to modify this behavior. If `wait_for_index`
is set to true, the API will wait for the index to be created and all primary
shards to be active.

If a timeout occurs before these conditions are met, the relevant exception will be
returned.

Currently the `wait_for_index` parameter is only supported when `wait_for_advance`
is true.

#### Request

`GET /<index>/_fleet/global_checkpoints`

#### Path parameters

`<index>`::
(Required, string)
A single index or index alias that resolves to a single index.

#### Query parameters

`wait_for_advance`::
(Optional, Boolean) A boolean value which controls whether to wait (until the
`timeout`) for the global checkpoints to advance past the provided
`checkpoints`. Defaults to `false`.

`wait_for_index`::
(Optional, Boolean) A boolean value which controls whether to wait (until the
`timeout`) for the target index to exist and all primary shards be active. Can
only be `true` when `wait_for_advance` is `true`. Defaults to `false`.

`checkpoints`::
(Optional, list) A comma separated list of previous global checkpoints.
When used in combination with `wait_for_advance`, the API will only return once
the global checkpoints advances past the `checkpoints`. Defaults to an empty list
which will cause Elasticsearch to immediately return the current global
checkpoints.

`timeout`::
(Optional, time units)
Period to wait for a global checkpoints to advance past `checkpoints`.
Defaults to `30s`.

#### Response body

`global_checkpoints`::
(array of integers) The global checkpoints for the index.

`timed_out`::
(Boolean) If `false` the global checkpoints did not advance past the
`checkpoints` within the specified `timeout`.
