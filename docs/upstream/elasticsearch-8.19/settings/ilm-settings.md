<!-- Converted from settings/ilm-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Index lifecycle management settings in Elasticsearch

These are the settings available for configuring index lifecycle management (ILM).

#### Cluster level settings

`xpack.ilm.enabled`::
(Static, Boolean)
deprecated:[7.8.0,Basic License features are always enabled] +
This deprecated setting has no effect and will be removed in Elasticsearch 8.0.

`indices.lifecycle.history_index_enabled`::
(Dynamic, Boolean)
Whether ILM's history index is enabled. If enabled, ILM will record the
history of actions taken as part of ILM policies to the `ilm-history-*`
indices. Defaults to `true`.

`indices.lifecycle.poll_interval`::
(Dynamic, time unit value)
How often index lifecycle management checks for indices that meet policy criteria. Defaults to `10m`.

`indices.lifecycle.rollover.only_if_has_documents`::
(Dynamic, Boolean)
Whether ILM will only roll over non-empty indices. If enabled, ILM will only roll over indices
as long as they contain at least one document. Defaults to `true`.

#### Index level settings

These index-level ILM settings are typically configured through index
templates. For more information, see ilm-gs-create-policy.

`index.lifecycle.indexing_complete`::
(Dynamic, Boolean)
Indicates whether or not the index has been rolled over.
Automatically set to `true` when ILM completes the rollover action.
You can explicitly set it to skip rollover.
Defaults to `false`.

`index.lifecycle.name`::
(Dynamic, string)
The name of the policy to use to manage the index. For information about how
Elasticsearch applies policy changes, see update-lifecycle-policy.
If you are restoring an index from snapshot that was previously managed by index lifecycle management,
you can override this setting to null during the restore operation to disable
further management of the index. See also index-lifecycle-rollover-alias.

`index.lifecycle.origination_date`::
(Dynamic, long)
If specified, this is the timestamp used to calculate the index age for its phase transitions.
Use this setting if you create a new index that contains old data and
want to use the original creation date to calculate the index age.
Specified as a Unix epoch value in milliseconds.

`index.lifecycle.parse_origination_date`::
(Dynamic, Boolean)
Set to `true` to parse the origination date from the index name.
This origination date is used to calculate the index age for its phase transitions.
The index name must match the pattern `^.*-{date_format}-\\d+`,
where the `date_format` is `yyyy.MM.dd` and the trailing digits are optional.
An index that was rolled over would normally match the full format,
for example `logs-2016.10.31-000002`).
If the index name doesn't match the pattern, index creation fails.

`index.lifecycle.step.wait_time_threshold`::
(Dynamic, time value)
Time to wait for the cluster to resolve allocation issues during an ILM
`shrink` action. Must be greater than `1h` (1 hour). Defaults to
`12h` (12 hours). See ilm-shrink-shard-allocation.

`index.lifecycle.rollover_alias`::
(Dynamic, string)
The index alias to update when the index rolls over. Specify when using a
policy that contains a rollover action. When the index rolls over, the alias is
updated to reflect that the index is no longer the write index. For more
information about rolling indices, see Rollover.
If you are restoring an index from snapshot that was previously managed by index lifecycle management,
you can override this setting to null during the restore operation to disable
further management of future indices. See also index-lifecycle-name.
