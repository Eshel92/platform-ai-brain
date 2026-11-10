---
Title: "OSS Cluster API"
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Use the OSS Cluster API to improve performance and keep applications current with cluster topology changes.
linktitle: "OSS Cluster API"
weight: $weight
url: '/operate/rs/7.22/clusters/optimize/oss-cluster-api/'
---
OSS Cluster API reduces access times and latency with near-linear scalability.
The OSS Cluster API provides a simple mechanism for Redis clients to know the cluster topology.

Clients must first connect to the master node to get the cluster topology,
and then they connect directly to the Redis proxy on each node that hosts a master shard.

> [!NOTE]
> You must use a client that supports the cluster API to connect to a database
> that has the cluster API enabled.


You can use the OSS Cluster API along with other Redis Enterprise Software high availability
to get high performance with low latency
and let applications stay current with cluster topology changes, including add node, remove node, and node failover.

For more about working with the OSS Cluster API in Redis Enterprise Software, see [Enable OSS Cluster API](/content/operate/rs/7.22/databases/configure/oss-cluster-api.md). 

To learn how to enable OSS Cluster API in Redis Cloud, see [Clustering Redis databases](/content/operate/rc/databases/configuration/clustering.md#cluster-api).
