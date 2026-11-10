<!-- Converted from how-to/use-elasticsearch-for-time-series-data.asciidoc (AsciiDoc). Includes are inlined. -->

## Use Elasticsearch for time series data

Elasticsearch offers features to help you store, manage, and search time series data,
such as logs and metrics. Once in Elasticsearch, you can analyze and visualize your data
using Kibana and other Elastic Stack features.

### Set up data tiers

Elasticsearch's ILM feature uses <<data-tiers,data
tiers>> to automatically move older data to nodes with less expensive hardware
as it ages. This helps improve performance and reduce storage costs.

The hot and content tiers are required. The warm, cold, and frozen tiers are
optional.

Use high-performance nodes in the hot and warm tiers for faster
indexing and faster searches on your most recent data. Use slower, less
expensive nodes in the cold and frozen tiers to reduce costs.

The content tier is not typically used for time series data. However, it's
required to create system indices and other indices that aren't part of a data
stream.

The steps for setting up data tiers vary based on your deployment type:

. Log in to the {ess-trial}[Elasticsearch Service Console].

. Add or select your deployment from the Elasticsearch Service home page or the deployments
page.

. From your deployment menu, select **Edit deployment**.

. To enable a data tier, click **Add capacity**.

**Enable autoscaling**

{cloud}/ec-autoscaling.html[Autoscaling] automatically adjusts your deployment's
capacity to meet your storage needs. To enable autoscaling, select **Autoscale
this deployment** on the **Edit deployment** page. Autoscaling is only available
for Elasticsearch Service.

To assign a node to a data tier, add the respective node role to
the node's `elasticsearch.yml` file. Changing an existing node's roles requires
a rolling restart.

```yaml
# Content tier
node.roles: [ data_content ]

# Hot tier
node.roles: [ data_hot ]

# Warm tier
node.roles: [ data_warm ]

# Cold tier
node.roles: [ data_cold ]

# Frozen tier
node.roles: [ data_frozen ]
```

We recommend you use dedicated nodes in the frozen tier. If needed, you can
assign other nodes to more than one tier.

```yaml
node.roles: [ data_content, data_hot, data_warm ]
```

Assign your nodes any other roles needed for your cluster. For example, a small
cluster may have nodes with multiple roles.

```yaml
node.roles: [ master, ingest, ml, data_hot, transform ]
```

### Register a snapshot repository

The cold and frozen tiers can use {search-snaps} to
reduce local storage costs.

To use {search-snaps}, you must register a supported snapshot repository. The
steps for registering this repository vary based on your deployment type and
storage provider:

When you create a cluster, Elasticsearch Service automatically registers a default
{cloud}/ec-snapshot-restore.html[`found-snapshots`] repository. This repository
supports {search-snaps}.

The `found-snapshots` repository is specific to your cluster. To use another
cluster's default repository, refer to the Cloud
{cloud}/ec-snapshot-restore.html[Snapshot and restore] documentation.

You can also use any of the following custom repository types with {search-snaps}:

* {cloud}/ec-gcs-snapshotting.html[Google Cloud Storage (GCS)]
* {cloud}/ec-azure-snapshotting.html[Azure Blob Storage]
* {cloud}/ec-aws-custom-repository.html[Amazon Web Services (AWS)]

Use any of the following repository types with searchable snapshots:

* AWS S3
* Google Cloud Storage
* Azure Blob Storage
* {plugins}/repository-hdfs.html[Hadoop Distributed File Store (HDFS)]
* Shared filesystems such as NFS
* Read-only HTTP and HTTPS repositories

You can also use alternative implementations of these repository types, for
instance MinIO, as long as they are fully compatible.
Use the repo-analysis-api API to analyze your repository's suitability for
use with searchable snapshots.

### Create or edit an index lifecycle policy

A data stream stores your data across multiple backing
indices. ILM uses an index lifecycle policy to
automatically move these indices through your data tiers.

If you use Fleet or Elastic Agent, edit one of Elasticsearch's built-in lifecycle policies.
If you use a custom application, create your own policy. In either case,
ensure your policy:

* Includes a phase for each data tier you've configured.
* Calculates the threshold, or `min_age`, for phase transition from rollover.
* Uses {search-snaps} in the cold and frozen phases, if wanted.
* Includes a delete phase, if needed.

Fleet and Elastic Agent use the following built-in lifecycle policies:

* `logs`
* `metrics`
* `synthetics`

You can customize these policies based on your performance, resilience, and
retention requirements.

To edit a policy in Kibana, open the main menu and go to **Stack Management >
Index Lifecycle Policies**. Click the policy you'd like to edit.

You can also use the update lifecycle policy API.

```console
PUT _ilm/policy/logs
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

To create a policy in Kibana, open the main menu and go to **Stack Management >
Index Lifecycle Policies**. Click **Create policy**.

You can also use the update lifecycle policy API.

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

**Tip:** If you use Fleet or Elastic Agent, skip to search-visualize-your-data.
Fleet and Elastic Agent use built-in templates to create data streams for you.

If you use a custom application, you need to set up your own data stream.
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

### Add data to a data stream

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

### Search and visualize your data

To explore and search your data in Kibana, open the main menu and select
**Discover**. See Kibana's [Discover documentation](https://www.elastic.co/guide/en/kibana/8.19/discover.html).

Use Kibana's **Dashboard** feature to visualize your data in a chart, table, map,
and more. See Kibana's [Dashboard documentation](https://www.elastic.co/guide/en/kibana/8.19/dashboard.html).

You can also search and aggregate your data using the <<search-search,search
API>>. Use runtime fields and <<grok,grok
patterns>> to dynamically extract data from log messages and other unstructured
content at search time.

```console
GET my-data-stream/_search
{
  "runtime_mappings": {
    "source.ip": {
      "type": "ip",
      "script": """
        String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ "message" ].value)?.sourceip;
        if (sourceip != null) emit(sourceip);
      """
    }
  },
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-1d/d",
              "lt": "now/d"
            }
          }
        },
        {
          "range": {
            "source.ip": {
              "gte": "192.0.2.0",
              "lte": "192.0.2.255"
            }
          }
        }
      ]
    }
  },
  "fields": [
    "*"
  ],
  "_source": false,
  "sort": [
    {
      "@timestamp": "desc"
    },
    {
      "source.ip": "desc"
    }
  ]
}
```

Elasticsearch searches are synchronous by default. Searches across frozen data, long time
ranges, or large datasets may take longer. Use the <<submit-async-search,async
search API>> to run searches in the background. For more search options, see
search-your-data.

```console
POST my-data-stream/_async_search
{
  "runtime_mappings": {
    "source.ip": {
      "type": "ip",
      "script": """
        String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ "message" ].value)?.sourceip;
        if (sourceip != null) emit(sourceip);
      """
    }
  },
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-2y/d",
              "lt": "now/d"
            }
          }
        },
        {
          "range": {
            "source.ip": {
              "gte": "192.0.2.0",
              "lte": "192.0.2.255"
            }
          }
        }
      ]
    }
  },
  "fields": [
    "*"
  ],
  "_source": false,
  "sort": [
    {
      "@timestamp": "desc"
    },
    {
      "source.ip": "desc"
    }
  ]
}
```
