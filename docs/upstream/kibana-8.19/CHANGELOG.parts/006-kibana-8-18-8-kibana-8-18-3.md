<!-- Part 6 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.18.8

The 8.18.8 release includes the following fixes.

**Important:** This release contains fixes for potential security vulnerabilities. Check our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.

### Fixes

Dashboards and Visualizations::
* Fixes text kerning issues in PDF/PNG exports of dashboards and visualizations ({kibana-pull}235516[#235516]).
* Updates dashboards to wait until controls are ready before rendering panels to prevent a double fetch of data ({kibana-pull}237169[#237169]).
* Fixes an issue with the Lens table's column sort order being different in the dashboard and the exported CSV ({kibana-pull}236673[#236673]).
* Fixes an issue where the dashboard title would not get updated in the breadcrumb when edited from the list of dashboards ({kibana-pull}236561[#236561]).
Data ingestion and Fleet::
* Adds a unique count to improve accuracy of the number of transforms on the integrations overview page ({kibana-pull}236177[#236177]).
* Validates the Logstash pipeline ID at the Kibana API level ({kibana-pull}236347[#236347]).
Discover::
* Clears sort by `timestamp` when navigating from classic to ES|QL mode ({kibana-pull}235338[#235338]).
Elastic Observability solution::
* Removes span documents from the `getServiceAgent` function ({kibana-pull}236732[#236732]).
Elastic Security solution::
For the Elastic Security 8.18.8 release information, refer to [Elastic Security Solution Release Notes](docs-content://release-notes/elastic-security/index.md).
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


## Kibana 8.18.7

The 8.18.7 release includes the following fixes.

### Fixes

Elastic Security solution::
For the Elastic Security 8.18.7 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes an issue causing the API Keys Management page to break when trying to load API keys with null names ({kibana-pull}234083[#234083]).
Search solution::
* Fixes the Docs Explorer paging information to correctly render bold text instead of escaped HTML ({kibana-pull}234079[#234079]).


## Kibana 8.18.6

The 8.18.6 release includes the following fixes.

### Enhancements

Kibana security::
* Improves error messages when your Kibana session fails to refresh a token ({kibana-pull}231118[#231118]).
Machine Learning::
* Improves error handling in Anomaly Explorer when fetching table data fails and category definition fails ({kibana-pull}231779[#231779]).

### Fixes

Alerting::
* Fixes an issue where maintenance windows with scoped queries were not being correctly applied to all rule types ({kibana-pull}232307[#232307]).
Dashboards and Visualizations::
* Fixes empty **Create tag** tooltip in dashboard details ({kibana-pull}232853[#232853]).
Data ingestion and Fleet::
* Ensures transform index templates include `index.mapping.ignore_malformed: true` to prevent failures due to invalid values in source indices in Fleet ({kibana-pull}232439[#232439]).
Elastic Observability solution::
* Adds a note about supported Helm versions to the onboarding flow ({kibana-pull}232618[#232618]).
Elastic Security solution::
For the Elastic Security 8.18.6 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes positioning of the **Add rule** popover on the **Role Mappings** page ({kibana-pull}231551[#231551]).
* Removes the default port from the interactive setup cluster address form, unless specified ({kibana-pull}230582[#230582]).
Machine Learning::
* Updates the prompt text for the `mv_slice` feature ({kibana-pull}231870[#231870]).
* Ensures that failed validation does not alter other fields in the AI Connector form ({kibana-pull}230321[#230321]).
Management::
* Fixes an issue where the **Restore Status** tab was not showing results when only system indices were restored ({kibana-pull}232839[#232839]).


## Kibana 8.18.5

The 8.18.5 release includes the following fixes.

### Fixes

Dashboards and Visualizations::
* Fixes an issue with the plus sign `+` not being properly encoded when it's part of a date math expression ({kibana-pull}230469[#230469]).
* Fixes an issue in Firefox preventing you from scrolling in the Lens editor flyout ({kibana-pull}228625[#228625]).
* Fixes an issue preventing you from saving linked TSVB visualizations when changing data views ({kibana-pull}228685[#228685]).
* Fixes a console error occurring when adding a Region map visualization to a dashboard ({kibana-pull}228669[#228669]).
Data ingestion and Fleet::
* Fixes an issue that could cause some SSL configurations set using the UI to be overridden ({kibana-pull}230758[#230758]).
* Fixes an issue where the SSL configuration isn't properly added to agent policies with pre-configured output types ({kibana-pull}230211[#230211]).
* Fixes agentless integrations using 'organization', 'division', or 'team' data fields being overwritten by package agentless metadata on the agent policy ({kibana-pull}230479[#230479]).
Discover::
* Improves performance of breakdown field search ({kibana-pull}229335[#229335]).
* Enables the **Save query** button after making changes ({kibana-pull}229053[#229053]).
* Fixes the field being picked for fetching stats in the sidebar popover ({kibana-pull}228969[#228969]).
* Fixes an issue where some Discover **Copy to clipboard** actions only worked when accessing Kibana in a secure browser context ({kibana-pull}229531[#229531]).
Elastic Observability solution::
* Prevents from performing destructive actions using Elastic AI Assistant ({kibana-pull}229497[#229497]).
* Fixes an issue with column sorting in the **Services** Errors table ({kibana-pull}229199[#229199]).
* Fixes an issue with dependencies infinitely loading when no data exists ({kibana-pull}228094[#228094]).
* Fixes an error in Uptime occurring when filters are missing in the parameters of a rule created using the API ({kibana-pull}229422[#229422]).
Elastic Security solution::
For the Elastic Security 8.18.5 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Fixes an issue with overlapping action icons in the **Data views** menu when on mobile ({kibana-pull}229771[#229771]).
* Fixes a display issue with counter indicators on toast messages ({kibana-pull}229300[#229300]).
* Fixes an issue leading to some features not being visible when updating a space solution view to Classic ({kibana-pull}230385[#230385]).
Machine Learning::
* Removes `removeIfExists` from the synchronization task scheduler ({kibana-pull}228783[#228783]).


## Kibana 8.18.4

The 8.18.4 release includes the following known issues and fixes.

### Known issues

**Issues with rules occur when xpack.alerting.rules.run.alerts.max is set to a value greater than 5000.**
*Details* +

If you've set `xpack.alerting.rules.run.alerts.max` to a value greater than `5000`, you will encounter `Result window is too large` error messages when a maintenance window is active.

*Workaround* +
To mitigate the issue, set `xpack.alerting.rules.run.alerts.max` to a value equal to or less than `5000`.

### Fixes

Alerting::
* Fixes an issue causing reports to fail with an invalid header error ({kibana-pull}225919[#225919]).
Dashboards and Visualizations::
* Fixes an issue with dashboard sharing links where copied links were not shortened and some users were unable to copy links in new spaces ({kibana-pull}227625[#227625]).
Data ingestion and Fleet::
* Fixes an issue with agentless integration policies appearing under the Agent-based section ({kibana-pull}225767[#225767]).
* Fixes an issue where the background task was not deleting some unenrolled agents ({kibana-pull}224808[#224808]).
Discover::
* Prevents selected document from changing when resizing the **Document** flyout with a keyboard ({kibana-pull}225594[#225594]).
Elastic Observability solution::
* Fixes sparklines in the **Dependencies** table ({kibana-pull}227211[#227211]).
* Shows **Uptime Monitors** in the Observability solution view when enabled in Advanced Settings ({kibana-pull}226999[#226999]).
* Fixes response handling of the `get_apm_dependencies` tool call in the AI Assistant ({kibana-pull}226601[#226601]).
* Fixes the **Span details** flyout on the APM **Operations** page ({kibana-pull}226423[#226423]).
* Collapses query tool calls when using Claude ({kibana-pull}226078[#226078]).
* Fixes `Unable to load page` error on the APM **Operations** page ({kibana-pull}226036[#226036]).
* Fixes `Unable to load page` error on the APM Settings **Schema** page ({kibana-pull}225481[#225481]).
* Fixes `Unable to load page` error on the APM Settings **Agent Explorer** page ({kibana-pull}225071[#225071]).
* Fixes unexpected error on some panels of the EDOT JVM metrics dashboard ({kibana-pull}224052[#224052]).
Elastic Security solution::
For the Elastic Security 8.18.4 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Prevents navigation feedback popup from reappearing in each session ({kibana-pull}227199[#227199]).
* Hides the header and side navigation when printing or exporting a dashboard with **Print layout** selected ({kibana-pull}227095[#227095]).
Search::
* Fixes handling of context limit errors in Playground when using the Elastic Managed LLM ({kibana-pull}225360[#225360]).


## Kibana 8.18.3

The 8.18.3 release includes the following known issues and fixes.

**Important:** The 8.18.3 release contains fixes for potential security vulnerabilities. Check our [security advisory for more details](https://discuss.elastic.co/c/announcements/security-announcements/31).

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

**Dashboard Copy link doesn't work when sharing from a space other than the default space**
**This issue is resolved in versions 8.19.0, 8.18.4, and 8.17.9** ({kibana-pull}227625[#227625]).

*Details* +
When attempting to share a dashboard from a space that isn't the default space, the **Copy link** action never completes.

*Workaround* +
To avoid this issue, don't upgrade Kibana to one of the affected versions, or upgrade to a higher version that includes a fix for it.

**Observability AI assistant gets stuck in a loop when attempting to call the `execute_connector` function.**
*Details* +
The Observability AI assistant gets stuck in a loop when calling the `execute_connector` function. Instead of completing queries, it times out with the error message `Failed to parse function call arguments when converting messages for inference: SyntaxError: Unexpected non-whitespace character after JSON at position 72 and Error: Tool call arguments for execute_connector (...) were invalid`.

**Observability AI Assistant - Elastic Managed LLM may be automatically selected as default connector**
*Details* +
The Elastic Managed LLM may be automatically selected as your default connector because of existing connector selection logic.
This can occur if you had not previously specified a connector for any of the following reasons:

- You only had one connector available and it was always automatically picked for your conversations.
- You had multiple connectors available but didn’t make a specific selection and used the automatically picked connector for your conversations.
- You previously selected a connector but cleared your browser's local storage or switched browsers or devices.

_And:_

- All of your existing connector names come after the “Elastic Managed LLM connector" when sorted alphabetically.

For more information, check [#2088](https://github.com/elastic/docs-content/issues/2088)
**Issues with rules occur when xpack.alerting.rules.run.alerts.max is set to a value greater than 5000.**
*Details* +

If you've set `xpack.alerting.rules.run.alerts.max` to a value greater than `5000`, you will encounter `Result window is too large` error messages when a maintenance window is active.

*Workaround* +
To mitigate the issue, set `xpack.alerting.rules.run.alerts.max` to a value equal to or less than `5000`.

### Enhancements

Elastic Observability solution::
* Improves system prompt and instructions to work better with Claude models ({kibana-pull}221965[#221965]).

Elastic Security solution::
For the Elastic Security 8.18.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Kibana security::
* The **Invalidate user sessions** API is now generally available ({kibana-pull}224076[#224076]).

Machine Learning::
* Adds local file path support for `xpack.productDocBase.artifactRepositoryUrl` ({kibana-pull}217046[#217046]).

### Fixes

Alerting::
* Fixes an issue causing Kibana to keep restarting when the `cancelAlertsOnRuleTimeout` Kibana configuration setting was set to `false` ({kibana-pull}222263[#222263]).
* Resolves multiple issues in the Watcher UI that were introduced in 8.18.0 and 8.18.1. This includes the table not displaying more than 10 watches, an error banner appearing unexpectedly in certain scenarios, and the search bar functionality not working as expected ({kibana-pull}223898[#223898]).
* Fixes an issue causing the interface to freeze when an error occurred after deleting a connector ({kibana-pull}221958[#221958]).
* Fixes an issue that caused errors when rules ran during an active maintenance window that had filters and a matching rule category ({kibana-pull}221702[#221702]).

Dashboards and Visualizations::
* Fixes an issue that prevented navigating through pages when inspecting a chart's data ({kibana-pull}223537[#223537]).
* Fixes an issue preventing Canvas embeddables from correctly refreshing ({kibana-pull}221326[#221326]).

Data ingestion and Fleet::
* Fixes the `UnenrollInactiveAgentsTask` task to correctly only unenroll agents inactive for longer than the value defined by the `unenroll_timeout` setting ({kibana-pull}222592[#222592]).
* Fixes an issue that could prevent some integrations from correctly showing as installed ({kibana-pull}221624[#221624]).

Discover::
* In version 8.18.0, we changed the way time ranges are handled for Discover ES|QL CSV exports ({kibana-pull}216792[#216792]). We realized that this change caused an issue with CSV Post URLs now using an absolute time range instead of a relative one, leading to duplicate reports being generated. We've reverted this change while we investigate different solutions ({kibana-pull}223249[#223249]).

Elastic Observability solution::
* Fixes an issue causing the screenshot of the first step to appear for each step of the last successful test run in Synthetics ({kibana-pull}224220[#224220]).
* Fixes an issue that could cause losing unsaved changes after manually running a Synthetics test ({kibana-pull}222503[#222503]).
* Fixes an accessibility issue in Synthetics settings, causing the focus to move out of the page when using `cc` and `bcc` elements in the email connector form ({kibana-pull}223828[#223828]).
* Avoids adding tool instructions to the system messages when tools are disabled ({kibana-pull}223278[#223278]).
* Fixes a navigation issue where clicking the error count on an APM waterfall item triggers a full page reload ({kibana-pull}221664[#221664]).
* Fixes an issue preventing metrics graphs from correctly showing in the Services **Inventory** page ({kibana-pull}222439[#222439]).
* Fixes pagination not working on the Services **Inventory** page when progressive loading is enabled ({kibana-pull}220514[#220514]).

Elastic Security solution::
For the Elastic Security 8.18.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Machine Learning::
* Fixes an issue with the Bedrock connector not using the action proxy configuration ({kibana-pull}224130[#224130]).
* Fixes an issue with **Anomaly Explorer** where the selected overall swimlane bucket is not respected for `viewBy jobId` ({kibana-pull}222845[#222845]).
* File upload: Fixes adding additional field when a pipeline is blank ({kibana-pull}222775[#222775]).
* Fixes the inference endpoint assignment to the trained model object ({kibana-pull}222076[#222076]).
* File upload: Correctly restricts auto-deployment to Elastic models ({kibana-pull}221357[#221357]).
* Ensures the OpenAI connector respects the action proxy configuration for all sub-actions ({kibana-pull}219617[#219617]).

Installation and upgrade::
* Fixes an issue where `/etc/default/kibana` on Debian packages and `/etc/sysconfig/kibana` on RPM packages would be overwritten during upgrade ({kibana-pull}221276[#221276]).
