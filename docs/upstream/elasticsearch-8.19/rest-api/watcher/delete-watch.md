<!-- Converted from rest-api/watcher/delete-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete watch API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Removes a watch from Watcher.

#### Request

`DELETE _watcher/watch/<watch_id>`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Description

When the watch is removed, the document representing the watch in the `.watches`
index is gone and it will never be run again.

Please note that deleting a watch **does not** delete any watch execution records
related to this watch from the watch history.

**Important:** Deleting a watch must be done via this API only. Do not delete the
            watch directly from the `.watches` index using the Elasticsearch
            DELETE Document API. When Elasticsearch security features are enabled, make
            sure no `write` privileges are granted to anyone over the `.watches`
            index.

#### Path parameters

`<watch_id>`::
  (Required, string) Identifier for the watch.

#### Examples

The following example deletes a watch with the `my-watch` id:

```console
DELETE _watcher/watch/my_watch
```

Response:

```console-result
{
   "found": true,
   "_id": "my_watch",
   "_version": 2
}
```
