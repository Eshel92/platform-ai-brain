<!-- Part 12 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.16.3

The 8.16.3 release includes the following known issues and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Alerting::
* Updates handling of invalid RRule params and prevents infinite looping ({kibana-pull}205650[#205650]).
* Fixes an issue with saving ECS group by fields at the root level for query DSL rules ({kibana-pull}203769[#203769]).
* Fixes race condition in alerting rules data view selector ({kibana-pull}203654[#203654]).
Data ingestion and Fleet::
* Fixes an issue with showing all agent tags when agent list is filtered ({kibana-pull}205163[#205163]).
Elastic Observability solution::
* Preserves `kuery` filters when switching between Universal Profiling pages in new solution navigation ({kibana-pull}203545[#203545]).
Elastic Search solution::
* Adds ML as required plugin to Search Assistant ({kibana-pull}204009[#204009]).
* Fixes web crawler name inconsistencies ({kibana-pull}202738[#202738]).
Elastic Security solution::
For the Elastic Security 8.16.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes Integration and Datastream name validation ({kibana-pull}204943[#204943]).
* Adds RBAC to the Automatic Import APIs ({kibana-pull}203882[#203882]).


## Kibana 8.16.2

The 8.16.2 release includes the following known issues, enhancements, and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Enhancements

In this release, we've introduced an image based on the hardened [Wolfi](https://github.com/wolfi-dev/) image to provide additional security to our self-managed customers, and improve our supply chain security posture. Wolfi-based images require Docker version 20.10.10 or higher.

### Bug fixes

Alerting::
* Fixes Slack API connectors not displayed under Slack connector when adding new connector to rule ({kibana-pull}202315[#202315]).
Dashboards::
* Prevents resetting panel to undefined or empty last saved state ({kibana-pull}203158[#203158]).
Data ingestion and Fleet::
* Allows to create integration policy with no agent policies ({kibana-pull}201051[#201051]).
Elastic Observability solution::
* Preserves `kuery` filters when switching between Universal Profiling pages in new solution navigation ({kibana-pull}203545[#203545]).
* Fixes error when opening rule flyout ({kibana-pull}202386[#202386]).
* Handles ops genie as default connector ({kibana-pull}201923[#201923]).
Elastic Search solution::
* Adds ML as required plugin to Search Assistant ({kibana-pull}204009[#204009]).
* Fixes web crawler name inconsistencies ({kibana-pull}202738[#202738]).
Elastic Security solution::
For the Elastic Security 8.16.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Adds `search` as a term for `elasticsearch` solution_type ({kibana-pull}201688[#201688]).
* Adds a11y connector improvements ({kibana-pull}201590[#201590]).
* Fixes issue with generating short url when copying share link ({kibana-pull}201475[#201475]).
Kibana security::
* Fixes error with opening a point in time query for session deletion by now accounting for partial results ({kibana-pull}203413[#203413]).
* Adds functionality to restrict unsupported log formats ({kibana-pull}202994[#202994]).
* Adds functionality to restrict and reject CEF logs in Automatic Import and redirect to CEF integration instead ({kibana-pull}201792[#201792]).
* Removes fields with @ from the script processor ({kibana-pull}201548[#201548]).
Lens & Visualizations::
* Fixes point visibility regression in *TSVB* ({kibana-pull}202358[#202358]).
Machine Learning::
* Trained Models: Fixes spaces sync to retrieve 10000 models ({kibana-pull}202712[#202712]).
* Trained Models: Shows deployment stats for unallocated deployments ({kibana-pull}202005[#202005]).
* Trained Models: Fixes start deployment with ML autoscaling and 0 active nodes ({kibana-pull}201256[#201256]).
* Trained Models: Fixes `NaN` in a progress bar during the download task initialization ({kibana-pull}201221[#201221]).
* Single Metric Viewer embeddable: Fixes continuous job refetch when errors are encountered ({kibana-pull}199726[#199726]).


## Kibana 8.16.1

The 8.16.1 release includes the following known issues and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Dashboards & Visualizations::
* Fixes an issue preventing a custom panel title from being saved correctly ({kibana-pull}200548[#200548]).
Elastic Observability solution::
* Changes the order of the errors shown on Infrastructure applications to be more relevant ({kibana-pull}200531[#200531]).
* Fixes the summary calculation for a calendar-aligned and occurrences-based SLO ({kibana-pull}199873[#199873]).
* Fixes the `kustomize` command ({kibana-pull}199758[#199758]).
Elastic Security solution::
For the Elastic Security 8.16.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Platform::
* Fixes an issue with duplicate references to objects when copying saved objects to other spaces ({kibana-pull}200053[#200053]).
* Fixes button colors in the "Share data view to spaces" flyout ({kibana-pull}196004[#196004]).
