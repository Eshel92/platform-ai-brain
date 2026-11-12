---
weight: 36
title: Prometheus service discovery
description: "Supported Prometheus-compatible service discovery mechanisms (Azure, Consul, DNS, Docker, EC2, GCE, Kubernetes, OpenStack, and more)"
menu:
  docs:
    parent: 'victoriametrics'
    weight: 36
tags:
  - metrics
aliases:
- /sd_configs.html
- /sd_configs/index.html
- /sd_configs/
---
# Supported service discovery configs

[vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/) and [single-node VictoriaMetrics](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-scrape-prometheus-exporters-such-as-node-exporter)
supports the following Prometheus-compatible service discovery options for Prometheus-compatible scrape targets in the file pointed by `-promscrape.config` command-line flag:

* `azure_sd_configs` is for scraping the targets registered in [Azure Cloud](https://azure.microsoft.com/en-us/). See [these docs](#azure_sd_configs).
* `consul_sd_configs` is for discovering and scraping targets registered in [Consul](https://www.consul.io/). See [these docs](#consul_sd_configs).
* `consulagent_sd_configs` is for discovering and scraping targets registered in [Consul Agent](https://developer.hashicorp.com/consul/api-docs/agent/service). See [these docs](#consulagent_sd_configs).
* `digitalocean_sd_configs` is for discovering and scraping targets registered in [DigitalOcean](https://www.digitalocean.com/). See [these docs](#digitalocean_sd_configs).
* `dns_sd_configs` is for discovering and scraping targets from [DNS](https://it.wikipedia.org/wiki/Domain_Name_System) records (SRV, A and AAAA). See [these docs](#dns_sd_configs).
* `docker_sd_configs` is for discovering and scraping [Docker](https://www.docker.com/) targets. See [these docs](#docker_sd_configs).
* `dockerswarm_sd_configs` is for discovering and scraping [Docker Swarm](https://docs.docker.com/engine/swarm/) targets. See [these docs](#dockerswarm_sd_configs).
* `ec2_sd_configs` is for discovering and scraping [Amazon EC2](https://aws.amazon.com/ec2/) targets. See [these docs](#ec2_sd_configs).
* `eureka_sd_configs` is for discovering and scraping targets registered in [Netflix Eureka](https://github.com/Netflix/eureka). See [these docs](#eureka_sd_configs).
* `file_sd_configs` is for scraping targets defined in external files (aka file-based service discovery). See [these docs](#file_sd_configs).
* `gce_sd_configs` is for discovering and scraping [Google Compute Engine](https://cloud.google.com/compute) targets. See [these docs](#gce_sd_configs).
* `hetzner_sd_configs` is for discovering and scraping [Hetzner Cloud](https://www.hetzner.com/cloud) and [Hetzner Robot](https://docs.hetzner.com/robot) targets. See [these docs](#hetzner_sd_configs).
* `http_sd_configs` is for discovering and scraping targets provided by external http-based service discovery. See [these docs](#http_sd_configs).
* `kubernetes_sd_configs` is for discovering and scraping [Kubernetes](https://kubernetes.io/) targets. See [these docs](#kubernetes_sd_configs).
* `kuma_sd_configs` is for discovering and scraping [Kuma](https://kuma.io) targets. See [these docs](#kuma_sd_configs).
* `linode_sd_configs` is for discovering and scraping [Linode](https://www.linode.com/) instances. See [these docs](#linode_sd_configs).
* `marathon_sd_configs` is for discovering and scraping [Marathon](https://github.com/d2iq-archive/marathon) targets. See [these docs](#marathon_sd_configs).
* `nomad_sd_configs` is for discovering and scraping targets registered in [HashiCorp Nomad](https://www.nomadproject.io/). See [these docs](#nomad_sd_configs).
* `openstack_sd_configs` is for discovering and scraping OpenStack targets. See [these docs](#openstack_sd_configs).
* `ovhcloud_sd_configs` is for discovering and scraping OVH Cloud VPS and dedicated server targets. See [these docs](#ovhcloud_sd_configs).
* `puppetdb_sd_configs` is for discovering and scraping PuppetDB targets. See [these docs](#puppetdb_sd_configs).
* `static_configs` is for scraping statically defined targets. See [these docs](#static_configs).
* `vultr_sd_configs` is for discovering and scraping [Vultr](https://www.vultr.com/) targets. See [these docs](#vultr_sd_configs).
* `yandexcloud_sd_configs` is for discovering and scraping [Yandex Cloud](https://cloud.yandex.com/en/) targets. See [these docs](#yandexcloud_sd_configs).

Note that the `refresh_interval` option isn't supported for these scrape configs. Use the corresponding `-promscrape.*CheckInterval`
command-line flag instead. For example, `-promscrape.consulSDCheckInterval=60s` sets `refresh_interval` for all the `consul_sd_configs`
entries to 60s. Run `vmagent -help` or `victoria-metrics -help` in order to see default values for the `-promscrape.*CheckInterval` flags.

Please file feature requests to [our issue tracker](https://github.com/VictoriaMetrics/VictoriaMetrics/issues) if you need other service discovery mechanisms
to be supported by VictoriaMetrics and `vmagent`.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `sd_configs.parts/`)

- `001-azure-sd-configs-dns-sd-configs.md`: azure_sd_configs … dns_sd_configs
- `002-docker-sd-configs-file-sd-configs.md`: docker_sd_configs … file_sd_configs
- `003-gce-sd-configs-http-sd-configs.md`: gce_sd_configs … http_sd_configs
- `004-kubernetes-sd-configs-kuma-sd-configs.md`: kubernetes_sd_configs … kuma_sd_configs
- `005-linode-sd-configs-ovhcloud-sd-configs.md`: linode_sd_configs … ovhcloud_sd_configs
- `006-puppetdb-sd-configs-scrape-configs.md`: puppetdb_sd_configs … scrape_configs
- `007-http-api-client-options.md`: HTTP API client options
