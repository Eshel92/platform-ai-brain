---
weight: 3
menu:
  docs:
    parent: victoriametrics
    weight: 3
title: vmagent
description: "agent for metrics collection, supporting both push and pull models, service discovery, relabeling, sharding, replication, on-disk buffering."
tags:
  - metrics
aliases:
  - /vmagent.html
  - /vmagent/index.html
  - /vmagent/
---

`vmagent` is a tiny agent that helps you collect metrics from various sources,
[relabel and filter the collected metrics](https://docs.victoriametrics.com/victoriametrics/relabeling/)
and store them in [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics)
or any other storage systems via the Prometheus `remote_write` protocol
or via the [VictoriaMetrics `remote_write` protocol](#victoriametrics-remote-write-protocol).

See [Quick Start](#quick-start) for details.

![vmagent](vmagent.webp)
{width="700"}

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `vmagent.parts/`)

- `001-motivation-quick-start.md`: Motivation … Quick Start
- `002-use-cases.md`: Use Cases
- `003-how-to-push-data-to-vmagent-victoriametrics-remote.md`: How to push data to vmagent … VictoriaMetrics remote write protocol
- `004-multitenancy-prometheus-staleness-markers.md`: Multitenancy … Prometheus staleness markers
- `005-metric-metadata-scraping-targets-via-unix-sockets.md`: Metric metadata … Scraping targets via unix sockets
- `006-on-disk-persistence-monitoring.md`: On-disk persistence … Monitoring
- `007-troubleshooting-profiling.md`: Troubleshooting … Profiling
- `008-advanced-usage.md`: Advanced usage
