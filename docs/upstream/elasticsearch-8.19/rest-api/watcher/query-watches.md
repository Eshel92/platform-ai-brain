<!-- Converted from rest-api/watcher/query-watches.asciidoc (AsciiDoc). Includes are inlined. -->

### Query watches API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Retrieves all registered watches.

#### Request

`GET /_watcher/_query/watches`

#### Prerequisites

* You must have `manage_watcher` or `monitor_watcher` cluster privileges to use
this API. For more information, see security-privileges.

Retrieves all watches in a paginated manner and
optionally filtering watches by a query.

This API supports the following fields:

|======
| Name              | Required | Default  | Description

| `from`            | no       | 0        | The offset from the first result to fetch. Needs to be non-negative.

| `size`            | no       | 10       | The number of hits to return. Needs to be non-negative.

| `query`           | no       | null     | Optional, query filter watches to be returned.

| `sort`            | no       | null     | Optional sort definition.

| `search_after`    | no       | null     | Optional search After to do pagination
                                            using last hit's sort values.
|======

Note that only the `_id` and `metadata.*` fields are queryable or sortable.

This api returns the following top level fields:

`count`::
    The total number of watches found.

`watches`::
    A list of watches based on the `from`, `size` or `search_after` request body parameters.

#### Examples

The following example list all stored watches:

```console
GET /_watcher/_query/watches
```

Response:

```console-result
{
    "count": 1,
    "watches": [
        {
            "_id": "my_watch",
            "watch": {
                "trigger": {
                    "schedule": {
                        "hourly": {
                            "minute": [
                                0,
                                5
                            ]
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
                "actions": {
                    "test_index": {
                        "index": {
                            "index": "test"
                        }
                    }
                }
            },
            "status": {
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
                },
                "version": -1
            },
            "_seq_no": 0,
            "_primary_term": 1
        }
    ]
}
```
