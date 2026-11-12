<!-- Part 1 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## azure_sd_configs

Azure SD configuration discovers scrape targets from [Microsoft Azure](https://azure.microsoft.com/en-us/) VMs.

Configuration example:

```yaml
scrape_configs:
- job_name: azure
  azure_sd_configs:

    # subscription_id is a mandatory subscription ID.
    #
  - subscription_id: "..."

    # environment is an optional Azure environment. By default "AzurePublicCloud" is used.
    #
    # environment: "..."

    # authentication_method is an optional authentication method, either OAuth, ManagedIdentity or WorkloadIdentity.
    # See https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview
    # By default OAuth is used.
    #
    # authentication_method: "..."

    # tenant_id is an optional tenant ID. Only required with authentication_method OAuth.
    #
    # tenant_id: "..."

    # client_id is an optional client ID. Only required with authentication_method OAuth.
    #
    # client_id: "..."

    # client_secret is an optional client secret. Only required with authentication_method OAuth.
    #
    # client_secret: "..."

    # resource_group is an optional resource group name. Limits discovery to this resource group.
    #
    # resource_group: "..."

    # port is an optional port to scrape metrics from.
    # Port 80 is used by default.
    #
    # port: ...

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

`authentication_method: WorkloadIdentity` {{% available_from "v1.156.0" %}} exchanges a Kubernetes service account token
for an Azure access token, so no client secret is needed. The tenant ID, client ID and token file path are read from
`AZURE_TENANT_ID`, `AZURE_CLIENT_ID` and `AZURE_FEDERATED_TOKEN_FILE` env vars. The token file is read before every token refresh.
[Azure Workload Identity](https://azure.github.io/azure-workload-identity/docs/) sets these env vars in the pod.

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<private_ip>:<port>`, where `<private_ip>` is the machine's private IP and the `<port>` is the `port`
option specified in the `azure_sd_configs`.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_azure_machine_id`: the machine ID
* `__meta_azure_machine_location`: the location the machine runs in
* `__meta_azure_machine_name`: the machine name
* `__meta_azure_machine_computer_name`: the machine computer name
* `__meta_azure_machine_os_type`: the machine operating system
* `__meta_azure_machine_private_ip`: the machine's private IP
* `__meta_azure_machine_public_ip`: the machine's public IP if it exists
* `__meta_azure_machine_resource_group`: the machine's resource group
* `__meta_azure_machine_scale_set`: the name of the scale set which the vm is part of (this value is only set if you are using a scale set)
* `__meta_azure_machine_size`: the machine size
* `__meta_azure_machine_tag_<tagname>`: each tag value of the machine
* `__meta_azure_subscription_id`: the subscription ID
* `__meta_azure_tenant_id`: the tenant ID

The list of discovered Azure targets is refreshed at the interval, which can be configured via `-promscrape.azureSDCheckInterval` command-line flag.


## consul_sd_configs

Consul SD configuration allows retrieving scrape targets from [Consul's Catalog API](https://www.consul.io/api-docs/catalog).

Configuration example:

```yaml
scrape_configs:
- job_name: consul
  consul_sd_configs:

    # server is an optional Consul server to connect to. By default, localhost:8500 is used
    #
  - server: "localhost:8500"

    # token is an optional Consul API token.
    # If the token isn't specified, then it is read from a file pointed by CONSUL_HTTP_TOKEN_FILE
    # environment var or from the CONSUL_HTTP_TOKEN environment var.
    #
    # token: "..."

    # datacenter is an optional Consul API datacenter.
    # If the datacenter isn't specified, then it is read from Consul server.
    # See https://www.consul.io/api-docs/agent#read-configuration
    #
    # datacenter: "..."

    # namespace is an optional Consul namespace.
    # See https://developer.hashicorp.com/consul/docs/enterprise/namespaces
    # If the namespace isn't specified, then it is read from CONSUL_NAMESPACE environment var.
    #
    # namespace: "..."

    # partition is an optional Consul partition.
    # See https://developer.hashicorp.com/consul/docs/enterprise/admin-partitions
    # If partition isn't specified, then the default partition is used.
    #
    # partition: "..."

    # scheme is an optional scheme (http or https) to use for connecting to Consul server.
    # By default, http scheme is used.
    #
    # scheme: "..."

    # services is an optional list of services for which targets are retrieved.
    # If omitted, all services are scraped.
    # See https://www.consul.io/api-docs/catalog#list-nodes-for-service .
    #
    # services: ["...", "..."]

    # tags is an optional list of tags used to filter nodes for a given service.
    # Services must contain all tags in the list.
    # Deprecated: use filter instead with ServiceTags selector.
    #
    # tags: ["...", "..."]

    # node_meta is an optional node metadata key/value pairs to filter nodes for a given service.
    # Deprecated: use filter instead with NodeMeta selector.
    #
    # node_meta:
    #   "...": "..."

    # tag_separator is an optional string by which Consul tags are joined into the __meta_consul_tags label.
    # By default, "," is used as a tag separator.
    # Individual tags are also available via __meta_consul_tag_<tagname> labels - see below.
    #
    # tag_separator: "..."

    # filter is an optional filter for service discovery.
    # Replaces tags and node_meta options.
    # Consul supports it since 1.14 version.
    # See the list of supported filters at https://developer.hashicorp.com/consul/api-docs/catalog#filtering-1
    # See filter examples at https://developer.hashicorp.com/consul/api-docs/features/filtering
    #
    # filter: "..."

    # allow_stale is an optional config, which allows stale Consul results.
    # See https://developer.hashicorp.com/consul/api-docs/features/consistency
    # Reduce load on Consul if set to true. By default, it is set to true.
    #
    # allow_stale: ...

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<service_or_node_addr>:<service_port>`, where `<service_or_node_addr>` is the service address. If the service address is empty,
then the node address is used instead. The `<service_port>` is the service port.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_consul_address`: the address of the target
* `__meta_consul_dc`: the datacenter name for the target
* `__meta_consul_health`: the health status of the service
* `__meta_consul_metadata_<key>`: each node metadata key value of the target
* `__meta_consul_namespace`: namespace of the service - see [namespace docs](https://developer.hashicorp.com/consul/docs/enterprise/namespaces)
* `__meta_consul_node`: the node name defined for the target
* `__meta_consul_partition`: partition of the service - see [partition docs](https://developer.hashicorp.com/consul/docs/enterprise/admin-partitions)
* `__meta_consul_service_address`: the service address of the target
* `__meta_consul_service_id`: the service ID of the target
* `__meta_consul_service_metadata_<key>`: each service metadata key value of the target
* `__meta_consul_service_port`: the service port of the target
* `__meta_consul_service`: the name of the service the target belongs to
* `__meta_consul_tagged_address_<key>`: each node tagged address key value of the target
* `__meta_consul_tag_<tagname>`: the value for the given <tagname> tag of the target
* `__meta_consul_tagpresent_<tagname>`: "true" for every <tagname> tag of the target
* `__meta_consul_tags`: the list of tags of the target joined by the `tag_separator`

The list of discovered Consul targets is refreshed at the interval, which can be configured via `-promscrape.consulSDCheckInterval` command-line flag.

If you have performance issues with `consul_sd_configs` on a large cluster, then consider using [consulagent_sd_configs](#consulagent_sd_configs) instead.


## consulagent_sd_configs

Consul Agent SD configuration allows retrieving scrape targets from [Consul Agent API](https://developer.hashicorp.com/consul/api-docs/agent/service).
When using the Agent API, only services registered in the locally running Consul Agent are discovered.
It is suitable for huge clusters for which using the [Catalog API](https://developer.hashicorp.com/consul/api-docs/catalog#list-services) would be too slow or resource intensive,
in other cases it is recommended to use [consul_sd_configs](#consul_sd_configs).

Configuration example:

```yaml
scrape_configs:
- job_name: consulagent
  consulagent_sd_configs:

    # server is an optional Consul Agent to connect to. By default, localhost:8500 is used
    #
  - server: "localhost:8500"

    # token is an optional Consul API token.
    # If the token isn't specified, then it is read from a file pointed by CONSUL_HTTP_TOKEN_FILE
    # environment var or from the CONSUL_HTTP_TOKEN environment var.
    #
    # token: "..."

    # datacenter is an optional Consul API datacenter.
    # If the datacenter isn't specified, then it is read from Consul server.
    # See https://www.consul.io/api-docs/agent#read-configuration
    #
    # datacenter: "..."

    # namespace is an optional Consul namespace.
    # See https://developer.hashicorp.com/consul/docs/enterprise/namespaces
    # If the namespace isn't specified, then it is read from CONSUL_NAMESPACE environment var.
    #
    # namespace: "..."

    # scheme is an optional scheme (http or https) to use for connecting to Consul server.
    # By default, http scheme is used.
    #
    # scheme: "..."

    # services is an optional list of services for which targets are retrieved.
    # If omitted, all services are scraped.
    # See https://www.consul.io/api-docs/catalog#list-nodes-for-service .
    #
    # services: ["...", "..."]

    # tag_separator is an optional string by which Consul tags are joined into the __meta_consul_tags label.
    # By default, "," is used as a tag separator.
    # Individual tags are also available via __meta_consul_tag_<tagname> labels - see below.
    #
    # tag_separator: "..."

    # filter is optional filter for service nodes discovery request.
    # Replaces tags and node_metadata options.
    # consul supports it since 1.14 version
    # list of supported filters https://developer.hashicorp.com/consul/api-docs/catalog#filtering-1
    # syntax examples https://developer.hashicorp.com/consul/api-docs/features/filtering
    #
    # filter: "..."

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<service_or_node_addr>:<service_port>`, where `<service_or_node_addr>` is the service address. If the service address is empty,
then the node address is used instead. The `<service_port>` is the service port.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_consulagent_address`: the address of the target
* `__meta_consulagent_dc`: the datacenter name for the target
* `__meta_consulagent_health`: the health status of the service
* `__meta_consulagent_metadata_<key>`: each node metadata key value of the target
* `__meta_consulagent_namespace`: namespace of the service - see [namespace docs](https://developer.hashicorp.com/consul/docs/enterprise/namespaces)
* `__meta_consulagent_node`: the node name defined for the target
* `__meta_consulagent_service_address`: the service address of the target
* `__meta_consulagent_service_id`: the service ID of the target
* `__meta_consulagent_service_metadata_<key>`: each service metadata key value of the target
* `__meta_consulagent_service_port`: the service port of the target
* `__meta_consulagent_service`: the name of the service the target belongs to
* `__meta_consulagent_tagged_address_<key>`: each node tagged address key value of the target
* `__meta_consulagent_tag_<tagname>`: the value for the given <tagname> tag of the target
* `__meta_consulagent_tagpresent_<tagname>`: "true" for every <tagname> tag of the target
* `__meta_consulagent_tags`: the list of tags of the target joined by the `tag_separator`

The list of discovered Consul Agent targets is refreshed at the interval, which can be configured via `-promscrape.consulagentSDCheckInterval` command-line flag.


## digitalocean_sd_configs

DigitalOcean SD configuration allows retrieving scrape targets from [DigitalOcean's Droplets API](https://docs.digitalocean.com/reference/api/reference/droplets/).

Configuration example:

```yaml
scrape_configs:
- job_name: digitalocean
  digitalocean_sd_configs:

    # server is an optional DigitalOcean API server to query.
    # By default, https://api.digitalocean.com is used.
    #
  - server: "https://api.digitalocean.com"

    # port is an optional port to scrape metrics from. By default, port 80 is used.
    #
    # port: ...

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<public_ip>:<port>`, where `<public_ip>` is a public ipv4 address of the droplet, while `<port>` is the port specified in the `digitalocean_sd_configs`.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_digitalocean_droplet_id`: the id of the droplet
* `__meta_digitalocean_droplet_name`: the name of the droplet
* `__meta_digitalocean_image`: the slug of the droplet's image
* `__meta_digitalocean_image_name`: the display name of the droplet's image
* `__meta_digitalocean_private_ipv4`: the private IPv4 of the droplet
* `__meta_digitalocean_public_ipv4`: the public IPv4 of the droplet
* `__meta_digitalocean_public_ipv6`: the public IPv6 of the droplet
* `__meta_digitalocean_region`: the region of the droplet
* `__meta_digitalocean_size`: the size of the droplet
* `__meta_digitalocean_status`: the status of the droplet
* `__meta_digitalocean_features`: the comma-separated list of features of the droplet
* `__meta_digitalocean_tags`: the comma-separated list of tags of the droplet
* `__meta_digitalocean_vpc`: the id of the droplet's VPC

The list of discovered DigitalOcean targets is refreshed at the interval, which can be configured via `-promscrape.digitaloceanSDCheckInterval` command-line flag.


## dns_sd_configs

DNS-based service discovery allows retrieving scrape targets from the specified DNS domain names.
These specified names are periodically queried to discover a list of targets with the interval
configured via `-promscrape.dnsSDCheckInterval` command-line flag.

Configuration example:

```yaml
scrape_configs:
- job_name: dns
  dns_sd_configs:

    # names must contain a list of DNS names to query.
    #
  - names: ["...", "..."]

    # type is an optional type of DNS query to perform.
    # Supported values are: SRV, A, AAAA or MX.
    # By default, SRV is used.
    #
    # type: ...

    # port is a port number to use if the query type is not SRV.
    #
    # port: ...
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to the `<addr>:<port>`, where `<addr>` is the discovered DNS address, while `<port>` is either the discovered port for SRV records or the port
specified in the `dns_sd_config`.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_dns_name`: the record name that produced the discovered target.
* `__meta_dns_srv_record_target`: the target field of the SRV record
* `__meta_dns_srv_record_port`: the port field of the SRV record
* `__meta_dns_mx_record_target`: the target field of the MX record.

The list of discovered DNS targets is refreshed at the interval, which can be configured via `-promscrape.dnsSDCheckInterval` command-line flag.
