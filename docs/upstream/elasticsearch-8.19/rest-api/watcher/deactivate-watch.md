<!-- Converted from rest-api/watcher/deactivate-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Deactivate watch API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

A watch can be either active or inactive. This
API enables you to deactivate a currently active watch.

#### Request

`PUT _watcher/watch/<watch_id>/_deactivate`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Path parameters

`<watch_id>`::
  (Required, string) Identifier for the watch.

#### Examples

The status of an active watch is returned with the watch definition when you
call the get watch API:

```console
GET _watcher/watch/my_watch
```

```console-result
{
  "found": true,
  "_id": "my_watch",
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "status": {
    "state" : {
      "active" : true,
      "timestamp" : "2015-08-20T12:21:32.734Z"
    },
    "actions": ...,
    "version": 1
  },
  "watch": ...
}
```

You can deactivate the watch by executing the following API call:

```console
PUT _watcher/watch/my_watch/_deactivate
```

The new state of the watch is returned as part of its overall status:

```console-result
{
  "status": {
    "state" : {
      "active" : false,
      "timestamp" : "2015-09-04T08:39:46.816Z"
    },
    "actions": ...,
    "version": 1
  }
}
```
