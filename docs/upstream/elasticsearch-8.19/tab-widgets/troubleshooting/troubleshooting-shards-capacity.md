<!-- Converted from tab-widgets/troubleshooting/troubleshooting-shards-capacity.asciidoc (AsciiDoc). Includes are inlined. -->

**Use Kibana**

. Log in to the {ess-console}[Elastic Cloud console].

. On the **Elasticsearch Service** panel, click the name of your deployment.

**Note:** If the name of your deployment is disabled your Kibana instances might be
unhealthy, in which case please contact [Elastic Support](https://support.elastic.co).
If your deployment doesn't include Kibana, all you need to do is
{cloud}/ec-access-kibana.html[enable it first].

. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Dev Tools > Console**.
(Figure: images/kibana-console.png)
. Check the current status of the cluster according the shards capacity indicator:
```console
GET _health_report/shards_capacity
```
The response will look like this:
```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "yellow",
      "symptom": "Cluster is close to reaching the configured maximum number of shards for data nodes.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000, <1>
          "current_used_shards": 988 <2>
        },
        "frozen": {
          "max_shards_in_cluster": 3000,
          "current_used_shards": 0
        }
      },
      "impacts": [
        ...
      ],
      "diagnosis": [
        ...
    }
  }
}
```
<1> Current value of the setting `cluster.max_shards_per_node`
<2> Current number of open shards across the cluster
. Update the `cluster.max_shards_per_node` setting with a proper value:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node": 1200
  }
}
```
This increase should only be temporary. As a long-term solution, we recommend
you add nodes to the oversharded data tier or
reduce your cluster's shard count on nodes that do not belong
to the frozen tier.

. To verify that the change has fixed the issue, you can get the current
status of the `shards_capacity` indicator by checking the `data` section of the
health API:
```console
GET _health_report/shards_capacity
```
The response will look like this:
```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "green",
      "symptom": "The cluster has enough room to add new shards.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000
        },
        "frozen": {
          "max_shards_in_cluster": 3000
        }
      }
    }
  }
}
```

. When a long-term solution is in place, we recommend you reset the
`cluster.max_shards_per_node` limit.
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node": null
  }
}
```

Check the current status of the cluster according the shards capacity indicator:

```console
GET _health_report/shards_capacity
```

The response will look like this:

```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "yellow",
      "symptom": "Cluster is close to reaching the configured maximum number of shards for data nodes.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000, <1>
          "current_used_shards": 988 <2>
        },
        "frozen": {
          "max_shards_in_cluster": 3000
        }
      },
      "impacts": [
        ...
      ],
      "diagnosis": [
        ...
    }
  }
}
```
<1> Current value of the setting `cluster.max_shards_per_node`
<2> Current number of open shards across the cluster

Using the `cluster settings API`, update the
`cluster.max_shards_per_node` setting:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node": 1200
  }
}
```

This increase should only be temporary. As a long-term solution, we recommend
you add nodes to the oversharded data tier or
reduce your cluster's shard count on nodes that do not belong
to the frozen tier. To verify that the change has fixed the issue, you can get the current
status of the `shards_capacity` indicator by checking the `data` section of the
health API:

```console
GET _health_report/shards_capacity
```

The response will look like this:

```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "green",
      "symptom": "The cluster has enough room to add new shards.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1200
        },
        "frozen": {
          "max_shards_in_cluster": 3000
        }
      }
    }
  }
}
```

When a long-term solution is in place, we recommend you reset the
`cluster.max_shards_per_node` limit.

```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node": null
  }
}
```

**Use Kibana**

. Log in to the {ess-console}[Elastic Cloud console].

. On the **Elasticsearch Service** panel, click the name of your deployment.

**Note:** If the name of your deployment is disabled your Kibana instances might be
unhealthy, in which case please contact [Elastic Support](https://support.elastic.co).
If your deployment doesn't include Kibana, all you need to do is
{cloud}/ec-access-kibana.html[enable it first].

. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Dev Tools > Console**.
(Figure: images/kibana-console.png)
. Check the current status of the cluster according the shards capacity indicator:
```console
GET _health_report/shards_capacity
```
The response will look like this:
```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "yellow",
      "symptom": "Cluster is close to reaching the configured maximum number of shards for frozen nodes.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000
        },
        "frozen": {
          "max_shards_in_cluster": 3000, <1>
          "current_used_shards": 2998 <2>
        }
      },
      "impacts": [
        ...
      ],
      "diagnosis": [
        ...
    }
  }
}
```
<1> Current value of the setting `cluster.max_shards_per_node.frozen`
<2> Current number of open shards used by frozen nodes across the cluster

. Update the `cluster.max_shards_per_node.frozen` setting:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node.frozen": 3200
  }
}
```
This increase should only be temporary. As a long-term solution, we recommend
you add nodes to the oversharded data tier or
reduce your cluster's shard count on nodes that belong
to the frozen tier.

. To verify that the change has fixed the issue, you can get the current
status of the `shards_capacity` indicator by checking the `data` section of the
health API:
```console
GET _health_report/shards_capacity
```
The response will look like this:
```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "green",
      "symptom": "The cluster has enough room to add new shards.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000
        },
        "frozen": {
          "max_shards_in_cluster": 3200
        }
      }
    }
  }
}
```
. When a long-term solution is in place, we recommend you reset the
`cluster.max_shards_per_node.frozen` limit.
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node.frozen": null
  }
}
```

Check the current status of the cluster according the shards capacity indicator:

```console
GET _health_report/shards_capacity
```

```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "yellow",
      "symptom": "Cluster is close to reaching the configured maximum number of shards for frozen nodes.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000
        },
        "frozen": {
          "max_shards_in_cluster": 3000, <1>
          "current_used_shards": 2998 <2>
        }
      },
      "impacts": [
        ...
      ],
      "diagnosis": [
        ...
    }
  }
}
```
<1> Current value of the setting `cluster.max_shards_per_node.frozen`.
<2> Current number of open shards used by frozen nodes across the cluster.

Using the `cluster settings API`, update the
`cluster.max_shards_per_node.frozen` setting:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node.frozen": 3200
  }
}
```

This increase should only be temporary. As a long-term solution, we recommend
you add nodes to the oversharded data tier or
reduce your cluster's shard count on nodes that belong
to the frozen tier. To verify that the change has fixed the issue, you can get the current
status of the `shards_capacity` indicator by checking the `data` section of the
health API:

```console
GET _health_report/shards_capacity
```

The response will look like this:

```console-result
{
  "cluster_name": "...",
  "indicators": {
    "shards_capacity": {
      "status": "green",
      "symptom": "The cluster has enough room to add new shards.",
      "details": {
        "data": {
          "max_shards_in_cluster": 1000
        },
        "frozen": {
          "max_shards_in_cluster": 3200
        }
      }
    }
  }
}
```

When a long-term solution is in place, we recommend you reset the
`cluster.max_shards_per_node.frozen` limit.

```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.max_shards_per_node.frozen": null
  }
}
```
