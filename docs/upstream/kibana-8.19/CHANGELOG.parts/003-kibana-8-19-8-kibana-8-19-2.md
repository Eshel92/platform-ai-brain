<!-- Part 3 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.19.8

The 8.19.8 release includes the following enhancements and fixes.

### Enhancements

Observability::
* Adds new sub-feature privileges for Synthetics global parameters  ({kibana-pull}243821[#243821]).

### Fixes

Alerting::
* Fixes pagination for the **Alerts** table, which was getting stuck on rule details pages ({kibana-pull}242275[#242275]).
* Fetches tracked alerts without depending on the task state ({kibana-pull}235253[#235253]).
Dashboards and Visualizations::
* Fixes an error that occurs when you deselect the **(blank)** option from the filter controls menu ({kibana-pull}242036[#242036]).
Data ingestion and Fleet::
* Adds retry behavior for `/api/fleet/agents` when transient issues with {Elasticsearch} are encountered ({kibana-pull}243105[#243105]).
* Fixes `ignore_above` mapping for `flattened` fields ({kibana-pull}238890[#238890]).
Discover::
* Fixes truncation for longer text in the Discover table ({kibana-pull}241440[#241440]).
Elastic Observability solution::
* Fixes AI assistant only appearing in the Log overview for documents with the `message` field ({kibana-pull}243437[#243437]).
* Improves handling of missing `error.id` in APM errors ({kibana-pull}243638[#243638]).
* Reverts showing transform errors across all SLO pages ({kibana-pull}243013[#243013]).
* Fixes the Kubernetes pod query by changing the gap policy to include zeros ({kibana-pull}239596[#239596]).
Elastic Security solution::
For the Elastic Security 8.19.8 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Fixes the production build favicon's CSS specificity ({kibana-pull}243351[#243351]).
* Fixes an issue on the **Index management** page where screen reader text was different from visible text ({kibana-pull}243802[#243802]).
* Fixes an issue with keyboard focus getting trapped on pages using document preview ({kibana-pull}243791[#243791]).
Machine Learning::
* Preserves cell selection in Anomaly Explorer when you click out of the **Alerts** popover ({kibana-pull}244183[#244183]).
* Ensures deleted text in AI connector or Inference endpoint forms is not sent as empty strings ({kibana-pull}244059[#244059]).
* Fixes import and improves validation for Anomaly Detection and Data Frame Analytics jobs ({kibana-pull}242263[#242263]).


## Kibana 8.19.7

The 8.19.7 release includes the following known issues, enhancements, and fixes.

### Known issues

**Alerts aren't generated for rules with alert flapping off and an alert delay higher than 1.**
*Details* +

Alerts aren't generated for rules that have **Alert flapping detection** turned off and the alert delay set to a value higher than 1.

*Workaround* +
Set the alert delay value to 1 or turn on **Alert flapping detection**.

### Enhancements

Machine Learning::
* Adds a feedback button to Anomaly Explorer and Single Metric Viewer ({kibana-pull}239883[#239883]).

### Fixes

Alerting::
* In Cases, tables no longer flash when the page is loading ({kibana-pull}240155[#240155]).
* Fixes an infinite loop issue occurring when the Investigation guide of a rule's details is too long ({kibana-pull}240472[#240472]).
Dashboards and Visualizations::
* Labels in Maps' **Create index** flow now render with the default **Use vector tiles** scaling as soon as label styling is applied (or after saving), without requiring a scaling toggle ({kibana-pull}240728[#240728]).
* Fixes an issue occurring when resetting a dashboard with unsaved changes after enabling `timeRestore` and setting a time range ({kibana-pull}239992[#239992]).
Data ingestion and Fleet::
* Allows Fleet setup retries on start in all environments ({kibana-pull}240342[#240342]).
Kibana platform::
* Ensures that the `max_tokens` parameter is correctly passed as expected when connecting to Anthropic ({kibana-pull}241212[#241212]) & ({kibana-pull}241188[#241188]).
* Removes the default fallback region for the Amazon Bedrock connector ({kibana-pull}241157[#241157]).
* Fixes index names causing incompatible cluster error when product docs are installed for multiple inference IDs ({kibana-pull}240506[#240506]).
Elastic Observability solution::
* Adds missing transaction action links ({kibana-pull}241336[#241336]).
* Fixes overlapping components in the Observability AI Assistant flyout on small screens ({kibana-pull}241026[#241026]).
* Excludes stale SLOs from "group by" stats ({kibana-pull}240077[#240077]).
* Prevents Kibana tool from failing when using a proxy ({kibana-pull}236653[#236653]).
Elastic Security solution::
For the Elastic Security 8.19.7 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Machine Learning::
* Ensures that the inference endpoints list loads properly even when using a custom inference provider ({kibana-pull}240189[#240189]).


## Kibana 8.19.6

The 8.19.6 release includes the following known issues, enhancements, and fixes.

### Known issues

**Alerts aren't generated for rules with alert flapping off and an alert delay higher than 1.**
*Details* +

Alerts aren't generated for rules that have **Alert flapping detection** turned off and the alert delay set to a value higher than 1.

*Workaround* +
Set the alert delay value to 1 or turn on **Alert flapping detection**.

### Enhancements

Elastic Security solution::
For the Elastic Security 8.19.6 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Enhances error message by explaining why the role is considered malformed ({kibana-pull}239098[#239098]).

### Fixes

Alerting and cases::
* Updates `nodemailer` to `7.0.9` ({kibana-pull}238816[#238816]).
* Isolates the configuration parameters for the Tines connector to the server side ({kibana-pull}236863[#236863]).
Dashboards and Visualizations::
* Fixes bug that prevented you from deleting unsaved dashboard changes after you had enabled the `timeRestore` setting and selected a time and date using the date picker ({kibana-pull}239992[#239992]).
* Fixes error that occured when you selected a blank value in the options list ({kibana-pull}239791[#239791]).
* Fixes a bug in Lens that incorrectly assigned unsaved, ad-hoc dataview references ({kibana-pull}239431[#239431]).
* Fixes bug that broke the filter functionalty in table rows when any column is used as a formula in Lens ({kibana-pull}239222[#239222]).
* Fixes metric color assignment when breakdown and a max dimension are defined in Lens ({kibana-pull}238901[#238901]).
* Ensures adhoc dataviews from ES|QL charts aren't being filtered out in the KQL search bar ({kibana-pull}238731[#238731]).
* Fixes bug where where an error in the visualization could cause the entire **Visualize Listing** page to error. This improves the error handling to make it easier to identify which visualization is causing problems ({kibana-pull}238355[#238355]).
* Fixes bug that prevented transforming of panels in sections from URL state ({kibana-pull}237382[#237382]).
Data ingestion and Fleet::
* Fixes bug that occured during an integration policy upgrade that prevented the new package global variables from being included and stale variable references from being removed ({kibana-pull}238542[#238542]).
* Fixes error when deleting orphaned integration policies and allows you to force delete orphaned integration policies using Fleet APIs ({kibana-pull}237875[#237875]).
* Fixes an issue where fields were resetting automatically when editing ingest pipeline settings ({kibana-pull}237509[#237509]).
Discover::
* Ensures that the combined filters are considered when selecting the correct fields for the query while the `courier:ignoreFilterIfFieldNotInIndex` advanced setting is enabled ({kibana-pull}238945[#238945]).
* Clears time field sorting after going from Classic to ES|QL mode ({kibana-pull}235338[#235338]).
Elastic Observability solution::
* Removes unecessary `_source` from APM query ({kibana-pull}239205[#239205]).
* Uses word boundaries to only replace the metric name as an identifier and not as part of other text ({kibana-pull}238849[#238849]).
* Fixes error when Observability AI Assistant is disabled ({kibana-pull}238811[#238811]).
* Uses `runWithCache` for Fleet bulk operations ({kibana-pull}238326[#238326]).
* Disables max attempts for private locations sync task ({kibana-pull}237784[#237784]).
* Fixes recover alert while monitor is down ({kibana-pull}237479[#237479]).
* Fixes the AI Assistant button tooltip by closing the tooltip when you are not hovering over the button ({kibana-pull}237202[#237202]).
Kibana platform::
* Fixes files management flyout crashing ({kibana-pull}237588[#237588]).
Management::
* Fixes a bug where creating a new component template with `@custom` suffix in its name would update mappings of all unrelated data streams and a message would display asking to rollover conflicting ones ({kibana-pull}237952[#237952]).
Search::
* Fixes an issue in the RAG Playground where invalid fields displayed red styling but no error message. Error text is now shown to help users identify and correct form issues ({kibana-pull}238284[#238284]).


## Kibana 8.19.5

The 8.19.5 release includes the following known issues and fixes.

**Important:** This release contains fixes for potential security vulnerabilities. Check our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.

### Known issues

**Alerts aren't generated for rules with alert flapping off and an alert delay higher than 1.**
*Details* +

Alerts aren't generated for rules that have **Alert flapping detection** turned off and the alert delay set to a value higher than 1.

*Workaround* +
Set the alert delay value to 1 or turn on **Alert flapping detection**.

### Fixes

Alerting::
* Rolls over the reporting data stream if its template version is newer than the version in the data stream's mappings ({kibana-pull}234119[#234119]).
Dashboards and Visualizations::
* Fixes text kerning issues in PDF/PNG exports of dashboards and visualizations ({kibana-pull}235516[#235516]).
* Fixes an issue where the dashboard title would not get updated in the breadcrumb when edited from the list of dashboards ({kibana-pull}236561[#236561]).
* Fixes an issue with the Lens table's column sort order being different in the dashboard and the exported CSV ({kibana-pull}236673[#236673]).
* Updates dashboards to wait until controls are ready before rendering panels to prevent a double fetch of data ({kibana-pull}237169[#237169]).
Data ingestion and Fleet::
* Fixes an issue where fields were resetting automatically when editing ingest pipeline settings ({kibana-pull}237509[#237509]).
* Adds a unique count to improve accuracy of the number of transforms on the integrations overview page ({kibana-pull}236177[#236177]).
* Validates the Logstash pipeline ID at the Kibana API level ({kibana-pull}236347[#236347]).
* Fixes malformed synthetics package policies ({kibana-pull}236176[#236176]).
Discover::
* Clears sort by `timestamp` when navigating from classic to ES|QL mode ({kibana-pull}235338[#235338]).
* Fixes sizing issues with the **Actions** column header ({kibana-pull}235227[#235227]).
Elastic Observability solution::
* Fixes the AI Assistant button's tooltip by closing it when you click anywhere else on the page ({kibana-pull}237202[#237202]).
* Removes span documents from the `getServiceAgent` function ({kibana-pull}236732[#236732]).
* Prevents synthetics package policies from becoming malformed and reporting {agents} as unhealthy ({kibana-pull}236104[#236104]).
* Cleans up extra synthetics package policies ({kibana-pull}235200[#235200]).
Elastic Security solution::
For the Elastic Security 8.19.5 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Allows `xpack.spaces.defaultSolution` to be configured through environment variables for Docker deployments ({kibana-pull}236570[#236570]).
* Adds the ability to do partial matches and searches in the **API keys** section of Stack Management ({kibana-pull}221959[#221959]).
Machine Learning::
* Improves trained model performance by adding filters to the request to fetch all index settings ({kibana-pull}237072[#237072]).
* Hides the show forecast checkbox when selecting a new job in the Single Metric Viewer ({kibana-pull}236724[#236724]).
* Makes alerts visible in Anomaly Explorer to all Machine Learning-only users regardless of where they create rules ({kibana-pull}236289[#236289]).
* Fixes the **Job details** flyout on the **Analytics Map** page ({kibana-pull}236131[#236131]).
* Limits log rate analysis category requests to reduce `msearch` usage ({kibana-pull}235611[#235611]).
* Fixes rendering of the dashboard panel in PDF reporting for the Anomaly Swim Lane ({kibana-pull}235475[#235475]).
Search solution::
* Adds search functionality to the **Query rules** details page ({kibana-pull}232579[#232579]).
Management::
* Fixes privilege requirements when reindexing indices through Upgrade Assistant. Previously, the `superuser` role was required, but now the `cluster: manage` and `all` privileges are sufficient ({kibana-pull}237055[#237055]).


## Kibana 8.19.4

The 8.19.4 release includes the following known issues, enhancements, and fixes.

### Known issues

**Alerts aren't generated for rules with alert flapping off and an alert delay higher than 1.**
*Details* +

Alerts aren't generated for rules that have **Alert flapping detection** turned off and the alert delay set to a value higher than 1.

*Workaround* +
Set the alert delay value to 1 or turn on **Alert flapping detection**.

### Enhancements

Stack management::
* Adds IPv6 support to remote clusters address fields ({kibana-pull}233415[#233415]).

### Fixes

Dashboards and Visualizations::
* Fixes an issue with the Save modal that allowed duplicate saves of dashboards, visualizations, and other objects when clicking the **Save** button multiple times ({kibana-pull}233933[#233933]).
Elastic Security solution::
For the Elastic Security 8.19.4 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes an issue causing the API Keys Management page to break when trying to load API keys with null names ({kibana-pull}234083[#234083]).
Search solution::
* Fixes the Docs Explorer paging information to correctly render bold text instead of escaped HTML ({kibana-pull}234079[#234079]).
Observability solution::
* Fixes an issue in synthetics where multiple package policies are being created if user have monitors in multiple spaces ({kibana-pull}235021[#235021]).


## Kibana 8.19.3

The 8.19.3 release includes the following known issues and fixes.

### Known issues

**Alerts aren't generated for rules with alert flapping off and an alert delay higher than 1.**
*Details* +

Alerts aren't generated for rules that have **Alert flapping detection** turned off and the alert delay set to a value higher than 1.

*Workaround* +
Set the alert delay value to 1 or turn on **Alert flapping detection**.

### Fixes

Alerting::
* Fixes an issue that prevents reports from showing in the Reporting UI when they're created in a non-default Kibana space ({kibana-pull}230876[#230876]).
Canvas::
* Fixes a rendering issue that affected progress elements in Canvas ({kibana-pull}232432[#232432]).
Dashboards and Visualizations::
* Ensures passing of the `allowLeadingWildcards` advanced setting for ES|QL charts in Lens ({kibana-pull}232609[#232609]).
* Removes the list of `availableOptions` from the ES|QL `VALUES_FROM_QUERY` saved object ({kibana-pull}231690[#231690]).
* Fixes older color mapping configuration in Lens ({kibana-pull}231563[#231563]).
* Fixes lost references when returning to unsaved dashboards with reference panels ({kibana-pull}231517[#231517]).
* Fixes screen reader-only header in the Dashboards list ({kibana-pull}230470[#230470]).
Discover::
* Disables sorting for JSON-like fields in ES|QL mode ({kibana-pull}231289[#231289]).
Elastic Security solution::
For the Elastic Security 8.19.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Fixes an issue where the `unusedUrlsCLeanupTask` run interval did not update correctly when changed ({kibana-pull}231883[#231883]).


## Kibana 8.19.2

The 8.19.2 release includes the following known issues, enhancements, and fixes.

### Known issues

**Alerts aren't generated for rules with alert flapping off and an alert delay higher than 1.**
*Details* +

Alerts aren't generated for rules that have **Alert flapping detection** turned off and the alert delay set to a value higher than 1.

*Workaround* +
Set the alert delay value to 1 or turn on **Alert flapping detection**.

### Enhancements

Search::
* Bumps default Gemini model for the Gemini Connector in Playground from Gemini 1.5 Pro to Gemini 2.5 Pro ({kibana-pull}230457[#230457]).

### Fixes

Alerting::
* Fixes an issue that prevents reports from showing in the Reporting UI when they're created in a non-default Kibana space ({kibana-pull}230876[#230876]).
Dashboards and Visualizations::
* Fixes screen reader-only header in the Dashboards list ({kibana-pull}230470[#230470]).
Elastic Observability solution::
* Fixes an issue with `setupLockManagerIndex` where if the first call failed, all subsequent calls would fail as well ({kibana-pull}230519[#230519]).
* Adds loading state to the **Install** and **Uninstall** buttons for Elastic documentation on the AI Assistant **Settings** page ({kibana-pull}229579[#229579]).
