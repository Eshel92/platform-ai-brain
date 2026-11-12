<!-- Part 26 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.8.2

Review the following information about the Kibana 8.8.2 release.

### Known issues

**Kibana can run out of memory during an upgrade when there are many Fleet agent policies.**
*Details* +
Due to a schema version update, during Fleet setup in 8.8.x, all agent policies are being queried and deployed.
This action triggers a lot of queries to the Elastic Package Registry (EPR) to fetch integration packages.  As a result,
there is an increase in Kibana's resident memory usage (RSS).

*Impact* +
Because the default batch size of `100` for schema version upgrade of Fleet agent policies is too high, this can
cause Kibana to run out of memory during an upgrade.  For example, we have observed 1GB Kibana instances run
out of memory during an upgrade when there were 20 agent policies with 5 integrations in each.

*Workaround* +
Two workaround options are available:

* Increase the Kibana instance size to 2GB. So far, we are not able to reproduce the issue with 2GB instances.
* Set `xpack.fleet.setup.agentPolicySchemaUpgradeBatchSize` to `2` in the `kibana.yml` and restart the Kibana instance(s).

In 8.9.0, we are addressing this by changing the default batch size to `2`.

### Bug fixes

APM::
* Fixes the latency graph displaying all service transactions, rather than the selected one, on the transaction detail page {kibana-pull}159085[#159085]

Dashboard::
* Fixes styling of top nav bar {kibana-pull}159754[#159754]
* Fixes alias redirect and update error handling {kibana-pull}159742[#159742]
* Fixes time range regression {kibana-pull}159337[#159337]

Elastic Security::
For the Elastic Security 8.8.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Enterprise Search::
For the Elastic Enterprise Search 8.8.2 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].

Fleet::
* Fixes usage of AsyncLocalStorage for audit log {kibana-pull}159807[#159807]
* Fixing issue of returning output API key {kibana-pull}159179[#159179]

Logs::
* Fixes log categorization UI failure due to an infinite loop {kibana-pull}159090[#159090]

Machine Learning::
* Hiding pattern analysis button for non-time series data {kibana-pull}160051[#160051]
* Fixes blocking forced downgrades/installation if indices can't be deleted {kibana-pull}159814[#159814]

Maps::
* Fixes layer group loading indicator always on when group has non-visible layer {kibana-pull}159517[#159517]
* Fixes geo line source not loading unless the Maps application is open {kibana-pull}159432[#159432]
* Fixes Maps orphan sources on layer deletion {kibana-pull}159067[#159067]

Monitoring::
* Permanently hide the telemetry notice on dismissal {kibana-pull}159893[#159893]

Observability::
* Handle buildEsQuery error (such as leading wildcard) in status change {kibana-pull}159891[#159891]

Platform::
* Fixes global search crash on missing tag {kibana-pull}159196[#159196]
* Fixes a regression where the "saved_object_resolve" audit action was not being logged per object {kibana-pull}160014[#160014]

Uptime::
* Ensures that users can configure custom `Content-Type` headers for HTTP monitors in the Synthetics app {kibana-pull}159737[#159737]
* Fixes an issue where alerting on Synthetics monitors was sometimes delayed {kibana-pull}159511[#159511]


## Kibana 8.8.1

Review the following information about the Kibana 8.8.1 release.

### Known issues

**Kibana can run out of memory during an upgrade when there are many Fleet agent policies.**
*Details* +
Due to a schema version update, during Fleet setup in 8.8.x, all agent policies are being queried and deployed.
This action triggers a lot of queries to the Elastic Package Registry (EPR) to fetch integration packages.  As a result,
there is an increase in Kibana's resident memory usage (RSS).

*Impact* +
Because the default batch size of `100` for schema version upgrade of Fleet agent policies is too high, this can
cause Kibana to run out of memory during an upgrade.  For example, we have observed 1GB Kibana instances run
out of memory during an upgrade when there were 20 agent policies with 5 integrations in each.

*Workaround* +
Two workaround options are available:

* Increase the Kibana instance size to 2GB. So far, we are not able to reproduce the issue with 2GB instances.
* Set `xpack.fleet.setup.agentPolicySchemaUpgradeBatchSize` to `2` in the `kibana.yml` and restart the Kibana instance(s).

In 8.9.0, we are addressing this by changing the default batch size to `2`.

**Memory leak in Fleet audit logging.**
*Details* +
Fleet introduced audit logging for various CRUD (create, read, update, and delete) operations in version 8.8.0.

While audit logging is not enabled by default, we have identified an off-heap memory leak in the implementation of Fleet audit logging that can result in poor Kibana performance, and in some cases Kibana instances being terminated by the OS kernel's oom-killer. This memory leak can occur even when Kibana audit logging is not explicitly enabled (regardless of whether `xpack.security.audit.enabled` is set in the `kibana.yml` settings file).

*Impact* +
The version 8.8.2 release includes in {kibana-pull}159807[a fix] for this problem. If you are using Fleet integrations
and Kibana audit logging in version 8.8.0 or 8.8.1, you should upgrade to 8.8.2 or above to obtain the fix.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.8.1, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in the Kibana 8.8.1 release.

To review the breaking changes in the previous release, check {kibana-ref-all}/8.8/release-notes-8.8.0.html#breaking-changes-8.8.0[8.8.0].

### Enhancements

Elastic Security::
For the Elastic Security 8.8.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
* Add Elastic Agent UI instructions for Universal Profile {kibana-pull}158936[#158936]

### Bug fixes

Alerting::
* Fixes a bug where ML embeddables, OsQuery, and IoCs attachments in a case render the wrong view {kibana-pull}158441[#158441]
* Makes alert links shorter {kibana-pull}158582[#158582]
* Throws a Mustache error when validating action message for warnings {kibana-pull}158668[#158668]
* Adds null checks when iterating through an index template list {kibana-pull}158742[#158742]

APM::
* Displays the size of hidden indices in storage explorer {kibana-pull}158746[#158746]
* Changes the APM latency value and latency threshold to microseconds {kibana-pull}158703[#158703]
* Fixes service transaction metrics by using `transaction.duration.histogram` for percentile aggregations {kibana-pull}158909[#158909]

Discover::
* Update single doc view locator to URL encode `rowId` {kibana-pull}158635[#158635]
* Fixes the display of grid row selection when in dark mode {kibana-pull}158231[#158231]

Elastic Security::
For the Elastic Security 8.8.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
* Include hidden data streams in package upgrade {kibana-pull}158654[#158654]

Logs::
* Fixes Log Categorization UI failure due to an infinite loop {kibana-pull}159090[#159090]

Machine Learning::
* Increases calendar events request limit {kibana-pull}158726[#158726]
* Disables the delete option for deployed models {kibana-pull}158533[#158533]
* Applies theme based on the User Profile settings {kibana-pull}158258[#158258]

Maps::
* Fixes toolbar action button not filled when selected {kibana-pull}158284[#158284]
* Fixes Maps to display dark theme when enabled {kibana-pull}158219[#158219]

Operations::
* Fixes configuration stacking order {kibana-pull}158827[#158827]

Platform::
* Fixes Kibana crashing on Safari versions prior to 16.4 {kibana-pull}158825[#158825]
* Updates all aliases with a single `updateAliases()` when relocating saved objects {kibana-pull}158940[#158940]
* Fixes a race condition that could cause intermittent upgrade migration failures when Kibana connects to a single node Elasticsearch cluster {kibana-pull}158182[#158182]
* Dynamically reduces the `migrations.batchSize` value when Kibana encounters a migration batch that's too big to process {kibana-pull}157494[#157494]
