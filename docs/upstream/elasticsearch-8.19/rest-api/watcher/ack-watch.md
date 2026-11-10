<!-- Converted from rest-api/watcher/ack-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Ack watch API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Acknowledging a watch enables you
to manually throttle execution of the watch's actions.

#### Request

`PUT _watcher/watch/<watch_id>/_ack` +

`PUT _watcher/watch/<watch_id>/_ack/<action_id>`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Description

An action's _acknowledgement state_ is stored in the
`status.actions.<id>.ack.state` structure.

**Important:** If the specified watch is currently being executed, this API will
return an error. The reason for this is to prevent overwriting of the watch
status from a watch execution.

#### Path parameters

`<action_id>`::
  (Optional, list) A comma-separated list of the action IDs to acknowledge. If you omit
  this parameter, all of the actions of the watch are acknowledged.

`<watch_id>`::
  (Required, string) Identifier for the watch.

#### Examples

To demonstrate let's create a new watch:

```console
PUT _watcher/watch/my_watch
{
  "trigger" : {
    "schedule" : {
      "yearly" : { "in" : "february", "on" : 29, "at" : "noon" }
    }
  },
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
  "actions": {
    "test_index": {
      "throttle_period": "15m",
      "index": {
        "index": "test"
      }
    }
  }
}
```

The current status of a watch and the state of its actions is returned with the
watch definition when you call the Get Watch API:

```console
GET _watcher/watch/my_watch
```

The action state of a newly-created watch is `awaits_successful_execution`:

```console-result
{
  "found": true,
  "_seq_no": 0,
  "_primary_term": 1,
  "_version": 1,
  "_id": "my_watch",
  "status": {
    "version": 1,
    "actions": {
      "test_index": {
        "ack": {
          "timestamp": "2015-05-26T18:04:27.723Z",
          "state": "awaits_successful_execution"
        }
      }
    },
    "state": ...
  },
  "watch": ...
}
```

When the watch executes and the condition matches, the value of the `ack.state`
changes to `ackable`. Let's force execution of the watch and fetch it again to
check the status:

```console
POST _watcher/watch/my_watch/_execute
{
  "record_execution" : true
}

GET _watcher/watch/my_watch
```

and the action is now in `ackable` state:

```console-result
{
  "found": true,
  "_id": "my_watch",
  "_seq_no": 1,
  "_primary_term": 1,
  "_version": 2,
  "status": {
    "version": 2,
    "actions": {
      "test_index": {
        "ack": {
          "timestamp": "2015-05-26T18:04:27.723Z",
          "state": "ackable"
        },
        "last_execution" : {
          "timestamp": "2015-05-25T18:04:27.723Z",
          "successful": true
        },
        "last_successful_execution" : {
          "timestamp": "2015-05-25T18:04:27.723Z",
          "successful": true
        }
      }
    },
    "state": ...,
    "execution_state": "executed",
    "last_checked": ...,
    "last_met_condition": ...
  },
  "watch": ...
}
```

Now we can acknowledge it:

```console
PUT _watcher/watch/my_watch/_ack/test_index
GET _watcher/watch/my_watch
```

```console-result
{
  "found": true,
  "_id": "my_watch",
  "_seq_no": 2,
  "_primary_term": 1,
  "_version": 3,
  "status": {
    "version": 3,
    "actions": {
      "test_index": {
        "ack": {
          "timestamp": "2015-05-26T18:04:27.723Z",
          "state": "acked"
        },
        "last_execution" : {
          "timestamp": "2015-05-25T18:04:27.723Z",
          "successful": true
        },
        "last_successful_execution" : {
          "timestamp": "2015-05-25T18:04:27.723Z",
          "successful": true
        }
      }
    },
    "state": ...,
    "execution_state": "executed",
    "last_checked": ...,
    "last_met_condition": ...
  },
  "watch": ...
}
```

Acknowledging an action throttles further executions of that action until its
`ack.state` is reset to `awaits_successful_execution`. This happens when the
condition of the watch is not met (the condition evaluates to `false`).

You can acknowledge multiple actions by assigning the `actions` parameter a
comma-separated list of action ids:

```console
POST _watcher/watch/my_watch/_ack/action1,action2
```

To acknowledge all of the actions of a watch, simply omit the `actions`
parameter:

```console
POST _watcher/watch/my_watch/_ack
```

The response looks like a get watch response, but only contains the status:

```console-result
{
  "status": {
    "state": {
      "active": true,
      "timestamp": "2015-05-26T18:04:27.723Z"
    },
    "last_checked": "2015-05-26T18:04:27.753Z",
    "last_met_condition": "2015-05-26T18:04:27.763Z",
    "actions": {
      "test_index": {
        "ack" : {
          "timestamp": "2015-05-26T18:04:27.713Z",
          "state": "acked"
        },
        "last_execution" : {
          "timestamp": "2015-05-25T18:04:27.733Z",
          "successful": true
        },
        "last_successful_execution" : {
          "timestamp": "2015-05-25T18:04:27.773Z",
          "successful": true
        }
      }
    },
    "execution_state": "executed",
    "version": 2
  }
}

```
