<!-- Converted from sql/apis/get-async-sql-search-status-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get async SQL search status API

**New API reference**
For the most up-to-date API details, refer to [SQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-sql).

Returns the current status of an async SQL search or a
stored synchronous SQL search.

```console
GET _sql/async/status/FmdMX2pIang3UWhLRU5QS0lqdlppYncaMUpYQ05oSkpTc3kwZ21EdC1tbFJXQToxOTI=?format=json
```

#### Request

`GET _sql/async/status/<search_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor`
cluster privilege to use this API.

##### Limitations

See sql-limitations.

#### Path parameters

`<search_id>`::
(Required, string) Identifier for the search.

#### Response body

`id`::
(string) Identifier for the search.

`is_running`::
(Boolean) If `true`, the search is still running. If `false`, the
search has finished.

`is_partial`::
(Boolean) If `true`, the response does not contain complete search results. If
`is_partial` is `true` and `is_running` is `true`, the search is still running.
If `is_partial` is `true` but `is_running` is `false`, the results are partial
due to a failure or timeout.

`start_time_in_millis`::
(integer) Timestamp, in milliseconds since the Unix epoch, when the search
started. The API only returns this property for running searches.

`expiration_time_in_millis`::
(integer) Timestamp, in milliseconds since the Unix epoch, when Elasticsearch will delete
the search and its results, even if the search is still running.

`completion_status`::
(integer) HTTP status code for the search. The API only returns this property
for completed searches.
