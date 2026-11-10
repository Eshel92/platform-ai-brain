<!-- Converted from rest-api/watcher/get-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Get watch API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Retrieves a watch by its ID.

#### Request

`GET _watcher/watch/<watch_id>`

#### Prerequisites

* You must have `manage_watcher` or `monitor_watcher` cluster privileges to use
this API. For more information, see
security-privileges.

#### Path parameters

`<watch_id>`::
  (Required, string) Identifier for the watch.

#### Examples

The following example gets a watch with `my_watch` id:

```console
GET _watcher/watch/my_watch
```

Response:

```console-result
{
  "found": true,
  "_id": "my_watch",
  "_seq_no": 0,
  "_primary_term": 1,
  "_version": 1,
  "status": { <1>
    "version": 1,
    "state": {
      "active": true,
      "timestamp": "2015-05-26T18:21:08.630Z"
    },
    "actions": {
      "test_index": {
        "ack": {
          "timestamp": "2015-05-26T18:21:08.630Z",
          "state": "awaits_successful_execution"
        }
      }
    }
  },
  "watch": {
    "input": {
      "simple": {
        "payload": {
          "send": "yes"
        }
      }
    },
    "condition": {
      "always": {}
    },
    "trigger": {
      "schedule": {
        "hourly": {
          "minute": [0, 5]
        }
      }
    },
    "actions": {
      "test_index": {
        "index": {
          "index": "test"
        }
      }
    }
  }
}
```

<1> The current status of the watch
