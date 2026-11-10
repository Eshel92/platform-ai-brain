<!-- Converted from security/operator-privileges/operator-only-functionality.asciidoc (AsciiDoc). Includes are inlined. -->

### Operator-only functionality

**Note:** {cloud-only}

Operator privileges provide protection for APIs and dynamic cluster settings.
Any API or cluster setting that is protected by operator privileges is known as
_operator-only functionality_. When the operator privileges feature is enabled,
operator-only APIs can be executed only by operator users. Likewise,
operator-only settings can be updated only by operator users. The list of
operator-only APIs and dynamic cluster settings are pre-determined in the
codebase. The list may evolve in future releases but it is otherwise fixed in a
given Elasticsearch version.

#### Operator-only APIs

* voting-config-exclusions
* delete-license
* update-license
* autoscaling-put-autoscaling-policy
* autoscaling-delete-autoscaling-policy
* update-desired-nodes
* get-desired-nodes
* delete-desired-nodes
* get-desired-balance
* delete-desired-balance

#### Operator-only dynamic cluster settings

* All IP filtering settings
* The following dynamic machine learning settings:
  - `xpack.ml.node_concurrent_job_allocations`
  - `xpack.ml.max_machine_memory_percent`
  - `xpack.ml.use_auto_machine_memory_percent`
  - `xpack.ml.max_lazy_ml_nodes`
  - `xpack.ml.process_connect_timeout`
  - `xpack.ml.nightly_maintenance_requests_per_second`
  - `xpack.ml.max_ml_node_size`
  - `xpack.ml.enable_config_migration`
  - `xpack.ml.persist_results_max_retries`
* The `cluster.routing.allocation.disk.threshold_enabled` setting
* The following recovery settings for managed services:
  - `node.bandwidth.recovery.operator.factor`
  - `node.bandwidth.recovery.operator.factor.read`
  - `node.bandwidth.recovery.operator.factor.write`
  - `node.bandwidth.recovery.operator.factor.max_overcommit`
