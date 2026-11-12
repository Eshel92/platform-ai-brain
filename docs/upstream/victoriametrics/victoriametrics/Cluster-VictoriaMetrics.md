---
weight: 2
menu:
  docs:
    identifier: vm-cluster-version
    parent: 'victoriametrics'
    weight: 2
title: Cluster version
description: "Deploy and configure cluster mode with vminsert, vmselect, and vmstorage components, including replication and multi-tenancy."
tags:
  - metrics
aliases:
  - /Cluster-VictoriaMetrics.html
  - /cluster-victoriametrics/index.html
  - /cluster-victoriametrics/
  - /Cluster-VictoriaMetrics/
---

VictoriaMetrics is a fast, cost-effective, and scalable solution for monitoring and managing time series data. It delivers high performance and reliability, making it an ideal choice for businesses of all sizes.

- **Case studies**: [Grammarly, Roblox, Wix, Spotify,...](https://docs.victoriametrics.com/victoriametrics/casestudies/).
- **Available**: [Binary releases](https://github.com/VictoriaMetrics/VictoriaMetrics/releases/latest), Docker images on [Docker Hub](https://hub.docker.com/r/victoriametrics/victoria-metrics/) and [Quay](https://quay.io/repository/victoriametrics/victoria-metrics), [Source code](https://github.com/VictoriaMetrics/VictoriaMetrics).
- **Deployment types**: [Single-node version](https://docs.victoriametrics.com/) and [Cluster version](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/) under [Apache License 2.0](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/LICENSE).
- **Getting started:** Read [key concepts](https://docs.victoriametrics.com/victoriametrics/keyconcepts/) and follow the
  [quick start guide](https://docs.victoriametrics.com/victoriametrics/quick-start/).
- **Community**: [Slack](https://slack.victoriametrics.com/)(join via [Slack Inviter](https://slack.victoriametrics.com/)), [X (Twitter)](https://x.com/VictoriaMetrics), [YouTube](https://www.youtube.com/@VictoriaMetrics). See full list [here](https://docs.victoriametrics.com/victoriametrics/#community-and-contributions).
- **Changelog**: Project evolves fast - check the [CHANGELOG](https://docs.victoriametrics.com/victoriametrics/changelog/), and [How to upgrade](https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/#how-to-upgrade-victoriametrics).
- **Enterprise support:** [Contact us](mailto:info@victoriametrics.com) for commercial support with additional [enterprise features](https://docs.victoriametrics.com/victoriametrics/enterprise/).
- **Enterprise releases:** Enterprise and [long-term support releases (LTS)](https://docs.victoriametrics.com/victoriametrics/lts-releases/) are publicly available and can be evaluated for free
  using a [free trial license](https://victoriametrics.com/products/enterprise/trial/).
- **Security:** we achieved [security certifications](https://victoriametrics.com/security/) for Database Software Development and Software-Based Monitoring Services.

There is also user-friendly database for logs - [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/).

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `Cluster-VictoriaMetrics.parts/`)

- `001-prominent-features-architecture-overview.md`: Prominent features … Architecture overview
- `002-cluster-setup.md`: Cluster setup
- `003-high-availability-cluster-resizing-and-scalability.md`: High availability … Cluster resizing and scalability
- `004-multitenancy.md`: Multitenancy
- `005-url-format.md`: URL format
- `006-operation.md`: Operation
- `007-deduplication-cardinality-limiter.md`: Deduplication … Cardinality limiter
- `008-capacity-planning-list-of-command-line-flags.md`: Capacity planning … List of command-line flags
