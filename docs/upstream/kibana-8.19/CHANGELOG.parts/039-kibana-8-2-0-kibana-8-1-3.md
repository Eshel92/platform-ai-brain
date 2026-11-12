<!-- Part 39 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.2.0

Review the following information about the Kibana 8.2.0 release.

### Known issue

Lens & visualizations::
A change in the Markdown library that Kibana uses to create *TSVB* *Markdown* visualizations and *Text* dashboard panels renders some tables differently. For more information, check out [#767](https://github.com/markdown-it/markdown-it/pull/767).

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.2.0.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Features

Kibana 8.2.0 adds the following new and notable features.

Alerting::
* Keep the number_of_scheduled_actions in event log {kibana-pull}128438[#128438]
* Remove defaultRuleTaskTimeout and set ruleType specific timeout from kibana.yml {kibana-pull}128294[#128294]
* Limit the executable actions per rule execution {kibana-pull}128079[#128079] and {kibana-pull}126902[#126902]

Cases::
* Adds Cases to the Stack Management page as a technical preview feature {kibana-pull}125224[#125224]

Dashboard::
* Adds time slider control {kibana-pull}128305[#128305]
* Adds Control group search settings {kibana-pull}128090[#128090]
* Adds hierarchical chaining setting to Controls {kibana-pull}126649[#126649]
* Adds options list API and validation system {kibana-pull}123889[#123889]

Discover::
* Enables document explorer by default {kibana-pull}125485[#125485]
* Adds `Copy to clipboard` ability for column name of Document Explorer {kibana-pull}123892[#123892]

Elastic Security::
For the Elastic Security 8.2.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Lens & Visualizations::
* Adds manual annotations in *Lens* {kibana-pull}126456[#126456]
* Adds multi-field group by in *TSVB* {kibana-pull}126015[#126015]
* Adds ability to navigate to *Lens* with your current *TSVB* configuration {kibana-pull}114794[#114794]

Machine Learning::
* Add link to maps in charts section of Anomaly Explorer {kibana-pull}128697[#128697]
* Testing trained models in UI {kibana-pull}128359[#128359]
* Space aware trained models {kibana-pull}123487[#123487]

Management::
* Adds support for auto-complete for data streams {kibana-pull}126235[#126235]
* Adds ability to filter Data View UI for runtime fields {kibana-pull}124114[#124114]
* Adds ability to share data views across spaces via data view management {kibana-pull}123991[#123991]

Observability::
* Adds button which allows users to signup for the Synthetics service public beta {kibana-pull}128798[#128798]
* Adds "View in App URL" {context.viewInAppUrl} variable to the rule templating language {kibana-pull}128281[#128281]
* Adds "View in App URL" {context.viewInAppUrl} variable to the rule templating language {kibana-pull}128243[#128243]
* Adds "View in App URL" {context.viewInAppUrl} variable to the rule templating language {kibana-pull}127890[#127890]
* Adds view in app url as an action variable in the alert message for uptime app {kibana-pull}127478[#127478]

For more information about the features introduced in 8.2.0, refer to What's new in 8.2.

### Enhancements and bug fixes

For detailed information about the 8.2.0 release, review the enhancements and bug fixes.

### Enhancements

Alerting::
* Adds error logs in rule details page {kibana-pull}128925[#128925]
* Simplify error banner on rules {kibana-pull}128705[#128705]
* Adds Previous Snooze button {kibana-pull}128539[#128539]
* Adds Snooze UI and Unsnooze API {kibana-pull}128214[#128214]
* Adds aggs to know how many rules are snoozed {kibana-pull}128212[#128212]
* Adds a connector for xMatters {kibana-pull}122357[#122357]

Dashboard::
* Adds option to open dashboard drilldowns in new tab or window {kibana-pull}125773[#125773]
* Adds range slider Control {kibana-pull}125584[#125584]

Discover::
Adds ability to edit histogram as vis {kibana-pull}125705[#125705]

Elastic Security::
For the Elastic Security 8.2.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Enterprise Search::
For the Elastic Enterprise Search 8.2.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].

Fleet::
* Merge settings & mappings component template in @package {kibana-pull}128498[#128498]
* Redesign agent flyout {kibana-pull}128381[#128381]
* Adds a link from agent details page to agent dashboard {kibana-pull}127882[#127882]
* Update add agent instructions in fleet managed mode for Kubernetes {kibana-pull}127703[#127703]
* Added time_series_metric mapping for metric_type package field {kibana-pull}126322[#126322]
* Added support for dimension field {kibana-pull}126257[#126257]
* Refactor auto upgrade package policies logic {kibana-pull}125909[#125909]
* Move mappings from index template to component template {kibana-pull}124013[#124013]

Lens & Visualizations::
* Adds normalize_by_unit function and option in *Lens* {kibana-pull}128303[#128303]
* Adds suffix formatter in *Lens* {kibana-pull}128246[#128246]
* Adds Xy gap settings in *Lens* {kibana-pull}127749[#127749]
* Implements null instead of zero switch in *Lens* {kibana-pull}127731[#127731]
* Adds ability to include empty rows setting for date histogram in *Lens* {kibana-pull}127453[#127453]
* Adds support for multi rows headers for the table visualization in *Lens* {kibana-pull}127447[#127447]
* Adds ability to open *Lens* visualizations in *Discover* from dashboards {kibana-pull}127355[#127355]
* Auto-set exists filtering for last value in *Lens* {kibana-pull}127251[#127251]
* Adds ability to include number of values in default terms field label in *lens* {kibana-pull}127222[#127222]
* Adds ability to drop partial buckets option in *Lens* {kibana-pull}127153[#127153]
* Addds ability to allow top metric for last value in *Lens* {kibana-pull}127151[#127151]
* Improves Datatable content height with custom row height in *Lens* {kibana-pull}127134[#127134]
* Adds ability to set legend pixel width in *Lens* {kibana-pull}126018[#126018]
* Adds underlying data editor navigation in *Lens* {kibana-pull}125983[#125983]
* Adds top metrics aggregation to AggConfigs, Expressions, and Visualize {kibana-pull}125936[#125936]
* Adds the ability to detach from global time range in *Lens* {kibana-pull}125563[#125563]
* Adds last value, min and max on dates, allow last value on ip_range, number_range, and date_range in *Lens* {kibana-pull}125389[#125389]
* Adds version-aware sorting to data table in *Lens* {kibana-pull}125361[#125361]
* Cancel discarded searches in *Timelion* {kibana-pull}125255[#125255]
* Cancel discarded searches in *TSVB* {kibana-pull}125197[#125197]
* Adds the ability to allow users to disable auto-apply in *Lens* {kibana-pull}125158[#125158]
* Adds Filter custom label for kibanaAddFilter in *Vega* {kibana-pull}124498[#124498]
* Adds metric Viz config options, title position, and sizing in *Lens* {kibana-pull}124124[#124124]
* Adds the ability to make graph edges easier to click {kibana-pull}124053[#124053]
* Adds "Show empty rows" options to intervals function in *Lens* {kibana-pull}118855[#118855]

Machine Learning::
* Combines annotations into one block if multiple annotations overlap {kibana-pull}128782[#128782]
* Adds `throughput_last_minute` to the deployment stats {kibana-pull}128611[#128611]
* Adds new API endpoint to improve anomaly chart performance {kibana-pull}128165[#128165]
* Utilize ML memory stats endpoint for the memory overview chart {kibana-pull}127751[#127751]
* Deleting trained model space checks {kibana-pull}127438[#127438]
* Show at least one correlation value and consolidate correlations columns {kibana-pull}126683[#126683]
* Include fields not in docs in Data Visualizer field name control {kibana-pull}126519[#126519]
* Anomaly Explorer performance enhancements {kibana-pull}126274[#126274]
* Fixes Index data visualizer reaching Elasticsearch rate request limits {kibana-pull}124898[#124898]
* Adds cache for data recognizer module configs to reduce number of privilege checks {kibana-pull}126338[#126338]

Management::
* Extend Transform Health alerting rule with error messages check {kibana-pull}128731[#128731]
* Enable opening queries from any UI {kibana-pull}127461[#127461]
* No Data Views Component {kibana-pull}125403[#125403]

Maps::
* Remove usage of max file size advanced setting 1GB limit in geo file upload {kibana-pull}127639[#127639]
* Adds support for geohex_grid aggregation {kibana-pull}127170[#127170]
* Lens choropleth chart {kibana-pull}126819[#126819]
* Register GeoJson upload with integrations page {kibana-pull}126350[#126350]
* Support custom icons in maps {kibana-pull}113144[#113144]

Observability::
* Guided setup progress {kibana-pull}128382[#128382]
* Enable check for public beta {kibana-pull}128240[#128240]
* Guided setup button on the overview page {kibana-pull}128172[#128172]
* Show warning when users exceed a Synthetics Node throttling limits {kibana-pull}127961[#127961]
* Adds logging to Inventory Threshold Rule {kibana-pull}127838[#127838]
* O11y rules page {kibana-pull}127406[#127406]
* Enrich documents generated by the synthetics service with `port` information {kibana-pull}127180[#127180]
* Make UI indices space aware (support for spaces) {kibana-pull}126176[#126176]
* Setting for default env for service inventory {kibana-pull}126151[#126151]
* Alerts in overview page {kibana-pull}125337[#125337]
* Adds log rate to Exploratory View {kibana-pull}125109[#125109]
* Support switching between log source modes {kibana-pull}124929[#124929]
* Overview style updates {kibana-pull}124702[#124702]
* Adds full screen/copy button ability in browser inline script editing {kibana-pull}124500[#124500]
* Update position of legend and it's controls {kibana-pull}115854[#115854]

Platform::
Allow customizing Elasticsearch client maxSockets {kibana-pull}126937[#126937]

### Bug fixes

Alerting::
* Fixes bug when providing a single value to the `fields` query parameter of the Cases find API {kibana-pull}128143[#128143]
* Fixes the count of alerts in the cases table. Only unique alerts are being counted {kibana-pull}127721[#127721]
* Do not show the lens action if Visualize feature is not enabled {kibana-pull}127613[#127613]

Dashboard::
* Fixes control removal {kibana-pull}128699[#128699]
* Select televant data view ID {kibana-pull}128440[#128440]
* Close controls flyouts on unmount, save, and view mode change {kibana-pull}128198[#128198]

Discover::
* Account for hidden time column in default sort {kibana-pull}129659[#129659]
* Make field icons consistent across field list and doc tables {kibana-pull}129621[#129621]
* Fixes `Filter for field present` in expanded document view of Document Explorer {kibana-pull}129588[#129588]
* Cancel long running request after navigating out from Discover {kibana-pull}129444[#129444]
* Fixes height of JSON tab in Document flyout when using Document explorer in Safari {kibana-pull}129348[#129348]
* Fixes stuck action menu in expanded document sidebar {kibana-pull}127588[#127588]

Elastic Security::
For the Elastic Security 8.2.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Lens & Visualizations::
* Fixes multi index pattern load bug in *TSVB* {kibana-pull}130428[#130428]
* Handle empty values for range formatters {kibana-pull}129572[#129572]
* Apply pinned filters to *Lens* {kibana-pull}129503[#129503]
* Imported vislib pie triggers unsaved viz warning when embedded on a dashboard in *Visualize* {kibana-pull}129336[#129336]
* Fixes auto session-renewal on non-timebased data views in *Lens* {kibana-pull}129313[#129313]
* Fixes steps behavior to happen at the change point in *TSVB* {kibana-pull}128741[#128741]
* Improve check for 0 opacity in *TSVB* {kibana-pull}128630[#128630]
* Fixes firefox scrollbars in *Vega* {kibana-pull}128515[#128515]
* Log data tables properly in *Lens* {kibana-pull}128297[#128297]
* Fixes annotation bounds bug in *TSVB* {kibana-pull}128242[#128242]
* Make sure x axis values are always strings in *Lens* {kibana-pull}128160[#128160]
* Use default number formatter as fallback if nothing else is specified in *Timelion* {kibana-pull}128155[#128155]
* Enable Save&Return button for canvas when dashboard permissions are off in *Visualize* {kibana-pull}128136[#128136]
* Fixes permission problem for "Save and return" button in *Lens* {kibana-pull}127963[#127963]
* Restore operation auto switch based on field type in *Lens* {kibana-pull}127861[#127861]
* Fixes mosaic color syncing in *Lens* {kibana-pull}127707[#127707]
* Make edge selection work {kibana-pull}127456[#127456]
* Remove opacity for fitting line series {kibana-pull}127176[#127176]
* Handle line/area fitting function when the editor has started with bar configuration in *Visualize* {kibana-pull}126891[#126891]
* Preserve custom label when changing with multi-terms settings in *Lens* {kibana-pull}126773[#126773]
* Fixes multi terms fields validation in *Lens* {kibana-pull}126618[#126618]
* Make Embeddable resilient when toggling actions in *Lens* {kibana-pull}126558[#126558]
* Make graph app resilient to no fields or missing data views {kibana-pull}126441[#126441]
* Fixes Formula to Quick functions does not preserve custom formatting in *Lens* {kibana-pull}124840[#124840]
* Inspector displays only visible content {kibana-pull}124677[#124677]
* Coloring tooltips in Heatmap are not properly positioned in *Visualize* {kibana-pull}124507[#124507]
* Adds rison helper and URL encoding for drilldown urls in *TSVB* {kibana-pull}124185[#124185]

Machine Learning::
* Fixes alignment of Anomaly Explorer swim lane annotations label on Firefox {kibana-pull}130274[#130274]
* Fixes Single Metric Viewer chart failing to load if no points during calendar event {kibana-pull}130000[#130000]
* Fixes Single Metric Viewer for jobs that haven't been run {kibana-pull}129063[#129063]
* Fix outlier detection results exploration color legend display {kibana-pull}129058[#129058]
* Fixes new anomaly detection job from saved search with no query filter {kibana-pull}129022[#129022]
* Fixes data frame analytics map saved object sync warning {kibana-pull}128876[#128876]
* Adds error toast to Data visualizer when using unpopulated time field {kibana-pull}127196[#127196]

Management::
* Transforms: Fix to not pass on default values in configurations {kibana-pull}129091[#129091]
* Encode + sign in ISO8601 time range in query {kibana-pull}126660[#126660]

Maps::
* Fixes lens region map visualization throws a silent error {kibana-pull}129608[#129608]
* Fixes double click issue when deleting a shape {kibana-pull}124661[#124661]

Monitoring::
* Exclude Malwarescore + Ransomware EP alerts from DRule telemetry {kibana-pull}130233[#130233]
* Rename "APM & Fleet Server" to "Integrations Server" {kibana-pull}128574[#128574]
* Fixes sorting by node status on nodes listing page {kibana-pull}128323[#128323]

Observability::
* Service environment should be selected when you edit the agent configuration {kibana-pull}129929[#129929]
* Adds migration to include synthetics and heartbeat indices on 8.2.0 {kibana-pull}129510[#129510]
* Rules summary on the Alerts view is not showing the count of rules {kibana-pull}129052[#129052]
* Fixes shadow for overview panels {kibana-pull}128878[#128878]
* Ensure rum_allow_origins setting only saves valid YAML strings {kibana-pull}128704[#128704]
* Standardize NOW as startedAt from executor options {kibana-pull}128020[#128020]
* Fixes synthetics recorder file upload {kibana-pull}127614[#127614]
* Service Maps popover detail metrics are aggregates over all transaction types {kibana-pull}125580[#125580]

Platform::
* Fixes an issue where duplicate data appears in the inspector datatable in *Lens* for heatmap visualizations, and stale data persists in the inspector datatable when you remove layers {kibana-pull}126786[#126786]
* Fixes an issue that caused Kibana to become unresponsive while generating a PDF report {kibana-pull}124787[#124787]
* Fixes an issue where an unfriendly notification title displays after you create a report {kibana-pull}123607[#123607]

Security::
* Fixes styles for "You do not have permission" screen {kibana-pull}129715[#129715]
* Change session expiration to override on app leave behavior {kibana-pull}129384[#129384]


## Kibana 8.1.3

Review the following information about the Kibana 8.1.3 release.

### Security update

The 8.1.3 release contains a fix to a potential security vulnerability. For more information, check [Security Announcements](https://discuss.elastic.co/t/kibana-7-17-3-and-8-1-3-security-update/302826).

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.1.3.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fix

Discover::
* Fixes toggle table column for classic table {kibana-pull}128603[#128603]
