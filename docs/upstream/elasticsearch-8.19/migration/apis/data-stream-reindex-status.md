<!-- Converted from migration/apis/data-stream-reindex-status.asciidoc (AsciiDoc). Includes are inlined. -->

### Reindex data stream status API

**New API reference**
For the most up-to-date API details, refer to [Migration APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-migration).

**Tip:** These APIs are designed for indirect use by Kibana's **Upgrade Assistant**.
We strongly recommend you use the **Upgrade Assistant** to upgrade from
{prev-major-last} to {version}. For upgrade instructions, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].
Obtains the current status of a reindex task for the requested data stream. This status is
available while the reindex task is running and for 24 hours after completion of the task,
whether it succeeds or fails. If the task is cancelled, the status is no longer available.
If the task fails, the exception will be listed within the status.

```console
POST _migration/reindex
{
    "source": {
        "index": "my-data-stream"
    },
    "mode": "upgrade"
}
```

```console
POST /_migration/reindex/my-data-stream/_cancel
DELETE _data_stream/my-data-stream
DELETE _index_template/my-data-stream-template
```

#### Request

`GET /_migration/reindex/<data-stream>/_status`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the data stream.

#### Path parameters

`<data-stream>`::
(Required, string)
Name of data stream to get status for. The reindex task for the
data stream should be currently running or have been completed in the last 24 hours.

#### Response body

`start_time`::
(Optional, time value) The time when the reindex task started.

`start_time_millis`::
(integer) The time when the reindex task started, in milliseconds since the epoch.

`complete`::
(boolean) `false` if the reindex task is still running, and `true` if the task has completed with success or failure.

`total_indices_in_data_stream`::
(integer) The total number of backing indices in the data stream, including the write index.

`total_indices_requiring_upgrade`::
(integer) The number of backing indices that need to be upgraded. These will consist of the indices which have an
older version and are not read-only.

`successes`::
(integer) The number of backing indices which have already been successfully upgraded.

`in_progress`::
(array of objects) Information on the backing indices which are currently being reindexed.
**Properties of objects in `in_progress`**
=====
`index`::
(string) The name of the source backing index.

`total_doc_count`::
(integer) The number of documents in the source backing index.

`reindexed_doc_count`::
(integer) The number of documents which have already been added to the destination backing index.
=====

`pending`::
(integer) The number of backing indices which still need to be upgraded and have not yet been started.

`errors`::
(array of objects) Information on any errors which have occurred.
**Properties of objects in `errors`**
=====
`index`::
(string) The name of a backing index which has had an error during reindex.

`message`::
(string) Description of the error.
=====

`exceptions`::
(Optional, string)
Exception message for a reindex failure if the failure could not be tied to a particular index.

#### Examples

```console
GET _migration/reindex/my-data-stream/_status
```

The following is a typical response:
```console-result
{
  "start_time_millis": 1737676174349,
  "complete": false,
  "total_indices_in_data_stream": 4,
  "total_indices_requiring_upgrade": 3,
  "successes": 1,
  "in_progress": [
    {
      "index": ".ds-my-data-stream-2025.01.23-000002",
      "total_doc_count": 10000000,
      "reindexed_doc_count": 1000
    }
  ],
  "pending": 1,
  "errors": []
}
```

For a more in-depth example showing the usage of this API along with the reindex and cancel APIs,
see this example.
