---
weight: 4
menu:
  docs:
    parent: victoriametrics
    weight: 4
title: vmalert
description: "Alerting and recording rule evaluation with Alertmanager integration and multi-tenancy support."
tags:
  - metrics
  - logs
aliases:
  - /vmalert.html
  - /vmalert/index.html
  - /vmalert/
---
`vmalert` executes a list of the given [alerting](https://docs.victoriametrics.com/victoriametrics/vmalert/#alerting-rules)
or [recording](https://docs.victoriametrics.com/victoriametrics/vmalert/#recording-rules)
rules against configured `-datasource.url`. For sending alerting notifications
`vmalert` relies on [Alertmanager](https://github.com/prometheus/alertmanager) configured via `-notifier.url` flag.
Recording rules results are persisted via remote write protocols and require `-remoteWrite.url` to be configured.
`vmalert` is heavily inspired by [Prometheus](https://prometheus.io/docs/alerting/latest/overview/)
implementation and aims to be compatible with its syntax.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `vmalert.parts/`)

- `001-features-groups.md`: Features … Groups
- `002-templating-multitenancy.md`: Templating … Multitenancy
- `003-reading-rules-from-object-storage-web.md`: Reading rules from object storage … Web
- `004-rules-backfilling-monitoring.md`: Rules backfilling … Monitoring
- `005-troubleshooting-profiling.md`: Troubleshooting … Profiling
- `006-configuration-how-to-build-from-sources.md`: Configuration … How to build from sources
