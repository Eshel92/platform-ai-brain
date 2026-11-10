<!-- Converted from security/authorization/built-in-roles.asciidoc (AsciiDoc). Includes are inlined. -->

### Built-in roles

The {stack-security-features} apply a default role to all users, including
anonymous users. The default role enables users to access
the authenticate endpoint, change their own passwords, and get information about
themselves.

There is also a set of built-in roles you can explicitly assign to users. These
roles have a fixed set of privileges and cannot be updated.

[[built-in-roles-apm-system]] `apm_system` ::
Grants access necessary for the APM system user to send system-level data
(such as monitoring) to Elasticsearch.

[[built-in-roles-apm-user]] `apm_user` ::
Grants the privileges required for APM users (such as `read` and
`view_index_metadata` privileges on the `apm-*` and `.ml-anomalies*` indices).
deprecated:[7.13.0,"See [APM app users and privileges\](https://www.elastic.co/guide/en/kibana/8.19/apm-app-users.html) for alternatives."].

[[built-in-roles-beats-admin]] `beats_admin` ::
Grants access to the `.management-beats` index, which contains configuration
information for the Beats.

[[built-in-roles-beats-system]] `beats_system` ::
Grants access necessary for the Beats system user to send system-level data
(such as monitoring) to Elasticsearch.
===============================
* This role should not be assigned to users as the granted permissions may
change between releases.
* This role does not provide access to the beats indices and is not
suitable for writing beats output to Elasticsearch.
===============================

[[built-in-roles-data-frame-transforms-admin]] `data_frame_transforms_admin` ::
Grants `manage_data_frame_transforms` cluster privileges, which enable you to
manage transforms. This role also includes all
[Kibana privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html) for the {ml-features}.
deprecated:[7.5.0,"Replaced by `transform_admin`"].

[[built-in-roles-data-frame-transforms-user]] `data_frame_transforms_user` ::
Grants `monitor_data_frame_transforms` cluster privileges, which enable you to
use transforms. This role also includes all
[Kibana privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html) for the {ml-features}.
deprecated:[7.5.0,"Replaced by `transform_user`"].

[[built-in-roles-editor]] `editor` ::

Grants full access to all features in Kibana (including Solutions) and read-only access to data indices.
===============================
* This role provides read access to any index that is not prefixed with a dot.
* This role automatically grants full access to new Kibana features as soon as they are released.
* Some Kibana features may also require creation or write access to data indices. Machine learning {dfanalytics-jobs}
  is an example. For such features those privileges must be defined in a separate role.
===============================

[[built-in-roles-enrich-user]] `enrich_user` ::
Grants access to manage *all* enrich indices (`.enrich-*`) and *all* operations on
ingest pipelines.

[[built-in-roles-inference-admin]] `inference_admin`::
Provides all of the privileges of the `inference_user` role and the full
use of the {inference} APIs. Grants the `manage_inference` cluster privilege.

[[built-in-roles-inference-user]] `inference_user`::
Provides the minimum privileges required to view {inference} configurations
and perform inference. Grants the `monitor_inference` cluster privilege.

[[built-in-roles-ingest-user]] `ingest_admin` ::
Grants access to manage *all* index templates and *all* ingest pipeline configurations.
**Note:** This role does *not* provide the ability to create indices; those privileges
must be defined in a separate role.

[[built-in-roles-kibana-dashboard]] `kibana_dashboard_only_user` ::
(This role is deprecated, please use
[Kibana feature privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html#kibana-feature-privileges)
instead).
Grants read-only access to the Kibana Dashboard in every
[space in Kibana](https://www.elastic.co/guide/en/kibana/8.19/xpack-spaces.html).
This role does not have access to editing tools in Kibana.

[[built-in-roles-kibana-system]] `kibana_system` ::
Grants access necessary for the Kibana system user to read from and write to the
Kibana indices, manage index templates and tokens, and check the availability of
the Elasticsearch cluster. It also permits
activating, searching, and retrieving user profiles,
as well as updating user profile data for the `kibana-*` namespace.
This role grants read access to the `.monitoring-*` indices and read and write
access to the `.reporting-*` indices. For more information,
see [Configuring Security in Kibana](https://www.elastic.co/guide/en/kibana/8.19/using-kibana-with-security.html).
**Note:** This role should not be assigned to users as the granted permissions may
change between releases.

[[built-in-roles-kibana-admin]] `kibana_admin`::
Grants access to all features in Kibana. For more information on Kibana authorization,
see [Kibana authorization](https://www.elastic.co/guide/en/kibana/8.19/xpack-security-authorization.html).

[[built-in-roles-kibana-user]] `kibana_user`::
(This role is deprecated, please use the
`kibana_admin` role instead.)
Grants access to all features in Kibana. For more information on Kibana authorization,
see [Kibana authorization](https://www.elastic.co/guide/en/kibana/8.19/xpack-security-authorization.html).

[[built-in-roles-logstash-admin]] `logstash_admin` ::
Grants access to the `.logstash*` indices for managing configurations, and grants
necessary access for logstash-specific APIs exposed by the logstash x-pack plugin.

[[built-in-roles-logstash-system]] `logstash_system` ::
Grants access necessary for the Logstash system user to send system-level data
(such as monitoring) to Elasticsearch. For more information, see
{logstash-ref}/ls-security.html[Configuring Security in Logstash].
===============================
* This role should not be assigned to users as the granted permissions may
change between releases.
* This role does not provide access to the logstash indices and is not
suitable for use within a Logstash pipeline.
===============================

[[built-in-roles-ml-admin]] `machine_learning_admin`::
Provides all of the privileges of the `machine_learning_user` role plus the full
use of the machine learning APIs. Grants `manage_ml` cluster privileges, read access to
`.ml-anomalies*`, `.ml-notifications*`, `.ml-state*`, `.ml-meta*` indices and
write access to `.ml-annotations*` indices. Machine learning administrators also need
index privileges for source and destination indices and roles that grant
access to Kibana. See {ml-docs-setup-privileges}.

[[built-in-roles-ml-user]] `machine_learning_user`::
Grants the minimum privileges required to view machine learning configuration,
status, and work with results. This role grants `monitor_ml` cluster privileges,
read access to the `.ml-notifications` and `.ml-anomalies*` indices
(which store machine learning results), and write access to `.ml-annotations*` indices.
Machine learning users also need index privileges for source and destination
indices and roles that grant access to Kibana. See {ml-docs-setup-privileges}.

[[built-in-roles-monitoring-user]] `monitoring_user`::
Grants the minimum privileges required for any user of {monitoring} other than those
required to use Kibana. This role grants access to the monitoring indices and grants
privileges necessary for reading basic cluster information. This role also includes
all [Kibana privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html) for the {stack-monitor-features}.
Monitoring users should also be assigned the `kibana_admin` role, or another role
with [access to the Kibana instance](https://www.elastic.co/guide/en/kibana/8.19/xpack-security-authorization.html).

[[built-in-roles-remote-monitoring-agent]] `remote_monitoring_agent`::
Grants the minimum privileges required to write data into the monitoring indices
(`.monitoring-*`). This role also has the privileges necessary to create
{metricbeat} indices (`metricbeat-*`) and write data into them.

[[built-in-roles-remote-monitoring-collector]] `remote_monitoring_collector`::
Grants the minimum privileges required to collect monitoring data for the Elastic Stack.

[[built-in-roles-reporting-user]] `reporting_user`::
Grants the specific privileges required for users of {reporting} other than those
required to use Kibana. This role grants access to the reporting indices; each
user has access to only their own reports.
Reporting users should also be assigned additional roles that grant
[access to Kibana](https://www.elastic.co/guide/en/kibana/8.19/xpack-security-authorization.html) as well as read
access to the indices that will be used to generate reports.

[[built-in-roles-rollup-admin]] `rollup_admin`::
Grants `manage_rollup` cluster privileges, which enable you to manage and execute all rollup actions.

[[built-in-roles-rollup-user]] `rollup_user`::
Grants `monitor_rollup` cluster privileges, which enable you to perform read-only operations related to rollups.

[[built-in-roles-snapshot-user]] `snapshot_user`::
Grants the necessary privileges to create snapshots of **all** the indices and
to view their metadata. This role enables users to view the configuration of
existing snapshot repositories and snapshot details. It does not grant authority
to remove or add repositories or to restore snapshots. It also does not enable
to change index settings or to read or update data stream or index data.

[[built-in-roles-superuser]] `superuser`::
Grants full access to cluster management and data indices. This role also grants
direct read-only access to restricted indices like `.security`. A user with the
`superuser` role can impersonate any other user in the system.
On Elastic Cloud, all standard users, including those with the `superuser` role are
restricted from performing operator-only actions.
**Important:** This role can manage security and create roles with unlimited privileges.
Take extra care when assigning it to a user.

[[built-in-roles-transform-admin]] `transform_admin`::
Grants `manage_transform` cluster privileges, which enable you to manage
transforms. This role also includes all
[Kibana privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html) for the {ml-features}.

[[built-in-roles-transform-user]] `transform_user`::
Grants `monitor_transform` cluster privileges, which enable you to perform
read-only operations related to transforms. This role also includes all
[Kibana privileges](https://www.elastic.co/guide/en/kibana/8.19/kibana-privileges.html) for the {ml-features}.

[[built-in-roles-transport-client]] `transport_client`::
Grants the privileges required to access the cluster through the Java Transport
Client. The Java Transport Client fetches information about the nodes in the
cluster using the _Node Liveness API_ and the _Cluster State API_ (when
sniffing is enabled). Assign your users this role if they use the
Transport Client.
**Note:** Using the Transport Client effectively means the users are granted access
to the cluster state. This means users can view the metadata over all indices,
index templates, mappings, node and basically everything about the cluster.
However, this role does not grant permission to view the data in all indices.

[[built-in-roles-viewer]] `viewer` ::

Grants read-only access to all features in Kibana (including Solutions) and to data indices.
===============================
* This role provides read access to any index that is not prefixed with a dot.
* This role automatically grants read-only access to new Kibana features as soon as they are available.
===============================

[[built-in-roles-watcher-admin]] `watcher_admin`::
Allows users to create and execute all Watcher actions. Grants read access to
the `.watches` index. Also grants read access to the watch history and the
triggered watches index.

[[built-in-roles-watcher-user]] `watcher_user`::
Grants read access to the `.watches` index, the get watch action and the watcher
stats.
