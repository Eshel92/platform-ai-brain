<!-- Converted from ingest/apis/simulate-ingest.asciidoc (AsciiDoc). Includes are inlined. -->

### Simulate ingest API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Executes ingest pipelines against a set of provided documents, optionally
with substitute pipeline definitions. This API is meant to be used for
troubleshooting or pipeline development, as it does not actually index any
data into Elasticsearch.

```console
POST /_ingest/_simulate
{
  "docs": [
    {
      "_index": "my-index",
      "_id": "id",
      "_source": {
        "foo": "bar"
      }
    },
    {
      "_index": "my-index",
      "_id": "id",
      "_source": {
        "foo": "rab"
      }
    }
  ],
  "pipeline_substitutions": { <1>
    "my-pipeline": {
      "processors": [
        {
          "set": {
            "field": "field3",
            "value": "value3"
          }
        }
      ]
    }
  },
  "component_template_substitutions": { <2>
    "my-component-template": {
      "template": {
        "mappings": {
          "dynamic": "true",
          "properties": {
            "field3": {
              "type": "keyword"
            }
          }
        },
        "settings": {
          "index": {
            "default_pipeline": "my-pipeline"
          }
        }
      }
    }
  },
  "index_template_substitutions": { <3>
    "my-index-template": {
      "index_patterns": ["my-index-*"],
      "composed_of": ["component_template_1", "component_template_2"]
    }
  },
  "mapping_addition": { <4>
    "dynamic": "strict",
    "properties": {
      "foo": {
        "type": "keyword"
      }
    }
  }
}
```

<1> This replaces the existing `my-pipeline` pipeline with the contents given here for the duration of this request.
<2> This replaces the existing `my-component-template` component template with the contents given here for the duration of this request.
These templates can be used to change the pipeline(s) used, or to modify the mapping that will be used to validate the result.
<3> This replaces the existing `my-index-template` index template with the contents given here for the duration of this request.
These templates can be used to change the pipeline(s) used, or to modify the mapping that will be used to validate the result.
<4> This mapping is merged into the index's final mapping just before validation. It is used only for the duration of this request.

#### Request

`POST /_ingest/_simulate`

`GET /_ingest/_simulate`

`POST /_ingest/<target>/_simulate`

`GET /_ingest/<target>/_simulate`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`index` or `create` index privileges
to use this API.

#### Description

The simulate ingest API simulates ingesting data into an index. It
executes the default and final pipeline for that index against a set
of documents provided in the body of the request. If a pipeline
contains a reroute processor, it follows that
reroute processor to the new index, executing that index's pipelines
as well the same way that a non-simulated ingest would. No data is
indexed into Elasticsearch. Instead, the transformed document is returned,
along with the list of pipelines that have been executed and the name
of the index where the document would have been indexed if this were
not a simulation. The transformed document is validated against the
mappings that would apply to this index, and any validation error is
reported in the result.

This API differs from the
simulate pipeline API in that you specify a
single pipeline for that API, and it only runs that one pipeline. The
simulate pipeline API is more useful for developing a single pipeline,
while the simulate ingest API is more useful for troubleshooting the
interaction of the various pipelines that get applied when ingesting
into an index.

By default, the pipeline definitions that are currently in the system
are used. However, you can supply substitute pipeline definitions in the
body of the request. These will be used in place of the pipeline
definitions that are already in the system. This can be used to replace
existing pipeline definitions or to create new ones. The pipeline
substitutions are only used within this request.

#### Path parameters

`<target>`::
(Optional, string)
The index to simulate ingesting into. This can be overridden by specifying an index
on each document. If you provide a <target> in the request path, it is used for any
documents that don’t explicitly specify an index argument.

#### Query parameters

`pipeline`::
(Optional, string)
Pipeline to use as the default pipeline. This can be used to override the default pipeline
of the index being ingested into.

#### Request body

`docs`::
(Required, array of objects)
Sample documents to test in the pipeline.
**Properties of `docs` objects**
`_id`::
(Optional, string)
Unique identifier for the document.

`_index`::
(Optional, string)
Name of the index that the document will be ingested into.

`_source`::
(Required, object)
JSON body for the document.

`pipeline_substitutions`::
(Optional, map of strings to objects)
Map of pipeline IDs to substitute pipeline definition objects.
**Properties of pipeline definition objects**
`description`::
(Optional, string)
Description of the ingest pipeline.

`on_failure`::
(Optional, array of processor objects)
Processors to run immediately after a processor failure.
Each processor supports a processor-level `on_failure` value. If a processor
without an `on_failure` value fails, Elasticsearch uses this pipeline-level parameter as
a fallback. The processors in this parameter run sequentially in the order
specified. Elasticsearch will not attempt to run the pipeline's remaining processors.

`processors`::
(Required, array of processor objects)
Processors used to perform transformations on documents before indexing.
Processors run sequentially in the order specified.

`version`::
(Optional, integer)
Version number used by external systems to track ingest pipelines.
See the `if_version` parameter above for
how the version attribute is used.

`_meta`::
(Optional, object)
Optional metadata about the ingest pipeline. May have any contents. This
map is not automatically generated by Elasticsearch.

`deprecated`::
(Optional, boolean)
Marks this ingest pipeline as deprecated.
When a deprecated ingest pipeline is referenced as the default or final pipeline when creating or updating a non-deprecated index template,
Elasticsearch will emit a deprecation warning.

`component_template_substitutions`::
(Optional, map of strings to objects)
Map of component template names to substitute component template definition objects.
**Properties of component template definition objects**

`template`::
(Required, object)
This is the template to be applied, may optionally include a `mappings`,
`settings`, or `aliases` configuration.
**Properties of `template`**
=====
`aliases`::
(Optional, object of objects) Aliases to add.
If the index template includes a `data_stream` object, these are data stream
aliases. Otherwise, these are index aliases. Data stream aliases ignore the
`index_routing`, `routing`, and `search_routing` options.
**Properties of `aliases` objects**
=======
`<alias>`::
(Required, object) The key is the alias name. Index alias names support
date math.
The object body contains options for the alias. Supports an empty object.
**Properties of `<alias>`**
======
`filter`::
(Optional, Query DSL object) Query used to limit documents the
alias can access.

`index_routing`::
(Optional, string) Value used to route indexing operations to a specific shard.
If specified, this overwrites the `routing` value for indexing operations.

`is_hidden`::
(Optional, Boolean) If `true`, the alias is hidden. Defaults to
`false`. All indices for the alias must have the same `is_hidden` value.

`is_write_index`::
(Optional, Boolean) If `true`, the index is the write index for
the alias. Defaults to `false`.

`routing`::
(Optional, string) Value used to route indexing and search operations to a
specific shard.

`search_routing`::
(Optional, string) Value used to route search operations to a specific shard. If
specified, this overwrites the `routing` value for search operations.
======
=======
`mappings`::
(Optional, mapping object) Mapping for fields in the index. If
specified, this mapping can include:

* Field names
* Field data types
* Mapping parameters

See mapping.
`settings`::
(Optional, index setting object) Configuration
options for the index. See index-modules-settings.
=====

`version`::
(Optional, integer)
Version number used to manage component templates externally.
This number is not automatically generated or incremented by Elasticsearch.

`allow_auto_create`::
(Optional, Boolean)
This setting overrides the value of the
`action.auto_create_index` cluster setting. If set to
`true` in a template, then indices can be automatically created using that
template even if auto-creation of indices is disabled via
`actions.auto_create_index`. If set to `false`, then indices or data streams matching the
template must always be explicitly created, and may never be automatically
created.

`_meta`::
(Optional, object)
Optional user metadata about the component template. May have any contents.
This map is not automatically generated by Elasticsearch.

`deprecated`::
(Optional, boolean)
Marks this component template as deprecated.
When a deprecated component template is referenced when creating or updating a non-deprecated index template,
Elasticsearch will emit a deprecation warning.

`index_template_substitutions`::
(Optional, map of strings to objects)
Map of index template names to substitute index template definition objects.
**Properties of index template definition objects**

`composed_of`::
(Optional, array of strings)
An ordered list of component template names. Component templates are merged in the order
specified, meaning that the last component template specified has the highest precedence. See
Composing multiple component templates for an example.

`data_stream`::
(Optional, object)
If this object is included, the template is used to create data streams and
their backing indices. Supports an empty object.
Data streams require a matching index template with a `data_stream` object.
See create an index template.
**Properties of `data_stream`**
=====
`allow_custom_routing`::
(Optional, Boolean) If `true`, the data stream supports
custom routing. Defaults to `false`.

`hidden`::
(Optional, Boolean) If `true`, the data stream is hidden. Defaults to
`false`.

`index_mode`::
(Optional, string) Type of data stream to create. Valid values are `null`
(standard data stream), `time_series` (time series data stream) and `logsdb` 
(logs data stream).
The template's `index_mode` sets the `index.mode` of the backing index.
=====

`index_patterns`::
(Required, array of strings)
Array of wildcard (`*`) expressions
used to match the names of data streams and indices during creation.
Elasticsearch includes several built-in index templates. To avoid naming collisions with
these templates, see avoid-index-pattern-collisions.

`_meta`::
(Optional, object)
Optional user metadata about the index template. May have any contents.
This map is not automatically generated by Elasticsearch.

`priority`::
(Optional, integer)
Priority to determine index template precedence when a new data stream or index is created. The index template with
the highest priority is chosen. If no priority is specified the template is treated as though it is
of priority 0 (lowest priority).
This number is not automatically generated by Elasticsearch.

`template`::
(Optional, object)
Template to be applied. It may optionally include an `aliases`, `mappings`, or
`settings` configuration.
**Properties of `template`**
=====
`aliases`::
(Optional, object of objects) Aliases to add.
If the index template includes a `data_stream` object, these are data stream
aliases. Otherwise, these are index aliases. Data stream aliases ignore the
`index_routing`, `routing`, and `search_routing` options.
**Properties of `aliases` objects**
=======
`<alias>`::
(Required, object) The key is the alias name. Index alias names support
date math.
The object body contains options for the alias. Supports an empty object.
**Properties of `<alias>`**
======
`filter`::
(Optional, Query DSL object) Query used to limit documents the
alias can access.

`index_routing`::
(Optional, string) Value used to route indexing operations to a specific shard.
If specified, this overwrites the `routing` value for indexing operations.

`is_hidden`::
(Optional, Boolean) If `true`, the alias is hidden. Defaults to
`false`. All indices for the alias must have the same `is_hidden` value.

`is_write_index`::
(Optional, Boolean) If `true`, the index is the write index for
the alias. Defaults to `false`.

`routing`::
(Optional, string) Value used to route indexing and search operations to a
specific shard.

`search_routing`::
(Optional, string) Value used to route search operations to a specific shard. If
specified, this overwrites the `routing` value for search operations.
======
=======
`mappings`::
(Optional, mapping object) Mapping for fields in the index. If
specified, this mapping can include:

* Field names
* Field data types
* Mapping parameters

See mapping.
`settings`::
(Optional, index setting object) Configuration
options for the index. See index-modules-settings.
=====

`version`::
(Optional, integer)
Version number used to manage index templates externally.
This number is not automatically generated by Elasticsearch.

`deprecated`::
(Optional, boolean)
Marks this index template as deprecated.
When creating or updating a non-deprecated index template that uses deprecated components,
Elasticsearch will emit a deprecation warning.

`mapping_addition`::
(Optional, mapping object)
Definition of a mapping that will be merged into the index's mapping for validation during the course of this request.

#### Examples

##### Use pre-existing pipeline definitions

In this example the index `index` has a default pipeline called `my-pipeline` and a final
pipeline called `my-final-pipeline`. Since both documents are being ingested into `index`,
both pipelines are executed using the pipeline definitions that are already in the system.

```console
POST /_ingest/_simulate
{
  "docs": [
    {
      "_index": "my-index",
      "_id": "123",
      "_source": {
        "foo": "bar"
      }
    },
    {
      "_index": "my-index",
      "_id": "456",
      "_source": {
        "foo": "rab"
      }
    }
  ]
}
```

The API returns the following response:

```console-result
{
   "docs": [
      {
         "doc": {
            "_id": "123",
            "_index": "my-index",
            "_version": -3,
            "_source": {
               "field1": "value1",
               "field2": "value2",
               "foo": "bar"
            },
            "executed_pipelines": [
               "my-pipeline",
               "my-final-pipeline"
            ]
         }
      },
      {
         "doc": {
            "_id": "456",
            "_index": "my-index",
            "_version": -3,
            "_source": {
               "field1": "value1",
               "field2": "value2",
               "foo": "rab"
            },
            "executed_pipelines": [
               "my-pipeline",
               "my-final-pipeline"
            ]
         }
      }
   ]
}
```

##### Specify a pipeline substitution in the request body

In this example the index `my-index` has a default pipeline called `my-pipeline` and a final
pipeline called `my-final-pipeline`. But a substitute definition of `my-pipeline` is
provided in `pipeline_substitutions`. The substitute `my-pipeline` will be used in place of
the `my-pipeline` that is in the system, and then the `my-final-pipeline` that is already
defined in the system will be executed.

```console
POST /_ingest/_simulate
{
  "docs": [
    {
      "_index": "my-index",
      "_id": "123",
      "_source": {
        "foo": "bar"
      }
    },
    {
      "_index": "my-index",
      "_id": "456",
      "_source": {
        "foo": "rab"
      }
    }
  ],
  "pipeline_substitutions": {
    "my-pipeline": {
      "processors": [
        {
          "uppercase": {
            "field": "foo"
          }
        }
      ]
    }
  }
}
```

The API returns the following response:

```console-result
{
   "docs": [
      {
         "doc": {
            "_id": "123",
            "_index": "my-index",
            "_version": -3,
            "_source": {
               "field2": "value2",
               "foo": "BAR"
            },
            "executed_pipelines": [
               "my-pipeline",
               "my-final-pipeline"
            ]
         }
      },
      {
         "doc": {
            "_id": "456",
            "_index": "my-index",
            "_version": -3,
            "_source": {
               "field2": "value2",
               "foo": "RAB"
            },
            "executed_pipelines": [
               "my-pipeline",
               "my-final-pipeline"
            ]
         }
      }
   ]
}
```

##### Specify a component template substitution in the request body

In this example, imagine that the index `my-index` has a strict mapping with only the `foo`
keyword field defined. Say that field mapping came from a component template named
`my-mappings-template`. We want to test adding a new field, `bar`. So a substitute definition of
`my-mappings-template` is provided in `component_template_substitutions`. The substitute
`my-mappings-template` will be used in place of the existing mapping for `my-index` and in place
of the `my-mappings-template` that is in the system.

```console
POST /_ingest/_simulate
{
  "docs": [
    {
      "_index": "my-index",
      "_id": "123",
      "_source": {
        "foo": "foo"
      }
    },
    {
      "_index": "my-index",
      "_id": "456",
      "_source": {
        "bar": "rab"
      }
    }
  ],
  "component_template_substitutions": {
    "my-mappings_template": {
      "template": {
        "mappings": {
          "dynamic": "strict",
          "properties": {
            "foo": {
              "type": "keyword"
            },
            "bar": {
              "type": "keyword"
            }
          }
        }
      }
    }
  }
}
```

The API returns the following response:

```console-result
{
   "docs": [
      {
         "doc": {
            "_id": "123",
            "_index": "my-index",
            "_version": -3,
            "_source": {
               "foo": "foo"
            },
            "executed_pipelines": []
         }
      },
      {
         "doc": {
            "_id": "456",
            "_index": "my-index",
            "_version": -3,
            "_source": {
               "bar": "rab"
            },
            "executed_pipelines": []
         }
      }
   ]
}
```
