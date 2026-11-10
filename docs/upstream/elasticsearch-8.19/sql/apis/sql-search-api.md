<!-- Converted from sql/apis/sql-search-api.asciidoc (AsciiDoc). Includes are inlined. -->

### SQL search API

**New API reference**
For the most up-to-date API details, refer to [SQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-sql).

Returns results for an SQL search.

```console
POST _sql?format=txt
{
  "query": "SELECT * FROM library ORDER BY page_count DESC LIMIT 5"
}
```

#### Request

`GET _sql`

`POST _sql`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the data stream, index,
or alias you search.

##### Limitations

See sql-limitations.

#### Query parameters

`delimiter`::
(Optional, string) Separator for CSV results. Defaults to `,`. The API only
supports this parameter for CSV responses.

`format`::
(Optional, string) Format for the response. For valid values, see
sql-rest-format.
You can also specify a format using the `Accept` HTTP header. If you specify
both this parameter and the `Accept` HTTP header, this parameter takes
precedence.

#### Request body

`allow_partial_search_results`::
(Optional, Boolean) If `true`, returns partial results if there are shard
request timeouts or shard failures. If `false`, returns an error with no
partial results. Defaults to `false`.

`catalog`::
(Optional, string) Default catalog (cluster) for queries. If unspecified, the
queries execute on the data in the local cluster only.
experimental:[] See cross-cluster search.

`columnar`::
(Optional, Boolean) If `true`, returns results in a columnar format. Defaults to
`false`. The API only supports this parameter for CBOR, JSON, SMILE, and YAML
responses. See sql-rest-columnar.

`cursor`::
(Optional, string) Cursor used to retrieve a set of paginated
results. If you specify a `cursor`, the API only uses the `columnar` and
`time_zone` request body parameters. It ignores other request body parameters.

`fetch_size`::
(Optional, integer) Maximum number of rows to return in the response. Defaults
to `1000`.

`field_multi_value_leniency`::
(Optional, Boolean) If `false`, the API returns an error for fields containing
array values. If `true`, the API returns the first value from the
array with no guarantee of consistent results. Defaults to `false`.

`filter`::
(Optional, object) Query DSL used to filter documents for the SQL
search. See sql-rest-filtering.

`index_include_frozen`::
(Optional, Boolean) If `true`, the search can run on frozen indices. Defaults to
`false`.

`keep_alive`::
(Optional, time value) Retention period for an
async or saved synchronous search. Defaults
to `5d` (five days).

`keep_on_completion`::
(Optional, Boolean) If `true`, Elasticsearch <<sql-store-searches,stores synchronous
searches>> if you also specify the `wait_for_completion_timeout` parameter. If
`false`, Elasticsearch only stores async searches that don't finish before
the `wait_for_completion_timeout`. Defaults to `false`.

`page_timeout`::
(Optional, time value) Minimum retention period for the scroll
cursor. After this time period, a pagination request might
fail because the scroll cursor is no longer available. Subsequent scroll requests
prolong the lifetime of the scroll cursor by the duration of `page_timeout` in
the scroll request. Defaults to `45s` (45 seconds).

`params`::
(Optional, array) Values for parameters in the `query`. For syntax, see
sql-rest-params.

`query`::
(Required, object) SQL query to run. For syntax, see sql-spec.

`request_timeout`::
(Optional, time value) Timeout before the request fails. Defaults
to `90s` (90 seconds).

`runtime_mappings`::
(Optional, object of objects)
Defines one or more runtime fields in the search
request. These fields take precedence over mapped fields with the same name.
**Properties of `runtime_mappings` objects**

`<field-name>`::
(Required, object)
Configuration for the runtime field. The key is the field name.
**Properties of `<field-name>`**
=====

`type`::
(Required, string)
Field type, which can be any of the following:
* `boolean`
* `composite`
* `date`
* `double`
* `geo_point`
* `ip`
* `keyword`
* `long`
* `lookup`
`script`::
(Optional, string)
Painless script executed at query time. The
script has access to the entire context of a document, including the original
`_source` and any mapped fields plus their values.
This script must include `emit` to return calculated values. For example:
```js
      "script": "emit(doc['@timestamp'].value.dayOfWeekEnum.toString())"
```

=====
`time_zone`::
(Optional, string) ISO-8601 time zone ID for the search. Several
SQL date/time functions use this time zone. Defaults
to `Z` (UTC).

`wait_for_completion_timeout`::
(Optional, time value) Period to wait for complete results.
Defaults to no timeout, meaning the request waits for complete search results.
If the search doesn’t finish within this period, the search becomes
async.
To save a synchronous search, you must specify this
parameter and the `keep_on_completion` parameter.

#### Response body

The SQL search API supports multiple response formats. Most
response formats use a tabular layout. JSON responses contain the following
properties:

`id`::
(string) Identifier for the search. This value is only returned for
async and saved synchronous searches. For
CSV, TSV, and TXT responses, this value is returned in the `Async-ID` HTTP
header.

`is_running`::
(Boolean) If `true`, the search is still running. If `false`, the search has
finished. This value is only returned for async and
saved synchronous searches. For CSV, TSV, and TXT
responses, this value is returned in the `Async-partial` HTTP header.

`is_partial`::
(Boolean) If `true`, the response does not contain complete search results. If
`is_partial` is `true` and `is_running` is `true`, the search is still running.
If `is_partial` is `true` but `is_running` is `false`, the results are partial
due to a failure or timeout.
This value is only returned for async and
saved synchronous searches. For CSV, TSV, and TXT
responses, this value is returned in the `Async-partial` HTTP header.

`rows`::
(array of arrays)
Values for the search results.

`columns`::
(array of objects)
Column headings for the search results. Each object is a column.
**Properties of `columns` objects**
`name`::
(string) Name of the column.

`type`::
(string) Data type for the column.

`cursor`::
(string) Cursor for the next set of paginated results. For
CSV, TSV, and TXT responses, this value is returned in the `Cursor` HTTP header.
