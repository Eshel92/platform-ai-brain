---
build:
  list: never
  publishResources: false
  render: never
sitemap:
  disable: true
---
VictoriaMetrics is a fast, cost-effective, and scalable solution for monitoring and managing time series data. It delivers high performance and reliability, making it an ideal choice for businesses of all sizes.

![README-components.webp](README-components.webp)
{width="600"}

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

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `README.parts/`)

- `001-prominent-features-how-to-upgrade-victoriametrics.md`: Prominent features … How to upgrade VictoriaMetrics
- `002-vmui-how-to-scrape-prometheus-exporters-such-as-no.md`: vmui … How to scrape Prometheus exporters such as [node-exporter](https://github.com/prometheus/node_exporter)
- `003-prometheus-querying-api-usage-how-to-delete-time-s.md`: Prometheus querying API usage … How to delete time series
- `004-forced-merge-how-to-export-time-series.md`: Forced merge … How to export time series
- `005-how-to-import-time-series-data-federation.md`: How to import time series data … Federation
- `006-capacity-planning-resource-usage-limits.md`: Capacity planning … Resource usage limits
- `007-high-availability-storage.md`: High availability … Storage
- `008-indexdb-retention.md`: IndexDB … Retention
- `009-downsampling-alerting.md`: Downsampling … Alerting
- `010-security-tsdb-stats.md`: Security … TSDB stats
- `011-track-ingested-metrics-usage-troubleshooting.md`: Track ingested metrics usage … Troubleshooting
- `012-push-metrics-documentation.md`: Push metrics … Documentation
- `013-victoriametrics-logo-list-of-command-line-flags.md`: VictoriaMetrics Logo … List of command-line flags
