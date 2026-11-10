<!-- Converted from ilm/actions/ilm-allocate.asciidoc (AsciiDoc). Includes are inlined. -->

### Allocate

Phases allowed: warm, cold.

Updates the index settings to change which nodes are allowed to host the index shards
and change the number of replicas.

The allocate action is not allowed in the hot phase.
The initial allocation for the index must be done manually or via
index templates.

You can configure this action to modify both the allocation rules and number of replicas,
only the allocation rules, or only the number of replicas.
For more information about how Elasticsearch uses replicas for scaling, see
scalability. See shard-allocation-filtering for more information about
controlling where Elasticsearch allocates shards of a particular index.

#### Options

You must specify the number of replicas or at least one
`include`, `exclude`, or `require` option.
An empty allocate action is invalid.

For more information about using custom attributes for shard allocation,
see shard-allocation-filtering.

`number_of_replicas`::
(Optional, integer)
Number of replicas to assign to the index.

`total_shards_per_node`::
(Optional, integer)
The maximum number of shards for the index on a single Elasticsearch node. A value of `-1` is
interpreted as unlimited. See total shards.

`include`::
(Optional, object)
Assigns an index to nodes that have at least _one_ of the specified custom attributes.

`exclude`::
(Optional, object)
Assigns an index to nodes that have _none_ of the specified custom attributes.

`require`::
(Optional, object)
Assigns an index to nodes that have _all_ of the specified custom attributes.

#### Example

The allocate action in the following policy changes the index's number of replicas to `2`.
No more than 200 shards for the index will be placed on any single node. Otherwise the index
allocation rules are not changed.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "allocate" : {
            "number_of_replicas" : 2,
            "total_shards_per_node" : 200
          }
        }
      }
    }
  }
}
```

##### Assign index to nodes using a custom attribute

The allocate action in the following policy assigns the index to nodes
that have a `box_type` of _hot_ or _warm_.

To designate a node's `box_type`, you set a custom attribute in the node configuration.
For example, set `node.attr.box_type: hot` in `elasticsearch.yml`.
For more information, see index-allocation-filters.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "allocate" : {
            "include" : {
              "box_type": "hot,warm"
            }
          }
        }
      }
    }
  }
}
```

##### Assign index to nodes based on multiple attributes

The allocate action can also assign indices to nodes based on multiple node
attributes. The following action assigns indices based on the `box_type` and
`storage` node attributes.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "cold": {
        "actions": {
          "allocate" : {
            "require" : {
              "box_type": "cold",
              "storage": "high"
            }
          }
        }
      }
    }
  }
}
```

##### Assign index to a specific node and update replica settings

The allocate action in the following policy updates the index to have one replica per shard
and be allocated to nodes that have a `box_type` of _cold_.

To designate a node's `box_type`, you set a custom attribute in the node configuration.
For example, set `node.attr.box_type: cold` in `elasticsearch.yml`.
For more information, see index-allocation-filters.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "actions": {
          "allocate" : {
            "number_of_replicas": 1,
            "require" : {
              "box_type": "cold"
            }
        }
        }
      }
    }
  }
}
```
