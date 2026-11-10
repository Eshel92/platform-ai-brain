<!-- Converted from migration/apis/data-stream-reindex-cancel.asciidoc (AsciiDoc). Includes are inlined. -->

### Reindex data stream cancel API

**New API reference**
For the most up-to-date API details, refer to [Migration APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-migration).

**Tip:** These APIs are designed for indirect use by Kibana's **Upgrade Assistant**.
We strongly recommend you use the **Upgrade Assistant** to upgrade from
{prev-major-last} to {version}. For upgrade instructions, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].
Cancels a running data stream reindex task which was started by the data stream reindex API.
Any backing indices that have already been reindexed and swapped into the data stream will remain in the data stream.
Only backing indices which are currently being reindexed, or pending backing indices which are still waiting to be reindexed, will be cancelled.
Once a data stream reindex task is cancelled it will no longer be accessible through the
status API. If a reindex task is not currently running
this API will return `resource_not_found_exception`.

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
POST _migration/reindex/my-data-stream/_cancel
```

#### Request

`GET /_migration/reindex/<data-stream>/_cancel`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the data stream.

#### Path parameters

`<data-stream>`::
(Required, string)
Name of data stream to cancel reindexing.
