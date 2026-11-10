<!-- Converted from sql/apis/get-async-sql-search-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get async SQL search API

**New API reference**
For the most up-to-date API details, refer to [SQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-sql).

Returns results for an async SQL search or a
stored synchronous SQL search.

```console
GET _sql/async/FmdMX2pIang3UWhLRU5QS0lqdlppYncaMUpYQ05oSkpTc3kwZ21EdC1tbFJXQToxOTI=?format=json
```

#### Request

`GET _sql/async/<search_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, only the user who first submitted
the SQL search can retrieve the search using this API.

##### Limitations

See sql-limitations.

#### Path parameters

`<search_id>`::
(Required, string) Identifier for the search.

#### Query parameters

`delimiter`::
(Optional, string) Separator for CSV results. Defaults to `,`. The API only
supports this parameter for CSV responses.

`format`::
(Required, string) Format for the response. You must specify a format using this
parameter or the `Accept` HTTP header. If you specify both, the API uses this
parameter. For valid values, see sql-rest-format.

`keep_alive`::
(Optional, time value) Retention period for the search and its
results. Defaults to the `keep_alive` period for the original SQL search.

`wait_for_completion_timeout`::
(Optional, time value) Period to wait for complete results.
Defaults to no timeout, meaning the request waits for complete search results.

#### Response body

The get async SQL search API returns the same response body as the
SQL search API.
