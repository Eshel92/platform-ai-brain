---
Title: Supported upgrade paths for Redis Software
alwaysopen: false
categories:
- docs
- operate
- rs
description: Supported paths to upgrade a Redis Software cluster.
linkTitle: Upgrade paths
weight: 30
tocEmbedHeaders: true
url: '/operate/rs/7.22/references/upgrade-paths/'
---

<span title="Check mark icon">&#x2705;</span> Supported – You can upgrade directly from the current Redis Software cluster version.

<span title="X icon">:x:</span> Not supported – You cannot upgrade directly from the current Redis Software cluster version. You must first upgrade to a supported intermediate version.

| Current Redis Software cluster version | Upgrade to Redis Software 7.2.x | Upgrade to Redis Software 7.4.x |  Upgrade to Redis Software 7.8.x | Upgrade to Redis Software 7.22.x | Upgrade to Redis Software 8.0.2-8.0.10 | Upgrade to Redis Software 8.0.16-8.0.20 | Upgrade to Redis Software 8.2.x |
|:-----------------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| 6.0.x | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 6.2.4<br />6.2.8 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 6.2.10<br />6.2.12<br />6.2.18 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 6.4.x | <span title="Supported">&#x2705;</span> |  <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Not supported">:x:</span> | <span title="Not supported">:x:</span> |
| 7.2.x | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 7.4.x | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 7.8.x | – | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 7.22.x | – | – | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 8.0.2<br />8.0.6<br />8.0.10 | – | – | – | – | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 8.0.16<br />8.0.18<br />8.0.20 | – | – | – | – | - | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| 8.2.x | – | – | – | – | – | – | <span title="Supported">&#x2705;</span> |


For detailed upgrade instructions, see [Upgrade a Redis Enterprise Software cluster](/content/operate/rs/7.22/installing-upgrading/upgrading/upgrade-cluster.md).

See the [Redis Enterprise Software product lifecycle](/content/operate/rs/7.22/installing-upgrading/product-lifecycle.md) for more information about release numbers and the end-of-life schedule.

> [!NOTE]
> Redis Enterprise for Kubernetes has its own support lifecycle, which accounts for the Kubernetes distribution lifecycle. For details, see [Supported Kubernetes distributions](/content/operate/kubernetes/reference/supported_k8s_distributions.md).
