<!-- Part 1 of 2 of victoriametrics/victoria_metrics_common_flags.md (split because the page is big). -->

---
build:
  list: never
  publishResources: false
  render: never
sitemap:
  disable: true
---
<!-- The file should not be updated manually. Run make docs-update-flags while preparing a new release to sync flags in docs from actual binaries. -->
```shellhelp

victoria-metrics is a time series database and monitoring solution.

See the docs at https://docs.victoriametrics.com/victoriametrics/

  -accountID uint
     The accountID of the stored data
  -bigMergeConcurrency int
     Deprecated: this flag does nothing
  -blockcache.missesBeforeCaching int
     The number of cache misses before putting the block into cache. Higher values may reduce indexdb/dataBlocks cache size at the cost of higher CPU and disk read usage (default 2)
  -cacheExpireDuration duration
     Items are removed from in-memory caches after they aren't accessed for this duration. Lower values may reduce memory usage at the cost of higher CPU usage. See also -prevCacheRemovalPercent (default 30m0s)
  -configAuthKey value
     Authorization key for accessing /config page. It must be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -configAuthKey=file:///abs/path/to/file or -configAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -configAuthKey=http://host/path or -configAuthKey=https://host/path
  -csvTrimTimestamp duration
     Trim timestamps when importing csv data to this duration. Minimum practical duration is 1ms. Higher duration (i.e. 1s) may be used for reducing disk space usage for timestamp data (default 1ms)
  -datadog.maxInsertRequestSize size
     The maximum size in bytes of a single DataDog POST request to /datadog/api/v2/series
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 67108864)
  -datadog.sanitizeMetricName
     Sanitize metric names for the ingested DataDog data to comply with DataDog behaviour described at https://docs.datadoghq.com/metrics/custom_metrics/#naming-custom-metrics (default true)
  -dedup.minScrapeInterval duration
     Leave only the last sample in every time series per each discrete interval equal to -dedup.minScrapeInterval > 0. See also -streamAggr.dedupInterval and https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#deduplication
  -deleteAuthKey value
     authKey for metrics' deletion via /api/v1/admin/tsdb/delete_series and /tags/delSeries. It could be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -deleteAuthKey=file:///abs/path/to/file or -deleteAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -deleteAuthKey=http://host/path or -deleteAuthKey=https://host/path
  -denyQueriesOutsideRetention
     Whether to deny queries outside the configured -retentionPeriod and -futureRetention. When set, then /api/v1/query_range will return an error for queries with 'from' value outside -retentionPeriod or 'to' value beyond -futureRetention. This may be useful when multiple data sources with distinct retentions are hidden behind query-tee
  -denyQueryTracing
     Whether to disable the ability to trace queries. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#query-tracing
  -disablePerDayIndex
     Disable per-day index and use global index for all searches. This may improve performance and decrease disk space usage for the use cases with fixed set of timeseries scattered across a big time range (for example, when loading years of historical data). See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#index-tuning
  -dryRun
     Whether to check config files without running VictoriaMetrics. The following config files are checked: -promscrape.config, -relabelConfig and -streamAggr.config. Unknown config entries aren't allowed in -promscrape.config by default. This can be changed with -promscrape.config.strictParse=false command-line flag
  -enableMetadata
     Whether to enable metadata processing for metrics scraped from targets, received via VictoriaMetrics remote write, Prometheus remote write v1 or OpenTelemetry protocol. See also remoteWrite.maxMetadataPerBlock (default true)
  -enableTCP6
     Whether to enable IPv6 for listening and dialing. By default, only IPv4 TCP and UDP are used
  -envflag.enable
     Whether to enable reading flags from environment variables in addition to the command line. Command line flag values have priority over values from environment vars. Flags are read only from the command line if this flag isn't set. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#environment-variables for more details
  -envflag.prefix string
     Prefix for environment variables if -envflag.enable is set
  -filestream.disableFadvise
     Whether to disable fadvise() syscall when reading large data files. The fadvise() syscall prevents from eviction of recently accessed data from OS page cache during background merges and backups. In some rare cases it is better to disable the syscall if it uses too much CPU
  -finalMergeDelay duration
     Deprecated: this flag does nothing
  -flagsAuthKey value
     Auth key for /flags endpoint. It must be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -flagsAuthKey=file:///abs/path/to/file or -flagsAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -flagsAuthKey=http://host/path or -flagsAuthKey=https://host/path
  -forceFlushAuthKey value
     authKey, which must be passed in query string to /internal/force_flush pages. It overrides -httpAuth.*
     Flag value can be read from the given file when using -forceFlushAuthKey=file:///abs/path/to/file or -forceFlushAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -forceFlushAuthKey=http://host/path or -forceFlushAuthKey=https://host/path
  -forceMergeAuthKey value
     authKey, which must be passed in query string to /internal/force_merge pages. It overrides -httpAuth.*
     Flag value can be read from the given file when using -forceMergeAuthKey=file:///abs/path/to/file or -forceMergeAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -forceMergeAuthKey=http://host/path or -forceMergeAuthKey=https://host/path
  -fs.disableAdviseRandomRead
     Whether to disable FADV_RANDOM and MADV_RANDOM hints for data part files. Typical queries with selectors access data part files at random offsets, so FADV_RANDOM is enforced to reduce excessive disk readahead.Use this flag if your query read pattern benefits from sequential read (e.g. query by metric name without selectors) to prefer FADV_NORMAL. (default true)
  -fs.disableMincore
     Whether to disable the mincore() syscall for checking mmap()ed files. By default, mincore() is used to detect whether mmap()ed file pages are resident in memory. Disabling mincore() may be needed on older ZFS filesystems (below 2.1.5), since it may trigger ZFS bug. See https://github.com/VictoriaMetrics/VictoriaMetrics/issues/10327 for details.
  -fs.disableMmap
     Whether to use pread() instead of mmap() for reading data files. By default, mmap() is used for 64-bit arches and pread() is used for 32-bit arches, since they cannot read data files bigger than 2^32 bytes in memory. mmap() is usually faster for reading small data chunks than pread()
  -fs.maxConcurrency int
     The maximum number of concurrent goroutines to work with files; smaller values may help reducing Go scheduling latency on systems with small number of CPU cores; higher values may help reducing data ingestion latency on systems with high-latency storage such as NFS or Ceph (default 16x CPU cores, capped at 256)
  -futureRetention value
     Data with timestamps bigger than now+futureRetention is automatically deleted. The minimum futureRetention is 2 days. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention
     The following optional suffixes are supported: s (second), h (hour), d (day), w (week), M (month), y (year). If suffix isn't set, then the duration is counted in months (default 2d)
  -graphite.sanitizeMetricName
     Sanitize metric names for the ingested Graphite data. See https://docs.victoriametrics.com/victoriametrics/integrations/graphite/#ingesting
  -graphiteListenAddr string
     TCP and UDP address to listen for Graphite plaintext data. Usually :2003 must be set. Doesn't work if empty. See also -graphiteListenAddr.useProxyProtocol
  -graphiteListenAddr.useProxyProtocol
     Whether to use proxy protocol for connections accepted at -graphiteListenAddr . See https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt
  -graphiteTrimTimestamp duration
     Trim timestamps for Graphite data to this duration. Minimum practical duration is 1s. Higher duration (i.e. 1m) may be used for reducing disk space usage for timestamp data (default 1s)
  -healthcheck
     Whether to check that the running process accepts connections at -httpListenAddr and exit. The exit code is non-zero if the check fails. This is useful for Docker HEALTHCHECK in images without curl or wget. Pass the same -httpListenAddr as the checked process has
  -http.connTimeout duration
     Incoming connections to -httpListenAddr are closed after the configured timeout. This may help evenly spreading load among a cluster of services behind TCP-level load balancer. Zero value disables closing of incoming connections (default 2m0s)
  -http.disableCORS
     Disable CORS for all origins (*)
  -http.disableKeepAlive
     Whether to disable HTTP keep-alive for incoming connections at -httpListenAddr
  -http.disableResponseCompression
     Disable compression of HTTP responses to save CPU resources. By default, compression is enabled to save network bandwidth
  -http.header.csp string
     Value for 'Content-Security-Policy' header, recommended: "default-src 'self'"
  -http.header.disableServerHostname
     Whether to disable 'X-Server-Hostname' header in HTTP responses
  -http.header.frameOptions string
     Value for 'X-Frame-Options' header
  -http.header.hsts string
     Value for 'Strict-Transport-Security' header, recommended: 'max-age=31536000; includeSubDomains'
  -http.idleConnTimeout duration
     Timeout for incoming idle http connections (default 1m0s)
  -http.maxGracefulShutdownDuration duration
     The maximum duration for a graceful shutdown of the HTTP server. During this period the server stops accepting new connections, but it will continue serving existing connections. The remaining in-flight requests are canceled before the deadline, so the shutdown can finish within this duration. A highly loaded server may require increased value for a graceful shutdown (default 7s)
  -http.pathPrefix string
     An optional prefix to add to all the paths handled by http server. For example, if '-http.pathPrefix=/foo/bar' is set, then all the http requests will be handled on '/foo/bar/*' paths. This may be useful for proxied requests. See https://www.robustperception.io/using-external-urls-and-proxies-with-prometheus
  -http.shutdownDelay duration
     Optional delay before http server shutdown. During this delay, the server returns non-OK responses from /health page, so load balancers can route new requests to other servers
  -httpAuth.password value
     Password for HTTP server's Basic Auth. The authentication is disabled if -httpAuth.username is empty
     Flag value can be read from the given file when using -httpAuth.password=file:///abs/path/to/file or -httpAuth.password=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -httpAuth.password=http://host/path or -httpAuth.password=https://host/path
  -httpAuth.username string
     Username for HTTP server's Basic Auth. The authentication is disabled if empty. See also -httpAuth.password
  -httpListenAddr array
     Addresses to listen for incoming http requests. Use unix:/path/to/socket to listen on Unix domain socket. Note that -tls and -httpListenAddr.useProxyProtocol cannot be used with Unix sockets
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -httpListenAddr.useProxyProtocol array
     Whether to use proxy protocol for connections accepted at the corresponding -httpListenAddr . See https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt . With enabled proxy protocol http server cannot serve regular /metrics endpoint. Use -pushmetrics.url for metrics pushing
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -import.maxLineLen size
     The maximum length in bytes of a single line accepted by /api/v1/import; the line length can be limited with 'max_rows_per_line' query arg passed to /api/v1/export
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 10485760)
  -influx.databaseNames array
     Comma-separated list of database names to return from /query and /influx/query API. This can be needed for accepting data from Telegraf plugins such as https://github.com/fangli/fluent-plugin-influxdb
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -influx.forceStreamMode
     Force stream mode parsing for ingested data. See https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/
  -influx.maxLineSize size
     The maximum size in bytes for a single InfluxDB line during parsing. Applicable for stream mode only. See https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 262144)
  -influx.maxRequestSize size
     The maximum size in bytes of a single InfluxDB request. Applicable for batch mode only. See https://docs.victoriametrics.com/victoriametrics/integrations/influxdb/
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 67108864)
  -influxDBLabel string
     Default label for the DB name sent over '?db={db_name}' query parameter (default "db")
  -influxListenAddr string
     TCP and UDP address to listen for InfluxDB line protocol data. Usually :8089 must be set. Doesn't work if empty. This flag isn't needed when ingesting data over HTTP - just send it to http://<victoriametrics>:8428/write . See also -influxListenAddr.useProxyProtocol
  -influxListenAddr.useProxyProtocol
     Whether to use proxy protocol for connections accepted at -influxListenAddr . See https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt
  -influxMeasurementFieldSeparator string
     Separator for '{measurement}{separator}{field_name}' metric name when inserted via InfluxDB line protocol (default "_")
  -influxSkipMeasurement
     Uses '{field_name}' as a metric name while ignoring '{measurement}' and '-influxMeasurementFieldSeparator'
  -influxSkipSingleField
     Uses '{measurement}' instead of '{measurement}{separator}{field_name}' for metric name if InfluxDB line contains only a single field
  -influxTrimTimestamp duration
     Trim timestamps for InfluxDB line protocol data to this duration. Minimum practical duration is 1ms. Higher duration (i.e. 1s) may be used for reducing disk space usage for timestamp data (default 1ms)
  -inmemoryDataFlushInterval duration
     The interval for guaranteed saving of in-memory data to disk. The saved data survives unclean shutdowns such as OOM crash, hardware reset, SIGKILL, etc. Bigger intervals may help increase the lifetime of flash storage with limited write cycles (e.g. Raspberry PI). Smaller intervals increase disk IO load. Minimum supported value is 1s (default 5s)
  -insert.maxQueueDuration duration
     The maximum duration to wait in the queue when -maxConcurrentInserts concurrent insert requests are executed (default 1m0s)
  -internStringCacheExpireDuration duration
     The expiry duration for caches for interned strings. See https://en.wikipedia.org/wiki/String_interning . See also -internStringMaxLen and -internStringDisableCache (default 6m0s)
  -internStringDisableCache
     Whether to disable caches for interned strings. This may reduce memory usage at the cost of higher CPU usage. See https://en.wikipedia.org/wiki/String_interning . See also -internStringCacheExpireDuration and -internStringMaxLen
  -internStringMaxLen int
     The maximum length for strings to intern. A lower limit may save memory at the cost of higher CPU usage. See https://en.wikipedia.org/wiki/String_interning . See also -internStringDisableCache and -internStringCacheExpireDuration (default 500)
  -logNewSeries
     Whether to log new series. This option is for debug purposes only. It can lead to performance issues when big number of new series are ingested into VictoriaMetrics
  -logNewSeriesAuthKey value
     authKey, which must be passed in query string to /internal/log_new_series. It overrides -httpAuth.*
     Flag value can be read from the given file when using -logNewSeriesAuthKey=file:///abs/path/to/file or -logNewSeriesAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -logNewSeriesAuthKey=http://host/path or -logNewSeriesAuthKey=https://host/path
  -loggerDisableTimestamps
     Whether to disable writing timestamps in logs
  -loggerErrorsPerSecondLimit int
     Per-second limit on the number of ERROR messages. If more than the given number of errors are emitted per second, the remaining errors are suppressed. Zero values disable the rate limit
  -loggerFormat string
     Format for logs. Possible values: default, json (default "default")
  -loggerJSONFields string
     Allows renaming fields in JSON formatted logs. Example: "ts:timestamp,msg:message" renames "ts" to "timestamp" and "msg" to "message". Supported fields: ts, level, caller, msg
  -loggerLevel string
     Minimum level of errors to log. Possible values: INFO, WARN, ERROR, FATAL, PANIC (default "INFO")
  -loggerMaxArgLen int
     The maximum length of a single logged argument. Longer arguments are replaced with 'arg_start..arg_end', where 'arg_start' and 'arg_end' is prefix and suffix of the arg with the length not exceeding -loggerMaxArgLen / 2 (default 5000)
  -loggerOutput string
     Output for the logs. Supported values: stderr, stdout (default "stderr")
  -loggerTimezone string
     Timezone to use for timestamps in logs. Timezone must be a valid IANA Time Zone. For example: America/New_York, Europe/Berlin, Etc/GMT+3 or Local (default "UTC")
  -loggerWarnsPerSecondLimit int
     Per-second limit on the number of WARN messages. If more than the given number of warns are emitted per second, then the remaining warns are suppressed. Zero values disable the rate limit
  -maxBackfillAge value
     The maximum allowed age for the ingested samples with historical timestamps. Samples with timestamps older than now-maxBackfillAge are rejected during data ingestion. By default, or when set to 0, -maxBackfillAge equals to -retentionPeriod, e.g. it is unlimited within the configured retention. This can be useful for limiting ingestion of historical samples, for example, when older data has been moved to another storage tier. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#retention
     The following optional suffixes are supported: s (second), h (hour), d (day), w (week), M (month), y (year). If suffix isn't set, then the duration is counted in months (default 0)
  -maxConcurrentInserts int
     The maximum number of concurrent insert requests. Set higher value when clients send data over slow networks. Default value depends on the number of available CPU cores. It should work fine in most cases since it minimizes resource usage. See also -insert.maxQueueDuration (default 2x CPU cores)
  -maxIngestionRate int
     The maximum number of samples vmsingle can receive per second. Data ingestion is paused when the limit is exceeded. By default there are no limits on samples ingestion rate.
  -maxInsertRequestSize size
     The maximum size in bytes of a single Prometheus remote_write API request
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 33554432)
  -maxLabelNameLen int
     The maximum length of label name in the accepted time series. Series with longer label name are ignored. In this case the vm_rows_ignored_total{reason="too_long_label_name"} metric at /metrics page is incremented. Value must be in range 1..65535. (default 256)
  -maxLabelValueLen int
     The maximum length of label values in the accepted time series. Series with longer label value are ignored. In this case the vm_rows_ignored_total{reason="too_long_label_value"} metric at /metrics page is incremented. Value must be in range 1..65535. (default 4096)
  -maxLabelsPerTimeseries int
     The maximum number of labels per time series to be accepted. Series with superfluous labels are ignored. In this case the vm_rows_ignored_total{reason="too_many_labels"} metric at /metrics page is incremented. (default 40)
  -memory.allowedBytes size
     Allowed size of system memory VictoriaMetrics caches may occupy. This option overrides -memory.allowedPercent if set to a non-zero value. Too low a value may increase the cache miss rate usually resulting in higher CPU and disk IO usage. Too high a value may evict too much data from the OS page cache resulting in higher disk IO usage. The process may behave unexpectedly if this flag is set too small (e.g., 1 byte).
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 0)
  -memory.allowedPercent float
     Allowed percent of system memory VictoriaMetrics caches may occupy. See also -memory.allowedBytes. Too low a value may increase cache miss rate usually resulting in higher CPU and disk IO usage. Too high a value may evict too much data from the OS page cache which will result in higher disk IO usage (default 60)
  -metricNamesStatsResetAuthKey value
     authKey for resetting metric names usage cache via /api/v1/admin/status/metric_names_stats/reset. It overrides -httpAuth.*. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#track-ingested-metrics-usage
     Flag value can be read from the given file when using -metricNamesStatsResetAuthKey=file:///abs/path/to/file or -metricNamesStatsResetAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -metricNamesStatsResetAuthKey=http://host/path or -metricNamesStatsResetAuthKey=https://host/path
  -metrics.exposeMetadata
     Whether to expose TYPE and HELP metadata at the /metrics page, which is exposed at -httpListenAddr . The metadata may be needed when the /metrics page is consumed by systems, which require this information. For example, Managed Prometheus in Google Cloud - https://cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#missing-metric-type
  -metricsAuthKey value
     Auth key for /metrics endpoint. It must be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -metricsAuthKey=file:///abs/path/to/file or -metricsAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -metricsAuthKey=http://host/path or -metricsAuthKey=https://host/path
  -newrelic.maxInsertRequestSize size
     The maximum size in bytes of a single NewRelic request to /newrelic/infra/v2/metrics/events/bulk
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 67108864)
  -opentelemetry.convertMetricNamesToPrometheus
     Whether to convert only metric names into Prometheus-compatible format for the metrics ingested via OpenTelemetry protocol; see https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/
  -opentelemetry.ignoreResourceAttributes array
     Control which resource attributes to ignore, can only be set when 'opentelemetry.promoteAllResourceAttributes' is true.
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -opentelemetry.labelNameUnderscoreSanitization
     Whether to enable prepending of 'key' to labels starting with '_' when -opentelemetry.usePrometheusNaming is enabled. Reserved labels starting with '__' are not modified. See https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/ (default true)
  -opentelemetry.maxRequestSize size
     The maximum size in bytes of a single OpenTelemetry request
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 67108864)
  -opentelemetry.promoteAllResourceAttributes
     Whether to promote all resource attributes to labels, except for the ones configured with 'opentelemetry.ignoreResourceAttributes'. (default true)
  -opentelemetry.promoteResourceAttributes array
     Promote specific list of resource attributes to labels.
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -opentelemetry.promoteScopeMetadata
     Whether to promote OTel scope metadata (i.e. name, version, schema URL, and attributes) to metric labels. (default true)
  -opentelemetry.usePrometheusNaming
     Whether to convert metric names and labels into Prometheus-compatible format for the metrics ingested via OpenTelemetry protocol; see https://docs.victoriametrics.com/victoriametrics/integrations/opentelemetry/
  -opentsdbHTTPListenAddr string
     TCP address to listen for OpenTSDB HTTP put requests. Usually :4242 must be set. Doesn't work if empty. See also -opentsdbHTTPListenAddr.useProxyProtocol
  -opentsdbHTTPListenAddr.useProxyProtocol
     Whether to use proxy protocol for connections accepted at -opentsdbHTTPListenAddr . See https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt
  -opentsdbListenAddr string
     TCP and UDP address to listen for OpenTSDB metrics. Telnet put messages and HTTP /api/put messages are simultaneously served on TCP port. Usually :4242 must be set. Doesn't work if empty. See also -opentsdbListenAddr.useProxyProtocol
  -opentsdbListenAddr.useProxyProtocol
     Whether to use proxy protocol for connections accepted at -opentsdbListenAddr . See https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt
  -opentsdbTrimTimestamp duration
     Trim timestamps for OpenTSDB 'telnet put' data to this duration. Minimum practical duration is 1s. Higher duration (i.e. 1m) may be used for reducing disk space usage for timestamp data (default 1s)
  -opentsdbhttp.maxInsertRequestSize size
     The maximum size of OpenTSDB HTTP put request
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 33554432)
  -opentsdbhttpTrimTimestamp duration
     Trim timestamps for OpenTSDB HTTP data to this duration. Minimum practical duration is 1ms. Higher duration (i.e. 1s) may be used for reducing disk space usage for timestamp data (default 1ms)
  -pprofAuthKey value
     Auth key for /debug/pprof/* endpoints. It must be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -pprofAuthKey=file:///abs/path/to/file or -pprofAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -pprofAuthKey=http://host/path or -pprofAuthKey=https://host/path
  -precisionBits int
     The number of precision bits to store per each value. Lower precision bits improves data compression at the cost of precision loss (default 64)
  -prevCacheRemovalPercent float
     Items in the previous caches are removed when the percent of requests it serves becomes lower than this value. Higher values reduce memory usage at the cost of higher CPU usage. See also -cacheExpireDuration (default 0.1)
  -projectID uint
     The projectID of the stored data
  -promscrape.azureSDCheckInterval duration
     Interval for checking for changes in Azure. This works only if azure_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#azure_sd_configs for details (default 1m0s)
  -promscrape.cluster.memberLabel string
     If non-empty, then the label with this name and the -promscrape.cluster.memberNum value is added to all the scraped metrics. See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more info
  -promscrape.cluster.memberNum string
     The number of vmagent instance in the cluster of scrapers. It must be a unique value in the range 0 ... promscrape.cluster.membersCount-1 across scrapers in the cluster. Can be specified as pod name of Kubernetes StatefulSet - pod-name-Num, where Num is a numeric part of pod name. See also -promscrape.cluster.memberLabel . See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more info (default "0")
  -promscrape.cluster.memberURLTemplate string
     An optional template for URL to access vmagent instance with the given -promscrape.cluster.memberNum value. Every %d occurrence in the template is substituted with -promscrape.cluster.memberNum at urls to vmagent instances responsible for scraping the given target at /service-discovery page. For example -promscrape.cluster.memberURLTemplate='http://vmagent-%d:8429/targets'. See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more details
  -promscrape.cluster.membersCount int
     The number of members in a cluster of scrapers. Each member must have a unique -promscrape.cluster.memberNum in the range 0 ... promscrape.cluster.membersCount-1 . Each member then scrapes roughly 1/N of all the targets. By default, cluster scraping is disabled, i.e. a single scraper scrapes all the targets. See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more info (default 1)
  -promscrape.cluster.name string
     Optional name of the cluster. If multiple vmagent clusters scrape the same targets, then each cluster must have unique name in order to properly de-duplicate samples received from these clusters. See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more info
  -promscrape.cluster.replicationFactor int
     The number of members in the cluster, which scrape the same targets. If the replication factor is greater than 1, then the deduplication must be enabled at remote storage side. See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more info (default 1)
  -promscrape.cluster.shardByLabels array
     Optional list of target labels, which will be used for sharding targets among cluster members if -promscrape.cluster.membersCount is greater than 1. If none of the specified labels are found in a target, then all the target labels will be used for sharding. See https://docs.victoriametrics.com/victoriametrics/vmagent/#scraping-big-number-of-targets for more info
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -promscrape.config string
     Optional path to Prometheus config file with 'scrape_configs' section containing targets to scrape. The path can point to local file and to http url. See https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter for details
  -promscrape.config.dryRun
     Checks -promscrape.config file for errors and unsupported fields and then exits. Returns non-zero exit code on parsing errors and emits these errors to stderr. See also -promscrape.config.strictParse command-line flag. Pass -loggerLevel=ERROR if you don't need to see info messages in the output.
  -promscrape.config.strictParse
     Whether to deny unsupported fields in -promscrape.config . Set to false in order to silently skip unsupported fields (default true)
  -promscrape.configCheckInterval duration
     Interval for checking for changes in -promscrape.config file. By default, the checking is disabled. See how to reload -promscrape.config file at https://docs.victoriametrics.com/victoriametrics/vmagent/#configuration-update
  -promscrape.consul.waitTime duration
     Wait time used by Consul service discovery. Default value is used if not set
  -promscrape.consulSDCheckInterval duration
     Interval for checking for changes in Consul. This works only if consul_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#consul_sd_configs for details (default 30s)
  -promscrape.consulagentSDCheckInterval duration
     Interval for checking for changes in Consul Agent. This works only if consulagent_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#consulagent_sd_configs for details (default 30s)
  -promscrape.digitaloceanSDCheckInterval duration
     Interval for checking for changes in digital ocean. This works only if digitalocean_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#digitalocean_sd_configs for details (default 1m0s)
  -promscrape.disableCompression
     Whether to disable sending 'Accept-Encoding: gzip' request headers to all the scrape targets. This may reduce CPU usage on scrape targets at the cost of higher network bandwidth utilization. It is possible to set 'disable_compression: true' individually per each 'scrape_config' section in '-promscrape.config' for fine-grained control
  -promscrape.disableKeepAlive
     Whether to disable HTTP keep-alive connections when scraping all the targets. This may be useful when targets has no support for HTTP keep-alive connection. It is possible to set 'disable_keepalive: true' individually per each 'scrape_config' section in '-promscrape.config' for fine-grained control. Note that disabling HTTP keep-alive may increase load on both vmagent and scrape targets
  -promscrape.discovery.concurrency int
     The maximum number of concurrent requests to Prometheus autodiscovery API (Consul, Kubernetes, etc.) (default 100)
  -promscrape.discovery.concurrentWaitTime duration
     The maximum duration for waiting to perform API requests if more than -promscrape.discovery.concurrency requests are simultaneously performed (default 1m0s)
  -promscrape.dnsSDCheckInterval duration
     Interval for checking for changes in dns. This works only if dns_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#dns_sd_configs for details (default 30s)
  -promscrape.dockerSDCheckInterval duration
     Interval for checking for changes in docker. This works only if docker_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#docker_sd_configs for details (default 30s)
  -promscrape.dockerswarmSDCheckInterval duration
     Interval for checking for changes in dockerswarm. This works only if dockerswarm_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#dockerswarm_sd_configs for details (default 30s)
  -promscrape.dropOriginalLabels
     Whether to drop original labels for scrape targets at /targets and /api/v1/targets pages. This may be needed for reducing memory usage when original labels for big number of scrape targets occupy big amounts of memory. Note that this reduces debuggability for improper per-target relabeling configs
  -promscrape.ec2SDCheckInterval duration
     Interval for checking for changes in ec2. This works only if ec2_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#ec2_sd_configs for details (default 1m0s)
  -promscrape.eurekaSDCheckInterval duration
     Interval for checking for changes in eureka. This works only if eureka_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#eureka_sd_configs for details (default 30s)
  -promscrape.fileSDCheckInterval duration
     Interval for checking for changes in 'file_sd_config'. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#file_sd_configs for details (default 1m0s)
  -promscrape.gceSDCheckInterval duration
     Interval for checking for changes in gce. This works only if gce_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#gce_sd_configs for details (default 1m0s)
  -promscrape.hetznerSDCheckInterval duration
     Interval for checking for changes in Hetzner API. This works only if hetzner_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#hetzner_sd_configs for details (default 1m0s)
  -promscrape.httpSDCheckInterval duration
     Interval for checking for changes in http endpoint service discovery. This works only if http_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http_sd_configs for details (default 1m0s)
  -promscrape.kubernetes.apiServerTimeout duration
     How frequently to reload the full state from Kubernetes API server (default 30m0s)
  -promscrape.kubernetes.attachNamespaceMetadataAll
     Whether to set attach_metadata.namespace=true for all the kubernetes_sd_configs at -promscrape.config . It is possible to set attach_metadata.namespace=false individually per each kubernetes_sd_configs . See https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs
  -promscrape.kubernetes.attachNodeMetadataAll
     Whether to set attach_metadata.node=true for all the kubernetes_sd_configs at -promscrape.config . It is possible to set attach_metadata.node=false individually per each kubernetes_sd_configs . See https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs
  -promscrape.kubernetes.useHTTP2Client
     Whether to use HTTP/2 client for connection to Kubernetes API server. This may reduce amount of concurrent connections to API server when watching for a big number of Kubernetes objects.
  -promscrape.kubernetesSDCheckInterval duration
     Interval for checking for changes in Kubernetes API server. This works only if kubernetes_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#kubernetes_sd_configs for details (default 30s)
  -promscrape.kumaSDCheckInterval duration
     Interval for checking for changes in kuma service discovery. This works only if kuma_sd_configs is configured in '-promscrape.config' file. See https://docs.victoriametrics.com/victoriametrics/sd_configs/#kuma_sd_configs for details (default 30s)
  -promscrape.linodeSDCheckInterval duration
