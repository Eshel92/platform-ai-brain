<!-- Part 2 of 2 of victoriametrics/victoria_metrics_common_flags.md (split because the page is big). -->

Interval for checking for changes in Linode. This works only if linode_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#linode_sd_configs for details (default 1m0s)
  -promscrape.marathonSDCheckInterval duration
     Interval for checking for changes in Marathon REST API. This works only if marathon_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#marathon_sd_configs for details (default 30s)
  -promscrape.maxDroppedTargets int
     The maximum number of droppedTargets to show at /api/v1/targets page. Increase this value if your setup drops more scrape targets during relabeling and you need investigating labels for all the dropped targets. Note that the increased number of tracked dropped targets may result in increased memory usage (default 10000)
  -promscrape.maxParseErrorsPerScrape int
     The maximum number of parse errors to log per each scrape of a target. The number of suppressed parse errors is logged after the scrape. Zero or negative value disables the limit. See also -promscrape.suppressScrapeErrors (default 20)
  -promscrape.maxResponseHeadersSize size
     The maximum size of http response headers from Prometheus scrape targets
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 4096)
  -promscrape.maxScrapeSize size
     The maximum size of uncompressed scrape response in bytes to process from Prometheus targets. Bigger uncompressed responses are rejected. See also max_scrape_size option at https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 16777216)
  -promscrape.minResponseSizeForStreamParse size
     The minimum target response size for automatic switching to stream parsing mode, which can reduce memory usage. See https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 1000000)
  -promscrape.noStaleMarkers
     Whether to disable sending Prometheus stale markers for metrics when scrape target disappears. This option may reduce memory usage if stale markers aren't needed for your setup. This option also disables populating the scrape_series_added metric. See https://prometheus.io/docs/concepts/jobs_instances/#automatically-generated-labels-and-time-series
  -promscrape.nomad.waitTime duration
     Wait time used by Nomad service discovery. Default value is used if not set
  -promscrape.nomadSDCheckInterval duration
     Interval for checking for changes in Nomad. This works only if nomad_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#nomad_sd_configs for details (default 30s)
  -promscrape.openstackSDCheckInterval duration
     Interval for checking for changes in openstack API server. This works only if openstack_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#openstack_sd_configs for details (default 30s)
  -promscrape.ovhcloudSDCheckInterval duration
     Interval for checking for changes in OVH Cloud API. This works only if ovhcloud_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#ovhcloud_sd_configs for details (default 30s)
  -promscrape.puppetdbSDCheckInterval duration
     Interval for checking for changes in PuppetDB API. This works only if puppetdb_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#puppetdb_sd_configs for details (default 30s)
  -promscrape.seriesLimitPerTarget int
     Optional limit on the number of unique time series a single scrape target can expose. See https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter for more info
  -promscrape.streamParse
     Whether to enable stream parsing for metrics obtained from scrape targets. This may be useful for reducing memory usage when millions of metrics are exposed per each scrape target. It is possible to set 'stream_parse: true' individually per each 'scrape_config' section in '-promscrape.config' for fine-grained control
  -promscrape.suppressDuplicateScrapeTargetErrors
     Whether to suppress 'duplicate scrape target' errors; see https://docs.victoriametrics.com/victoriametrics/vmagent/#troubleshooting for details
  -promscrape.suppressScrapeErrors
     Whether to suppress scrape errors logging. The last error for each target is always available at '/targets' page even if scrape errors logging is suppressed. See also -promscrape.suppressScrapeErrorsDelay
  -promscrape.suppressScrapeErrorsDelay duration
     The delay for suppressing repeated scrape errors logging per each scrape targets. This may be used for reducing the number of log lines related to scrape errors. See also -promscrape.suppressScrapeErrors
  -promscrape.vultrSDCheckInterval duration
     Interval for checking for changes in Vultr. This works only if vultr_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#vultr_sd_configs for details (default 30s)
  -promscrape.yandexcloudSDCheckInterval duration
     Interval for checking for changes in Yandex Cloud API. This works only if yandexcloud_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#yandexcloud_sd_configs for details (default 30s)
  -pushmetrics.disableCompression
     Whether to disable request body compression when pushing metrics to every -pushmetrics.url
  -pushmetrics.extraLabel array
     Optional labels to add to metrics pushed to every -pushmetrics.url . For example, -pushmetrics.extraLabel='instance="foo"' adds instance="foo" label to all the metrics pushed to every -pushmetrics.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -pushmetrics.header array
     Optional HTTP request header to send to every -pushmetrics.url . For example, -pushmetrics.header='Authorization: Basic foobar' adds 'Authorization: Basic foobar' header to every request to every -pushmetrics.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -pushmetrics.interval duration
     Interval for pushing metrics to every -pushmetrics.url (default 10s)
  -pushmetrics.url array
     Optional URL to push metrics exposed at /metrics page. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#push-metrics . By default, metrics exposed at /metrics page aren't pushed to any remote storage
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -relabelConfig string
     Optional path to a file with relabeling rules, which are applied to all the ingested metrics. The path can point either to local file or to http url. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#relabeling for details. The config is reloaded on SIGHUP signal
  -reloadAuthKey value
     Auth key for /-/reload http endpoint. It must be passed via authKey query arg. It overrides httpAuth.* settings.
     Flag value can be read from the given file when using -reloadAuthKey=file:///abs/path/to/file or -reloadAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -reloadAuthKey=http://host/path or -reloadAuthKey=https://host/path
  -retentionPeriod value
     Data with timestamps outside the retentionPeriod is automatically deleted. The minimum retentionPeriod is 24h or 1d. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention. See also -retentionFilter
     The following optional suffixes are supported: s (second), h (hour), d (day), w (week), M (month), y (year). If suffix isn't set, then the duration is counted in months (default 1M)
  -retentionTimezoneOffset duration
     The offset for performing indexdb rotation. If set to 0, then the indexdb rotation is performed at 4am UTC time per each -retentionPeriod. If set to 2h, then the indexdb rotation is performed at 4am EET time (the timezone with +2h offset)
  -rpc.disableCompression
     Whether to disable compression of the data sent from vmstorage to vmselect. This reduces CPU usage at the cost of higher network bandwidth usage
  -rpc.handshakeTimeout duration
     Timeout for RPC handshake between vminsert/vmselect and vmstorage. Increase this value if transient handshake failures occur. See https://docs.victoriametrics.com/victoriametrics/troubleshooting/#cluster-instability section for more details. (default 5s)
  -search.cacheTimestampOffset duration
     The maximum duration since the current time for response data, which is always queried from the original raw data, without using the response cache. Increase this value if you see gaps in responses due to time synchronization issues between VictoriaMetrics and data sources. See also -search.disableAutoCacheReset (default 5m0s)
  -search.disableAutoCacheReset
     Whether to disable automatic response cache reset if a sample with timestamp outside -search.cacheTimestampOffset is inserted into VictoriaMetrics
  -search.disableCache
     Whether to disable response caching. This may be useful when ingesting historical data. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#backfilling . See also -search.resetRollupResultCacheOnStartup
  -search.disableImplicitConversion
     Whether to return an error for queries that rely on implicit subquery conversions, see https://docs.victoriametrics.com/victoriametrics/metricsql/#subqueries for details. See also -search.logImplicitConversion.
  -search.graphiteMaxPointsPerSeries int
     The maximum number of points per series Graphite render API can return (default 1000000)
  -search.graphiteStorageStep duration
     The interval between datapoints stored in the database. It is used at Graphite Render API handler for normalizing the interval between datapoints in case it isn't normalized. It can be overridden by sending 'storage_step' query arg to /render API or by sending the desired interval via 'Storage-Step' http header during querying /render API (default 10s)
  -search.ignoreExtraFiltersAtLabelsAPI
     Whether to ignore match[], extra_filters[] and extra_label query args at /api/v1/labels and /api/v1/label/.../values . This may be useful for decreasing load on VictoriaMetrics when extra filters match too many time series. The downside is that superfluous labels or series could be returned, which do not match the extra filters. See also -search.maxLabelsAPISeries and -search.maxLabelsAPIDuration
  -search.inmemoryBufSizeBytes size
     Size for in-memory data blocks used during processing search requests. By default, the size is automatically calculated based on available memory. Adjust this flag value if you observe that vm_tmp_blocks_max_inmemory_file_size_bytes metric constantly shows much higher values than vm_tmp_blocks_inmemory_file_size_bytes. See https://github.com/VictoriaMetrics/VictoriaMetrics/pull/6851
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -search.latencyOffset duration
     The time when data points become visible in query results after the collection. It can be overridden on per-query basis via latency_offset arg. Too small value can result in incomplete last points for query results (default 30s)
  -search.logImplicitConversion
     Whether to log queries with implicit subquery conversions, see https://docs.victoriametrics.com/victoriametrics/metricsql/#subqueries for details. Such conversion can be disabled using -search.disableImplicitConversion.
  -search.logQueryMemoryUsage size
     Log query and increment vm_memory_intensive_queries_total metric each time the query requires more memory than specified by this flag. This may help detecting and optimizing heavy queries. Query logging is disabled by default. See also -search.logSlowQueryDuration and -search.maxMemoryPerQuery
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -search.logSlowQueryDuration duration
     Log queries with execution time exceeding this value. Zero disables slow query logging. See also -search.logQueryMemoryUsage (default 5s)
  -search.maxBinaryOpPushdownLabelValues int
     The maximum number of values for a label in the first expression that can be extracted as a common label filter and pushed down to the second expression in a binary operation. A larger value makes the pushed-down filter more complex but fewer time series will be returned. This flag is useful when selective label (e.g., 'instance') contains numerous values, and storage resources are abundant. (default 100)
  -search.maxConcurrentRequests int
     The maximum number of concurrent search requests. It shouldn't be high, since a single request can saturate all the CPU cores, while many concurrently executed requests may require high amounts of memory. See also -search.maxQueueDuration and -search.maxMemoryPerQuery (default 2x CPU cores, capped at 16)
  -search.maxDeleteDuration duration
     The maximum duration for /api/v1/admin/tsdb/delete_series call (default 5m0s)
  -search.maxDeleteSeries int
     The maximum number of time series, which can be deleted using /api/v1/admin/tsdb/delete_series. This option allows limiting memory usage (default 1000000)
  -search.maxExportDuration duration
     The maximum duration for /api/v1/export call (default 720h0m0s)
  -search.maxExportSeries int
     The maximum number of time series, which can be returned from /api/v1/export* APIs. This option allows limiting memory usage (default 10000000)
  -search.maxFederateSeries int
     The maximum number of time series, which can be returned from /federate. This option allows limiting memory usage (default 1000000)
  -search.maxGraphitePathExpressionLen int
     The maximum length of pathExpression field in Graphite series. Longer expressions are truncated to prevent memory exhaustion on complex nested queries. Set to 0 to disable truncation. (default 1024)
  -search.maxGraphiteSeries int
     The maximum number of time series, which can be scanned during queries to Graphite Render API. See https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#render-api (default 300000)
  -search.maxGraphiteTagKeys int
     The maximum number of tag keys returned from Graphite API, which returns tags. See https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#tags-api (default 100000)
  -search.maxGraphiteTagValues int
     The maximum number of tag values returned from Graphite API, which returns tag values. See https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#tags-api (default 100000)
  -search.maxLabelsAPIDuration duration
     The maximum duration for /api/v1/labels, /api/v1/label/.../values and /api/v1/series requests. See also -search.maxLabelsAPISeries and -search.ignoreExtraFiltersAtLabelsAPI (default 5s)
  -search.maxLabelsAPISeries int
     The maximum number of time series, which could be scanned when searching for the matching time series at /api/v1/labels and /api/v1/label/.../values. This option allows limiting memory usage and CPU usage. See also -search.maxLabelsAPIDuration, -search.maxTagKeys, -search.maxTagValues and -search.ignoreExtraFiltersAtLabelsAPI (default 1000000)
  -search.maxLookback duration
     Synonym to -query.lookback-delta from Prometheus. The value is dynamically detected from interval between time series datapoints if not set. It can be overridden on per-query basis via max_lookback arg. See also '-search.maxStalenessInterval' flag, which has the same meaning due to historical reasons
  -search.maxMemoryPerQuery size
     The maximum amounts of memory a single query may consume. Queries requiring more memory are rejected. The total memory limit for concurrently executed queries can be estimated as -search.maxMemoryPerQuery multiplied by -search.maxConcurrentRequests . See also -search.logQueryMemoryUsage
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -search.maxPointsPerTimeseries int
     The maximum points per a single timeseries returned from /api/v1/query_range. This option doesn't limit the number of scanned raw samples in the database. The main purpose of this option is to limit the number of per-series points returned to graphing UI such as VMUI or Grafana. There is no sense in setting this limit to values bigger than the horizontal resolution of the graph. See also -search.maxResponseSeries (default 30000)
  -search.maxPointsSubqueryPerTimeseries int
     The maximum number of points per series, which can be generated by subquery. See https://valyala.medium.com/prometheus-subqueries-in-victoriametrics-9b1492b720b3 (default 100000)
  -search.maxQueryDuration duration
     The maximum duration for query execution. It can be overridden to a smaller value on a per-query basis via 'timeout' query arg (default 30s)
  -search.maxQueryLen size
     The maximum search query length in bytes
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 16384)
  -search.maxQueueDuration duration
     The maximum time the request waits for execution when -search.maxConcurrentRequests limit is reached; see also -search.maxQueryDuration (default 10s)
  -search.maxResponseSeries int
     The maximum number of time series which can be returned from /api/v1/query and /api/v1/query_range . The limit is disabled if it equals to 0. See also -search.maxPointsPerTimeseries and -search.maxUniqueTimeseries
  -search.maxSamplesPerQuery int
     The maximum number of raw samples a single query can process across all time series. This protects from heavy queries, which select unexpectedly high number of raw samples. See also -search.maxSamplesPerSeries (default 1000000000)
  -search.maxSamplesPerSeries int
     The maximum number of raw samples a single query can scan per each time series. This option allows limiting memory usage (default 30000000)
  -search.maxSeries int
     The maximum number of time series, which can be returned from /api/v1/series. This option allows limiting memory usage (default 30000)
  -search.maxSeriesPerAggrFunc int
     The maximum number of time series an aggregate MetricsQL function can generate (default 1000000)
  -search.maxStalenessInterval duration
     The maximum interval for staleness calculations. By default, it is automatically calculated from the median interval between samples. This flag could be useful for tuning Prometheus data model closer to Influx-style data model. See https://prometheus.io/docs/prometheus/latest/querying/basics/#staleness for details. See also '-search.setLookbackToStep' flag
  -search.maxStatusRequestDuration duration
     The maximum duration for /api/v1/status/* requests (default 5m0s)
  -search.maxStepForPointsAdjustment duration
     The maximum step when /api/v1/query_range handler adjusts points with timestamps closer than -search.latencyOffset to the current time. The adjustment is needed because such points may contain incomplete data (default 1m0s)
  -search.maxTSDBStatusSeries int
     The maximum number of time series, which can be processed during the call to /api/v1/status/tsdb. This option allows limiting memory usage (default 10000000)
  -search.maxTSDBStatusTopNSeries int
     The maximum value of 'topN' argument that can be passed to /api/v1/status/tsdb API. This option allows limiting memory usage. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#tsdb-stats (default 1000)
  -search.maxTagKeys int
     The maximum number of tag keys returned per search. See also -search.maxLabelsAPISeries and -search.maxLabelsAPIDuration (default 100000)
  -search.maxTagValueSuffixesPerSearch int
     The maximum number of tag value suffixes returned from /metrics/find (default 100000)
  -search.maxTagValues int
     The maximum number of tag values returned per search. See also -search.maxLabelsAPISeries and -search.maxLabelsAPIDuration (default 100000)
  -search.maxUniqueTimeseries int
     The maximum number of unique time series, which can be scanned during every query. This allows protecting against heavy queries, which select unexpectedly high number of series. When set to zero, the limit is automatically calculated based on -search.maxConcurrentRequests (inversely proportional) and memory available to the process (proportional). See also -search.max* command-line flags at vmselect
  -search.maxWorkersPerQuery int
     The maximum number of CPU cores a single query can use. The default value should work good for most cases. The flag can be set to lower values for improving performance of big number of concurrently executed queries. The flag can be set to bigger values for improving performance of heavy queries, which scan big number of time series (>10K) and/or big number of samples (>100M). There is no sense in setting this flag to values bigger than the number of CPU cores available on the system (default CPU cores, capped at 32)
  -search.minStalenessInterval duration
     The minimum interval for staleness calculations. This flag could be useful for removing gaps on graphs generated from time series with irregular intervals between samples. See also '-search.maxStalenessInterval'
  -search.minWindowForInstantRollupOptimization duration
     Enable cache-based optimization for repeated queries to /api/v1/query (aka instant queries), which contain rollup functions with lookbehind window exceeding the given value (default 3h0m0s)
  -search.noStaleMarkers
     Set this flag to true if the database doesn't contain Prometheus stale markers, so there is no need in spending additional CPU time on its handling. Staleness markers may exist only in data obtained from Prometheus scrape targets
  -search.queryStats.lastQueriesCount int
     Query stats for /api/v1/status/top_queries is tracked on this number of last queries. Zero value disables query stats tracking (default 20000)
  -search.queryStats.minQueryDuration duration
     The minimum duration for queries to track in query stats at /api/v1/status/top_queries. Queries with lower duration are ignored in query stats (default 1ms)
  -search.queryStats.minQueryMemoryUsage size
     The minimum memory bytes consumption for queries to track in query stats at /api/v1/status/top_queries. Queries with lower memory bytes consumption are ignored in query stats
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 1024)
  -search.resetCacheAuthKey value
     Optional authKey for resetting rollup cache via /internal/resetRollupResultCache call. It could be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -search.resetCacheAuthKey=file:///abs/path/to/file or -search.resetCacheAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -search.resetCacheAuthKey=http://host/path or -search.resetCacheAuthKey=https://host/path
  -search.resetRollupResultCacheOnStartup
     Whether to reset rollup result cache on startup. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#rollup-result-cache . See also -search.disableCache
  -search.setLookbackToStep
     Whether to fix lookback interval to 'step' query arg value. If set to true, the query model becomes closer to InfluxDB data model. If set to true, then -search.maxLookback and -search.maxStalenessInterval are ignored
  -search.treatDotsAsIsInRegexps
     Whether to treat dots as is in regexp label filters used in queries. For example, foo{bar=~"a.b.c"} will be automatically converted to foo{bar=~"a\\.b\\.c"}, i.e. all the dots in regexp filters will be automatically escaped in order to match only dot char instead of matching any char. Dots in ".+", ".*" and ".{n}" regexps aren't escaped. This option is DEPRECATED in favor of {__graphite__="a.*.c"} syntax for selecting metrics matching the given Graphite metrics filter
  -secret.flags array
     Comma-separated list of flag names with secret values. Values for these flags are hidden in logs and on /metrics page
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -selfScrapeInstance string
     Value for 'instance' label, which is added to self-scraped metrics (default "self")
  -selfScrapeInterval duration
     Interval for self-scraping own metrics at /metrics page
  -selfScrapeJob string
     Value for 'job' label, which is added to self-scraped metrics (default "victoria-metrics")
  -smallMergeConcurrency int
     Deprecated: this flag does nothing
  -snapshotAuthKey value
     authKey, which must be passed in query string to /snapshot* pages. It overrides -httpAuth.*
     Flag value can be read from the given file when using -snapshotAuthKey=file:///abs/path/to/file or -snapshotAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -snapshotAuthKey=http://host/path or -snapshotAuthKey=https://host/path
  -snapshotCreateTimeout duration
     Deprecated: this flag does nothing
  -snapshotsMaxAge value
     Automatically delete snapshots older than -snapshotsMaxAge if it is set to non-zero duration. Make sure that backup process has enough time to finish the backup before the corresponding snapshot is automatically deleted
     The following optional suffixes are supported: s (second), h (hour), d (day), w (week), M (month), y (year). If suffix isn't set, then the duration is counted in months (default 3d)
  -sortLabels
     Whether to sort labels for incoming samples before writing them to storage. This may be needed for reducing memory usage at storage when the order of labels in incoming samples is random. For example, if m{k1="v1",k2="v2"} may be sent as m{k2="v2",k1="v1"}. Enabled sorting for labels can slow down ingestion performance a bit
  -storage.cacheSizeIndexDBDataBlocks size
     Overrides max size for indexdb/dataBlocks cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.cacheSizeIndexDBDataBlocksSparse size
     Overrides max size for indexdb/dataBlocksSparse cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.cacheSizeIndexDBIndexBlocks size
     Overrides max size for indexdb/indexBlocks cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.cacheSizeIndexDBTagFilters size
     Overrides max size for indexdb/tagFiltersToMetricIDs cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.cacheSizeMetricNamesStats size
     Overrides max size for storage/metricNamesStatsTracker cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.cacheSizeStorageMetricName size
     Overrides max size for storage/metricName cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.cacheSizeStorageTSID size
     Overrides max size for storage/tsid cache. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cache-tuning
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.finalDedupScheduleCheckInterval duration
     The interval for checking when final deduplication process should be started.Storage unconditionally adds 25% jitter to the interval value on each check evaluation. Changing the interval to the bigger values may delay downsampling, deduplication for historical data. See also https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication (default 1h0m0s)
  -storage.idbPrefillStart duration
     Specifies how early VictoriaMetrics starts pre-filling indexDB records before indexDB rotation. Starting the pre-fill process earlier can help reduce resource usage spikes during rotation. In most cases, this value should not be changed. The maximum allowed value is 23h. (default 1h0m0s)
  -storage.maxDailySeries int
     The maximum number of unique series can be added to the storage during the last 24 hours. Excess series are logged and dropped. This can be useful for limiting series churn rate. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter . Setting this flag to '-1' sets limit to maximum possible value (2147483647) which is useful in order to enable series tracking without enforcing limits. See also -storage.maxHourlySeries
  -storage.maxHourlySeries int
     The maximum number of unique series can be added to the storage during the last hour. Excess series are logged and dropped. This can be useful for limiting series cardinality. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#cardinality-limiter . Setting this flag to '-1' sets limit to maximum possible value (2147483647) which is useful in order to enable series tracking without enforcing limits. See also -storage.maxDailySeries
  -storage.maxMetadataStorageSize size
     Overrides max size for metrics metadata entries in-memory storage. If set to 0 or a negative value, defaults to 1% of allowed memory.
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -storage.minFreeDiskSpaceBytes size
     The minimum free disk space at -storageDataPath after which the storage stops accepting new data
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 100000000)
  -storage.trackMetricNamesStats
     Whether to track ingest and query requests for timeseries metric names. This feature allows to track metric names unused at query requests. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#track-ingested-metrics-usage (default true)
  -storageDataPath string
     Path to storage data (default "victoria-metrics-data")
  -streamAggr.config string
     Optional path to file with stream aggregation config. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/ . See also -streamAggr.keepInput, -streamAggr.dropInput and -streamAggr.dedupInterval
  -streamAggr.dedupInterval duration
     Input samples are de-duplicated with this interval before optional aggregation with -streamAggr.config . See also -streamAggr.dropInputLabels and -dedup.minScrapeInterval and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#deduplication
  -streamAggr.dropInput
     Whether to drop input samples that not matching any rule in -streamAggr.config. By default, only matched raw samples are dropped, while unmatched samples are written to the remote storage.See also -streamAggr.keepInput and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/
  -streamAggr.dropInputLabels array
     An optional list of labels to drop from samples before stream de-duplication and aggregation . See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#dropping-unneeded-labels
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -streamAggr.enableWindows
     Enables aggregation within fixed windows for all aggregators. This allows to get more precise results, but impacts resource usage as it requires twice more memory to store two states. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#aggregation-windows.
  -streamAggr.ignoreFirstIntervals int
     Number of aggregation intervals to skip after the start. Increase this value if you observe incorrect aggregation results after restarts. It could be caused by receiving unordered delayed data from clients pushing data into the database. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#ignore-aggregation-intervals-on-start
  -streamAggr.ignoreOldSamples
     Whether to ignore input samples with old timestamps outside the current aggregation interval. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#ignoring-old-samples
  -streamAggr.keepInput
     Whether to keep input samples that match any rule in -streamAggr.config. By default, matched raw samples are aggregated and dropped, while unmatched samples are written to the remote storage. See also -streamAggr.dropInput and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/
  -tls array
     Whether to enable TLS for incoming HTTP requests at the given -httpListenAddr (aka https). -tlsCertFile and -tlsKeyFile must be set if -tls is set. See also -mtls
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -tlsCertFile array
     Path to file with TLS certificate for the corresponding -httpListenAddr if -tls is set. Prefer ECDSA certs instead of RSA certs as RSA certs are slower. The provided certificate file is automatically re-read every second, so it can be dynamically updated. See also -tlsAutocertHosts
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -tlsCipherSuites array
     Optional list of TLS cipher suites for incoming requests over HTTPS if -tls is set. See the list of supported cipher suites at https://pkg.go.dev/crypto/tls#pkg-constants
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -tlsKeyFile array
     Path to file with TLS key for the corresponding -httpListenAddr if -tls is set. The provided key file is automatically re-read every second, so it can be dynamically updated. See also -tlsAutocertHosts
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -tlsMinVersion array
     Optional minimum TLS version to use for the corresponding -httpListenAddr if -tls is set. Supported values: TLS10, TLS11, TLS12, TLS13
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -usePromCompatibleNaming
     Whether to replace characters unsupported by Prometheus with underscores in the ingested metric names and label names. For example, foo.bar{a.b='c'} is transformed into foo_bar{a_b='c'} during data ingestion if this flag is set. See https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels
  -version
     Show VictoriaMetrics version
  -vmalert.proxyURL string
     Optional URL for proxying requests to vmalert. For example, if -vmalert.proxyURL=http://vmalert:8880 , then alerting API requests such as /api/v1/rules from Grafana will be proxied to http://vmalert:8880/api/v1/rules . See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#vmalert
  -vmselectAddr string
     TCP address to listen for incoming connections from vmselect. When set, the node will be able to accept cluster-native vmselect RPC requests as if it were vmstorage. The tenant ID assigned to this node's data is controlled by -accountID and -projectID flags. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#multi-tenancy
  -vmui.customDashboardsPath string
     Optional path to vmui dashboards. See https://github.com/VictoriaMetrics/VictoriaMetrics/tree/master/app/vmui/packages/vmui/public/dashboards
  -vmui.defaultTimezone string
     The default timezone to be used in vmui. Timezone must be a valid IANA Time Zone. For example: America/New_York, Europe/Berlin, Etc/GMT+3 or Local
  -zabbixconnector.addDuplicateTagsSeparator string
     If set to non-empty value, enables merging of duplicate Zabbix tag values and set a separator for the values of these labels.
  -zabbixconnector.addEmptyTagsValue string
     If set to non-empty value, enables adding Zabbix tags without values to labels and set value for these labels.
  -zabbixconnector.addGroupsValue string
     If set to non-empty value, enables adding Zabbix host groups to labels and set value for these labels.
  -zabbixconnector.maxLineLen size
     The maximum length in bytes of a single line accepted by /zabbixconnector/api/v1/history
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 33554432)
```
