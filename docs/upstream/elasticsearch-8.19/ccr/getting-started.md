<!-- Converted from ccr/getting-started.asciidoc (AsciiDoc). Includes are inlined. -->

### Tutorial: Set up cross-cluster replication

Use this guide to set up cross-cluster replication (CCR) between clusters in two
datacenters. Replicating your data across datacenters provides several benefits:

* Brings data closer to your users or application server to reduce latency and
response time
* Provides your mission-critical applications with the tolerance to withstand datacenter or region outages

In this guide, you'll learn how to:

* Configure a remote cluster with a leader index
* Create a follower index on a local cluster
* Create an auto-follow pattern to automatically follow time series indices
that are periodically created in a remote cluster

You can manually create follower indices to replicate specific indices on a
remote cluster, or configure auto-follow patterns to replicate rolling time series indices.

**Tip:** If you want to replicate data across clusters in the cloud, you can
link:{cloud}/ec-enable-ccs.html[configure remote clusters on Elasticsearch Service]. Then, you
can search across clusters and set up cross-cluster replication.

#### Prerequisites

To complete this tutorial, you need:

* The `manage` cluster privilege on the local cluster.
* A license on both clusters that includes cross-cluster replication. [Activate a free 30-day trial](https://www.elastic.co/guide/en/kibana/8.19/managing-licenses.html).
* An index on the remote cluster that contains the data you want to replicate.
This tutorial uses the sample eCommerce orders data set.
[Load sample data](https://www.elastic.co/guide/en/kibana/8.19/get-started.html#gs-get-data-into-kibana).
* In the local cluster, all nodes with the `master` node role must
also have the `remote_cluster_client` role. The local cluster
must also have at least one node with both a data role and the
`remote_cluster_client` role. Individual tasks for coordinating
replication scale based on the number of data nodes with the
`remote_cluster_client` role in the local cluster.

#### Connect to a remote cluster

To replicate an index on a remote cluster (Cluster A) to a local cluster (Cluster B), you configure Cluster A as a remote on Cluster B.

(Figure: images/ccr-tutorial-clusters.png)

To configure a remote cluster from Stack Management in Kibana:

. Set up a secure connection as needed.
. Select *Remote Clusters* from the side navigation.
. Specify the Elasticsearch endpoint URL, or the IP address or host name of the remote
cluster (`ClusterA`) followed by the transport port (defaults to `9300`). For
example, `cluster.es.eastus2.staging.azure.foundit.no:9400` or
`192.168.1.1:9300`.

**API example**
You can also use the cluster update settings API to
add a remote cluster:

```console
PUT /_cluster/settings
{
  "persistent" : {
    "cluster" : {
      "remote" : {
        "leader" : {
          "seeds" : [
            "127.0.0.1:9300" <1>
          ]
        }
      }
    }
  }
}
```
<1> Specifies the hostname and transport port of a seed node in the remote
    cluster.

You can verify that the local cluster is successfully connected to the remote
cluster.

```console
GET /_remote/info
```

The API response indicates that the local cluster is connected to the remote
cluster with cluster alias `leader`.

```console-result
{
  "leader" : {
    "seeds" : [
      "127.0.0.1:9300"
    ],
    "connected" : true,
    "num_nodes_connected" : 1, <1>
    "max_connections_per_cluster" : 3,
    "initial_connect_timeout" : "30s",
    "skip_unavailable" : true,
    "mode" : "sniff"
  }
}
```
<1> The number of nodes in the remote cluster the local cluster is
    connected to.

(See `security/authentication/remote-clusters-privileges-cert.md`)

#### Create a follower index to replicate a specific index

When you create a follower index, you reference the remote cluster and the
leader index in your remote cluster.

To create a follower index from Stack Management in Kibana:

. Select *Cross-Cluster Replication* in the side navigation and choose the
*Follower Indices* tab.
. Choose the cluster (ClusterA) containing the leader index you want to
replicate.
. Enter the name of the leader index, which is
`kibana_sample_data_ecommerce` if you are following the tutorial.
. Enter a name for your follower index, such as `follower-kibana-sample-data`.

Elasticsearch initializes the follower using the
remote recovery
process, which transfers the existing Lucene segment files from the leader
index to the follower index. The index status changes to *Paused*. When the
remote recovery process is complete, the index following begins and the status
changes to *Active*.

When you index documents into your leader index, Elasticsearch replicates the documents
in the follower index.

(Figure: images/ccr-follower-index.png)

**API example**
You can also use the create follower API to create follower
indices. When you create a follower index, you must reference the remote cluster
and the leader index that you created in the remote cluster.

When initiating the follower request, the response returns before the
remote recovery process completes. To wait for the process
to complete, add the `wait_for_active_shards` parameter to your request.

```console
PUT /server-metrics-follower/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "leader",
  "leader_index" : "server-metrics"
}
```

```console-result
{
  "follow_index_created" : true,
  "follow_index_shards_acked" : true,
  "index_following_started" : true
}
```

Use the
get follower stats API to inspect the status of
replication.

```console
POST /server-metrics-follower/_ccr/pause_follow

POST /server-metrics-follower/_close

POST /server-metrics-follower/_ccr/unfollow
```

#### Create an auto-follow pattern to replicate time series indices

You use auto-follow patterns to automatically create new
followers for rolling time series indices. Whenever the name of a new index on
the remote cluster matches the auto-follow pattern, a corresponding follower
index is added to the local cluster. Note that only indices created on the
remote cluster after the auto-follow pattern is created will be auto-followed:
existing indices on the remote cluster are ignored even if they match the pattern.

An auto-follow pattern specifies the remote cluster you want to replicate from,
and one or more index patterns that specify the rolling time series indices you
want to replicate.

To create an auto-follow pattern from Stack Management in Kibana:

. Select *Cross Cluster Replication* in the side navigation and choose the
*Auto-follow patterns* tab.
. Enter a name for the auto-follow pattern, such as `beats`.
. Choose the remote cluster that contains the index you want to replicate,
which in the example scenario is Cluster A.
. Enter one or more index patterns that identify the indices you want to
replicate from the remote cluster. For example, enter
`metricbeat-* packetbeat-*` to automatically create followers for {metricbeat} and {packetbeat} indices.
. Enter *follower-* as the prefix to apply to the names of the follower indices so
you can more easily identify replicated indices.

As new indices matching these patterns are
created on the remote, Elasticsearch automatically replicates them to local follower indices.

(Figure: images/auto-follow-patterns.png)

**API example**
Use the create auto-follow pattern API to
configure auto-follow patterns.

```console
PUT /_ccr/auto_follow/beats
{
  "remote_cluster" : "leader",
  "leader_index_patterns" :
  [
    "metricbeat-*", <1>
    "packetbeat-*" <2>
  ],
  "follow_index_pattern" : "{{leader_index}}-copy" <3>
}
```
<1> Automatically follow new {metricbeat} indices.
<2> Automatically follow new {packetbeat} indices.
<3> The name of the follower index is derived from the name of the leader index
    by adding the suffix `-copy` to the name of the leader index.

```console-result
{
  "acknowledged" : true
}
```

```console
DELETE /_ccr/auto_follow/beats
```
