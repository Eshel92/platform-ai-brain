<!-- Part 24 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.10.0

**Important:** Kibana 8.10.0 has been withdrawn.

For information about the Kibana 8.10.0 release, review the following information.

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

### Security updates

* An issue was discovered by Elastic whereby sensitive information is recorded
in Kibana logs in the event of an error. The issue impacts only Kibana version
8.10.0 when logging in the JSON layout or when the pattern layout is configured
to log the `%meta` pattern.
The issue is resolved in Kibana 8.10.1. Version 8.10.0 has been removed from our
download sites.
For more information, see our related
https://discuss.elastic.co/t/kibana-8-10-1-security-update/343287[security
announcement].

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.10.0, review the breaking changes, then mitigate the impact to your application.

**New summary search capabilities cause existing SLOs to stop working**
*Details* +
New summary search capabilities introduce breaking changes in various places, and we have decided not to handle backward compatibility:

* SLO find API body parameters have changed.
* The index mapping used by the rollup data has changed, and we have added a summary index that becomes the new source of truth for search.
* The rollup transforms have been updated, but existing SLO with their transforms won't be updated.

If some SLOs have been installed in a prior version at 8.10, they won't work after migrating to 8.10. There are two approaches to handle this breaking change. The recommended route is to delete all SLOs before migrating to 8.10. The alternative is to migrate to 8.10 and manually remove the SLOs.

*Removing SLOs before migrating to 8.10*

Use the SLO UI or the SLO delete API to delete all existing SLOs. This takes care of the Saved Object, Transform and rollup data. When all SLOs have been deleted, then delete the residual rollup indices: `.slo-observability.sli-v1*`. Note that this is v1.

*Removing SLOs after migrating to 8.10*

After migrating to 8.10, the previously created SLOs won’t appear in the UI because the API is using a new index. The previously created SLOs still exist, and associated transforms are still rolling up data into the previous index `.slo-observability.sli-v1*`. The SLO delete API can't be used now, so remove the resources resources manually:

. Find all existing transforms
All SLO related transforms start with the `slo-` prefix, this request returns them all:
```bash
GET _transform/slo-*
```
Make a note of all the transforms IDs for later.

. Stop all transforms
```bash
POST _transform/slo-*/_stop?force=true
```

. Remove all transforms
From the list of transforms returned during the first step, now delete them one by one:
```bash
DELETE _transform/{transform_id}?force=true
```

. Find the SLO saved objects
This request lists all the SLO saved objects. The SLO IDs and the saved object IDs are not the same.
```bash
GET kbn:/api/saved_objects/_find?type=slo
```
Make a note of all the saved object IDs from the response.

. Remove the SLO saved objects
For each saved object ID, run the following:
```bash
DELETE kbn:/api/saved_objects/slo/{Saved_Object_Id}
```

. Delete the rollup indices v1
Note that this is v1.
```bash
DELETE .slo-observability.sli-v1*
```

**Get case metrics APIs now internal**
*Details* +
The get case metrics APIs are now internal. For more information, refer to ({kibana-pull}162506[#162506]).

**Case limits**
*Details* +
Limits are now imposed on the number of objects cases can process or the amount of data those objects can store.
For the full list, refer to [#146945](https://github.com/elastic/kibana/issues/146945).

.`addProcessorDefinition` is removed
*Details* +
The function `addProcessorDefinition` is removed from the Console plugin start contract (server side). For more information, refer to ({kibana-pull}159041[#159041]).

**The Download CSV endpoint has changed.**
*Details* +
The API endpoint for downloading a CSV file from a saved search in the Dashboard application has changed to reflect the fact that this is an internal API. The previous API path of
`/api/reporting/v1/generate/immediate/csv_searchsource` has been changed to `/internal/reporting/generate/immediate/csv_searchsource`. For more information, refer to {kibana-pull}162288[#162288].

### Deprecations

The following functionality is deprecated in 8.10.0, and will be removed in 9.0.0.
Deprecated functionality does not have an immediate impact on your application, but we strongly recommend
you make the necessary updates after you upgrade to 8.10.0.

**Action variables in the UI and in tests that were no longer used have been replaced**
*Details* +
The following rule action variables have been deprecated; use the recommended variables (in parentheses) instead:

* alertActionGroup (alert.actionGroup)
* alertActionGroupName (alert.actionGroupName)
* alertActionSubgroup (alert.actionSubgroup)
* alertId (rule.id)
* alertInstanceId (alert.id)
* alertName (rule.name)
* params (rule.params)
* spaceId (rule.spaceId)
* tags (rule.tags)

For more information, refer to ({kibana-pull}161136[#161136]).

### Features

Kibana 8.10.0 adds the following new and notable features.

Alerting::
* Adds support for self-signed SSL certificate authentication in webhook connector ({kibana-pull}161894[#161894]).
* Allow runtime fields to be selected for Elasticsearch query rule type 'group by' or 'aggregate over' options ({kibana-pull}160319[#160319]).
APM::
* Adds KQL filtering in APM rules ({kibana-pull}163825[#163825]).
* Make service group saved objects exportable ({kibana-pull}163569[#163569]).
* Added ability to manage cross-cluster API keys ({kibana-pull}162363[#162363]).
* Enable Trace Explorer by default ({kibana-pull}162308[#162308]).
* Adds error.grouping_name to group alerts in Error Count rule ({kibana-pull}161810[#161810]).
* Adds query to check for overflow bucket in service groups ({kibana-pull}159990[#159990]).
Elastic Security::
For the Elastic Security 8.10.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.10.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].
Fleet::
* Only enable secret storage once all fleet servers are above 8.10.0 ({kibana-pull}163627[#163627]).
* Kafka integration API ({kibana-pull}159110[#159110]).
Machine Learning::
* AIOps: Adds/edits change point charts embeddable from the Dashboard app ({kibana-pull}163694[#163694]).
* AIOps: Adds change point detection charts embeddable ({kibana-pull}162796[#162796]).
* Adds ability to deploy trained models for data frame analytics jobs ({kibana-pull}162537[#162537]).
* Adds map view for models in Trained Models and expands support for models in Analytics map ({kibana-pull}162443[#162443]).
* Adds new Data comparison view ({kibana-pull}161365[#161365]).
Management::
* Added ability to create a remote cluster with the API key based security model ({kibana-pull}161836[#161836]).
* REST endpoint for swapping saved object references ({kibana-pull}157665[#157665]).
Maps::
* Maps tracks layer now uses group by time series logic ({kibana-pull}159267[#159267]).
Observability::
* SLO definition and computed values are now summarized periodically into a summary search index, allowing users to search by name, tags, SLO budgeting type or time window, and even by and sort by error budget consumed, error budget remaining, SLI value or status ({kibana-pull}162665[#162665]).
* Adds indicator to support histogram fields ({kibana-pull}161582[#161582]).

For more information about the features introduced in 8.10.0, refer to What's new in 8.10.

### Enhancements and bug fixes

For detailed information about the 8.10.0 release, review the enhancements and bug fixes.

### Enhancements

Alerting::
* Fixes the event log data stream to use Data stream lifecycle instead of Index Lifecycle Management. If you had previously customized the Kibana event log ILM policy, you should now update the lifecycle of the event log data stream itself. ({kibana-pull}163210[#163210]).
* KQL search bar for Rules page ({kibana-pull}158106[#158106]).
APM::
* Lens function ({kibana-pull}163872[#163872]).
* Adds several function implementations to the AI Assistant ({kibana-pull}163764[#163764]).
* Feature controls ({kibana-pull}163232[#163232]).
* Added improved JVM runtime metrics dashboard ({kibana-pull}162460[#162460]).
* Move to new plugin, update design and use connectors ({kibana-pull}162243[#162243]).
* Adding endpoint to upload android map files ({kibana-pull}161252[#161252]).
* Navigate from the transaction details view into the Profiling ({kibana-pull}159686[#159686]).
Dashboard::
* Change badge color in options list ({kibana-pull}161401[#161401]).
* Edit title, description, and tags from dashboard listing page ({kibana-pull}161399[#161399]).
* Editing toolbar update ({kibana-pull}154966[#154966]).
Discover::
* Inline shard failures warnings ({kibana-pull}161271[#161271]).
* Improve shard error message formatting ({kibana-pull}161098[#161098]).
Elastic Security::
For the Elastic Security 8.10.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.10.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].
Fleet::
* Adds support for runtime fields ({kibana-pull}161129[#161129]).
Lens & Visualizations::
* Migrate range slider to `EuiDualRange` and make styling consistent across all controls ({kibana-pull}162651[#162651]).
* Introduce new duration formatter in *Lens* ({kibana-pull}162246[#162246]).
* Create a filter with field:value when last value metric is used on a data table in *Lens* ({kibana-pull}160509[#160509]).
* Adds tooltip for partition and heatmap filtering ({kibana-pull}162716[#162716]).
Machine Learning::
* Hides paging controls in anomaly swim lane if only one page is available ({kibana-pull}163931[#163931]).
* Adds a throughput description in the Trained Models Deployment stats table ({kibana-pull}163481[#163481]).
* Provides hints for empty fields in dropdown options in Anomaly detection & Transform creation wizards, Change point detection view ({kibana-pull}163371[#163371]).
* AIOps: Adds dip support to log rate analysis in ML AIOps Labs ({kibana-pull}163100[#163100]).
* AIOps: Improves table hovering for log rate analysis ({kibana-pull}162941[#162941]).
* AIOps: Adds dip support for log rate analysis in observability alert details page ({kibana-pull}162476[#162476]).
* Adds validation of field selected for log pattern analysis ({kibana-pull}162319[#162319]).
* AIOps: Renames Explain Log Rate Spikes to Log Rate Analysis ({kibana-pull}161764[#161764]).
* Adds new Data comparison view ({kibana-pull}161365[#161365]).
* Adds test UI for text expansion models ({kibana-pull}159150[#159150]).
* Adds update index mappings step to ML pipeline config workflow ({kibana-pull}163723[#163723]).
Management::
* Adds multiple formats for geo_point fields and make geo conversion tools part of field_format/common/utils ({kibana-pull}147272[#147272]).
Maps::
* Support time series split for top hits per entity source ({kibana-pull}161799[#161799]).
Observability::
* Adds support for group by to SLO burn rate rule ({kibana-pull}163434[#163434]).
* Applying consistent design to Histogram and Custom Metric forms ({kibana-pull}162083[#162083]).
* Adds preview chart to custom metric indicator ({kibana-pull}161597[#161597]).
* Support filters for good/total custom metrics ({kibana-pull}161308[#161308]).
Reporting::
* Increase max size bytes default to 250mb ({kibana-pull}161318[#161318]).
Security::
* Change the default value of `session.idleTimeout` from 8 hours to 3 days ({kibana-pull}162313[#162313]).
* User roles displayed on the user profile page ({kibana-pull}161375[#161375]).
Uptime::
* Implement private location run once ({kibana-pull}162582[#162582]).

### Bug fixes

APM::
* Fixes styling and port issue with new onboarding ({kibana-pull}163922[#163922]).
* Fixes missing alert index issue ({kibana-pull}163600[#163600]).
* Fixes trace waterfall loading logic to handle empty scenarios ({kibana-pull}163397[#163397]).
* Fixes the action menu overlapping the 'Create custom link' flyout ({kibana-pull}162664[#162664]).
* Improve service groups error messages and validations ({kibana-pull}162556[#162556]).
* Fixes throwing appropriate error when user is missing necessary permission ({kibana-pull}162466[#162466]).
* Hide components when there is no support from agents ({kibana-pull}161970[#161970]).
* Fixes link to onboarding page in the Observability Onboarding plugin ({kibana-pull}161847[#161847]).
Dashboard::
* Disables top navigation actions when cloning or overlay is showing ({kibana-pull}162091[#162091]).
Discover::
* Fixes document failing to load when the ID contains a slash ({kibana-pull}160239[#160239]).
* Fixes NoData screen in alignment with Dashboard and Lends behavior ({kibana-pull}160747[#160747]).
Elastic Security::
For the Elastic Security 8.10.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Enterprise Search::
For the Elastic Enterprise Search 8.10.0 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].
Fleet::
* Only show agent dashboard links if there is more than one non-server agent and if the dashboards exist ({kibana-pull}164469[#164469]).
* Exclude Synthetics from per-policy-outputs ({kibana-pull}161949[#161949]).
* Fixing the path for hint templates for auto-discover ({kibana-pull}161075[#161075]).
Lens & Visualizations::
* Fixes params._interval conversion to Lens formula ({kibana-pull}164150[#164150]).
* Fixes issues with field name that contains the `:` character in it in *Lens* ({kibana-pull}163626[#163626]).
* Fixes other request merge behavior when empty string key is retrieved ({kibana-pull}163187[#163187]).
* Fixes editing of multi values filters when adding a custom item ({kibana-pull}161940[#161940]).
* Allow setting custom colors to be collapsed by slices pie's multiple metrics in *Lens* ({kibana-pull}160592[#160592]).
* Fixes data table sorting for keyword values in *Lens* ({kibana-pull}160163[#160163]).
* Fixes override parameter when creating data views ({kibana-pull}160953[#160953]).
Logs::
* Amend lazy imports in logs_shared plugin ({kibana-pull}164102[#164102]).
Machine Learning::
* Fixes Trained models list crashes on browser refresh if not on page 1 ({kibana-pull}164163[#164163]).
* Fixes query bar not switching from KQL to Lucene and vice versa in Anomaly explorer ({kibana-pull}163625[#163625]).
* Data Frame Analytics creation wizard: ensures validation works correctly ({kibana-pull}163446[#163446]).
* Fixes capabilities polling in manage page ({kibana-pull}163399[#163399]).
* Fixes unhandled promise rejection from ML plugin ({kibana-pull}163129[#163129]).
* AIOps: Uses Kibana's http service instead of fetch and fixes throttling ({kibana-pull}162335[#162335]).
* Uses model supplied mask token for testing trained models ({kibana-pull}162168[#162168]).
Management::
* Fixes how a bulk request body with variables are processed in Console ({kibana-pull}162745[#162745]).
* Improves a way of variable substitution and its documentation in Console ({kibana-pull}162382[#162382]).
* Transforms: Reduces rerenders and multiple fetches of source index on transform wizard load ({kibana-pull}160979[#160979]).
Maps::
* Fixes Map layer preview blocks adding layer until all tiles are loaded ({kibana-pull}161994[#161994]).
Monitoring::
* Rewrite CPU usage rule to improve accuracy ({kibana-pull}159351[#159351]).
Observability::
* Fixes email connector rule URL ({kibana-pull}162954[#162954]).
* Disable the 'View rule details' option from the Alert Details' Actions list when the rule is deleted ({kibana-pull}163183[#163183]).
Reporting::
* Fixes a bug where Kibana Reporting would not work in Elastic Docker without adding a special setting in kibana.yml to disable the Chromium sandbox. ({kibana-pull}149080[#149080]).
* Fixes an issue where certain international characters would not appear correctly in the contents of a print-optimized PDF report of a dashboard ({kibana-pull}161825[#161825]).
Uptime::
* Fixes auto-expand feature for failed step detail ({kibana-pull}162747[#162747]).


## Kibana 8.9.2

Review the following information about the Kibana 8.9.2 release.

### Enhancements

Fleet::
* Adds the configuration setting `xpack.fleet.packageVerification.gpgKeyPath` as an environment variable in the Kibana container ({kibana-pull}163783[#163783]).

### Bug fixes

Dashboard::
* Fixes missing state on short URLs could be lost on an alias match redirect ({kibana-pull}163658[#163658]).
* Fixes 'Download CSV' returning no data when panel has custom time range outside the time range of the global time picker ({kibana-pull}163887[#163887]).
* Fixes **Dashboard** getting stuck at loading in Kibana when Controls is used and mapping changed from integer to keyword ({kibana-pull}163529[#163529]).
Elastic Security::
For the Elastic Security 8.9.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Lens & Visualizations::
* Allow removing temporary data view from event annotation group in *Lens* ({kibana-pull}163976[#163976]).
Machine Learning::
* Anomaly detection wizard: ensure custom URLs test functionality works as expected ({kibana-pull}165055[#165055]).
* Fixes anomaly detection module manifest queries for Kibana sample data sets, so cold and frozen tiers are not queried ({kibana-pull}164332[#164332]).
Management::
* Transforms: Fixes privileges check ({kibana-pull}163687[#163687]).
Operations::
* Fixes an issue where Kibana did not start on CentOS/RHEL 7 ({kibana-pull}165151[#165151]).
Reporting::
* Allow custom roles to use image reporting in **Dashboard** ({kibana-pull}163873[#163873]).
