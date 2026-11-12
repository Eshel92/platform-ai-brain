<!-- Converted from data-streams/lifecycle/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Data stream lifecycle

A data stream lifecycle is the built-in mechanism data streams use to manage their lifecycle. It enables you to easily
automate the management of your data streams according to your retention requirements. For example, you could configure
the lifecycle to:

* Ensure that data indexed in the data stream will be kept at least for the retention time you defined.
* Ensure that data older than the retention period will be deleted automatically by Elasticsearch at a later time.

To achieve that, it supports:

* Automatic rollover, which chunks your incoming data in smaller pieces to facilitate better performance
and backwards incompatible mapping changes.
* Configurable retention, which allows you to configure the time period for which your data is guaranteed to be stored.
Elasticsearch is allowed at a later time to delete data older than this time period. Retention can be configured on the data stream level
or on a global level. Read more about the different options in this tutorial.

A data stream lifecycle also supports downsampling the data stream backing indices.
See the downsampling example for
more details.

### How does it work?

In intervals configured by `data_streams.lifecycle.poll_interval`, Elasticsearch goes over
each data stream and performs the following steps:

1. Checks if the data stream has a data stream lifecycle configured, skipping any indices not part of a managed data stream.
2. Rolls over the write index of the data stream, if it fulfills the conditions defined by
`cluster.lifecycle.default.rollover`.
3. After an index is not the write index anymore (i.e. the data stream has been rolled over),
automatically tail merges the index. Data stream lifecycle executes a merge operation that only targets
the long tail of small segments instead of the whole shard. As the segments are organised
into tiers of exponential sizes, merging the long tail of small segments is only a
fraction of the cost of force merging to a single segment. The small segments would usually
hold the most recent data so tail merging will focus the merging resources on the higher-value
data that is most likely to keep being queried.
4. If downsampling is configured it will execute
all the configured downsampling rounds.
5. Applies retention to the remaining backing indices. This means deleting the backing indices whose
`generation_time` is longer than the effective retention period (read more about the
effective retention calculation). The `generation_time` is only applicable to rolled
over backing indices and it is either the time since the backing index got rolled over, or the time optionally configured
in the `index.lifecycle.origination_date` setting.

**Important:** We use the `generation_time` instead of the creation time because this ensures that all data in the backing
index have passed the retention period. As a result, the retention period is not the exact time data gets deleted, but
the minimum time data will be stored.

**Note:** Steps `2-4` apply only to backing indices that are not already managed by ILM, meaning that these indices either do
not have an ILM policy defined, or if they do, they have `index.lifecycle.prefer_ilm`
set to `false`.

### Configuring data stream lifecycle

Since the lifecycle is configured on the data stream level, the process to configure a lifecycle on a new data stream and
on an existing one differ.

In the following sections, we will go through the following tutorials:

* To create a new data stream with a lifecycle, you need to add the data stream lifecycle as part of the index template
that matches the name of your data stream (see tutorial-manage-new-data-stream). When a write operation
with the name of your data stream reaches Elasticsearch then the data stream will be created with the respective data stream lifecycle.
* To update the lifecycle of an existing data stream you need to use the data stream lifecycle APIs
to edit the lifecycle on the data stream itself (see tutorial-manage-existing-data-stream).
* Migrate an existing ILM managed data stream to Data stream lifecycle using tutorial-migrate-data-stream-from-ilm-to-dsl.

**Note:** Updating the data stream lifecycle of an existing data stream is different from updating the settings or the mapping,
because it is applied on the data stream level and not on the individual backing indices.

(See `data-streams/lifecycle/tutorial-manage-new-data-stream.md`)
(See `data-streams/lifecycle/tutorial-manage-existing-data-stream.md`)
(See `data-streams/lifecycle/tutorial-manage-data-stream-retention.md`)
(See `data-streams/lifecycle/tutorial-migrate-data-stream-from-ilm-to-dsl.md`)
