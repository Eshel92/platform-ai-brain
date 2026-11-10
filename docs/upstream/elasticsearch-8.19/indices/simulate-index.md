<!-- Converted from indices/simulate-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Simulate index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Returns the index configuration that would be applied to the specified index from an
existing index template.

```console
POST /_index_template/_simulate_index/my-index-000001
```

#### Request

`POST /_index_template/_simulate_index/<index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_index_templates` or `manage` <<privileges-list-cluster,cluster
privilege>> to use this API.

#### Path parameters

`<index>`::
(Required, string)
Name of the index to simulate. 

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`include_defaults`::
(Optional, Boolean) Functionality in preview:[]. If `true`, return all default settings in the response.
Defaults to `false`.

#### Response body

`overlapping`::
(array) Any templates that also matched the index but were superseded by a higher-priority template.
Response includes an empty array if there are no overlapping templates. 
**Properties of `overlapping`**
`name`::
(string) Name of the superseded template.

`index_patterns`:: 
(array) Index patterns that the superseded template applies to.

`template`::
(object)
The settings, mappings, and aliases that would be applied to the index. 
**Properties of `template`**
`aliases`::
(object) Aliases for the index. If no aliases apply, the response returns an
empty `aliases` object.
=====
`<alias>`::
(object) The key is the alias name. The object body contains options for the
alias.
**Properties of `<alias>`**
======
`filter`::
(Query DSL object) Query used to limit documents the alias can
access.

`index_routing`::
(string) Value used to route indexing operations to a specific shard. This
overwrites the `routing` value for indexing operations.

`is_hidden`::
(Boolean) If `true`, the alias is hidden.

`is_write_index`::
(Boolean) If `true`, the index is the write index for the alias.

`routing`::
(string) Value used to route indexing and search operations to a specific shard.

`search_routing`::
(string) Value used to route search operations to a specific shard. This
overwrites the `routing` value for search operations.
======
=====

`mappings`::
(Optional, mapping object) Mapping for fields in the index. If
specified, this mapping can include:

* Field names
* Field data types
* Mapping parameters

See mapping.
Omitted from the response if no mappings would be applied.

`settings`::
(Optional, index setting object) Configuration
options for the index. See index-modules-settings.
Response includes an empty object if no settings would be applied. 

#### Examples

The following example shows the configuration that would be applied to `my-index-000001` by 
an existing template.

```console
PUT /_component_template/ct1                    <1>
{
  "template": {
    "settings": {
      "index.number_of_shards": 2
    }
  }
}

PUT /_component_template/ct2                    <2>
{
  "template": {
    "settings": {
      "index.number_of_replicas": 0
    },
    "mappings": {
      "properties": {
        "@timestamp": {
          "type": "date"
        }
      }
    }
  }
}

PUT /_index_template/final-template             <3>
{
  "index_patterns": ["my-index-*"],
  "composed_of": ["ct1", "ct2"],
  "priority": 5
}

POST /_index_template/_simulate_index/my-index-000001 <4>
```
<1> Create a component template (`ct1`) that sets the number of shards to 2
<2> Create a second component template (`ct2`) that sets the number of replicas to 0 and defines a mapping
<3> Create an index template (`final-template`) that uses the component templates
<4> Show the configuration that would be applied to `my-index-000001`

The response shows the index settings, mappings, and aliases applied by the `final-template`:

```console-result
{
  "template" : {
    "settings" : {
      "index" : {
        "number_of_shards" : "2",
        "number_of_replicas" : "0",
        "routing" : {
          "allocation" : {
            "include" : {
              "_tier_preference" : "data_content"
            }
          }
        }
      }
    },
    "mappings" : {
      "properties" : {
        "@timestamp" : {
          "type" : "date"
        }
      }
    },
    "aliases" : { }
  },
  "overlapping" : [
    {
      "name" : "template_1",
      "index_patterns" : [
        "my-index-*"
      ]
    }
  ]
}
```
