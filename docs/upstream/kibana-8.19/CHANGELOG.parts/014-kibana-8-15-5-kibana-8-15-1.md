<!-- Part 14 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.15.5

The 8.15.5 release includes the following known issues and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Canvas::
* Fixes an issue with Canvas not rendering maps with queries or filters ({kibana-pull}199339[#199339]).
Discover::
* Fixes an issue where the `has_es_data` check was causing Kibana to hang ({kibana-pull}200476[#200476]).
Elastic Observability solution::
* Changes the order of the errors shown on Infrastructure applications to be more relevant ({kibana-pull}200531[#200531]).
* Fixes the summary calculation for a calendar-aligned and occurrences-based SLO ({kibana-pull}199873[#199873]).
Elastic Security solution::
For the Elastic Security 8.15.5 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Platform::
* Fixes an issue with duplicate references to objects when copying saved objects to other spaces ({kibana-pull}200053[#200053]).
* Fixes button colors in the "Share data view to spaces" flyout ({kibana-pull}196004[#196004]).


## Kibana 8.15.4

The 8.15.4 release includes the following known issues and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Dashboards and visualizations::
* Fixes incomplete string escaping and encoding in *TSVB* ({kibana-pull}196248[#196248]).
* Adds scroll margin to panels ({kibana-pull}193430[#193430]).
* Fixes an issue where label truncation in heat map legends was not working properly in *Lens* ({kibana-pull}195928[#195928]).
Discover::
* Fixes the width for saved object Type column ({kibana-pull}194388[#194388]).
Elastic Observability solution::
* Changes the slice outcome from bad to good whenever there is no data during the slice window ({kibana-pull}196942[#196942]).
Elastic Search solution::
* Fixes a bug with the [Network Drive connector](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors-network-drive.html) where advanced configuration fields were not displayed for CSV file role mappings with `Drive Type: Linux` selected ({kibana-pull}195567[#195567]).
Elastic Security solution::
For the Elastic Security 8.15.4 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Fixes an issue causing the wrong date to show in the header of a report when generated from a relative date ({kibana-pull}197027[#197027]).
* Fixes an issue with the export options for PNG/PDF reports in a dashboard ({kibana-pull}192530[#192530]).
Machine Learning::
* Fixes an issue preventing Anomaly swim lane panels from updating on query changes ({kibana-pull}195090[#195090]).
Management::
* Fixes the pagination of the source documents data grid in Transforms ({kibana-pull}196119[#196119]).


## Kibana 8.15.3

The 8.15.3 release includes the following known issues and bug fixes.

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
* Fixes a storage configuration error that could prevent the Stack Management > Alerts page from loading correctly ({kibana-pull}194785[#194785]).
* Fixes a bug preventing certain alerts with Role visibility set to "Stack Rules" from being shown on the Stack Management page ({kibana-pull}194615[#194615]).
* Fixes an issue where rules created from Discover before version 8.11.0 could no longer be accessed after upgrading ({kibana-pull}192321[#192321]).
Dashboards::
* Fixes an issue where the `embed=true` parameter was missing when sharing a dashboard with the Embed code option ({kibana-pull}194366[#194366]).
Discover::
* Fixes an issue with the document viewer panel not opening in focus mode ({kibana-pull}191039[#191039]).
Elastic Observability solution::
* Fixes the OpenTelemetry guided onboarding for MacOS with x86_64 architectures ({kibana-pull}194915[#194915]).
* Fixes a bug where the SLO creation form was allowing multiple values for timestamp fields ({kibana-pull}194311[#194311]).
Elastic Search solution::
* Fixes a bug with the [Network Drive connector](https://www.elastic.co/guide/en/enterprise-search/8.15/connectors-network-drive.html) where advanced configuration fields were not displayed for CSV file role mappings with `Drive Type: Linux` selected ({kibana-pull}195567[#195567]).
Elastic Security solution::
For the Elastic Security 8.15.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Automatic Import no longer asks the LLM to map fields to reserved ECS fields ({kibana-pull}195168[#195168]).
* Fixes an issue that was causing the Grok processor to return non-ECS compatible fields when processing structured or unstructured syslog samples in Automatic Import ({kibana-pull}194727[#194727]).
* Fixes the integrationName when uploading a new version of an existing integration using a ZIP upload ({kibana-pull}194298[#194298]).
* Fixes a bug that caused the Deploy step of Automatic Import to fail after a pipeline was edited and saved ({kibana-pull}194203[#194203]).
* Fixes an issue in the Kibana Management > Roles page where users could not sort the table by clicking the column headers ({kibana-pull}194196[#194196]).
Lens & Visualizations::
* Fixes an issue where the legend label truncation setting wasn't working properly for heat maps in Lens ({kibana-pull}195928[#195928]).
Machine Learning::
* Fixes an issue preventing Anomaly swim lane panels from updating on query changes ({kibana-pull}195090[#195090]).
* Fixes an issue that could cause the "rows per page" option to disappear from the Anomaly timeline view in the Anomaly Explorer ({kibana-pull}194531[#194531]).
* Fixes an issue causing screen flickering on the Results Explorer and Analytics Map pages when no jobs are available ({kibana-pull}193890[#193890]).


## Kibana 8.15.2

The 8.15.2 release includes the following known issues, enhancements, and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Enhancements

Elastic Security solution::
For the Elastic Security 8.15.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Bumps maximum supported package spec version to 3.2 ({kibana-pull}193574[#193574]).
Kibana security::
* Adds a feature to add support for handling `syslogs with unsupported message body` ({kibana-pull}192817[#192817]).
* Automatic Import now performs reproducible sampling from the list of log entries instead of just truncating them ({kibana-pull}191598[#191598]).
* Adds support for Google Gemini, OpenAI, and Azure OpenAI connectors to Automatic Import ({kibana-pull}191577[#191577]).
* Displays better error messages for issues with logs sample file upload in Automatic Import ({kibana-pull}191310[#191310]).

### Bug fixes

Alerting::
* Fixes error when saving a rule after toggling alerts filter properties on and off ({kibana-pull}192522[#192522]).
Dashboards::
* Fixes map layers that disappear from map panel when using session storage to continue editing a dashboard ({kibana-pull}193629[#193629]).
Discover::
* Fixes "View conflicts" button when a data view ID has special characters ({kibana-pull}192374[#192374]).
Elastic Observability solution::
* Fixes OpenTelemetry agent names ({kibana-pull}193134[#193134]).
* Resolves an issue for multi-step browser journeys where timings for cached resources within the same step were inaccurate within the waterfall chart ({kibana-pull}193089[#193089]).
* Updates parsing to skip replacing missing values in Synthetics monitors ({kibana-pull}192662[#192662]).
Elastic Security solution::
For the Elastic Security 8.15.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Prevents extra agent_status call with empty policyId ({kibana-pull}192549[#192549]).
* Sets correct title for Restart upgrade agent modal under agent list ({kibana-pull}192536[#192536]).
Kibana security::
* Stops removing message field for unstructured logs when using Automatic Import ({kibana-pull}193678[#193678]).
* Integrations created using Automatic Import now indicate that they have been developed by the `Community` instead of Elastic ({kibana-pull}193002[#193002]).
* Fixes issues with rendering the package manifest in Automatic Import ({kibana-pull}192316[#192316]).
Machine Learning::
* Fixes deletion in Check interval input for anomaly detection rule ({kibana-pull}193420[#193420]).
* Fixes unnecessary ML services initialization during plugin setup ({kibana-pull}193153[#193153]).
* Fixes link to anomaly detection wizard from pattern analysis in Discover ({kibana-pull}192375[#192375]).
* Fixes an issue with the `http_endpoint` input config loading incorrectly in an Automatic Import workflow ({kibana-pull}191964[#191964]).


## Kibana 8.15.1

The 8.15.1 release includes the following known issues and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Data Discovery::
* Fixes time range filter ({kibana-pull}187010[#187010]).
Elastic Security::
For the Elastic Security 8.15.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Remove duplicative retries from client-side requests to APIs that depend on EPR ({kibana-pull}190722[#190722]).
Lens & Visualizations::
* Visualization blows up when invalid color is passed in *TSVB* ({kibana-pull}190658[#190658]).
Observability::
* Enables wildcard search for the Synthetics waterfall chart ({kibana-pull}191132[#191132]).
* Fixes accordion disclosure keyboard focus border ({kibana-pull}190436[#190436]).
* Always pass allowLeadingWildcards as true to the KQL validation in the custom threshold rule API param validation ({kibana-pull}190031[#190031]).
* Prevent excess calls to get agent namespace ({kibana-pull}189995[#189995]).
* Fixes blank storage explorer summary when filter string is active ({kibana-pull}189760[#189760]).
* Observability AI Assistant: Use internal user when fetching connectors ({kibana-pull}190462[#190462]).
* Observability AI Assistant: Fixes bug “Cannot set initialMessages if initialConversationId is set" ({kibana-pull}189885[#189885]).
Platform::
* Fixes handling of splittable subkeys when processing values ({kibana-pull}190590[#190590]). Fixes a bug when processing YAML configuration keys that contain dotted notation in objects in arrays. This can manifest as a validation error causing Kibana to not start.
Presentation::
* Fixes by-value map embeddables have broken layers ({kibana-pull}190996[#190996]).
* Fixes text readability on map scale, attribution, and coordinate controls ({kibana-pull}189639[#189639]).
Search::
* Fixes index error incorrectly showing up ({kibana-pull}189283[#189283]). Fixes a bug where an index error about the `semantic_text` field would be incorrectly displayed when the inference endpoint was configured and available.
Uptime::
* Fixes broken pagination in Uptime when a filter is applied ({kibana-pull}189831[#189831]).
