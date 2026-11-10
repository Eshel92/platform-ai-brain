<!-- Converted from settings/snapshot-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Snapshot and restore settings

The following cluster settings configure <<snapshot-restore,snapshot and
restore>>.

`snapshot.max_concurrent_operations`::
(Dynamic, integer) Maximum number of concurrent
snapshot operations. Defaults to `1000`.
This limit applies in total to all ongoing snapshot creation, cloning, and
deletion operations. Elasticsearch will reject any operations that would exceed this
limit.

#### SLM settings

The following cluster settings configure <<automate-snapshots-slm,snapshot lifecycle management
(SLM)>>.

`slm.history_index_enabled`::
(Dynamic, Boolean)
Controls whether SLM records the history of actions taken as part of SLM policies
to the `slm-history-*` indices. Defaults to `true`.

`slm.retention_schedule`::
(Dynamic, cron scheduler value)
Controls when the retention task runs.
Can be a periodic or absolute time schedule.
Supports all values supported by the cron scheduler.
Defaults to daily at 1:30am UTC: `0 30 1 * * ?`.

`slm.retention_duration`::
(Dynamic, time value)
Limits how long SLM should spend deleting old snapshots.
Defaults to one hour: `1h`.

`slm.health.failed_snapshot_warn_threshold`::
(Dynamic, Long)
The number of failed invocations since last successful snapshot that
indicate a problem with the policy in the health api.
Defaults to a health api warning after five repeated failures: `5L`.

`repositories.url.allowed_urls` ::
(Static)
Specifies the read-only URL repositories that snapshots can be restored from.
