<!-- Converted from modules/gateway.asciidoc (AsciiDoc). Includes are inlined. -->

### Local gateway settings

The local gateway stores the cluster state and shard data across full
cluster restarts.

The following _static_ settings, which must be set on every master-eligible node,
control how long a freshly elected master should wait before it tries to
recover the cluster state and the cluster's data.

**Note:** These settings only take effect during a full cluster restart.

`gateway.expected_data_nodes`::
(Static)
Number of data nodes expected in the cluster.
Recovery of local shards begins when the expected number of
data nodes join the cluster. Defaults to `0`.

`gateway.recover_after_time`::
(Static)
If the expected number of nodes is not achieved, the recovery process waits
for the configured amount of time before trying to recover.
Defaults to `5m`.
Once the `recover_after_time` duration has timed out, recovery will start
as long as the following condition is met:

`gateway.recover_after_data_nodes`::
(Static)
Recover as long as this many data nodes have joined the cluster.

These settings can be configured in `elasticsearch.yml` as follows:

```yaml
gateway.expected_data_nodes: 3
gateway.recover_after_time: 600s
gateway.recover_after_data_nodes: 3
```
