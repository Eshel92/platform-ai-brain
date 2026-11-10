<!-- Converted from eql/get-async-eql-status-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get async EQL status API

**New API reference**
For the most up-to-date API details, refer to [EQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-eql).

Returns the current status for an async EQL search or
a stored synchronous EQL search
without returning results. This is a more lightweight API than
get async EQL search API as it doesn't return
search results, and reports only the status.

If the Elasticsearch security features are enabled, the access to the get async
eql status API is restricted to the monitoring_user role.

```console
GET /_eql/search/status/FkpMRkJGS1gzVDRlM3g4ZzMyRGlLbkEaTXlJZHdNT09TU2VTZVBoNDM3cFZMUToxMDM=
```

#### Request

`GET /_eql/search/status/<search_id>`

#### Path parameters

`<search_id>`::
(Required, string)
Identifier for the search.
A search ID is provided in the EQL search API's response for
an async search. A search ID is also provided if the
request's `keep_on_completion` parameter
is `true`.

#### Response body

`id`::
(string)
Identifier for the search.

`is_running`::
(boolean)
If `true`, the search request is still executing.
If `false`, the search is completed.

`is_partial`::
(boolean)
If `true`, the response does not contain complete search results.
This could be because either the search is still running
(`is_running` status is `false`), or because it is already completed
(`is_running` status is `true`)  and results are partial due to
failures or timeouts.

`start_time_in_millis`::
(Long)
For a running search shows a timestamp when the eql search
started, in milliseconds since the Unix epoch.

`expiration_time_in_millis`::
(long)
Shows a timestamp when the eql search will be expired, in milliseconds
since the Unix epoch. When this time is reached, the search and its results
are deleted, even if the search is still ongoing.

`completion_status`::
(Integer)
For a completed search shows the http status code of the completed
search.

#### Examples

```console
GET /_eql/search/status/FmNJRUZ1YWZCU3dHY1BIOUhaenVSRkEaaXFlZ3h4c1RTWFNocDdnY2FSaERnUTozNDE=?keep_alive=5d
```

If the search is still running, the status response has the following form:

```console-result
{
  "id" : "FmNJRUZ1YWZCU3dHY1BIOUhaenVSRkEaaXFlZ3h4c1RTWFNocDdnY2FSaERnUTozNDE=",
  "is_running" : true,
  "is_partial" : true,
  "start_time_in_millis" : 1611690235000,
  "expiration_time_in_millis" : 1611690295000

}
```

If the search is completed the status response doesn't have
`start_time_in_millis`, but has an additional `completion_status`
field that shows the status code of the completed eql search:

```console-result
{
  "id" : "FmNJRUZ1YWZCU3dHY1BIOUhaenVSRkEaaXFlZ3h4c1RTWFNocDdnY2FSaERnUTozNDE=",
  "is_running" : false,
  "is_partial" : false,
  "expiration_time_in_millis" : 1611690295000,
  "completion_status" : 200 <1>
}
```

<1> Indicates that the eql search was successfully completed
