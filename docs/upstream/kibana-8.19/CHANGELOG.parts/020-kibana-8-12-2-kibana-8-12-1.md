<!-- Part 20 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.12.2

The 8.12.2 release includes the following bug fixes.

### Bug Fixes

Alerting::
* Fixes Discover results when an alert excludes matches from previous runs ({kibana-pull}176690[#176690]).
* Fixes bug where using select all on the rules list bypassed filters ({kibana-pull}176962[#176962]).
Elastic Security::
For the Elastic Security 8.12.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes a popover about inactive agents not being dismissible ({kibana-pull}176929[#176929]).
* Fixes logstash output being [RFC-952](https://www.rfc-editor.org/rfc/rfc952) compliant ({kibana-pull}176298[#176298]).
* Fixes assets being unintentionally moved to the default space during Fleet setup ({kibana-pull}176173[#176173]).
* Fixes categories labels in integration overview ({kibana-pull}176141[#176141]).
* Fixes the ability to delete agent policies with inactive agents from UI, the inactive agents need to be unenrolled first ({kibana-pull}175815[#175815]).
Machine Learning::
* Fixes Single Metric Viewer's zoom range settings in URL not being restored if the URL specifies a `forecastId` ({kibana-pull}176969[#176969]).
* Fixes incorrect document count values in Top Values statistics ({kibana-pull}176328[#176328]).
* Fixes color of markers in Single Metric Viewer when there is sparse data for anomaly detection ({kibana-pull}176303[#176303]).
Management::
* Fixes package showing 'Needs authorization' warning even after transform assets were authorized successfully ({kibana-pull}176647[#176647]).
Observability::
* Fixes and simplifies write access default behavior ({kibana-pull}177088[#177088]).
* Fixes recall speed when using CVS output ({kibana-pull}176428[#176428]).


## Kibana 8.12.1

The 8.12.1 release includes the following enhancements and bug fixes.

### Enhancements

Elastic Security::
For the Elastic Security 8.12.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Observability::
* Adds `defer_validation: true` to transforms on creation to stop errors when the destination index doesn't exist yet ({kibana-pull}174463[#174463]).

### Bug Fixes

Alerting::
* Fixes context variables not being passed in to the action parameters when an alert- as-data document is available ({kibana-pull}175682[#175682]).
* Fixes the Rules page loosing user selections when navigating back ({kibana-pull}174954[#174954]).
* Fixes the custom threshold rendering in the create rule flyout ({kibana-pull}174982[#174982]).
APM::
* Fixes a transactions error link for mobile ({kibana-pull}174655[#174655]).
* Increases the number of maximum function calls from 3 to 5 ({kibana-pull}175588[#175588]).
Dashboard::
* Fixes a caching issue that caused problems updating dashboard information ({kibana-pull}175635[#175635]).
Elastic Security::
For the Elastic Security 8.12.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes the display of category label on the Integration overview page ({kibana-pull}176141[#176141]).
* Fixes conflicting dynamic template mappings for intermediate objects ({kibana-pull}175970[#175970]).
* Fixes reserved keys for Elasticsearch output YAML box ({kibana-pull}175901[#175901]).
* Prevent deletion of agent policies with inactive agents from UI ({kibana-pull}175815[#175815]).
* Fixes incorrect count of agents in bulk actions ({kibana-pull}175318[#175318]).
* Fixes a custom integrations not displaying on the Installed integrations page ({kibana-pull}174804[#174804]).
Lens & Visualizations::
* Fixes a validation error for invalid formula and math columns in *Lens* ({kibana-pull}175644[#175644]).
Machine Learning::
* Fixes Allocation rendering for failed deployments ({kibana-pull}174882[#174882]).
* Fixes an issue where a user could create an anomaly rule but couldn't see it or interact with the rule via stack management ({kibana-pull}174791[#174791]).
Security::
* Fixes API Key table sorting ({kibana-pull}175813[#175813]).
* Ensures all API Keys have a defined name ({kibana-pull}175721[#175721]).
* Fixes an issue with `@kbn-handlebars`, where nested inputs were not being escaped properly ({kibana-pull}175490[#175490]).
