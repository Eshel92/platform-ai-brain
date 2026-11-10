<!-- Converted from data-streams/modify-data-streams-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Modify data streams API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Performs one or more data stream modification actions in a single atomic
operation.

```console
POST _data_stream/_modify
{
  "actions": [
    {
      "remove_backing_index": {
        "data_stream": "my-logs",
        "index": ".ds-my-logs-2099.01.01-000001"
      }
    },
    {
      "add_backing_index": {
        "data_stream": "my-logs",
        "index": "index-to-add"
      }
    }
  ]
}
```

#### Request

`POST /_data_stream/_modify`

#### Request body

`actions`::
(Required, array of objects) Actions to perform.
**Properties of `actions` objects**
`<action>`::
(Required, object) The key is the action type. At least one action is required.
**Valid `<action>` keys**
=====
`add_backing_index`::
Adds an existing index as a backing index for a data stream. The index is
hidden as part of this operation.

**Warning:** Adding indices with the `add_backing_index` action
can potentially result in improper data stream behavior.
This should be considered an expert level API.

`remove_backing_index`::
Removes a backing index from a data stream. The index is unhidden
as part of this operation. A data stream's write index cannot be removed.

=====
The object body contains options for the action.
**Properties of `<action>`**
=====
`data_stream`::
(Required*, string) Data stream targeted by the action.

`index`::
(Required*, string) Index for the action.
=====
