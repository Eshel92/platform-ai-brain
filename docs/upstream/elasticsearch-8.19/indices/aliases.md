<!-- Converted from indices/aliases.asciidoc (AsciiDoc). Includes are inlined. -->

### Aliases API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Performs one or more alias actions in a single atomic operation.

```console
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "my-data-stream",
        "alias": "my-alias"
      }
    }
  ]
}
```

#### Request

`POST _aliases`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the following
index privileges:

** To use the `add` or `remove` action, you must have the `manage` index
privilege for the alias and its data streams or indices.

** To use the `remove_index` action, you must have the `manage` index privilege
for the index.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`actions`::
(Required, array of objects) Actions to perform.
**Properties of `actions` objects**
`<action>`::
(Required, object) The key is the action type. At least one action is required.
**Valid `<action>` keys**
=====
`add`::
Adds a data stream or index to an alias. If the alias doesn't exist, the `add`
action creates it.

`remove`::
Removes a data stream or index from an alias.

`remove_index`::
Deletes an index. You cannot use this action on aliases or data streams.
=====
The object body contains options for the alias. Supports an empty object.
**Properties of `<action>`**
=====
`alias`::
(Required*, string) Alias for the action. Index alias names support
date math. If `aliases` is not specified, the `add`
and `remove` actions require this parameter. For the `remove` action, this
parameter supports wildcards (`*`). The `remove_index` action doesn't support
this parameter.

`aliases`::
(Required*, array of strings) Aliases for the action. Index alias names support
date math. If `alias` is not specified, the `add` and
`remove` actions require this parameter. For the `remove` action, this parameter
supports wildcards (`*`). The `remove_index` action doesn't support this
parameter.

`filter`::
(Optional, Query DSL object Query used to limit documents the
alias can access.
Only the `add` action supports this parameter.

`index`::
(Required*, string) Data stream or index for the action. Supports wildcards
(`*`). If `indices` is not specified, this parameter is required. For the `add`
and `remove_index` actions, wildcard patterns that match both data streams and
indices return an error.

`indices`::
(Required*, array of strings) Data streams or indices for the action. Supports
wildcards (`*`). If `index` is not specified, this parameter is required. For
the `add` and `remove_index` actions, wildcard patterns that match both data
streams and indices return an error.

`index_routing`::
(Optional, string) Value used to route indexing operations to a specific shard.
If specified, this overwrites the `routing` value for indexing operations. Data
stream aliases don't support this parameter.
Only the `add` action supports this parameter.

`is_hidden`::
(Optional, Boolean) If `true`, the alias is hidden. Defaults to
`false`. All data streams or indices for the alias must have the same
`is_hidden` value.
Only the `add` action supports this parameter.

`is_write_index`::
(Optional, Boolean) If `true`, sets the write index or data stream for the
alias.
If an alias points to multiple indices or data streams and `is_write_index`
isn't set, the alias rejects write requests. If an index alias points to one
index and `is_write_index` isn't set, the index automatically acts as the write
index. Data stream aliases don't automatically set a write data stream, even if
the alias points to one data stream.
Only the `add` action supports this parameter.

`must_exist`::
(Optional, Boolean)
Affects the behavior when attempting to remove an alias which does not exist.
If `true`, removing an alias which does not exist will cause all actions to fail.
If `false`, removing an alias which does not exist will only cause that removal to fail.
Defaults to `false`.
Only the `remove` action supports this parameter.

`routing`::
(Optional, string) Value used to route indexing and search operations to a
specific shard. Data stream aliases don't support this parameter.
Only the `add` action supports this parameter.

`search_routing`::
(Optional, string) Value used to route search operations to a specific shard. If
specified, this overwrites the `routing` value for search operations. Data
stream aliases don't support this parameter.
Only the `add` action supports this parameter.
=====

#### Response body

`acknowledged`::
(Boolean)
If `true`, the request received a response from the master node within the
`timeout` period.

`errors`::
(Boolean)
If `true`, at least one of the requested actions failed.

`action_results`::
(Optional, array of objects) Results for each requested action.
**Properties of `action_results` objects**

`action`::
(object)
Description of the associated action request.
**Properties of `action` object**
=====
`type`::
(string) The type of the associated action, one of `add`, `remove`, or `remove_index`.

`indices`::
(array of strings) List of indices in the associated action.

`aliases`::
(array of strings) List of aliases in the associated action.
=====

`status`::
(integer) HTTP status code returned for the action.

`error`::
(Optional, object) Contains additional information about the failed action.
Only present if the action failed.
