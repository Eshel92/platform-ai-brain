<!-- Converted from api/upgrade-assistant.asciidoc (AsciiDoc). Includes are inlined. -->

## Upgrade assistant APIs

Check the upgrade status of your Elasticsearch cluster and reindex indices that were created in the previous major version. The assistant helps you prepare for the next major version of Elasticsearch.

The following upgrade assistant APIs are available:

* Upgrade readiness status API to check the status of your cluster

* Start or resume reindex API to start a new reindex or resume a paused reindex

* Batch start or resume reindex API to start or resume multiple reindex tasks

* Batch reindex queue API to check the current reindex batch queue

* Check reindex status API to check the status of the reindex operation

* Cancel reindex API to cancel reindexes that are waiting for the Elasticsearch reindex task to complete

(See `api/upgrade-assistant/status.md`)
(See `api/upgrade-assistant/reindexing.md`)
(See `api/upgrade-assistant/batch_reindexing.md`)
(See `api/upgrade-assistant/batch_queue.md`)
(See `api/upgrade-assistant/check_reindex_status.md`)
(See `api/upgrade-assistant/cancel_reindex.md`)
