<!-- Converted from indices/put-component-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update component template API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Creates or updates a component template. Component templates are building blocks
for constructing index templates that specify index
mappings, settings, and
aliases.

```console
PUT _component_template/template_1
{
  "template": {
    "settings": {
      "number_of_shards": 1
    },
    "mappings": {
      "_source": {
        "enabled": false
      },
      "properties": {
        "host_name": {
          "type": "keyword"
        },
        "created_at": {
          "type": "date"
        }
      }
    }
  }
}
```

```console
DELETE _component_template/template_*
```

#### Request

`PUT /_component_template/<component-template>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Description

An index template can be composed of multiple component templates.
To use a component template, specify it in an index template's `composed_of` list.
Component templates are only applied to new data streams and indices
as part of a matching index template.

Settings and mappings specified directly in the index template or the create index
request override any settings or mappings specified in a component template.

Component templates are only used during index creation. For data streams, this
includes data stream creation and the creation of a stream's backing indices.
Changes to component templates do not
affect existing indices, including a stream's backing indices.

##### Comments in component templates

You can use C-style /* */ block comments in component templates.
You can include comments anywhere in the request body,
except before the opening curly bracket.

#### Path parameters

`<component-template>`::
(Required, string)
Name of the component template to create.

**Important:**
Elasticsearch includes the following built-in component templates:

- `logs@mappings`
- `logs@settings`
- `metrics@mappings`
- `metrics@settings`
- `metrics@tsdb-settings`
- `synthetics@mapping`
- `synthetics@settings`

{fleet-guide}/fleet-overview.html[Elastic Agent] uses these templates to configure
backing indices for its data streams.
If you want to customize these templates, don't override them as they may be reset after an update.
Instead, look for a `*@custom` component template in the `composed_of` section of the managed index template.
These custom component templates allow you to customize the mappings of managed index templates,
without having to override managed index templates or component templates.
Note that the custom component templates may not exist yet.
After you create them using the indices-component-template, they'll be picked up by the index template.
See data-streams-change-mappings-and-settings on how to apply the changes to the corresponding data stream.

To avoid naming collisions with built-in and Fleet-managed component templates,
avoid using `@` as part of your own component template names.
The exception of that rule are the `*@custom` component templates that let you safely customize managed index templates.

#### Query parameters

`create`::
(Optional, Boolean)
If `true`, this request cannot replace or update existing component templates.
Defaults to `false`.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

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
end::template[]

#### Examples

##### Component template with index aliases

You can include index aliases in a component template.

```console
PUT _component_template/template_1
{
  "template": {
    "settings" : {
        "number_of_shards" : 1
    },
    "aliases" : {
        "alias1" : {},
        "alias2" : {
            "filter" : {
                "term" : {"user.id" : "kimchy" }
            },
            "routing" : "shard-1"
        },
        "{index}-alias" : {} <1>
    }
  }
}
```
<1> the `{index}` placeholder in the alias name will be replaced with the
actual index name that the template gets applied to, during index creation.

##### Applying component templates

You cannot directly apply a component template to a data stream or index.
To be applied, a component template must be included in an index template's `composed_of` list. See index-templates.

##### Component template versioning

You can use the `version` parameter to add a version number to a component template.
External systems can use these version numbers to simplify template management.

The `version` parameter is optional and not automatically generated or used by Elasticsearch.

To unset a `version`, replace the template without specifying one.

```console
PUT /_component_template/template_1
{
  "template": {
    "settings" : {
        "number_of_shards" : 1
    }
  },
  "version": 123
}
```

To check the `version`, you can use the get component template API.

##### Component template metadata

You can use the `_meta` parameter to add arbitrary metadata to a component template.
This user-defined object is stored in the cluster state,
so keeping it short is preferable.

The `_meta` parameter is optional and not automatically generated or used by Elasticsearch.

To unset `_meta`, replace the template without specifying one.

```console
PUT /_component_template/template_1
{
  "template": {
    "settings" : {
        "number_of_shards" : 1
    }
  },
  "_meta": {
    "description": "set number of shards to one",
    "serialization": {
      "class": "MyComponentTemplate",
      "id": 10
    }
  }
}
```

To check the `_meta`, you can use the get component template API.
