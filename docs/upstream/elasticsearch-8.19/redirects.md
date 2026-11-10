<!-- Converted from redirects.asciidoc (AsciiDoc). Includes are inlined. -->

# Deleted pages

The following pages have moved or been deleted.

### Node discovery

Refer to Discovery.

#### Troubleshooting node discovery

Refer to Troubleshooting discovery.

### JWT realm

Refer to JWT authentication.

#### Role mapping with JWT

Refer to Authorizing with the role mapping API.

### Feature upgrade APIs

Refer to Feature migration APIs.

### Java transport client and security

The Java transport client has been removed. Use the
https://www.elastic.co/guide/en/elasticsearch/client/java-rest/7.15/java-rest-high.html[Java
high-level REST client] instead. For migration steps, refer to the
https://www.elastic.co/guide/en/elasticsearch/client/java-rest/7.15/java-rest-high-level-migration.html[migration
guide].

### Snapshot lifecycle management (SLM)

See automate-snapshots-slm.

### Tutorial: Automate backups with SLM

See automate-snapshots-slm.

### Security and SLM

See slm-security.

### Snapshot retention

See slm-retention-task.

### Delete a snapshot

See delete-snapshot.

### Monitor snapshot progress

See monitor-snapshot.

### Back up a cluster

See snapshots-take-snapshot.

### Back up a cluster's data

See snapshots-take-snapshot.

### Back up a cluster's configuration

See back-up-config-files.

### Back up a cluster's security configuration

See back-up-config-files and cluster-state-snapshots.

### Encrypting communications in an Elasticsearch Docker Container

Refer to Starting a multi-node cluster with Docker Compose.

### Start a multi-node cluster with TLS enabled

Refer to Starting a multi-node cluster with Docker Compose.

### Cross-cluster search, clients, and integrations

Refer to Securing clients and integrations.

### Cross-cluster search and security

Refer to remote-clusters.

#### Cross-cluster search and Kibana

Refer to remote-clusters.

### Configure cross-cluster replication

Refer to Set up cross-cluster replication.

#### Connect a remote cluster

Refer to Connecting remote clusters.

### Remote clusters

Refer to Remote clusters.

#### Configuring remote clusters

Refer to Connect remote clusters.

#### Remote cluster settings

Refer to Remote clusters settings.

### Restore a cluster's data

See restore-entire-cluster.

### Freeze index API

The freeze index API was removed in 8.0.
Frozen indices are no longer useful due to
https://www.elastic.co/blog/significantly-decrease-your-elasticsearch-heap-memory-usage[recent
improvements in heap memory usage].

### Freeze ILM action

The freeze ILM action was removed in 8.0.
Frozen indices are no longer useful due to
https://www.elastic.co/blog/significantly-decrease-your-elasticsearch-heap-memory-usage[recent
improvements in heap memory usage].

### Freeze ILM action

The freeze ILM action was removed in 8.0.
Frozen indices are no longer useful due to
https://www.elastic.co/blog/significantly-decrease-your-elasticsearch-heap-memory-usage[recent
improvements in heap memory usage].

### Aliases

For field aliases, refer to the alias field type.

For index and data stream aliases, refer to aliases.

### Other security layers

Refer to modules-scripting-security.

### Grok basics

See Grokking grok.

#### Create users

Refer to the `elasticsearch-reset-password` tool for resetting
passwords of built-in users.

### Generate certificates

See Set up basic security for the Elastic Stack.

### Tutorial: Encrypting communications

See Set up basic security for the Elastic Stack.

### Encrypting internode communication

See Set up basic security for the Elastic Stack.

### Tutorial: Getting started with security

See Secure the Elastic Stack.

### Configure Elasticsearch for OpenID Connect authentication

See Configure Elasticsearch for OpenID Connect authentication.

#### Claims mapping

See Claims mapping for OpenID Connect.

### Configuring Kibana

See Configuring Kibana for OpenID Connect.

### Configuring role mappings

See Configuring OpenID Connect role mappings.

### Configure SAML single-sign on

See Configuring SAML single-sign-on on the Elastic Stack.

### Configuring Kibana

See Configuring Kibana for SAML.

### Configure Elasticsearch for SAML authentication

See Configure Elasticsearch for SAML authentication.

#### Attribute mapping

See SAML attribute mapping.

##### User properties

See Elasticsearch user properties.

### Setting up SSL between Elasticsearch and Active Directory

See Encrypting communications between Elasticsearch and Active Directory.

### Security overview

See Secure the Elastic Stack.

### Enable Elasticsearch security features

See Set up minimal security for Elasticsearch.

### Set up TLS on a cluster

See Encrypt internode communication.

### Configure TLS

See Encrypt internode communication.

#### Encrypt HTTP client communications

See Encrypt HTTP client communications.

#### Encrypt internode communication

See Encrypt internode communications.

#### Generating node certificates

See Generate the certificate authority.

### Configure security in Elasticsearch

See Configuring security for the Elastic Stack.

### Encrypting communications

See Configuring security for the Elastic Stack.

### Search user profile API

See Suggest user profile API.

### Stored scripts

See Store and retrieve scripts

### Node name setting

See Node name setting.

### Cluster name setting

See Cluster name setting.

### Heap size settings

See heap-size-settings.

### Leader index retaining operations for replication

See Requirements for leader indices.

### Remedying a follower that has fallen behind

See Recreating a follower index.

### Remote recovery process

See Remote recovery process.

### Leader index requirements

See Requirements for leader indices.

### Cross-cluster replication overview

See Cross-cluster replication.

### Upgrade API

The `_upgrade` API is no longer useful and will be removed.
For information about upgrading, see
{stack-ref}/upgrading-elasticsearch.html[Upgrading Elasticsearch].

### `_parent` field

The `_parent` field has been removed in favour of the `join` field.

### Warmers

Warmers have been removed. There have been significant improvements to the
index that make warmers not necessary anymore.

### Types Exists

The types exists endpoint has been removed. See removal-of-types for
more details.

### X-Pack commands

See commands.

### X-Pack APIs

Elasticsearch X-Pack APIs are now documented in REST APIs.

[role="exclude",id="ml-calendar-resource"]]

### Calendar resources

See ml-get-calendar and
{ml-docs}/ml-ad-run-jobs.html#ml-ad-calendars[Calendars and scheduled events].

### Filter resources

See ml-get-filter and
{ml-docs}/ml-ad-run-jobs.html#ml-ad-rules[Machine learning custom rules].

### Scheduled event resources

See ml-get-calendar-event and
{ml-docs}/ml-ad-run-jobs.html#ml-ad-calendars[Calendars and scheduled events].

### Index APIs

Elasticsearch index APIs are now documented in indices.

### Doc value fields parameter for request body search API

See request-body-search-docvalue-fields.

### Explain parameter for request body search API

See request-body-search-explain.

### Collapse parameter for request body search API

See collapse-search-results.

### From and size parameters for request body search API

See paginate-search-results.

### Highlight parameter for request body search API

See highlighting.

### Index boost parameter for request body search API

See index-boost.

### Inner hits parameter for request body search API

See inner-hits.

### Minimum score parameter for request body search API

See search-api-min-score.

### Named query parameter for request body search API

See named-queries.

### Post filter parameter for request body search API

See post-filter.

### Preference parameter for request body search API

See search-preference.

### Query parameter for request body search API

See request-body-search-query.

### Rescoring parameter for request body search API

See rescore.

### Script fields parameter for request body search API

See script-fields.

### Scroll parameter for request body search API

See scroll-search-results.

### Search after parameter for request body search API

See search-after.

### Search type parameter for request body search API

See search-type.

### Sequence numbers and primary terms parameter for request body search API

See optimistic-concurrency-control.

### Sort parameter for request body search API

See sort-search-results.

### Source filtering parameter for request body search API

See source-filtering.

### Stored fields parameter for request body search API

See stored-fields.

### Track total hits parameter for request body search API

See track-total-hits.

### Version parameter for request body search API

See request-body-search-version.

### Term suggester

See term-suggester.

### Phrase suggester

See phrase-suggester.

### Completion suggester

See completion-suggester.

### Context suggester

See context-suggester.

### Return suggester type

See return-suggesters-type.

### Profiling queries

See profiling-queries.

### Profiling aggregations

See profiling-aggregations.

### Profiling considerations

See profiling-considerations.

### Explain analyze API

See explain-analyze-api.

### Synced flush API

The synced flush API has been removed. Use the flush API
instead. A regular flush has the same effect as a synced flush in 7.6 and later.

### Synced flush API

The synced flush API has been removed. Use the flush API
instead. A regular flush has the same effect as a synced flush in 7.6 and later.

### Snapshot repositories

See snapshots-register-repository.

### Snapshot

See snapshots-take-snapshot.

### Exploring your cluster

See cat.

### Cluster health

See cat-health.

### List all indices

See cat-indices.

### Create an index

See indices-create-index.

### Index and query a document

See getting-started-index.

### Delete an index

See indices-delete-index.

### Modifying your data

See docs-update.

### Indexing/replacing documents

See docs-index_.

### Exploring your data

See getting-started-search.

### Search API

See getting-started-search.

### Cross-cluster search reduction

See ccs-works.

### Administering Elasticsearch

See high-availability.

### Snapshot lifecycle management API

See snapshot-lifecycle-management-api.

### Delete transforms API

See delete-transform.

### Get transform statistics API

See get-transform-stats.

### Get transforms API

See get-transform.

### Preview transforms API

See preview-transform.

### Create transforms API

See put-transform.

### Start transforms API

See start-transform.

### Stop transforms API

See stop-transform.

### Update transforms API

See update-transform.

### Transform APIs

See transform-apis.

### Transform resources

See transform-resource.

### Dest objects

See transform-resource.

#### Source objects

See transform-resource.

#### Pivot objects

See transform-resource.

### Monitoring Elasticsearch

See monitor-elasticsearch-cluster.

### Docker Run

See docker-cli-run-dev-mode.

### Audit logging

See enable-audit-logging.

### Compound word token filters

See analysis-dict-decomp-tokenfilter and
analysis-hyp-decomp-tokenfilter.

### Configuring a native realm

See native-realm-configuration.

#### Native realm settings

See ref-native-settings.

### Configuring a SAML realm

See saml-guide-stack.

#### SAML realm settings

See ref-saml-settings.

#### SAML realm signing settings

See ref-saml-signing-settings.

#### SAML realm encryption settings

See ref-saml-encryption-settings.

#### SAML realm SSL settings

See ref-saml-ssl-settings.

### Configuring a file realm

See file-realm-configuration.

### User search mode and user DN templates mode

See ldap-realm-configuration.

### Configuring an LDAP realm

See ldap-realm-configuration.

### LDAP realm settings

See ref-ldap-settings.

### Setting up SSL between Elasticsearch and LDAP

See tls-ldap.

### Configuring a Kerberos realm

See kerberos-realm-configuration.

### Beats and Security

See:

* {auditbeat-ref}/securing-auditbeat.html[{auditbeat}]
* {filebeat-ref}/securing-filebeat.html[{filebeat}]
* {heartbeat-ref}/securing-heartbeat.html[{heartbeat}]
* {metricbeat-ref}/securing-metricbeat.html[{metricbeat}]
* {packetbeat-ref}/securing-packetbeat.html[{packetbeat}]
* {winlogbeat-ref}/securing-winlogbeat.html[{winlogbeat}]

### Configuring a PKI realm

See pki-realm.

#### PKI realm settings

See ref-pki-settings.

### Configuring an Active Directory realm

See ad-realm-configuration.

### Active Directory realm settings

See ref-ad-settings.

### Mapping Active Directory users and groups to roles

See ad-realm-configuration.

### How security works

See configuring-stack-security.

### Rollup job configuration

See rollup-put-job-api-request-body.

### Job resources

This page was deleted.
See the details in
ml-put-job, ml-update-job, and ml-get-job.

### Datafeed resources

This page was deleted.
See the details in ml-put-datafeed, ml-update-datafeed,
ml-get-datafeed,
ml-get-datafeed-stats.

### Job statistics

This
page
was
deleted.
See
the details in ml-get-job-stats.

### Model snapshot resources

This page was deleted.
See ml-update-snapshot and ml-get-snapshot.

### Transform resources

This page was deleted.
See put-transform, preview-transform, update-transform,
get-transform.

### {dfanalytics-cap} job resources

This page was deleted.
See put-dfanalytics.

### Create trained model API

See put-trained-models.

### Get trained model statistics API

See get-trained-models-stats.

### Get trained model API

See get-trained-models.

### Delete trained model API

See delete-trained-models.

### Transforms  settings in Elasticsearch

See transform-settings.

#### General transforms settings

See general-transform-settings.

### Results resources

This page was deleted.
See ml-get-bucket,
ml-get-bucket,
ml-get-influencer,
ml-get-record,
ml-get-category, and
ml-get-overall-buckets.

### Snapshot module

See snapshot-restore.

#### Repository plugins

See self-managed-repo-types.

#### Change index settings during restore

See restore-snapshot-api-index-settings.

### Restore snapshot

See snapshots-restore-snapshot.

### Snapshot repositories

See snapshots-register-repository.

### Analysis configuration objects

This page was deleted.
See put-dfanalytics.

### SLM delete policy API

See slm-api-delete-policy.

### SLM execute lifecycle API

See slm-api-execute-lifecycle.

### SLM execute lifecycle API

See slm-api-execute-lifecycle.

### SLM get policy API

See slm-api-get-policy.

### SLM get stats API

See slm-api-get-stats.

### SLM status API

See slm-api-get-status.

### SLM put policy API

See slm-api-put-policy.

### Start snapshot lifecycle management API

See slm-api-start.

### Stop snapshot lifecycle management API

See slm-api-stop.

### How cross-cluster search works

See ccs-gateway-seed-nodes and ccs-min-roundtrips.

### Component template APIs

See index template APIs.

### Indices module

See:

* circuit-breaker
* indexing-buffer
* modules-fielddata
* query-cache
* recovery
* search-settings
* shard-request-cache

### Testing

This page was deleted.
Information about the Java testing framework was removed
([#55257](https://github.com/elastic/elasticsearch/issues/55257)) from the Elasticsearch Guide
because it was out of date and erroneously implied that it should be used by application developers.
There is an issue ([#55258](https://github.com/elastic/elasticsearch/issues/55258))
for providing general testing guidance for applications that communicate with Elasticsearch.

### Java testing framework

This page was deleted.
Information about the Java testing framework was removed
([55257](https://github.com/elastic/elasticsearch/issues/55257)) from the Elasticsearch Guide because it was out of date and
erroneously implied that it should be used by application developers.

There is an issue ([#55258](https://github.com/elastic/elasticsearch/issues/55258)) for providing general testing
guidance for applications that communicate with Elasticsearch.

### Why randomized testing?

This page was deleted.
Information about the Java testing framework was removed
([55257](https://github.com/elastic/elasticsearch/issues/55257)) from the Elasticsearch Guide
because it was out of date and erroneously implied that it should be used by application developers.
There is an issue ([#55258](https://github.com/elastic/elasticsearch/issues/))
for providing general testing guidance for applications that communicate with Elasticsearch.

### Using the Elasticsearch test classes

This page was deleted.
Information about the Java testing framework was removed
([55257](https://github.com/elastic/elasticsearch/issues/55257)) from the Elasticsearch Guide
because it was out of date and erroneously implied that it should be used by application developers.
There is an issue ([#55258](https://github.com/elastic/elasticsearch/issues/55258))
for providing general testing guidance for applications that communicate with Elasticsearch.

### Unit tests

This page was deleted.
Information about the Java testing framework was removed
([55257](https://github.com/elastic/elasticsearch/issues/55257)) from the Elasticsearch Guide
because it was out of date and erroneously implied that it should be used by application developers.
There is an issue ([#55258](https://github.com/elastic/elasticsearch/issues/55258))
for providing general testing guidance for applications that communicate with Elasticsearch.

### Integration tests

This page was deleted.
Information about the Java testing framework was removed
([55257](https://github.com/elastic/elasticsearch/issues/55257)) from the Elasticsearch Guide
because it was out of date and erroneously implied that it should be used by application developers.
There is an issue ([#55258](https://github.com/elastic/elasticsearch/issues/55258))
for providing general testing guidance for applications that communicate with Elasticsearch.

#### Number of shards

This section was deleted.

#### Generic helper methods

This section was deleted.

#### Test cluster methods

This section was deleted.

#### Changing node settings

This section was deleted.

#### Accessing clients

This section was deleted.

#### Scoping

This section was deleted.

#### Changing plugins via configuration

This section was deleted.

### Randomized testing

This page was deleted.

#### Generating random data

This section was deleted.

### Assertions

This page was deleted.

### ILM actions

See ilm-actions.

#### Allocate action

See ilm-allocate.

#### Delete action

See ilm-delete.

#### Force merge action

See ilm-forcemerge.

#### Migrate action

See ilm-migrate.

#### Read only action

See ilm-readonly.

#### Rollover action

See ilm-rollover.

#### Searchable snapshot action

See ilm-searchable-snapshot.

#### Set priority action

See ilm-set-priority.

#### Shrink action

See ilm-shrink.

#### Unfollow action

See ilm-unfollow.

#### Wait for snapshot action

See ilm-wait-for-snapshot.

### ILM policy definition

See ilm-index-lifecycle.

### URI search

See search-search.

### Dangling indices

See dangling-indices.

### Cluster-level shard allocation

See cluster-shard-allocation-settings.

### Disk-based shard allocation

See disk-based-shard-allocation.

### Shard allocation awareness

See shard-allocation-awareness.

### Cluster-level shard allocation filtering

See cluster-shard-allocation-filtering.

### Miscellaneous cluster settings

See misc-cluster-settings.

### Modules

This page has been removed.

See Configuring Elasticsearch for settings information:

* circuit-breaker
* modules-cluster
* modules-discovery-settings
* modules-fielddata
* recovery
* indexing-buffer
* modules-gateway
* modules-network
* query-cache
* search-settings
* shard-request-cache

For other information, see:

* modules-threadpool
* modules-node
* modules-plugins
* remote-clusters

### HTTP

See Networking.

### Transport

See Networking.

### Adding and removing nodes

See add-elasticsearch-nodes.

### Timing

See ilm-phase-transitions.

### Installation

See install-elasticsearch.

### `_ttl` mappings

The `_ttl` mappings have been removed. As a replacement for `_ttl`
mappings, we recommend using ILM to create
time-based indices.

### Running as a service on Linux

See starting-elasticsearch.

### Painless syntax

See {painless}/painless-lang-spec.html[Painless language specification].

### Using policies to manage index rollover

See getting-started-index-lifecycle-management.

### Applying a policy to our index

See ilm-gs-apply-policy.

### Directory layout

See settings.

### Scan and scroll

See scroll-search-results.

### Dynamic mapping

See dynamic-mapping.

### Applying a policy to an index template

See ilm-gs-apply-policy.

### Index status API

The index `_status` API has been replaced with the <<indices-stats,index
stats>> and index recovery APIs.

### Search facets

See search-aggregations.

### Executing searches

See getting-started-search.

### Mapping root object type

Mapping types have been removed. See mapping.

### Query DSL filters

See query-filter-context.

### {esms}

We have stopped adding new customers to our {esms}.

If you are interested in similar capabilities, contact
[Elastic Support](https://support.elastic.co) to discuss available options.

### Manage existing periodic indices with ILM

See ilm-existing-indices-apply.

### Reindexing via ILM

See ilm-existing-indices-reindex.

### Path hierarchy tokenizer examples

See analysis-pathhierarchy-tokenizer-detailed-examples.

### Tribe node

Tribe node functionality has been removed in favor of cross-cluster search. See
modules-cross-cluster-search.

### Release highlights

See release-highlights.

### SQL access settings in Elasticsearch

The `xpack.sql.enabled` setting has been deprecated. SQL access is always enabled.

### Index templates [[getting]]

See index-templates.

### Index template exists (legacy)

See indices-template-exists-v1.

### Run a search

See run-an-es-search.

### How highlighters work internally

See how-es-highlighters-work-internally.

### Run an EQL search

See run-an-eql-search.

### EQL limitations

See eql-syntax-limitations.

### EQL requirements

See eql-required-fields.

### Tableau Desktop

See sql-client-apps-tableau-desktop and sql-client-apps-tableau-server.

### Request body search

This page has been removed.

For search API reference documentation, see search-search.

For search examples, see search-your-data.

#### Doc value fields

See doc value fields.

#### Fast check for any matching docs

See quickly-check-for-matching-docs.

#### Field collapsing

See collapse-search-results.

#### From / size

See paginate-search-results.

#### Highlighting

See highlighting.

#### How highlighters work internally

See how-es-highlighters-work-internally.

#### Index boost

See index-boost.

#### Inner hits

See inner-hits.

#### `min_score`

See the `min_score` parameter.

#### Named queries

See named-queries.

#### Post filter

See post-filter.

#### Preference

See search-preference.

#### Rescoring

See rescore.

#### Script fields

See script-fields.

#### Scroll

See scroll-search-results.

#### Clear scroll API

See clear-scroll-api.

#### Sliced scroll

See slice-scroll.

#### Search after

See search-after.

#### Search type

See search-type.

#### Sort

See sort-search-results.

#### Source filtering

See source-filtering.

#### Stored fields

See stored-fields.

#### Track total hits

See track-total-hits.

### Joining queries notes

See joining-queries-notes.

### Percolate query notes

See percolate-query-notes.

### Point in time API

See point-in-time-api.

### Constant keyword field type

See constant-keyword-field-type.

### Wildcard field type

See wildcard-field-type.

### Searchable snapshot repository statistics API

We have removed documentation for this API. This a low-level API used to get
information about searchable snapshot indices. We plan to remove or drastically
change this API as part of a future release.

For other searchable snapshot APIs, see searchable-snapshots-apis.

### Avoid oversharding

See size-your-shards.

### elasticsearch-croneval parameters

See elasticsearch-croneval-parameters.

### Autoscaling decision API

The autoscaling decision API has been renamed to capacity,
see autoscaling-get-autoscaling-capacity.

### Caching heavy aggregations

See agg-caches.

### Returning only aggregation results

See return-only-agg-results.

### Aggregation metadata

See add-metadata-to-an-agg.

### Returning the type of the aggregation

See return-agg-type.

### Indexing aggregation results with transforms

See transforms.

### Matrix aggregations

See search-aggregations-matrix-stats-aggregation.

### Moving average aggregation

The moving average aggregation has been removed. Use the
moving function aggregation
instead.

### `fielddata` mapping parameter

See fielddata-mapping-param.

### Pipeline definition

See ingest.

### Accessing data in pipelines

See access-source-fields, access-metadata-fields, and
access-ingest-metadata.

### Conditional execution in pipelines

See conditionally-run-processor.

### Handling nested fields in conditionals

See conditionally-run-processor.

### Complex conditionals

See conditionally-run-processor.

### Conditionals with the pipeline processor

See conditionally-apply-pipelines.

### Conditionals with the regular expressions

See conditionally-run-processor.

### Handling failures in pipelines

See handling-pipeline-failures.

### Ingest processors

See processors.

### Enrich policy definition

See put-enrich-policy-api.

### Rollup API

See rollup-apis.

### Get Elasticsearch up and running

See configuring-stack-security.

### Index some documents

See {estc-welcome}/getting-started-general-purpose.html#gp-gs-add-data[Add data].

### Start searching

See {estc-welcome}/getting-started-general-purpose.html#gp-gs-search-data[Search and sort data].

### Analyze results with aggregations

See search-aggregations.

### Setting JVM options

See set-jvm-options.

### Terms enum API

See search-terms-enum.

### Frozen indices

For API documentation, see unfreeze-index-api.

### Best practices for frozen indices

For API documentation, see unfreeze-index-api.

### Searching a frozen index

For API documentation, see unfreeze-index-api.

### Monitoring frozen indices

For API documentation, see unfreeze-index-api.

### Glossary

See the {glossary}/terms.html[Elastic glossary].

### Multi-target syntax

See api-multi-index.

#### Hidden data streams and indices

See multi-hidden.

### Date math support in system and index alias names

See api-date-math-index-names.

### Cron expressions

See api-cron-expressions.

### URL-based access control

See api-url-access-control.

### Field usage stats API

See field-usage-stats.

### Enroll Kibana API

See security-api-kibana-enrollment.

### Supported REST parameters for SQL search API

See the request body parameters for the
SQL search API.

### Full cluster restart upgrade

When upgrading to Elasticsearch 8.0 and later, you must first upgrade to {prev-major-last}
even if you opt to perform a full-cluster restart instead of a rolling upgrade.
For more information about upgrading, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].

### Rolling upgrade

When upgrading to Elasticsearch 8.0 and later, you must first upgrade to {prev-major-last}
whether you opt to perform a rolling upgrade (upgrade one node at a time) or a full-cluster restart upgrade.
For more information about upgrading, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].

### Reindex before upgrading

Before upgrading to Elasticsearch 8.0 and later, you must reindex any indices created in
a 6.x version. We recommend using the **Upgrade Assistant** to guide you
through this process.

For more information about upgrading, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].

For more information about reindexing, refer to docs-reindex.

### Reindex in place

Before upgrading to Elasticsearch 8.0 and later, you must reindex any indices created in
a 6.x version. We recommend using the **Upgrade Assistant** to guide you
through this process.

For more information about upgrading, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].
For more information about reindexing, refer to docs-reindex.

### Reindex from a remote cluster

Before upgrading to Elasticsearch 8.0 and later, you must reindex any indices created in
a 6.x version. We recommend using the **Upgrade Assistant** to guide you
through this process.

For more information about upgrading, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].
For more information about reindexing from a remote cluster, refer to
reindex-from-remote.

### Infer trained model deployment API

See infer-trained-model.

### Watching event data

This example has been removed, as the Meetup.com streaming API has been
discontinued.

Refer to example-watches for other Watcher examples.

### Fix watermark errors

Refer to fix-watermark-errors.

### Delete the lifecycle of a data stream

Refer to Delete data stream lifecycle API.

### Explain the lifecycle of a data stream

Refer to Explain data stream lifecycle API.

### Get the lifecycle of a data stream

Refer to Get data stream lifecycle API.

### Update the lifecycle of a data stream

Refer to Update data stream lifecycle API.

### Get synonyms set API

See get-synonyms-set

### Delete synonyms sets API

See delete-synonyms-set

### Create or delete synonyms sets API

See put-synonyms-set

### Remote clusters

Refer to remote-clusters

#### Dynamically configure remote clusters

Refer to remote-clusters.

### Configure roles and users for remote clusters

Refer to remote-clusters.

### Create or update geoip database configuration API

Refer to put-ip-location-database-api.

### Get geoip database configuration

Refer to get-ip-location-database-api.

### Delete geoip database configuration API

Refer to delete-ip-location-database-api.
