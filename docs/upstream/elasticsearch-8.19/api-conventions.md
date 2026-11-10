<!-- Converted from api-conventions.asciidoc (AsciiDoc). Includes are inlined. -->

## API conventions

The Elasticsearch REST APIs are exposed over HTTP.
Except where noted, the following conventions apply across all APIs.

### Content-type requirements

The type of the content sent in a request body must be specified using
the `Content-Type` header. The value of this header must map to one of
the supported formats that the API supports. Most APIs support JSON,
YAML, CBOR, and SMILE. The bulk and multi-search APIs support NDJSON,
JSON, and SMILE; other types will result in an error response.

When using the `source` query string parameter, the content type must be
specified using the `source_content_type` query string parameter.

Elasticsearch only supports UTF-8-encoded JSON. Elasticsearch ignores any other encoding headings
sent with a request. Responses are also UTF-8 encoded.

### `X-Opaque-Id` HTTP header

You can pass an `X-Opaque-Id` HTTP header to track the origin of a request in
Elasticsearch logs and tasks. If provided, Elasticsearch surfaces the `X-Opaque-Id` value in the:

* Response of any request that includes the header
* Task management API response
* Slow logs
* Deprecation logs

For the deprecation logs, Elasticsearch also uses the `X-Opaque-Id` value to throttle
and deduplicate deprecation warnings. See _deprecation_logs_throttling.

The `X-Opaque-Id` header accepts any arbitrary value. However, we recommend you
limit these values to a finite set, such as an ID per client. Don't generate a
unique `X-Opaque-Id` header for every request. Too many unique `X-Opaque-Id`
values can prevent Elasticsearch from deduplicating warnings in the deprecation logs.

### `traceparent` HTTP header

Elasticsearch also supports a `traceparent` HTTP header using the
https://www.w3.org/TR/trace-context/#traceparent-header[official W3C trace
context spec]. You can use the `traceparent` header to trace requests across
Elastic products and other services. Because it's only used for traces, you can
safely generate a unique `traceparent` header for each request.

If provided, Elasticsearch surfaces the header's `trace-id` value as `trace.id` in the:

* JSON Elasticsearch server logs
* Slow logs
* Deprecation logs

For example, the following `traceparent` value would produce the following
`trace.id` value in the above logs.

```txt
`traceparent`: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01
`trace.id`: 0af7651916cd43dd8448eb211c80319c
```

### GET and POST requests

A number of Elasticsearch GET APIs--most notably the search API--support a request body.
While the GET action makes sense in the context of retrieving information,
GET requests with a body are not supported by all HTTP libraries.
All Elasticsearch GET APIs that require a body can also be submitted as POST requests.
Alternatively, you can pass the request body as the
`source` query string parameter
when using GET.

(See `rest-api/cron-expressions.md`)

### Date math support in index and index alias names

Date math name resolution lets you to search a range of time series indices or
index aliases rather than searching all of your indices and filtering the
results. Limiting the number of searched indices reduces cluster load and
improves search performance. For example, if you are searching for errors in
your daily logs, you can use a date math name template to restrict the search to
the past two days.

Most APIs that accept an index or index alias argument support date math. A date
math name takes the following form:

```txt
<static_name{date_math_expr{date_format|time_zone}}>
```

Where:

`static_name`:: Static text
`date_math_expr`:: Dynamic date math expression that computes the date dynamically
`date_format`:: Optional format in which the computed date should be rendered. Defaults to `yyyy.MM.dd`. Format should be compatible with java-time https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html
`time_zone`:: Optional time zone. Defaults to `UTC`.

**Note:** Pay attention to the usage of small vs capital letters used in the `date_format`. For example:
`mm` denotes minute of hour, while `MM` denotes month of year. Similarly `hh` denotes the hour in the
`1-12` range in combination with `AM/PM`, while `HH` denotes the hour in the `0-23` 24-hour range.

Date math expressions are resolved locale-independent. Consequently, it is not possible to use any other
calendars than the Gregorian calendar.

You must enclose date math names in angle brackets. If you use the name in a
request path, special characters must be URI encoded. For example:

```console
# PUT /<my-index-{now/d}>
PUT /%3Cmy-index-%7Bnow%2Fd%7D%3E
```

**Percent encoding of date math characters**
======================================================
The special characters used for date rounding must be URI encoded as follows:

`<`:: `%3C`
`>`:: `%3E`
`/`:: `%2F`
`{`:: `%7B`
`}`:: `%7D`
`|`:: `%7C`
`+`:: `%2B`
`:`:: `%3A`
`,`:: `%2C`
======================================================

The following example shows different forms of date math names and the final names
they resolve to given the current time is 22nd March 2024 noon UTC.

|======
| Expression                                |Resolves to
| `<logstash-{now/d}>`                      | `logstash-2024.03.22`
| `<logstash-{now/M}>`                      | `logstash-2024.03.01`
| `<logstash-{now/M{yyyy.MM}}>`             | `logstash-2024.03`
| `<logstash-{now/M-1M{yyyy.MM}}>`          | `logstash-2024.02`
| `<logstash-{now/d{yyyy.MM.dd\|+12:00}}>`  | `logstash-2024.03.23`
|======

To use the characters `{` and `}` in the static part of a name template, escape them
with a backslash `\`, for example:

 * `<elastic\\{ON\\}-{now/M}>` resolves to `elastic{ON}-2024.03.01`

The following example shows a search request that searches the Logstash indices for the past
three days, assuming the indices use the default Logstash index name format,
`logstash-YYYY.MM.dd`.

```console
# GET /<logstash-{now/d-2d}>,<logstash-{now/d-1d}>,<logstash-{now/d}>/_search
GET /%3Clogstash-%7Bnow%2Fd-2d%7D%3E%2C%3Clogstash-%7Bnow%2Fd-1d%7D%3E%2C%3Clogstash-%7Bnow%2Fd%7D%3E/_search
{
  "query" : {
    "match": {
      "test": "data"
    }
  }
}
```

### Multi-target syntax

Most APIs that accept a `<data-stream>`, `<index>`, or `<target>` request path
parameter also support _multi-target syntax_.

In multi-target syntax, you can use a comma-separated list to run a request on
multiple resources, such as data streams, indices, or aliases:
`test1,test2,test3`. You can also use [glob-like](https://en.wikipedia.org/wiki/Glob_(programming))
wildcard (`*`) expressions to target resources that match a pattern: `test*` or
`*test` or `te*t` or `*test*`.

You can exclude targets using the `-` character: `test*,-test3`.

**Important:** Aliases are resolved after wildcard expressions. This can result in a
request that targets an excluded alias. For example, if `test3` is an index
alias, the pattern `test*,-test3` still targets the indices for `test3`. To
avoid this, exclude the concrete indices for the alias instead.

You can also exclude clusters from a list of clusters to search using the `-` character:
`remote*:*,-remote1:*,-remote4:*` will search all clusters with an alias that starts
with "remote" except for "remote1" and "remote4". Note that to exclude a cluster
with this notation you must exclude all of its indexes. Excluding a subset of indexes
on a remote cluster is currently not supported. For example, this will throw an exception:
`remote*:*,-remote1:logs*`.

Multi-target APIs that can target indices support the following query
string parameters:

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
The defaults settings for the above parameters depend on the API being used.

Some multi-target APIs that can target indices also support the following query
string parameter:

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `true`.
deprecated:[7.16.0]
**Note:** APIs with a single target, such as the get document API, do
not support multi-target syntax.

#### Hidden data streams and indices

For most APIs, wildcard expressions do not match hidden data streams and indices
by default. To match hidden data streams and indices using a wildcard
expression, you must specify the `expand_wildcards` query parameter.

Alternatively, querying an index pattern starting with a dot, such as
`.watcher_hist*`, will match hidden indices by default. This is intended to
mirror Unix file-globbing behavior and provide a smoother transition path to
hidden indices.

You can create hidden data streams by setting `data_stream.hidden` to `true` in
the stream's matching index template. You can hide
indices using the `index.hidden` index setting.

The backing indices for data streams are hidden automatically. Some features,
such as machine learning, store information in hidden indices.

Global index templates that match all indices are not applied to hidden indices.

#### System indices

Elasticsearch modules and plugins can store configuration and state information in internal _system indices_.
You should not directly access or modify system indices
as they contain data essential to the operation of the system.

**Important:** Direct access to system indices is deprecated and
will no longer be allowed in a future major version.

To view system indices within cluster:

```console
GET _cluster/state/metadata?filter_path=metadata.indices.*.system
```

**Warning:** When overwriting current cluster state, system indices should be restored
as part of their [feature state](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshot-restore.html#feature-state).

#### Node specification

Some cluster-level APIs may operate on a subset of the nodes which can be specified with node filters. For example, task management, node stats, and node info APIs can all report results from a filtered set of nodes rather than from all nodes. Learn more.

#### Component selectors

A data stream component is a logical grouping of indices that help organize data inside a data stream. All data streams contain a `data` component by default. The `data` component comprises the data stream's backing indices. When searching, managing, or indexing into a data stream, the data component is what you are interacting with by default.

Some data stream features are exposed as additional components alongside its `data` component. These other components are comprised of separate sets of backing indices. These additional components store supplemental data independent of the data stream's regular backing indices. An example of another component is the `failures` component exposed by the data stream failure store feature, which captures documents that fail to be ingested in a separate set of backing indices on the data stream.

Some APIs that accept a `<data-stream>`, `<index>`, or `<target>` request path parameter also support selector syntax which defines which component on a data stream the API should operate on. To use a selector, it is appended to the index or data stream name. Selectors can be combined with other index pattern syntax like date math and wildcards.

There are two selector suffixes supported by Elasticsearch APIs:

`::data`::
  Refers to a data stream's backing indices containing regular data. Data streams always contain a data component.
`::failures`::
  This component refers to the internal indices used for a data stream's failure store.

As an example, search, field capabilities, and index stats APIs can all report results from a different component rather than from the default data.

```console
# Search a data stream normally
GET my-data-stream/_search

# Search a data stream's failure data if present
GET my-data-stream::failures/_search

# Syntax can be combined with other index pattern syntax (wildcards, multi-target, date math, cross cluster search, etc)
GET logs-*::failures/_search
GET logs-*::data,logs-*::failures/_count
GET remote-cluster:logs-*-*::failures/_search
GET *::data,*::failures,-logs-rdbms-*::failures/_stats
GET <logs-{now/d}>::failures/_search
```

### Parameters

Rest parameters (when using HTTP, map to HTTP URL parameters) follow the
convention of using underscore casing.

### Request body in query string

For libraries that don't accept a request body for non-POST requests,
you can pass the request body as the `source` query string parameter
instead. When using this method, the `source_content_type` parameter
should also be passed with a media type value that indicates the format
of the source, such as `application/json`.

### REST API version compatibility

Major version upgrades often include a number of breaking changes
that impact how you interact with Elasticsearch.
While we recommend that you monitor the deprecation logs and
update applications before upgrading Elasticsearch,
having to coordinate the necessary changes can be an impediment to upgrading.

You can enable an existing application to function without modification after
an upgrade by including API compatibility headers, which tell Elasticsearch you are still
using the previous version of the REST API. Using these headers allows the
structure of requests and responses to remain the same; it does not guarantee
the same behavior.

You set version compatibility on a per-request basis in the `Content-Type` and `Accept` headers.
Setting `compatible-with` to the same major version as
the version you're running has no impact,
but ensures that the request will still work after Elasticsearch is upgraded.

To tell Elasticsearch 8.0 you are using the 7.x request and response format,
set `compatible-with=7`:

```sh
Content-Type: application/vnd.elasticsearch+json; compatible-with=7
Accept: application/vnd.elasticsearch+json; compatible-with=7
```

### HTTP `429 Too Many Requests` status code push back

Elasticsearch APIs may respond with the HTTP `429 Too Many Requests` status code, indicating that the cluster is too busy
to handle the request. When this happens, consider retrying after a short delay. If the retry also receives
a `429 Too Many Requests` response, extend the delay by backing off exponentially before each subsequent retry.

### URL-based access control

Many users use a proxy with URL-based access control to secure access to
Elasticsearch data streams and indices. For multi-search,
multi-get, and bulk requests, the user has
the choice of specifying a data stream or  index in the URL and on each individual request
within the request body. This can make URL-based access control challenging.

To prevent the user from overriding the data stream or index specified in the
URL, set `rest.action.multi.allow_explicit_index` to `false` in `elasticsearch.yml`.

This causes  Elasticsearch to
reject requests that explicitly specify a data stream or index in the request body.

### Boolean Values

All REST API parameters (both request parameters and JSON body) support
providing boolean "false" as the value `false` and boolean "true" as the
value `true`. All other values will raise an error.

### Number Values

When passing a numeric parameter in a request body, you may use a `string`
containing the number instead of the native numeric type. For example:

```console
POST /_search
{
  "size": "1000"
}
```

Integer-valued fields in a response body are described as `integer` (or
occasionally `long`) in this manual, but there are generally no explicit bounds
on such values. JSON, SMILE, CBOR and YAML all permit arbitrarily large integer
values. Do not assume that `integer` fields in a response body will always fit
into a 32-bit signed integer.

### Byte size units

Whenever the byte size of data needs to be specified, e.g. when setting a buffer size
parameter, the value must specify the unit, like `10kb` for 10 kilobytes. Note that
these units use powers of 1024, so `1kb` means 1024 bytes. The supported units are:

`b`::   Bytes
`kb`::  Kilobytes
`mb`::  Megabytes
`gb`::  Gigabytes
`tb`::  Terabytes
`pb`::  Petabytes

### Distance Units

Wherever distances need to be specified, such as the `distance` parameter in
the query-dsl-geo-distance-query), the default unit is meters if none is specified.
Distances can be specified in other units, such as `"1km"` or
`"2mi"` (2 miles).

The full list of units is listed below:

Mile::          `mi` or `miles`
Yard::          `yd` or `yards`
Feet::          `ft` or `feet`
Inch::          `in` or `inch`
Kilometer::     `km` or `kilometers`
Meter::         `m` or `meters`
Centimeter::    `cm` or `centimeters`
Millimeter::    `mm` or `millimeters`
Nautical mile:: `NM`, `nmi`, or `nauticalmiles`

### Time units

Whenever durations need to be specified, e.g. for a `timeout` parameter, the duration must specify
the unit, like `2d` for 2 days. The supported units are:

`d`::       Days
`h`::       Hours
`m`::       Minutes
`s`::       Seconds
`ms`::      Milliseconds
`micros`::  Microseconds
`nanos`::   Nanoseconds

### Unit-less quantities

Unit-less quantities means that they don't have a "unit" like "bytes" or "Hertz" or "meter" or "long tonne".

If one of these quantities is large we'll print it out like 10m for 10,000,000 or 7k for 7,000. We'll still print 87
when we mean 87 though. These are the supported multipliers:

`k`::  Kilo
`m`::  Mega
`g`::  Giga
`t`::  Tera
`p`::  Peta
