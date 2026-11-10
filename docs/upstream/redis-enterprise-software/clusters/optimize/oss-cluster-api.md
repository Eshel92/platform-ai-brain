---
Title: "OSS Cluster API"
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
- kubernetes
description: Use the Redis OSS Cluster API to improve performance and keep applications current with cluster topology changes.
linktitle: "Redis OSS Cluster API"
weight: $weight
---
OSS Cluster API reduces access times and latency with near-linear scalability.
The OSS Cluster API provides a simple mechanism for Redis clients to know the cluster topology.

Clients must first connect to the master node to get the cluster topology,
and then they connect directly to the Redis proxy on each node that hosts a master shard.

> [!NOTE]
> You must use a client that supports the cluster API to connect to a database
> that has the cluster API enabled.


You can use the Redis OSS Cluster API along with other Redis Enterprise Software high availability
to get high performance with low latency
and let applications stay current with cluster topology changes, including add node, remove node, and node failover.

For more about working with the OSS Cluster API in Redis Software, see [Enable OSS Cluster API](/content/operate/rs/databases/configure/oss-cluster-api.md). 

To learn how to enable OSS Cluster API in Redis Cloud, see [Clustering Redis databases](/content/operate/rc/databases/configuration/clustering.md#cluster-api).

To enable OSS Cluster API in Kubernetes, see [Enable cluster-aware clients (OSS Cluster API)](/content/operate/kubernetes/networking/cluster-aware-clients.md).
