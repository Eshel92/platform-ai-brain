<!-- Converted from data-streams/tsds-index-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Time series index settings

Backing indices in a time series data stream (TSDS) support the
following index settings.

`index.mode`::
(Static, string) Mode for the index.
Valid values are `time_series` and `null` (no mode).
Defaults to `null`.

`index.time_series.start_time`::
(Static, string) Earliest `@timestamp`
value (inclusive) accepted by the index. Only indices with an `index.mode` of
`time_series` support this setting. For more information,
refer to time-bound-indices.

`index.time_series.end_time`::
(Dynamic, string) Latest `@timestamp`
value (exclusive) accepted by the index. Only indices with an `index.mode` of
`time_series` support this setting. For more information, refer to
time-bound-indices.

`index.look_ahead_time`::
(Static, time units)
Interval used to calculate the `index.time_series.end_time` for a TSDS's write
index. Defaults to `30m` (30 minutes). Accepts `1m` (one minute) to `2h` (two
hours). Only indices with an `index.mode` of `time_series` support this setting.
For more information, refer to tsds-look-ahead-time. Additionally this setting
can not be less than `time_series.poll_interval` cluster setting.

**Note:** Increasing the `look_ahead_time` will also increase the amount of time Index lifecycle management
waits before being able to proceed with executing the actions that expect the
index to not receive any writes anymore. For more information, refer to time-bound-indices.

`index.look_back_time`::
(Static, time units)
Interval used to calculate the `index.time_series.start_time` for a TSDS's first
backing index when a tsdb data stream is created. Defaults to `2h` (2 hours).
Accepts `1m` (one minute) to `7d` (seven days). Only indices with an `index.mode`
of `time_series` support this setting. For more information,
refer to tsds-look-back-time.

[[index-routing-path]] `index.routing_path`::
(Static, string or array of strings) Plain `keyword`
fields used to route documents in a TSDS to index shards. Supports wildcards
(`*`). Only indices with an `index.mode` of `time_series` support this setting.
Defaults to an empty list, except for data streams then defaults to the list
of dimension fields with a `time_series_dimension`
value of `true` defined in your component and index templates. For more
information, refer to dimension-based-routing.

`index.mapping.dimension_fields.limit`::
(Dynamic, integer)
Maximum number of time series dimensions for the
index. Defaults to `32768`.
