<!-- Converted from rest-api/watcher/execute-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Execute watch API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Forces the execution of a stored watch.

#### Request

`POST _watcher/watch/<watch_id>/_execute` +

`POST _watcher/watch/_execute`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Description

This API can be used to force execution of the watch outside of its triggering
logic or to simulate the watch execution for debugging purposes.

For testing and debugging purposes, you also have fine-grained control on how
the watch runs. You can execute the watch without executing all of its actions
or alternatively by simulating them. You can also force execution by ignoring
the watch condition and control whether a watch record would be written to the
watch history after execution.

##### Inline watch execution

You can use the Execute API to execute watches that are not yet registered by
specifying the watch definition inline. This serves as great tool for testing
and debugging your watches prior to adding them to Watcher.

#### Path parameters

`<watch_id>`::
  (Optional, string) Identifier for the watch.

#### Query parameters

`debug`::
  (Optional, Boolean) Defines whether the watch runs in debug mode. The default
  value is `false`.

#### Request body

This API supports the following fields:

|======
| Name                | Required | Default  | Description

| `trigger_data`      | no       |          | This structure is parsed as the data of the trigger event
                                              that will be used during the watch execution

| `ignore_condition`  | no       | false    | When set to `true`, the watch execution uses the
                                              always condition.
                                              This can also be specified as an HTTP parameter.

| `alternative_input` | no       | null     | When present, the watch uses this object as a payload
                                              instead of executing its own input.

| `action_modes`      | no       | null     | Determines how to handle the watch actions as part of the
                                              watch execution. See watcher-api-execute-watch-action-mode
                                              for more information.

| `record_execution`  | no       | false    | When set to `true`, the watch record representing the watch
                                              execution result is persisted to the `.watcher-history`
                                              index for the current time. In addition, the status of the
                                              watch is updated, possibly throttling subsequent executions.
                                              This can also be specified as an HTTP parameter.

| `watch`             | no       | null     | When present, this watch is used
                                              instead of the one specified in the request. This watch is
                                              not persisted to the index and record_execution cannot be set.
|======

##### Action execution modes

Action modes define how actions are handled during the watch execution. There
are five possible modes an action can be associated with:

|======
| Name              | Description

| `simulate`        | The action execution is simulated. Each action type
                      defines its own simulation operation mode. For example, the
                      `email` action creates
                      the email that would have been sent but does not actually
                      send it. In this mode, the action might be throttled if the
                      current state of the watch indicates it should be.

| `force_simulate`  | Similar to the `simulate` mode, except the action is
                      not throttled even if the current state of the watch
                      indicates it should be.

| `execute`         | Executes the action as it would have been executed if the
                      watch had been triggered by its own trigger. The
                      execution might be throttled if the current state of the
                      watch indicates it should be.

| `force_execute`   | Similar to the `execute` mode, except the action is not
                      throttled even if the current state of the watch indicates
                      it should be.

| `skip`            | The action is skipped and is not executed or simulated.
                      Effectively forces the action to be throttled.
|======

##### Security integration

When Elasticsearch security features are enabled on your cluster, watches
are executed with the privileges of the user that stored the watches. If your
user is allowed to read index `a`, but not index `b`, then the exact same set of
rules will apply during execution of a watch.

When using the execute watch API, the authorization data of the user that
called the API will be used as a base, instead of the information who stored
the watch.

#### Examples

The following example executes the `my_watch` watch:

```console
POST _watcher/watch/my_watch/_execute
```

The following example shows a comprehensive example of executing the `my-watch` watch:

```console
POST _watcher/watch/my_watch/_execute
{
  "trigger_data" : { <1>
     "triggered_time" : "now",
     "scheduled_time" : "now"
  },
  "alternative_input" : { <2>
    "foo" : "bar"
  },
  "ignore_condition" : true, <3>
  "action_modes" : {
    "my-action" : "force_simulate" <4>
  },
  "record_execution" : true <5>
}
```

<1> The triggered and schedule times are provided.
<2> The input as defined by the watch is ignored and instead the provided input
    is used as the execution payload.
<3> The condition as defined by the watch is ignored and is assumed to
    evaluate to `true`.
<4> Forces the simulation of `my-action`. Forcing the simulation means that
    throttling is ignored and the watch is simulated by Watcher instead of
    being executed normally.
<5> The execution of the watch creates a watch record in the watch history,
    and the throttling state of the watch is potentially updated accordingly.

This is an example of the output:

```console-result
{
  "_id": "my_watch_0-2015-06-02T23:17:55.124Z", <1>
  "watch_record": { <2>
    "@timestamp": "2015-06-02T23:17:55.124Z",
    "watch_id": "my_watch",
    "node": "my_node",
    "messages": [],
    "trigger_event": {
      "type": "manual",
      "triggered_time": "2015-06-02T23:17:55.124Z",
      "manual": {
        "schedule": {
          "scheduled_time": "2015-06-02T23:17:55.124Z"
        }
      }
    },
    "state": "executed",
    "status": {
      "version": 1,
      "execution_state": "executed",
      "state": {
        "active": true,
        "timestamp": "2015-06-02T23:17:55.111Z"
      },
      "last_checked": "2015-06-02T23:17:55.124Z",
      "last_met_condition": "2015-06-02T23:17:55.124Z",
      "actions": {
        "test_index": {
          "ack": {
            "timestamp": "2015-06-02T23:17:55.124Z",
            "state": "ackable"
          },
          "last_execution": {
            "timestamp": "2015-06-02T23:17:55.124Z",
            "successful": true
          },
          "last_successful_execution": {
            "timestamp": "2015-06-02T23:17:55.124Z",
            "successful": true
          }
        }
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
    "result": { <3>
      "execution_time": "2015-06-02T23:17:55.124Z",
      "execution_duration": 12608,
      "input": {
        "type": "simple",
        "payload": {
          "foo": "bar"
        },
        "status": "success"
      },
      "condition": {
        "type": "always",
        "met": true,
        "status": "success"
      },
      "actions": [
        {
          "id": "test_index",
          "index": {
            "response": {
              "index": "test",
              "version": 1,
              "created": true,
              "result": "created",
              "id": "AVSHKzPa9zx62AzUzFXY"
            }
          },
          "status": "success",
          "type": "index"
        }
      ]
    },
    "user": "test_admin" <4>
  }
}
```
<1> The id of the watch record as it would be stored in the `.watcher-history` index.
<2> The watch record document as it would be stored in the `.watcher-history` index.
<3> The watch execution results.
<4> The user used to execute the watch.

You can set a different execution mode for every action by associating the mode
name with the action id:

```console
POST _watcher/watch/my_watch/_execute
{
  "action_modes" : {
    "action1" : "force_simulate",
    "action2" : "skip"
  }
}
```

You can also associate a single execution mode with all the actions in the watch
using `_all` as the action id:

```console
POST _watcher/watch/my_watch/_execute
{
  "action_modes" : {
    "_all" : "force_execute"
  }
}
```

The following example shows how to execute a watch inline:

```console
POST _watcher/watch/_execute
{
  "watch" : {
    "trigger" : { "schedule" : { "interval" : "10s" } },
    "input" : {
      "search" : {
        "request" : {
          "indices" : [ "logs" ],
          "body" : {
            "query" : {
              "match" : { "message": "error" }
            }
          }
        }
      }
    },
    "condition" : {
      "compare" : { "ctx.payload.hits.total" : { "gt" : 0 }}
    },
    "actions" : {
      "log_error" : {
        "logging" : {
          "text" : "Found {{ctx.payload.hits.total}} errors in the logs"
        }
      }
    }
  }
}
```

All other settings for this API still apply when inlining a watch. In the
following snippet, while the inline watch defines a `compare` condition,
during the execution this condition will be ignored:

```console
POST _watcher/watch/_execute
{
  "ignore_condition" : true,
  "watch" : {
    "trigger" : { "schedule" : { "interval" : "10s" } },
    "input" : {
      "search" : {
        "request" : {
          "indices" : [ "logs" ],
          "body" : {
            "query" : {
              "match" : { "message": "error" }
            }
          }
        }
      }
    },
    "condition" : {
      "compare" : { "ctx.payload.hits.total" : { "gt" : 0 }}
    },
    "actions" : {
      "log_error" : {
        "logging" : {
          "text" : "Found {{ctx.payload.hits.total}} errors in the logs"
        }
      }
    }
  }
}
```
