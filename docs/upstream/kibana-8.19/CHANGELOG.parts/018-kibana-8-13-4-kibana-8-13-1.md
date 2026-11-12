<!-- Part 18 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.13.4

The 8.13.4 release includes the following bug fixes.

### Bug Fixes

Lens & Visualizations::
* Fixes table sorting when changing the interval on the time picker in *Lens* ({kibana-pull}182173[#182173]).
Dashboards::
* Fixes a bug with drilldowns where the control group on a source dashboard could be replaced by the control group from the destination dashboard ({kibana-pull}179485[#179485]).


## Kibana 8.13.3

The 8.13.3 release includes the following bug fixes.

### Bug Fixes

Alerting::
* Manage loading fields at initialization ({kibana-pull}180412[#180412]).
Elastic Security::
For the Elastic Security 8.13.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes managed agent policy preconfiguration update ({kibana-pull}181624[#181624]).
* Use lowercase dataset in template names ({kibana-pull}180887[#180887]).
* Fixes KQL/kuery for getting Fleet Server agent count ({kibana-pull}180650[#180650]).
Index Management::
* Fixes `allow_auto_create` field in the Index Template form ({kibana-pull}178321[#178321]).
Lens & Visualizations::
* Fixes controls on fields with custom label ({kibana-pull}180615[#180615]).
Machine Learning::
* Fixes deep link for Index data visualizer & ES|QL data visualizer ({kibana-pull}180389[#180389]).
Observability::
* Make anomalyDetectorTypes optional ({kibana-pull}180717[#180717]).
SharedUX::
* Revert change to shared UX markdown component for dashboard vis ({kibana-pull}180906[#180906]).
Sharing::
* Default to saved object description when panel description is not provided ({kibana-pull}181177[#181177]).


## Kibana 8.13.2

The 8.13.2 release includes the following bug fixes.

### Bug Fixes

Canvas::
* Fixes text settings to be honored in Canvas markdown elements ({kibana-pull}179948[#179948]).
* Fixes custom styling for Canvas markdown Workpads ({kibana-pull}180070[#180070]).
Discover::
* Fixes keyboard navigation for search input on the document viewer flyout ({kibana-pull}180022[#180022]).
Elastic Security::
For the Elastic Security 8.13.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes having to wait ten minutes after agent upgrade if agent cleared watching state ({kibana-pull}179917[#179917]).
Fixes using the latest available version in K8's manifest instead of the latest compatible version ({kibana-pull}179662[#179662]).
* Fixes a step in add agent instructions where a query to get all agents was unnecessary ({kibana-pull}179603[#179603]).
Lens & Visualizations::
* Fixes custom styling for TSVB markdown visualizations ({kibana-pull}180053[#180053]).
Machine Learning::
* Single Metric Viewer embeddable: Ensures the detector index is passed to chart correctly ({kibana-pull}179761[#179761]).
* AIOps: Fixes text field candidate selection for log rate analysis ({kibana-pull}179699[#179699]).
Management::
* Fixes the Response tab loading time to be faster ({kibana-pull}180035[#180035]).
Maps::
* Fixes APM data view ID ({kibana-pull}179257[#179257]).
Monitoring::
* Fixes a runtime error by adding a default value for source and target ({kibana-pull}180043[#180043]).
Operations::
* Fixes an issue with Kibana looking for a configuration file outside of the Kibana home directory, potentially preventing startup due to insufficient permissions ({kibana-pull}179847[#179847]).


## Kibana 8.13.1

The 8.13.1 release includes the following bug fixes.

### Enhancements

Fleet::
* Remove `index.query.default_field` setting from managed component template settings ({kibana-pull}178020[#178020]).

### Bug Fixes

Alerting::
* Limit useEffect to calculate view in app URL ({kibana-pull}179197[#179197]).
Data Discovery::
* Hide "Save"/"Save as" actions from "Unsaved changes" badge for read-only users ({kibana-pull}179132[#179132]).
Elastic Security::
For the Elastic Security 8.13.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Use index exists check in fleet-metrics-task ({kibana-pull}179404[#179404]).
Lens & Visualizations::
* Fixes wilcard complex scenarios ({kibana-pull}178938[#178938]).
Machine Learning::
* AIOps: Fix text field candidate selection for log rate analysis ({kibana-pull}179699[#179699]).
Observability::
* Fall back to top 5 docs on scoring error ({kibana-pull}179615[#179615]).
* Fixing APM data view id ({kibana-pull}179257[#179257]).
