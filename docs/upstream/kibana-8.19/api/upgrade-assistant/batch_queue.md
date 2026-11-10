<!-- Converted from api/upgrade-assistant/batch_queue.asciidoc (AsciiDoc). Includes are inlined. -->

### Batch reindex queue API

experimental["The underlying Upgrade Assistant concepts are stable, but the APIs for managing Upgrade Assistant are experimental."]

Check the current reindex batch queue.

#### Request

`GET /api/upgrade_assistant/reindex/batch/queue`

#### Response code

`200`::
  Indicates a successful call.

#### Example

The API returns the following:

```js
{
  "queue": [ <1>
    {
      "indexName": "index1",
      "newIndexName": "reindexed-v8-index2",
      "status": 3,
      "lastCompletedStep": 0,
      "locked": null,
      "reindexTaskId": null,
      "reindexTaskPercComplete": null,
      "errorMessage": null,
      "runningReindexCount": null,
      "reindexOptions": {
        "queueSettings": {
          "queuedAt": 1583406985489
        }
      }
    },
    {
      "indexName": "index2",
      "newIndexName": "reindexed-v8-index2",
      "status": 3,
      "lastCompletedStep": 0,
      "locked": null,
      "reindexTaskId": null,
      "reindexTaskPercComplete": null,
      "errorMessage": null,
      "runningReindexCount": null,
      "reindexOptions": {
        "queueSettings": {
          "queuedAt": 1583406987334
        }
      }
    }
  ]
}
```

<1> Items in this array indicate reindex tasks at a given point in time and the order in which they will be executed.
