<!-- Part 3 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## gce_sd_configs

GCE SD configuration allows retrieving scrape targets from [GCP GCE instances](https://cloud.google.com/compute).

Configuration example:

```yaml
scrape_configs:
- job_name: gce
  gce_sd_configs:

    # project is an optional GCE project where targets must be discovered.
    # By default, the local project is used.
    #
  - project: "..."

    # zone is an optional zone where targets must be discovered.
    # By default, the local zone is used.
    # If zone equals to '*', then targets in all the zones for the given project are discovered.
    # The zone may contain a list of zones: zone["us-east1-a", "us-east1-b"]
    #
    # zone: "..."

    # filter is an optional filter for the instance list.
    # See https://cloud.google.com/compute/docs/reference/latest/instances/list
    #
    # filter: "..."

    # port is an optional port to scrape metrics from.
    # By default, port 80 is used.
    #
    # port: ...

    # tag_separator is an optional separator for tags in `__meta_gce_tags` label.
    # By default, "," is used.
    #
    # tag_separator: "..."
```

Credentials are discovered by looking in the following places, preferring the first location found:

1. a JSON file specified by the `GOOGLE_APPLICATION_CREDENTIALS` environment variable
1. a JSON file in the well-known path `$HOME/.config/gcloud/application_default_credentials.json`
1. fetched from the GCE metadata server

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<iface_ip>:<port>`, where `<iface_ip>` is private IP of the discovered instance, while `<port>` is the `port` value
specified in the `gce_sd_configs`.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_gce_instance_id`: the numeric id of the instance
* `__meta_gce_instance_name`: the name of the instance
* `__meta_gce_label_<labelname>`: each GCE label of the instance
* `__meta_gce_machine_type`: full or partial URL of the machine type of the instance
* `__meta_gce_metadata_<name>`: each metadata item of the instance
* `__meta_gce_network`: the network URL of the instance
* `__meta_gce_private_ip`: the private IP address of the instance
* `__meta_gce_interface_ipv4_<name>`: IPv4 address of each named interface
* `__meta_gce_internal_ipv6`: the internal IPv6 address of the instance, if present
* `__meta_gce_public_ipv6`: the public IPv6 address of the instance, if present
* `__meta_gce_project`: the GCP project in which the instance is running
* `__meta_gce_public_ip`: the public IP address of the instance, if present
* `__meta_gce_subnetwork`: the subnetwork URL of the instance
* `__meta_gce_tags`: list of instance tags separated by tag_separator
* `__meta_gce_zone`: the GCE zone URL in which the instance is running

The list of discovered GCE targets is refreshed at the interval, which can be configured via `-promscrape.gceSDCheckInterval` command-line flag.


## hetzner_sd_configs

Hetzner SD configuration allows retrieving scrape targets from [Hetzner Cloud](https://www.hetzner.com/cloud) and [Hetzner Robot](https://docs.hetzner.com/robot).

Configuration example:

```yaml
scrape_configs:
- job_name: hetzner
  hetzner_sd_configs:

    # The mandatory Hetzner role for entity discovery.
    # Must be either 'robot' or 'hcloud'.
    #
    role: "hcloud"

    # Required credentials for API server authentication for 'hcloud' role.
    #
    authorization:
      credentials: "..."
      # type: "..."  # default: Bearer
      # credentials_file: "..."  # is mutually-exclusive with credentials

    # Required credentials for API server authentication for 'robot' role.
    #
    # basic_auth:
    #  username: "..."
    #  username_file: "..."  # is mutually-exclusive with username
    #  password: "..."
    #  password_file: "..."  # is mutually-exclusive with password

    # port is an optional port to scrape metrics from.
    # By default, port 80 is used.
    #
    # port: ...

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<FQDN>:<port>`, where FQDN is discovered instance address and `<port>` is the port from the `hetzner_sd_configs` (default port is `80`).

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

Common labels for both `hcloud` and `robot` roles:

* `__meta_hetzner_datacenter`: the datacenter of the server. **Deprecated for the `robot` role** — use `__meta_hetzner_robot_datacenter` instead. **Deprecated for the `hcloud` role** — use `__meta_hetzner_hcloud_location` and `__meta_hetzner_hcloud_location_network_zone` instead; the upstream Hetzner Cloud API `datacenter` field is being removed after 2026-07-01 (see [Hetzner changelog](https://docs.hetzner.cloud/changelog#2025-12-16-phasing-out-datacenters))
* `__meta_hetzner_public_ipv4`: the public IPv4 address of the server
* `__meta_hetzner_public_ipv6_network`: the public IPv6 network (/64) of the server
* `__meta_hetzner_role`: the current role `hcloud` or `robot`
* `__meta_hetzner_server_id`: the ID of the server
* `__meta_hetzner_server_name`: the name of the server
* `__meta_hetzner_server_status`: the status of the server

Additional labels for `role: hcloud`:

* `__meta_hetzner_hcloud_location`: the location name of the server
* `__meta_hetzner_hcloud_location_network_zone`: the network zone of the server
* `__meta_hetzner_hcloud_datacenter_location`: **deprecated**, use `__meta_hetzner_hcloud_location` instead (still emitted for backward compatibility)
* `__meta_hetzner_hcloud_datacenter_location_network_zone`: **deprecated**, use `__meta_hetzner_hcloud_location_network_zone` instead (still emitted for backward compatibility)
* `__meta_hetzner_hcloud_cpu_cores`: the CPU cores count of the server
* `__meta_hetzner_hcloud_cpu_type`: the CPU type of the server (shared or dedicated)
* `__meta_hetzner_hcloud_disk_size_gb`: the disk size of the server (in GB)
* `__meta_hetzner_hcloud_image_description`: the description of the server image
* `__meta_hetzner_hcloud_image_name`: the image name of the server
* `__meta_hetzner_hcloud_image_os_flavor`: the OS flavor of the server image
* `__meta_hetzner_hcloud_image_os_version`: the OS version of the server image
* `__meta_hetzner_hcloud_label_<labelname>`: each label of the server
* `__meta_hetzner_hcloud_labelpresent_<labelname>`: true for each label of the server
* `__meta_hetzner_hcloud_memory_size_gb`: the amount of memory of the server (in GB)
* `__meta_hetzner_hcloud_private_ipv4_<networkname>`: the private IPv4 address of the server within a given network
* `__meta_hetzner_hcloud_server_type`: the type of the server

Additional labels for `role: robot`:

* `__meta_hetzner_robot_datacenter`: the datacenter name of the server
* `__meta_hetzner_robot_cancelled`: the server cancellation status
* `__meta_hetzner_robot_product`: the product of the server

The list of discovered Hetzner targets is refreshed at the interval, which can be configured via `-promscrape.hetznerSDCheckInterval` command-line flag.


## http_sd_configs

HTTP-based service discovery fetches targets from the specified `url`.

Configuration example:

```yaml
scrape_configs:
- job_name: http
  http_sd_configs:

    # url must contain the URL from which the targets are fetched.
    #
  - url: "http://..."

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

See [these examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/#http-based-target-discovery) on how to configure http-based target discovery.

The service at `url` must return JSON response in the following format:

```json
[
  {
    "targets": [ "<host>", ... ],
    "labels": {
      "<labelname>": "<labelvalue>",
      ...
    }
  },
  ...
]
```

The `url` is queried periodically with the interval specified in `-promscrape.httpSDCheckInterval` command-line flag.
Discovery errors are tracked in `promscrape_discovery_http_errors_total` metric.

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to one of the targets returned by the http service.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_url`: the URL from which the target was extracted

The list of discovered HTTP-based targets is refreshed at the interval, which can be configured via `-promscrape.httpSDCheckInterval` command-line flag.
