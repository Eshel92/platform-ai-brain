<!-- Part 23 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.11.0

For information about the Kibana 8.11.0 release, review the following information.

### Known issues

**Errors appear when loading Observability Infrastructure inventory views after upgrading to version 8.10.0 or higher.**
*Details* +
After upgrading to version 8.10.0 or higher, you may encounter errors when loading inventory views.

For more information, refer to [#187254](https://github.com/elastic/kibana/issues/187254).

*Workaround* +
You can mitigate the issue by completing the following steps:

. Search the `.kibana_*` index for `type: inventory_view`.

. Copy the `_id` field, which will be formatted as `inventory-view:<id>`. For example, `inventory-view:3d3d06b0-f873-4373-8446-f6a8341cd8b1`. Omit the `inventory-view:` portion and copy only the string of `_id` characters.

. The offending documents are those with fields `inventory-view.legend.steps` > 18. Delete these documents by running the following in *Console*:

```js
DELETE kbn:/api/infra/inventory-views/<id>
```
**Gatekeeper error on macOS**
*Details* +
Due to a version upgrade of the server binary used by Kibana and an upstream notarization issue, a Gatekeeper error may display for "node"
when starting Kibana in macOS environments.

*Workaround* +
More information can be found at install-darwin64.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.11.0, review the breaking changes, then mitigate the impact to your application.

**Improve config output validation for default output.**
*Details* +
Improve config output validation to not allow to defining multiple default outputs in Kibana configuration. For more information, refer to ({kibana-pull}167085[#167085]).

**Convert filterQuery to KQL.**
*Details* +
Converts `filterQuery` to a KQL query string. For more information, refer to ({kibana-pull}161806[#161806]).

### Deprecations

The following functionality is deprecated in 8.11.0, and will be removed in 9.0.0.
Deprecated functionality does not have an immediate impact on your application, but we strongly recommend
you make the necessary updates after you upgrade to 8.11.0.

**Updates to move from doc_root.vulnerability.package -> doc_root.package (ECS).**
*Details* +
This updates all instances of vulnerability.package to the ECS standard package fieldset. For more information, refer to ({kibana-pull}164651[#164651]).

### Features

Kibana 8.11.0 adds the following new and notable features.

Alerting::
* Adds support for the new ES|QL language for Elasticsearch query rules ({kibana-pull}165973[#165973]).
* Elasticsearch query rule can select multiple group-by terms ({kibana-pull}166146[#166146]).
* Adds a Log tab to the Observability Rules page ({kibana-pull}165115[#165115]).
APM::
* Adds bulk action to untrack selected alerts ({kibana-pull}167579[#167579]).
* Introduce custom dashboards tab in service overview ({kibana-pull}166789[#166789]).
* Adds service profiling Top 10 Functions ({kibana-pull}166226[#166226]).
* Adds service profiling flamegraph ({kibana-pull}165360[#165360]).
Cases::
* Adds custom fields in Cases ({kibana-pull}167016[#167016]).
Dashboard::
* Copy panel refactor ({kibana-pull}166991[#166991]).
* Make links panel available under technical preview ({kibana-pull}166896[#166896]).
* Store view mode in local storage ({kibana-pull}166523[#166523]).
* Adds a read only state for Managed Dashboards ({kibana-pull}166204[#166204]).
Discover::
* Adds resize support to the Discover field list sidebar ({kibana-pull}167066[#167066]).
Elastic Security::
For the Elastic Security 8.11.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search service::
For the Elastic Enterprise Search service 8.11.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Release notes_].
Fleet::
* Set env variable `ELASTIC_NETINFO:false` in Kibana ({kibana-pull}166156[#166156]).
* Added restart upgrade action ({kibana-pull}166154[#166154]).
* Adds ability to set a proxy for agent binary source ({kibana-pull}164168[#164168]).
* Adds ability to set a proxy for agent download source ({kibana-pull}164078[#164078]).
Lens & Visualizations::
* Adds color mapping for categorical dimensions in *Lens* available under technical preview ({kibana-pull}162389[#162389]).
* Inline editing of **Lens** panels on a dashboard or canvas ({kibana-pull}166169[#166169]).
* Individual annotation editing from library ({kibana-pull}163346[#163346]).
Logs::
* Convert log explorer profile into standalone app available under technical preview ({kibana-pull}164493[#164493]).
Machine Learning::
* Adds support for the ELSER v2 download in the Trained Models UI ({kibana-pull}167407[#167407]).
* Adds data drift detection workflow from Trained Models to Data comparison view ({kibana-pull}162853[#162853]).
Management::
* Supports for viewing and editing data retention per data stream in Index Management is available under technical preview ({kibana-pull}167006[#167006]).
* Supports for viewing and editing data retention per data stream in Index Management is available under technical preview ({kibana-pull}167006[#167006]).
* Index details can now be viewed on a new index details page in Index Management ({kibana-pull}165705[#165705]).
* Supports for managing, executing, and deleting enrich policies in Index Management ({kibana-pull}164080[#164080]).
Platform::
* ES|QL, a new query language, is available under technical preview in Discover and Dashboards ({kibana-pull}146971[#146971]).
Querying & Filtering::
* Saved queries can now be shared between multiple spaces ({kibana-pull}163436[#163436]).
Uptime::
* Adds a document viewer to the summary pings table ({kibana-pull}163926[#163926]).

For more information about the features introduced in 8.11.0, refer to What's new in 8.11.

### Enhancements and bug fixes

For detailed information about the 8.11.0 release, review the enhancements and bug fixes.

### Enhancements

APM::
* Changed mobile badge from 'technical preview' to 'beta' ({kibana-pull}167543[#167543]).
* New Profiling ES Flamegraph API ({kibana-pull}167477[#167477]).
* Adds Universal Profiling to O11y overview and Setup guide ({kibana-pull}165092[#165092]).
* Mark disabled alerts as Untracked in both Stack Management and o11y ({kibana-pull}164788[#164788]).
* Adds time range to event metadata API ({kibana-pull}167132[#167132]).
* New settings to control CO2 calculation ({kibana-pull}166637[#166637]).
* Adds permissions for "input-only" package ({kibana-pull}166234[#166234]).
* Adds selecting the consumer based on the authorized consumers when a user is creating an ES Query threshold rule ({kibana-pull}166032[#166032]).
* Migrate Ace based `EuiCodeEditor` to Monaco based code editor ({kibana-pull}165951[#165951]).
* Mobile UI crash widget added ({kibana-pull}163527[#163527]).
Cases::
* Show a warning message to inform user that navigating after the 10Kth case is not possible ({kibana-pull}164323[#164323]).
Dashboard::
* Focus on a single panel while disabling all other panels ({kibana-pull}165417[#165417]).
* Adds filter details to panel settings ({kibana-pull}162913[#162913]).
* Adds support for date fields in the options list controls ({kibana-pull}164362[#164362]).
Discover::
* Redesign for the grid, panels and sidebar ({kibana-pull}165866[#165866]).
* Set data table row height to auto-fit by default ({kibana-pull}164218[#164218]).
* Allow fetching more documents on Discover page ({kibana-pull}163784[#163784]).
Elastic Security::
For the Elastic Security 8.11.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Search::
* Self-managed connector clients now show advanced configuration options in the UI ({kibana-pull}167770[#167770]).
Fleet::
* Adds sidebar navigation showing headings extracted from the readme ({kibana-pull}167216[#167216]).
Inspector::
* Clusters tab added under Inspector ({kibana-pull}166025[#166025]).
* Open incomplete response warning in Inspector ({kibana-pull}167205[#167205]).
Lens & Visualizations::
* Other bucket defaults to false for top values greater than equal 1000 in *Lens* ({kibana-pull}167141[#167141]).
* Adds support for decimals in percentiles in *Lens* ({kibana-pull}165703[#165703]).
Machine Learning::
* Updates ELSER version for Elastic Assistant ({kibana-pull}167522[#167522]).
* Retains `created_by` setting when exporting anomaly detection jobs ({kibana-pull}167319[#167319]).
* Improves the wording of awaiting ML nodes messages ({kibana-pull}167306[#167306]).
* Adds `created_by` job property for the advanced wizard ({kibana-pull}167021[#167021]).
* Trained model testing: only show indices with supported fields ({kibana-pull}166490[#166490]).
* Alerts as data integration for Anomaly Detection rule type ({kibana-pull}166349[#166349]).
* Data Frame Analytics Trained models: adds the ability to reindex after pipeline creation ({kibana-pull}166312[#166312]).
* Adds Create a data view button to index or saved search selector in ML pages and Transforms management ({kibana-pull}166668[#166668]).
* Improvements to UX of adding ML embeddables to a dashboard ({kibana-pull}165714[#165714]).
* AIOps: Supports text fields in log rate analysis ({kibana-pull}165124[#165124]).
* Data Frame Analytics creation wizard: adds ability to add custom URLs to jobs ({kibana-pull}164520[#164520]).
Management::
* Adds Create a data view button to index or saved search selector in ML pages and Transforms management ({kibana-pull}166668[#166668]).
* Improve loading behavior of Transforms list if stats request is slow or is not available ({kibana-pull}166320[#166320]).
* Adds support for PATCH requests in Console ({kibana-pull}165634[#165634]).
* Improves autocomplete to suggest knn in search query ({kibana-pull}165531[#165531]).
* Improves display for long descriptions in Transforms ({kibana-pull}165149[#165149]).
* Improve transform list reloading behavior ({kibana-pull}164296[#164296]).
Maps::
* Allow by value styling for EMS boundary fields ({kibana-pull}166306[#166306]).
* Adds support for `geo_shape` fields as the entity geospatial field when creating tracking containment alerts ({kibana-pull}164100[#164100]).
Observability::
* ES|QL query generation ({kibana-pull}166041[#166041]).
Querying & Filtering::
* New "Saved Query Management" privilege to allow saving queries across Kibana ({kibana-pull}166937[#166937]).
* Improvements to the filter builder inputs for long fields ({kibana-pull}166024[#166024]).
Uptime::
* Added ability to hide public locations ({kibana-pull}164863[#164863]).

### Bug Fixes

Alerting::
* Improve error handling in ES Index action response ({kibana-pull}164841[#164841]).
* Bring back toggle column on alert table ({kibana-pull}168158[#168158]).
* Fixes Errors rules link on observability alert page ({kibana-pull}167027[#167027]).
* Enable read-only users to access rules ({kibana-pull}167003[#167003]).
* Fixes rule snooze toast copy ({kibana-pull}166030[#166030]).
APM::
* Ensure APM data view is available across all spaces ({kibana-pull}167704[#167704]).
* Adds an environment param to the service metadata details endpoint ({kibana-pull}167173[#167173]).
* Fixes set up process ({kibana-pull}167067[#167067]).
Dashboard::
* Generate new panel IDs on Dashboard clone ({kibana-pull}166299[#166299]).
Elastic Security::
For the Elastic Security 8.11.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Search::
* Native connector external documentation links are now rendered conditionally to avoid empty links ({kibana-pull}169121[#169121]).
* Fixed an issue which caused Access Control Syncs to be scheduled when Document Level Security was disabled ({kibana-pull}168987[#168987]).
* Restored access and admin checks for App Search and Workplace Search product cards ({kibana-pull}168890[#168890]).
* The filter box in the *Browse documents* tab under *Search > Content > Indices* now escapes Lucene reserved characters instead of throwing errors ({kibana-pull}168092[#168092]).
* Fixed an issue associated with changing the indices underlying a search application. When a user modifies the indices underlying a search application in Kibana, the associated search template is now reverted to the default template ({kibana-pull}167532[#167532]).
* Fixed an issue where the Search plugin was inaccessible for unauthenticated users, eg. for Kibana in read-only demo setups ({kibana-pull}167171[#167171]).
* Fixed an issue with the welcome banner in Search ({kibana-pull}166814[#166814]).
* Self managed connector clients now show advanced configuration options in the UI ({kibana-pull}167770[#167770]).
Fleet::
* Vastly improve performance of Fleet final pipeline's date formatting logic for `event.ingested` ({kibana-pull}167318[#167318]).
Lens & Visualizations::
* Fixes heatmap color assignment on single value scenario in *Lens* ({kibana-pull}167995[#167995]).
* Fixes mosaic with 2 axis coloring in *Lens* ({kibana-pull}167035[#167035]).
* Show icons/titles instead of previews in suggestions panel in *Lens* ({kibana-pull}166808[#166808]).
* Consider root level filters buckets correctly when building other terms bucket ({kibana-pull}165656[#165656]).
* Prevent user to use decimals for custom Percentile rank function in Top values in *Lens* ({kibana-pull}165616[#165616]).
* Fixes the Graph application settings tab when in dark mode ({kibana-pull}165614[#165614]).
* Fixes Visualize List search and CRUD operations via content management ({kibana-pull}165485[#165485]).
Logs::
* Use correct ML API to query blocking tasks ({kibana-pull}167779[#167779]).
Machine Learning::
* AIOps: Fixes log pattern analysis sparklines and chart ({kibana-pull}168337[#168337]).
* AIOps: Fixes Data View runtime fields support in the Change point detection UI ({kibana-pull}168249[#168249]).
* Fixes anomaly charts when partition field contains an empty string ({kibana-pull}168102[#168102]).
* Data Frame analytics outlier detection results: ensure scatterplot matrix adheres to bounding box ({kibana-pull}167941[#167941]).
* Fixes Anomaly charts embeddable fails to load if partition value is empty string ({kibana-pull}167827[#167827]).
Management::
* Fixes `isErrorResponse` when cluster details are provided ({kibana-pull}166667[#166667]).
* Fixes autocomplete not to be prompted between triple quotes ({kibana-pull}165535[#165535]).
* Fixes autocomplete on only 1 letter typed in Console's request editor ({kibana-pull}164707[#164707]).
* Fixing duration field formatter showing 0 seconds instead of "few seconds" ({kibana-pull}164659[#164659]).
* Fixes a bug that autocomplete does not work right after a comma ({kibana-pull}164608[#164608]).
* Fixes unnecessary autocompletes on HTTP methods ({kibana-pull}163233[#163233]).
Presentation::
* Fixes ES query rule boundary field changed when editing the rule ({kibana-pull}165155[#165155]).


## Kibana 8.10.4

The 8.10.4 release includes the following bug fixes.

### Bug Fixes

Elastic Security::
For the Elastic Security 8.10.4 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes validation errors in KQL queries ({kibana-pull}168329[#168329]).


## Kibana 8.10.3

### Security updates

* **Kibana heap buffer overflow vulnerability**
On Sept 11, 2023, Google Chrome announced CVE-2023-4863, described as “Heap buffer overflow in libwebp in Google Chrome prior to 116.0.5845.187 and libwebp 1.3.2 allowed a remote attacker to perform an out of bounds memory write via a crafted HTML page”. Kibana includes a bundled version of headless Chromium that is only used for Kibana’s reporting capabilities and which is affected by this vulnerability. An exploit for Kibana has not been identified, however as a resolution, the bundled version of Chromium is updated in this release.
The issue is resolved in 8.10.3.
For more information, see our related
https://discuss.elastic.co/t/kibana-8-10-3-7-17-14-security-update/344735[security
announcement].

### Enhancements

Elastic Security::
For the Elastic Security 8.10.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

### Bug Fixes

Dashboard::
* Fixes an error the panel descriptions weren't retrieved from the right method ({kibana-pull}166825[#166825]).
Discover::
* Soften saved search content management response `sort` schema ({kibana-pull}166886[#166886]).
Elastic Security::
For the Elastic Security 8.10.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.10.3 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].
Fleet::
* Fixes incorrect index template used from the data stream name ({kibana-pull}166941[#166941]).
* Increase package install max timeout limit and add concurrency control to rollovers ({kibana-pull}166775[#166775]).
* Fixes bulk action dropdown ({kibana-pull}166475[#166475]).
Machine Learning::
* AIOps: Fixes render loop when using a saved search ({kibana-pull}166934[#166934]).
Monitoring::
* Convert node roles into array ({kibana-pull}167628[#167628]).
Observability::
* Fixes a set up process error in Universal Profiling ({kibana-pull}167068[#167068]).
Uptime::
* Fixes an error when updating browser monitor in a project ({kibana-pull}168064[#168064]).


## Kibana 8.10.2

The 8.10.2 release includes the following bug fixes.

### Bug fixes

Fleet::
* Fixes force delete package, updated used by agents check ({kibana-pull}166623[#166623]).
Management::
* Fixes showing `Received partial message` instead of results when there are some remote shard errors in a cross-cluster search ({kibana-pull}166544[#166544]).


## Kibana 8.10.1

The 8.10.1 release includes the following bug fixes.

### Bug fixes

Dashboard::
* Fixes content editor flyout footer ({kibana-pull}165907[#165907]).
Elastic Security::
For the Elastic Security 8.10.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Show snapshot version in agent upgrade modal and allow custom values ({kibana-pull}165978[#165978]).
Observability::
* Fix(slo): Use comma-separarted list of source index for transform ({kibana-pull}166294[#166294]).
Presentation::
* Fixes air-gapped enviroment hitting `400` error when loading fonts for layer ({kibana-pull}165986[#165986]).
