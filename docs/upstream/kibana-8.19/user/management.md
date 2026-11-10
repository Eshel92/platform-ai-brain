<!-- Converted from user/management.asciidoc (AsciiDoc). Includes are inlined. -->

# Stack Management

*Stack Management* is home to UIs for managing all things Elastic Stack&mdash;
indices, clusters, licenses, UI settings, data views, spaces, and more.

Access to individual features is governed by Elasticsearch and Kibana privileges.
Consult your administrator if you do not have the appropriate access.

## Ingest

|===

| [Ingest Pipelines](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ingest.html)
| Create and manage ingest pipelines that let you perform common transformations
and enrichments on your data.

| {logstash-ref}/logstash-centralized-pipeline-management.html[Logstash Pipelines]
| Create, edit, and delete your Logstash pipeline configurations.

|===

## Data

|===

a| [Index Management](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index-mgmt.html)
| View index settings, mappings, and statistics and perform operations, such as refreshing,
flushing, and clearing the cache. Practicing good index management ensures
that your data is stored cost effectively.

| [Index Lifecycle Policies](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index-lifecycle-management.html)
|Create a policy for defining the lifecycle of an index as it ages
through the hot, warm, cold, and delete phases.
Such policies help you control operation costs
because you can put data in different resource tiers.

| [Snapshot and Restore](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/snapshot-restore.html)
|Define a policy that creates, schedules, and automatically deletes snapshots to ensure that you
have backups of your cluster in case something goes wrong.

| Rollup Jobs
| deprecated:[8.11.0,'Rollups are deprecated and will be removed in a future version. Use downsampling instead.'] Create a job that periodically aggregates data from one or more indices, and then
rolls it into a new, compact index. Rollup indices are a good way to store months or
years of historical data in combination with your raw data.

| [Transforms](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/transforms.html)
|Use transforms to pivot existing Elasticsearch indices into summarized or entity-centric indices.

| [Cross-Cluster Replication](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ccr-getting-started.html)
|Replicate indices on a remote cluster and copy them to a follower index on a local cluster.
This is important for
disaster recovery. It also keeps data local for faster queries.

| [Remote Clusters](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ccr-getting-started.html#ccr-getting-started-remote-cluster)
|Manage your remote clusters for use with cross-cluster search and cross-cluster replication.
You can add and remove remote clusters, and check their connectivity.
|===

## Alerts and Insights

|===

| {rules-ui}
| Centrally manage your rules across Kibana.

| Cases
| Create and manage cases to investigate issues.

| {connectors-ui}
| Create and manage reusable connectors for triggering actions.

| Reporting
| Monitor the generation of reports&mdash;PDF, PNG, and CSV&mdash;and download reports that you previously generated.
A report can contain a dashboard, visualization, table with Discover search results, or Canvas workpad.

| Machine Learning Jobs
| View, export, and import your anomaly detection and
{dfanalytics} jobs. Open the Single Metric
Viewer or Anomaly Explorer to see your anomaly detection results.

| Watcher
| Detect changes in your data by creating, managing, and monitoring alerts.
For example, you might create an alert when the maximum total CPU usage on a machine goes
above a certain percentage.

| Maintenance windows
| Suppress rule notifications for scheduled periods of time.

|===

## Security

|===

a| Users
|View the users that have been defined on your cluster.
Add or delete users and assign roles that give users
specific privileges.

| Roles
|View the roles that exist on your cluster. Customize
the actions that a user with the role can perform, on a cluster, index, and space level.

| API Keys
| Create secondary credentials so that you can send requests on behalf of the user.
Secondary credentials have the same or lower access rights.

| Role Mappings
| Assign roles to your users using a set of rules. Role mappings are required
when authenticating via an external identity provider, such as Active Directory,
Kerberos, PKI, OIDC, and SAML.

|===

## Kibana

|===

a| Data Views
|Manage the fields in the data views that retrieve your data from Elasticsearch.

| Saved Objects
| Copy, edit, delete, import, and export your saved objects.
These include dashboards, visualizations, maps, data views, Canvas workpads, and more.

| Tags
|Create, manage, and assign tags to your saved objects.

| Search Sessions
| Manage your saved search sessions, groups of queries that run in the background.
Search sessions are useful when your queries take longer than usual to process,
for example, when you have a large volume of data or when the performance of your storage location is slow.

| Spaces
| Create spaces to organize your dashboards and other saved objects into categories.
A space is isolated from all other spaces,
so you can tailor it to your needs without impacting others.

a| Advanced Settings
| Customize Kibana to suit your needs. Change the format for displaying dates, turn on dark mode,
set the timespan for notification messages, and much more.

|===

## Stack

|===

| License Management
| View the status of your license, start a trial, or install a new license. For
the full list of features that are included in your license,
see the [subscription page](https://www.elastic.co/subscriptions).

|===

(See `management/cases/cases.md`)
(See `management/cases/setup-cases.md`)
(See `management/cases/manage-cases.md`)
(See `management/cases/manage-cases-settings.md`)
(See `management/action-types.md`)
(See `management/managing-licenses.md`)
(See `management/maintenance-windows/maintenance-windows.md`)
(See `management/manage-data-views.md`)
(See `management/numeral.md`)
(See `management/rollups/create_and_manage_rollups.md`)
(See `management/managing-saved-objects.md`)
(See `management/saved-objects/saved-object-ids.md`)
(See `user/security/index.md`)
(See `spaces/index.md`)
(See `management/advanced-options.md`)
(See `management/managing-tags.md`)
(See `management/upgrade-assistant.md`)
(See `management/watcher-ui/index.md`)
