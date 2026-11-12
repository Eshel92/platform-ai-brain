<!-- Part 42 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.0.0

Review the Kibana 8.0.0 changes, then use the {kibana-ref-all}/7.17/upgrade-assistant.html[Upgrade Assistant] to complete the upgrade.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.0.0, review the breaking change, then mitigate the impact to your application.

**Removes the `console.ssl` setting**
*Details* +
The `console.ssl` setting has been removed. For more information, refer to {kibana-pull}123754[#123754].

*Impact* +
Before you upgrade to 8.0.0, remove `console.ssl` from kibana.yml.

To review the breaking changes in previous versions, refer to the following:

8.0.0-rc2 | 8.0.0-rc1 | 8.0.0-beta1 | 8.0.0-alpha2 |
8.0.0-alpha1

### Deprecation

The following functionality is deprecated in 8.0.0, and will be removed in 9.0.0.
Deprecated functionality does not have an immediate impact on your application, but we strongly recommend
you make the necessary updates after you upgrade to 8.0.0.

**Removes support for `monitoring.cluster_alerts.allowedSpaces`**
*Details* +
The `monitoring.cluster_alerts.allowedSpaces` setting, which Kibana uses to create Stack Monitoring alerts, has been removed. For more information, refer to {kibana-pull}123229[#123229].

*Impact* +
Before you upgrade to 8.0.0, remove `monitoring.cluster_alerts.allowedSpaces` from kibana.yml.

To review the deprecations in previous versions, refer to the following:

8.0.0-rc1 | 8.0.0-alpha1

### Known issue

**Importing and copying saved objects causes weak links to break**
*Details* +
Kibana supports weak links in some saved objects. For example, a dashboard may include a Markdown panel that contains a relative URL to
another dashboard. Weak links are defined by free text, _not_ the saved object's relationships, and can break if **both** of the following
conditions are true:

* You are importing saved objects into multiple spaces, _OR_ you are copying saved objects into another space
* Before you upgraded to 8.0.0, the saved objects did not already exist in the destinations

In 8.0.0 and later, weak links break because saved object IDs can change during import or copy.
This applies to both the UI and the API.
For more information, refer to {kibana-issue}123550[#123550].

*Impact* +
Saved objects in 7.x that are migrated during upgrade are **not** impacted.
Only _new_ saved objects that are imported or copied _multiple times_ (causing object IDs to change) are impacted.
If you are impacted, you can re-import or re-copy your saved objects after the fix is
implemented to preserve the weak links.

### Features

For information about the features introduced in 8.0.0, refer to What's new in 8.0.

Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

To review the features in previous versions, refer to the following:

8.0.0-rc2 | 8.0.0-rc1 | 8.0.0-beta1 | 8.0.0-alpha2

### Enhancements and bug fixes

For detailed information about the 8.0.0 release, review the enhancements and bug fixes.

#### Enhancements

Dashboard::
Clone ReferenceOrValueEmbeddables by value {kibana-pull}122199[#122199]

Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

#### Bug fixes

APM::
Restrict aggregated transaction metrics search to date range {kibana-pull}123445[#123445]

Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
Allow empty strings for required text fields in package policies {kibana-pull}123610[#123610]

Maps::
Fixes Label border color is not removed from legend when disabled {kibana-pull}122705[#122705]

Monitoring::
Ensure logstash getNodes always contains a uuid {kibana-pull}124201[#124201]

Security::
Long-running requests no longer cause sporadic logouts in certain cases, even when user sessions are active {kibana-pull}122155[#122155]


## Kibana 8.0.0-rc2

For information about the Kibana 8.0.0-rc2 release, review the following information.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

**Removes the ability to use `elasticsearch.username: elastic` in production**
*Details* +
In production, you are no longer able to use the `elastic` superuser to authenticate to Elasticsearch. For more information, refer to {kibana-pull}122722[#122722].

*Impact* +
When you configure `elasticsearch.username: elastic`, Kibana fails.

To review the breaking changes in previous versions, refer to the following:

8.0.0-rc1 | 8.0.0-beta1 | 8.0.0-alpha2 |
8.0.0-alpha1

### Features

Kibana 8.0.0-rc2 adds the following new and notable features.

Dashboard::
Dashboard Integration {kibana-pull}115991[#115991]
Elastic Security::
For the Elastic Security 8.0.0-rc2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Monitoring::
Enterprise Search Stack Monitoring {kibana-pull}114303[#114303]
Observability::
* Adds Agent Keys in APM settings - Create agent keys {kibana-pull}120373[#120373]
* Adds Agent Keys in APM settings - Agent key table {kibana-pull}119543[#119543]
* Allows users to set Download Speed, Upload Speed, and Latency for their synthetic monitors in Uptime {kibana-pull}118594[#118594]
Platform::
Changes saved objects management inspect view to a read-only JSON view of the whole saved object {kibana-pull}112034[#112034]

### Enhancements and bug fixes

For detailed information about the 8.0.0-rc2 release, review the enhancements and bug fixes.

#### Enhancements

Elastic Security::
For the Elastic Security 8.0.0-rc2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Security::
Adds session cleanup audit logging {kibana-pull}122419[#122419]
Observability::
Make a monitor's steps details page work on mobile resolutions in Uptime {kibana-pull}122171[#122171]

#### Bug fixes

Alerting::
Fixes PagerDuty timestamp validation {kibana-pull}122321[#122321]
Dashboard::
* Creates Explicit Diffing System {kibana-pull}121241[#121241]
* Fixes blank panel save and display issue {kibana-pull}120815[#120815]
* Fixes full screen error when pressing back arrow on browser {kibana-pull}118113[#118113]
Elastic Security::
For the Elastic Security 8.0.0-rc2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Maps::
* Fixes Point to point and Tracks layers label properties not showing in the legend {kibana-pull}122993[#122993]
* Fixes Color ramp UI for percent of a top term in join layer is broken {kibana-pull}122718[#122718]
Observability::
* Updates index pattern permission error in APM {kibana-pull}122680[#122680]
* Honor time unit for Inventory Threshold in Metrics {kibana-pull}122294[#122294]
* Adds locator to aid other plugins in linking properly to Uptime {kibana-pull}123004[#123004]
* Fixes a bug in which headers would be incorrectly centered on desktop in Uptime {kibana-pull}122643[#122643]


## Kibana 8.0.0-rc1

Review the Kibana 8.0.0-rc1 changes, then use the Upgrade Assistant to complete the upgrade.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

**Splits package policy `upgrade` endpoint for Fleet**
*Details* +
For package policy upgrades, the packagePolicy `upgrade` endpoint format supports a mutative upgrade operation (when `dryRun: false`) and a read-only dry run operation (when `dryRun: true`):

 POST /package_policies/upgrade
 {
   packagePolicyIds: [...],
   dryRun: false
 }

For more information, refer to {kibana-pull}118854[#118854].

*Impact* +
The endpoint is now split into two separate endpoints:

 POST /package_policies/upgrade
 {
   packagePolicyIds: [...]
 }

 POST /package_policies/upgrade/dry_run
 {
   packagePolicyIds: [...]
 }

**Removes APM jobs from Machine Learning**
*Details* +
APM Node.js and RUM JavaScript anomaly detection job modules have been removed. For more information, refer to {kibana-pull}119945[#119945].

*Impact* +
When you upgrade to 8.0.0, you are unable to create and view the APM Node.js and RUM JavaScript jobs in Machine Learning.

**Fails migrations for unknown types**
*Details* +
Unknown saved object types now cause Kibana migrations to fail. For more information, refer to {kibana-issue}107678[#107678].

*Impact* +
To complete the migration, re enable plugins or delete documents from the index in the previous version.

**Removes deprecated config fields from Logs and Metrics APIs and saved objects**
*Details* +
On the Logs and Metrics UIs, references to the following API and saved object deprecated fields have been removed:

* `timestamp`
* `tiebreaker`
* `container`
* `pod`
* `host`

For more information, refer to {kibana-pull}116821[#116821] and {kibana-pull}115874[#115874].

*Impact* +
When you upgrade to 8.0.0, you are unable to use references to the deprecated fields.

To review the breaking changes in previous versions, refer to the following:

8.0.0-beta1 | 8.0.0-alpha2 |
8.0.0-alpha1

### Deprecations

Deprecated functionality does not have an immediate impact on your application, but we strongly recommend you make the necessary updates after you complete the upgrade.

**Renames the `autocreate` data view APM setting**
*Details* +
The `xpack.apm.autocreateApmIndexPattern` APM setting has been removed. For more information, refer to {kibana-pull}120689[#120689].

*Impact* +
To automatically create data views in APM, use `xpack.apm.autoCreateApmDataView`.

**Updates Fleet API to improve consistency**
*Details* +
The Fleet API has been updated to improve consistency:

* Hyphens are changed to underscores in some names.
* The `pkgkey` path parameter in the packages endpoint is split.
* The `response` and `list` properties are renamed to `items` or `item` in some
responses.

For more information, refer to {kibana-pull}119494[#119494].

*Impact* +
When you upgrade to 8.0.0, use the following API changes:

* Use `enrollment_api_keys` instead of `enrollment-api-keys`.

* Use `agent_status` instead of `agent-status`.

* Use `service_tokens` instead of `service-tokens`.

* Use `/epm/packages/{packageName}/{version}` instead of `/epm/packages/{pkgkey}`.

* Use `items[]` instead of `response[]` in:
/api/fleet/enrollment_api_keys
/api/fleet/agents
/epm/packages/
/epm/categories
/epm/packages/_bulk
/epm/packages/limited
/epm/packages/{packageName}/{version} <1>
<1> Use `items[]` when the verb is `POST` or `DELETE`. Use `item` when the verb
is `GET` or `PUT`.

For more information, refer to {fleet-guide}/fleet-api-docs.html[Fleet APIs].

To review the deprecations in previous versions, refer to the 8.0.0-alpha1 release notes.

### Features

Kibana 8.0.0-rc1 adds the following new and notable features.

Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Management::
Display managed badge for transforms {kibana-pull}117679[#117679]
Monitoring::
Enterprise Search Stack Monitoring {kibana-pull}114303[#114303]
Observability::
* Adds ability to create agent keys in APM settings {kibana-pull}120373[#120373]
* Adds Agent key table in APM settings {kibana-pull}119543[#119543]
* Allows users to set Download Speed, Upload Speed, and Latency for their synthetic monitors {kibana-pull}118594[#118594]

### Enhancements and bug fixes

For detailed information about the 8.0.0-rc1 release, review the enhancements and bug fixes.

### Enhancements

Canvas::
Reverts By-Value Embeddables {kibana-pull}117613[#117613]
Discover::
Adds multi-layer time axis for opt-out only {kibana-pull}115853[#115853]
Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
Adds consistent `_meta` property to all Fleet ES assets {kibana-pull}119380[#119380]
Kibana Home & Add Data::
Moves overview page and link to the accordion solution title {kibana-pull}114018[#114018]
Lens & Visualizations::
* Handle removal of deprecated date histogram interval in *Vega* {kibana-pull}109090[#109090]
* Adds value labels to Heatmap in *Lens* {kibana-pull}106406[#106406]
Machine Learning::
* Adds support for `force` stop deployment {kibana-pull}118563[#118563]
* Refactors data view loading to remove unnecessary searches {kibana-pull}116455[#116455]
Observability::
* Service Maps: Adds sparklines to the detail popover {kibana-pull}120021[#120021]
* Offer users upgrade to multi-metric job {kibana-pull}119980[#119980]
* Display relevant anomalies from multi-metric job {kibana-pull}119709[#119709]
* Adds service icon for the originating service in traces table {kibana-pull}119421[#119421]
* Auto attachment for java agent beta in APM integration settings {kibana-pull}119131[#119131]
* Errors: Enhancements to the Errors list page (part II) {kibana-pull}118878[#118878]
* Store Alerts View table state in localStorage {kibana-pull}118207[#118207]
* Handle other values popup when correlated value is not in top 10 {kibana-pull}118069[#118069]
* Adds links to navigate from alerts table to rule {kibana-pull}118035[#118035]
* Reinstates ML multi-metric job {kibana-pull}117836[#117836]
* Re-enables metric-based UI {kibana-pull}117021[#117021]
* Make Alerts page use shared Kibana time range {kibana-pull}115192[#115192]
* Adds enabled toggle {kibana-pull}119994[#119994]
* Adds missing tooltip to the report metric badge in *Exploratory View* {kibana-pull}119940[#119940]
* Adds step duration in step list {kibana-pull}116266[#116266]
Platform::
Moves developer architecture docs to user docs {kibana-pull}119125[#119125]
Reporting::
* Decouples screenshotting plugin from the reporting {kibana-pull}120110[#120110]
* Updates the design of the *Reports* management UI, including the addition of a link to Kibana app where the report was generated {kibana-pull}111412[#111412]
Security::
Adds ability to clone role mappings {kibana-pull}118434[#118434]
Adds user logout audit events {kibana-pull}121455[#121455]

### Bug fixes

Canvas::
* Fixes Error overflow {kibana-pull}122158[#122158]
* Fixes expression input {kibana-pull}121490[#121490]
* Hides edit menu when in view-only mode {kibana-pull}118779[#118779]
Dashboard::
* Allow text wrapping for panel titles and dashboard descriptions for PDF generation {kibana-pull}121360[#121360]
* Page now resets to zero when rows per page is changed on *Add from Library* window {kibana-pull}118627[#118627]
* Fixes full screen error when pressing back arrow in browser {kibana-pull}118113[#118113]
Elastic Security::
For the Elastic Security 8.0.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Adds `installed_kibana_space_id` to `epm-packages` saved objects {kibana-pull}120517[#120517]
* Handle Saved Object ID changes {kibana-pull}119527[#119527]
* Fixes upgradeable agents filter {kibana-pull}119338[#119338]
Lens & Visualizations::
* Enables normal mode for percentage charts in *Lens* {kibana-pull}120197[#120197]
* Fixes existing fields query for epoch_millis dates in *Lens* {kibana-pull}119508[#119508]
* Include frozen indices in *Lens* {kibana-pull}118555[#118555]
* Fixes focus on legend action popovers in *Lens* {kibana-pull}115066[#115066]
Machine Learning::
* Fixes data view search based on title {kibana-pull}120737[#120737]
* Data frame analytics wizard: Only allow data view creation if job will be started immediately {kibana-pull}120042[#120042]
* Fixes anomaly detection module manifest queries to ignore frozen and cold data tiers {kibana-pull}119635[#119635]
* Catches syntax error in job wizard editor {kibana-pull}119457[#119457]
* Fixes error handling for missing data view in data frame analytics wizard {kibana-pull}119455[#119455]
* Ensures auto refresh interval is used in Data Frame Analytics list {kibana-pull}117959[#117959]
* Ignores frozen indices in data recognizer {kibana-pull}117208[#117208]
Management::
* Fixes data grid column actions button when histogram charts are visible {kibana-pull}120202[#120202]
* Disables delete data view for data frame analytics and transforms wizards {kibana-pull}119732[#119732]
* Check Kibana capabilities for all saving, editing, and deleting {kibana-pull}118480[#118480]
* Adds autocomplete for search_after and pit in search query {kibana-pull}117864[#117864]
* Autocomplete for t_test aggregation {kibana-pull}117782[#117782]
* Disables create data view for data frame analytics and transforms wizards {kibana-pull}117690[#117690]
Maps::
* Fixes an issue where drawings do not show when there is a global filter {kibana-pull}121239[#121239]
* Use minimum symbol size if meta is not loaded {kibana-pull}119119[#119119]
* Do not fail migration when JSON.parse fails {kibana-pull}117342[#117342]
* Do not allow label overlap {kibana-pull}116190[#116190]
Monitoring::
Correct linear regression formula {kibana-pull}120222[#120222]
Observability::
* Renames alerting types in Infra {kibana-pull}121061[#121061]
* Renames occurrences of `alert_type` to `rule_type` in Infra {kibana-pull}120455[#120455]
* Fixes failing alerts table pagination functional tests {kibana-pull}119985[#119985]
* Switch to _source for updating documents instead of fields API {kibana-pull}118245[#118245]
* Fixes an issue where search terms with certain characters caused the APM UI to crash {kibana-pull}118063[#118063]
* Ignore unavailable indices for ML jobs {kibana-pull}117632[#117632]
* Disables the actions button when users have inadequate privileges {kibana-pull}117488[#117488]
* Replaces manual rate calculation with `rate` agg {kibana-pull}115651[#115651]
* Adds migration to fix incorrect action group spelling {kibana-pull}119626[#119626]
* Fixes bug with manage views button {kibana-pull}118547[#118547]
* Disables No Data checkboxes for doc count alerts {kibana-pull}117194[#117194]
* Prevent event propagation on step_duration {kibana-pull}122039[#122039]
* Disables the button to create alerts in Uptime when users do not have permissions to do so {kibana-pull}120379[#120379]
* Fixes a bug that prevented users from saving Uptime configurations when the `inspect` option was turned on {kibana-pull}119142[#119142]
* Adds a callout to informs users that they do not have permissions to create ML jobs for Uptime monitors {kibana-pull}117684[#117684]
Platform::
Fixes font glitches in code editor {kibana-pull}121392[#121392]
Reporting::
Fixes an issue where PDF and PNG reports break on Windows operating systems when the Kibana server hostname is `0.0.0.0` {kibana-pull}117022[#117022]
