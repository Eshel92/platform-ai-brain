<!-- Converted from search/clear-scroll-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear scroll API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Clears the search context and results for a
scrolling search.

```console
DELETE /_search/scroll
{
  "scroll_id" : "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAD4WYm9laVYtZndUQlNsdDcwakFMNjU1QQ=="
}
```

#### Request

`DELETE /_search/scroll/<scroll_id>`
deprecated:[7.0.0]

`DELETE /_search/scroll`

#### Path parameters

`<scroll_id>`::
deprecated:[7.0.0]
(Optional, string)
Comma-separated list of scroll IDs to clear. To clear all scroll IDs, use `_all`.
**Important:** Scroll IDs can be long. We recommend only specifying
scroll IDs using the <<clear-scroll-api-scroll-id-param,`scroll_id` request body
parameter>>.

#### Query parameters

`scroll_id`::
deprecated:[7.0.0]
(Optional, string)
Comma-separated list of scroll IDs to clear. To clear all scroll IDs, use `_all`.
**Important:** Scroll IDs can be long. We recommend only specifying
scroll IDs using the <<clear-scroll-api-scroll-id-param,`scroll_id` request body
parameter>>.

#### Request body

`scroll_id`::
(Required, string or array of strings)
Scroll IDs to clear. To clear all scroll IDs, use `_all`.

#### Response body

`succeeded`::
(Boolean)
If `true`, the request succeeded. This does not indicate whether any scrolling
search requests were cleared.

`num_freed`::
(integer)
Number of scrolling search requests cleared.
