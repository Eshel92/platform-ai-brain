<!-- Converted from troubleshooting/common-issues/high-cpu-usage.asciidoc (AsciiDoc). Includes are inlined. -->

### High CPU usage

Elasticsearch uses thread pools to manage CPU resources for
concurrent operations. High CPU usage typically means one or more thread pools
are running low.

If a thread pool is depleted, Elasticsearch will reject requests
related to the thread pool. For example, if the `search` thread pool is
depleted, Elasticsearch will reject search requests until more threads are available.

You might experience high CPU usage if a data tier, and therefore the nodes assigned to that tier, is experiencing more traffic than other tiers. This imbalance in resource utilization is also known as hot spotting.

****
If you're using Elastic Cloud Hosted, then you can use AutoOps to monitor your cluster. AutoOps significantly simplifies cluster management with performance recommendations, resource utilization visibility, real-time issue detection and resolution paths. For more information, refer to [Monitor with AutoOps](https://www.elastic.co/guide/en/cloud/current/ec-autoops.html).
****

#### Diagnose high CPU usage

**Check CPU usage**

You can check the CPU usage per node using the cat nodes API:

```console
GET _cat/nodes?v=true&s=cpu:desc
```

The response's `cpu` column contains the current CPU usage as a percentage.
The `name` column contains the node's name. Elevated but transient CPU usage is
normal. However, if CPU usage is elevated for an extended duration, it should be
investigated.

To track CPU usage over time, we recommend enabling monitoring:

* (Recommended) Enable {cloud}/ec-monitoring-setup.html[logs and metrics]. When logs and metrics are enabled, monitoring information is visible on Kibana's [Stack Monitoring](https://www.elastic.co/guide/en/kibana/8.19/xpack-monitoring.html) page. 
You can also enable the [CPU usage threshold alert](https://www.elastic.co/guide/en/kibana/8.19/kibana-alerts.html) to be notified about potential issues through email.

* From your deployment menu, view the {cloud}/ec-saas-metrics-accessing.html[**Performance**] page. On this page, you can view two key metrics:
** **CPU usage**: Your deployment's CPU usage, represented as a percentage.
** **CPU credits**: Your remaining CPU credits, measured in seconds of CPU time.

Elasticsearch Service grants {cloud}/ec-vcpu-boost-instance.html[CPU credits] per deployment
to provide smaller clusters with performance boosts when needed. High CPU
usage can deplete these credits, which might lead to {cloud}/ec-scenario_why_is_performance_degrading_over_time.html[performance degradation] and {cloud}/ec-scenario_why_are_my_cluster_response_times_suddenly_so_much_worse.html[increased cluster response times].

* Enable Elasticsearch monitoring. When logs and metrics are enabled, monitoring information is visible on Kibana's [Stack Monitoring](https://www.elastic.co/guide/en/kibana/8.19/xpack-monitoring.html) page.
You can also enable the [CPU usage threshold alert](https://www.elastic.co/guide/en/kibana/8.19/kibana-alerts.html) to be notified about potential issues through email.

**Check hot threads**

If a node has high CPU usage, use the <<cluster-nodes-hot-threads,nodes hot
threads API>> to check for resource-intensive threads running on the node.

```console
GET _nodes/hot_threads
```

This API returns a breakdown of any hot threads in plain text. High CPU usage
frequently correlates to <<task-queue-backlog,a long-running task, or a
backlog of tasks>>.

#### Reduce CPU usage

The following tips outline the most common causes of high CPU usage and their
solutions.

**Scale your cluster**

Heavy indexing and search loads can deplete smaller thread pools. To better
handle heavy workloads, add more nodes to your cluster or upgrade your existing
nodes to increase capacity.

**Spread out bulk requests**

While more efficient than individual requests, large bulk indexing
or multi-search requests still require CPU resources. If
possible, submit smaller requests and allow more time between them.

**Cancel long-running searches**

Long-running searches can block threads in the `search` thread pool. To check
for these searches, use the task management API.

```console
GET _tasks?actions=*search&detailed
```

The response's `description` contains the search request and its queries.
`running_time_in_nanos` shows how long the search has been running.

```console-result
{
  "nodes" : {
    "oTUltX4IQMOUUVeiohTt8A" : {
      "name" : "my-node",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1:9300",
      "tasks" : {
        "oTUltX4IQMOUUVeiohTt8A:464" : {
          "node" : "oTUltX4IQMOUUVeiohTt8A",
          "id" : 464,
          "type" : "transport",
          "action" : "indices:data/read/search",
          "description" : "indices[my-index], search_type[QUERY_THEN_FETCH], source[{\"query\":...}]",
          "start_time_in_millis" : 4081771730000,
          "running_time_in_nanos" : 13991383,
          "cancellable" : true
        }
      }
    }
  }
}
```

To cancel a search and free up resources, use the API's `_cancel` endpoint.

```console
POST _tasks/oTUltX4IQMOUUVeiohTt8A:464/_cancel
```

For additional tips on how to track and avoid resource-intensive searches, see
Avoid expensive searches.
