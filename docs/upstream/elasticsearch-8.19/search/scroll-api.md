<!-- Converted from search/scroll-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Scroll API

**Important:** We no longer recommend using the scroll API for deep pagination. If
you need to preserve the index state while paging through more than 10,000 hits,
use the `search_after` parameter with a point in time (PIT).

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Retrieves the next batch of results for a <<scroll-search-results,scrolling
search>>.

```console
GET /_search/scroll
{
  "scroll_id" : "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAD4WYm9laVYtZndUQlNsdDcwakFMNjU1QQ=="
}
```

#### Request

`GET /_search/scroll/<scroll_id>`
deprecated:[7.0.0]

`GET /_search/scroll`

`POST /_search/scroll/<scroll_id>`
deprecated:[7.0.0]

`POST /_search/scroll`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias.

#### Description

You can use the scroll API to retrieve large sets of results from a single
scrolling search request.

The scroll API requires a scroll ID. To get a scroll ID, submit a
search API request that includes an argument for the
`scroll` query parameter. The `scroll`
parameter indicates how long Elasticsearch should retain the
search context for the request.

The search response returns a scroll ID in the `_scroll_id` response body
parameter. You can then use the scroll ID with the scroll API to retrieve the
next batch of results for the request. If the Elasticsearch security features are enabled,
the access to the results of a specific scroll ID is restricted to
the user or API key that submitted the search.

You can also use the scroll API to specify a new `scroll` parameter that extends
or shortens the retention period for the search context.

See scroll-search-results.

**Important:** Results from a scrolling search reflect the state of the index at the
time of the initial search request. Subsequent indexing or document changes only
affect later search and scroll requests.

#### Path parameters

`<scroll_id>`::
deprecated:[7.0.0]
(Optional, string)
Scroll ID of the search.
**Important:** Scroll IDs can be long. We recommend only specifying scroll IDs using
the `scroll_id` request body parameter.

#### Query parameters

`scroll`::
(Optional, time value)
Period to retain the search context for scrolling. See
scroll-search-results.
This value overrides the duration set by the original search API request's
`scroll` parameter.
By default, this value cannot exceed `1d` (24 hours). You can change
this limit using the `search.max_keep_alive` cluster-level setting.
**Important:** You can also specify this value using the `scroll` request body
parameter. If both parameters are specified, only the query parameter is used.

`scroll_id`::
deprecated:[7.0.0]
(Optional, string)
Scroll ID for the search.
**Important:** Scroll IDs can be long. We recommend only specifying scroll IDs using
the `scroll_id` request body parameter.

`rest_total_hits_as_int`::
(Optional, Boolean)
If `true`, the API response's `hit.total` property is returned as an integer.
If `false`, the API response's `hit.total` property is returned as an object.
Defaults to `false`.

#### Request body

`scroll`::
(Optional, time value)
Period to retain the search context for scrolling. See
scroll-search-results.
This value overrides the duration set by the original search API request's
`scroll` parameter.
By default, this value cannot exceed `1d` (24 hours). You can change
this limit using the `search.max_keep_alive` cluster-level setting.
**Important:** You can also specify this value using the `scroll` query
parameter. If both parameters are specified, only the query parameter is used.

`scroll_id`::
(Required, string)
Scroll ID for the search.

#### Response body

The scroll API returns the same response body as the search API. See the search
API's response body parameters.
