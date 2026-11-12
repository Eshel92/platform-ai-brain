<!-- Part 6 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## puppetdb_sd_configs

PuppetDB SD configuration{{% available_from "v1.106.0" %}} allows retrieving scrape targets from [PuppetDB](https://www.puppet.com/docs/puppetdb/8/overview.html) resources.

This SD discovers resources and will create a target for each resource returned by the API.

Configuration example:

```yaml
scrape_configs:
- job_name: puppetdb_job
  puppetdb_sd_configs:
    # The URL of the PuppetDB root query endpoint.
    - url: <string>

      # Puppet Query Language (PQL) query. Only resources are supported.
      # https://puppet.com/docs/puppetdb/latest/api/query/v4/pql.html
      query: <string>

      # Whether to include the parameters as meta labels.
      # Due to the differences between parameter types and Prometheus labels,
      # some parameters might not be rendered. The format of the parameters might
      # also change in future releases.
      #
      # Note: Enabling this exposes parameters in the VMUI and API. Make sure
      # that you don't have secrets exposed as parameters if you enable this.
      #
      # include_parameters: <boolean> | default false

      # The port to scrape metrics from.
      #
      # port: <int> | default = 80

      # Additional HTTP API client options can be specified here.
      # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

The resource address is the `certname` of the resource and can be changed during relabeling.
The following meta labels are available on targets during relabeling:

* `__meta_puppetdb_query`: the Puppet Query Language (PQL) query.
* `__meta_puppetdb_certname`: the name of the node associated with the resource.
* `__meta_puppetdb_resource`: a SHA-1 hash of the resource’s type, title, and parameters, for identification.
* `__meta_puppetdb_type`: the resource type.
* `__meta_puppetdb_title`: the resource title.
* `__meta_puppetdb_exported`: whether the resource is exported (`"true"` or `"false"`).
* `__meta_puppetdb_tags`: comma separated list of resource tags.
* `__meta_puppetdb_file`: the manifest file in which the resource was declared.
* `__meta_puppetdb_environment`: the environment of the node associated with the resource.
* `__meta_puppetdb_parameter_<parametername>`: the parameters of the resource.

The list of discovered PuppetDB targets is refreshed at the interval, which can be configured via `-promscrape.puppetdbSDCheckInterval` command-line flag.


## static_configs

A static config allows specifying a list of targets and a common label set for them.

Configuration example:

```yaml
scrape_configs:
- job_name: static
  static_configs:

    # targets must contain a list of `host:port` targets to scrape.
    # The `http://host:port/metrics` endpoint is scraped per each configured target then.
    # The `http` scheme can be changed to `https` by setting it via `scheme` field at `scrape_config` level.
    # The `/metrics` path can be changed to arbitrary path via `metrics_path` field at `scrape_config` level.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#scrape_configs .
    #
    # Alternatively the scheme and path can be changed via `relabel_configs` section at `scrape_config` level.
    # See https://docs.victoriametrics.com/victoriametrics/relabeling/ .
    #
    # It is also possible specifying full target urls here, e.g. "http://host:port/metrics/path?query_args"
    #
  - targets:
    - "vmsingle1:8428"
    - "vmsingleN:8428"

    # labels is an optional labels to add to all the targets.
    #
    # labels:
    #   <labelname1>: "<labelvalue1>"
    #   ...
    #   <labelnameN>: "<labelvalueN>"
```

See [these examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/#static-configs) on how to configure scraping for static targets.


## vultr_sd_configs

Vultr SD configuration discovers scrape targets from [Vultr](https://www.vultr.com/) Instances.

Configuration example:

```yaml
scrape_configs:
- job_name: vultr
  vultr_sd_configs:

    # bearer_token is a Bearer token to send in every HTTP API request during service discovery (mandatory).
    # See: https://my.vultr.com/settings/#settingsapi
  - bearer_token: "..."

    # Vultr provides query arguments to filter instances.
    # See: https://www.vultr.com/api/#tag/instances

    # label is an optional query arguments to filter instances by label.
    #
    # label: "..."

    # main_ip is an optional query arguments to filter instances by main ip address.
    #
    # main_ip: "..."

    # region is an optional query arguments to filter instances by region id.
    #
    # region: "..."

    # firewall_group_id is an optional query arguments to filter instances by firewall group id.
    #
    # firewall_group_id: "..."

    # hostname is an optional query arguments to filter instances by hostname.
    #
    # hostname: "..."

    # port is an optional port to scrape metrics from.
    # By default, port 80 is used.
    #
    # port: ...

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options


```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<FQDN>:<port>`, where FQDN is discovered instance address and `<port>` is the port from the `vultr_sd_configs` (default port is `80`).

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_vultr_instance_allowed_bandwidth_gb`: monthly bandwidth quota in GB.
* `__meta_vultr_instance_disk_gb`: the size of the disk in GB.
* `__meta_vultr_instance_features`: comma-separated list of features available to instance, such as "auto_backups", "ipv6", "ddos_protection".
* `__meta_vultr_instance_hostname`: hostname for this instance.
* `__meta_vultr_instance_id`: unique ID for the VPS Instance.
* `__meta_vultr_instance_internal_ip`: internal IP used by this instance, if set. Only relevant when a VPC is attached.
* `__meta_vultr_instance_label`: user-supplied label for this instance.
* `__meta_vultr_instance_main_ip`: main IPv4 address.
* `__meta_vultr_instance_main_ipv6`: main IPv6 network address.
* `__meta_vultr_instance_os`: [operating System name](https://www.vultr.com/api/#operation/list-os).
* `__meta_vultr_instance_os_id`: [operating System id](https://www.vultr.com/api/#operation/list-os) used by this instance.
* `__meta_vultr_instance_plan`: unique ID for the Plan.
* `__meta_vultr_instance_ram_mb`: the amount of RAM in MB.
* `__meta_vultr_instance_region`: [region id](https://www.vultr.com/api/#operation/list-regions) where the Instance is located.
* `__meta_vultr_instance_server_status`: server health status, which could be `none`, `locked`, `installingbooting`, `ok`.
* `__meta_vultr_instance_tags`: comma-separated list of tags applied to the instance.
* `__meta_vultr_instance_vcpu_count`: the number of vCPUs.

The list of discovered Vultr targets is refreshed at the interval, which can be configured via `-promscrape.vultrSDCheckInterval` command-line flag, default: 30s.


## yandexcloud_sd_configs

[Yandex Cloud](https://cloud.yandex.com/en/) SD configurations allow retrieving scrape targets from accessible folders.

Configuration example:

```yaml
scrape_configs:
- job_name: yandexcloud
  yandexcloud_sd_configs:

    # service is a mandatory option for yandexcloud service discovery
    # currently only "compute" service is supported
    #
  - service: compute

    # api_endpoint is an optional API endpoint for service discovery
    # The https://api.cloud.yandex.net endpoint is used by default.
    #
    # api_endpoint: "https://api.cloud.yandex.net"

    # folder_ids is an optional list of folder IDs for direct discovery.
    # If set, only the given folders are queried and the folder enumeration
    # step is skipped.
    #
    # folder_ids:
    #   - "b1gxxxxxxxxxxxxxxxxx"

    # yandex_passport_oauth_token is an optional OAuth token
    # for querying yandexcloud API. See https://cloud.yandex.com/en-ru/docs/iam/concepts/authorization/oauth-token
    #
    # yandex_passport_oauth_token: "..."

    # tls_config is an optional tls config.
    # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config
    #
    # tls_config:
    #   ...
```

Yandex Cloud SD support both user [OAuth token](https://cloud.yandex.com/en-ru/docs/iam/concepts/authorization/oauth-token)
and [instance service account](https://cloud.yandex.com/en-ru/docs/compute/operations/vm-connect/auth-inside-vm) if `yandex_passport_oauth_token` is omitted:

```yaml
scrape_configs:
- job_name: YC_with_oauth
  yandexcloud_sd_configs:
  - service: compute
    yandex_passport_oauth_token: "AQAAAAAsfasah<...>7E10SaotuL0"
  relabel_configs:
  - source_labels: [__meta_yandexcloud_instance_public_ip_0]
    target_label: __address__
    replacement: "$1:9100"

- job_name: YC_with_Instance_service_account
  yandexcloud_sd_configs:
  - service: compute
  relabel_configs:
  - source_labels: [__meta_yandexcloud_instance_private_ip_0]
    target_label: __address__
    replacement: "$1:9100"
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to the FQDN of the discovered instance.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_yandexcloud_instance_name`: the name of instance
* `__meta_yandexcloud_instance_id`: the id of instance
* `__meta_yandexcloud_instance_fqdn`: generated FQDN for instance
* `__meta_yandexcloud_instance_status`: the status of instance
* `__meta_yandexcloud_instance_platform_id`: instance platform ID (i.e. "standard-v3")
* `__meta_yandexcloud_instance_resources_cores`: instance vCPU cores
* `__meta_yandexcloud_instance_resources_core_fraction`: instance core fraction
* `__meta_yandexcloud_instance_resources_memory`: instance memory
* `__meta_yandexcloud_folder_id`: instance folder ID
* `__meta_yandexcloud_instance_label_<label name>`: each label from instance
* `__meta_yandexcloud_instance_private_ip_<interface index>`: private IP of <interface index> network interface
* `__meta_yandexcloud_instance_public_ip_<interface index>`: public (NAT) IP of <interface index> network interface
* `__meta_yandexcloud_instance_private_dns_<record number>`: if configured DNS records for private IP
* `__meta_yandexcloud_instance_public_dns_<record number>`: if configured DNS records for public IP

The list of discovered Yandex Cloud targets is refreshed at the interval, which can be configured via `-promscrape.yandexcloudSDCheckInterval` command-line flag.


## scrape_configs

The `scrape_configs` section at file pointed by `-promscrape.config` command-line flag can contain [supported service discovery options](#supported-service-discovery-configs).
Additionally, it can contain the following options:

```yaml
scrape_configs:
  # job_name must contain value for `job` label, which is added
  # to all the metrics collected from the configured and discovered scrape targets.
  # See https://prometheus.io/docs/concepts/jobs_instances/ .
  #
- job_name: "..."

  # scrape_interval is an optional interval to scrape targets.
  # By default, the scrape_interval specified in `global` section is used.
  # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file
  # If `global` section doesn't contain the `scrape_interval` option,
  # then one minute interval is used.
  # Example values:
  # - "30s" - 30 seconds
  # - "2m" - 2 minutes
  # The scrape_interval can be set on a per-target basis by specifying `__scrape_interval__`
  # label during target relabeling phase.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # scrape_interval: <duration>

  # scrape_timeout is an optional timeout when scraping the targets.
  # By default, the scrape_timeout specified in `global` section is used.
  # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file
  # If `global` section doesn't contain the `scrape_timeout` option,
  # then 10 seconds interval is used.
  # Example values:
  # - "30s" - 30 seconds
  # - "2m" - 2 minutes
  # The `scrape_timeout` cannot exceed the `scrape_interval`.
  # The scrape_timeout can be set on a per-target basis by specifying `__scrape_timeout__`
  # label during target relabeling phase.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # scrape_timeout: <duration>

  # max_scrape_size is an optional parameter for limiting the response size in bytes from scraped targets.
  # If max_scrape_size isn't set, then the limit from -promscrape.maxScrapeSize command-line flag is used instead.
  # Example values:
  # - "10MiB" - 10 * 1024 * 1024 bytes
  # - "100MB" - 100 * 1000 * 1000 bytes
  # The max_scrape_size can be set on a per-target basis by specifying `__max_scrape_size__`
  # label during target relabeling phase.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # max_scrape_size: <size>

  # metrics_path is the path to fetch metrics from targets.
  # By default, metrics are fetched from "/metrics" path.
  #
  # metrics_path: "..."

  # honor_labels controls how to handle conflicts between labels that are
  # already present in scraped data and labels that would be attached
  # server-side "job" and "instance" labels, manually configured target
  # labels, labels generated by service discovery, etc.
  #
  # If honor_labels is set to "true", label conflicts are resolved by keeping label
  # values from the scraped data and ignoring the conflicting server-side labels.
  #
  # If honor_labels is set to "false", label conflicts are resolved by renaming
  # conflicting labels in the scraped data to "exported_<original-label>" (for
  # example "exported_instance", "exported_job") and then attaching server-side
  # labels.
  #
  # Setting honor_labels to "true" is useful for use cases such as federation and
  # scraping the Pushgateway, where all labels specified in the target should be
  # preserved.
  #
  # By default, honor_labels is set to false for security and consistency reasons.
  #
  # honor_labels: <boolean>

  # honor_timestamps controls whether to respect the timestamps present in scraped data.
  #
  # If honor_timestamps is set to "true", the timestamps of the metrics exposed
  # by the target will be used.
  #
  # If honor_timestamps is set to "false", the timestamps of the metrics exposed
  # by the target will be ignored.
  #
  # By default, honor_timestamps is set to false.
  # See https://github.com/VictoriaMetrics/VictoriaMetrics/issues/4697#issuecomment-1656540535 for details.
  #
  # honor_timestamps: <boolean>

  # scheme configures the protocol scheme used for requests.
  # Supported values: http and https.
  # By default, http is used.
  #
  # scheme: "..."

  # Optional query arg parameters to add to scrape url.
  #
  # params:
  #   "param_name1": ["value1", ..., "valueN"]
  #   ...
  #   "param_nameM": ["valueM1", ..., "valueMN"]

  # relabel_configs is an optional relabeling configurations
  # for the specified and discovered scrape targets.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # relabel_configs:
  # - <relabel_config> ...

  # metric_relabel_configs is an optional relabeling configs
  # for the collected metrics from active scrape targets.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # metric_relabel_configs:
  # - <relabel_config> ...

  # sample_limit is an optional per-scrape limit on number
  # of scraped samples that will be accepted.
  # If more than this number of samples are present after metric relabeling
  # the entire scrape will be treated as failed.
  # By default, the limit is disabled.
  # The `global` sample_limit sets a default limit for all scrape targets. Available starting from v1.133.0.
  # The sample_limit can be set on a per-target basis by specifying `__sample_limit__`
  # label during target relabeling phase. Available starting from v1.103.0.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # sample_limit: <int>

  # disable_compression allows disabling HTTP compression for responses received from scrape targets.
  # By default, scrape targets are queried with `Accept-Encoding: gzip` http request header,
  # so targets could send compressed responses in order to save network bandwidth.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#scrape_config-enhancements
  #
  # disable_compression: <boolean>

  # disable_keepalive allows disabling HTTP keep-alive when scraping targets.
  # By default, HTTP keep-alive is enabled, so TCP connections to scrape targets
  # could be reused.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#scrape_config-enhancements
  #
  # disable_keepalive: <boolean>

  # stream_parse allows enabling stream parsing mode when scraping targets.
  # By default, stream parsing mode is disabled for targets which return up to a few thousands samples.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#stream-parsing-mode .
  # The stream_parse can be set on a per-target basis by specifying `__stream_parse__`
  # label during target relabeling phase.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # stream_parse: <boolean>

  # scrape_align_interval allows aligning scrapes to the given interval.
  # Example values:
  # - "5m" - align scrapes to every 5 minutes.
  # - "1h" - align scrapes to every hour.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#scrape_config-enhancements
  #
  # scrape_align_interval: <duration>

  # scrape_offset allows specifying the exact offset for scrapes.
  # Example values:
  # - "5m" - align scrapes to every 5 minutes.
  # - "1h" - align scrapes to every hour.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#scrape_config-enhancements
  #
  # scrape_offset: <duration>

  # series_limit is an optional limit on the number of unique time series
  # a single target can expose during all the scrapes on the time window of 24h.
  # By default, there is no limit on the number of exposed series.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#cardinality-limiter .
  # The series_limit can be set on a per-target basis by specifying `__series_limit__`
  # label during target relabeling phase.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # series_limit: <int>

  # label_limit is an optional limit on the number of labels per each sample
  # exposed by a target. It can be set globally for a whole scrape configuration and for each scrape job
  #
  # By default, the limit is disabled.
  # The label_limit can be set on a per-target basis by specifying `__label_limit__`
  # label during target relabeling phase. Available starting from v1.121.0.
  # See https://docs.victoriametrics.com/victoriametrics/relabeling/
  #
  # label_limit: <int>

  # no_stale_markers allows disabling staleness tracking.
  # By default, staleness tracking is enabled for all the discovered scrape targets.
  # See https://docs.victoriametrics.com/victoriametrics/vmagent/#prometheus-staleness-markers
  #
  # no_stale_markers: <boolean>

  # Additional HTTP client options for target scraping can be specified here.
  # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```
