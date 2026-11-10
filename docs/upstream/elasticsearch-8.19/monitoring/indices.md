<!-- Converted from monitoring/indices.asciidoc (AsciiDoc). Includes are inlined. -->

## Configuring data streams/indices for monitoring

Monitoring data is stored in data streams or indices in Elasticsearch. The default data
stream or index settings may not work for your situation. For example, you might
want to change index lifecycle management (ILM) settings, add custom mappings,
or change the number of shards and replicas. The steps to change these
settings depend on the monitoring method:

* config-monitoring-data-streams-elastic-agent
* config-monitoring-data-streams-metricbeat-8 (the default for version 8 
Elasticsearch Service deployments on Elastic Cloud)
* config-monitoring-indices-metricbeat-7-internal-collection 

**Important:** Changing mappings or settings can cause your monitoring dashboards to
stop working correctly.

### Configuring data streams created by Elastic Agent

When monitoring using Elastic Agent, data is stored in a
set of data streams named
`metrics-{product}.stack_monitoring.{dataset}-{namespace}`. For example:
`metrics-elasticsearch.stack_monitoring.shard-default`. 

The settings and mappings for these data streams are determined by an index
template named `metrics-{product}.stack_monitoring.{dataset}`. For example:
`metrics-elasticsearch.stack_monitoring.shard`. 

To change the settings of each data stream, edit the
`metrics-{product}.stack_monitoring.{dataset}@custom` component template that
already exists. You can do this in Kibana:

* Navigate to *Stack Management* > *Index Management* > *Component Templates*.
* Search for the component template.
* Select the *Edit* action.

You can also use the Elasticsearch API:

* Retrieve the component template using the <<getting-component-templates,get 
component template API>>.
* Edit the component template.
* Store the updated component template using the <<indices-component-template,
update component template API>>.

After changing the component template, the updated settings are only applied
to the data stream's new backing indices.
Roll over the data stream to immediately
apply the updated settings to the data stream’s write index.

### Configuring data streams created by {metricbeat} 8

When monitoring using {metricbeat} 8, data is stored
in a set of data streams called `.monitoring-{product}-8-mb`. For example:
`.monitoring-es-8-mb`. 

The settings and mappings for these data streams are determined by an index
template named `.monitoring-{product}-mb`. For example: `.monitoring-es-mb`. You
can alter the settings of each data stream by cloning this index template and
editing it. 

**Warning:** You need to repeat this procedure when upgrading the Elastic Stack to get the
latest updates to the default monitoring index templates.

You can clone index templates in Kibana:

* Navigate to *Stack Management* > *Index Management* > *Index Templates*.
* From the *View* dropdown, select *System templates*.
* Search for the index template.
* Select the *Clone* action.
* Change the name, for example into `custom_monitoring`.
* Set the priority to `500`, to ensure it overrides the default index template.
* Specify the settings you want to change in the `settings` section.
* Save the cloned template.

You can also use the Elasticsearch API:

* Retrieve the index template using the <<indices-get-template,get index 
template API>>.
* Edit the index template: set the template `priority` to `500`, and specify the 
settings you want to change in the `settings` section.
* Store the updated index template under a different name, for example 
`custom_monitoring`, using the 
create index template API.

**Note:** {metricbeat} 8 uses composable templates, rather than
legacy templates.

After changing the index template, the updated settings are only applied to the
data stream's new backing indices.
Roll over the data stream to immediately
apply the updated settings to the data stream’s write index.

### Configuring indices created by {metricbeat} 7 or internal collection

When monitoring using {metricbeat} 7 or
{filebeat-ref}/monitoring-internal-collection.html[internal collection], data is
stored in a set of indices called either:

* `.monitoring-{product}-7-mb-{date}`, when using {metricbeat} 7.
* `.monitoring-{product}-7-{date}`, when using internal collection.

The settings and mappings for these indices are determined by
legacy index templates named `.monitoring-{product}`.
You can retrieve these templates in Kibana by navigating to *Stack Management* >
*Index Management* > *Index Templates*, or by using the Elasticsearch `_template` API:

```console
GET /_template/.monitoring-*
```

To change the settings of the indices, add a custom index template. You can do 
that in Kibana, or using the Elasticsearch API:

* Set `index_patterns` to match the `.monitoring-{product}-7-*` indices.
* Set the template `order` to `1`. This ensures your template is
applied after the default template, which has an order of 0.
* Specify the `number_of_shards` and/or `number_of_replicas` in the `settings`
section.

```console
PUT /_template/custom_monitoring
{
  "index_patterns": [".monitoring-beats-7-*", ".monitoring-es-7-*", ".monitoring-kibana-7-*", ".monitoring-logstash-7-*"],
  "order": 1,
  "settings": {
    "number_of_shards": 5,
    "number_of_replicas": 2
  }
}
```

After changing the index template, the updated settings are only applied to new
indices.
