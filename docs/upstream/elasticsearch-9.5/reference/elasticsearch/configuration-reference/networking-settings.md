---
mapped_pages:
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-network.html
applies_to:
  stack: ga
  serverless: unavailable
products:
  - id: elasticsearch
---

# Networking settings [modules-network]

Each Elasticsearch node has two different network interfaces. Clients send requests to Elasticsearch's REST APIs using its [HTTP interface](#http-settings), but nodes communicate with other nodes using the [transport interface](#transport-settings). The transport interface is also used for communication with [remote clusters](docs-content://deploy-manage/remote-clusters/remote-clusters-self-managed.md). The transport interface uses a custom binary protocol sent over [long-lived](#long-lived-connections) TCP channels. Both interfaces can be configured to use [TLS for security](docs-content://deploy-manage/security.md).

You can configure both of these interfaces at the same time using the `network.*` settings. If you have a more complicated network, you might need to configure the interfaces independently using the `http.*` and `transport.*` settings. Where possible, use the `network.*` settings that apply to both interfaces to simplify your configuration and reduce duplication.

By default Elasticsearch binds only to `localhost` which means it cannot be accessed remotely. This configuration is sufficient for a local development cluster made of one or more nodes all running on the same host. To form a cluster across multiple hosts, or which is accessible to remote clients, you must adjust some [network settings](#common-network-settings) such as `network.host`.

::::{admonition} Be careful with the network configuration!
:class: warning

Never expose an unprotected node to the public internet. If you do, you are permitting anyone in the world to download, modify, or delete any of the data in your cluster.

::::


Configuring Elasticsearch to bind to a non-local address will [convert some warnings into fatal exceptions](docs-content://deploy-manage/deploy/self-managed/important-settings-configuration.md#bootstrap-checks). If a node refuses to start after configuring its network settings then you must address the logged exceptions before proceeding.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `networking-settings.parts/`)

- `001-commonly-used-network-settings-common-network-sett.md`: Commonly used network settings [common-network-settings] … Advanced network settings [advanced-network-settings]
- `002-advanced-http-settings-http-settings.md`: Advanced HTTP settings [http-settings]
- `003-advanced-transport-settings-transport-settings-adv.md`: Advanced transport settings [transport-settings] … Advanced remote cluster (API key based model) settings [remote-cluster-network-settings]
- `004-request-tracing-request-tracing-tcp-readiness-port.md`: Request tracing [_request_tracing] … TCP readiness port [tcp-readiness-port]
