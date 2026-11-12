<!-- Part 11 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.17.0

coming::[8.17.0]

For information about the Kibana 8.17.0 release, review the following information.

The 8.17.0 release includes the following known issues.

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
**Observability AI assistant Knowledge Base entries with empty text can lead to Kibana OOM or restarts.**
*Details* +
The semantic text migration can cause excessive traffic to a cluster and might eventually cause the Kibana instance to crash due to OOM, together with increase of requests to Elasticsearch & ML nodes.

The problem can occur when there is one or more empty text Knowledge Base documents.

The migration script does not handle this scenario and will indefinitely update the same document.

Because the document update involves semantic_text an ML node is kept warm further increasing the costs.

The issue involves semantic_text field type (and thus the semantic_text migration which is causing this issue), introduced in the knowledge base feature in 8.17.

*Workaround* +

1. Pause the Kibana instance if possible. If not possible, skip this step.
2. Run a dry run query to identify if you have empty Knowledge Base documents. If you have at least 1 hit, you can be affected by the problem.
```sh
GET .kibana-observability-ai-assistant-kb/_search
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```
3. Execute the deletion. For extra safety, you might want to trigger a snapshot before executing it.
```sh
POST .kibana-observability-ai-assistant-kb/_delete_by_query
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```

For more information, check:

* [#220339](https://github.com/elastic/kibana/issues/220339)
* [#220342](https://github.com/elastic/kibana/issues/220342)

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

**Upgrade Assistant displays configured source mode in mappings as critical deprecation issue.**
*Details* +
When upgrading to a newer version, the Upgrade Assistant displays critical warnings for the deprecation of configuring source mode in mappings. These warnings can safely be ignored.

For more information, refer to [#206400](https://github.com/elastic/kibana/issues/206400).

### Deprecations

The following functionality is deprecated in 8.17.0, and will be removed in 9.0.0.
Deprecated functionality does not have an immediate impact on your application, but we strongly recommend
you make the necessary updates after you upgrade to 8.17.0.

**The Observability > Logs > Explorer app is now deprecated in favor of Discover.**
*Details* +
Both the Logs Explorer and Logs Stream applications are now deprecated and will be removed in 9.0. We continue to make enhancements to Discover to offer similar functionality in 9.x.

### Features

Kibana 8.17.0 adds the following new and notable features.

Cases::
* Files can now be attached to cases directly via API ({kibana-pull}198377[#198377]).
Data ingestion and Fleet::
* Exposes advanced file logging configuration in the UI ({kibana-pull}200274[#200274]).
Dashboards and visualizations::
* AIOps: Adds Log Rate Analysis embeddable for dashboards ({kibana-pull}197943[#197943]).
Discover and ES|QL::
* Keeps the preferred chart configuration when possible when writing ES|QL queries in Discover ({kibana-pull}197453[#197453]).
ES|QL::
* Adds the ability to star queries in the ES|QL editor ({kibana-pull}198362[#198362]).
Elastic Observability solution::
* Adds ability to show monitors from all permitted spaces in a single view in Synthetics ({kibana-pull}196109[#196109]).
* Adds fix it flow for field limit ({kibana-pull}195561[#195561]).
* Adds permissions to reopen and add comments to cases ({kibana-pull}194898[#194898]).
* Adds built-in definitions for core Kubernetes entities ({kibana-pull}196916[#196916]).
Elastic Security solution::
For the Elastic Security 8.17.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Kibana's FIPS mode is no longer considered experimental ({kibana-pull}200734[#200734]).
* When running in FIPS mode, Kibana now forbids usage of PKCS12 configuration options ({kibana-pull}192627[#192627]).

For more information about the features introduced in 8.17.0, refer to What's new in 8.17.

### Enhancements and bug fixes

For detailed information about the 8.17.0 release, review the enhancements and bug fixes.

### Enhancements

Alerting::
* Allows users to create rules with predefined nonrandom IDs ({kibana-pull}199119[#199119]).
Cases::
* The Jira Connector has been updated to use the latest API and support the Jira Data Center ({kibana-pull}197787[#197787]).
* The Case action is now GA ({kibana-pull}196972[#196972]).
Dashboards & Visualizations::
* Allows creating a dashboard with ES|QL chart even when there are no data views ({kibana-pull}196658[#196658]).
* Newly and default configured line charts are now interpolated by default with a straight linear interpolation in *Lens* ({kibana-pull}196184[#196184]).
* Simplifies access to some actions when hovering over panels ({kibana-pull}182535[#182535]).
* Improves URL drilldown authoring experience ({kibana-pull}197454[#197454]).
* The `metrics:allowCheckingForFailedShards` advanced setting has been removed. With this change, it is no longer possible to suppress warnings about failed shards in TSVB. For more information, refer to ({kibana-pull}197227[#197227]).
Data ingestion and Fleet::
* Filters integrations/packages list shown depending on the `policy_templates_behavior` field ({kibana-pull}200605[#200605]).
* Adds a `<type>@custom` component template to integrations index template's `composed_of` array ({kibana-pull}192731[#192731]).
Discover::
* Enables drag & drop for reordering columns in Discover ({kibana-pull}197832[#197832]).
ES|QL::
* Prevents suggestions with unsupported fields when writing ES|QL queries ({kibana-pull}200544[#200544]).
* Adds autocomplete and validation to support MATCH and QSRT when writing ES|QL queries ({kibana-pull}199032[#199032]).
Elastic Observability solution::
* Supports querying `semantic_text` fields in search connectors ({kibana-pull}200184[#200184]).
* Adds retry statements as an attempt to resolve flaky tests ({kibana-pull}200022[#200022]).
* Changes `host.hostname` to `host.name` in java metrics query ({kibana-pull}199208[#199208]).
* Improves analyzer by filtering unsuitable tokens ({kibana-pull}197868[#197868]).
* Uses `semantic_text` for internal knowledge base ({kibana-pull}186499[#186499]).
Elastic Security solution::
For the Elastic Security 8.17.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Introduces explicit configuration for routes that require superuser access and moves the `api/encrypted_saved_objects/_rotate_key` endpoint to the new configuration. ({kibana-pull}196586[#196586]).
* Enforces standard on API Actions definitions by separating operations and subjects ({kibana-pull}193140[#193140]).
Machine Learning::
* AIOps: Adds action for adding Log Rate analysis embeddable to a dashboard ({kibana-pull}200557[#200557]).
* AIOps: Adds action for adding Log Pattern embeddable to a dashboard and case ({kibana-pull}199478[#199478]).
* Single Metric Viewer embeddable: Adds action for dashboard to apply filter from the embeddable to the page ({kibana-pull}198869[#198869]).
* File upload: Adds deployment initialization step ({kibana-pull}198446[#198446]).
* Data visualizer: Changes refresh button in Data View and Data Drift view to indicate an update is pending ({kibana-pull}196537[#196537]).
* Anomaly Detection: Adds never expire option to forecast creation modal ({kibana-pull}195151[#195151]).
Kibana platform::
* When attempting to save an object with a name that already exists, the name is automatically appended with a suffix to make it unique ({kibana-pull}198777[#198777]).

### Bug fixes

Dashboards & Visualizations::
* Prevents identical include and exclude values in *Lens* ({kibana-pull}197628[#197628]).
* Fixes React Warning when rendering a recoverable error in *Lens* ({kibana-pull}196285[#196285]).
* Fixes an issue allowing to save a dashboard while there were no pending changes. The button is now disabled if there are no changes to save ({kibana-pull}196137[#196137]).
* Fixes an issue in Lens where the table exported did not match what was visible in the UI. ({kibana-pull}193780[#193780]).
Data ingestion and Fleet::
* Allows to create integration policy with no agent policies ({kibana-pull}201051[#201051]).
Discover::
* Addresses chart performance issues for non-transformational and non-time-based ES|QL queries ({kibana-pull}200583[#200583]).
ES|QL::
* Fixes an issue causing the the ES|QL editor to incorrectly use the light theme in some cases ({kibana-pull}200233[#200233]).
Elastic Observability solution::
* Fixes incorrect Y-axis and hover values in log rate chart on service overview ({kibana-pull}201361[#201361]).
* Observability AI Assistant: Fetch user instructions using the user ID instead of the username ({kibana-pull}200137[#200137]).
* Observability AI Assistant: Adds instructions about the slack connector to avoid executing a loop ({kibana-pull}199531[#199531]).
* Observability AI Assistant: Updates the term "chat" to "conversation" across the UI ({kibana-pull}199216[#199216]).
* Observability AI Assistant: Removes the "Copy" button if there is no content to copy ({kibana-pull}199064[#199064]).
* Observability AI Assistant: Adds uuid to knowledge base entries to avoid accidental overrides ({kibana-pull}191043[#191043]).
* Observability AI Assistant: Fixes error when opening an old conversation ({kibana-pull}197745[#197745]).
* Observability AI Assistant: Allows the input box to be resized off-screen ({kibana-pull}197063[#197063]).
* SLOs: Handle custom DSL query filters ({kibana-pull}198073[#198073]).
* Enables sub-feature permissions to edit Labs settings ({kibana-pull}197092[#197092]).
* Uses `telemetry.sdk` as a fallback for missing `agent.name` on non-tracing data ({kibana-pull}196529[#196529]).
* Adds support for simultaneous edits for private locations in Synthetics({kibana-pull}195874[#195874]).
Elastic Security solution::
For the Elastic Security 8.17.0 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Machine Learning::
* Adds query guardrails and technical preview badge to the ES|QL data visualizer ({kibana-pull}200325[#200325]).
* AIOps: fixes time range filter in change point charts ({kibana-pull}200183[#200183]).
* Anomaly detection: Adds spacer below split card charts in job wizard ({kibana-pull}199708[#199708]).
* Adds missing aria labels to button icons ({kibana-pull}199447[#199447]).
Kibana platform::
* Fixes an issue with the global search field that could open the wrong page when pressing "Enter" while results were not yet fully loaded ({kibana-pull}197750[#197750]).


## Kibana 8.16.6

The 8.16.6 release includes the following known issues, enhancements, and fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Enhancements

Elastic Observability Solution::
* Splits up the top dependencies API for improved speed and response size ({kibana-pull}211441[#211441]).

### Fixes

Alerting::
* Fixes a bug with ServiceNow where users could not create the connector from the UI form using OAuth ({kibana-pull}213658[#213658]).
Data ingestion and Fleet::
* Fixes an issue with the Agent binary download field being blank when a policy uses the default download source ({kibana-pull}214360[#214360]).
Elastic Observability Solution::
* Passes telemetry.sdk* data when loading a dashboard ({kibana-pull}214356[#214356]).
* Fixes missing summary data in error sample ({kibana-pull}213430[#213430]).
* Fixes service maps not building paths when the trace's root transaction has a `parent.id` ({kibana-pull}212998[#212998]).
* Fixes span links with OTel data ({kibana-pull}212806[#212806]).
Elastic Security solution::
For the Elastic Security 8.16.6 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes structured log flow to handle multiple types of structured logs ({kibana-pull}212611[#212611]).
Management::
* Fixes error when opening a rollup data view in Discover ({kibana-pull}214656[#214656]).


## Kibana 8.16.5

The 8.16.5 release includes the following known issues, enhancements, and bug fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Enhancements

Elastic Observability solution::
* Improve performance in `dependencies` endpoints to prevent high CPU usage ({kibana-pull}209999[#209999]).
Management::
* Increase search timeout toast lifetime to 1 week ({kibana-pull}210576[#210576]).

### Bug fixes

Alerting::
* Fixes error message in cases list if case assignee is an empty string ({kibana-pull}209973[#209973]).
* Provides a fallback view to recover from Stack Alerts page filters bar errors ({kibana-pull}209559[#209559]).
* Fixes an issue where the popover in the rules page may get stuck when being clicked more than once ({kibana-pull}208996[#208996]).
Dashboards and Visualizations::
* Fixes link settings not persisting ({kibana-pull}211041[#211041]).
* Fixes the Save to library action that could break the chart panel when triggered from a from a "by value" panel ({kibana-pull}210125[#210125]).
* Fixes an issue with dynamic coloring being disabled for Last value aggregation types in *Lens* ({kibana-pull}209110[#209110]).
Data ingestion and Fleet::
* Updates component templates with deprecated setting ({kibana-pull}210200[#210200]).
Discover::
* Fixes Discover session embeddable drilldown ({kibana-pull}211678[#211678]).
* Fixes "Untitled" export title when exporting CSV on a dashboard ({kibana-pull}210143[#210143]).
Elastic Observability solution::
* Missing items in the trace waterfall shouldn't break it entirely ({kibana-pull}210210[#210210]).
Kibana security::
* Fixes structured log flow to handle multiple types of structured logs ({kibana-pull}212611[#212611]).
Machine Learning::
* Fixes unattended Transforms in integration packages not automatically restarting after reauthorizing ({kibana-pull}210217[#210217]).


## Kibana 8.16.4

The 8.16.4 release includes the following known issues and bug fixes.

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
* Fixes an issue with all embeddables getting rebuilt on refresh ({kibana-pull}209677[#209677]).
* Sets options list control to fetch a maximum of 1,000 terms upon scrolling ({kibana-pull}207901[#207901]).
* Fixes scroll-jumping when interacting with the Lens editor flyout ({kibana-pull}207429[#207429]).
* Fixes an issue with Kibana Chrome appearing in generated reports ({kibana-pull}206988[#206988]).
* Fixes missing highlight theme for HJSON in *Vega* ({kibana-pull}208858[#208858]).
* Adds an accessible label to range slider in *Lens* ({kibana-pull}205308[#205308]).
Discover::
* Fixes document comparison table padding ({kibana-pull}205984[#205984]).
Osquery::
* Increases maximum Osquery timeout to 24 hours ({kibana-pull}207276[#207276]).
Elastic Observability solution::
* Displays `No Data` in Threshold breached component ({kibana-pull}209561[#209561]).
* Fixes the preview chart in the Custom threshold rule creation form when the field name has slashes ({kibana-pull}209263[#209263]).
* Fixes multiple AI assistant flyouts ({kibana-pull}209158[#209158]).
* Fixes using data view runtime fields during rule execution for the custom threshold rule ({kibana-pull}209133[#209133]).
* Fixes an issue with running processes missing from the processes table ({kibana-pull}209076[#209076]).
* Fixes heatmap regression when Inspect flag is turned off ({kibana-pull}208726[#208726]).
* Fixes missing exception stack trace ({kibana-pull}208577[#208577]).
* Fixes leading wildcard issue on the Custom threshold alert details page ({kibana-pull}206615[#206615]).
Elastic Security solution::
For the Elastic Security 8.16.4 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes breaks in YAML parsing by using single quotes in Structured log template ({kibana-pull}209736[#209736]).
* Adds missing fields to input manifest templates ({kibana-pull}208768[#208768]).
* Adds missing fields into AWS S3 manifest ({kibana-pull}208080[#208080]).
