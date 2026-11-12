<!-- Part 21 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.12.0

For information about the Kibana 8.12.0 release, review the following information.

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
**Index templates UI incorrectly sets the `allow_auto_create` field to `false` by default.**
*Details* +
If you are creating or editing an index template using the Index Templates form under the Index Management page, the `allow_auto_create` field is incorrectly set to `false` by default (the default value should be `undefined`). For more information, refer to ({kibana-issue}177938[#177938]).

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.12.0, review the breaking changes, then mitigate the impact to your application.

**New SLO architecture**
*Details* +
We introduce a breaking change in the SLO features that will break any SLOs created before 8.12. These SLOs have to be manually reset through an API until we provide a UI for it. The data aggregated over time (rollup) is still available in the sli v2 index, but won't be used for summary calculation when reset.

The previous summary transforms summarizing every SLOs won't be used anymore and can be stopped and deleted:

* slo-summary-occurrences-7d-rolling
* slo-summary-occurrences-30d-rolling
* slo-summary-occurrences-90d-rolling
* slo-summary-occurrences-monthly-aligned
* slo-summary-occurrences-weekly-aligned
* slo-summary-timeslices-7d-rolling
* slo-summary-timeslices-30d-rolling
* slo-summary-timeslices-90d-rolling
* slo-summary-timeslices-monthly-aligned
* slo-summary-timeslices-weekly-aligned

Be aware that when installing a new SLO (or after resetting an SLO), we install two transforms (one for the rollup data and one that summarize the rollup data). Do not delete the new `slo-summary-{slo_id}-{slo_revision}` transforms. For more information, refer to ({kibana-pull}172224[#172224]).

**A new sub-feature privilege to control user access to the cases settings**
*Details* +
Roles with at least a sub-feature privilege configured will not have access to the cases setting like they had previously. All roles without a sub-feature privilege configured will not be affected. For more information, refer to ({kibana-pull}170635[#170635]).

### Features

Kibana 8.12.0 adds the following new and notable features.

APM::
* Adds viewInApp URL to the custom threshold rule type ({kibana-pull}171985[#171985]).
* Adds back the mobile crashes & errors tab ({kibana-pull}165892[#165892]).
Cases::
* The case list filter bar is now customizable, filters are removable and custom fields can be used as filters ({kibana-pull}172276[#172276]).
Elastic Security::
For the Elastic Security 8.12.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Elastic Search::
* Display E5 multilingual callout ({kibana-pull}171887[#171887]).
* Replace model selection dropdown with list ({kibana-pull}171436[#171436]).
Fleet::
* Adds support for preconfigured output secrets (Scrypt edition) ({kibana-pull}172041[#172041]).
* Adds UI components to create and edit output secrets ({kibana-pull}169429[#169429]).
* Adds support for remote ES output ({kibana-pull}169252[#169252]).
* Adds the ability to specify secrets in outputs ({kibana-pull}169221[#169221]).
* Adds an integrations configs tab to display input templates ({kibana-pull}168827[#168827]).
* Adds a Kibana task to publish Agent metrics ({kibana-pull}168435[#168435]).
Lens & Visualizations::
* Adds the ability to edit charts made by ES|QL queries in Dashboard ({kibana-pull}169911[#169911]).
Machine Learning::
* Adds E5 model configurations ({kibana-pull}172053[#172053]).
* Adds the ability to create a categorization anomaly detection job from pattern analysis ({kibana-pull}170567[#170567]).
* Adds and displays alerts data in the Anomaly Explorer ({kibana-pull}167998[#167998]).
Observability::
* Adds logic to update flyout highlights ({kibana-pull}172193[#172193]).
* Adds logic to display highlights in the flyout ({kibana-pull}170650[#170650]).
* Changes the Custom threshold title to Beta ({kibana-pull}172360[#172360]).
Security::
* Disables the connector parameters field ({kibana-pull}173610[#173610]).
* Adds a risk engine missing privileges callout ({kibana-pull}171250[#171250]).
* Asset criticality privileges API ({kibana-pull}172441[#172441]).
Uptime::
* Global params Public APIs ({kibana-pull}169669[#169669]).
* Private location public API's ({kibana-pull}169376[#169376]).
* Settings public API ({kibana-pull}163400[#163400]).

For more information about the features introduced in 8.12.0, refer to What's new in 8.12.

### Enhancements and bug fixes

For detailed information about the 8.12.0 release, review the enhancements and bug fixes.

### Enhancements

Alerting::
* Auto close ServiceNow incidents when alerts are resolved ({kibana-pull}171760[#171760]).
* PagerDuty connector now supports the links and `custom_details` attributes ({kibana-pull}171748[#171748]).
* Adds a mute and unmute action component in the alerts table row actions ({kibana-pull}170651[#170651]).
* Extends the PagerDuty connector API to support the `links` and `custom_details` attributes provided by the Event API ({kibana-pull}170459[#170459]).
* Adds toggle for alert as data fields in alert templating ({kibana-pull}170162[#170162]).
APM::
* Perform functions and LLM interactions on the server ({kibana-pull}172590[#172590]).
* Adds viewInApp URL to the custom threshold rule type ({kibana-pull}171985[#171985]).
* Adds the KQL bar to embeddables ({kibana-pull}171016[#171016]).
* Enables the average mobile app launch time panel ({kibana-pull}170773[#170773]).
* Enables the mobile most launches panel ({kibana-pull}168925[#168925]).
* Improves the Differential Top N functions grid view ({kibana-pull}170008[#170008]).
Cases::
* Users can copy to the clipboard the hashes of files uploaded to cases ({kibana-pull}172450[#172450]).
* Allow users to configure which columns are displayed in the cases list including custom fields ({kibana-pull}170950[#170950]).
* Adds a new sub-feature privilege to control user access to the cases settings ({kibana-pull}170635[#170635]).
Dashboard::
* Adds Links to the Visualization library ({kibana-pull}170810[#170810]).
Discover::
* Adds a field tokens column in the grid header ({kibana-pull}167179[#167179]).
* Enables the addition of columns from the document viewer when using ES|QL ({kibana-pull}171083[#171083]).
* Adds field search via wildcards in the document viewer ({kibana-pull}168616[#168616]).
* Improves search for field names by handling spaces like wildcards ({kibana-pull}168381[#168381]).
* Updates mapping conflict popover with types list ({kibana-pull}169855[#169855]).
* On search source error, show 'view details' action that opens request in inspector ({kibana-pull}170790[#170790]).
* Adds an Unsaved changes label when in an unsaved state of saved search ({kibana-pull}169548[#169548]).
* Allows changing the current sample size and saving it with a saved search ({kibana-pull}157269[#157269]).
* Adds new sparse vector and dense vector icons ({kibana-pull}169493[#169493]).
* Adds `sparse_vector` field support ({kibana-pull}168186[#168186]).
Elastic Security::
For the Elastic Security 8.12.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Elastic Search::
*  Trained models can now be deployed and started directly from the Machine Learning inference pipeline configuration flyout ({kibana-pull}173434[#173434]).
Fleet::
* Adds support for Elasticsearch output performance presets ({kibana-pull}172359[#172359]).
* Adds a new `keep_monitoring_alive` flag to agent policies ({kibana-pull}168865[#168865]).
* Adds support for additional types for dynamic mappings ({kibana-pull}168842[#168842]).
* Implements Elastic Agent upgrade states UI ({kibana-pull}167539[#167539]).
* Use default component templates from Elasticsearch ({kibana-pull}163731[#163731]).
Lens & Visualizations::
* Moves the tagcloud visualization in *Lens* out of experimental status ({kibana-pull}168824[#168824]).
* Allows coloring an entire metric panel when applying a maximum value to the metric visualization in **Lens** ({kibana-pull}172531[#172531]).
* Adds truncation for data view pickers and field lists with many characters ({kibana-pull}172296[#172296]).
* Allows searching in the ES|QL inline documentation description ({kibana-pull}171916[#171916]).
* Allows setting non-numeric metrics for metric visualizations in *Lens* ({kibana-pull}169258[#169258]).
Machine Learning::
* Removes the beta badge from ML alerting rules ({kibana-pull}173545[#173545]).
* Removes the technical preview badge from AIOps log rate analysis ({kibana-pull}172722[#172722]).
* Adds anomaly description as an alert message for the anomaly detection rule type ({kibana-pull}172473[#172473]).
* Adds a sampled percentage of documents, and cardinality, for text fields for the Data Visualizer Field statistics tab and addresses an issue with a missing bucket in the document count chart ({kibana-pull}172378[#172378]).
* Adds option to display an overlay chart on the data drift expanded row ({kibana-pull}172239[#172239]).
* AIOps: Shows top N results when no documents are in baseline or deviation in log rate analysis({kibana-pull}171924[#171924]).
* AIOps: Adds support to restore baseline and deviation from URL state on page refresh for log rate analysis ({kibana-pull}171398[#171398]).
* Validates and limits threading parameters for starting a model deployment ({kibana-pull}171921[#171921]).
* Trained models: Adds a missing job node to models map view when original job has been deleted ({kibana-pull}171590[#171590]).
* Trained models list: Disables the View training data action if data frame analytics job no longer exists ({kibana-pull}171061[#171061]).
* Adds a trained model flyout with available models to download for in the Trained Models UI ({kibana-pull}171024[#171024]).
* Allows temporary data views in the anomaly detection jobs wizards ({kibana-pull}170112[#170112]).
* Assigns downloaded ELSER models to the `*` space ({kibana-pull}169939[#169939]).
* Adds pattern analysis to the anomaly action menu ({kibana-pull}169400[#169400]).
* Adds test pipeline action for data frame analysis trained models in models list ({kibana-pull}168400[#168400]).
Management::
* Adds a search bar to the Clusters and shards tab ({kibana-pull}171806[#171806]).
* Aligns data view and destination index creation workflows in Transforms and Data Frame Analytics wizards ({kibana-pull}171202[#171202]).
* The index lifecycle summary on the Index lifecycle page is now displayed in a separate tab ({kibana-pull}170726[#170726]).
* Adds the ability to view mappings conflicts in data views on the data view management page ({kibana-pull}169381[#169381]).
* Implements index overview cards ({kibana-pull}168153[#168153]).
Observability::
* Reset UI for updating outdated SLOs ({kibana-pull}172883[#172883]).
* Adds timeslice metric indicator for SLOs ({kibana-pull}168539[#168539]).
* Adds logic to update flyout highlights ({kibana-pull}172193[#172193]).
* Sets budget consumed mode as the default mode for burn rate rule configuration ({kibana-pull}171433[#171433]).
* Allow users to define burn rate windows using budget consumed ({kibana-pull}170996[#170996]).
* Makes rules created in Discover visible in Observability ({kibana-pull}171364[#171364]).
* Adds support for document count to custom metric indicator ({kibana-pull}170913[#170913]).
* Improves displaying inline frames ({kibana-pull}169212[#169212]).
* Adds summary insight to the Differential flamegraph ({kibana-pull}168978[#168978]).
* Include `search-*` when recalling documents ({kibana-pull}173710[#173710]).
Platform::
* Limits `elasticsearch.maxSockets` to 800 by default ({kibana-pull}151911[#151911]).
Presentation::
* Adds popover message in the control title ({kibana-pull}172094[#172094]).
* Displays incomplete results warning in layer legend ({kibana-pull}171144[#171144]).
* Updates incomplete data messaging ({kibana-pull}169578[#169578]).
Reporting::
* Makes searches used for CSV export inspectable ({kibana-pull}171248[#171248]).
* Adds `max_concurrent_shards` setting to schema for the point in time CSV report generation ({kibana-pull}170344[#170344]).
Security::
* The default value of the `elasticsearch.requestHeadersWhitelist` configuration option has been expanded to include the `es-client-authentication` HTTP header, in addition to `authorization` ({kibana-pull}172444[#172444]).
* Adds risk engine missing privileges callout ({kibana-pull}171250[#171250]).
* Implements Asset Criticality Create, Read & Delete APIs ({kibana-pull}172073[#172073]).

### Bug Fixes

Alerting::
* Fixes the alert details page search bar not considering Query configurations in the Kibana advanced settings ({kibana-pull}172498[#172498]).
* Fixes adding evaluation threshold to alert payload for ES query rule ({kibana-pull}171571[#171571]).
* Hides the Logs tab in Rules page to unauthorized users ({kibana-pull}171417[#171417]).
* Fixes hyperlinks in Slack messages being broken when there is "_" or "*" in the URL ({kibana-pull}170067[#170067]).
APM::
* Removes usage of internal client when fetching agent configuration etags metrics ({kibana-pull}173001[#173001]).
* Fixes encoding custom links values ({kibana-pull}171032[#171032]).
* Fixes an issue where data views were previously not space aware ({kibana-pull}170857[#170857]).
* Fixes issue with onboarding page around java agent ({kibana-pull}168816[#168816]).
* Adds a data tier filter to the `/has_data` API ({kibana-pull}173382[#173382]).
Cases::
* Fixes a bug that prevented users with read permission from being assigned to cases ({kibana-pull}172047[#172047]).
Dashboard::
* Prevents unnecessary loss of dashboard unsaved state ({kibana-pull}167707[#167707]).
Discover::
* Fixes escaping column names when copying ({kibana-pull}170997[#170997]).
* Discover sharing links now preserve customized column widths ({kibana-pull}172405[#172405]).
* Fixes displaying the columns as they are returned from the query ({kibana-pull}171874[#171874]).
* Fixes issue with `defaultColumns` when changing data views ({kibana-pull}168994[#168994]).
Elastic Security::
For the Elastic Security 8.12.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Allows agent upgrades if patch version is higher than Kibana ({kibana-pull}173167[#173167]).
* Fixes secrets with dot-separated variable names ({kibana-pull}173115[#173115]).
* Fixes endpoint privilege management endpoints return errors ({kibana-pull}171722[#171722]).
* Fixes expiration time for immediate bulk upgrades being too short ({kibana-pull}170879[#170879]).
* Fixes incorrect overwrite of `logs-*` and `metrics-*` data views on every integration install ({kibana-pull}170188[#170188]).
* Creates intermediate objects when using dynamic mappings ({kibana-pull}169981[#169981]).
Lens & Visualizations::
* Fixes the sorting of null values so they are displayed last ({kibana-pull}172691[#172691]).
* Fixes the overwriting of chart descriptions after editing a visualization in *Lens* ({kibana-pull}172653[#172653]).
* Fixes an issue where the timerange panel wasn't correctly assigned during a conversion from dashboard to *Lens* ({kibana-pull}172647[#172647]).
* Various fixes for heatmap in *Lens* ({kibana-pull}172602[#172602]).
* Fixes filters being lost when navigating from dashboard -> editor -> *Lens* in *TSVB* ({kibana-pull}172566[#172566]).
* Ignore drop ES|QL commands for date histogram in discover ({kibana-pull}171769[#171769]).
Machine Learning::
* Ensures data frame analytics job can be deleted from analytics map ({kibana-pull}174212[#174212]).
* Fixes filter for boolean fields filtering for numbers in Field statistics / Data Visualizer ({kibana-pull}174212[#174050])
* Fixes registering of the ML alerting rules with the basic license ({kibana-pull}173644[#173644]).
* Fixes display of actions column in the datafeed chart flyout ({kibana-pull}173365[#173365]).
* Fixes View in Discover option in Anomaly explorer not handling multiple field values or values with quotation marks ({kibana-pull}172897[#172897]).
* Fixes field stats in Discover showing 0 sample count at times when switching data views ({kibana-pull}172734[#172734]).
* Fixes long field names overflowing in Anomaly detection wizard detector selection ({kibana-pull}172715[#172715]).
* Fixes data drift numeric fields not showing correctly ({kibana-pull}172504[#172504]).
* Fixes Data Visualizer / ML field stats and Data Frame Analytics to exclude _tier fields ({kibana-pull}172223[#172223]).
* Uses standard analyzer in log pattern analysis to ensure filter in Discover matches correct documents ({kibana-pull}172188[#172188]).
* Fixes ML node check and checks user privileges to create job button in dashboard ({kibana-pull}172022[#172022]).
* Fixes Kibana object list in new job from recognized index page ({kibana-pull}171935[#171935]).
Management::
* Fixes retention policy field name not setting by default correctly in the Transform creation wizard ({kibana-pull}172609[#172609]).
Metrics::
* Moves formulas and dashboard config to inventory models ({kibana-pull}171872[#171872]).
Platform::
* Fixes a bug that could cause the `rollingFile` log appender to not properly rotate files on DST switch days ({kibana-pull}173811[#173811]).
* Fixes context formula functions ({kibana-pull}172710[#172710]).
Observability::
* Removes legacy screenshot image data from the codepath in Synthetics ({kibana-pull}172684[#172684]).
* Fixes incorrect rule parameters when changing aggregation type using a custom equation ({kibana-pull}171958[#171958]).
* Adds parent link in host detail's breadcrumb ({kibana-pull}170792[#170792]).
Presentation::
* Fixes validation query for nested fields ({kibana-pull}173690[#173690]).
* Fixes user privileges around Links panels saved to the library ({kibana-pull}173332[#173332]).
* Prevents overflowing dashboard title on saved toast notifications ({kibana-pull}172620[#172620]).
* Ignore indices without geometry field in vector tile requests ({kibana-pull}171472[#171472]).
* Fixes layer displaying no data instead of error ({kibana-pull}170084[#170084]).


## Kibana 8.11.4

### Bug fixes and enhancements

There are no user-facing changes in the 8.11.4 release.
