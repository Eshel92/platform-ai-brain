<!-- Part 2 of 7 of victoriametrics/sd_configs.md (split because the page is big). -->

## docker_sd_configs

Docker SD configuration allows retrieving scrape targets from [Docker Engine](https://docs.docker.com/engine/) hosts.

Configuration example:

```yaml
scrape_configs:
- job_name: docker
  docker_sd_configs:

    # host must contain the address of the Docker daemon.
    #
  - host: "..."

    # port is an optional port to scrape metrics from.
    # By default, port 80 is used.
    #
    # port: ...

    # host_networking_host is an optional host to use if the container is in host networking mode.
    # By default, localhost is used.
    #
    # host_networking_host: "..."

    # Sort all networks in ascending order based on network name and
    # get the first network if the container has multiple networks defined,
    # thus avoiding collecting duplicate targets.
    #
    # match_first_network: "<boolean>" | default true

    # filters is an optional filters to limit the discovery process to a subset of available resources.
    # See https://docs.docker.com/engine/api/v1.40/#operation/ContainerList
    #
    # filters:
    # - name: "..."
    #   values: ["...", "..."]

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<ip_address>:<port>`, where `<ip_address>` is the exposed ip address of the docker container, while the `<port>` is either the exposed port
of the docker container or the port specified in the `docker_sd_configs` if the docker container has no exposed ports.
If a container exposes multiple ip addresses, then multiple targets will be discovered - one per each exposed ip address.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_docker_container_id`: the id of the container
* `__meta_docker_container_name`: the name of the container
* `__meta_docker_container_network_mode`: the network mode of the container
* `__meta_docker_container_label_<labelname>`: each label of the container
* `__meta_docker_network_id`: the ID of the network
* `__meta_docker_network_name`: the name of the network
* `__meta_docker_network_ingress`: whether the network is ingress
* `__meta_docker_network_internal`: whether the network is internal
* `__meta_docker_network_label_<labelname>`: each label of the network
* `__meta_docker_network_scope`: the scope of the network
* `__meta_docker_network_ip`: the IP of the container in this network
* `__meta_docker_port_private`: the port on the container
* `__meta_docker_port_public`: the external port if a port-mapping exists
* `__meta_docker_port_public_ip`: the public IP if a port-mapping exists

The list of discovered Docker targets is refreshed at the interval, which can be configured via `-promscrape.dockerSDCheckInterval` command-line flag.


## dockerswarm_sd_configs

Docker Swarm SD configuration allows retrieving scrape targets from [Docker Swarm engine](https://docs.docker.com/engine/swarm/).

Configuration example:

```yaml
scrape_configs:
- job_name: dockerswarm
  dockerswarm_sd_configs:

    # host must contain the address of the Docker daemon.
    #
  - host: "..."

    # role must contain `services`, `tasks` or `nodes` as described below.
    #
    role: ...

    # port is an optional port to scrape metrics from, when `role` is nodes, and for discovered
    # tasks and services that don't have published ports.
    # By default, port 80 is used.
    #
    # port: ...

    # filters is an optional filters to limit the discovery process to a subset of available resources.
    # The available filters are listed in the upstream documentation:
    # Services: https://docs.docker.com/engine/api/v1.40/#operation/ServiceList
    # Tasks: https://docs.docker.com/engine/api/v1.40/#operation/TaskList
    # Nodes: https://docs.docker.com/engine/api/v1.40/#operation/NodeList
    #
    # filters:
    # - name: "..."
    #   values: ["...", "..."]

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

One of the following roles can be configured to discover targets:

### Dockerswarm role: services

  The `role: services` discovers all Swarm services.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<ip>:<port>`, where `<ip>` is the endpoint's virtual IP, while the `<port>` is the published port of the service.
  If the service has multiple published ports, then multiple targets are generated - one per each port.
  If the service has no published ports, then the `<port>` is set to the `port` value obtained from `dockerswarm_sd_configs`.

  Available meta labels for `role: services` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_dockerswarm_service_id`: the id of the service
* `__meta_dockerswarm_service_name`: the name of the service
* `__meta_dockerswarm_service_mode`: the mode of the service
* `__meta_dockerswarm_service_endpoint_port_name`: the name of the endpoint port, if available
* `__meta_dockerswarm_service_endpoint_port_publish_mode`: the publishing mode of the endpoint port
* `__meta_dockerswarm_service_label_<labelname>`: each label of the service
* `__meta_dockerswarm_service_task_container_hostname`: the container hostname of the target, if available
* `__meta_dockerswarm_service_task_container_image`: the container image of the target
* `__meta_dockerswarm_service_updating_status`: the status of the service, if available
* `__meta_dockerswarm_network_id`: the ID of the network
* `__meta_dockerswarm_network_name`: the name of the network
* `__meta_dockerswarm_network_ingress`: whether the network is ingress
* `__meta_dockerswarm_network_internal`: whether the network is internal
* `__meta_dockerswarm_network_label_<labelname>`: each label of the network
* `__meta_dockerswarm_network_scope`: the scope of the network

### Dockerswarm role: tasks

  The `role: tasks` discovers all Swarm tasks.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<ip>:<port>`, where the `<ip>` is the node IP, while the `<port>` is the published port of the task.
  If the task has multiple published ports, then multiple targets are generated - one per each port.
  If the task has no published ports, then the `<port>` is set to the `port` value obtained from `dockerswarm_sd_configs`.

  Available meta labels for `role: tasks` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_dockerswarm_container_label_<labelname>`: each label of the container
* `__meta_dockerswarm_task_id`: the id of the task
* `__meta_dockerswarm_task_container_id`: the container id of the task
* `__meta_dockerswarm_task_desired_state`: the desired state of the task
* `__meta_dockerswarm_task_slot`: the slot of the task
* `__meta_dockerswarm_task_state`: the state of the task
* `__meta_dockerswarm_task_port_publish_mode`: the publishing mode of the task port
* `__meta_dockerswarm_service_id`: the id of the service
* `__meta_dockerswarm_service_name`: the name of the service
* `__meta_dockerswarm_service_mode`: the mode of the service
* `__meta_dockerswarm_service_label_<labelname>`: each label of the service
* `__meta_dockerswarm_network_id`: the ID of the network
* `__meta_dockerswarm_network_name`: the name of the network
* `__meta_dockerswarm_network_ingress`: whether the network is ingress
* `__meta_dockerswarm_network_internal`: whether the network is internal
* `__meta_dockerswarm_network_label_<labelname>`: each label of the network
* `__meta_dockerswarm_network_label`: each label of the network
* `__meta_dockerswarm_network_scope`: the scope of the network
* `__meta_dockerswarm_node_id`: the ID of the node
* `__meta_dockerswarm_node_hostname`: the hostname of the node
* `__meta_dockerswarm_node_address`: the address of the node
* `__meta_dockerswarm_node_availability`: the availability of the node
* `__meta_dockerswarm_node_label_<labelname>`: each label of the node
* `__meta_dockerswarm_node_platform_architecture`: the architecture of the node
* `__meta_dockerswarm_node_platform_os`: the operating system of the node
* `__meta_dockerswarm_node_role`: the role of the node
* `__meta_dockerswarm_node_status`: the status of the node

  The `__meta_dockerswarm_network_*` meta labels are not populated for ports which are published with `mode=host`.

### Dockerswarm role: nodes

  The `role: nodes` is used to discover Swarm nodes.

  Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
  to `<ip>:<port>`, where `<ip>` is the node IP, while the `<port>` is the `port` value obtained from the `dockerswarm_sd_configs`.

  Available meta labels for `role: nodes` during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_dockerswarm_node_address`: the address of the node
* `__meta_dockerswarm_node_availability`: the availability of the node
* `__meta_dockerswarm_node_engine_version`: the version of the node engine
* `__meta_dockerswarm_node_hostname`: the hostname of the node
* `__meta_dockerswarm_node_id`: the ID of the node
* `__meta_dockerswarm_node_label_<labelname>`: each label of the node
* `__meta_dockerswarm_node_manager_address`: the address of the manager component of the node
* `__meta_dockerswarm_node_manager_leader`: the leadership status of the manager component of the node (true or false)
* `__meta_dockerswarm_node_manager_reachability`: the reachability of the manager component of the node
* `__meta_dockerswarm_node_platform_architecture`: the architecture of the node
* `__meta_dockerswarm_node_platform_os`: the operating system of the node
* `__meta_dockerswarm_node_role`: the role of the node
* `__meta_dockerswarm_node_status`: the status of the node

The list of discovered Docker Swarm targets is refreshed at the interval, which can be configured via `-promscrape.dockerswarmSDCheckInterval` command-line flag.


## ec2_sd_configs

EC2 SD configuration allows retrieving scrape targets from [AWS EC2 instances](https://aws.amazon.com/ec2/).

Configuration example:

```yaml
scrape_configs:
- job_name: ec2
  ec2_sd_configs:

    # region is an optional config for AWS region.
    # By default, the region from the instance metadata is used.
    #
  - region: "..."

    # endpoint is an optional custom AWS API endpoint to use.
    # By default, the standard endpoint for the given region is used.
    #
    # endpoint: "..."

    # sts_endpoint is an optional custom STS API endpoint to use.
    # By default, the standard endpoint for the given region is used.
    #
    # sts_endpoint: "..."

    # access_key is an optional AWS API access key.
    # By default, the access key is loaded from AWS_ACCESS_KEY_ID environment var.
    #
    # access_key: "..."

    # secret_key is an optional AWS API secret key.
    # By default, the secret key is loaded from AWS_SECRET_ACCESS_KEY environment var.
    #
    # secret_key: "..."

    # role_arn is an optional AWS Role ARN, an alternative to using AWS API keys.
    #
    # role_arn: "..."

    # profile is an optional named AWS profile from ~/.aws/config and ~/.aws/credentials.
    # When set, credentials and role_arn are resolved from the profile, with source_profile
    # chaining supported. See https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
    #
    # profile: "..."

    # port is an optional port to scrape metrics from.
    # By default, port 80 is used.
    #
    # port: ...

    # filters is an optional filters for the instance list.
    # Available filter criteria can be found here:
    # https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html
    # Filter API documentation: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Filter.html
    #
    # filters:
    # - name: "..."
    #   values: ["...", "..."]

    # az_filters is an optional filters for the availability zones list.
    # Available filter criteria can be found here:
    # https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html
    # Filter API documentation: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Filter.html
    #
    # az_filters:
    # - name: "..."
    #   values: ["...", "..."]
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<instance_ip>:<port>`, where `<instance_ip>` is the private IP of the instance, while the `<port>` is set to the `port` value
obtain from `ec2_sd_configs`.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_ec2_ami`: the EC2 Amazon Machine Image
* `__meta_ec2_architecture`: the architecture of the instance
* `__meta_ec2_availability_zone`: the availability zone in which the instance is running
* `__meta_ec2_availability_zone_id`: the availability zone ID in which the instance is running (requires ec2:DescribeAvailabilityZones)
* `__meta_ec2_instance_id`: the EC2 instance ID
* `__meta_ec2_instance_lifecycle`: the lifecycle of the EC2 instance, set only for 'spot' or 'scheduled' instances, absent otherwise
* `__meta_ec2_instance_state`: the state of the EC2 instance
* `__meta_ec2_instance_type`: the type of the EC2 instance
* `__meta_ec2_ipv6_addresses`: comma separated list of IPv6 addresses assigned to the instance's network interfaces, if present
* `__meta_ec2_owner_id`: the ID of the AWS account that owns the EC2 instance
* `__meta_ec2_platform`: the Operating System platform, set to 'windows' on Windows servers, absent otherwise
* `__meta_ec2_primary_subnet_id`: the subnet ID of the primary network interface, if available
* `__meta_ec2_private_dns_name`: the private DNS name of the instance, if available
* `__meta_ec2_private_ip`: the private IP address of the instance, if present
* `__meta_ec2_public_dns_name`: the public DNS name of the instance, if available
* `__meta_ec2_public_ip`: the public IP address of the instance, if available
* `__meta_ec2_region`: EC2 region for the discovered instance
* `__meta_ec2_subnet_id`: comma separated list of subnets IDs in which the instance is running, if available
* `__meta_ec2_tag_<tagkey>`: each tag value of the instance
* `__meta_ec2_vpc_id`: the ID of the VPC in which the instance is running, if available

The list of discovered EC2 targets is refreshed at the interval, which can be configured via `-promscrape.ec2SDCheckInterval` command-line flag.


## eureka_sd_configs

Eureka SD configuration allows retrieving scrape targets using the [Eureka REST API](https://github.com/Netflix/eureka/wiki/Eureka-REST-operations).

Configuration example:

```yaml
scrape_configs:
- job_name: eureka
  eureka_sd_configs:

    # server is an optional URL to connect to the Eureka server.
    # By default, the http://localhost:8080/eureka/v2 is used.
    #
  - server: "..."

    # Additional HTTP API client options can be specified here.
    # See https://docs.victoriametrics.com/victoriametrics/sd_configs/#http-api-client-options
```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to `<instance_host>:<instance_port>`, where `<instance_host>` is the discovered instance hostname, while the `<instance_port>`
is the discovered instance port. If the instance has no port, then port 80 is used.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_eureka_app_name`: the name of the app
* `__meta_eureka_app_instance_id`: the ID of the app instance
* `__meta_eureka_app_instance_hostname`: the hostname of the instance
* `__meta_eureka_app_instance_homepage_url`: the homepage url of the app instance
* `__meta_eureka_app_instance_statuspage_url`: the status page url of the app instance
* `__meta_eureka_app_instance_healthcheck_url`: the health check url of the app instance
* `__meta_eureka_app_instance_ip_addr`: the IP address of the app instance
* `__meta_eureka_app_instance_vip_address`: the VIP address of the app instance
* `__meta_eureka_app_instance_secure_vip_address`: the secure VIP address of the app instance
* `__meta_eureka_app_instance_status`: the status of the app instance
* `__meta_eureka_app_instance_port`: the port of the app instance
* `__meta_eureka_app_instance_port_enabled`: the port enabled of the app instance
* `__meta_eureka_app_instance_secure_port`: the secure port address of the app instance
* `__meta_eureka_app_instance_secure_port_enabled`: the secure port of the app instance
* `__meta_eureka_app_instance_country_id`: the country ID of the app instance
* `__meta_eureka_app_instance_metadata_<metadataname>`: app instance metadata
* `__meta_eureka_app_instance_datacenterinfo_name`: the datacenter name of the app instance
* `__meta_eureka_app_instance_datacenterinfo_metadata_<metadataname>`: the datacenter metadata

The list of discovered Eureka targets is refreshed at the interval, which can be configured via `-promscrape.eurekaSDCheckInterval` command-line flag.


## file_sd_configs

File-based service discovery reads a set of files with lists of targets to scrape.

Configuration example:

```yaml
scrape_configs:
- job_name: file
  file_sd_configs:

    # files must contain a list of file patterns for files with scrape targets.
    # The last path segment can contain `*`, which matches any number of chars in file name.
    #
    # files may contain http/https urls additionally to local files. These urls cannot contain `*`.
    #
  - files:
    - "my/path/*.yaml"
    - "another/path.json"
    - "http://central-config-server/targets?type=foobar"
```

See [these examples](https://docs.victoriametrics.com/victoriametrics/scrape_config_examples/#file-based-target-discovery) on how to configure file-based target discovery.

The referred files and urls must contain a list of static configs in one of the following formats:

* JSON:

  ```json
  [
    {
      "targets": ["<host>", ... ],
      "labels": {
        "<labelname>": "<labelvalue>",
        ...,
      }
    },
    ...
  ]
  ```

* YAML:

  ```yaml
  - targets: ["<host>", ... ]
    labels:
      <labelname>: <labelvalue>
      ...
    ...
  ```

Each discovered target has an [`__address__`](https://docs.victoriametrics.com/victoriametrics/relabeling/#how-to-modify-scrape-urls-in-targets) label set
to one of the `target` value specified in the target files.

The following meta labels are available on discovered targets during [relabeling](https://docs.victoriametrics.com/victoriametrics/relabeling/):

* `__meta_filepath`: the filepath from which the target was extracted

See the [list of integrations](https://prometheus.io/docs/operating/integrations/#file-service-discovery) with `file_sd_configs`.

The list of discovered file-based targets is refreshed at the interval, which can be configured via `-promscrape.fileSDCheckInterval` command-line flag.
