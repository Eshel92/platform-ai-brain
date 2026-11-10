<!-- Converted from data-streams/set-up-a-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

## Set up a data stream

To set up a data stream, follow these steps:

. create-index-lifecycle-policy
. create-component-templates
. create-index-template
. create-data-stream
. secure-data-stream

You can also <<convert-index-alias-to-data-stream,convert an index alias to
a data stream>>.

If you use Fleet, Elastic Agent, or Logstash, skip this tutorial. 
They all set up data streams for you. 

For Fleet and Elastic Agent, check out this {fleet-guide}/data-streams.html[data streams documentation].
For Logstash, check out the
{logstash-ref}/plugins-outputs-elasticsearch.html#plugins-outputs-elasticsearch-data_stream[data streams settings]
for the `elasticsearch output` plugin.

### Create an index lifecycle policy

While optional, we recommend using ILM to automate the management of your
data stream's backing indices. ILM requires an index lifecycle policy.

To create an index lifecycle policy in Kibana, open the main menu and go to
*Stack Management > Index Lifecycle Policies*. Click *Create policy*.

You can also use the create lifecycle policy API.

```console
PUT _ilm/policy/my-lifecycle-policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_primary_shard_size": "50gb"
          }
        }
      },
      "warm": {
        "min_age": "30d",
        "actions": {
          "shrink": {
            "number_of_shards": 1
          },
          "forcemerge": {
            "max_num_segments": 1
          }
        }
      },
      "cold": {
        "min_age": "60d",
        "actions": {
          "searchable_snapshot": {
            "snapshot_repository": "found-snapshots"
          }
        }
      },
      "frozen": {
        "min_age": "90d",
        "actions": {
          "searchable_snapshot": {
            "snapshot_repository": "found-snapshots"
          }
        }
      },
      "delete": {
        "min_age": "735d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

### Create component templates

A data stream requires a matching index template. In most cases, you compose
this index template using one or more component templates. You typically use
separate component templates for mappings and index settings. This lets you
reuse the component templates in multiple index templates.

When creating your component templates, include:

* A `date` or `date_nanos` mapping for the `@timestamp`
field. If you don't specify a mapping, Elasticsearch maps `@timestamp` as a `date` field
with default options.

* Your lifecycle policy in the `index.lifecycle.name` index setting.

**Tip:**
Use the {ecs-ref}[Elastic Common Schema (ECS)] when mapping your fields. ECS
fields integrate with several Elastic Stack features by default.

If you're unsure how to map your fields, use <<runtime-search-request,runtime
fields>> to extract fields from <<mapping-unstructured-content,unstructured
content>> at search time. For example, you can index a log message to a
`wildcard` field and later extract IP addresses and other data from this field
during a search.

To create a component template in Kibana, open the main menu and go to *Stack
Management > Index Management*. In the *Index Templates* view, click *Create
component template*.

You can also use the <<indices-component-template,create component template
API>>.

```console
# Creates a component template for mappings
PUT _component_template/my-mappings
{
  "template": {
    "mappings": {
      "properties": {
        "@timestamp": {
          "type": "date",
          "format": "date_optional_time||epoch_millis"
        },
        "message": {
          "type": "wildcard"
        }
      }
    }
  },
  "_meta": {
    "description": "Mappings for @timestamp and message fields",
    "my-custom-meta-field": "More arbitrary metadata"
  }
}

# Creates a component template for index settings
PUT _component_template/my-settings
{
  "template": {
    "settings": {
      "index.lifecycle.name": "my-lifecycle-policy"
    }
  },
  "_meta": {
    "description": "Settings for ILM",
    "my-custom-meta-field": "More arbitrary metadata"
  }
}
```

### Create an index template

Use your component templates to create an index template. Specify:

* One or more index patterns that match the data stream's name. We recommend
using our {fleet-guide}/data-streams.html#data-streams-naming-scheme[data stream
naming scheme].

* That the template is data stream enabled.

* Any component templates that contain your mappings and index settings.

* A priority higher than `200` to avoid collisions with built-in templates.
See avoid-index-pattern-collisions.

To create an index template in Kibana, open the main menu and go to *Stack
Management > Index Management*. In the *Index Templates* view, click *Create
template*.

You can also use the create index template API.
Include the `data_stream` object to enable data streams.

```console
PUT _index_template/my-index-template
{
  "index_patterns": ["my-data-stream*"],
  "data_stream": { },
  "composed_of": [ "my-mappings", "my-settings" ],
  "priority": 500,
  "_meta": {
    "description": "Template for my time series data",
    "my-custom-meta-field": "More arbitrary metadata"
  }
}
```

### Create the data stream

Indexing requests add documents to a data
stream. These requests must use an `op_type` of `create`. Documents must include
a `@timestamp` field.

To automatically create your data stream, submit an indexing request that
targets the stream's name. This name must match one of your index template's
index patterns.

```console
PUT my-data-stream/_bulk
{ "create":{ } }
{ "@timestamp": "2099-05-06T16:21:15.000Z", "message": "192.0.2.42 - - [06/May/2099:16:21:15 +0000] \"GET /images/bg.jpg HTTP/1.0\" 200 24736" }
{ "create":{ } }
{ "@timestamp": "2099-05-06T16:25:42.000Z", "message": "192.0.2.255 - - [06/May/2099:16:25:42 +0000] \"GET /favicon.ico HTTP/1.0\" 200 3638" }

POST my-data-stream/_doc
{
  "@timestamp": "2099-05-06T16:21:15.000Z",
  "message": "192.0.2.42 - - [06/May/2099:16:21:15 +0000] \"GET /images/bg.jpg HTTP/1.0\" 200 24736"
}
```

You can also manually create the stream using the
create data stream API. The stream's name must
still match one of your template's index patterns.

```console
PUT _data_stream/my-data-stream
```

### Secure the data stream

Use index privileges to control access to a data
stream. Granting privileges on a data stream grants the same privileges on its
backing indices.
For an example, see data-stream-privileges.

### Convert an index alias to a data stream

Prior to Elasticsearch 7.9, you'd typically use an
index alias with a write index
to manage time series data. Data streams replace this functionality, require
less maintenance, and automatically integrate with data tiers.

To convert an index alias with a write index to a data stream with the same
name, use the migrate to data stream API.
During conversion, the alias’s indices become hidden backing indices for the
stream. The alias’s write index becomes the stream’s write index. The stream
still requires a matching index template with data stream enabled.

```console
POST _data_stream/_migrate/my-time-series-data
```

### Get information about a data stream

To get information about a data stream in Kibana, open the main menu and go to
*Stack Management > Index Management*. In the *Data Streams* view, click the
data stream's name.

You can also use the get data stream API.

```console
GET _data_stream/my-data-stream
```

### Delete a data stream

To delete a data stream and its backing indices in Kibana, open the main menu and
go to *Stack Management > Index Management*. In the *Data Streams* view, click
the trash icon. The icon only displays if you have the `delete_index`
security privilege for the data stream.

You can also use the delete data stream API.

```console
DELETE _data_stream/my-data-stream
```
