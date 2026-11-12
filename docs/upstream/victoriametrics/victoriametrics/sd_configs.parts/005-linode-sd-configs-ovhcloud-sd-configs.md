<!-- Part 5 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## linode_sd_configs

Linode SD configuration {{% available_from "v1.150.0" %}} allows retrieving scrape targets from [Linode](https://www.linode.com/) instances.
The following [Linode API](https://www.linode.com/docs/api/) token scopes are required: `linodes:read_only` and `ips:read_only`.

Configuration example:

```yaml
scrape_configs:
- job_name: linode
  linode_sd_configs:

    # server is an optional Linode API server to query.
    # By default, https://api.linode.com is used.
    #
    # server: "https://api.linode.com"

    # port is an optional port to scrape metrics from. By default, port 80 is used.
    #
    # port: ...

    # tag_separator is an optional string used to join multi-value labels such as tags and extra IPs.
    # By default, "," is used.
    #
    # tag_separator: ","

    # region is an optional Linode region to filter instances by.
    # By default, instances from all regions are returned.
    #
    # region: "..."

    # Required credentials for Linode API authentication.
    #
    authorization:
      credentials: "..."
      # type: "..."  # default: Bearer
      # credentials_file: "..."  # is mutually-exclusive with credentials

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<ip>:<port>`, where `<ip>` is the public IPv4 of the Linode instance when available, otherwise the private IPv4, and `<port>` is the port specified in the `linode_sd_configs`.
Instances without a usable IPv4 address are skipped.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_linode_instance_id`: the id of the linode instance
* `__meta_linode_instance_label`: the label of the linode instance
* `__meta_linode_image`: the slug of the linode instance's image
* `__meta_linode_private_ipv4`: the private IPv4 of the linode instance
* `__meta_linode_public_ipv4`: the public IPv4 of the linode instance
* `__meta_linode_public_ipv6`: the public IPv6 of the linode instance
* `__meta_linode_private_ipv4_rdns`: the reverse DNS for the first private IPv4 of the linode instance
* `__meta_linode_public_ipv4_rdns`: the reverse DNS for the first public IPv4 of the linode instance
* `__meta_linode_public_ipv6_rdns`: the reverse DNS for the first public IPv6 of the linode instance
* `__meta_linode_region`: the region of the linode instance
* `__meta_linode_type`: the type of the linode instance
* `__meta_linode_status`: the status of the linode instance
* `__meta_linode_tags`: a list of tags of the linode instance joined by the tag separator
* `__meta_linode_group`: the display group a linode instance is a member of
* `__meta_linode_gpus`: the number of GPUs of the linode instance
* `__meta_linode_hypervisor`: the virtualization software powering the linode instance
* `__meta_linode_backups`: the backup service status of the linode instance
* `__meta_linode_specs_disk_bytes`: the amount of storage space the linode instance has access to
* `__meta_linode_specs_memory_bytes`: the amount of RAM the linode instance has access to
* `__meta_linode_specs_vcpus`: the number of VCPUs this linode has access to
* `__meta_linode_specs_transfer_bytes`: the amount of network transfer the linode instance is allotted each month
* `__meta_linode_extra_ips`: a list of all extra IPv4 addresses assigned to the linode instance joined by the tag separator
* `__meta_linode_ipv6_ranges`: a list of IPv6 ranges with mask assigned to the linode instance joined by the tag separator

The list of discovered Linode targets is refreshed at the interval, which can be configured via `-promscrape.linodeSDCheckInterval` command-line flag.
Discovery failures are tracked in the `vm_promscrape_discovery_linode_failures_total` metric.


## marathon_sd_configs

Marathon SD configuration {{% available_from "v1.109.0" %}} allows retrieving scrape targets from [Marathon](https://github.com/d2iq-archive/marathon) REST API.

Configuration example:

```yaml
scrape_configs:
- job_name: marathon
  marathon_sd_configs:
    # List of URLs to be used to contact Marathon servers.
    # You need to provide at least one server URL, but should provide URLs for
    # all masters you have running.
    #
    servers:
      - "host1:port1"
      - "host2:port2"
      - "..."

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_marathon_app`: the name of the app (with slashes replaced by dashes)
* `__meta_marathon_image`: the name of the Docker image used (if available)
* `__meta_marathon_task`: the ID of the Mesos task
* `__meta_marathon_app_label_<labelname>`: any Marathon labels attached to the app
* `__meta_marathon_port_definition_label_<labelname>`: the port definition labels
* `__meta_marathon_port_mapping_label_<labelname>`: the port mapping labels
* `__meta_marathon_port_index`: the port index number (e.g. `1` for `PORT1`)

The list of discovered Marathon targets is refreshed at the interval, which can be configured via `-promscrape.marathonSDCheckInterval` command-line flag.


## nomad_sd_configs

Nomad SD configuration allows retrieving scrape targets from [HashiCorp Nomad Services](https://www.hashicorp.com/en/blog/nomad-service-discovery).

Configuration example:

```yaml
scrape_configs:
- job_name: nomad
  nomad_sd_configs:

    # server is an optional Nomad server to connect to.
    # If the server isn't specified, then it is read from NOMAD_ADDR environment var.
    # If the NOMAD_ADDR environment var isn't set, then localhost:4646 is used.
    #
  - server: "localhost:4646"

    # namespace is an optional Nomad namespace.
    # If the namespace isn't specified, then it is read from NOMAD_NAMESPACE environment var.
    #
    # namespace: "..."

    # region is an optional Nomad region.
    # If the region isn't specified, then it is read from NOMAD_REGION environment var.
    # If NOMAD_REGION environment var isn't set, then "global" region is used
    #
    # region: "..."

    # tag_separator is an optional string by which Nomad tags are joined into the __meta_nomad_tags label.
    # By default, "," is used as a tag separator.
    # Individual tags are also available via __meta_nomad_tag_<tagname> labels - see below.
    #
    # tag_separator: "..."

    # allow_stale is an optional config, which allows stale Nomad results.
    # See https://developer.hashicorp.com/consul/api-docs/features/consistency
    # Reduces load on Nomad if set to true. By default, it is set to true.
    #
    # allow_stale: ...

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<addr>:<port>`, where `<addr>` is the service address, while `<port>` is the service port.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_nomad_address`: the address of the target
* `__meta_nomad_dc`: the datacenter name for the target
* `__meta_nomad_namespace`: namespace of the service
* `__meta_nomad_node_id`: the node ID defined for the target
* `__meta_nomad_service`: the name of the service the target belongs to
* `__meta_nomad_service_address`: the service address of the target
* `__meta_nomad_service_alloc_id`: the AllocID of the target service
* `__meta_nomad_service_id`: the ID of the target service
* `__meta_nomad_service_job_id`: the JobID of the target service
* `__meta_nomad_service_port`: the service port of the target
* `__meta_nomad_tag_<tagname>`: the value for the given <tagname> tag of the target
* `__meta_nomad_tagpresent_<tagname>`: "true" for every <tagname> tag of the target
* `__meta_nomad_tags`: the list of tags of the target joined by the `tag_separator`

The list of discovered Nomad targets is refreshed at the interval, which can be configured via `-promscrape.nomadSDCheckInterval` command-line flag.


## openstack_sd_configs

OpenStack SD configuration allows retrieving scrape targets from [OpenStack Nova](https://docs.openstack.org/nova/latest/) instances.

[OpenStack identity API v3](https://docs.openstack.org/api-ref/identity/v3/) is supported only.

Configuration example:

```yaml
scrape_configs:
- job_name: openstack
  openstack_sd_configs:

    # role must contain either `hypervisor` or `instance`.
    # See docs below for details.
    #
  - role: "..."

    # region must contain OpenStack region for targets' discovery.
    #
    region: "..."

    # identity_endpoint is an optional HTTP Identity API endpoint.
    # By default, it is read from OS_AUTH_URL environment variable.
    #
    # identity_endpoint: "..."

    # username is an optional username to query Identity API.
    # By default, it is read from OS_USERNAME environment variable.
    #
    # username: "..."

    # userid is an optional userid to query Identity API.
    # By default, it is read from OS_USERID environment variable.
    #
    # userid: "..."

    # password is an optional password to query Identity API.
    # By default, it is read from OS_PASSWORD environment variable.
    #
    # password: "..."

    # At most one of domain_id and domain_name must be provided.
    # By default, they are read from OS_DOMAIN_NAME and OS_DOMAIN_ID environment variables.
    #
    # domain_name: "..."
    # domain_id: "..."

    # project_name and project_id are optional project name and project id.
    # By default, it is read from OS_PROJECT_NAME and OS_PROJECT_ID environment variables.
    # If these vars are empty, then the options are read
    # from OS_TENANT_NAME and OS_TENANT_ID environment variables.
    #
    # project_name: "..."
    # project_id: "..."

    # By default, these fields are read from OS_APPLICATION_CREDENTIAL_NAME
    # and OS_APPLICATION_CREDENTIAL_ID environment variables
    #
    # application_credential_name: "..."
    # application_credential_id: "..."

    # By default, this field is read from OS_APPLICATION_CREDENTIAL_SECRET
    #
    # application_credential_secret: "..."

    # all_tenants can be set to true if all instances in all projects must be discovered.
    # It is only relevant for the 'role: instance' and usually requires admin permissions.
    #
    # all_tenants: ...

    # port is an optional port to scrape metrics from.
    # Port 80 is used by default.
    #
    # port: ...

    # availability is the availability of the endpoint to connect to.
    # Must be one of public, admin or internal.
    # By default, it is set to public
    #
    # availability: "..."

    # tls_config is an optional tls config.
    # See https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config
    #
    # tls_config:
    #   ...
```

One of the following `role` types can be configured to discover OpenStack targets:

### OpenStack role: hypervisor

  The `role: hypervisor` discovers one target per Nova hypervisor node.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<host>:<port>`, where `<host>` is the discovered node IP, while `<port>` is the port specified in the `openstack_sd_configs`.

  The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_openstack_hypervisor_host_ip`: the hypervisor node's IP address.
* `__meta_openstack_hypervisor_hostname`: the hypervisor node's name.
* `__meta_openstack_hypervisor_id`: the hypervisor node's ID.
* `__meta_openstack_hypervisor_state`: the hypervisor node's state.
* `__meta_openstack_hypervisor_status`: the hypervisor node's status.
* `__meta_openstack_hypervisor_type`: the hypervisor node's type.

### OpenStack role: instance

  The `role: instance` discovers one target per network interface of Nova instance.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<host>:<port>`, where `<host>` is the private IP address of the discovered instance, while `<port>` is the port specified in the `openstack_sd_configs`.

  The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_openstack_address_pool`: the pool of the private IP.
* `__meta_openstack_instance_flavor`: the flavor of the OpenStack instance.
* `__meta_openstack_instance_id`: the OpenStack instance ID.
* `__meta_openstack_instance_name`: the OpenStack instance name.
* `__meta_openstack_instance_status`: the status of the OpenStack instance.
* `__meta_openstack_private_ip`: the private IP of the OpenStack instance.
* `__meta_openstack_project_id`: the project (tenant) owning this instance.
* `__meta_openstack_public_ip`: the public IP of the OpenStack instance.
* `__meta_openstack_tag_<tagkey>`: each tag value of the instance.
* `__meta_openstack_user_id`: the user account owning the tenant.

The list of discovered OpenStack targets is refreshed at the interval, which can be configured via `-promscrape.openstackSDCheckInterval` command-line flag.


## ovhcloud_sd_configs

OVH Cloud SD configuration{{% available_from "v1.104.0" %}} allows retrieving scrape targets from [OVH Cloud VPS](https://www.ovhcloud.com/en/vps/)
and [OVH Cloud dedicated server](https://ovhcloud.com/en/bare-metal/).

Configuration example:

```yaml
scrape_configs:
- job_name: ovh_job
  ovhcloud_sd_configs:

  # (optional) depending on the API you want to use, you may set the endpoint to:
  # `ovh-eu` for OVH Europe API (default).
  # `ovh-us` for OVH US API.
  # `ovh-ca` for OVH North-America API.
  # `soyoustart-eu` for "So you Start Europe API".
  # `soyoustart-ca` for "So you Start North America API".
  # `kimsufi-eu` for Kimsufi Europe API.
  # `kimsufi-ca` for Kimsufi North America API.
  # See: https://github.com/ovh/go-ovh?tab=readme-ov-file#supported-apis
  - endpoint: "..."

    # (mandatory) application_key is a self generated tokens.
    # create one by visiting: https://eu.api.ovh.com/createApp/
    application_key: "..."

    # (mandatory) application_secret holds the application secret key.
    application_secret: "..."

    # (mandatory) consumer_key holds the user/app specific token. It must have been validated before use.
    consumer_key: "..."

    # (mandatory) service could be either `vps` or `dedicated_server`.
    service: "..."

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set to either `<ipv4>` address or `<ipv6>` address.

In addition, the `instance` label for the VPS/dedicated server will be set to the VPS/dedicated server name as retrieved from OVH Cloud API.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/).

VPS:

* `__meta_ovhcloud_vps_cluster`: the cluster of the server.
* `__meta_ovhcloud_vps_datacenter`: the datacenter of the server.
* `__meta_ovhcloud_vps_disk`: the disk of the server.
* `__meta_ovhcloud_vps_display_name`: the display name of the server.
* `__meta_ovhcloud_vps_ipv4`: the IPv4 of the server.
* `__meta_ovhcloud_vps_ipv6`: the IPv6 of the server.
* `__meta_ovhcloud_vps_keymap`: the KVM keyboard layout of the server.
* `__meta_ovhcloud_vps_maximum_additional_ip`: the maximum additional IPs of the server.
* `__meta_ovhcloud_vps_memory_limit`: the memory limit of the server.
* `__meta_ovhcloud_vps_memory`: the memory of the server.
* `__meta_ovhcloud_vps_monitoring_ip_blocks`: the monitoring IP blocks of the server.
* `__meta_ovhcloud_vps_name`: the name of the server.
* `__meta_ovhcloud_vps_netboot_mode`: the netboot mode of the server.
* `__meta_ovhcloud_vps_offer_type`: the offer type of the server.
* `__meta_ovhcloud_vps_offer`: the offer of the server.
* `__meta_ovhcloud_vps_state`: the state of the server.
* `__meta_ovhcloud_vps_vcore`: the number of virtual cores of the server.
* `__meta_ovhcloud_vps_version`: the version of the server.
* `__meta_ovhcloud_vps_zone`: the zone of the server.

Dedicated servers:

* `__meta_ovhcloud_dedicated_server_commercial_range`: the commercial range of the server.
* `__meta_ovhcloud_dedicated_server_datacenter`: the datacenter of the server.
* `__meta_ovhcloud_dedicated_server_ipv4`: the IPv4 of the server.
* `__meta_ovhcloud_dedicated_server_ipv6`: the IPv6 of the server.
* `__meta_ovhcloud_dedicated_server_link_speed`: the link speed of the server.
* `__meta_ovhcloud_dedicated_server_name`: the name of the server.
* `__meta_ovhcloud_dedicated_server_no_intervention`: the [intervention](https://support.us.ovhcloud.com/hc/en-us/articles/27991435200147-FAQ-Interventions-and-Hardware-Replacement) of the server.
* `__meta_ovhcloud_dedicated_server_os`: the operating system of the server.
* `__meta_ovhcloud_dedicated_server_rack`: the rack of the server.
* `__meta_ovhcloud_dedicated_server_reverse`: the reverse DNS name of the server.
* `__meta_ovhcloud_dedicated_server_server_id`: the ID of the server.
* `__meta_ovhcloud_dedicated_server_state`: the state of the server.
* `__meta_ovhcloud_dedicated_server_support_level`: the support level of the server.

The list of discovered OVH Cloud targets is refreshed at the interval, which can be configured via `-promscrape.ovhcloudSDCheckInterval` command-line flag.
