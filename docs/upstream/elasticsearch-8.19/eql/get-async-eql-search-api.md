<!-- Converted from eql/get-async-eql-search-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get async EQL search API

**New API reference**
For the most up-to-date API details, refer to [EQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-eql).

Returns the current status and available results for an <<eql-search-async,async
EQL search>> or a <<eql-search-store-sync-eql-search,stored synchronous EQL
search>>.

```console
GET /_eql/search/FkpMRkJGS1gzVDRlM3g4ZzMyRGlLbkEaTXlJZHdNT09TU2VTZVBoNDM3cFZMUToxMDM=
```

#### Request

`GET /_eql/search/<search_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, only the user who first submitted
the EQL search can retrieve the search using this API.

* See eql-required-fields.

##### Limitations

See EQL limitations.

#### Path parameters

`<search_id>`::
(Required, string)
Identifier for the search.
A search ID is provided in the EQL search API's response for
an async search. A search ID is also provided if the
request's `keep_on_completion` parameter
is `true`.

#### Query parameters

`keep_alive`::
(Optional, time value)
Period for which the search and its results are stored on the cluster. Defaults
to the `keep_alive` value set by the search's <<eql-search-api,EQL search
API>> request.
If specified, this parameter sets a new `keep_alive` period for the search,
starting when the get async EQL search API request executes. This new period
overwrites the one specified in the EQL search API request.
When this period expires, the search and its results are deleted, even if the
search is ongoing.

`wait_for_completion_timeout`::
(Optional, time value)
Timeout duration to wait for the request to finish. Defaults to no timeout,
meaning the request waits for complete search results.
If this parameter is specified and the request completes during this period,
complete search results are returned.
If the request does not complete during this period, the response returns an
`is_partial` value of `true` and no search results.

#### Response body

The async EQL search API returns the same response body as the EQL search API.
See the EQL search API's <<eql-search-api-response-body,response body
parameters>>.
