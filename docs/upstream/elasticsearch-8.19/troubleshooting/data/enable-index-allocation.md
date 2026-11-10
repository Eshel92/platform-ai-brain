<!-- Converted from troubleshooting/data/enable-index-allocation.asciidoc (AsciiDoc). Includes are inlined. -->

## Allow Elasticsearch to allocate the index

The allocation of data can be controlled using the <<index-routing-allocation-enable-setting, enable 
allocation configuration>>.
In certain circumstances users might want to temporarily disable or restrict the
allocation of data. 

Forgetting to re-allow all data allocation can lead to unassigned shards.

In order to (re)allow all data to be allocated follow these steps:

In order to get the shards assigned we'll need to change the value of the 
configuration that restricts the 
assignemnt of the shards to `all`.

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

. Inspect the `index.routing.allocation.enable` index setting 
for the index with unassigned shards:
```console
GET /my-index-000001/_settings/index.routing.allocation.enable?flat_settings
```
The response will look like this:
```console-result
{
  "my-index-000001": {
    "settings": {
      "index.routing.allocation.enable": "none" <1>
    }
  }
}
```

<1> Represents the current configured value that controls if the index is allowed 
to be partially or totally allocated.

. Change the configuration 
value to allow the index to be fully allocated:
```console
PUT /my-index-000001/_settings
{
  "index" : {
    "routing.allocation.enable" : "all" <1>
  }
}
```

<1> The new value for the `allocation.enable` configuration for the `my-index-000001` index
is changed to allow all the shards to be allocated. 

In order to get the shards assigned we'll need to change the value of the 
configuration that restricts the 
assignemnt of the shards to `all`.

. Inspect the `index.routing.allocation.enable` index setting 
for the index with unassigned shards:
```console
GET /my-index-000001/_settings/index.routing.allocation.enable?flat_settings
```
The response will look like this:
```console-result
{
  "my-index-000001": {
    "settings": {
      "index.routing.allocation.enable": "none" <1>
    }
  }
}
```

<1> Represents the current configured value that controls if the index is allowed 
to be partially or totally allocated.

. Change the configuration 
value to allow the index to be fully allocated:
```console
PUT /my-index-000001/_settings
{
  "index" : {
    "routing.allocation.enable" : "all" <1>
  }
}
```

<1> The new value for the `allocation.enable` configuration for the `my-index-000001` index
is changed to allow all the shards to be allocated.
