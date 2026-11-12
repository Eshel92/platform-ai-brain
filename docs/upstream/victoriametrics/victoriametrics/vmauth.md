---
weight: 5
menu:
  docs:
    parent: victoriametrics
    weight: 5
title: vmauth
description: "HTTP auth proxy, load balancer, and request router with support for basic auth, bearer tokens, per-user routing, and IP-based filters."
tags:
  - metrics
aliases:
  - /vmauth.html
  - /vmauth/index.html
  - /vmauth/
---
`vmauth` is an HTTP proxy, which can [authorize](https://docs.victoriametrics.com/victoriametrics/vmauth/#authorization), [route](https://docs.victoriametrics.com/victoriametrics/vmauth/#routing), and [load balance](https://docs.victoriametrics.com/victoriametrics/vmauth/#load-balancing) requests across [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) components or any other HTTP backends.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `vmauth.parts/`)

- `001-quick-start.md`: Quick start
- `002-use-cases.md`: Use cases
- `003-dropping-request-path-prefix-config-reload.md`: Dropping request path prefix … Config reload
- `004-concurrency-limiting-access-log.md`: Concurrency limiting … Access log
- `005-auth-config-automatic-issuing-of-tls-certificates.md`: Auth config … Automatic issuing of TLS certificates
- `006-monitoring-advanced-usage.md`: Monitoring … Advanced usage
