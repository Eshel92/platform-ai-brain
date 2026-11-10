<!-- Converted from tab-widgets/troubleshooting/data/enable-cluster-allocation-widget.asciidoc (AsciiDoc). Includes are inlined. -->

In order to get the shards assigned we'll need to change the value of the
configuration that restricts the 
assignemnt of the shards to allow all shards to be allocated.

We'll achieve this by inspecting the system-wide `cluster.routing.allocation.enable` 
cluster setting and changing the configured value to 
`all`.

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

. Inspect the `cluster.routing.allocation.enable` cluster setting:
```console
GET /_cluster/settings?flat_settings
```
The response will look like this:
```console-result
{
  "persistent": {
    "cluster.routing.allocation.enable": "none" <1>
  },
  "transient": {}
}
```

<1> Represents the current configured value that controls if data is partially
or fully allowed to be allocated in the system.

. Change the configuration 
value to allow all the data in the system to be fully allocated:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.routing.allocation.enable" : "all" <1>
  }
}
```

<1> The new value for the `allocation.enable` system-wide configuration 
is changed to allow all the shards to be allocated. 

In order to get the shards assigned we'll need to change the value of the
configuration that restricts the 
assignemnt of the shards to allow all shards to be allocated.

We'll achieve this by inspecting the system-wide `cluster.routing.allocation.enable` 
cluster setting and changing the configured value to 
`all`.

. Inspect the `cluster.routing.allocation.enable` cluster setting:
```console
GET /_cluster/settings?flat_settings
```
The response will look like this:
```console-result
{
  "persistent": {
    "cluster.routing.allocation.enable": "none" <1>
  },
  "transient": {}
}
```

<1> Represents the current configured value that controls if data is partially
or fully allowed to be allocated in the system.

. Change the configuration 
value to allow all the data in the system to be fully allocated:
```console
PUT _cluster/settings
{
  "persistent" : {
    "cluster.routing.allocation.enable" : "all" <1>
  }
}
```

<1> The new value for the `allocation.enable` system-wide configuration 
is changed to allow all the shards to be allocated.
