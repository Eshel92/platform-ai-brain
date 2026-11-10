<!-- Converted from setup/upgrade.asciidoc (AsciiDoc). Includes are inlined. -->

## Upgrade Kibana

To upgrade from 7.16.0 or earlier to {version},
**you must first upgrade to {prev-major-last}**, which enables you to use the *Upgrade Assistant* to
{stack-ref}/upgrading-elastic-stack.html#prepare-to-upgrade[prepare for the upgrade].
Before you upgrade, you must resolve all critical issues identified by the *Upgrade Assistant*.

In addition, we recommend to carefully review the list of breaking changes and deprecations and to take any necessary actions to mitigate their impact on the upgrade.
You can enable the deprecated APIs debug logs config to get information about calls to deprecated APIs.

Rolling upgrades are unsupported in Kibana. To upgrade,
you must shut down all Kibana instances, install the new software, and restart Kibana.
Upgrading while older Kibana instances are running can cause data loss or upgrade failures.

**Warning:**
When required, Kibana automatically migrates saved objects.
In case of an upgrade failure, you can roll back to an
earlier version of Kibana. To roll back, you **must** have a
[backup snapshot](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshot-restore.html) that includes the `kibana` feature
state. By default, snapshots include the `kibana` feature state.

For more information about upgrading,
refer to {stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}.]

**Important:** You can upgrade to pre-release versions for testing,
but upgrading from a pre-release to the General Available version is unsupported.
You should use pre-release versions only for testing in a temporary environment.

### Upgrading multiple Kibana instances

When upgrading several Kibana instances connected to the same Elasticsearch cluster,
ensure that all outdated instances are shut down before starting the upgrade.

Rolling upgrades are unsupported in Kibana. However, when outdated instances are shut down, you can start all upgraded instances in parallel,
which allows all instances to participate in the upgrade migration in parallel.

For large deployments with more than 10 Kibana instances, and more than 10,000 saved objects,
you can reduce the upgrade downtime by bringing up a single Kibana instance and waiting for it to
complete the upgrade migration before bringing up the remaining instances.

### Preparing for migration

Take these extra steps to ensure you are ready for migration.

#### Ensure your Elasticsearch cluster is healthy

Problems with your Elasticsearch cluster can prevent Kibana upgrades from succeeding.

During the upgrade process, Kibana creates new indices into which updated documents are written. If a cluster is approaching the low watermark, there's a high risk of Kibana not being able to create these. Reading, transforming and writing updated documents can be memory intensive, using more available heap than during routine operation. You must make sure that enough heap is available to prevent requests from timing out or throwing errors from circuit breaker exceptions. You should also ensure that all shards are replicated and assigned.

A healthy cluster has:

 * Enough free disk space, at least twice the amount of storage taken up by the `.kibana` and `.kibana_task_manager` indices
 * Sufficient heap size
 * A "green" cluster status

#### Ensure that all Kibana instances are the same

When you perform an upgrade migration of different Kibana versions, the migration can fail.
Ensure that all Kibana instances are running the same version, configuration, and plugins.

#### Back up your data

Be sure to have a [snapshot](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshot-restore.html) of all your data before attempting a migration.
If something goes wrong during migration, you can restore from the snapshot and try again.

Review the common causes of Kibana upgrade failures and how to prevent them.

(See `setup/upgrade/saved-objects-migration.md`)
(See `setup/upgrade/resolving-migration-failures.md`)
(See `setup/upgrade/rollback-migration.md`)
