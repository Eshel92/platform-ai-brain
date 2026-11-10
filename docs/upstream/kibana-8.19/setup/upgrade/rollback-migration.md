<!-- Converted from setup/upgrade/rollback-migration.asciidoc (AsciiDoc). Includes are inlined. -->

### Roll back to a previous version of Kibana

If you've followed preparing for migration
and resolving migration failures, and
Kibana is still unable to successfully upgrade, rollback Kibana until
you're able to identify and fix the root cause.

**Warning:** Before you roll back Kibana, ensure that the version you want to roll back to is compatible with
your Elasticsearch cluster. If the version you want to roll back to is not compatible, you must also rollback Elasticsearch.
Any changes made after an upgrade are lost when you roll back to a previous version.

To roll back after a failed upgrade migration, you must also roll back the Kibana feature state to be compatible with the previous Kibana version.

#### Roll back by restoring the Kibana feature state from a snapshot

. Before proceeding, [take a snapshot](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshots-take-snapshot.html) that contains the `kibana` feature state.
   By default, snapshots include the `kibana` feature state.
. To make sure no Kibana instances are performing an upgrade migration, shut down all Kibana instances.
. [Restore](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshots-restore-snapshot.html) the `kibana` feature state from a snapshot taken before the failed Kibana upgrade. The following Elasticsearch request will only restore the Kibana feature state 
```console
POST _snapshot/my_repository/my_snapshot_2099.05.06/_restore
{
  "indices": "-*", <1>
  "feature_states": ["kibana"]
}
```
<1> Exclude all indices and data streams from the restore operation to ensure that only the Kibana system indices included in the Kibana feature state will be restored.
. Start all Kibana instances on the older version you want to rollback to.
