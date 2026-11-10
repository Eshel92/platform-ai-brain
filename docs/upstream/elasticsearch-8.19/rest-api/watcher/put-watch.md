<!-- Converted from rest-api/watcher/put-watch.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update watch API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Either registers a new watch in Watcher or updates an existing one.

#### Request

`PUT _watcher/watch/<watch_id>`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Description

When a watch is registered, a new document that represents the watch is added to
the `.watches` index and its trigger is immediately registered with the relevant
trigger engine. Typically for the `schedule` trigger, the scheduler is the
trigger engine.

**Important:** You must use Kibana or this API to create a watch. Do not add a watch
            directly to the `.watches` index using the Elasticsearch index API.
            If Elasticsearch security features are enabled, do not give users `write`
            privileges on the `.watches` index.

When adding a watch you can also define its initial
active state. You do that by setting the `active`
parameter.

##### Security integration

When Elasticsearch security features are enabled, your watch can index or search only
on indices for which the user that stored the watch has privileges. If the user
is able to read index `a`, but not index `b`, the same will apply, when the watch
is executed.

#### Path parameters

`<watch_id>`::
  (Required, string) Identifier for the watch.

#### Query parameters

`active`::
  (Optional, Boolean) Defines whether the watch is active or inactive by default.
  The default value is `true`, which means the watch is active by default.

#### Request body

A watch has the following fields:

|======
| Name              | Description

| `trigger`         | The trigger that defines when
                      the watch should run.

| `input`           | The input that defines the input
                      that loads the data for the watch.

| `condition`       | The condition that defines if
                      the actions should be run.

| `actions`         | The list of actions that will be
                      run if the condition matches

| `transform`       | The transform that processes the 
                      watch payload to prepare it for the watch actions.

| `metadata`        | Metadata json that will be copied into the history entries.

| `throttle_period` | The minimum time between actions being run, the default
                      for this is 5 seconds. This default can be changed in the
                      config file with the setting
                      `xpack.watcher.throttle.period.default_period`. If both
                      this value and the `throttle_period_in_millis` parameter
                      are specified, Watcher uses the last parameter
                      included in the request.

| `throttle_period_in_millis` | Minimum time in milliseconds between actions
                                being run. Defaults to `5000`. If both this
                                value and the `throttle_period` parameter are
                                specified, Watcher uses the last parameter
                                included in the request.

|======

#### Examples

The following example adds a watch with the `my-watch` id that has the following
characteristics:

* The watch schedule triggers every minute.
* The watch search input looks for any 404 HTTP responses that occurred in the
  last five minutes.
* The watch condition checks if any search hits where found.
* When found, the watch action sends an email to an administrator.

```console
PUT _watcher/watch/my-watch
{
  "trigger" : {
    "schedule" : { "cron" : "0 0/1 * * * ?" }
  },
  "input" : {
    "search" : {
      "request" : {
        "indices" : [
          "logstash*"
        ],
        "body" : {
          "query" : {
            "bool" : {
              "must" : {
                "match": {
                   "response": 404
                }
              },
              "filter" : {
                "range": {
                  "@timestamp": {
                    "from": "{{ctx.trigger.scheduled_time}}||-5m",
                    "to": "{{ctx.trigger.triggered_time}}"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "condition" : {
    "compare" : { "ctx.payload.hits.total" : { "gt" : 0 }}
  },
  "actions" : {
    "email_admin" : {
      "email" : {
        "to" : "admin@domain.host.com",
        "subject" : "404 recently encountered"
      }
    }
  }
}
```

When you add a watch you can also define its initial
active state. You do that
by setting the `active` parameter. The following command adds a watch and sets
it to be inactive by default:

```js
PUT _watcher/watch/my-watch?active=false
```

**Note:** If you omit the `active` parameter, the watch is active by default.
