<!-- Part 2 of 2 of victoriametrics/vmagent_common_flags.md (split because the page is big). -->

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
  -reloadAuthKey value
     Auth key for /-/reload http endpoint. It must be passed via authKey query arg. It overrides -httpAuth.*
     Flag value can be read from the given file when using -reloadAuthKey=file:///abs/path/to/file or -reloadAuthKey=file://./relative/path/to/file.
     Flag value can be read from the given http/https url when using -reloadAuthKey=http://host/path or -reloadAuthKey=https://host/path
  -remoteWrite.aws.accessKey array
     Optional AWS AccessKey to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.ec2Endpoint array
     Optional AWS EC2 API endpoint to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.region array
     Optional AWS region to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.roleARN array
     Optional AWS roleARN to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.secretKey array
     Optional AWS SecretKey to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.service array
     Optional AWS Service to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set. Defaults to "aps"
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.stsEndpoint array
     Optional AWS STS API endpoint to use for the corresponding -remoteWrite.url if -remoteWrite.aws.useSigv4 is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.aws.useSigv4 array
     Enables SigV4 request signing for the corresponding -remoteWrite.url. It is expected that other -remoteWrite.aws.* command-line flags are set if sigv4 request signing is enabled
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.basicAuth.password array
     Optional basic auth password to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.basicAuth.passwordFile array
     Optional path to basic auth password to use for the corresponding -remoteWrite.url. The file is re-read every second
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.basicAuth.username array
     Optional basic auth username to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.basicAuth.usernameFile array
     Optional path to basic auth username to use for the corresponding -remoteWrite.url. The file is re-read every second
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.bearerToken array
     Optional bearer auth token to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.bearerTokenFile array
     Optional path to bearer token file to use for the corresponding -remoteWrite.url. The token is re-read from the file every second
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.disableMetadata array
     Whether to disable sending metadata to the corresponding -remoteWrite.url. By default, metadata sending is controlled by the global -enableMetadata flag, and is always disabled for URLs with -remoteWrite.mdx.enable=true
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.disableOnDiskQueue array
     Whether to disable storing pending data to -remoteWrite.tmpDataPath when the remote storage system at the corresponding -remoteWrite.url cannot keep up with the data ingestion rate. See https://docs.victoriametrics.com/victoriametrics/vmagent/#disabling-on-disk-persistence . See also -remoteWrite.dropSamplesOnOverload
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.dropSamplesOnOverload
     Whether to drop samples when -remoteWrite.disableOnDiskQueue is set and if the samples cannot be pushed into the configured -remoteWrite.url systems in a timely manner. See https://docs.victoriametrics.com/victoriametrics/vmagent/#disabling-on-disk-persistence
  -remoteWrite.flushInterval duration
     Interval for flushing the data to remote storage. This option takes effect only when less than -remoteWrite.maxRowsPerBlock data points per -remoteWrite.flushInterval are pushed to -remoteWrite.url (default 1s)
  -remoteWrite.forcePromProto array
     Whether to force Prometheus remote write protocol for sending data to the corresponding -remoteWrite.url . See https://docs.victoriametrics.com/victoriametrics/vmagent/#victoriametrics-remote-write-protocol
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.forceVMProto array
     Whether to force VictoriaMetrics remote write protocol for sending data to the corresponding -remoteWrite.url . See https://docs.victoriametrics.com/victoriametrics/vmagent/#victoriametrics-remote-write-protocol
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.headers array
     Optional HTTP headers to send with each request to the corresponding -remoteWrite.url. For example, -remoteWrite.headers='My-Auth:foobar' would send 'My-Auth: foobar' HTTP header with every request to the corresponding -remoteWrite.url. Multiple headers must be delimited by '^^': -remoteWrite.headers='header1:value1^^header2:value2'
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.inmemoryQueues array
     The number of additional workers per each -remoteWrite.url, which send only recently ingested data from the in-memory queue, while the file-based queue at -remoteWrite.tmpDataPath is drained by workers configured via -remoteWrite.queues. This reduces delivery lag for fresh samples when the file-based queue contains a backlog accumulated during remote storage outages. (default 0)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.keepDanglingQueues
     Keep persistent queues contents at -remoteWrite.tmpDataPath in case there are no matching -remoteWrite.url. Useful when -remoteWrite.url is changed temporarily and persistent queue files will be needed later on.
  -remoteWrite.label array
     Optional label in the form 'name=value' to add to all the metrics before sending them to all -remoteWrite.url.
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.maxBlockSize size
     The maximum block size to send to remote storage. Bigger blocks may improve performance at the cost of the increased memory usage. See also -remoteWrite.maxRowsPerBlock
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB (default 8388608)
  -remoteWrite.maxDailySeries int
     The maximum number of unique series vmagent can send to remote storage systems during the last 24 hours. Excess series are logged and dropped. This can be useful for limiting series churn rate. Setting this flag to '-1' sets limit to maximum possible value (2147483647) which is useful in order to enable series tracking without enforcing limits. See https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter
  -remoteWrite.maxDiskUsagePerURL array
     The maximum file-based buffer size in bytes at -remoteWrite.tmpDataPath for each -remoteWrite.url. When buffer size reaches the configured maximum, then old data is dropped when adding new data to the buffer. Buffered data is stored in ~500MB chunks. It is recommended to set the value for this flag to a multiple of the block size 500MB. Disk usage is unlimited if the value is set to 0
     Supports the following optional suffixes for size values: KB, MB, GB, TB, KiB, MiB, GiB, TiB. (default 0)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.maxHourlySeries int
     The maximum number of unique series vmagent can send to remote storage systems during the last hour. Excess series are logged and dropped. This can be useful for limiting series cardinality. Setting this flag to '-1' sets limit to maximum possible value (2147483647) which is useful in order to enable series tracking without enforcing limits. See https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter
  -remoteWrite.maxMetadataPerBlock int
     The maximum number of metadata to send in each block to remote storage. Higher number may improve performance at the cost of the increased memory usage. See also -remoteWrite.maxBlockSize (default 5000)
  -remoteWrite.maxRowsPerBlock int
     The maximum number of samples to send in each block to remote storage. Higher number may improve performance at the cost of the increased memory usage. See also -remoteWrite.maxBlockSize (default 10000)
  -remoteWrite.mdx.enable array
     Whether to only retain metrics from VictoriaMetrics services before sending them to the corresponding -remoteWrite.url. Can be combined with -remoteWrite.obfuscateLabels to hide sensitive label values in the forwarded metrics. Please see https://docs.victoriametrics.com/victoriametrics/vmagent/#monitoring-data-exchange
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.oauth2.clientID array
     Optional OAuth2 clientID to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.oauth2.clientSecret array
     Optional OAuth2 clientSecret to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.oauth2.clientSecretFile array
     Optional OAuth2 clientSecretFile to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.oauth2.endpointParams array
     Optional OAuth2 endpoint parameters to use for the corresponding -remoteWrite.url . The endpoint parameters must be set in JSON format: {"param1":"value1",...,"paramN":"valueN"}
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.oauth2.scopes array
     Optional OAuth2 scopes to use for the corresponding -remoteWrite.url. Scopes must be delimited by ';'
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.oauth2.tokenUrl array
     Optional OAuth2 tokenURL to use for the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.obfuscateLabels ^^
     List of label names whose values will be obfuscated before being sent to the corresponding -remoteWrite.url. Multiple label names should be separated by ^^, e.g. "job^^instance,ip". Can be combined with -remoteWrite.mdx.enable to hide sensitive label values in VictoriaMetrics self-monitoring metrics. Please see https://docs.victoriametrics.com/victoriametrics/vmagent/#obfuscating-label-values
     Supports an `array` of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.proxyURL array
     Optional proxy URL for writing data to the corresponding -remoteWrite.url. Supported proxies: http, https, socks5. Example: -remoteWrite.proxyURL=socks5://proxy:1234
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.queues array
     The number of concurrent queues to each -remoteWrite.url. Set more queues if default number of queues isn't enough for sending high volume of collected data to remote storage. Default value depends on the number of available CPU cores. It should work fine in most cases since it minimizes resource usage (default 2x CPU cores)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.rateLimit array
     Optional rate limit in bytes per second for data sent to the corresponding -remoteWrite.url. By default, the rate limit is disabled. It can be useful for limiting load on remote storage when big amounts of buffered data is sent after temporary unavailability of the remote storage. See also -maxIngestionRate (default 0)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.relabelConfig string
     Optional path to file with relabeling configs, which are applied to all the metrics before sending them to -remoteWrite.url. See also -remoteWrite.urlRelabelConfig. The path can point either to local file or to http url. See https://docs.victoriametrics.com/victoriametrics/relabeling/
  -remoteWrite.retryMaxInterval array
     The maximum delay between retry attempts to send a block of data to the corresponding -remoteWrite.url.  The delay doubles with each retry until this maximum is reached, after which it remains constant. See also -remoteWrite.retryMinInterval (default 1m0s)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.retryMaxTime array
     The max time spent on retry attempts to send a block of data to the corresponding -remoteWrite.url. This flag is deprecated, use -remoteWrite.retryMaxInterval instead (default 1m0s)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.retryMinInterval array
     The minimum delay between retry attempts to send a block of data to the corresponding -remoteWrite.url. Every next retry attempt will double the delay to prevent hammering of remote database. See also -remoteWrite.retryMaxInterval (default 1s)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.roundDigits array
     Round metric values to this number of decimal digits after the point before writing them to remote storage. Examples: -remoteWrite.roundDigits=2 would round 1.236 to 1.24, while -remoteWrite.roundDigits=-1 would round 126.78 to 130. By default, digits rounding is disabled. Set it to 100 for disabling it for a particular remote storage. This option may be used for improving data compression for the stored metrics. See also -remoteWrite.significantFigures (default 100)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.sendTimeout array
     Timeout for sending a single block of data to the corresponding -remoteWrite.url (default 1m0s)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.shardByURL
     Whether to shard outgoing series across all the remote storage systems enumerated via -remoteWrite.url. By default the data is replicated across all the -remoteWrite.url . See https://docs.victoriametrics.com/victoriametrics/vmagent/#sharding-among-remote-storages . See also -remoteWrite.shardByURLReplicas
  -remoteWrite.shardByURL.ignoreLabels array
     Optional list of labels, which must be ignored when sharding outgoing samples among remote storage systems if -remoteWrite.shardByURL command-line flag is set. By default all the labels are used for sharding in order to gain even distribution of series over the specified -remoteWrite.url systems. See also -remoteWrite.shardByURL.labels
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.shardByURL.labels array
     Optional list of labels, which must be used for sharding outgoing samples among remote storage systems if -remoteWrite.shardByURL command-line flag is set. By default all the labels are used for sharding in order to gain even distribution of series over the specified -remoteWrite.url systems. See also -remoteWrite.shardByURL.ignoreLabels
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.shardByURLReplicas int
     How many copies of data to make among remote storage systems enumerated via -remoteWrite.url when -remoteWrite.shardByURL is set. See https://docs.victoriametrics.com/victoriametrics/vmagent/#sharding-among-remote-storages (default 1)
  -remoteWrite.showURL
     Whether to show -remoteWrite.url in the exported metrics. It is hidden by default, since it can contain sensitive info such as auth key
  -remoteWrite.significantFigures array
     The number of significant figures to leave in metric values before writing them to remote storage. See https://en.wikipedia.org/wiki/Significant_figures . Zero value saves all the significant figures. This option may be used for improving data compression for the stored metrics. See also -remoteWrite.roundDigits (default 0)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.streamAggr.config array
     Optional path to file with stream aggregation config for the corresponding -remoteWrite.url. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/ . See also -remoteWrite.streamAggr.keepInput, -remoteWrite.streamAggr.dropInput and -remoteWrite.streamAggr.dedupInterval
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.streamAggr.dedupInterval array
     Input samples are de-duplicated with this interval before optional aggregation with -remoteWrite.streamAggr.config at the corresponding -remoteWrite.url. See also -dedup.minScrapeInterval and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#deduplication (default 0s)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.streamAggr.dropInput array
     Whether to drop input samples that not matching any rule in the corresponding -remoteWrite.streamAggr.config. By default, only matched raw samples are dropped, while unmatched samples are written to the corresponding -remoteWrite.url . See also -remoteWrite.streamAggr.keepInput and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.streamAggr.dropInputLabels array
     An optional list of labels to drop from samples before stream de-duplication and aggregation with -remoteWrite.streamAggr.config and -remoteWrite.streamAggr.dedupInterval at the corresponding -remoteWrite.url. Multiple labels per remoteWrite.url must be delimited by '^^': -remoteWrite.streamAggr.dropInputLabels='replica^^az,replica'. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#dropping-unneeded-labels
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.streamAggr.enableWindows array
     Enables aggregation within fixed windows for all remote write's aggregators. This allows to get more precise results, but impacts resource usage as it requires twice more memory to store two states. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#aggregation-windows.
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.streamAggr.ignoreFirstIntervals array
     Number of aggregation intervals to skip after the start for the corresponding -remoteWrite.streamAggr.config at the corresponding -remoteWrite.url. Increase this value if you observe incorrect aggregation results after vmagent restarts. It could be caused by receiving buffered delayed data from clients pushing data into the vmagent. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#ignore-aggregation-intervals-on-start (default 0)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.streamAggr.ignoreOldSamples array
     Whether to ignore input samples with old timestamps outside the current aggregation interval for the corresponding -remoteWrite.streamAggr.config at the corresponding -remoteWrite.url. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#ignoring-old-samples
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.streamAggr.keepInput array
     Whether to keep input samples that match any rule in the corresponding -remoteWrite.streamAggr.config. By default, matched raw samples are aggregated and dropped, while unmatched samples are written to the corresponding -remoteWrite.url . See also -remoteWrite.streamAggr.dropInput and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.tlsCAFile array
     Optional path to TLS CA file to use for verifying connections to the corresponding -remoteWrite.url. By default, system CA is used
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.tlsCertFile array
     Optional path to client-side TLS certificate file to use when connecting to the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.tlsHandshakeTimeout array
     The timeout for establishing tls connections to the corresponding -remoteWrite.url (default 20s)
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to default value.
  -remoteWrite.tlsInsecureSkipVerify array
     Whether to skip tls verification when connecting to the corresponding -remoteWrite.url
     Supports array of values separated by comma or specified via multiple flags.
     Empty values are set to false.
  -remoteWrite.tlsKeyFile array
     Optional path to client-side TLS certificate key to use when connecting to the corresponding -remoteWrite.url
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.tlsServerName array
     Optional TLS server name to use for connections to the corresponding -remoteWrite.url. By default, the server name from -remoteWrite.url is used
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.tmpDataPath string
     Path to directory for storing pending data, which isn't sent to the configured -remoteWrite.url . See also -remoteWrite.maxDiskUsagePerURL and -remoteWrite.disableOnDiskQueue (default "vmagent-remotewrite-data")
  -remoteWrite.url array
     Remote storage URL to write data to. It must support either VictoriaMetrics remote write protocol or Prometheus remote_write protocol. Example url: http://<victoriametrics-host>:8428/api/v1/write . Pass multiple -remoteWrite.url options in order to replicate the collected data to multiple remote storage systems. The data can be sharded among the configured remote storage systems if -remoteWrite.shardByURL flag is set
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.urlRelabelConfig array
     Optional path to relabel configs for the corresponding -remoteWrite.url. See also -remoteWrite.relabelConfig. The path can point either to local file or to http url. See https://docs.victoriametrics.com/victoriametrics/relabeling/
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -remoteWrite.vmProtoCompressLevel int
     The compression level for VictoriaMetrics remote write protocol. Higher values reduce network traffic at the cost of higher CPU usage. Negative values reduce CPU usage at the cost of increased network traffic. See https://docs.victoriametrics.com/victoriametrics/vmagent/#victoriametrics-remote-write-protocol
  -secret.flags array
     Comma-separated list of flag names with secret values. Values for these flags are hidden in logs and on /metrics page
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -sortLabels
     Whether to sort labels for incoming samples before writing them to all the configured remote storage systems. This may be needed for reducing memory usage at remote storage when the order of labels in incoming samples is random. For example, if m{k1="v1",k2="v2"} may be sent as m{k2="v2",k1="v1"}Enabled sorting for labels can slow down ingestion performance a bit
  -streamAggr.config string
     Optional path to file with stream aggregation config. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/ . See also -streamAggr.keepInput, -streamAggr.dropInput and -streamAggr.dedupInterval
  -streamAggr.dedupInterval duration
     Input samples are de-duplicated with this interval on aggregator before optional aggregation with -streamAggr.config . See also -dedup.minScrapeInterval and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#deduplication
  -streamAggr.dropInput
     Whether to drop input samples that not matching any rule in -streamAggr.config. By default, only matched raw samples are dropped, while unmatched samples are written to the remote storage. See also -streamAggr.keepInput and https://docs.victoriametrics.com/victoriametrics/stream-aggregation/
  -streamAggr.dropInputLabels array
     An optional list of labels to drop from samples for aggregator before stream de-duplication and aggregation . See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#dropping-unneeded-labels
     Supports an array of values separated by comma or specified via multiple flags.
     Each array item can contain comma inside single-quoted or double-quoted string, {}, [] and () braces.
  -streamAggr.enableWindows
     Enables aggregation within fixed windows for all global aggregators. This allows to get more precise results, but impacts resource usage as it requires twice more memory to store two states. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#aggregation-windows.
  -streamAggr.ignoreFirstIntervals int
     Number of aggregation intervals to skip after the start for aggregator. Increase this value if you observe incorrect aggregation results after vmagent restarts. It could be caused by receiving unordered delayed data from clients pushing data into the vmagent. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#ignore-aggregation-intervals-on-start
  -streamAggr.ignoreOldSamples
     Whether to ignore input samples with old timestamps outside the current aggregation interval for aggregator. See https://docs.victoriametrics.com/victoriametrics/stream-aggregation/#ignoring-old-samples
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
