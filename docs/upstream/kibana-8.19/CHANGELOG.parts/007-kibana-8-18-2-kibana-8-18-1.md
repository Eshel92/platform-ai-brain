<!-- Part 7 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.18.2

The 8.18.2 release includes the following known issues and fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

**Errors in rule executions occur when maintenance windows have filters.**
*Details* +
Errors occur when rules run during an active maintenance window that has filters and a matching rule category.

*Workaround* +
Remove any filters added to the active maintenance window.

*Resolved* +
This issue is resolved in 8.18.3.

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
**Upgrading Kibana from 8.x to 8.18.2 fails due to a configuration conflict in the kibana.yml file.**
**This issue is resolved in version 8.18.3** ({kibana-pull}222263[#222263]).

*Details* +
Upgrading Kibana from version 8.x to 8.18.2 fails due to a configuration conflict if `xpack.alerting.cancelAlertsOnRuleTimeout` is set to `false` in the `kibana.yml` file. Kibana fails to boot and shows a fatal error message in the Kibana logs that's similar to the following:

```sh
FATAL Error: Rule type "transform_health" cannot have both cancelAlertsOnRuleTimeout set to false and autoRecoverAlerts set to true.
```

This failure occurs when the `xpack.alerting.cancelAlertsOnRuleTimeout` setting is set to `false`, which is incompatible with the default configuration of an internal setting (`autoRecoverAlerts`) in 8.18.2.

*Workaround* +
To temporarily resolve the issue and allow the upgrade to proceed, follow these steps:

. Remove the `xpack.alerting.cancelAlertsOnRuleTimeout: false` setting from the `kibana.yml` file.
. Restart Kibana to apply the changes.

### Fixes

Dashboards and Visualizations::
* Fixes success message and auto-scroll behavior after adding a panel to a dashboard from the library ({kibana-pull}220122[#220122]).
* Allows ES|QL queries to suggest a chart even when there is no data returned from a query. ({kibana-pull}218085[#218085]).
Elastic Observability Solution::
* Updates SLO created in a previous version to handle `createdBy` and `updatedBy` fields in an ingest pipeline ({kibana-pull}221158[#221158]).
* Fixes errors in `error_marker.tsx` to support **Mobile Services** ({kibana-pull}220424[#220424]).
Elastic Security solution::
For the Elastic Security 8.18.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].


## Kibana 8.18.1

**Important:**
The 8.18.1 release contains fixes for potential security vulnerabilities. See our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.

The 8.18.1 release includes the following known issues, enhancements and fixes.

### Known issues

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

**Errors in rule executions occur when maintenance windows have filters.**
*Details* +
Errors occur when rules run during an active maintenance window that has filters and a matching rule category.

*Workaround* +
Remove any filters added to the active maintenance window.

*Resolved* +
This issue is resolved in 8.18.3.

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

### Enhancements

Elastic Security solution::
For the Elastic Security 8.18.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

### Fixes

Dashboards and Visualizations::
* Syncs the dashboard ES|QL query and filters with the corresponding visualization query in *Lens* ({kibana-pull}218997[#218997]).
* Correctly formats keywords in metric visualizations ({kibana-pull}218233[#218233]).
* When exploring a dashboard, the request inspector now shows the correct request and response in any successful scenario ({kibana-pull}216519[#216519]).
Discover::
* Fixes incorrect behavior for requests on fields where the *Allow hidden and system indices* (`allow_hidden`) option of the data view could be ignored ({kibana-pull}217628[#217628]).
* Fixes the result of the *Generate CSV report* action for ES|QL panels ({kibana-pull}216325[#216325]).
Elastic Observability Solution::
* Prevents unnecessary suggestion requests when interacting with inputs on the APM *Custom Links* page ({kibana-pull}218927[#218927]).
* Filters out null values from `sourceDataStreams` ({kibana-pull}218772[#218772]).
* Fixes a bug with navigating to the *Search Connectors* tab in the AI Assistant Settings ({kibana-pull}217749[#217749]).
* Improves `aria-label` attributes for correlations ({kibana-pull}217512[#217512]).
Elastic Security solution::
For the Elastic Security 8.18.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana platform::
* Fixes broken icons in integrations coming from the Home plugin ({kibana-pull}219206[#219206]).
Kibana security::
* Removes check for unused connector role ({kibana-pull}219358[#219358]).
Machine Learning::
* Fixes error when switching Service providers in the *Inference Endpoint* flyout ({kibana-pull}219020[#219020]).
* Corrects quotes in ES|QL queries for function arguments ({kibana-pull}217680[#217680]).
